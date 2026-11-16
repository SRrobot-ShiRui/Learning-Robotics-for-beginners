#!/usr/bin/env python3
"""第 15 期配套：为什么「闭着眼」走两步就歪——IMU 零偏与二次积分漂移。

真实轨迹：0–2 s 加速到 1 m/s，2–8 s 匀速，8–10 s 减速到 0，全程 8 m。
三种观测量对比：真值 / 纯 IMU 二次积分 / 轮速里程计积分。

仅依赖 numpy / matplotlib。
    python3 imu_drift.py           打印全部实测数字
    python3 imu_drift.py --plot    另在 figs/ 生成 2 张配图
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

DT = 1.0e-3
T_END = 10.0
BIAS = 0.02            # 加速度计零偏 m/s^2（消费级 MEMS 常见量级）
ACC_NOISE = 0.005      # 加速度噪声标准差 m/s^2
ODO_SCALE_ERR = 0.005  # 轮速里程计比例误差 0.5%
ODO_NOISE = 0.002      # 轮速噪声标准差 m/s
FIG_DIR = Path(__file__).resolve().parents[1] / "figs"


def true_motion(t):
    """解析真值：返回 (位置 m, 速度 m/s, 加速度 m/s^2)，不累积数值误差。"""
    a = np.where(t < 2.0, 0.5, np.where(t < 8.0, 0.0, -0.5))
    v = np.where(t < 2.0, 0.5 * t,
                 np.where(t < 8.0, 1.0, 1.0 - 0.5 * (t - 8.0)))
    x = np.where(t < 2.0, 0.25 * t ** 2,
                 np.where(t < 8.0, 1.0 + (t - 2.0),
                          7.0 + (t - 8.0) - 0.25 * (t - 8.0) ** 2))
    return x, v, a


def dead_reckon(a_meas, dt=DT, x0=0.0, v0=0.0):
    """纯惯性航迹推算：把加速度二次积分成位置。返回 (位置, 速度) 序列。"""
    n = len(a_meas)
    x = np.empty(n)                       # (1) 预分配，避免循环里动态拼接
    v = np.empty(n)
    xx, vv = x0, v0
    for i in range(n):
        vv = vv + a_meas[i] * dt            # (2) 加速度 → 速度（显式欧拉）
        xx = xx + vv * dt                    # (3) 速度 → 位置（半隐式：用刚更新的速度）
        x[i], v[i] = xx, vv                 # (4) 记录本时刻状态
    return x, v


def integrate_odometry(v_meas, dt=DT):
    """轮速里程计：直接积分速度（只有一次积分，误差线性增长而非二次）。"""
    return np.cumsum(v_meas) * dt


def bias_sweep(biases):
    """零偏扫描：同一个 10 s 轨迹，不同零偏下的终点位置误差（含噪声，固定种子）。"""
    t = np.arange(0, T_END, DT)
    x_true, v_true, a_true = true_motion(t)
    rng = np.random.default_rng(2026)
    noise = rng.normal(0.0, ACC_NOISE, size=len(t))
    out = []
    for b in biases:
        x_est, _ = dead_reckon(a_true + b + noise)
        out.append(abs(x_est[-1] - x_true[-1]))
    return np.asarray(out)


def plot_all(t, x_true, v_true, a_true, x_imu, x_odo, err_imu, err_odo):
    FIG_DIR.mkdir(exist_ok=True)
    orange, blue, green, gray = "#ea580c", "#1d4ed8", "#059669", "#78716c"

    # ---- fig15-01：位置 + 误差 ----
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    ax = axes[0]
    ax.plot(t, x_true, color=gray, lw=3, label="真实位置")
    ax.plot(t, x_odo, color=green, lw=1.8, ls="--", label="轮速里程计")
    ax.plot(t, x_imu, color=orange, lw=1.8, label="纯 IMU 二次积分")
    ax.set_xlabel("时间 (s)"); ax.set_ylabel("位置 (m)")
    ax.set_title("走完 8 m：纯 IMU 读数是 9 m")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(t, err_imu, color=orange, lw=2, label="纯 IMU 位置误差")
    ax.plot(t, 0.5 * BIAS * t ** 2, color=blue, lw=1.5, ls="--",
            label=r"理论 $0.5bt^2$")
    ax.plot(t, err_odo, color=green, lw=1.8, label="轮速里程计误差")
    ax.set_xlabel("时间 (s)"); ax.set_ylabel("位置误差 (m)")
    ax.set_title("误差随时间平方增长：零偏被积分了两次")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig15-01-imu-drift.png", dpi=160)
    plt.close(fig)

    # ---- fig15-02：零偏扫描 + 二次律验证 ----
    biases = np.logspace(-4, -1, 25)
    errs = bias_sweep(biases)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    ax = axes[0]
    ax.loglog(biases, errs, "o-", color=orange, lw=2, ms=4)
    ax.axvline(BIAS, color=blue, ls="--", lw=1.5, label="消费级 IMU 0.02 m/s²")
    ax.axhline(0.1, color=gray, ls=":", lw=1.5, label="10 cm 精度线")
    ax.set_xlabel(r"加速度计零偏 $b$ (m/s²)")
    ax.set_ylabel("10 s 后位置误差 (m)")
    ax.set_title("零偏小 100 倍，漂移才小 100 倍")
    ax.legend(fontsize=9); ax.grid(alpha=0.3, which="both")

    ax = axes[1]
    mask = t > 0.5
    ratio = err_imu[mask] / (t[mask] ** 2)
    ax.plot(t[mask], ratio, color=blue, lw=1.5)
    ax.axhline(BIAS / 2, color=orange, ls="--", lw=2,
               label=r"理论 $b/2=0.01$")
    ax.set_xlabel("时间 (s)"); ax.set_ylabel(r"误差 $/t^2$ (m/s²)")
    ax.set_ylim(0, 0.02)
    ax.set_title("误差除以 t² 基本是常数 → 确认二次律")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig15-02-bias-sweep.png", dpi=160)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    args = ap.parse_args()

    t = np.arange(0, T_END, DT)
    x_true, v_true, a_true = true_motion(t)
    rng = np.random.default_rng(2026)
    a_meas = a_true + BIAS + rng.normal(0.0, ACC_NOISE, size=len(t))
    x_imu, v_imu = dead_reckon(a_meas)
    rng2 = np.random.default_rng(11)
    v_odo_meas = v_true * (1 + ODO_SCALE_ERR) + rng2.normal(0.0, ODO_NOISE, size=len(t))
    x_odo = integrate_odometry(v_odo_meas)
    err_imu = np.abs(x_imu - x_true)
    err_odo = np.abs(x_odo - x_true)

    print("=== 第 15 期实测数字（文章引用值以此为准） ===")
    print(f"[1] 真实轨迹：10 s 走 {x_true[-1]:.4f} m，末速度 {v_true[-1]:.4f} m/s")
    print(f"[2] 加速度计零偏 b = {BIAS} m/s²，噪声 σ = {ACC_NOISE} m/s²")
    print(f"    纯 IMU 10 s 位置        = {x_imu[-1]:.4f} m")
    print(f"    纯 IMU 10 s 位置误差    = {err_imu[-1]:.4f} m")
    print(f"    理论 0.5*b*t²           = {0.5 * BIAS * T_END ** 2:.4f} m")
    print(f"    误差 / t² 在 t>0.5 s 的均值 = {np.mean(err_imu[t > 0.5] / (t[t > 0.5] ** 2)):.6f} "
          f"（理论 b/2 = {BIAS / 2:.6f}）")
    print(f"[3] 轮速里程计（比例误差 {ODO_SCALE_ERR:.1%}）")
    print(f"    10 s 位置误差            = {err_odo[-1]:.4f} m")
    print(f"[4] 零偏扫描：10 s 漂移")
    for b in (2.0e-4, 2.0e-3, 2.0e-2, 1.0e-1):
        print(f"    b={b:.0e} m/s² -> 漂移 {bias_sweep([b])[0]:.4f} m")
    print(f"[5] 想让 10 s 漂移 < 0.1 m，零偏需 < {2 * 0.1 / T_END ** 2:.0e} m/s² "
          f"（比当前好 {BIAS / (2 * 0.1 / T_END ** 2):.0f} 倍）")

    if args.plot:
        plot_all(t, x_true, v_true, a_true, x_imu, x_odo, err_imu, err_odo)
        print("[图] 已生成 fig15-01 / fig15-02")


if __name__ == "__main__":
    main()
