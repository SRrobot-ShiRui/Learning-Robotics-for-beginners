#!/usr/bin/env python3
"""第 13 期配套：接触力学入门——摩擦锥、互补条件与「腿式机器人为什么会抖」。

同一个质量块压在地面上，叠加一个周期性的机身高低起伏载荷（8 Hz，步态量级），
用两种接触模型算同一段运动：
  1) 硬接触（速度级 LCP）：严格满足 Signorini 互补条件 + 库仑摩擦锥
  2) 软接触（惩罚法 / 弹簧-阻尼）：把地面当成很硬的弹簧

仅依赖 numpy / matplotlib。
    python3 contact_demo.py           打印全部实测数字（文章引用值以此为准）
    python3 contact_demo.py --plot    另在 figs/ 生成 3 张配图
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

M = 1.0          # 质量 kg
G = 9.81         # 重力 m/s^2
MU = 0.6         # 摩擦系数（橡胶-干混凝土的常见量级）
DT = 1.0e-3      # 积分步长 s
FIG_DIR = Path(__file__).resolve().parents[1] / "figs"


def solve_contact_lcp(v_n, v_t, f_n, f_t, m, dt, mu):
    """单接触点、速度级 LCP 的解析解：返回 (法向接触力, 切向接触力)，单位 N。

    约定：v_n 为法向速度（向上为正，向下趋近地面为负），接触力向上为正。
    """
    v_n_free = v_n + dt * f_n / m                       # (1) 不含接触力的自由法向速度
    v_t_free = v_t + dt * f_t / m                       # (2) 不含接触力的自由切向速度
    if v_n_free >= 0.0:                                 # (3) 互补条件：正在分离，接触力必须为 0
        return 0.0, 0.0
    lam_n = -m * v_n_free / dt                         # (4) 恰好把法向速度消到 0 的力
    lam_needed = -m * v_t_free / dt                    # (5) 想让切向速度也归零所需要的力
    lam_t = float(np.clip(lam_needed, -mu * lam_n, mu * lam_n))  # (6) 摩擦锥投影 + 最大耗散
    return lam_n, lam_t


def soft_contact(z, v_n, v_t, k, c, mu, v_eps=0.01):
    """惩罚法：地面是刚度 k、阻尼 c 的弹簧；摩擦用 tanh 正则化的库仑律。"""
    penetration = max(0.0, -z)                           # 穿透深度（z<0 才算陷进去）
    lam_n = max(0.0, k * penetration + c * max(0.0, -v_n))
    lam_t = -mu * lam_n * np.tanh(v_t / v_eps)
    return lam_n, lam_t


def simulate(kind, k=5.0e3, c=14.14, load_amp=3.0, load_hz=8.0,
             f_t=0.0, steps=400, dt=DT):
    """块从 z=0 静止接触出发，承受机身高低起伏载荷；半隐式欧拉积分。"""
    z = v_n = v_t = 0.0
    rec = {"t": [], "z": [], "v_n": [], "v_t": [], "lam_n": [], "lam_t": [],
           "target": []}
    for i in range(steps):
        t = i * dt
        f_n = -M * G - load_amp * np.sin(2 * np.pi * load_hz * t)  # 重力 + 周期性附加载荷
        target = M * G + load_amp * np.sin(2 * np.pi * load_hz * t)  # 无误差时的真实支撑力
        if kind == "lcp":
            lam_n, lam_t = solve_contact_lcp(v_n, v_t, f_n, f_t, M, dt, MU)
        else:
            lam_n, lam_t = soft_contact(z, v_n, v_t, k, c, MU)
        v_n += dt * (f_n + lam_n) / M                    # (7) 先更新速度
        v_t += dt * (f_t + lam_t) / M
        z += dt * v_n                                    # (8) 再更新位置（半隐式，弹簧更稳）
        for key, val in (("t", t), ("z", z), ("v_n", v_n), ("v_t", v_t),
                         ("lam_n", lam_n), ("lam_t", lam_t), ("target", target)):
            rec[key].append(val)
    return {key: np.asarray(val) for key, val in rec.items()}


def verify_complementarity(n=2000, seed=7):
    """随机工况检验：互补残差、摩擦锥违反、法向不穿透三项必须全部达标。"""
    rng = np.random.default_rng(seed)
    max_comp, max_cone, min_vn = 0.0, 0.0, 1.0e9
    for _ in range(n):
        v_n = rng.uniform(-3.0, 3.0)
        v_t = rng.uniform(-3.0, 3.0)
        f_n = rng.uniform(-20.0, 20.0)
        f_t = rng.uniform(-20.0, 20.0)
        mu = rng.uniform(0.1, 1.0)
        lam_n, lam_t = solve_contact_lcp(v_n, v_t, f_n, f_t, M, DT, mu)
        v_n_plus = v_n + DT * (f_n + lam_n) / M
        max_comp = max(max_comp, abs(lam_n * v_n_plus))
        max_cone = max(max_cone, abs(lam_t) - mu * lam_n)
        min_vn = min(min_vn, v_n_plus)
    return max_comp, max_cone, min_vn


def find_slip_threshold():
    """扫描水平推力，找块从粘滞转为滑动的临界值，与解析值 mu*m*g 对照。"""
    analytic = MU * M * G
    f_grid = np.arange(0.0, 10.0001, 0.001)
    steady_v = []
    for f in f_grid:
        s = simulate("lcp", load_amp=0.0, f_t=f, steps=20)
        steady_v.append(s["v_t"][-1])                 # 0.02 s 后的切向速度
    steady_v = np.asarray(steady_v)
    idx = int(np.argmax(steady_v > 1.0e-9))
    measured = f_grid[idx] if steady_v.max() > 1e-9 else float("nan")
    return analytic, measured, f_grid, steady_v


def stiffness_sweep():
    """刚度扫描：固定阻尼比 0.1，看力跟踪误差与稳态穿透如何随 k 变化。"""
    ks = np.array([2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5])
    zeta = 0.1
    rms, pen = [], []
    for k in ks:
        c = 2 * zeta * np.sqrt(k * M)
        s = simulate("soft", k=k, c=c, steps=400)
        err = s["lam_n"][100:] - s["target"][100:]     # 去掉起始瞬态，取后 0.3 s
        rms.append(float(np.sqrt(np.mean(err ** 2))))
        pen.append(float(np.mean(np.maximum(0.0, -s["z"][100:])) * 1000.0))  # mm
    return ks, np.asarray(rms), np.asarray(pen)


def check_numerical_stiffness():
    """数值刚性：软接触刚度越高，允许的积分步长越小；硬约束 LCP 不受步长限制。"""
    k, zeta = 2.0e5, 0.1
    c = 2 * zeta * np.sqrt(k * M)
    out = {}
    for dt in (1.0e-3, 5.0e-3):
        s = simulate("soft", k=k, c=c, steps=200, dt=dt)
        out[dt] = float(np.max(np.abs(s["lam_n"])))
    for dt in (1.0e-3, 5.0e-3):
        s = simulate("lcp", steps=200, dt=dt)
        out[("lcp", dt)] = float(np.max(np.abs(s["lam_n"])))
    return out


def plot_all():
    FIG_DIR.mkdir(exist_ok=True)
    orange, blue, gray = "#ea580c", "#1d4ed8", "#78716c"

    # ---- fig13-01：摩擦锥 + 互补条件 ----
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axes[0]
    lam_n = np.linspace(0, 20, 300)
    ax.fill_betweenx(lam_n, -MU * lam_n, MU * lam_n, color="#fed7aa", alpha=0.8,
                     label=r"可行域 $|\lambda_t|\leq\mu\lambda_n$")
    ax.plot(-MU * lam_n, lam_n, color=orange, lw=2)
    ax.plot(MU * lam_n, lam_n, color=orange, lw=2)
    ax.hlines(M * G, -MU * M * G, MU * M * G, color=blue, lw=3,
              label=r"$mg=9.81$ N 时的切向上限")
    ax.set_xlabel(r"切向接触力 $\lambda_t$ (N)")
    ax.set_ylabel(r"法向接触力 $\lambda_n$ (N)")
    ax.set_xlim(-13, 13); ax.set_ylim(0, 20)
    ax.set_title(r"库仑摩擦锥（$\mu=0.6$）")
    ax.legend(fontsize=9, loc="upper left"); ax.grid(alpha=0.3)

    ax = axes[1]
    v_free = np.linspace(-0.06, 0.06, 400)
    lam = np.where(v_free >= 0, 0.0, -M * v_free / DT)
    ax.plot(v_free * 1000, lam, color=orange, lw=2.2)
    ax.axvline(0, color=gray, ls="--", lw=1)
    ax.set_xlabel(r"自由法向速度 $v_n^{free}$ (mm/s)")
    ax.set_ylabel(r"$\lambda_n$ (N)")
    ax.set_title("Signorini 互补条件：分离时力必须为 0")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig13-01-friction-cone.png", dpi=160)
    plt.close(fig)

    # ---- fig13-02：周期载荷下硬接触 vs 软接触 ----
    hard = simulate("lcp")
    soft = simulate("soft", k=5.0e3, c=14.14)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axes[0]
    ax.plot(hard["t"], hard["target"], color=gray, ls="--", lw=1.5, label="真实所需支撑力")
    ax.plot(hard["t"], hard["lam_n"], color=blue, lw=2, label="硬接触 LCP（严格跟踪）")
    ax.plot(soft["t"], soft["lam_n"], color=orange, lw=1.4, label="软接触（k=5e3）")
    ax.set_xlabel("时间 (s)"); ax.set_ylabel(r"法向接触力 $\lambda_n$ (N)")
    ax.set_title("8 Hz 机身起伏下：软接触放大且滞后")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    ax = axes[1]
    ax.plot(hard["t"], -hard["z"] * 1000, color=blue, lw=2, label="硬接触 LCP（0 穿透）")
    ax.plot(soft["t"], -soft["z"] * 1000, color=orange, lw=1.4, label="软接触")
    ax.set_xlabel("时间 (s)"); ax.set_ylabel("穿透深度 (mm)")
    ax.set_title("软接触靠「陷进去」产生支持力，硬接触不需要")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig13-02-soft-vs-hard.png", dpi=160)
    plt.close(fig)

    # ---- fig13-03：刚度扫描 + 滑动阈值 ----
    ks, rms, pen = stiffness_sweep()
    analytic, measured, f_grid, steady_v = find_slip_threshold()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axes[0]
    ax.loglog(ks, np.maximum(rms, 1e-6), "o-", color=orange, lw=2, label="力跟踪 RMS (N)")
    ax.set_xlabel(r"接触刚度 $k$ (N/m)"); ax.set_ylabel("力跟踪 RMS (N)", color=orange)
    ax.tick_params(axis="y", labelcolor=orange)
    ax2 = ax.twinx()
    ax2.loglog(ks, np.maximum(pen, 1e-6), "s--", color=blue, lw=2, label="稳态穿透 (mm)")
    ax2.set_ylabel("稳态穿透 (mm)", color=blue)
    ax2.tick_params(axis="y", labelcolor=blue)
    ax.set_title("刚度两难：软了共振/陷进去，硬了要更小步长")
    ax.grid(alpha=0.3, which="both")
    ax = axes[1]
    ax.plot(f_grid, steady_v, color=blue, lw=2)
    ax.axvline(analytic, color=orange, ls="--", lw=2,
               label=r"解析临界 $\mu m g=5.886$ N")
    ax.set_xlabel("水平推力 F (N)"); ax.set_ylabel("0.02 s 后切向速度 (m/s)")
    ax.set_title("粘滞→滑动的分界：摩擦锥决定推不推得动")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig13-03-stiffness-and-slip.png", dpi=160)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true", help="生成配图")
    args = ap.parse_args()

    comp, cone, min_vn = verify_complementarity()
    analytic, measured, _, _ = find_slip_threshold()
    hard = simulate("lcp")
    soft = simulate("soft", k=5.0e3, c=14.14)
    hard_err = hard["lam_n"][100:] - hard["target"][100:]
    soft_err = soft["lam_n"][100:] - soft["target"][100:]
    ks, rms, pen = stiffness_sweep()
    stiff = check_numerical_stiffness()

    print("=== 第 13 期实测数字（文章引用值以此为准） ===")
    print("[1] LCP 严格性（2000 组随机工况）")
    print(f"    max |lambda_n * v_n+|        = {comp:.3e}   （互补残差，应为 0）")
    print(f"    max (|lambda_t| - mu*lam_n) = {cone:.3e} N（摩擦锥违反，应 <= 0）")
    print(f"    min v_n+                    = {min_vn:.3e} m/s（法向不得穿透）")
    print("[2] 粘滞→滑动临界推力")
    print(f"    解析 mu*m*g                 = {analytic:.4f} N")
    print(f"    扫描实测首个滑动点          = {measured:.4f} N")
    print("[3] 8 Hz 周期载荷下，0.1~0.4 s 的力跟踪表现")
    print(f"    硬接触 LCP：RMS = {np.sqrt(np.mean(hard_err ** 2)):.3e} N，"
          f"最大穿透 = {np.max(np.maximum(0.0, -hard['z'])) * 1000:.3e} mm")
    print(f"    软接触    ：RMS = {np.sqrt(np.mean(soft_err ** 2)):.3f} N，"
          f"稳态穿透 = {np.mean(np.maximum(0.0, -soft['z'][100:])) * 1000:.4f} mm，"
          f"力峰值 = {soft['lam_n'].max():.3f} N")
    print("[4] 刚度扫描（阻尼比固定 0.1）：k / 力跟踪 RMS / 稳态穿透")
    for k, r, p in zip(ks, rms, pen):
        print(f"    k={k:>8.0f} N/m   RMS={r:>8.3f} N   penetration={p:>8.4f} mm")
    print("[5] 数值刚性：k=2e5 时不同步长的 |lambda_n| 峰值")
    print(f"    软接触 dt=1e-3: {stiff[1e-3]:>10.3f} N   dt=5e-3: {stiff[5e-3]:>12.3e} N")
    print(f"    硬接触 dt=1e-3: {stiff[('lcp', 1e-3)]:>10.3f} N   "
          f"dt=5e-3: {stiff[('lcp', 5e-3)]:>12.3f} N")
    if args.plot:
        plot_all()
        print("[图] 已生成 figs/fig13-01/02/03")


if __name__ == "__main__":
    main()
