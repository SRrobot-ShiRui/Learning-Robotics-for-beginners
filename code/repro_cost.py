#!/usr/bin/env python3
"""第 14 期配套：复现一篇机器人论文的成本核算模型（可复现的量级估算）。

重要：这里的参数是「公开基准的常见量级」，用于演示核算方法，
不是任何一篇具体论文的真实账单。所有结论均由本脚本实跑输出。
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["mathtext.fontset"] = "dejavusans"
FIG_DIR = Path(__file__).resolve().parents[1] / "figs"

# ---- 单价假设（人民币，量级估计，可按自己单位改）----
PRICE = {
    "gpu_hour": 8.0,        # ¥ / GPU·h，云上 A100 量级
    "teleop_hour": 120.0,   # ¥ / h，遥操作采集员
    "engineer_month": 30000.0,  # ¥ / 人月，全负担成本
    "robot_hour": 300.0,    # ¥ / h，真机机时（含折旧与损耗）
}
MIN_PER_EPISODE = 1.0       # 每条示范数据耗时（min），含重置与筛选
DISCARD_RATE = 0.25         # 采集后废弃比例
RERUN_FACTOR = 1.6          # 训练失败/调参重跑倍数
OVERHEAD = 0.15             # 隐性开销占比：环境搭建、复现实验、写报告

# 三档规模（参数本身是量级估计，不是某论文实测）
SCENARIOS = {
    "小规模\n单臂仿真 RL": dict(gpu_hours=200, episodes=200, engineers=1,
                              months=1.0, robot_hours=0),
    "中规模\nVLA 微调": dict(gpu_hours=1500, episodes=5000, engineers=2,
                           months=3.0, robot_hours=120),
    "大规模\n具身预训练": dict(gpu_hours=20000, episodes=50000, engineers=6,
                             months=9.0, robot_hours=600),
}
ITEMS = ["算力", "数据采集", "人力", "真机机时", "隐性开销"]


def cost_breakdown(p, gpu_price=None, data_scale=1.0, robot_scale=1.0,
                   gpu_scale=1.0):
    """按参数算五项成本（¥）。data_scale 放大数据量，算力按平方根亚线性增长。"""
    gpu_price = PRICE["gpu_hour"] if gpu_price is None else gpu_price
    compute = p["gpu_hours"] * RERUN_FACTOR * (data_scale ** 0.5) * gpu_price * gpu_scale
    raw_hours = p["episodes"] * data_scale * MIN_PER_EPISODE / 60.0
    data = raw_hours / (1 - DISCARD_RATE) * PRICE["teleop_hour"]
    human = p["engineers"] * p["months"] * PRICE["engineer_month"]
    robot = p["robot_hours"] * robot_scale * PRICE["robot_hour"]
    direct = compute + data + human + robot
    overhead = direct * OVERHEAD
    return np.array([compute, data, human, robot, overhead]), direct + overhead


def plot_all():
    FIG_DIR.mkdir(exist_ok=True)
    orange = "#ea580c"
    colors = ["#1d4ed8", "#ea580c", "#059669", "#7c3aed", "#78716c"]

    # ---- fig14-01：三档规模成本堆叠 ----
    names = list(SCENARIOS)
    matrix = np.array([cost_breakdown(p)[0] for p in SCENARIOS.values()]).T  # 5 x 3
    totals = matrix.sum(axis=0)
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bottom = np.zeros(3)
    for i, (label, row) in enumerate(zip(ITEMS, matrix)):
        ax.bar(names, row, bottom=bottom, color=colors[i], label=label, width=0.55)
        for j, v in enumerate(row):
            if v / totals[j] > 0.09:
                ax.text(j, bottom[j] + v / 2, f"{v/10000:.1f}万",
                        ha="center", va="center", fontsize=9, color="white", weight="bold")
        bottom += row
    for j, t in enumerate(totals):
        ax.text(j, t * 1.02, f"合计 {t/10000:.1f} 万", ha="center", fontsize=11, weight="bold", color="#7c2d12")
    ax.set_ylabel("成本（元）")
    ax.set_title("复现成本结构：最贵的从来不是 GPU，是人")
    ax.legend(ncol=5, fontsize=9, loc="upper left")
    ax.set_ylim(0, totals.max() * 1.18)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig14-01-cost-stack.png", dpi=160)
    plt.close(fig)

    # ---- fig14-02：两个敏感性实验 ----
    p = SCENARIOS["中规模\nVLA 微调"]
    base = cost_breakdown(p)[1]
    scales = np.array([1, 2, 5, 10, 20])
    totals_scale = np.array([cost_breakdown(p, data_scale=s, robot_scale=s)[1] for s in scales])
    price_ratio = np.array([1.0, 0.5, 0.25, 0.125])
    totals_price = np.array([cost_breakdown(p, gpu_price=PRICE["gpu_hour"] * r)[1] for r in price_ratio])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    ax = axes[0]
    ax.plot(scales, totals_scale / 10000, "o-", color=orange, lw=2)
    ax.set_xlabel("数据规模倍数（同时线性放大真机机时）")
    ax.set_ylabel("总成本（万元）")
    ax.set_title("数据 ×20，总成本涨到 %.1f 倍" % (totals_scale[-1] / totals_scale[0]))
    ax.grid(alpha=0.3)
    for s, t in zip(scales, totals_scale):
        ax.annotate(f"{t/10000:.0f}", (s, t/10000), textcoords="offset points",
                    xytext=(0, 8), ha="center", fontsize=9)

    ax = axes[1]
    ax.plot(price_ratio, (totals_price / base - 1) * 100, "s-", color="#1d4ed8", lw=2)
    ax.invert_xaxis()
    ax.set_xlabel("GPU 单价降到原来的 …（对数刻度）")
    ax.set_ylabel("总成本变化（%）")
    ax.set_xscale("log")
    ax.set_title("GPU 降到 1/8，总成本只降 %.1f%%" % abs((totals_price[-1] / base - 1) * 100))
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig14-02-sensitivity.png", dpi=160)
    plt.close(fig)
    return totals, totals_scale, totals_price, base


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    args = ap.parse_args()

    print("=== 第 14 期成本核算模型实跑输出（量级估算，非具体论文账单）===")
    print(f"单价假设：GPU {PRICE['gpu_hour']} ¥/h，遥操作 {PRICE['teleop_hour']} ¥/h，"
          f"工程师 {PRICE['engineer_month']} ¥/人月，真机 {PRICE['robot_hour']} ¥/h")
    print(f"重跑系数 {RERUN_FACTOR}，数据废弃率 {DISCARD_RATE}，隐性开销 {OVERHEAD:.0%}")
    grand = {}
    for name, p in SCENARIOS.items():
        parts, total = cost_breakdown(p)
        grand[name] = (parts, total)
        print(f"\n[{name.replace(chr(10), ' ')}] 合计 {total:,.0f} 元（{total/10000:.2f} 万）")
        for label, v in zip(ITEMS, parts):
            print(f"    {label:<6} {v:>12,.0f} 元  占比 {v/total:>6.1%}")

    p = SCENARIOS["中规模\nVLA 微调"]
    base = cost_breakdown(p)[1]
    print("\n[敏感性 A] 中规模，数据规模倍数 -> 总成本")
    for s in (1, 2, 5, 10, 20):
        t = cost_breakdown(p, data_scale=s, robot_scale=s)[1]
        print(f"    ×{s:<2}  {t:>12,.0f} 元  相对 ×1 的 {t/base:.2f} 倍")
    print("[敏感性 B] 中规模，GPU 单价倍数 -> 总成本")
    for r in (1.0, 0.5, 0.25, 0.125):
        t = cost_breakdown(p, gpu_price=PRICE["gpu_hour"] * r)[1]
        print(f"    ×{r:<5} {t:>12,.0f} 元  相对原价 {(t/base-1)*100:+.2f}%")

    if args.plot:
        plot_all()
        print("\n[图] 已生成 fig14-01 / fig14-02")


if __name__ == "__main__":
    main()
