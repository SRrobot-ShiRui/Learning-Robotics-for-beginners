# 在ROS下使用传感器（Joystick & RGBD）
## 在ROS中使用游戏手柄

### 一、概述
游戏手柄在ROS中可以作为一个传感器，发布手柄摇杆量和按键状态消息。这些消息可以用于控制机器人或其他设备。

### 二、功能设计
#### 1. 发布摇杆量和按键状态
将手柄摇杆量转化为控制速度发出，话题名称为`SystemState.topics.joy_speed`，消息类型为`state_interfaces::msg::Speed`，当检测到手柄摇杆量变化时发布。

话题名称`SystemState::topics::joy_button`，消息类型`state_interfaces::msg::Button`，当检测到手柄按键变化时发布。
#### 2. 配置文件
ROS内置了`Joy`节点，实时将`/dev/input/js0`的数据转化为`sensor_msgs::Joy`消息。其数据结构如下：

```python
sensor_msgs.msg.Joy(
	header=std_msgs.msg.Header(
		stamp=builtin_interfaces.msg.Time(
			sec=1690353442,
			nanosec=770217921
		),
		frame_id='joy'
	),
	axes=[
		-0.0,   # 左摇杆 x 轴   : 左+ 右-
		-0.0,   # 左摇杆 y 轴   : 上+ 下-
		-0.0,   # 右摇杆 y 轴   : 上+ 下-
		-0.0,   # 右摇杆 x 轴   : 左+ 右-
		0.0,    # 左侧方向键 x 轴: 左+ 右-
		0.0     # 左侧方向键 y 轴: 上+ 下-
	],
	buttons=[
		0,      #  0 右侧按键 1
		0,      #  1 右侧按键 2
		0,      #  2 右侧按键 3
		0,      #  3 右侧按键 4
		0,      #  4 左上侧按键 1
		0,      #  5 右上侧按键 1
		0,      #  6 左上侧按键 2
		0,      #  7 右上侧按键 2
		0,      #  8 select
		0,      #  9 start
		0,      # 10 左摇杆按键
		0       # 11 右摇杆按键
	]
)
```

不同手柄读取的摇杆量和按键状态不同，需要对其进行映射，并统一转化为控制速度和按键消息。映射文件（`.json`）中需要给出的键值，值为下标（`int`）。

## 在ROS中使用RGBD传感器
### 一、概述
RGBD传感器可以提供彩色图像和深度图像，对于实现机器人自主导航、环境感知和3D建模等应用具有重要意义。

### 二、使用方式
#### (一)、 旭日X3派平台
##### 1. 准备工作
1) 确认摄像头正确接入旭日X3派，RGBD模组的接入方式如下图（注意：RGBD模组需要额外转接板才能接到旭日X3派上）。
2) 旭日X3派已烧录好地平线提供的Ubuntu 20.04系统镜像。
3) 旭日X3派已成功安装`tros.b`。
4) 确认PC机能够通过网络访问旭日X3派。
5) PC端需安装`ros2 foxy`版本和`rviz2`，安装命令如下：

```bash
sudo apt install ros-foxy-rviz-common ros-foxy-rviz-default-plugins ros-foxy-rviz2
```
##### 2. 启动hobot_sensor节点
通过SSH登录旭日X3派，并通过下述命令启动`hobot_sensor`节点：

```bash
# 配置 tros.b 环境：
source /opt/tros/local_setup.bash
cp -r /opt/tros/lib/rgbd_sensor/parameter .
# launch 方式启动
ros2 launch rgbd_sensor rgbd_sensor.launch.py
```

 如程序输出如下信息，说明节点已成功启动：

```plaintext
[WARN] [1654573498.706920307] [example]: [wuwl]->This is rgbd!
...
[INFO] [1662723985.860666547] [rgbd_node]: publish camera info.
[INFO] [1662723985.866077156] [rgbd_node]: [pub_ori_pcl]->pub pcl w:h=24192:1,nIdx-24192:sz=24192.
[INFO] [1662723985.876428980] [rgbd_node]: [timer_ros_pub]->pub dep w:h=224:129,sz=982464, infra w:h=224:108, sz=24192.
...
```

通过RViz查看RGBD图像和点云数据。
#### （二）、Tango ROS Streamer
##### 1. 简介
 Tango ROS Streamer是一个用于从Tango设备获取RGBD图像和姿态信息的ROS节点。它能够将Tango的数据流转。
##### 2. 使用方法
安装Tango ROS Streamer：

```bash
sudo apt-get install ros-noetic-tango-ros-streamer
```

启动Tango ROS Streamer：

```bash
roslaunch tango_ros_streamer tango_ros_streamer.launch
```

通过RViz查看RGBD图像和姿态信息。

## 旭日X3派接入RGBD模组需要注意的事项

### 一、硬件连接
#### 确认摄像头正确接入旭日X3派
RGBD模组需要额外的转接板才能接到旭日X3派上。确保转接板和模组连接正确，避免松动或接触不良。
### 二、系统准备
#### 1. 烧录系统镜像
确认旭日X3派已烧录好地平线提供的Ubuntu 20.04系统镜像。
#### 2. 安装tros.b
确认旭日X3派已成功安装`tros.b`。
#### 3. 网络连接
确认PC机能够通过网络访问旭日X3派。
### 三、软件安装
#### 安装ROS 2 Foxy
PC端需安装`ros2 foxy`版本和`rviz2`，安装命令如下：

```bash
sudo apt install ros-foxy-rviz-common ros-foxy-rviz-default-plugins ros-foxy-rviz2
```
### 四、启动hobot_sensor节点
#### 配置环境
通过SSH登录旭日X3派，并配置`tros.b`环境：

```bash
source /opt/tros/local_setup.bash
cp -r /opt/tros/lib/rgbd_sensor/parameter .
```
#### 启动节点
启动`hobot_sensor`节点：

```bash
ros2 launch rgbd_sensor rgbd_sensor.launch.py
```
####  检查节点启动状态
如程序输出如下信息，说明节点已成功启动：

```plaintext
[WARN] [1654573498.706920307] [example]: [wuwl]->This is rgbd!
...
[INFO] [1662723985.860666547] [rgbd_node]: publish camera info.
[INFO] [1662723985.866077156] [rgbd_node]: [pub_ori_pcl]->pub pcl w:h=24192:1,nIdx-24192:sz=24192.
[INFO] [1662723985.876428980] [rgbd_node]: [timer_ros_pub]->pub dep w:h=224:129,sz=982464, infra w:h=224:108, sz=24192.
...
```
### 五、数据预览
#### 查询当前话题
```bash
source /opt/ros/foxy/local_setup.bash
ros2 topic list
```

输出应包含以下话题：

```plaintext
/rgbd_CP3AM/depth/image_rect_raw
/rgbd_CP3AM/depth/color/points
/rgbd_CP3AM/color/camera_info
/rgbd_CP3AM/aligned_depth_to_color/color/points
/rgbd_CP3AM/infra/image_rect_raw
/rgbd_CP3AM/color/image_rect_raw
/parameter_events
/rosout
```
#### 预览摄像头数据
```bash
source /opt/ros/foxy/local_setup.bash
ros2 run rviz2 rviz2
```

在`rviz2`界面上点击`add`按钮，添加`rgbd_sensor`发布的topic（参见目录3所标示的`rgbd_CP3AM`相关topic），订阅点云需要把`rviz2`配置的Global Options里面的选项“Fixed Frame”修改为“depth”，就可以观看实时点云信息。在point话题配置中，里面point type选择`points`即可。
#### 查询相机内参
```bash
source /opt/ros/foxy/local_setup.bash
ros2 topic echo /rgbd_CP3AM/color/camera_info
```
### 六、问题排查
如遇到`hobot_sensor`节点启动异常，可通过以下步骤进行问题排查：

1. 检查硬件连接是否正确。
2. 确认系统镜像和`tros.b`安装是否正确。
3. 检查网络连接是否正常。
4. 查看启动日志，查找具体的错误信息并进行处理。



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