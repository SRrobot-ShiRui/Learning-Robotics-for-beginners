"""
文 01 配套代码：旋转表示与 SE(3) 的最小实现与验证
依赖：numpy, scipy, matplotlib（均为常见库，无需机器人专用包）

运行：
    python3 se3_demo.py            # 跑全部数值验证
    python3 se3_demo.py --plot     # 额外输出 assets/ 下的图
"""
import numpy as np
from scipy.spatial.transform import Rotation as R

np.set_printoptions(precision=6, suppress=True)


# ---------------------------------------------------------------- 基础工具
def hat(w):
    """so(3) 的 hat 映射：3 维向量 -> 3x3 反对称矩阵"""
    return np.array([[0.0, -w[2], w[1]],
                     [w[2], 0.0, -w[0]],
                     [-w[1], w[0], 0.0]])


def vee(W):
    """hat 的逆映射"""
    return np.array([W[2, 1], W[0, 2], W[1, 0]])


def exp_so3(w):
    """Rodrigues 公式：so(3) -> SO(3)"""
    theta = np.linalg.norm(w)
    if theta < 1e-12:
        return np.eye(3) + hat(w)  # 一阶近似
    k = w / theta
    K = hat(k)
    return np.eye(3) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)


def log_so3(Rm):
    """SO(3) -> so(3)，Shepperd 四元数路径，全程良态。

    不用 trace-arccos：arccos 在 cos→±1 处导数发散，θ 接近 0 或 π 时
    矩阵舍入误差被 1/sinθ 放大。四元数 half-angle 公式
    θ = 2*atan2(||q_v||, |q_w|) 在全区间条件数良好。
    """
    tr = np.trace(Rm)
    if tr > 0:                                   # (S1) qw 最大分支
        s = 2.0 * np.sqrt(tr + 1.0)              # s = 4*qw
        qw = 0.25 * s
        qx = (Rm[2, 1] - Rm[1, 2]) / s
        qy = (Rm[0, 2] - Rm[2, 0]) / s
        qz = (Rm[1, 0] - Rm[0, 1]) / s
    else:                                        # (S2) 按最大对角元选分支
        i = int(np.argmax(np.diag(Rm)))
        j, k = (i + 1) % 3, (i + 2) % 3
        s = 2.0 * np.sqrt(1.0 + Rm[i, i] - Rm[j, j] - Rm[k, k])  # s = 4*q_i
        qw = (Rm[k, j] - Rm[j, k]) / s
        q = [0.0, 0.0, 0.0]
        q[i] = 0.25 * s
        q[j] = (Rm[j, i] + Rm[i, j]) / s
        q[k] = (Rm[k, i] + Rm[i, k]) / s
        qx, qy, qz = q
    qv = np.array([qx, qy, qz])
    n = np.linalg.norm(qv)
    if n < 1e-12:                                # θ≈0，q_v 本身就是 θ/2 阶近似
        return 2.0 * qv
    theta = 2.0 * np.arctan2(n, abs(qw))         # (S3) half-angle，θ∈[0,π]
    axis = qv / n * (1.0 if qw >= 0 else -1.0)   # (S4) 负半球时轴取反
    return theta * axis


def exp_se3(xi):
    """SE(3) 指数映射：xi = [rho(3), phi(3)]，顺序为 twist 平移在前、旋转在后"""
    rho, phi = xi[:3], xi[3:]
    theta = np.linalg.norm(phi)
    if theta < 1e-12:
        J = np.eye(3) + 0.5 * hat(phi)
    else:
        K = hat(phi)
        J = (np.eye(3)
             + (1 - np.cos(theta)) / theta**2 * K
             + (theta - np.sin(theta)) / theta**3 * (K @ K))
    T = np.eye(4)
    T[:3, :3] = exp_so3(phi)
    T[:3, 3] = J @ rho
    return T


def log_se3(T):
    """SE(3) 对数映射"""
    Rm, t = T[:3, :3], T[:3, 3]
    phi = log_so3(Rm)
    theta = np.linalg.norm(phi)
    if theta < 1e-12:
        J_inv = np.eye(3) - 0.5 * hat(phi)
    else:
        K = hat(phi)
        J_inv = (np.eye(3)
                 - 0.5 * K
                 + (1.0 / theta**2 - (1 + np.cos(theta)) / (2 * theta * np.sin(theta)))
                 * (K @ K))
    return np.concatenate([J_inv @ t, phi])


# ---------------------------------------------------- 验证 1：旋转矩阵的自由度
def check_dof():
    """用数值雅可比证明：SO(3) 局部只有 3 个自由度"""
    np.random.seed(0)
    Rm = exp_so3(np.array([0.3, -1.2, 2.0]))
    eps = 1e-7
    cols = []
    for i in range(9):                     # 对 9 个元素逐个扰动
        dR = np.zeros(3)
        # 用“扰动的 9 维方向”构造矩阵，再投影回切空间
    # 更直接的做法：对 3 个旋转参数求导，看切空间维数
    for i in range(3):
        d = np.zeros(3)
        d[i] = eps
        cols.append((Rm @ exp_so3(d) - Rm @ exp_so3(-d)) / (2 * eps))
    J = np.stack([c.reshape(-1) for c in cols], axis=1)   # 9x3
    rank = np.linalg.matrix_rank(J, tol=1e-6)
    print(f"[1] 切空间数值雅可比 shape={J.shape}, rank={rank}  -> 只有 3 个方向可动，"
          f"另外 6 个方向被正交性约束锁死")


# ------------------------------------- 验证 2：指数/对数映射互为逆（含边界）
def check_exp_log_roundtrip():
    np.random.seed(1)
    err = 0.0
    for _ in range(2000):
        w = np.random.randn(3)
        w = w / np.linalg.norm(w) * np.random.uniform(0, np.pi - 1e-3)
        err = max(err, np.linalg.norm(log_so3(exp_so3(w)) - w))
    # 接近 pi 的难例
    w_hard = np.array([np.pi - 1e-7, 0, 0])
    err_hard = np.linalg.norm(log_so3(exp_so3(w_hard)) - w_hard)
    print(f"[2] SO(3) exp->log 往返最大误差 {err:.2e}；接近 pi 的难例误差 {err_hard:.2e}")
    print("    注意：接近 pi 时 log 的符号会翻转（+pi 与 -pi 是同一个旋转），"
          "这是优化里出现跳变的常见来源")

    # 逐步观察：小角度应该正常，大角度才暴露问题
    for ang in [0.3, 1.0, 2.0, 3.0]:
        ax_ = np.array([0.3, 0.5, -0.8])
        ax_ = ax_ / np.linalg.norm(ax_) * ang
        xi = np.concatenate([[0.4, -0.2, 0.1], ax_])
        out = log_se3(exp_se3(xi))
        same_pose = np.allclose(exp_se3(out), exp_se3(xi), atol=1e-9)
        print(f"    |phi|={ang:.1f}: 回代后位姿一致={same_pose}, "
              f"参数差={np.linalg.norm(out - xi):.3f}")
    print("    说明：SE(3) 的 log 在 |phi| 接近 pi 时参数不唯一，"
          "但位姿仍然一致 —— 优化时用位姿残差而不是参数残差")


# ------------------------------ 验证 3：左扰动 vs 右扰动，作用方向不同
def check_perturbation():
    T = exp_se3(np.array([0.2, 0.0, 0.1, 0.1, 0.2, -0.3]))
    d = np.array([0, 0, 0, 0, 0, 0.1])          # 只有绕 z 的旋转扰动

    left = exp_se3(d) @ T        # 左乘：扰动在“世界系”
    right = T @ exp_se3(d)       # 右乘：扰动在“本体系”

    # 观察平移分量的变化：左乘会同时改变平移，右乘不会
    d_left = (left - T)[:3, 3]
    d_right = (right - T)[:3, 3]
    print(f"[4] 左扰动引起的平移变化 : {d_left}  (非零，因为绕世界原点转)")
    print(f"    右扰动引起的平移变化 : {d_right} (为零，绕本体自身轴转不改变位置)")
    print("    这就是为什么状态估计里几乎总用右扰动：更新量只影响姿态，"
          "不会把位置的估计一起带偏")


# ---------------------- 验证 4：同一旋转的三种表示，误差如何随角度放大
def check_representation_error(max_deg=90, n=200):
    """绕一个倾斜轴旋转，比较两种插值方式在“中点”处偏离真实半程旋转多少度"""
    axis = np.array([0.6, 0.5, 0.62])
    axis /= np.linalg.norm(axis)          # 倾斜轴：让三个欧拉角同时变化
    angles = np.linspace(1, max_deg, n)
    err_mat, err_euler, err_quat = [], [], []
    e0 = R.from_matrix(np.eye(3)).as_euler("ZYX")

    for deg in angles:
        t = np.deg2rad(deg)
        true_R = exp_so3(axis * t)
        target = exp_so3(axis * t / 2)     # 真实“半程”旋转

        def dev(Rx):
            d = Rx.T @ target
            return np.rad2deg(np.arccos(np.clip((np.trace(d) - 1) / 2, -1, 1)))

        # (a) 矩阵逐元素线性混合：结果不再是旋转矩阵
        half = 0.5 * np.eye(3) + 0.5 * true_R
        u, _, vt = np.linalg.svd(half)
        err_mat.append(dev(u @ vt))        # 最近正交矩阵

        # (b) 欧拉角线性插值
        e1 = R.from_matrix(true_R).as_euler("ZYX")
        err_euler.append(dev(R.from_euler("ZYX", 0.5 * (e0 + e1)).as_matrix()))

        # (c) 四元数插值（slerp 的常规做法：归一化线性插值 nlerp）
        q0 = R.from_matrix(np.eye(3)).as_quat()
        q1 = R.from_matrix(true_R).as_quat()
        if q0 @ q1 < 0:                    # 处理双覆盖
            q1 = -q1
        qh = 0.5 * q0 + 0.5 * q1
        err_quat.append(dev(R.from_quat(qh / np.linalg.norm(qh)).as_matrix()))

    i = -1
    print(f"[5] 绕倾斜轴转到 {max_deg}° 时，半程旋转的角度偏差：")
    print(f"    矩阵线性混合 {'(SVD 投影后)':<10} {err_mat[i]:7.3f}°")
    print(f"    欧拉角线性插值{'':<8} {err_euler[i]:7.3f}°")
    print(f"    四元数归一化插值{'':<6} {err_quat[i]:7.3f}°  <- 应接近 0")
    return angles, err_mat, err_euler, err_quat


def plot_representation(angles, err_mat, err_euler, err_quat):
    import os
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs("../assets", exist_ok=True)
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=170)
    ax.plot(angles, err_mat, label="matrix linear blend")
    ax.plot(angles, err_euler, label="euler angle blend (ZYX)")
    ax.plot(angles, err_quat, "--", label="quaternion nlerp")
    ax.set_xlabel("rotation angle of the motion (deg)")
    ax.set_ylabel("angular error at midpoint (deg)")
    ax.set_title("How far does naive interpolation drift from the true half-way pose?")
    ax.legend(frameon=False)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig("../assets/fig01-interp-error.png")
    print("    图已保存到 assets/fig01-interp-error.png")


if __name__ == "__main__":
    import sys
    check_dof()
    check_exp_log_roundtrip()
    check_perturbation()
    res = check_representation_error()
    if "--plot" in sys.argv:
        plot_representation(*res)
