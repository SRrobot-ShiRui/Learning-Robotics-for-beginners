"""rnea_demo.py —— 平面 2R 机械臂的递归牛顿-欧拉算法（RNEA）演示。

运行：
    python3 rnea_demo.py            # 数值验证（打印 5 组结果）
    python3 rnea_demo.py --plot     # 额外生成 docs/Robot_Alchemy/figs/fig10-*.png

依赖：numpy / matplotlib（无第三方机器人库）。
本文所有数字都可由本脚本复现，文章与图取自同一次运行。

物理模型：
    两根均质细杆，长度 l1/l2，质量 m1/m2，绕质心转动惯量 I_i = m_i*l_i^2/12。
    关节角 q = [q1, q2] 为相对转角，重力沿 -y（g = 9.81 m/s^2）。
    广义坐标下：   tau = M(q)*qdd + c(q,qd) + g(q)
    RNEA 用 O(n) 递推直接算出 tau，不显式组装 M / c / g。
"""
import sys
import numpy as np

# ---------------------------------------------------------------- 常量
L1, L2 = 1.0, 0.8          # 连杆长度 / m
M1, M2 = 2.0, 1.5          # 连杆质量 / kg
I1 = M1 * L1 ** 2 / 12     # 绕质心转动惯量 / kg·m^2
I2 = M2 * L2 ** 2 / 12
G = 9.81                    # 重力加速度 / m/s^2

# 便于拉格朗日解析式的中间量
_a = I1 + I2 + M1 * L1 ** 2 / 4 + M2 * (L1 ** 2 + L2 ** 2 / 4)
_b = M2 * L1 * L2 / 2
_c = I2 + M2 * L2 ** 2 / 4


def cross2(u, v):
    """二维叉积的 z 分量：u_x*v_y - u_y*v_x。"""
    return u[0] * v[1] - u[1] * v[0]


def rot_z(theta):
    """绕 z 轴旋转 theta 的 2x2 矩阵。"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


# ---------------------------------------------------------------- 解析式（交叉验证用）
def lagrange_terms(q, qd):
    """返回 M(2x2)、科氏/离心向量 c(2)、重力向量 g(2)。

    由 T = 1/2*M11*qd1^2 + M12*qd1*qd2 + 1/2*M22*qd2^2 与
    V = m1*g*y_c1 + m2*g*y_c2 经拉格朗日方程推导，独立于 RNEA。
    """
    c2, s2 = np.cos(q[1]), np.sin(q[1])
    M = np.array([
        [_a + 2 * _b * c2, _c + _b * c2],
        [_c + _b * c2,     _c],
    ])
    cc = np.array([
        -_b * s2 * (2 * qd[0] * qd[1] + qd[1] ** 2),
        _b * s2 * qd[0] ** 2,
    ])
    c1, c12 = np.cos(q[0]), np.cos(q[0] + q[1])
    gg = np.array([
        G * (M1 * L1 / 2 * c1 + M2 * (L1 * c1 + L2 / 2 * c12)),
        G * (M2 * L2 / 2 * c12),
    ])
    return M, cc, gg


def tau_lagrange(q, qd, qdd):
    M, cc, gg = lagrange_terms(q, qd)
    return M @ qdd + cc + gg


# ---------------------------------------------------------------- RNEA 主体
def rnea(q, qd, qdd, with_gravity=True):
    """递归牛顿-欧拉：O(n) 计算关节力矩 tau = [tau1, tau2]。

    前向递推（基座 -> 末端）：传播角速度、角加速度、质心线加速度。
      技巧：把重力等效为基座加速度 a_0 = -g = (0, +G)，
            这样 a_c 自动含重力，后向递推无需另加重力项。
    后向递推（末端 -> 基座）：累加力 f 与力矩 n，投影到关节轴取 z 分量。
    """
    q = np.asarray(q, float)
    qd = np.asarray(qd, float)
    qdd = np.asarray(qdd, float)

    # --- 几何：各关节原点 O_i 与各连杆质心 c_i 的位置 ---
    p_O = [np.zeros(2)]                                   # O_1 = 基座原点
    p_O.append(L1 * np.array([np.cos(q[0]), np.sin(q[0])]))   # O_2 = 关节 2
    p_c = [L1 / 2 * np.array([np.cos(q[0]), np.sin(q[0])])]   # 连杆 1 质心
    p_c.append(p_O[1] + L2 / 2 * np.array(
        [np.cos(q[0] + q[1]), np.sin(q[0] + q[1])]))     # 连杆 2 质心

    # --- 前向：运动学量传播（平面平行轴，角速度/角加速度为标量 z 分量）---
    w = [qd[0], qd[0] + qd[1]]          # omega_i = sum_{k<=i} qd_k
    al = [qdd[0], qdd[0] + qdd[1]]      # alpha_i = sum_{k<=i} qdd_k
    a_O0 = np.array([0.0, G]) if with_gravity else np.zeros(2)   # 重力等效基座加速度
    # 关节 2 的线加速度：a_O2 = a_O1 + alpha_1 x r - omega_1^2 r
    r_O1O2 = p_O[1] - p_O[0]
    a_O1 = a_O0
    a_O2 = a_O1 + al[0] * np.array([-r_O1O2[1], r_O1O2[0]]) - w[0] ** 2 * r_O1O2
    a_O = [a_O1, a_O2]
    a_c = []
    for i in range(2):
        r = p_c[i] - p_O[i]
        a_c.append(a_O[i] + al[i] * np.array([-r[1], r[0]]) - w[i] ** 2 * r)

    # --- 后向：力/力矩累加 ---
    mass = [M1, M2]
    inertia = [I1, I2]
    f_next = np.zeros(2)     # f_{n+1} = 0（末端无外力）
    n_next = 0.0             # n_{n+1} = 0
    tau = np.zeros(2)
    for i in (1, 0):         # 从末端连杆 i=2 回到 i=1
        mi_aci = mass[i] * a_c[i]
        f_i = f_next + mi_aci
        # n_i = n_{i+1} + I_i*alpha_i + (c_i - O_i) x m_i*a_ci + (O_{i+1} - O_i) x f_{i+1}
        lever_next = (p_O[i + 1] - p_O[i]) if i + 1 < len(p_O) else np.zeros(2)
        n_i = (n_next + inertia[i] * al[i]
               + cross2(p_c[i] - p_O[i], mi_aci)
               + cross2(lever_next, f_next))
        tau[i] = n_i         # 旋转轴为 z，直接取 z 分量
        f_next, n_next = f_i, n_i
    return tau


def mass_matrix_from_rnea(q):
    """用同一份 RNEA 提取质量矩阵：第 j 列 = rnea(qdd=e_j, qd=0) - rnea(qdd=0, qd=0)。

    这是工程师常用的技巧：不必另写 CRBA，改输入即可让递推吐出 M 的列。
    """
    tau0 = rnea(q, [0, 0], [0, 0])
    return np.column_stack([
        rnea(q, [0, 0], [1, 0]) - tau0,
        rnea(q, [0, 0], [0, 1]) - tau0,
    ])


def total_energy(q, qd):
    """T + V，用于功率平衡验证：tau·qd 应等于 dE/dt。"""
    M, _, _ = lagrange_terms(q, qd)
    T = 0.5 * qd @ M @ qd
    y_c1 = L1 / 2 * np.sin(q[0])
    y_c2 = L1 * np.sin(q[0]) + L2 / 2 * np.sin(q[0] + q[1])
    V = M1 * G * y_c1 + M2 * G * y_c2
    return T + V


# ---------------------------------------------------------------- 数值验证
def verify():
    rng = np.random.default_rng(20261109)
    print("[1] RNEA vs 拉格朗日解析式（随机 2000 组 q/qd/qdd）")
    worst = 0.0
    for _ in range(2000):
        q = rng.uniform(-np.pi, np.pi, 2)
        qd = rng.uniform(-4, 4, 2)
        qdd = rng.uniform(-8, 8, 2)
        e = np.abs(rnea(q, qd, qdd) - tau_lagrange(q, qd, qdd)).max()
        worst = max(worst, e)
    print("    最大绝对误差 = %.3e N·m" % worst)

    print("[2] 由 RNEA 提取 M(q)，与解析 M 对比 + 对称正定性")
    q = np.array([0.6, -0.9])
    Mr = mass_matrix_from_rnea(q)
    Ml, _, _ = lagrange_terms(q, qd=[0, 0])
    eig = np.linalg.eigvalsh(Mr)
    print("    |Mr - Ml| = %.3e ；对称性 %.3e ；特征值 = (%.4f, %.4f) 均为正"
          % (np.abs(Mr - Ml).max(), np.abs(Mr - Mr.T).max(), eig[0], eig[1]))

    print("[3] 静止悬停：qd=qdd=0 时 RNEA 应只输出重力力矩")
    tau = rnea(q, [0, 0], [0, 0])
    _, _, gg = lagrange_terms(q, [0, 0])
    print("    RNEA = (%.4f, %.4f) N·m ；解析重力项 = (%.4f, %.4f) N·m"
          % (tau[0], tau[1], gg[0], gg[1]))

    print("[4] 功率平衡：tau·qd 与 dE/dt（数值微分）")
    qd = np.array([0.8, -0.5])
    qdd = np.array([0.3, 0.7])
    tau = rnea(q, qd, qdd)
    dt = 1e-6
    dE = (total_energy(q + qd * dt + 0.5 * qdd * dt ** 2, qd + qdd * dt)
          - total_energy(q - qd * dt + 0.5 * qdd * dt ** 2, qd - qdd * dt)) / (2 * dt)
    print("    tau·qd = %.6f W ；dE/dt = %.6f W ；相对误差 %.2e"
          % (tau @ qd, dE, abs(tau @ qd - dE) / max(1.0, abs(dE))))

    print("[5] 递推复杂度：n 连杆的理论 O(n) 与显式组装 M 的 O(n^2) 对照")
    print("    本例 n=2：RNEA 递推 2 次前向 + 2 次后向；组装 M 需 n(n+1)/2 次调用")
    return q


# ---------------------------------------------------------------- 配图
def _setup_font():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    for cand in ["Noto Sans CJK JP", "Noto Sans CJK SC", "WenQuanYi Zen Hei"]:
        if any(cand in fm.name for fm in font_manager.fontManager.ttflist):
            plt.rcParams["font.family"] = cand
            break
    plt.rcParams["axes.unicode_minus"] = False
    return plt


def plot_recursion(plt):
    """图 1：RNEA 两阶段递推示意 + 一个具体工况的力矩分解。"""
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.0))

    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 7.2); ax.axis("off")

    def box(x, y, w, h, text, fc, ec, fs=9.5, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                    fc=fc, ec=ec, lw=1.5))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fs, fontweight="bold" if bold else "normal")

    def arrow(x1, y1, x2, y2, color, style="-|>", lw=1.7):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                     mutation_scale=15, color=color, lw=lw))

    ax.text(5.0, 6.75, "RNEA：一次前向、一次后向，O(n) 算出全部关节力矩",
            ha="center", fontsize=11, fontweight="bold")
    box(0.3, 4.9, 4.2, 1.25,
        "① 前向递推（基座 → 末端）\n传播角速度 / 角加速度 / 质心加速度\n输入：q、qd、qdd",
        "#dbeafe", "#1d4ed8", fs=9, bold=True)
    box(5.5, 4.9, 4.2, 1.25,
        "② 后向递推（末端 → 基座）\n累加惯性力与力矩，投影到关节轴\n输出：tau1、tau2 …",
        "#dcfce7", "#15803d", fs=9, bold=True)
    arrow(4.55, 5.52, 5.45, 5.52, "#1d4ed8")
    arrow(5.45, 5.05, 4.55, 5.05, "#15803d", style="-|>")

    rows = [
        (r"$a_0=(0,+g)$", "把重力等效成基座加速度，后向递推不用再单独加 G(q)"),
        (r"$\omega_i=\omega_{i-1}+\dot q_i$", "平面平行轴，角速度直接累加（标量）"),
        (r"$a_{c_i}=a_{O_i}+\alpha_i\times r-\omega_i^2 r$", "切向 + 向心两项，齐次变换的加速度版"),
        (r"$f_i=f_{i+1}+m_i a_{c_i}$", "子树惯性力逐层往回累加"),
        (r"$n_i=n_{i+1}+I_i\alpha_i+r\times f$", "力矩累加；旋转轴取 z 分量即关节力矩"),
    ]
    y = 3.95
    for k, (lhs, rhs) in enumerate(rows):
        box(0.3, y, 9.4, 0.62, "", "#f8fafc" if k % 2 == 0 else "#f1f5f9", "#94a3b8")
        ax.text(0.6, y + 0.31, lhs, fontsize=9.3, va="center", color="#0f172a",
                fontweight="bold")
        ax.text(4.4, y + 0.31, rhs, fontsize=9.0, va="center")
        y -= 0.72
    ax.set_title("两阶段递推的五条核心式子", fontsize=10)

    # 右图：一个具体工况下 τ 的三项分解
    ax = axes[1]
    q = np.array([0.6, -0.9]); qd = np.array([0.8, -0.5]); qdd = np.array([0.3, 0.7])
    M, cc, gg = lagrange_terms(q, qd)
    inertia = M @ qdd
    labels = [r"$\tau_1$ (肩)", r"$\tau_2$ (肘)"]
    x = np.arange(2); w = 0.55
    p1 = ax.bar(x, inertia, w, label=r"惯性项 $M(q)\ddot q$", color="#3b82f6")
    p2 = ax.bar(x, cc, w, bottom=inertia, label=r"科氏/离心 $c(q,\dot q)$", color="#f59e0b")
    p3 = ax.bar(x, gg, w, bottom=inertia + cc, label="重力项 g(q)", color="#ef4444")
    ax.axhline(0, color="#334155", lw=1)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel("关节力矩 / N·m")
    ax.set_title("工况 q=(0.6, −0.9) 的力矩分解\n重力项占比 %.0f%% / %.0f%%"
                 % (100 * abs(gg[0]) / (abs(inertia[0]) + abs(cc[0]) + abs(gg[0])),
                    100 * abs(gg[1]) / (abs(inertia[1]) + abs(cc[1]) + abs(gg[1]))))
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    for bars in (p1, p2, p3):
        for b in bars:
            h = b.get_height()
            if abs(h) > 0.4:
                ax.text(b.get_x() + b.get_width() / 2,
                        b.get_y() + h + (0.25 if h > 0 else -0.55),
                        "%.1f" % h, ha="center", fontsize=8.5)
    fig.tight_layout()
    return fig


def plot_consistency(plt):
    """图 2：RNEA 与拉格朗日解析式的一致性（含有限差分提取 M 的误差）。"""
    rng = np.random.default_rng(7)
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.6))

    ax = axes[0]
    errs = []
    for _ in range(500):
        q = rng.uniform(-np.pi, np.pi, 2)
        qd = rng.uniform(-4, 4, 2)
        qdd = rng.uniform(-8, 8, 2)
        errs.append(np.abs(rnea(q, qd, qdd) - tau_lagrange(q, qd, qdd)).max())
    ax.semilogy(errs, ".", ms=3, color="#1d4ed8", alpha=0.65)
    ax.axhline(np.max(errs), color="#dc2626", ls="--", lw=1.3,
               label="最大 %.1e N·m" % np.max(errs))
    ax.set_xlabel("随机工况编号（500 组）")
    ax.set_ylabel("|力矩差| / N·m")
    ax.set_title("两套独立实现的力矩完全一致")
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=9)

    ax = axes[1]
    q2s = np.linspace(-np.pi, np.pi, 120)
    cond, lam_min = [], []
    for q2 in q2s:
        M = mass_matrix_from_rnea([0.3, q2])
        e = np.linalg.eigvalsh(M)
        cond.append(e[1] / e[0]); lam_min.append(e[0])
    ax.plot(q2s, cond, color="#7c3aed", lw=2, label=r"条件数 $\kappa(M)$")
    ax.set_xlabel(r"肘关节角 $q_2$ / rad")
    ax.set_ylabel(r"条件数 $\kappa(M)$", color="#7c3aed")
    ax.tick_params(axis="y", labelcolor="#7c3aed")
    ax.grid(alpha=0.3)
    ax2 = ax.twinx()
    ax2.plot(q2s, lam_min, color="#059669", lw=2, ls="--", label="最小特征值")
    ax2.set_ylabel(r"最小特征值 / $\mathrm{kg\,m^2}$", color="#059669")
    ax2.tick_params(axis="y", labelcolor="#059669")
    ax.set_title("质量矩阵随构型变化，但始终正定\n（控制增益要按 M(q) 调度）")
    lines = ax.get_lines() + ax2.get_lines()
    ax.legend(lines, [l.get_label() for l in lines], fontsize=9, loc="upper center")
    fig.tight_layout()
    return fig


def plot_trajectory(plt):
    """图 3：一条搬运轨迹上的力矩曲线，展示重力项如何主导。"""
    T, N = 2.0, 240
    t = np.linspace(0, T, N)
    # 平滑起停轨迹：q1 从 -0.6 摆到 0.9，q2 从 1.2 收到 0.2
    s = 10 * (t / T) ** 3 - 15 * (t / T) ** 4 + 6 * (t / T) ** 5
    ds = (30 * (t / T) ** 2 - 60 * (t / T) ** 3 + 30 * (t / T) ** 4) / T
    dds = (60 * (t / T) - 180 * (t / T) ** 2 + 120 * (t / T) ** 3) / T ** 2
    q = np.vstack([-0.6 + 1.5 * s, 1.2 - 1.0 * s]).T
    qd = np.vstack([1.5 * ds, -1.0 * ds]).T
    qdd = np.vstack([1.5 * dds, -1.0 * dds]).T

    tau_inertia, tau_c, tau_g, tau_total = [], [], [], []
    for k in range(N):
        M, cc, gg = lagrange_terms(q[k], qd[k])
        tau_inertia.append(M @ qdd[k]); tau_c.append(cc); tau_g.append(gg)
        tau_total.append(rnea(q[k], qd[k], qdd[k]))

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))
    ax = axes[0]
    ax.plot(t, np.array(tau_total)[:, 0], color="#0f172a", lw=2.4, label=r"$\tau_1$ 总力矩 (RNEA)")
    ax.plot(t, np.array(tau_g)[:, 0], color="#ef4444", lw=1.8, ls="--", label=r"$\tau_1$ 重力项")
    ax.plot(t, np.array(tau_inertia)[:, 0], color="#3b82f6", lw=1.6, label=r"$\tau_1$ 惯性项")
    ax.fill_between(t, 0, np.array(tau_g)[:, 0], color="#ef4444", alpha=0.10)
    ax.set_xlabel("时间 / s"); ax.set_ylabel("力矩 / N·m")
    ax.set_title("肩关节：2 秒搬运轨迹上的力矩构成")
    ax.grid(alpha=0.3); ax.legend(fontsize=9)

    ax = axes[1]
    inertia_mag = np.abs(np.array(tau_inertia)).sum(axis=1)
    c_mag = np.abs(np.array(tau_c)).sum(axis=1)
    g_mag = np.abs(np.array(tau_g)).sum(axis=1)
    # 分母用「各项幅度之和」而非总力矩：总力矩里惯性项可能与重力项抵消，
    # 用它会算出 >100% 的假占比。
    ratio = g_mag / np.maximum(inertia_mag + c_mag + g_mag, 1e-9)
    ax.plot(t, ratio * 100, color="#b45309", lw=2.2)
    ax.axhline(50, color="#64748b", ls=":", lw=1.2, label="50% 参考线")
    ax.set_xlabel("时间 / s"); ax.set_ylabel("重力项占 |τ| 的比例 / %")
    ax.set_ylim(0, 105)
    ax.set_title("全程重力力矩占比（均值 %.0f%%）\n→ 重力补偿是最划算的一项"
                 % np.mean(ratio * 100))
    ax.grid(alpha=0.3); ax.legend(fontsize=9)
    fig.tight_layout()
    return fig


def main():
    q = verify()
    if "--plot" in sys.argv:
        plt = _setup_font()
        outdir = "../docs/Robot_Alchemy/figs/"
        figs = [
            ("fig10-01-rnea-recursion.png", plot_recursion(plt)),
            ("fig10-02-consistency.png", plot_consistency(plt)),
            ("fig10-03-torque-trajectory.png", plot_trajectory(plt)),
        ]
        for name, fig in figs:
            fig.savefig(outdir + name, dpi=130, bbox_inches="tight")
            plt.close(fig)
            print("  saved", name)
    print("done. q =", np.round(q, 3))


if __name__ == "__main__":
    main()
