# SRrobot 视睿机器人 | 机器人学习知识库与《机器人炼金术》专栏

> **把数学、机械、代码和物理，炼成会动的东西。**

面向机器人学习者与从业者的系统化中文知识库：从 Arduino 入门到人形机器人前沿，覆盖数学基础、运动学、动力学、控制、状态估计与具身智能。

**在线阅读**：https://srrobot-shirui.github.io/Learning-Robotics-for-beginners/

## 这是什么

本仓库是「SRrobot 视睿机器人」知识库的 **MkDocs 源工程**，包含两大板块：

### 1. 机器人编程教程（入门 → 高级）

- **Arduino 系列**：C/C++ 与 Arduino 代码区别、数字/模拟信号读写、PWM、中断、I2C/SPI 等，每个例程配完整代码与接线说明
- **学习路径**：入门篇（点亮 LED、串口通信）→ 实践篇（传感器与执行器）→ 进阶篇（ROS 与运动控制）→ 高级篇（SLAM 与自主导航）

### 2. 《机器人炼金术》专栏（周更）

每周两篇的机器人学系统专栏，两条主线：

- **理论主线**：位姿与李群（SE(3)）→ 运动学 → 动力学与接触力学 → 最优控制 → 状态估计 → 系统工程，每篇配可运行 Python 代码与数值实验
- **前沿主线**：人形机器人产业数据解读、VLA 视觉-语言-动作模型、世界模型、具身智能论文精读，全部标注信源与可信度评级

## 适合谁读

- 想入门机器人编程的学生和转行者（从 Arduino 零基础开始）
- 机械/自动化/计算机专业学生（需要系统的机器人学数学基础）
- 具身智能从业者（需要前沿模型解读与可复现的代码实现）

## 快速开始

```bash
# 本地构建本站
git clone https://github.com/SRrobot-ShiRui/Learning-Robotics-for-beginners.git
cd Learning-Robotics-for-beginners
pip install mkdocs mkdocs-material pymdown-extensions
mkdocs serve        # 浏览器打开 http://127.0.0.1:8000
```

## 关键词

机器人学 · robotics · 人形机器人 · humanoid robot · 具身智能 · embodied AI · 李群李代数 · SE(3) · 旋转矩阵 · 四元数 · 运动学 · 动力学 · MPC · 状态估计 · 卡尔曼滤波 · SLAM · VLA 模型 · Arduino 教程 · ROS · MkDocs 知识库

## 相关链接

- CSDN 完整版专栏（含完整可用代码）：https://blog.csdn.net/2301_81238088/category_13220213.html
- 仓库问题反馈：[Issues](https://github.com/SRrobot-ShiRui/Learning-Robotics-for-beginners/issues)

## 许可与引用

文章原创，欢迎在注明出处（SRrobot 视睿机器人 + 本仓库链接）的前提下转载与教学使用。
