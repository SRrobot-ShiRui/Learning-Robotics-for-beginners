# 3D建模与仿真（ROS URDF & Gazebo）

## 一、创建URDF文件
### （一）URDF简介
URDF（Unified Robot Description Format）是一种用于描述机器人模型的XML格式文件。它定义了机器人的各个部件（links）和连接这些部件的关节（joints），以及它们的物理和视觉属性。
### （二）基本结构
一个URDF文件通常包含以下部分：

- **声明XML版本**：

```xml
<?xml version="1.0" ?>
```

- **定义机器人**：

```xml
<robot name="my_robot">
```

- **定义部件（Link）**：

```xml
<link name="base_link">
	<visual>
		<origin xyz="0 0 0" rpy="0 0 0" />
		<geometry>
			<box size="0.1 0.1 0.1" />
		</geometry>
		<material name="red">
			<color rgba="1 0 0 1"/>
		</material>
	</visual>
</link>
```

- **定义关节（Joint）**：

```xml
<joint name="joint1" type="revolute">
	<origin xyz="0 0 0.1" rpy="0 0 0" />
	<parent link="base_link"/>
	<child link="link1"/>
	<axis xyz="0 0 1"/>
	<limit lower="-3.14" upper="3.14" effort="10" velocity="1"/>
</joint>
```

- **结束机器人定义**：

```xml
</robot>
```

## 二、使用Xacro文件
### （一）Xacro简介
Xacro（XML Macros）是一种用于生成URDF文件的宏语言。它允许在URDF文件中使用变量、宏、条件语句等，使得模型的描述更加灵活和模块化。
### （二）基本结构
一个Xacro文件通常包含以下部分：

- **声明XML版本和Xacro命名空间**：

```xml
<?xml version="1.0" ?>
<robot name="my_robot" xmlns:xacro="http://www.ros.org/wiki/xacro">
```

- **定义属性（Property）**：

```xml
<xacro:property name="M_PI" value="3.1415926" />
<xacro:property name="wheel_radius" value="0.06" />
```

- **定义宏（Macro）**：

```xml
<xacro:macro name="wheel" params="prefix reflect">
	<joint name="${prefix}_wheel_joint" type="continuous">
		<origin xyz="${wheel_joint_x} ${reflect*wheel_joint_y} ${-wheel_joint_z}" rpy="0 0 0" />
		<parent link="base_link" />
		<child link="${prefix}_wheel_link" />
		<axis xyz="0 1 0" />
	</joint>
	<link name="${prefix}_wheel_link">
		<visual>
			<origin xyz="0 0 0" rpy="${M_PI/2} 0 0"/>
			<geometry>
				<cylinder length="${wheel_length}" radius="${wheel_radius}"/>
			</geometry>
			<material name="white" />
		</visual>
	</link>
</xacro:macro>
```

- **调用宏**：

```xml
<xacro:wheel prefix="left"  reflect="1"/>
<xacro:wheel prefix="right"  reflect="-1"/>
```

- **结束机器人定义**：

```xml
</robot>
```
### （三）转换Xacro文件为URDF
```bash
xacro my_robot.xacro > my_robot.urdf
```

## 三、使用Gazebo进行仿真
### （一）安装Gazebo
```bash
sudo apt-get install ros-noetic-gazebo-ros-pkgs
sudo apt-get install ros-noetic-gazebo-ros-control
```
### （二）启动Gazebo
```bash
roscore
rosrun gazebo_ros gazebo
```
### （三）加载机器人模型
1. **使用`spawn_entity.py`脚本加载URDF模型**：

```bash
rosrun gazebo_ros spawn_entity.py -entity my_robot -file my_robot.urdf -x 0 -y 0 -z 0.5
```
2. **使用`robot_state_publisher`发布模型描述**：

```bash
rosparam load my_robot.urdf robot_description
rosrun robot_state_publisher robot_state_publisher
```
### （四）配置Gazebo属性和控制器插件
在URDF文件中添加Gazebo属性和控制器插件：

```xml
<gazebo>
    <plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">
        <robotNamespace>/my_robot</robotNamespace>
    </plugin>
</gazebo>
```
### （五）创建自定义环境
在功能包中新建一个`world`文件夹，放入自定义的环境模型文件`myworld.world`，并通过命令启动：

```bash
gazebo --verbose -s libgazebo_ros_init.so -s libgazebo_ros_factory.so $(find mbot_description)/worlds/myworld.world
```
### （六）使用Launch文件启动Gazebo并加载模型
创建一个Launch文件`display_mbot_xacro.launch`：

```xml
<launch>
    <arg name="model" default="$(find xacro)/xacro '$(find mbot_description)/urdf/mbot_base.xacro'" />
    <param name="robot_description" command="$(arg model)" />
    <param name="use_gui" value="true"/>
    <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />
    <node name="spawn_entity" pkg="gazebo_ros" type="spawn_entity.py" args="-entity my_robot -file $(find mbot_description)/urdf/mbot_base.urdf -x 0 -y 0 -z 0.5" />
</launch>
```

启动Launch文件：

```bash
roslaunch mbot_description display_mbot_xacro.launch
```



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