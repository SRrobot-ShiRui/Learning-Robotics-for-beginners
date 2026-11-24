#!/usr/bin/env python3
"""第 17 篇配套：从「演示视频」到「工时账单」的可靠性量化（纯 numpy/matplotlib）。

把 5 个常被混用的数字拆开算：
  1) 单任务成功率 p 与整班次「无人干预」概率 p^N（N 为一班次任务数）
  2) 「演示视频看起来 100% 成功」的剪辑偏差：拍 K 条取最好一条
  3) 平均故障间隔 MTTF、每班次人工介入次数、有效工时
  4) 达到班次可靠性目标所需的单次成功率
  5) p 的敏感性：从 0.90 提到 0.999 分别值多少钱

运行：python3 deployment_metrics.py --plot
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

# 一班次的参数（量级假设，文章中标注为口径而非某厂商真实数据）
SHIFT_HOURS = 8.0
TASK_MIN = 1.0          # 单个任务耗时（分钟）
RECOVER_MIN = 6.0       # 每次人工介入的恢复耗时（分钟）


def tasks_per_shift():
    return SHIFT_HOURS * 60 / TASK_MIN


def exp1_shift_reliability():
    N = int(tasks_per_shift())
    print("=== 实验 1：单任务成功率 -> 整班次无干预概率 ===")
    print(f"班次 {SHIFT_HOURS:g} h，单任务 {TASK_MIN:g} min => N = {N} 次任务/班")
    rows = []
    for p in (0.90, 0.95, 0.98, 0.99, 0.995, 0.999, 0.9999):
        p_shift = p ** N
        exp_fail = N * (1 - p)
        rows.append((p, p_shift, exp_fail))
        print(f"p = {p:<7.4f}  整班无干预 = {p_shift:>9.4%}  期望失败次数 = {exp_fail:>8.2f}")
    target = 0.95
    p_need = target ** (1.0 / N)
    print(f"要让整班无干预概率达到 {target:.0%}，需要单任务 p >= {p_need:.6f}")
    print(f"即每 {1/(1-p_need):.0f} 次任务最多失败 1 次")
    return N, rows, p_need


def exp2_demo_bias():
    print("\n=== 实验 2：演示视频的剪辑偏差（拍 K 条取最好一条） ===")
    print("观众看到的是「至少一条成功」，真实指标是单次成功率 p")
    rows = []
    for p in (0.30, 0.50, 0.70, 0.90):
        line = []
        for K in (1, 5, 20, 50, 100):
            at_least_one = 1 - (1 - p) ** K
            line.append(at_least_one)
        rows.append((p, line))
        print(f"p = {p:.2f} : " + "  ".join(
            f"K={K}: {v:.2%}" for K, v in zip((1, 5, 20, 50, 100), line)))
    print("结论：p=0.30 拍 20 条就有 99.92% 概率剪出一条「完美演示」")
    return rows


def exp3_work_hours():
    N = int(tasks_per_shift())
    print("\n=== 实验 3：有效工时与人工介入 ===")
    rows = []
    for p in (0.90, 0.95, 0.98, 0.99, 0.995, 0.999):
        exp_fail = N * (1 - p)
        lost_h = exp_fail * RECOVER_MIN / 60
        eff_h = SHIFT_HOURS - lost_h
        good_tasks = N - exp_fail
        rows.append((p, exp_fail, lost_h, eff_h, good_tasks))
        print(f"p = {p:<6.3f} 介入 {exp_fail:>6.2f} 次，损失 {lost_h:>5.2f} h，"
              f"有效 {eff_h:>5.2f} h，完成 {good_tasks:>6.1f} 件")
    return rows


def exp4_sensitivity():
    N = int(tasks_per_shift())
    print("\n=== 实验 4：把 p 从 0.90 提到 0.999 值多少 ===")
    base_p, base = 0.90, None
    for p in (0.90, 0.95, 0.99, 0.999):
        exp_fail = N * (1 - p)
        eff_h = SHIFT_HOURS - exp_fail * RECOVER_MIN / 60
        if base is None:
            base = eff_h
        print(f"p = {p:<6.3f} 有效工时 {eff_h:>5.2f} h  (相对 0.90 提升 {(eff_h/base-1)*100:>5.1f}%)")
    print("注意：p 的绝对增量只有 0.099，有效工时却提升 148.5%（3.20 -> 7.95 h）——可靠性是非线性的")
    return


def make_plots(e1, e2, e3):
    OUT.mkdir(parents=True, exist_ok=True)
    N, rows1, p_need = e1
    rows2 = e2
    rows3 = e3

    # ---- fig17-01：p vs 整班无干预（不同 N） ----
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))
    ax = axes[0]
    ps = np.linspace(0.90, 0.9999, 400)
    for n, c in [(50, "#16a34a"), (N, "#dc2626"), (1000, "#7c3aed")]:
        ax.plot(ps, ps ** n, lw=2.2, color=c, label=f"$N={n}$ 次任务/班")
    ax.axhline(0.95, color="0.5", ls="--", lw=1.2)
    ax.axvline(p_need, color="#dc2626", ls=":", lw=1.5)
    ax.text(p_need, 0.05, f"  $p\\geq{p_need:.4f}$", color="#dc2626", fontsize=10)
    ax.set_xlabel("单任务成功率 $p$")
    ax.set_ylabel("整班次无人工干预概率 $p^N$")
    ax.set_title("99% 听起来很高，乘上 N 次就塌了")
    ax.set_ylim(-0.02, 1.02)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    ax = axes[1]
    Ks = np.array([1, 5, 20, 50, 100])
    for p, c in [(0.30, "#dc2626"), (0.50, "#ea580c"), (0.70, "#2563eb"), (0.90, "#16a34a")]:
        ax.plot(Ks, 1 - (1 - p) ** Ks, "o-", lw=2, color=c, label=f"真实 $p={p:.2f}$")
    ax.set_xlabel("拍摄条数 $K$（取最好一条）")
    ax.set_ylabel("观众看到「至少一条成功」的概率")
    ax.set_title("演示视频的 100% 成功，与真实成功率无关")
    ax.set_ylim(-0.02, 1.02)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    fig.suptitle("从演示视频到工时账单：可靠性是怎么被误读的", fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "fig17-01-reliability-and-demo-bias.png", dpi=150)
    plt.close(fig)

    # ---- fig17-02：有效工时 ----
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.8))
    ax = axes[0]
    pvals = [r[0] for r in rows3]
    effs = [r[3] for r in rows3]
    lost = [r[2] for r in rows3]
    ax.bar(range(len(pvals)), effs, color="#16a34a", alpha=0.85, label="有效工时")
    ax.bar(range(len(pvals)), lost, bottom=effs, color="#dc2626", alpha=0.85, label="人工介入损失")
    ax.axhline(SHIFT_HOURS, color="0.4", ls="--", lw=1.2)
    ax.set_xticks(range(len(pvals)))
    ax.set_xticklabels([f"{p:.3f}" for p in pvals], rotation=30, fontsize=9)
    ax.set_xlabel("单任务成功率 $p$")
    ax.set_ylabel("工时 / h")
    ax.set_title("8 小时班次里，真正干活的时间")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3, axis="y")

    ax = axes[1]
    n_interv = [r[1] for r in rows3]
    ax.plot(pvals, n_interv, "o-", lw=2.3, color="#dc2626")
    for p, y in zip(pvals, n_interv):
        ax.annotate(f"{y:.1f}", (p, y), textcoords="offset points", xytext=(0, 8),
                    ha="center", fontsize=9)
    ax.set_xlabel("单任务成功率 $p$")
    ax.set_ylabel("每班人工介入次数")
    ax.set_title("运维人力才是部署的隐性成本")
    ax.grid(alpha=0.3)
    fig.suptitle("工时账单：可靠性最终折算成人", fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "fig17-02-effective-work-hours.png", dpi=150)
    plt.close(fig)

    print("\n=== 配图已生成 ===")
    for p in sorted(OUT.glob("fig17-*.png")):
        print(" ", p.name, f"{p.stat().st_size/1024:.1f} KB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    args = ap.parse_args()
    e1 = exp1_shift_reliability()
    e2 = exp2_demo_bias()
    e3 = exp3_work_hours()
    exp4_sensitivity()
    if args.plot:
        make_plots(e1, e2, e3)


if __name__ == "__main__":
    main()
