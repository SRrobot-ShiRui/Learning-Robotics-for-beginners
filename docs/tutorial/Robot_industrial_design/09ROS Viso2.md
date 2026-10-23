# 计算机视觉（ROS Viso2）

## 一、安装USB摄像头驱动
### 1. 安装`usb_cam`包
使用`apt-get`命令安装`usb_cam`包：

```bash
sudo apt-get install ros-<rosdistro>-usb-cam
```

其中`<rosdistro>`替换为对应的ROS版本，例如`noetic`或`melodic`。
### 2. 源码编译（可选）
如果需要从源码编译，可以按照以下步骤操作：

```bash
cd /path/to/colcon_ws/src
git clone https://github.com/ros-drivers/usb_cam.git
cd /path/to/colcon_ws
rosdep install --from-paths src --ignore-src -y
colcon build
source /path/to/colcon_ws/install/setup.bash
```

对于ROS 1，使用`catkin_make`代替`colcon build`。

## 二、启动摄像头
### 1. 启动`usb_cam`节点
使用`roslaunch`或`rosrun`命令启动`usb_cam`节点：

```bash
roslaunch usb_cam usb_cam-test.launch
```

或者使用参数文件启动：

```bash
ros2 run usb_cam usb_cam_node_exe --ros-args --params-file /path/to/usb_cam/config/params.yaml
```

对于ROS 1，使用`rosrun`命令：

```bash
rosrun usb_cam usb_cam_node
```

或者使用`roslaunch`文件。
### 2. 检查话题发布
使用`rostopic list`或`ros2 topic list`命令查看发布的图像话题：

```bash
rostopic list
```

图像数据一般会以`/image_raw`相关的名称发布。

## ROS与OpenCV库

### 一、安装OpenCV
#### 1. 安装OpenCV
 使用`apt-get`命令安装OpenCV：

```bash
sudo apt-get install libopencv-dev
```
#### 2. 安装Python绑定（可选）
安装Python绑定：

```bash
sudo apt-get install python3-opencv
```

### 二、使用OpenCV读取图像
```python
import cv2
cap = cv2.VideoCapture(0)  # 使用第一个摄像头
while True:
	ret, frame = cap.read()
	if not ret:
		break
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
```

## 使用ROS标定摄像头
#### 1. 安装`camera_calibration`包
使用`apt-get`命令安装`camera_calibration`包：

```bash
sudo apt-get install ros-<rosdistro>-camera-calibration
```
#### 2. 启动标定程序
使用`rosrun`命令启动标定程序：

```bash
rosrun camera_calibration cameracalibrator.py --size 6x7 --square 0.108 image:=/usb_cam/image_raw camera:=/usb_cam
```

其中`--size 6x7`表示棋盘格的内部角点个数，`--square 0.108`表示棋盘格的边长。
#### 3. 标定过程
标定过程中，需要将棋盘格放在摄像头视野的不同位置，包括左边、右边、上边和下边，确保标定板既有倾斜的，也有水平的。

## 视觉里程计
### 一、使用`viso2`库
#### 1. 安装`viso2`包
使用`apt-get`命令安装`viso2`包：

```bash
sudo apt-get install ros-<rosdistro>-viso2
```
#### 2. 启动`viso2`节点
使用`roslaunch`命令启动`viso2`节点：

```bash
roslaunch viso2_ros stereo_euroc.launch
```

或者根据具体需求修改`launch`文件。

### 二、使用`libviso2`库
#### 1. 下载和编译`libviso2`
下载`libviso2`源码并编译：

```bash
git clone https://github.com/ethz-asl/libviso2.git
cd libviso2
mkdir build
cd build
cmake ..
make
sudo make install
```
#### 2. 使用`libviso2`进行视觉里程计
使用`libviso2`进行视觉里程计的示例代码：

```cpp
#include <viso2/visual_odometry.h>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

int main() {
	viso2::VisualOdometryMono vo;
	vo.set_calib(640, 480, 525.0, 525.0, 320.0, 240.0);

	cv::VideoCapture cap(0);
	cv::Mat frame;

	while (true) {
		cap >> frame;
		if (frame.empty()) break;

		viso2::Image img(frame.data, frame.cols, frame.rows, viso2::MONO);
		vo.process(img);

		if (vo.has_result()) {
			const viso2::Matrix& T = vo.get_result();
			std::cout << "Translation: " << T.t() << std::endl;
			std::cout << "Rotation: " << T.R() << std::endl;
		}

		cv::imshow("frame", frame);
		if (cv::waitKey(30) >= 0) break;
	}

	return 0;
}
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