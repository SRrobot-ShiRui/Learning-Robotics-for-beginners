"""
文 01 付费版配套：log_so3 在 θ→π 边界的压力测试
依赖：numpy
运行：python3 se3_boundary_test.py
"""
import numpy as np

np.set_printoptions(precision=6, suppress=True)


def hat(w):
    return np.array([[0.0, -w[2], w[1]],
                     [w[2], 0.0, -w[0]],
                     [-w[1], w[0], 0.0]])


def vee(W):
    return np.array([W[2, 1], W[0, 2], W[1, 0]])


def exp_so3(w):
    theta = np.linalg.norm(w)
    if theta < 1e-12:
        return np.eye(3) + hat(w)
    k = w / theta
    K = hat(k)
    return np.eye(3) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)


def log_so3(Rm):
    """Shepperd 四元数路径（与主文件一致），全程良态。"""
    tr = np.trace(Rm)
    if tr > 0:
        s = 2.0 * np.sqrt(tr + 1.0)
        qw = 0.25 * s
        qx = (Rm[2, 1] - Rm[1, 2]) / s
        qy = (Rm[0, 2] - Rm[2, 0]) / s
        qz = (Rm[1, 0] - Rm[0, 1]) / s
    else:
        i = int(np.argmax(np.diag(Rm)))
        j, k = (i + 1) % 3, (i + 2) % 3
        s = 2.0 * np.sqrt(1.0 + Rm[i, i] - Rm[j, j] - Rm[k, k])
        qw = (Rm[k, j] - Rm[j, k]) / s
        q = [0.0, 0.0, 0.0]
        q[i] = 0.25 * s
        q[j] = (Rm[j, i] + Rm[i, j]) / s
        q[k] = (Rm[k, i] + Rm[i, k]) / s
        qx, qy, qz = q
    qv = np.array([qx, qy, qz])
    n = np.linalg.norm(qv)
    if n < 1e-12:
        return 2.0 * qv
    theta = 2.0 * np.arctan2(n, abs(qw))
    axis = qv / n * (1.0 if qw >= 0 else -1.0)
    return theta * axis


def test_boundary(n=20000):
    """θ ∈ [π-0.05, π) 随机采样，判据是位姿回代一致（容忍双值）"""
    rng = np.random.default_rng(42)
    fails = []
    param_flips = 0
    for _ in range(n):
        w = rng.normal(size=3)
        w = w / np.linalg.norm(w) * rng.uniform(np.pi - 0.05, np.pi)
        out = log_so3(exp_so3(w))
        if not np.allclose(exp_so3(out), exp_so3(w), atol=1e-9):
            fails.append((w, out))
        # 参数级双值：out 与 w 方向相反也算合法（位姿相同）
        if out @ w < 0 and np.allclose(exp_so3(out), exp_so3(w), atol=1e-9):
            param_flips += 1
    assert not fails, f"{len(fails)} 例位姿回代失败"
    print(f"[boundary] {n} 例边界采样：位姿回代 100% 通过；"
          f"其中 {param_flips} 例参数符号翻转（±π 双值，合法）")


def test_sign_flip():
    """双值性直接验证"""
    w = np.array([np.pi - 1e-7, 0.0, 0.0])
    out = log_so3(exp_so3(w))
    assert abs(abs(out[0]) - np.pi) < 1e-4, out
    assert np.allclose(exp_so3(out), exp_so3(w), atol=1e-9)
    print(f"[sign-flip] θ=π-1e-7 时 log 返回 {out} —— ±π 双值，位姿等价")


def test_perturbation_free_zone():
    """对照：远离边界的正常区，参数回代应严格一致"""
    rng = np.random.default_rng(7)
    worst = 0.0
    for _ in range(20000):
        w = rng.normal(size=3)
        w = w / np.linalg.norm(w) * rng.uniform(0, np.pi - 0.1)
        worst = max(worst, np.linalg.norm(log_so3(exp_so3(w)) - w))
    print(f"[normal-zone] 正常区 20000 例参数往返最大误差 {worst:.2e}（应 ~1e-11 量级）")


def bench():
    """边界分支的正常分支性能对照"""
    import timeit
    ws = []
    rng = np.random.default_rng(1)
    for _ in range(2000):
        w = rng.normal(size=3)
        ws.append(w / np.linalg.norm(w) * rng.uniform(0, np.pi))
    t = timeit.timeit(lambda: [log_so3(exp_so3(w)) for w in ws], number=50) / (50 * len(ws))
    print(f"[bench] exp+log 单次往返平均 {t*1e6:.2f} µs")


if __name__ == "__main__":
    test_boundary()
    test_sign_flip()
    test_perturbation_free_zone()
    bench()
