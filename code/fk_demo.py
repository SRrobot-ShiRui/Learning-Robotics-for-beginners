#!/usr/bin/env python3
"""正运动学 (Forward Kinematics) 三种建模方式对比演示。

涵盖：
  - 累计角 FK（平面臂最自然的写法）
  - 标准 DH 齐次矩阵连乘
  - 乘积指数 PoE（空间旋量，现代库 Pinocchio/Drake 的底层）

结论：三者对同一条臂给出完全一致的末端位姿。脚本同时绘制
  fig07-01 同一构型下 DH 连杆坐标系 与 PoE 旋量轴 的等价可视化
  fig07-02 工作空间可达性热力图（纯 FK 采样）

用法：
    python3 fk_demo.py --plot    # 出图到 ../docs/Robot_Alchemy/figs/
"""
import argparse
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# ---- 中文字体（与全站统一，避免方框乱码）----
_cjk = None
for cand in ["Noto Sans CJK JP", "Noto Sans CJK SC", "WenQuanYi Zen Hei"]:
    if any(cand in fm.name for fm in font_manager.fontManager.ttflist):
        _cjk = cand
        break
if _cjk:
    plt.rcParams["font.family"] = _cjk
plt.rcParams["axes.unicode_minus"] = False

L = np.array([1.0, 0.8, 0.6])  # 三段连杆长度 (m)


# ---------- 三种 FK 实现 ----------
def fk_cum(q):
    """累计角写法：平面臂最直观的 FK。返回 4 个关节点（基座、J1、J2、末端）。"""
    ang = np.cumsum(q)
    pts = [np.zeros(2)]
    p = np.zeros(2)
    for i in range(3):
        p = p + L[i] * np.array([np.cos(ang[i]), np.sin(ang[i])])
        pts.append(p.copy())
    return np.array(pts)


def _dh(theta, a):
    c, s = np.cos(theta), np.sin(theta)
    # 正确的经典 DH 基本矩阵 A = Rz(theta) · Tx(a)：平移列 = a·(cosθ, sinθ)
    return np.array([[c, -s, 0, a * c], [s, c, 0, a * s], [0, 0, 1, 0], [0, 0, 0, 1]])


def fk_dh(q):
    """标准 DH：每个转动关节一串 4x4 齐次变换连乘，取末端平移列。"""
    T = np.eye(4)
    for i in range(3):
        T = T @ _dh(q[i], L[i])
    return T[0:2, 3]


def _skew(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def _exp_rot(w, th):
    K = _skew(w / np.linalg.norm(w))
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)


def _screw_exp(S, th):
    w, v = S[:3], S[3:]
    R = _exp_rot(w, th)
    G = np.eye(3) * th + (1 - np.cos(th)) * _skew(w) + (th - np.sin(th)) * _skew(w) @ _skew(w)
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = G @ v
    return T


# 空间 PoE 旋量轴：第 i 个转动关节，轴 = +z，穿过零位时关节位置 o_i
_joint_pos = [np.array([0.0, 0.0, 0.0]),
              np.array([L[0], 0.0, 0.0]),
              np.array([L[0] + L[1], 0.0, 0.0])]
_S = []
for o in _joint_pos:
    w = np.array([0.0, 0.0, 1.0])
    v = -np.cross(w, o)  # v = -w × o
    _S.append(np.concatenate([w, v]))
_M = np.eye(4)
_M[0, 3] = L.sum()  # 零位末端位置


def fk_poe(q):
    """乘积指数：T(q)=e^{[S1]q1} e^{[S2]q2} e^{[S3]q3} M。"""
    T = np.eye(4)
    for i in range(3):
        T = T @ _screw_exp(_S[i], q[i])
    T = T @ _M
    return T[0:2, 3]


# ---------- 验证 ----------
def verify():
    rng = np.random.default_rng(0)
    max_err = 0.0
    for _ in range(500):
        q = rng.uniform(-np.pi, np.pi, 3)
        p_cum = fk_cum(q)[-1]
        p_dh = fk_dh(q)
        p_poe = fk_poe(q)
        max_err = max(max_err, np.linalg.norm(p_cum - p_dh),
                      np.linalg.norm(p_cum - p_poe))
    print("[V] 500 组随机构型下 三种FK 末端位置最大互差 = %.2e m" % max_err)
    q0 = np.array([0.6, -0.4, 0.9])
    print("[V] 示例构型 q=(%.2f, %.2f, %.2f)" % tuple(q0))
    print("    累计角 末端 =", np.round(fk_cum(q0)[-1], 4))
    print("    DH     末端 =", np.round(fk_dh(q0), 4))
    print("    PoE    末端 =", np.round(fk_poe(q0), 4))
    return max_err


# ---------- 配图 ----------
def plot_frames_vs_screws():
    q = np.array([0.6, -0.4, 0.9])
    pts = fk_cum(q)
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    # 连杆
    ax.plot(pts[:, 0], pts[:, 1], "-o", color="#1f77b4", lw=4, ms=8,
            label="连杆 (DH 连杆坐标系的 x 轴连线)")
    # DH 关节坐标系（小箭头表示每个连杆的 x 朝向）
    ang = np.cumsum(q)
    for i in range(3):
        o = pts[i]
        d = np.array([np.cos(ang[i]), np.sin(ang[i])])
        ax.quiver(o[0], o[1], d[0], d[1], angles="xy", scale_units="xy",
                  scale=1.6, color="#2ca02c", width=0.012, label=None)
    # PoE 旋量轴（穿过零位关节位置的 z 轴，用垂直于纸面的圆点表示）
    for o in _joint_pos:
        ax.plot(o[0], o[1], "X", ms=14, mec="#d62728", mfc="none",
                mew=2.2, label=None)
    ax.plot(_joint_pos[1][0], _joint_pos[1][1], "X", ms=14, mec="#d62728",
            mfc="none", mew=2.2, label="PoE 旋量轴 (穿过各关节零位)")
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_xlabel("x / m")
    ax.set_ylabel("y / m")
    ax.set_title("同一构型：DH 连杆坐标系 与 PoE 旋量轴 等价")
    ax.legend(loc="upper right", fontsize=9)
    fig.tight_layout()
    return fig


def plot_workspace():
    # 工作空间末端密度：向量化采样 200 万组构型，histogram2d 统计
    rng = np.random.default_rng(1)
    n = 2_000_000
    ang = rng.uniform(-np.pi, np.pi, (3, n))
    c = np.cos(ang)
    s = np.sin(ang)
    x = L[0] * c[0] + L[1] * (c[0] * c[1] - s[0] * s[1]) + L[2] * (
        c[0] * (c[1] * c[2] - s[1] * s[2]) - s[0] * (c[1] * s[2] + s[1] * c[2]))
    y = L[0] * s[0] + L[1] * (s[0] * c[1] + c[0] * s[1]) + L[2] * (
        s[0] * (c[1] * c[2] - s[1] * s[2]) + c[0] * (c[1] * s[2] + s[1] * c[2]))
    H, xe, ye = np.histogram2d(x, y, bins=300,
                               range=[[-2.6, 2.6], [-2.6, 2.6]])
    fig, ax = plt.subplots(figsize=(6.8, 6.2))
    im = ax.imshow(H.T, extent=[xe[0], xe[-1], ye[0], ye[-1]],
                   origin="lower", cmap="magma",
                   norm=matplotlib.colors.LogNorm())
    q = np.array([0.6, -0.4, 0.9])
    pts = fk_cum(q)
    ax.plot(pts[:, 0], pts[:, 1], "-o", color="cyan", lw=2.5, ms=6)
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(2.4 * np.cos(th), 2.4 * np.sin(th), "--", color="white", lw=1.2, alpha=0.7)
    ax.set_aspect("equal")
    ax.set_xlabel("x / m")
    ax.set_ylabel("y / m")
    ax.set_title("工作空间末端密度（200 万构型采样，白圈 = 最大可达半径 2.4 m）")
    fig.colorbar(im, ax=ax, label="采样命中次数（对数）")
    fig.tight_layout()
    return fig


def main():
    max_err = verify()
    assert max_err < 1e-9, "三种 FK 不一致"
    import os
    out = os.path.join(os.path.dirname(__file__), "..", "docs", "Robot_Alchemy", "figs")
    os.makedirs(out, exist_ok=True)
    plot_frames_vs_screws().savefig(os.path.join(out, "fig07-01-fk-frames.png"), dpi=130)
    plot_workspace().savefig(os.path.join(out, "fig07-02-workspace.png"), dpi=130)
    print("[V] 已生成 fig07-01-fk-frames.png / fig07-02-workspace.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    args = ap.parse_args()
    if args.plot:
        main()
    else:
        verify()
