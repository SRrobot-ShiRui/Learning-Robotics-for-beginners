# ROS中机器人配置及相关功能实现（Navigation & RViz）

## 一、机器人配置
### （一）安装导航栈
首先，确保安装了ROS导航栈。对于ROS Noetic，可以使用以下命令安装：

```bash
sudo apt-get install ros-noetic-navigation
```

对于ROS 2，可以使用以下命令安装：

```bash
sudo apt install ros-$ROS_DISTRO-navigation2
sudo apt install ros-$ROS_DISTRO-nav2-bringup
```
### （二）配置参数文件
复制配置文件到你的包中，并进行修改。例如，复制`nav2_params.yaml`文件：

```bash
cp /opt/ros/humble/share/nav2_bringup/params/nav2_params.yaml .
```

修改参数文件，例如设置机器人的半径：

```yaml
robot_radius: 0.12
```

## 二、全局和局部代价地图
### （一）代价地图简介
代价地图（Costmap）是ROS中用于路径规划的重要工具。它分为全局代价地图（Global Costmap）和局部代价地图（Local Costmap）。
### （二）配置代价地图
#### 1. 通用参数配置（`costmap_common_params.yaml`）

```yaml
robot_radius: 0.2
obstacle_layer:
  enabled: true
  combination_method: 1
  track_unknown_space: true
  obstacle_range: 2.5
  raytrace_range: 3.0
  observation_sources: laser_scan_sensor
  laser_scan_sensor: {
    sensor_frame: /robot0_laser_0,
    data_type: LaserScan,
    topic: /robot0/laser_0,
    marking: true,
    clearing: true
  }
inflation_layer:
  enabled: true
  cost_scaling_factor: 5.0
  inflation_radius: 0.36
static_layer:
  enabled: true
```
#### 2. 全局代价地图配置（`global_costmap_params.yaml`）

```yaml
global_costmap:
  global_frame: /map
  robot_base_frame: /robot0
  update_frequency: 0.5
  static_map: true
  rolling_window: false
  transform_tolerance: 1.0
  plugins:
    - {name: static_layer,    type: "costmap_2d::StaticLayer"}
    - {name: obstacle_layer,  type: "costmap_2d::ObstacleLayer"}
    - {name: inflation_layer, type: "costmap_2d::InflationLayer"}
```
#### 3. 局部代价地图配置（`local_costmap_params.yaml`）

```yaml
local_costmap:
  global_frame: /map_static
  robot_base_frame: /robot0
  update_frequency: 5.0
  publish_frequency: 3.0
  static_map: false
  rolling_window: true
  width: 4.0
  height: 4.0
  resolution: 0.05
  transform_tolerance: 0.5
  plugins:
    - {name: obstacle_layer,  type: "costmap_2d::ObstacleLayer"}
    - {name: inflation_layer, type: "costmap_2d::InflationLayer"}
```

## 三、RViz详细配置
### （一）启动RViz并加载配置文件
```bash
rosrun rviz rviz -d /path/to/your/rviz_config.rviz
```
### （二）添加显示内容

- **机器人模型**：选择`RobotModel`，设置`Robot Description`为`robot_description`。

- **地图**：选择`Map`，设置`Topic`为`/map`。

- **全局代价地图**：选择`Map`，设置`Topic`为`/move_base/global_costmap/costmap`，设置`Color Scheme`为`Costmap`。

- **局部代价地图**：选择`Map`，设置`Topic`为`/move_base/local_costmap/costmap`，设置`Color Scheme`为`Costmap`。

- **导航路线**：选择`Path`，设置`Topic`为`/move_base/GlobalPlanner/plan`，设置`Line Style`为`Billboards`。

## 四、自适应蒙特卡洛定位（AMCL）
### （一）安装AMCL
```bash
sudo apt-get install ros-noetic-amcl
```
### （二）启动AMCL
```xml
<node pkg="amcl" type="amcl" name="amcl">
  <param name="use_map_topic" value="true"/>
  <param name="initial_pose_x" value="0.0"/>
  <param name="initial_pose_y" value="0.0"/>
  <param name="initial_pose_a" value="0.0"/>
</node>
```

## 五、避障
### （一）配置避障参数
在`costmap_common_params.yaml`中配置避障参数：

```yaml
obstacle_layer:
  enabled: true
  combination_method: 1
  track_unknown_space: true
  obstacle_range: 2.5
  raytrace_range: 3.0
  observation_sources: laser_scan_sensor
  laser_scan_sensor: {
    sensor_frame: /robot0_laser_0,
    data_type: LaserScan,
    topic: /robot0/laser_0,
    marking: true,
    clearing: true
  }
inflation_layer:
  enabled: true
  cost_scaling_factor: 5.0
  inflation_radius: 0.36
```
### （二）动态避障
在`local_costmap_params.yaml`中配置局部代价地图，确保动态避障：

```yaml
local_costmap:
  global_frame: /map_static
  robot_base_frame: /robot0
  update_frequency: 5.0
  publish_frequency: 3.0
  static_map: false
  rolling_window: true
  width: 4.0
  height: 4.0
  resolution: 0.05
  transform_tolerance: 0.5
  plugins:
    - {name: obstacle_layer,  type: "costmap_2d::ObstacleLayer"}
    - {name: inflation_layer, type: "costmap_2d::InflationLayer"}
```

## 六、目标发送
### （一）使用RViz发送目标
在RViz中，使用`2D Nav Goal`工具发送目标点。点击`2D Nav Goal`，然后在地图上点击目标位置，机器人将自动导航到该位置。
### （二）使用命令行发送目标
使用`rostopic`命令发送目标点：

```bash
rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'map'
pose:
  position:
    x: 1.0
    y: 1.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
```

通过以上步骤，您可以完成机器人的配置，设置全局和局部代价地图，详细配置RViz，实现自适应蒙特卡洛定位，配置避障功能，并发送目标点。这些功能是机器人导航和自主移动的基础。



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