# 导航功能包入门（Transform system）

## 一、创建变换（TF）
### （一）TF简介
TF（Transform）是ROS中用于管理坐标变换的工具。它允许节点在不同的坐标系之间进行转换，常用于机器人导航、传感器数据融合等任务。
### （二）发布TF
#### C++示例
在C++中，可以使用`tf2_ros`库来发布TF。例如，发布一个从`base_link`到`laser`的变换：

```cpp
#include <ros/ros.h>
#include <tf2_ros/transform_broadcaster.h>
#include <geometry_msgs/TransformStamped.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "tf_broadcaster");
	ros::NodeHandle nh;

	tf2_ros::TransformBroadcaster br;
	geometry_msgs::TransformStamped transformStamped;

	transformStamped.header.stamp = ros::Time::now();
	transformStamped.header.frame_id = "base_link";
	transformStamped.child_frame_id = "laser";

	transformStamped.transform.translation.x = 0.0;
	transformStamped.transform.translation.y = 0.0;
	transformStamped.transform.translation.z = 0.5;

	transformStamped.transform.rotation.x = 0.0;
	transformStamped.transform.rotation.y = 0.0;
	transformStamped.transform.rotation.z = 0.0;
	transformStamped.transform.rotation.w = 1.0;

	ros::Rate rate(10.0);
	while (ros::ok()) {
		br.sendTransform(transformStamped);
		rate.sleep();
	}

	return 0;
}
```
#### Python示例
在Python中，可以使用`tf2_ros`库来发布TF。例如，发布一个从`base_link`到`laser`的变换：

```python
import rospy
import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
	rospy.init_node('tf_broadcaster')
	br = tf2_ros.TransformBroadcaster()
	rate = rospy.Rate(10.0)

	while not rospy.is_shutdown():
		t = geometry_msgs.msg.TransformStamped()
		t.header.stamp = rospy.Time.now()
		t.header.frame_id = "base_link"
		t.child_frame_id = "laser"

		t.transform.translation.x = 0.0
		t.transform.translation.y = 0.0
		t.transform.translation.z = 0.5

		t.transform.rotation.x = 0.0
		t.transform.rotation.y = 0.0
		t.transform.rotation.z = 0.0
		t.transform.rotation.w = 1.0

		br.sendTransform(t)
		rate.sleep()
```
### （三）监听TF
####  C++示例
在C++中，可以使用`tf2_ros`库来监听TF。例如，监听从`base_link`到`laser`的变换：

```cpp
#include <ros/ros.h>
#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/TransformStamped.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "tf_listener");
	ros::NodeHandle nh;

	tf2_ros::Buffer tfBuffer;
	tf2_ros::TransformListener tfListener(tfBuffer);

	ros::Rate rate(10.0);
	while (ros::ok()) {
		try {
			geometry_msgs::TransformStamped transformStamped;
			transformStamped = tfBuffer.lookupTransform("base_link", "laser", ros::Time(0));
			ROS_INFO("Laser is at (%.2f, %.2f, %.2f) relative to base_link",
					 transformStamped.transform.translation.x,
					 transformStamped.transform.translation.y,
					 transformStamped.transform.translation.z);
		} catch (tf2::TransformException &ex) {
			ROS_WARN("%s", ex.what());
			rate.sleep();
			continue;
		}

		rate.sleep();
	}

	return 0;
}
```
#### Python示例
 在Python中，可以使用`tf2_ros`库来监听TF。例如，监听从`base_link`到`laser`的变换：

```python
import rospy
import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
	rospy.init_node('tf_listener')
	tfBuffer = tf2_ros.Buffer()
	listener = tf2_ros.TransformListener(tfBuffer)

	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():
		try:
			trans = tfBuffer.lookup_transform('base_link', 'laser', rospy.Time())
			rospy.loginfo("Laser is at (%.2f, %.2f, %.2f) relative to base_link",
						  trans.transform.translation.x,
						  trans.transform.translation.y,
						  trans.transform.translation.z)
		except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
			rospy.logwarn("%s", e)
			rate.sleep()
			continue

		rate.sleep()
```

## 二、发布传感器消息
### （一）发布LaserScan消息
#### C++示例
在C++中，可以使用`sensor_msgs`库来发布LaserScan消息。例如，发布一个LaserScan消息：

```cpp
#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "laser_publisher");
	ros::NodeHandle nh;

	ros::Publisher laser_pub = nh.advertise<sensor_msgs::LaserScan>("scan", 50);

	sensor_msgs::LaserScan scan;
	scan.header.frame_id = "laser";
	scan.angle_min = -1.57;
	scan.angle_max = 1.57;
	scan.angle_increment = 0.01;
	scan.time_increment = 0.0;
	scan.scan_time = 0.1;
	scan.range_min = 0.1;
	scan.range_max = 10.0;

	scan.ranges.resize(314);
	scan.intensities.resize(314);

	ros::Rate rate(10.0);
	while (ros::ok()) {
		scan.header.stamp = ros::Time::now();
		for (size_t i = 0; i < scan.ranges.size(); ++i) {
			scan.ranges[i] = 1.0;  // 示例数据
			scan.intensities[i] = 0.5;  // 示例数据
		}

		laser_pub.publish(scan);
		rate.sleep();
	}

	return 0;
}
```
#### Python示例
在Python中，可以使用`sensor_msgs`库来发布LaserScan消息。例如，发布一个LaserScan消息：

```python
import rospy
from sensor_msgs.msg import LaserScan

if __name__ == '__main__':
	rospy.init_node('laser_publisher')
	laser_pub = rospy.Publisher('scan', LaserScan, queue_size=50)

	scan = LaserScan()
	scan.header.frame_id = 'laser'
	scan.angle_min = -1.57
	scan.angle_max = 1.57
	scan.angle_increment = 0.01
	scan.time_increment = 0.0
	scan.scan_time = 0.1
	scan.range_min = 0.1
	scan.range_max = 10.0

	scan.ranges = [1.0] * 314
	scan.intensities = [0.5] * 314

	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():
		scan.header.stamp = rospy.Time.now()
		laser_pub.publish(scan)
		rate.sleep()
```
### （二）发布Imu消息
#### C++示例
在C++中，可以使用`sensor_msgs`库来发布Imu消息。例如，发布一个Imu消息：

```cpp
#include <ros/ros.h>
#include <sensor_msgs/Imu.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "imu_publisher");
	ros::NodeHandle nh;

	ros::Publisher imu_pub = nh.advertise<sensor_msgs::Imu>("imu", 50);

	sensor_msgs::Imu imu;
	imu.header.frame_id = "imu_link";
	imu.linear_acceleration.x = 0.0;
	imu.linear_acceleration.y = 0.0;
	imu.linear_acceleration.z = 9.81;
	imu.angular_velocity.x = 0.0;
	imu.angular_velocity.y = 0.0;
	imu.angular_velocity.z = 0.0;

	ros::Rate rate(10.0);
	while (ros::ok()) {
		imu.header.stamp = ros::Time::now();
		imu_pub.publish(imu);
		rate.sleep();
	}

	return 0;
}
```
#### Python示例
在Python中，可以使用`sensor_msgs`库来发布Imu消息。例如，发布一个Imu消息：

```python
import rospy
from sensor_msgs.msg import Imu

if __name__ == '__main__':
	rospy.init_node('imu_publisher')
	imu_pub = rospy.Publisher('imu', Imu, queue_size=50)

	imu = Imu()
	imu.header.frame_id = 'imu_link'
	imu.linear_acceleration.x = 0.0
	imu.linear_acceleration.y = 0.0
	imu.linear_acceleration.z = 9.81
	imu.angular_velocity.x = 0.0
	imu.angular_velocity.y = 0.0
	imu.angular_velocity.z = 0.0

	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():
		imu.header.stamp = rospy.Time.now()
		imu_pub.publish(imu)
		rate.sleep()
```

## 三、发布里程数据信息
### （一）发布Odometry消息
####  C++示例
在C++中，可以使用`nav_msgs`库来发布Odometry消息。例如，发布一个Odometry消息：

```cpp
#include <ros/ros.h>
#include <nav_msgs/Odometry.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "odometry_publisher");
	ros::NodeHandle nh;

	ros::Publisher odom_pub = nh.advertise<nav_msgs::Odometry>("odom", 50);

	nav_msgs::Odometry odom;
	odom.header.frame_id = "odom";
	odom.child_frame_id = "base_link";
	odom.pose.pose.position.x = 0.0;
	odom.pose.pose.position.y = 0.0;
	odom.pose.pose.position.z = 0.0;
	odom.pose.pose.orientation.x = 0.0;
	odom.pose.pose.orientation.y = 0.0;
	odom.pose.pose.orientation.z = 0.0;
	odom.pose.pose.orientation.w = 1.0;
	odom.twist.twist.linear.x = 0.0;
	odom.twist.twist.linear.y = 0.0;
	odom.twist.twist.linear.z = 0.0;
	odom.twist.twist.angular.x = 0.0;
	odom.twist.twist.angular.y = 0.0;
	odom.twist.twist.angular.z = 0.0;

	ros::Rate rate(10.0);
	while (ros::ok()) {
		odom.header.stamp = ros::Time::now();
		odom_pub.publish(odom);
		rate.sleep();
	}

	return 0;
}
```
#### Python示例
在Python中，可以使用`nav_msgs`库来发布Odometry消息。例如，发布一个Odometry消息：

```python
import rospy
from nav_msgs.msg import Odometry

if __name__ == '__main__':
	rospy.init_node('odometry_publisher')
	odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)

	odom = Odometry()
	odom.header.frame_id = 'odom'
	odom.child_frame_id = 'base_link'
	odom.pose.pose.position.x = 0.0
	odom.pose.pose.position.y = 0.0
	odom.pose.pose.position.z = 0.0
	odom.pose.pose.orientation.x = 0.0
	odom.pose.pose.orientation.y = 0.0
	odom.pose.pose.orientation.z = 0.0
	odom.pose.pose.orientation.w = 1.0
	odom.twist.twist.linear.x = 0.0
	odom.twist.twist.linear.y = 0.0
	odom.twist.twist.linear.z = 0.0
	odom.twist.twist.angular.x = 0.0
	odom.twist.twist.angular.y = 0.0
	odom.twist.twist.angular.z = 0.0

	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():
		odom.header.stamp = rospy.Time.now()
		odom_pub.publish(odom)
		rate.sleep()
```

## 四、创建基础控制器
### （一）基础控制器简介
基础控制器用于控制机器人的运动，通常通过订阅速度命令话题并发布关节控制命令来实现。
### （二）创建基础控制器
#### 1. C++示例
在C++中，可以创建一个基础控制器节点，订阅速度命令话题并发布关节控制命令。例如：

```cpp
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Float64.h>

class BaseController {
public:
	BaseController() {
		vel_sub_ = nh_.subscribe("cmd_vel", 10, &BaseController::velCallback, this);
		left_wheel_pub_ = nh_.advertise<std_msgs::Float64>("left_wheel_cmd", 10);
		right_wheel_pub_ = nh_.advertise<std_msgs::Float64>("right_wheel_cmd", 10);
	}

	void velCallback(const geometry_msgs::Twist::ConstPtr& msg) {
		double linear_vel = msg->linear.x;
		double angular_vel = msg->angular.z;

		double left_wheel_vel = linear_vel - angular_vel * wheel_distance_ / 2.0;
		double right_wheel_vel = linear_vel + angular_vel * wheel_distance_ / 2.0;

		std_msgs::Float64 left_msg;
		left_msg.data = left_wheel_vel;
		left_wheel_pub_.publish(left_msg);

		std_msgs::Float64 right_msg;
		right_msg.data = right_wheel_vel;
		right_wheel_pub_.publish(right_msg);
	}

private:
	ros::NodeHandle nh_;
	ros::Subscriber vel_sub_;
	ros::Publisher left_wheel_pub_;
	ros::Publisher right_wheel_pub_;
	double wheel_distance_ = 0.5;  // 轮子间距
};

int main(int argc, char** argv) {
	ros::init(argc, argv, "base_controller");
	BaseController controller;
	ros::spin();
	return 0;
}
```
#### 2. Python示例
在Python中，可以创建一个基础控制器节点，订阅速度命令话题并发布关节控制命令。例如：

```python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class BaseController:
	def __init__(self):
		self.vel_sub_ = rospy.Subscriber('cmd_vel', Twist, self.vel_callback)
		self.left_wheel_pub_ = rospy.Publisher('left_wheel_cmd', Float64, queue_size=10)
		self.right_wheel_pub_ = rospy.Publisher('right_wheel_cmd', Float64, queue_size=10)
		self.wheel_distance_ = 0.5  # 轮子间距

	def vel_callback(self, msg):
		linear_vel = msg.linear.x
		angular_vel = msg.angular.z

		left_wheel_vel = linear_vel - angular_vel * self.wheel_distance_ / 2.0
		right_wheel_vel = linear_vel + angular_vel * self.wheel_distance_ / 2.0

		left_msg = Float64()
		left_msg.data = left_wheel_vel
		self.left_wheel_pub_.publish(left_msg)

		right_msg = Float64()
		right_msg.data = right_wheel_vel
		self.right_wheel_pub_.publish(right_msg)

if __name__ == '__main__':
	rospy.init_node('base_controller')
	controller = BaseController()
	rospy.spin()
```

## 五、创建地图
### （一）地图简介
地图是机器人导航中的重要组成部分，通常用于路径规划和定位。ROS中常用的地图格式包括`nav_msgs/OccupancyGrid`，表示2D栅格地图。
### （二）创建静态地图
#### 1. 使用`map_server`发布静态地图
`map_server`是一个ROS节点，用于发布静态地图。首先，创建一个地图文件`map.yaml`和一个地图图像文件`map.pgm`。`map.yaml`文件示例：

```yaml
image: map.pgm
resolution: 0.1
origin: [0.0, 0.0, 0.0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196
```

`map.pgm`文件是一个图像文件，表示地图的栅格数据。启动`map_server`：

```bash
rosrun map_server map_server map.yaml
```
#### 2. 使用`rviz`查看地图
```bash
rviz
```

在`rviz`中，添加`OccupancyGrid`显示类型，选择`/map`话题，可以查看地图。
### （三）创建动态地图
#### 1. 使用`gmapping`进行SLAM（Simultaneous Localization and Mapping）
`gmapping`是一个ROS包，用于实时创建地图并进行定位。首先，确保安装了`gmapping`：

```bash
sudo apt-get install ros-noetic-gmapping
```

启动`gmapping`：

```bash
roslaunch gmapping slam_gmapping.launch
```

`gmapping`会订阅激光雷达数据和里程数据，实时创建地图并发布到`/map`话题。
#### 2. 使用`cartographer`进行SLAM
`cartographer`是一个更先进的SLAM系统，支持2D和3D地图创建。首先，确保安装了`cartographer`：

```bash
sudo apt-get install ros-noetic-cartographer-ros
```

启动`cartographer`：

```bash
roslaunch cartographer_ros demo_backpack_2d.launch
```

`cartographer`会订阅激光雷达数据和里程数据，实时创建地图并发布到`/map`话题。


通过以上步骤，您可以创建自定义的机器人3D模型，发布传感器消息，发布里程数据信息，创建基础控制器，并创建地图。这些功能是机器人导航和自主移动的基础。


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