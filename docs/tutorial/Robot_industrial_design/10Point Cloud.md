# 点云（Point Cloud）

## 一、点云的定义
**点云（Point Cloud）** 是指在三维空间中由大量点组成的集合，每个点包含三维坐标（X, Y, Z）以及可能的其他属性，如颜色（R, G, B）、强度（Intensity）等。点云数据通常用于表示物体或环境的三维形状和结构，广泛应用于机器人导航、环境感知、3D建模、物体识别等领域。

## 二、点云的来源
### 1. RGBD传感器
RGBD传感器（如Kinect、Realsense等）可以同时提供彩色图像（RGB）和深度图像（D），通过深度图像可以生成点云数据。每个像素点的深度值可以转换为三维坐标，从而形成点云。例如，使用Realsense传感器生成点云：

```bash
roslaunch realsense2_camera rs_camera.launch
```
### 2. 激光雷达（LiDAR）
激光雷达通过发射激光束并测量反射时间（TOF）或相位差来获取环境的深度信息，生成点云数据。激光雷达点云通常具有较高的精度和分辨率。例如，使用Velodyne激光雷达生成点云：

```bash
roslaunch velodyne_pointcloud VLP16_points.launch
```
### 3. 立体视觉（Stereo Vision）
通过两个或多个摄像头获取同一场景的多张图像，利用视差原理计算深度信息，生成点云数据。立体视觉点云的生成依赖于图像匹配算法。例如，使用`stereo_image_proc`包生成点云：

```bash
roslaunch stereo_image_proc stereo.launch
```

## 三、点云在ROS中的表示
在ROS中，点云数据通常以`sensor_msgs/PointCloud2`消息类型表示。`PointCloud2`消息是一种高效的二进制格式，可以包含点云的多种属性。

**`sensor_msgs/PointCloud2`消息结构**：

- **header**：包含时间戳和帧ID。

- **height**：点云的高度（行数）。

- **width**：点云的宽度（列数）。

- **fields**：描述每个点的属性（如X, Y, Z, R, G, B等）。

- **is_bigendian**：数据的字节序。

- **point_step**：每个点的字节数。

- **row_step**：每行的字节数。

- **data**：点云数据的二进制表示。

## 四、点云的处理和应用
### 1. 滤波
**体素滤波**：通过体素网格对点云进行下采样，减少点云数据量。

```cpp
#include <pcl/filters/voxel_grid.h>
// ...
pcl::VoxelGrid<pcl::PointXYZ> sor;
sor.setInputCloud(cloud);
sor.setLeafSize(0.01, 0.01, 0.01);
sor.filter(*cloud_filtered);
```

**统计滤波**：去除离群点。

```cpp
#include <pcl/filters/statistical_outlier_removal.h>
// ...
pcl::StatisticalOutlierRemoval<pcl::PointXYZ> sor;
sor.setInputCloud(cloud);
sor.setMeanK(50);
sor.setStddevMulThresh(1.0);
sor.filter(*cloud_filtered);
```
### 2. 特征提取
**法线估计**：计算点云中每个点的法线向量。

```cpp
#include <pcl/features/normal_3d.h>
// ...
pcl::NormalEstimation<pcl::PointXYZ, pcl::Normal> ne;
ne.setInputCloud(cloud);
ne.setKSearch(50);
ne.compute(*cloud_normals);
```
### 3. 配准与匹配
**ICP（Iterative Closest Point）**：将两个点云对齐。

```cpp
#include <pcl/registration/icp.h>
// ...
pcl::IterativeClosestPoint<pcl::PointXYZ, pcl::PointXYZ> icp;
icp.setInputSource(cloud_src);
icp.setInputTarget(cloud_tgt);
pcl::PointCloud<pcl::PointXYZ> Final;
icp.align(Final);
```
### 4. 分割
**欧几里得聚类**：将点云分割成多个独立的物体。

```cpp
#include <pcl/segmentation/euclidean_cluster_extraction.h>
// ...
pcl::EuclideanClusterExtraction<pcl::PointXYZ> ec;
ec.setClusterTolerance(0.02);
ec.setMinClusterSize(100);
ec.setMaxClusterSize(25000);
ec.setInputCloud(cloud);
std::vector<pcl::PointIndices> cluster_indices;
ec.extract(cluster_indices);
```
### 5. 可视化
**使用RViz**：在RViz中添加`PointCloud2`显示类型，选择对应的点云话题。

**使用PCL可视化工具**：使用`pcl::visualization::CloudViewer`显示点云。

```cpp
#include <pcl/visualization/cloud_viewer.h>
// ...
pcl::visualization::CloudViewer viewer("PointCloud Viewer");
viewer.showCloud(cloud);
while (!viewer.wasStopped ()) {}
```

## 五、点云的应用示例
### 1. 环境感知
机器人使用点云数据感知周围环境，识别障碍物和路径。例如，使用点云进行导航和避障：

```cpp
#include <pcl/filters/passthrough.h>
// ...
pcl::PassThrough<pcl::PointXYZ> pass;
pass.setInputCloud(cloud);
pass.setFilterFieldName("z");
pass.setFilterLimits(0.0, 1.0);
pass.filter(*cloud_filtered);
```
### 2. 物体识别
通过点云特征提取和分类算法识别物体。例如，使用SIFT特征识别物体：

```cpp
#include <pcl/features/sift_keypoint.h>
// ...
pcl::SIFTKeypoint<pcl::PointXYZ, pcl::PointWithScale> sift;
sift.setInputCloud(cloud);
pcl::PointCloud<pcl::PointWithScale> keypoints;
sift.compute(keypoints);
```
### 3. 3D建模
使用点云数据生成三维模型。例如，使用`pcl::MarchingCubes`生成三维模型：

```cpp
#include <pcl/surface/marching_cubes.h>
// ...
pcl::MarchingCubes<pcl::PointXYZ> mc;
mc.setInputCloud(cloud);
mc.setIsoLevel(0.01);
pcl::PolygonMesh mesh;
mc.reconstruct(mesh);
```

## ROS中点云库及相关操作
### 1. 点云库（PCL）
**PCL（Point Cloud Library）** 是一个用于处理点云数据的开源库，提供了丰富的点云处理功能，如滤波、特征提取、配准与匹配、分割等。
### 2. 可视化点云
**使用RViz可视化点云**：RViz是ROS中常用的可视化工具，可以方便地显示点云数据。
首先，确保安装了`rviz`包：

```bash
sudo apt-get install ros-<distro>-rviz
```

然后，启动RViz并添加`PointCloud2`显示类型，选择对应的点云话题即可。

**使用PCL可视化点云**：PCL提供了自己的可视化工具`pcl::visualization::CloudViewer`，可以用于显示点云数据。

```cpp
#include <pcl/visualization/cloud_viewer.h>
// ...
pcl::visualization::CloudViewer viewer("PointCloud Viewer");
viewer.showCloud(cloud);
while (!viewer.wasStopped ()) {}
```
### 3. 滤波和缩减采样
**体素滤波下采样**：用于减少点云数据量，提高处理效率。

```cpp
#include <pcl/filters/voxel_grid.h>
// ...
pcl::VoxelGrid<pcl::PointXYZ> sor;
sor.setInputCloud(cloud);
sor.setLeafSize(leaf_size, leaf_size, leaf_size);
sor.filter(*cloud_filtered);
```

**统计滤波**：用于去除离群点。

```cpp
#include <pcl/filters/statistical_outlier_removal.h>
// ...
pcl::StatisticalOutlierRemoval<pcl::PointXYZ> sor;
sor.setInputCloud(cloud);
sor.setMeanK(mean_k);
sor.setStddevMulThresh(stddev_mul_thresh);
sor.filter(*cloud_filtered);
```
### 4. 配准与匹配
**使用PCL进行点云配准**：PCL提供了多种点云配准算法，如ICP（Iterative Closest Point）。

```cpp
#include <pcl/registration/icp.h>
// ...
pcl::IterativeClosestPoint<pcl::PointXYZ, pcl::PointXYZ> icp;
icp.setInputSource(cloud_src);
icp.setInputTarget(cloud_tgt);
pcl::PointCloud<pcl::PointXYZ> Final;
icp.align(Final);
```
### 5. 点云分区
**使用PCL进行点云分割**：PCL提供了多种点云分割算法，如区域生长分割、欧几里得聚类等。

```cpp
#include <pcl/segmentation/euclidean_cluster_extraction.h>
// ...
pcl::EuclideanClusterExtraction<pcl::PointXYZ> ec;
ec.setClusterTolerance(cluster_tolerance);
ec.setMinClusterSize(min_cluster_size);
ec.setMaxClusterSize(max_cluster_size);
ec.setInputCloud(cloud);
std::vector<pcl::PointIndices> cluster_indices;
ec.extract(cluster_indices);
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