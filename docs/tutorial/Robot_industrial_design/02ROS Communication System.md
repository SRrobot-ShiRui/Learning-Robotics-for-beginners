# ROS架构及通信机制（ROS Communication System）
## 一、ROS文件系统
### （一）概念
ROS文件系统是组织和管理ROS软件包及相关资源的结构。它为ROS的开发和运行提供了基础框架，使得软件包的开发、分发和使用更加规范和高效。
### （二）主要组成部分
#### 1. 工作空间（Workspace）
工作空间是用户进行ROS开发的主要目录。通常，一个工作空间包含多个软件包。可以通过`catkin_make`命令创建和管理工作空间。例如，创建一个名为`my_ws`的工作空间，可以在终端输入：

```bash
mkdir -p ~/my_ws/src
cd ~/my_ws/
catkin_make
```

这样就会在`my_ws`目录下创建一个`src`文件夹用于存放软件包，以及`build`、 `devel`等文件夹用于编译和开发过程中的输出。
#### 2. 软件包（Package）
软件包是ROS中最小的开发单元，包含节点、消息、服务定义、库等资源。每个软件包都有一个`package.xml`文件，用于描述软件包的元信息，如名称、版本、依赖关系等。例如，一个名为`my_package`的软件包的`package.xml`文件可能包含如下内容：

```xml
<package format="2">
  <name>my_package</name>
  <version>0.0.1</version>
  <description>My custom ROS package</description>
  <maintainer email="user@example.com">User Name</maintainer>
  <license>BSD</license>
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>roscpp</build_depend>
  <exec_depend>roscpp</exec_depend>
</package>
```

这表示该软件包名为`my_package`，依赖于`roscpp`库。
#### 3. 元软件包（Metapackage）
元软件包是一个特殊的软件包，它不包含可执行代码，而是用于将多个相关的软件包组织在一起。元软件包通过`package.xml`文件中的`<metapackage/>`标签标识。例如，一个名为`my_metapackage`的元软件包可以包含多个子软件包，方便用户一次性安装和管理这些子软件包。

## 二、计算图
### （一）概念
ROS计算图是由节点、话题、服务和参数等组成的分布式计算架构。它描述了ROS系统中各个组件之间的通信和协作关系，是ROS实现分布式机器人软件开发的核心机制。
### （二）主要组成部分

#### 1. 节点（Node）
#### 定义
节点是ROS中执行特定功能的程序。每个节点可以独立运行，负责完成特定的任务，如传感器数据采集、数据处理、控制命令发布等。节点是ROS计算图的基本单元，通过与其他节点的通信实现复杂的功能。
#### 示例
例如，一个名为`camera_node`的节点负责从摄像头获取图像数据，并将其发布到一个名为`camera_image`的话题上。另一个名为`image_processor_node`的节点订阅`camera_image`话题，对图像数据进行处理，如目标检测、边缘提取等。
### 2. 话题（Topic）
#### 定义
话题是节点之间进行异步通信的渠道。节点可以通过发布（Publish）和订阅（Subscribe）话题来传递息。发布者将消息发送到指定的话题，订阅者从该话题接收消息。这种通信方式是多对多的，一个话题可以有多个发布者和多个订阅者。
#### 示例
在前面的例子中，`camera_node`发布`camera_image`话题，`image_processor_node`订阅该话题。消息类型通常是一个预定义的ROS消息类型，如`sensor_msgs/Image`，用于描述图像数据的格式。
#### 消息类型
ROS提供了丰富的消息类型，用于描述不同类型的数据。例如，`std_msgs`包中包含基本的数据类型消息，如`std_msgs/String`、`std_msgs/Int32`等；`sensor_msgs`包中包含传感器数据类型消息，如`sensor_msgs/Image`、`sensor_msgs/LaserScan`等。用户也可以自定义消息类型，通过创建`.msg`文件来定义新的消息结构。
### 3. 服务（Service）
#### 定义
服务是节点之间进行同步通信的机制。服务调用者（Client）向服务提供者（Server）发送请求，服务提供者处理请求并返回响应。服务通信是请求 - 响应模式，适用于需要即时反馈的场景，如参数查询、命令执行等。
#### 示例
例如，一个名为`robot_control_node`的节点提供一个名为`move_robot`的服务，用于控制机器人的运动。另一个节点可以通过调用`move_robot`服务，发送运动命令（如目标位置、速度等），`robot_control_node`处理这些命令并返回执行结果。
#### 服务类型
ROS提供了多种预定义的服务类型，如`std_srvs`包中的基本服务类型，用户也可以自定义服务类型，通过创建`.srv`文件来定义新的服务结构。例如，一个自定义的服务`MoveRobot.srv`可能包含如下内容：

```plaintext
float64 x
float64 y
---
bool success
string message
```

这表示请求包含两个浮点数`x`和`y`，表示目标位置；响应包含一个布尔值`success`和一个字符串`message`，表示操作是否成功和相关消息。
### 4. 参数（Parameter）
#### 定义
参数是ROS中用于配置节点行为的键值对。参数可以存储在ROS参数服务器上，节点可以通过读取和写入参数来动态调整其行为。参数可以是基本数据类型，如整数、浮点数、字符串等，也可以是复杂的数据结构，如列表、字典等。
#### 示例
例如，一个节点可能需要配置摄像头的分辨率参数。可以在ROS参数服务器上设置一个名为`camera_resolution`的参数，节点在启动时读取该参数，根据参数值调整摄像头的分辨率。参数可以通过命令行、配置文件或节点代码动态设置和读取。

## 三、消息传输机制
### （一）话题通信机制
#### 1. 发布 - 订阅模型
##### 发布者（Publisher）
发布者节点创建一个发布者对象，指定要发布的话题名称和消息类型。发布者定期将消息发送到指定的话题。例如，使用`roscpp`库创建一个发布者：

```cpp
#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "talker");
	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<std_msgs::String>("chatter", 1000);
	ros::Rate rate(10); // 10 Hz

	while (ros::ok())
	{
		std_msgs::String msg;
		msg.data = "hello world";
		pub.publish(msg);
		rate.sleep();
	}

	return 0;
}
```

这个节点每秒发布一次`"hello world"`消息到`chatter`话题。
##### 订阅者（Subscriber）
订阅者节点创建一个订阅者对象，指定要订阅的话题名称和消息类型。订阅者通过回调函数接收消息。例如，使用`roscpp`库创建一个订阅者：

```cpp
#include <ros/ros.h>
#include <std_msgs/String.h>

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
	ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "listener");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe("chatter", 1000, chatterCallback);
	ros::spin();
	return 0;
}
```

这个节点订阅`chatter`话题，每当收到消息时，调用`chatterCallback`函数处理消息。
#### 2. 消息队列
每个订阅者可以设置一个消息队列，用于缓存从发布者接收到的消息。队列的大小可以通过参数设置。如果队列已满，新的消息会替换掉队列中最旧的消息。这可以防止消息丢失，但也会增加内存使用。

#### 3. 连接管理
ROS会自动管理发布者和订阅者之间的连接。当新的订阅者订阅某个话题时，ROS会通知发布者，建立连接。当订阅者取消订阅或关闭时，ROS会断开连接。发布者和订阅者之间通过TCP/IP协议进行通信，确保消息的可靠传输。
### （二）服务通信机制

#### 1. 请求 - 响应模型
##### 服务提供者（Server）
服务提供者节点创建一个服务对象，指定服务名称和类型。服务提供者通过回调函数处理请求并返回响应。例如，使用`roscpp`库创建一个服务提供者：

```cpp
#include <ros/ros.h>
#include <beginner_tutorials/AddTwoInts.h>

bool add(beginner_tutorials::AddTwoInts::Request &req,
		 beginner_tutorials::AddTwoInts::Response &res)
{
	res.sum = req.a + req.b;
	ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
	ROS_INFO("sending back response: [%ld]", (long int)res.sum);
	return true;
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "add_two_ints_server");
	ros::NodeHandle nh;
	ros::ServiceServer service = nh.advertiseService("add_two_ints", add);
	ROS_INFO("Ready to add two ints.");
	ros::spin();
	return 0;
}
```

这个节点提供一个名为`add_two_ints`的服务，处理两个整数的加法请求。
##### 服务调用者（Client）
服务调用者节点创建一个服务客户端对象，指定服务名称和类型。服务调用者通过调用服务并等待响应。例如，使用`roscpp`库创建一个服务调用者：

```cpp
#include <ros/ros.h>
#include <beginner_tutorials/AddTwoInts.h>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "add_two_ints_client");
	ros::NodeHandle nh;
	ros::ServiceClient client = nh.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");

	beginner_tutorials::AddTwoInts srv;
	srv.request.a = 42;
	srv.request.b = 7;

	if (client.call(srv))
	{
		ROS_INFO("Sum: %ld", (long int)srv.response.sum);
	}
	else
	{
		ROS_ERROR("Failed to call service add_two_ints");
		return 1;
	}

	return 0;
}
```

这个节点调用`add_two_ints`服务，发送两个整数`42`和`7`，并接收返回的和。
#### 2. 同步通信
服务通信是同步的，服务调用者在发送请求后会阻塞，直到收到响应。这种机制确保了请求和响应的即时性，适用于需要即时反馈的场景，如参数查询、命令执行等。
#### 3. 服务发现
ROS会自动管理服务提供者和服务调用者之间的连接。当服务调用者调用某个服务时，ROS会查找服务提供者并建立连接。如果服务提供者不存在，调用会失败。服务提供者和调用者之间通过TCP/IP协议进行通信，确保请求和响应的可靠传输。

通过这些机制，ROS实现了节点之间的高效、灵活的通信，支持复杂的机器人应用开发。


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