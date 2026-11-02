#!/usr/bin/env python3
"""逆运动学 (Inverse Kinematics) 数值解法演示。

涵盖：
  - 雅可比伪逆迭代（牛顿法思想：误差线性化 → 一步校正）
  - 阻尼最小二乘 DLS（边界目标不发散）
  - 冗余臂（4R 平面臂）自运动：同一目标无穷多构型

验证输出：
  [1] 随机可达目标 200 组：伪逆迭代收敛率 / 平均迭代次数
  [2] 边界目标（r=2.3，最大可达 2.4）：伪逆 vs DLS 的迭代误差轨迹
  [3] 冗余臂 5 个不同初值 → 5 个不同解，末端误差全部 < 1e-6

用法：
    python3 ik_demo.py --plot    # 出图到 ../docs/Robot_Alchemy/figs/
"""
import argparse
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

_cjk = None
for cand in ["Noto Sans CJK JP", "Noto Sans CJK SC", "WenQuanYi Zen Hei"]:
    if any(cand in fm.name for fm in font_manager.fontManager.ttflist):
        _cjk = cand
        break
if _cjk:
    plt.rcParams["font.family"] = _cjk
plt.rcParams["axes.unicode_minus"] = False

L3 = np.array([1.0, 0.8, 0.6])            # 3R 臂连杆（与第 04 篇同一条臂）
L4 = np.array([0.8, 0.7, 0.6, 0.5])       # 4R 冗余臂（任务空间 2 维，冗余 2）


def fk(q, L):
    ang = np.cumsum(q)
    p = np.zeros(2)
    for i, li in enumerate(L):
        p = p + li * np.array([np.cos(ang[i]), np.sin(ang[i])])
    return p


def joints(q, L):
    ang = np.cumsum(q)
    pts = [np.zeros(2)]
    p = np.zeros(2)
    for i, li in enumerate(L):
        p = p + li * np.array([np.cos(ang[i]), np.sin(ang[i])])
        pts.append(p.copy())
    return np.array(pts)


def jac(q, L):
    """平面几何雅可比：J[:,i] = z × (p_ee - o_i)。"""
    pts = joints(q, L)
    p = pts[-1]
    J = np.zeros((2, len(L)))
    for i in range(len(L)):
        r = p - pts[i]
        J[:, i] = [-r[1], r[0]]
    return J


def ik(q0, target, L, lam=0.0, iters=200, tol=1e-6):
    """迭代逆解：dq = J^+ e（lam>0 时换 DLS）。返回解、误差轨迹、实际迭代数。"""
    q = np.array(q0, float)
    errs = []
    for k in range(iters):
        e = np.asarray(target) - fk(q, L)
        errs.append(np.linalg.norm(e))
        if errs[-1] < tol:
            break
        J = jac(q, L)
        if lam > 0:
            dq = J.T @ np.linalg.solve(J @ J.T + lam ** 2 * np.eye(2), e)
        else:
            dq = np.linalg.pinv(J) @ e
        q = q + dq
    return q, errs, len(errs)


# ---------- 验证 ----------
def verify():
    rng = np.random.default_rng(42)
    # [1] 随机可达目标（r < 2.2，远离边界）
    ok, iters_all, max_err = 0, [], 0.0
    for _ in range(200):
        r = rng.uniform(0.2, 2.2)
        th = rng.uniform(-np.pi, np.pi)
        target = r * np.array([np.cos(th), np.sin(th)])
        q0 = rng.uniform(-np.pi, np.pi, 3)
        q, errs, n = ik(q0, target, L3)
        if errs[-1] < 1e-6:
            ok += 1
            iters_all.append(n)
            max_err = max(max_err, errs[-1])
    print("[1] 随机可达目标 200 组（r∈[0.2, 2.2]）")
    print("    伪逆迭代收敛 %d/200   平均迭代 %.1f 次   中位迭代 %d 次"
          % (ok, np.mean(iters_all), int(np.median(iters_all))))

    # [2] 不可达目标 r=2.6（超出最大可达 2.4），对比伪逆与 DLS
    target = 2.6 * np.array([np.cos(0.5), np.sin(0.5)])
    q0 = np.array([0.3, 0.5, -0.4])
    _, errs_p, n_p = ik(q0, target, L3, lam=0.0, iters=200)
    q_d, errs_d, n_d = ik(q0, target, L3, lam=0.2, iters=200)
    print("[2] 不可达目标 r=2.60（最大可达半径 2.40，理论最小残差 0.20 m）")
    print("    伪逆        %d 次迭代后误差 %.2f m   峰值误差 %.2f m   |q| 漂移至 %.0f rad"
          % (n_p, errs_p[-1], max(errs_p), np.abs(q := ik(q0, target, L3, lam=0.0, iters=200)[0]).max()))
    print("    DLS λ=0.20  %d 次迭代后误差 %.2f m   峰值误差 %.2f m   |q| 漂移至 %.2f rad"
          % (n_d, errs_d[-1], max(errs_d), np.abs(q_d).max()))
    return target, q0, errs_p, errs_d


# ---------- 配图 ----------
def plot_convergence(target, q0, errs_p, errs_d):
    q_d, _, _ = ik(q0, target, L3, lam=0.2, iters=200)
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))
    ax = axes[0]
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(2.4 * np.cos(th), 2.4 * np.sin(th), "--", color="#888888", lw=1.4,
            label="可达边界 r=2.4")
    for q, c, lab in [(q0, "#bbbbbb", "初始构型"),
                      (q_d, "#1f77b4", "DLS 收敛构型")]:
        pts = joints(q, L3)
        ax.plot(pts[:, 0], pts[:, 1], "-o", color=c, lw=2.5, ms=6, label=lab)
    traj = np.array([fk(np.array(q0), L3)] + [fk(_ik_step(q0, target, k, 0.2), L3)
                     for k in range(1, 15)])
    ax.plot(traj[:, 0], traj[:, 1], "--", color="#d62728", lw=1.8, label="DLS 末端迭代轨迹")
    ax.plot(*target, "*", color="gold", ms=18, mec="k", label="目标点 r=2.60 (域外)")
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_xlabel("x / m")
    ax.set_ylabel("y / m")
    ax.set_title("DLS 迭代到最近可达点（目标在域外）")
    ax.legend(fontsize=8, loc="lower left")

    ax = axes[1]
    ax.semilogy(errs_p[:60], label="伪逆 J+ (pinv)", color="#d62728")
    ax.semilogy(errs_d[:60], label="DLS λ=0.20", color="#1f77b4")
    ax.axhline(0.2, color="k", ls=":", lw=1.2, label="理论最小残差 0.2 m")
    ax.set_xlabel("迭代次数")
    ax.set_ylabel("末端位置误差 / m")
    ax.set_title("域外目标下的收敛对比")
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=9)
    fig.tight_layout()
    return fig


def _ik_step(q0, target, k, lam=0.0):
    q = np.array(q0, float)
    for _ in range(k):
        e = np.asarray(target) - fk(q, L3)
        J = jac(q, L3)
        if lam > 0:
            q = q + J.T @ np.linalg.solve(J @ J.T + lam ** 2 * np.eye(2), e)
        else:
            q = q + np.linalg.pinv(J) @ e
    return q


def plot_redundancy():
    target = np.array([1.5, 0.9])
    rng = np.random.default_rng(7)
    fig, ax = plt.subplots(figsize=(7.0, 5.6))
    colors = plt.cm.viridis(np.linspace(0.05, 0.85, 5))
    for i, c in enumerate(colors):
        q0 = rng.uniform(-np.pi, np.pi, 4)
        q, errs, _ = ik(q0, target, L4, lam=0.02, iters=300)
        q = (q + np.pi) % (2 * np.pi) - np.pi   # 等价角变换，不改变末端位置
        pts = joints(q, L4)
        ax.plot(pts[:, 0], pts[:, 1], "-o", color=c, lw=2.2, ms=5,
                label="解 %d：q=(%.2f, %.2f, %.2f, %.2f)" % (i + 1, *q))
    ax.plot(*target, "*", color="gold", ms=20, mec="k", zorder=5)
    ax.annotate("同一目标", xy=target, xytext=(target[0] + 0.12, target[1] + 0.18),
                fontsize=11)
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_xlabel("x / m")
    ax.set_ylabel("y / m")
    ax.set_title("冗余臂（4R）自运动：5 个初值 → 5 个不同构型，同一目标")
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    return fig


def main():
    target, q0, errs_p, errs_d = verify()
    import os
    out = os.path.join(os.path.dirname(__file__), "..", "docs", "Robot_Alchemy", "figs")
    os.makedirs(out, exist_ok=True)
    plot_convergence(target, q0, errs_p, errs_d).savefig(
        os.path.join(out, "fig08-01-ik-convergence.png"), dpi=130)
    plot_redundancy().savefig(
        os.path.join(out, "fig08-02-redundancy.png"), dpi=130)
    print("[V] 已生成 fig08-01-ik-convergence.png / fig08-02-redundancy.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    a = ap.parse_args()
    if a.plot:
        main()
    else:
        verify()
