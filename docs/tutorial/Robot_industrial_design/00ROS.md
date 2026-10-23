# ROS课程介绍

## 课程概述
本课程旨在帮助学生全面了解和掌握机器人操作系统（ROS）的基本原理和应用技术。通过理论与实践相结合的方式，学生将能够快速上手ROS，并在机器人开发中应用所学知识。课程内容涵盖ROS的基本概念、架构、通信机制、包管理、仿真与测试等多个方面，适合不同层次的学习者。

## 课程目标
- 了解ROS的起源、发展历程和基本概念。
- 掌握ROS的核心架构和通信机制。
- 学会创建和管理ROS包，编写和运行ROS节点。
- 熟悉常用的ROS工具和命令，如`roscore`、`rosrun`、`roslaunch`等。
- 学会使用Gazebo进行机器人仿真。
- 掌握ROS中的导航和运动控制功能。
- 学会使用OpenCV和PCL进行计算机视觉和3D感知。


## 第1章：ROS入门
ROS概述
Ubuntu系统安装
ROS环境搭建
虚拟机和Docker的使用


## 第2章：ROS架构及通信机制
ROS文件系统
计算图
节点
话题
服务
参数等概念
消息传输机制


## 第3章：可视化和调试工具
调试ROS节点
日志消息
检测系统状态
设置动态参数
`roswtf`
可视化节点诊断
绘制标量数据图
图像可视化
3D可视化
保存与回放数据
插件


## 第4章：3D建模与仿真
自定义机器人3D模型
创建URDF文件、xacro文件
使用Gazebo进行仿真


## 第5章：导航功能包入门
创建变换
发布传感器消息
里程数据信息
创建基础控制器
创建地图


## 第6章：导航功能包进阶
机器人配置
全局和局部代价地图
rviz详细配置
自适应蒙特卡洛定位
避障
目标发送


## 第7章：使用MoveIt！
机械臂
体系结构
简单运动规划
抓取放置任务


## 第8章：在ROS下使用传感器
使用游戏手柄
使用RGBD传感器


## 第9章：计算机视觉
ROS摄像头驱动
ROS与OpenCV库
标定摄像头
视觉里程计


## 第10章：点云
点云库
可视化点云
滤波和缩减采样
配准与匹配
点云分区


## 课程主要使用命令
### 1. **创建工作空间**
- 新建文件夹并初始化工作空间：`mkdir -p ~/dev/catkin_ws/src`，`cd ~/dev/catkin_ws/src`，`catkin_init_workspace`。

- 编译工作空间：`cd ..`，`catkin_make`。

- 完成配置：`source devel/setup.bash`。

### 2. **创建与编译ROS功能包**
- 使用`catkin_create_pkg`命令创建包：`catkin_create_pkg package_name dependency1 dependency2`。

- 编写节点代码并在`src`目录下保存。

- 修改`CMakeLists.txt`和`package.xml`文件，配置包的依赖和编译选项。

- 使用`catkin_make`或`catkin build`命令构建包。

### 3. **运行节点**
- 使用`rosrun`命令运行节点：`rosrun package_name node_name`。
- 使用`roslaunch`命令运行多个节点及设置运行选项：`roslaunch package_name launch_file.launch`。

### 4. **发布和订阅话题**
- 定义消息类型，创建发布者和订阅者对象。

- 发布者通过`publish`方法发送消息，订阅者通过回调函数处理接收到的消息。

### 5. **使用服务**
- 创建`srv`文件定义服务类型。

- 编写服务端和客户端节点代码。

- 服务端通过`advertiseService`方法提供服务，客户端通过`serviceClient`调用服务。

### 6. **使用参数服务器**
- 使用`rosparam`命令设置和获取参数。

- 在节点中通过`ros::NodeHandle`获取和设置参数。

### 7. **记录和回放数据**
- 使用`rosbag`命令记录数据：`rosbag record topic_name`。

- 使用`rosbag play`命令回放数据：`rosbag play bag_file.bag`。

### 8. **使用Gazebo进行仿真**
- 创建URDF文件描述机器人模型。

- 使用`roslaunch`命令启动Gazebo仿真环境：`roslaunch package_name world.launch`。

- 在仿真环境中控制机器人运动。



## 视频讲解
**BiliBili：** [视睿网络-哔哩哔哩视频 (bilibili.com)](https://space.bilibili.com/1985904092/lists/1497284)

<iframe
  width=auto
  height=auto
  src="//player.bilibili.com/player.html?isOutside=true&aid=230442258&bvid=BV19h411w7rf&cid=1183170164&p=1" 
  scrolling="no" 
  border="0" 
  frameborder="no" 
  framespacing="0" 
  allowfullscreen="true"></iframe>