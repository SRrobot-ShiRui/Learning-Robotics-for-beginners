#!/usr/bin/env python3
"""第 16 篇配套：卡尔曼滤波的几何解释（纯 numpy/matplotlib）。

四个可复现实验：
  1) 两个高斯相乘 = 信息融合，后验比任何一个都更「窄」
  2) 二维匀速模型：预测步把协方差椭圆拉长旋转，更新步收缩
  3) EKF 一阶线性化在强非线性 / 大噪声下偏离蒙特卡洛真值
  4) 全状态直接平均角度会在 ±π 处失效，误差状态在切空间上不会

运行：python3 kalman_geometry.py --plot
"""
import argparse
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "dejavusans"

OUT = Path(__file__).resolve().parents[1] / "figs"


def gaussian(x, mu, var):
    return np.exp(-0.5 * (x - mu) ** 2 / var) / np.sqrt(2 * np.pi * var)


def exp1_gaussian_product():
    """实验 1：先验 N(mu1,P1) 与观测 N(mu2,P2) 相乘。"""
    mu1, P1 = 0.0, 4.0
    mu2, P2 = 3.0, 1.0
    K = P1 / (P1 + P2)
    P_post = P1 * P2 / (P1 + P2)
    mu_post = mu1 + K * (mu2 - mu1)

    # 数值验证：把两个高斯密度相乘再归一化，用网格积分求均值与方差
    x = np.linspace(-8, 10, 400001)
    prod = gaussian(x, mu1, P1) * gaussian(x, mu2, P2)
    w = prod / np.trapezoid(prod, x)
    mu_grid = np.trapezoid(x * w, x)
    var_grid = np.trapezoid((x - mu_grid) ** 2 * w, x)

    print("=== 实验 1：高斯相乘 = 信息融合 ===")
    print(f"先验 N({mu1:.3f}, {P1:.3f})，观测 N({mu2:.3f}, {P2:.3f})")
    print(f"卡尔曼增益 K            = {K:.6f}")
    print(f"后验方差 P (解析)       = {P_post:.6f}  (< min(P1,P2) = {min(P1,P2):.3f})")
    print(f"后验均值 mu (解析)      = {mu_post:.6f}")
    print(f"网格积分 mu / var       = {mu_grid:.6f} / {var_grid:.6f}")
    print(f"解析 vs 网格 误差       = {abs(mu_post-mu_grid):.2e} / {abs(P_post-var_grid):.2e}")
    print(f"信息量（1/P）相加       = 1/{P1:.0f} + 1/{P2:.0f} = {1/P1+1/P2:.4f} = 1/{P_post:.4f}")
    return (mu1, P1, mu2, P2, mu_post, P_post, K)


def exp2_ellipse(dt=1.0, q=0.02, R=0.5, n_steps=25):
    """实验 2：二维匀速模型的协方差椭圆演化 + Riccati 递推稳态。"""
    F = np.array([[1.0, dt], [0.0, 1.0]])
    Q = q * np.array([[dt**3 / 3, dt**2 / 2], [dt**2 / 2, dt]])
    H = np.array([[1.0, 0.0]])
    P = np.eye(2) * 2.0

    P_pred = F @ P @ F.T + Q
    S = H @ P_pred @ H.T + R
    K_vec = (P_pred @ H.T / S).ravel()
    P_upd = (np.eye(2) - np.outer(K_vec, H.ravel())) @ P_pred

    det0, det_pred, det_upd = np.linalg.det(P), np.linalg.det(P_pred), np.linalg.det(P_upd)

    # Riccati 递推到稳态，看 K 收敛
    Ps, Ks = P.copy(), []
    for _ in range(n_steps):
        Pp = F @ Ps @ F.T + Q
        Ss = float((H @ Pp @ H.T + R)[0, 0])
        kv = (Pp @ H.T / Ss).ravel()
        Ps = (np.eye(2) - np.outer(kv, H.ravel())) @ Pp
        Ks.append(kv[0])

    print("\n=== 实验 2：协方差椭圆与增益收敛 ===")
    print(f"det(P) 初始 / 预测后 / 更新后 = {det0:.6f} / {det_pred:.6f} / {det_upd:.6f}")
    print(f"更新把不确定面积压到预测的   = {det_upd/det_pred*100:.2f}%")
    print(f"首步 K(位置) = {K_vec[0]:.6f}，K(速度) = {K_vec[1]:.6f}")
    print(f"Riccati 递推 {n_steps} 步：K(位置) {Ks[0]:.6f} -> {Ks[-1]:.6f}（稳态）")
    print(f"稳态 P 对角  = {Ps[0,0]:.6f}, {Ps[1,1]:.6f}")
    return (F, Q, H, R, P, P_pred, P_upd, Ks)


def exp3_ekf_linearization(sigmas=(0.05, 0.2, 0.5, 1.0, 2.0), n_mc=200000, seed=0):
    """实验 3：非线性观测 h(x)=sqrt(x^2+y^2)，EKF 用一阶线性化 vs 蒙特卡洛真值。"""
    rng = np.random.default_rng(seed)
    truth = np.array([3.0, 0.0])
    rows = []
    for s in sigmas:
        samples = truth + rng.normal(0, s, size=(n_mc, 2))
        r = np.linalg.norm(samples, axis=1)
        mc_mean, mc_var = r.mean(), r.var()
        # EKF：在均值处线性化，h(mu)=||mu||，Jacobian = mu/||mu||
        h_mu = np.linalg.norm(truth)
        J = truth / h_mu
        ekf_mean = h_mu
        ekf_var = float(J @ (s**2 * np.eye(2)) @ J)
        rows.append((s, mc_mean, ekf_mean, abs(mc_mean - ekf_mean), mc_var, ekf_var))

    print("\n=== 实验 3：EKF 一阶线性化的偏差（h = 距离） ===")
    print(f"{'sigma':>7}{'MC 真均值':>13}{'EKF 均值':>11}{'均值偏差':>12}{'MC 方差':>12}{'EKF 方差':>12}")
    for s, m, e, d, mv, ev in rows:
        print(f"{s:>7.2f}{m:>13.5f}{e:>11.5f}{d:>12.5f}{mv:>12.5f}{ev:>12.5f}")
    print(f"sigma=2.0 时均值偏差 {rows[-1][3]:.5f}，是 sigma=0.05 时 {rows[0][3]:.2e} 的 "
          f"{rows[-1][3]/max(rows[0][3],1e-12):.0f} 倍")
    return rows


def exp4_error_state():
    """实验 4：角度平均的 wrap 陷阱 —— 为什么姿态要用误差状态。"""
    deg = np.pi / 180
    a1, a2 = 179 * deg, -179 * deg
    naive = 0.5 * (a1 + a2)                      # 全状态直接平均
    # 误差状态：以 a1 为标称，把 a2 的差 wrap 到 (-pi, pi]，在切空间求增量
    delta = (a2 - a1 + np.pi) % (2 * np.pi) - np.pi
    es_mean = a1 + 0.5 * delta
    es_deg = (es_mean / deg + 180) % 360 - 180
    true_mean = 180 * deg
    err_naive = abs((naive - true_mean + np.pi) % (2 * np.pi) - np.pi) / deg
    err_es = abs((es_mean - true_mean + np.pi) % (2 * np.pi) - np.pi) / deg

    # 姿态四元数/旋转矩阵上「均值不封闭」的补充：旋转 180° 附近的两个Rotation
    print("\n=== 实验 4：全状态平均 vs 误差状态平均（角度 wrap） ===")
    print(f"两个角度                 = +179° 与 -179°（真均值应为 ±180°）")
    print(f"全状态直接平均           = {naive/deg:.3f}°，与真值差 {err_naive:.3f}°（指反了方向）")
    print(f"误差状态切空间平均       = {es_deg:.3f}°，与真值差 {err_es:.3f}°")
    print(f"切空间增量 delta         = {delta/deg:.3f}°（wrap 到 (-180°, 180°]）")
    return (naive, es_mean, err_naive, err_es, delta)


def ellipse_points(P, mu, n=240, scale=1.0):
    vals, vecs = np.linalg.eigh(P)
    t = np.linspace(0, 2 * np.pi, n)
    circ = np.vstack([np.cos(t), np.sin(t)])
    pts = vecs @ (np.sqrt(vals)[:, None] * circ) * scale
    return mu[0] + pts[0], mu[1] + pts[1]


def make_plots(e1, e2, e3, e4):
    OUT.mkdir(parents=True, exist_ok=True)
    mu1, P1, mu2, P2, mu_post, P_post, K = e1
    F, Q, H, R, P, P_pred, P_upd, Ks = e2

    # ---- fig16-01：高斯乘积 + 协方差椭圆 ----
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))
    ax = axes[0]
    x = np.linspace(-7, 9, 1200)
    ax.plot(x, gaussian(x, mu1, P1), lw=2, color="#2563eb", label=f"先验 $N({mu1:g},{P1:g})$")
    ax.plot(x, gaussian(x, mu2, P2), lw=2, color="#16a34a", label=f"观测 $N({mu2:g},{P2:g})$")
    ax.plot(x, gaussian(x, mu_post, P_post), lw=2.6, color="#dc2626",
            label=f"后验 $N({mu_post:.2f},{P_post:.2f})$")
    ax.fill_between(x, 0, gaussian(x, mu_post, P_post), color="#dc2626", alpha=0.12)
    ax.set_xlabel("位置 $x$")
    ax.set_ylabel("概率密度")
    ax.set_title("两个高斯相乘：后验比两者都窄")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    ax = axes[1]
    mu = np.array([0.0, 0.0])
    for Pp, c, lab, ls in [(P, "#94a3b8", "初始 $P$", "--"),
                           (P_pred, "#2563eb", "预测后（拉长/旋转）", "-"),
                           (P_upd, "#dc2626", "更新后（收缩）", "-")]:
        ex, ey = ellipse_points(Pp, mu, scale=2.0)
        ax.plot(ex, ey, lw=2.2, color=c, ls=ls, label=lab)
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_xlabel("位置 $p$")
    ax.set_ylabel("速度 $v$")
    ax.set_title("预测把椭圆拉斜，观测把它压窄")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    fig.suptitle("卡尔曼滤波的几何：信息融合与协方差演化", fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "fig16-01-gaussian-fusion.png", dpi=150)
    plt.close(fig)

    # ---- fig16-02：EKF 线性化偏差 + 增益收敛 ----
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))
    ax = axes[0]
    ss = [r[0] for r in e3]
    ax.plot(ss, [r[3] for r in e3], "o-", lw=2.2, color="#dc2626", label="均值偏差 $|E[h]-h(\\mu)|$")
    ax.plot(ss, [abs(r[4] - r[5]) for r in e3], "s--", lw=2, color="#2563eb", label="方差偏差 $|V_{MC}-V_{EKF}|$")
    ax.set_xlabel("先验标准差 $\\sigma$")
    ax.set_ylabel("偏差")
    ax.set_yscale("log")
    ax.set_title("噪声越大，一阶线性化越不准")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3, which="both")

    ax = axes[1]
    ax.plot(range(1, len(Ks) + 1), Ks, "o-", lw=2.2, color="#ea580c")
    ax.set_xlabel("Riccati 递推步数")
    ax.set_ylabel("卡尔曼增益 $K_p$")
    ax.set_title(f"增益收敛到稳态 {Ks[-1]:.4f}（与初值无关）")
    ax.grid(alpha=0.3)
    fig.suptitle("线性化误差与增益的稳态", fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "fig16-02-ekf-bias-and-gain.png", dpi=150)
    plt.close(fig)

    # ---- fig16-03：角度 wrap 示意 ----
    fig, ax = plt.subplots(figsize=(7.2, 5.4), subplot_kw={"projection": "polar"})
    deg = np.pi / 180
    ax.scatter([179 * deg, -179 * deg], [1, 1], s=110, c="#2563eb", zorder=5, label="两个观测角度")
    ax.scatter([e4[0]], [1], s=170, marker="x", linewidths=3, c="#dc2626", zorder=6,
               label=f"全状态平均 {e4[0]/deg:.0f}°（错）")
    ax.scatter([e4[1] % (2 * np.pi)], [1], s=120, marker="*", c="#16a34a", zorder=6,
               label="误差状态平均 180°（对）")
    ax.set_ylim(0, 1.25)
    ax.set_title("角度不是向量：全状态平均会指反方向", pad=18, fontsize=13, fontweight="bold")
    ax.legend(loc="lower left", bbox_to_anchor=(-0.15, -0.12), fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "fig16-03-error-state.png", dpi=150)
    plt.close(fig)

    print("\n=== 配图已生成 ===")
    for p in sorted(OUT.glob("fig16-*.png")):
        print(" ", p.name, f"{p.stat().st_size/1024:.1f} KB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true", help="生成配图")
    args = ap.parse_args()
    e1 = exp1_gaussian_product()
    e2 = exp2_ellipse()
    e3 = exp3_ekf_linearization()
    e4 = exp4_error_state()
    if args.plot:
        make_plots(e1, e2, e3, e4)


if __name__ == "__main__":
    main()
