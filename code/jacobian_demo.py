"""机器人炼金术 04 期配套代码：雅可比、可操作度、奇异性与阻尼最小二乘。

运行:
    python3 jacobian_demo.py            # 跑全部数值验证
    python3 jacobian_demo.py --plot     # 同时生成 4 张配图到 ../figs/
依赖: numpy, matplotlib
"""
import os
import numpy as np

L = [1.0, 0.8, 0.6]  # 三段连杆长度 (m)


# ---------- 正运动学与几何雅可比（平面 3R） ----------
def fk(q):
    """返回 (关节位置 3x2, 末端位置, 末端绝对朝向角)"""
    a1 = q[0]
    a2 = a1 + q[1]
    a3 = a2 + q[2]
    d1 = L[0] * np.array([np.cos(a1), np.sin(a1)])
    d2 = L[1] * np.array([np.cos(a2), np.sin(a2)])
    d3 = L[2] * np.array([np.cos(a3), np.sin(a3)])
    j1 = np.zeros(2)
    j2 = j1 + d1
    j3 = j2 + d2
    p = j3 + d3
    joints = np.vstack([j1, j2, j3])
    return joints, p, a3


def jacobian_analytic(q):
    """几何雅可比: 第 i 列 = z_i × (p - p_i)，平面臂 z 全部朝外"""
    joints, p, _ = fk(q)
    J = np.zeros((3, 3))
    for i in range(3):
        r = p - joints[i]
        J[0, i] = -r[1]
        J[1, i] = r[0]
        J[2, i] = 1.0
    return J


def jacobian_numeric(q, h=1e-6):
    """SE(3) 差分数值雅可比（本体侧），用于对照验证"""
    J = np.zeros((3, 3))
    for i in range(3):
        dq = q.copy()
        dq[i] += h
        _, p1, t1 = fk(dq)
        dq[i] -= 2 * h
        _, p0, t0 = fk(dq)
        J[:2, i] = (p1 - p0) / (2 * h)
        J[2, i] = (t1 - t0) / (2 * h)
    return J


def manipulability(J):
    """可操作度 w = σ1·σ2·σ3 = sqrt(det(J J^T))"""
    return np.sqrt(max(np.linalg.det(J @ J.T), 0.0))


def dls_step(J, v, lam):
    """阻尼最小二乘逆解 q̇ = Jᵀ(JJᵀ + λ²I)⁻¹ v"""
    return J.T @ np.linalg.solve(J @ J.T + lam**2 * np.eye(3), v)


# ---------- 数值验证 ----------
def verify():
    rng = np.random.default_rng(42)
    print("[1] 解析雅可比 vs 数值雅可比（200 组随机构型）")
    err = np.zeros((200, 3, 3))
    for k in range(200):
        q = rng.uniform(-np.pi, np.pi, 3)
        err[k] = jacobian_analytic(q) - jacobian_numeric(q)
    print(f"    空间侧最大偏差 {np.abs(err[:2]).max():.2e}   "
          f"本体侧最大偏差 {np.abs(err[2]).max():.2e}")

    print("[2] J(全伸直) =")
    J = jacobian_analytic([0, 0, 0])
    print(J)

    print("[3] 可操作度扫描")
    for q in ([0.5, 0.7, -0.4], [0.05, 0.03, 0.02], [0, 0, 0]):
        Jq = jacobian_analytic(q)
        s = np.linalg.svd(Jq, compute_uv=False)
        print(f"    q={q}  σ={np.round(s, 3)}  κ={s[0]/s[-1]:.1f}  w={manipulability(Jq):.3f}")

    print("[4] 伪逆 vs DLS：末端沿直线逼近近边界点")
    for lam in (0.0, 0.02, 0.10):
        q = np.array([0.4, 0.4, 0.4])
        target_dir = np.array([0.5, 0.0, 0.0])
        peaks, err = [], []
        for step in range(400):
            _, p, _ = fk(q)
            v_des = target_dir
            Jq = jacobian_analytic(q)
            qd = dls_step(Jq, v_des, lam) if lam else np.linalg.pinv(Jq) @ v_des
            q = q + 0.01 * qd
            _, p2, _ = fk(q)
            err.append(np.linalg.norm(p[:2] + v_des[:2] * 0.02 - p2) * 1000)
            peaks.append(np.linalg.norm(qd))
        print(f"    {'伪逆' if lam == 0 else 'DLS'} λ={lam:<5}|q̇|峰值 = {max(peaks):8.3f} rad/s   "
              f"末端误差 = {max(err):7.2f} mm")


# ---------- 配图 ----------
def make_plots():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK JP", "Noto Serif CJK JP", "sans-serif"]
    plt.rcParams["axes.unicode_minus"] = False
    out = os.path.join(os.path.dirname(__file__), "..", "docs", "Robot_Alchemy", "figs")
    os.makedirs(out, exist_ok=True)
    C_ARM, C_ELL, C_END = "#c0392b", "#2980b9", "#f39c12"

    # ---- 图1：两种构型的速度椭球 ----
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
    for ax, q, title in (
        (axes[0], [0.948, 0.942, 1.147], "弯曲构型（远离奇异）"),
        (axes[1], [0.220, 0.219, 0.266], "接近伸直（临近奇异）"),
    ):
        J = jacobian_analytic(q)
        joints, p, _ = fk(q)
        th = np.linspace(0, 2 * np.pi, 200)
        circle = np.vstack([np.cos(th), np.sin(th)])
        vel = J[:2] @ np.vstack([circle, np.zeros_like(th)])
        s = np.linalg.svd(J[:2], compute_uv=False)
        ax.plot(vel[0], vel[1], color=C_ELL, lw=2, label="速度可操作度椭球")
        ax.plot(*np.vstack([joints, p]).T, "-o", color=C_ARM, lw=2.5,
                ms=6, label="机械臂")
        ax.plot(*p, "*", color=C_END, ms=17, label="末端")
        ax.set_title(f"{title}\n奇异值 σ=({s[0]:.2f}, {s[1]:.2f})，κ={s[0]/s[1]:.1f}",
                     fontsize=11)
        ax.set_xlabel("x (m)"); ax.set_ylabel("y (m)")
        ax.set_aspect("equal"); ax.legend(fontsize=8); ax.grid(alpha=0.3)
    fig.suptitle("图1 同一目标点附近，两种构型的末端速度能力差异", fontsize=13)
    fig.savefig(os.path.join(out, "fig04-01-arm-ellipsoid.png"), dpi=150)
    plt.close(fig)

    # ---- 图2：逼近边界，可操作度跌向 0 ----
    q = np.array([0.9, 0.7, 0.6])
    direction = np.array([1.0, -0.10, 0.0])
    ts, ws, errs = [], [], []
    for k in range(80):
        J = jacobian_analytic(q)
        v = direction * 0.15
        qd = np.linalg.pinv(J) @ v
        _, p, _ = fk(q)
        q = q + 0.05 * qd
        _, p2, _ = fk(q)
        ts.append(0.05 * k)
        ws.append(manipulability(jacobian_analytic(q)))
        errs.append(np.linalg.norm(v[:2] * 0.05 - (p2 - p)[:2]) * 1000)
    fig, ax1 = plt.subplots(figsize=(8.5, 4.2), constrained_layout=True)
    ax1.plot(ts, ws, color="#1e8449", lw=2.5, label="可操作度 w = σ1·σ2·σ3")
    ax2 = ax1.twinx()
    ax2.plot(ts, errs, color="#c0392b", lw=2.5, label="末端跟踪误差")
    ax1.set_xlabel("时间 (s)"); ax1.set_ylabel("可操作度 w", color="#1e8449")
    ax2.set_ylabel("末端跟踪误差 (mm)", color="#c0392b")
    ax1.set_title("图2 逼近工作空间边界：可操作度跌向 0，末端开始跟不上指令", fontsize=12)
    fig.legend(loc="upper left", bbox_to_anchor=(0.12, 0.92), fontsize=9)
    fig.savefig(os.path.join(out, "fig04-02-conditioning.png"), dpi=150)
    plt.close(fig)

    # ---- 图3：伪逆 vs DLS ----
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
    for lam, color, label in ((0.0, "#c0392b", "伪逆 (λ=0)"),
                              (0.02, "#2471a3", "DLS (λ=0.02)"),
                              (0.10, "#1e8449", "DLS (λ=0.10)")):
        q = np.array([0.4, 0.4, 0.4])
        speed, err = [], []
        for step in range(45):
            J = jacobian_analytic(q)
            v = np.array([0.5, 0.0, 0.0])
            qd = dls_step(J, v, lam) if lam else np.linalg.pinv(J) @ v
            _, p, _ = fk(q)
            q = q + 0.01 * qd
            _, p2, _ = fk(q)
            speed.append(np.linalg.norm(qd))
            err.append(np.linalg.norm(v[:2] * 0.01 - (p2 - p)[:2]) * 1000)
        a1.plot(speed, color=color, lw=2, label=label)
        a2.plot(err, color=color, lw=2, label=label)
    a1.set_yscale("log"); a1.set_xlabel("轨迹步数")
    a1.set_title("关节速度范数 |q̇|（伪逆在奇异区爆炸）", fontsize=11)
    a2.set_xlabel("轨迹步数")
    a2.set_title("末端跟踪误差（阻尼越大，误差越大）", fontsize=11)
    a1.legend(fontsize=8); a2.legend(fontsize=8)
    a1.grid(alpha=0.3, which="both"); a2.grid(alpha=0.3)
    fig.suptitle("图3 阻尼最小二乘：用一点精度，换关节速度的确定性", fontsize=13)
    fig.savefig(os.path.join(out, "fig04-03-dls-vs-pinv.png"), dpi=150)
    plt.close(fig)

    # ---- 图4：万向锁条件数发散 ----
    pitch = np.linspace(0, 89.5, 300)
    kappa = 1.0 / np.cos(np.radians(pitch))
    fig, ax = plt.subplots(figsize=(8.5, 4.2), constrained_layout=True)
    ax.semilogy(pitch, kappa, color="#8e44ad", lw=2.5)
    ax.set_xlabel("俯仰角 θ (°)")
    ax.set_ylabel("欧拉角速率雅可比条件数 κ(E)")
    ax.set_title("图4 无人机姿态：俯仰趋近 90° 时，欧拉角速率换算矩阵条件数发散", fontsize=12)
    ax.annotate("万向锁：θ→90°，κ→∞\n此处偏航与滚转退化成同一个自由度",
                xy=(88, 15), xytext=(48, 80), fontsize=9, color="#c0392b",
                arrowprops=dict(arrowstyle="->", color="#c0392b"))
    ax.grid(alpha=0.3, which="both")
    fig.savefig(os.path.join(out, "fig04-04-gimbal-lock.png"), dpi=150)
    plt.close(fig)
    print("4 张配图已生成到 docs/Robot_Alchemy/figs/")


if __name__ == "__main__":
    import sys
    verify()
    if "--plot" in sys.argv:
        make_plots()
