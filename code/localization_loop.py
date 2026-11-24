#!/usr/bin/env python3
"""第 18 篇配套：为什么扫地机器人「知道自己在哪」（纯 numpy/matplotlib）。

两个可复现实验：
  1) 轮式里程计开环航迹推算：小比例误差 + 小角偏差，误差随路程累积
  2) 加「看到地标就重定位」的闭环（简化 EKF 位置融合）：误差被压到有界

关键设计：闭环与开环的**预测步完全同源**（同样的 0.8% 比例误差、
同样的 0.0015 rad/s 陀螺零偏），唯一差别是闭环每 obs_every 步有一次
带噪声的绝对位置观测（视觉重定位 / 看到充电桩 / 匹配上地图）。
因此两组误差的差别只能来自「有没有观测回流」。

对照第 15 篇的 IMU 二次积分漂移，为第 19 篇因子图 / VIO 埋钩子。

运行：python3 localization_loop.py --plot
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

S_SCALE = 1.008       # 里程计比例误差 +0.8%
GYRO_BIAS = 0.0015    # 陀螺零偏 rad/s
POS_NOISE = 0.02      # 重定位观测噪声 (m, 1 sigma)，视觉地标/二维码量级
OBS_EVERY = 50        # 每 50 步（5 s，约 5 m）看到一次地标


def turn_rate(k, n, dt=0.1):
    """前 1/3 直行，中间 1/3 匀速转 90°，后 1/3 直行。返回角速度 rad/s。"""
    if k < n // 3:
        return 0.0
    if k < 2 * n // 3:
        return (np.pi / 2) / ((n // 3) * dt)
    return 0.0


def truth_trajectory(n=400, dt=0.1, v=1.0):
    xs, ys, th = [0.0], [0.0], 0.0
    for k in range(n):
        th = th + turn_rate(k, n, dt) * dt
        xs.append(xs[-1] + v * dt * np.cos(th))
        ys.append(ys[-1] + v * dt * np.sin(th))
    return np.array(xs), np.array(ys)


def odometry_open_loop(n, dt=0.1, v=1.0):
    """开环：只用带误差的里程计积分，无任何外部观测。"""
    ox, oy, th = [0.0], [0.0], 0.0
    for k in range(n):
        th = th + (turn_rate(k, n, dt) + GYRO_BIAS) * dt
        step = v * dt * S_SCALE
        ox.append(ox[-1] + step * np.cos(th))
        oy.append(oy[-1] + step * np.sin(th))
    return np.array(ox), np.array(oy)


def relocalization_ekf(xs, ys, n, dt=0.1, v=1.0, seed=3):
    """闭环：同样的预测步 + 周期性绝对位置观测（H = I 的 EKF 融合）。"""
    rng = np.random.default_rng(seed)
    X = np.array([0.0, 0.0])
    P = np.eye(2) * 1e-4      # 起点已知，不确定性很小
    Q = np.eye(2) * 2e-5      # 预测过程噪声（每步约 4.5 mm）
    R = np.eye(2) * POS_NOISE ** 2

    cx, cy, th = [0.0], [0.0], 0.0
    errs = [0.0]
    corrections = {}
    for k in range(n):
        # --- 预测：与开环完全同源的带误差里程计增量 ---
        th = th + (turn_rate(k, n, dt) + GYRO_BIAS) * dt
        step = v * dt * S_SCALE
        X = X + np.array([step * np.cos(th), step * np.sin(th)])
        P = P + Q

        # --- 观测：看到地标 => 得到一次带噪声的绝对位置 ---
        if (k + 1) % OBS_EVERY == 0:
            z = np.array([xs[k + 1], ys[k + 1]]) + rng.normal(0, POS_NOISE, 2)
            S = P + R                      # H = I
            K = P @ np.linalg.inv(S)
            before = float(np.linalg.norm(X - np.array([xs[k + 1], ys[k + 1]])))
            X = X + K @ (z - X)
            P = (np.eye(2) - K) @ P
            after = float(np.linalg.norm(X - np.array([xs[k + 1], ys[k + 1]])))
            corrections[k + 1] = (before, after)

        cx.append(X[0])
        cy.append(X[1])
        errs.append(float(np.linalg.norm(X - np.array([xs[k + 1], ys[k + 1]]))))
    return np.array(cx), np.array(cy), np.array(errs), corrections


def run():
    n, dt, v = 400, 0.1, 1.0
    xs, ys = truth_trajectory(n, dt, v)
    ox, oy = odometry_open_loop(n, dt, v)
    cx, cy, errs, corrections = relocalization_ekf(xs, ys, n, dt, v)

    open_err = np.linalg.norm(np.column_stack([ox - xs, oy - ys]), axis=1)
    total_len = n * dt * v

    print("=== 实验 1：开环里程计（纯积分，无观测回流） ===")
    print(f"总路程                 = {total_len:.2f} m")
    print(f"里程计比例误差         = +0.8%，陀螺零偏 = 0.0015 rad/s")
    print(f"末端位置误差           = {open_err[-1]:.4f} m")
    print(f"误差 / 路程            = {open_err[-1]/total_len*100:.2f}%")
    print(f"中点误差 / 末端误差    = {open_err[len(open_err)//2]:.4f} / {open_err[-1]:.4f}")
    print(f"误差单调增长           = {bool(np.all(np.diff(open_err) > -1e-9))}")

    print(f"\n=== 实验 2：每 {OBS_EVERY} 步（{OBS_EVERY*dt:.1f} s）重定位一次 ===")
    print(f"观测                   = 绝对位置，噪声 1σ = {POS_NOISE:.2f} m")
    print(f"末端位置误差           = {errs[-1]:.4f} m（开环 {open_err[-1]:.4f} m）")
    print(f"末端抑制倍数           = {open_err[-1]/max(errs[-1],1e-9):.1f} 倍")
    print(f"全程误差均值 / 最大值  = {np.mean(errs):.4f} / {np.max(errs):.4f} m")
    print(f"开环全程误差均值       = {np.mean(open_err):.4f} m")
    first_k = min(corrections)
    b, a = corrections[first_k]
    print(f"首次修正（第 {first_k} 步）: {b:.4f} -> {a:.4f} m，单次拉回 {b-a:.4f} m")
    ks = sorted(corrections)
    print(f"共 {len(ks)} 次修正，平均每次拉回 "
          f"{np.mean([corrections[k][0]-corrections[k][1] for k in ks]):.4f} m")
    print(f"修正后误差 > 修正前的次数 = "
          f"{sum(1 for k in ks if corrections[k][1] > corrections[k][0])} / {len(ks)}")
    return (xs, ys, ox, oy, cx, cy, open_err, errs, corrections)


def make_plots(res):
    OUT.mkdir(parents=True, exist_ok=True)
    xs, ys, ox, oy, cx, cy, open_err, errs, corrections = res
    lms = np.array([[8.0, 10.0], [29.0, 3.0]])

    # ---- fig18-01：轨迹对比 ----
    fig, ax = plt.subplots(figsize=(7.8, 6.0))
    ax.plot(xs, ys, lw=3, color="#111827", label="真实轨迹")
    ax.plot(ox, oy, lw=2, color="#dc2626", ls="--", label="开环里程计（越走越偏）")
    ax.plot(cx, cy, lw=2, color="#16a34a", label="闭环定位（定期重定位）")
    ax.scatter(lms[:, 0], lms[:, 1], s=170, marker="*", c="#ea580c", zorder=6, label="地标 / 充电桩")
    for k in sorted(corrections)[:3]:
        ax.annotate("", xy=(xs[k], ys[k]), xytext=(cx[k], cy[k]),
                    arrowprops=dict(arrowstyle="->", color="#16a34a", lw=1.1, alpha=0.7))
    ax.set_xlabel("$x$ / m")
    ax.set_ylabel("$y$ / m")
    ax.set_title("同样的传感器，有没有「回头看」决定了一切")
    ax.legend(fontsize=10, loc="upper left", bbox_to_anchor=(0.02, 0.62))
    ax.set_aspect("equal", adjustable="datalim")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "fig18-01-open-vs-closed-loop.png", dpi=150)
    plt.close(fig)

    # ---- fig18-02：误差曲线 ----
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))
    ax = axes[0]
    t = np.arange(len(open_err)) * 0.1
    ax.plot(t, open_err, lw=2.3, color="#dc2626", label="开环里程计")
    ax.plot(t, errs, lw=2.3, color="#16a34a", label="闭环定位")
    for k in sorted(corrections):
        ax.axvline(k * 0.1, color="#16a34a", lw=0.7, alpha=0.25)
    ax.set_xlabel("时间 $t$ / s")
    ax.set_ylabel("位置误差 / m")
    ax.set_title("开环发散，闭环被锯齿状拉回")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    ax = axes[1]
    ks = sorted(corrections)
    before = [corrections[k][0] for k in ks]
    after = [corrections[k][1] for k in ks]
    xpos = np.arange(len(ks))
    ax.plot(xpos, before, "o--", lw=1.8, color="#dc2626", label="修正前")
    ax.plot(xpos, after, "s-", lw=1.8, color="#16a34a", label="修正后")
    ax.set_xlabel("观测修正序号")
    ax.set_ylabel("该时刻位置误差 / m")
    ax.set_title("8 次重定位中 7 次把误差拉回（首次例外）")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    fig.suptitle("定位的本质：不是算得更准，而是允许被纠正", fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "fig18-02-error-and-corrections.png", dpi=150)
    plt.close(fig)

    print("\n=== 配图已生成 ===")
    for p in sorted(OUT.glob("fig18-*.png")):
        print(" ", p.name, f"{p.stat().st_size/1024:.1f} KB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    args = ap.parse_args()
    res = run()
    if args.plot:
        make_plots(res)


if __name__ == "__main__":
    main()
