# 可视化和调试工具（ROS Visualization）

## 一、调试ROS节点
### （一）使用`roslaunch`和`rosrun`的调试选项
#### 1. `rosrun`
`rosrun`命令用于运行单个节点。可以通过添加`--ros-args`和`- - log-level`选项来设置日志级别。例如：

```bash
rosrun my_package my_node --ros-args --log-level=debug
```

这会将节点的日志级别设置为调试模式，输出更详细的信息。
#### 2. `roslaunch`
`roslaunch`命令用于启动多个节点和配置文件。可以通过在`launch`文件中设置`<node>`标签的`output`属性来控制日志输出。例如：

```xml
<node name="my_node" pkg="my_package" type="my_node" output="screen" />
```

这会将节点的输出直接显示在终端屏幕上。还可以使用`--screen`选项在命令行中查看节点输出：

```bash
roslaunch my_package my_launch.launch --screen
```
### （二）使用`gdb`和`valgrind`
#### 1. `gdb`
`gdb`是一个强大的调试工具，可以用于调试C++编写的ROS节点。可以通过`rosrun`或`roslaunch`的`--prefix`选项来启动`gdb`。例如：

```bash
rosrun --prefix "gdb --args" my_package my_node
```

这会启动`gdb`并加载节点程序，可以在`gdb`中设置断点、单步执行等。
#### 2. `valgrind`
`valgrind`是一个内存检测工具，可以用于检测内存泄漏和内存错误。同样可以通过`--prefix`选项启动`valgrind`。例如：

```bash
rosrun --prefix "valgrind" my_package my_node
```

## 二、日志消息
### （一）日志级别
ROS提供了多种日志级别，用于控制日志输出的详细程度：

- `DEBUG`：最详细的信息，用于调试。

- `INFO`：一般的信息，用于正常运行时的输出。

- `WARN`：警告信息，表示可能的问题。

- `ERROR`：错误信息，表示严重的问题。

- `FATAL`：致命错误，通常会导致节点崩溃。
### （二）日志输出
在C++中，可以使用`ROS_*`宏来输出日志信息。例如：

```cpp
ROS_DEBUG("This is a debug message");
ROS_INFO("This is an info message: %d", value);
ROS_WARN("This is a warning message");
ROS_ERROR("This is an error message");
ROS_FATAL("This is a fatal error message");
```

在Python中，可以使用`rospy.log*`函数来输出日志信息。例如：

```python
rospy.logdebug("This is a debug message")
rospy.loginfo("This is an info message: %d", value)
rospy.logwarn("This is a warning message")
rospy.logerr("This is an error message")
rospy.logfatal("This is a fatal error message")
```

## 三、检测系统状态

### （一）使用`rosnode`命令
#### 1. 查看节点列表
`rosnode list`命令可以列出当前运行的所有节点。例如：

```bash
rosnode list
```
#### 2. 查看节点信息
`rosnode info`命令可以查看特定节点的详细信息，包括订阅和发布的话题、服务等。例如：

```bash
rosnode info /my_node
```
### （二）使用`rostopic`命令
#### 1. 查看话题列表
`rostopic list`命令可以列出当前所有的话题。例如：

```bash
rostopic list
```
#### 2. 查看话题信息
`rostopic info`命令可以查看特定话题的详细信息，包括发布者和订阅者。例如：

```bash
rostopic info /my_topic
```
#### 3. 查看话题消息
`rostopic echo`命令可以实时查看话题的消息内容。例如：

```bash
rostopic echo /my_topic
```
### （三）使用`rosservice`命令
#### 1. 查看服务列表
`rosservice list`命令可以列出当前所有可用的服务。例如：

```bash
rosservice list
```
#### 2. 查看服务信息
`rosservice info`命令可以查看特定服务的详细信息，包括服务类型和提供者。例如：

```bash
rosservice info /my_service
```

## 四、设置动态参数
### （一）使用`dynamic_reconfigure`库
#### 1. 创建配置文件
在ROS包中创建一个`cfg`目录，用于存放配置文件。例如，创建一个`MyConfig.cfg`文件：

```python
#! /usr/bin/env python
PACKAGE = "my_package"

from dynamic_reconfigure.parameter_generator_catkin import *

gen = ParameterGenerator()
gen.add("int_param", int_t, 0, "An integer parameter", 42, 0, 100)
gen.add("double_param", double_t, 0, "A double parameter", 1.0, 0.0, 10.0)
gen.add("str_param", str_t, 0, "A string parameter", "hello")
gen.add("bool_param", bool_t, 0, "A boolean parameter", True)

exit(gen.generate(PACKAGE, "my_package", "MyConfig"))
```
#### 2. 生成配置文件
在`CMakeLists.txt`文件中添加以下内容：

```cmake
generate_dynamic_reconfigure_options(
  cfg/MyConfig.cfg
  DEPENDENCIES other_package
)
```

运行`catkin_make`生成配置文件。
#### 3. 在节点中使用动态参数
在C++节点中，可以使用`dynamic_reconfigure::Server`类来处理动态参数。例如：

```cpp
#include <dynamic_reconfigure/server.h>
#include <my_package/MyConfig.h>

void callback(my_package::MyConfig &config, uint32_t level)
{
	ROS_INFO("Reconfigure Request: %d %f %s %s %d",
			 config.int_param, config.double_param, config.str_param.c_str(),
			 config.bool_param ? "True" : "False", config.size);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "my_node");
	dynamic_reconfigure::Server<my_package::MyConfig> server;
	dynamic_reconfigure::Server<my_package::MyConfig>::CallbackType f;
	f = boost::bind(&callback, _1, _2);
	server.setCallback(f);
	ros::spin();
	return 0;
}
```

在Python节点中，可以使用`dynamic_reconfigure.server`模块来处理动态参数。例如：

```python
import rospy
from dynamic_reconfigure.server import Server
from my_package.cfg import MyConfig

def callback(config, level):
	rospy.loginfo("""Reconfigure Request: {int_param}, {double_param},\ 
		  {str_param}, {bool_param}, {size}""".format(**config))
	return config

if __name__ == "__main__":
	rospy.init_node("my_node", anonymous=True)
	srv = Server(MyConfig, callback)
	rospy.spin()
```

## 五、`roswtf`
### （一）概念
`roswtf`是一个用于检测ROS系统问题的工具。它可以检查节点、话题、服务等的配置和运行状态，帮助开发者发现潜在的问题。
### （二）运行`roswtf`
在终端中输入以下命令：

```bash
roswtf
```

`roswtf`会检查当前运行的ROS系统，输出潜在的问题和建议。

## 六、可视化节点诊断
### （一）使用`rqt`工具
#### 1. 安装`rqt`
```bash
sudo apt-get install ros-noetic-rqt
```
#### 2. 启动`rqt`
```bash
rqt
```
#### 3. 常用插件
- **`rqt_graph`**：显示ROS计算图，包括节点、话题、服务等的连接关系。

- **`rqt_console`**：显示节点的日志信息。

- **`rqt_plot`**：绘制标量数据图。

- **`rqt_image_view`**：显示图像数据。

- **`rqt_tf_tree`**：显示TF树结构。

## 七、绘制标量数据图
### （一）使用`rqt_plot`
#### 1. 启动`rqt_plot`
```bash
rqt_plot
```
#### 2. 选择话题
在`rqt_plot`窗口中，选择要绘制的话题。例如，选择`/my_topic/data`，可以实时绘制该话题的标量数据。
### （二）使用`plotjuggler`
#### 1. 安装`plotjuggler`
```bash
sudo apt-get install ros-noetic-plotjuggler
```
#### 2. 启动`plotjuggler`
```bash
plotjuggler
```
#### 3. 选择话题
在`plotjuggler`窗口中，选择要绘制的话题，可以实时绘制该话题的标量数据，并支持多种图表类型和数据处理功能。

## 八、图像可视化
### （一）使用`rqt_image_view`
#### 1. 启动`rqt_image_view`
```bash
rqt_image_view
```
#### 2. 选择话题
在`rqt_image_view`窗口中，选择要显示的图像话题。例如，选择`/camera/image_raw`，可以实时显示摄像头捕获的图像。
### （二）使用`image_view`节点
#### 1. 安装`image_view`
```bash
sudo apt-get install ros-noetic-image-view
```
#### 2. 启动`image_view`节点
```bash
rosrun image_view image_view image:=/camera/image_raw
```

这会打开一个窗口，实时显示`/camera/image_raw`话题的图像数据。

## 九、3D可视化rviz
`rviz`是一个3D可视化工具，可以用于显示机器人模型、传感器数据、路径规划等。
#### 1. 安装`rviz`
```bash
sudo apt-get install ros-noetic-rviz
```
#### 2. 启动`rviz`
```bash
rviz
```
#### 3. 配置显示
在`rviz`窗口中，可以添加多种显示类型，如`PointCloud`、`LaserScan`、`RobotModel`等。通过配置这些显示类型，可以实时查看3D数据。

## 十、保存与回放数据---rosbag工具
#### 1. 录制数据
```bash
rosbag record /my_topic /another_topic
```
这会将指定话题的数据录制到一个`.bag`文件中。
#### 2. 回放数据
```bash
rosbag play my_bag.bag
```
 这会将录制的数据重新发布到ROS系统中，可以用于测试和调试。

## 十一、插件
### （一）概念
ROS支持多种插件，用于扩展功能。插件可以是节点、库、工具等，可以通过安装和配置来使用。
### （二）常用插件
#### 1. `rqt`插件
`rqt`提供了多种插件，如`rqt_graph`、`rqt_console`、`rqt_plot`等，可以通过`rqt`的插件管理器安装和配置。
#### 2. `rviz`插件
`rviz`支持多种插件，如`rviz_plugin_tutorials`，可以通过安装和配置来扩展`rviz`的功能。
#### 3. `rosbag`插件
`rosbag`支持多种插件，如`rosbag_filter`，可以通过安装和配置来过滤和处理录制的数据。



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