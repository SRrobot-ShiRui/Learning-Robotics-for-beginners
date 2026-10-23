# ROS中使用MoveIt进行机械臂操作（MoveIt）
## 一、体系结构
MoveIt是一个用于机器人运动规划和操作的ROS框架。它提供了丰富的工具和库，用于实现机械臂的运动规划、抓取和放置等任务。MoveIt的体系结构主要包括以下几个部分：

1. **Planning Scene**：表示机器人的环境和状态，包括机器人模型、碰撞对象等。
2. **Planning Interface**：提供与规划场景交互的接口，用于添加和移除碰撞对象、查询场景状态等。
3. **Motion Planning**：核心功能，用于生成从当前状态到目标状态的运动路径。
4. **Execution**：将规划好的路径发送给机器人执行。

## 二、简单运动规划
### （一）安装MoveIt
```bash
sudo apt-get install ros-noetic-moveit
```
### （二）配置MoveIt
#### 1. 创建MoveIt配置包
```bash
rosrun moveit_setup_assistant setup_assistant.py
```

按照提示进行操作，生成配置文件。
#### 2. 启动MoveIt
```bash
roslaunch moveit_planning_execution.launch
```
### （三）编写运动规划代码
#### C++示例
创建一个C++节点，使用MoveIt的API进行运动规划：

```cpp
#include <moveit/move_group_interface/move_group_interface.h>
#include <rclcpp/rclcpp.hpp>

int main(int argc, char** argv) {
	rclcpp::init(argc, argv);
	rclcpp::NodeOptions options;
	auto node = rclcpp::Node::make_shared("moveit_demo", options);

	moveit::planning_interface::MoveGroupInterface move_group(node, "panda_arm");

	// 设置目标姿态
	geometry_msgs::msg::Pose target_pose;
	target_pose.position.x = 0.5;
	target_pose.position.y = 0.0;
	target_pose.position.z = 0.5;
	target_pose.orientation.x = 0.0;
	target_pose.orientation.y = 0.0;
	target_pose.orientation.z = 0.0;
	target_pose.orientation.w = 1.0;

	move_group.setPoseTarget(target_pose);

	// 规划并执行
	moveit::planning_interface::MoveGroupInterface::Plan plan;
	bool success = (move_group.plan(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
	if (success) {
		move_group.execute(plan);
	}

	rclcpp::shutdown();
	return 0;
}
```
#### Python示例
创建一个Python节点，使用MoveIt的API进行运动规划：

```python
import rospy
import moveit_commander

def main():
	rospy.init_node("moveit_demo")

	move_group = moveit_commander.MoveGroupCommander("panda_arm")

	# 设置目标姿态
	target_pose = move_group.get_pose_reference_frame()
	target_pose.position.x = 0.5
	target_pose.position.y = 0.0
	target_pose.position.z = 0.5
	target_pose.orientation.x = 0.0
	target_pose.orientation.y = 0.0
	target_pose.orientation.z = 0.0
	target_pose.orientation.w = 1.0

	move_group.set_pose_target(target_pose)

	# 规划并执行
	plan = move_group.plan()
	if plan:
		move_group.execute(plan)

if __name__ == "__main__":
	main()
```

## 三、抓取放置任务
### （一）下载MoveIt任务构造器
#### 1. 克隆MoveIt任务构造器仓库
```bash
cd ~/ws_moveit2/src
git clone https://github.com/ros-planning/moveit_task_constructor.git
```
#### 2. 创建新包
```bash
ros2 pkg create --build-type ament_cmake --node-name mtc_tutorial mtc_tutorial
```
#### 3. 添加依赖
修改`package.xml`文件，添加依赖：

```xml
<depend>moveit_task_constructor_core</depend>
<depend>rclcpp</depend>
```
### （二）编写抓取放置任务代码

#### C++示例
创建一个C++节点，使用MoveIt任务构造器进行抓取和放置任务：

```cpp
#include <rclcpp/rclcpp.hpp>
#include <moveit/planning_scene/planning_scene.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit/task_constructor/task.h>
#include <moveit/task_constructor/solvers.h>
#include <moveit/task_constructor/stages.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>
#include <tf2_eigen/tf2_eigen.hpp>

static const rclcpp::Logger LOGGER = rclcpp::get_logger("mtc_tutorial");
namespace mtc = moveit::task_constructor;

class MTCTaskNode {
public:
	MTCTaskNode(const rclcpp::NodeOptions& options);
	rclcpp::node_interfaces::NodeBaseInterface::SharedPtr getNodeBaseInterface();
	void doTask();
	void setupPlanningScene();
private:
	mtc::Task createTask();
	mtc::Task task_;
	rclcpp::Node::SharedPtr node_;
};

rclcpp::node_interfaces::NodeBaseInterface::SharedPtr MTCTaskNode::getNodeBaseInterface() {
	return node_->get_node_base_interface();
}

MTCTaskNode::MTCTaskNode(const rclcpp::NodeOptions& options)
	: node_{ std::make_shared<rclcpp::Node>("mtc_node", options) } {
}

void MTCTaskNode::setupPlanningScene() {
	moveit_msgs::msg::CollisionObject object;
	object.id = "object";
	object.header.frame_id = "world";
	object.primitives.resize(1);
	object.primitives[0].type = shape_msgs::msg::SolidPrimitive::CYLINDER;
	object.primitives[0].dimensions = { 0.1, 0.02 };
	geometry_msgs::msg::Pose pose;
	pose.position.x = 0.5;
	pose.position.y = -0.25;
	pose.orientation.w = 1.0;
	object.pose = pose;
	moveit::planning_interface::PlanningSceneInterface psi;
	psi.applyCollisionObject(object);
}

void MTCTaskNode::doTask() {
	task_ = createTask();
	try {
		task_.init();
	} catch (mtc::InitStageException& e) {
		RCLCPP_ERROR_STREAM(LOGGER, e);
		return;
	}
	if (!task_.plan(5)) {
		RCLCPP_ERROR_STREAM(LOGGER, "Task planning failed");
		return;
	}
	task_.introspection().publishSolution(*task_.solutions().front());
	auto result = task_.execute(*task_.solutions().front());
	if (result.val != moveit_msgs::msg::MoveItErrorCodes::SUCCESS) {
		RCLCPP_ERROR_STREAM(LOGGER, "Task execution failed");
		return;
	}
}

mtc::Task MTCTaskNode::createTask() {
	mtc::Task task;
	task.stages()->setName("demo task");
	task.loadRobotModel(node_);
	const auto& arm_group_name = "panda_arm";
	const auto& hand_group_name = "hand";
	const auto& hand_frame = "panda_hand";
	task.setProperty("group", arm_group_name);
	task.setProperty("eef", hand_group_name);
	task.setProperty("ik_frame", hand_frame);

	auto stage_state_current = std::make_unique<mtc::stages::CurrentState>("current");
	task.add(std::move(stage_state_current));

	auto sampling_planner = std::make_shared<mtc::solvers::PipelinePlanner>(node_);
	auto interpolation_planner = std::make_shared<mtc::solvers::JointInterpolationPlanner>();
	auto cartesian_planner = std::make_shared<mtc::solvers::CartesianPath>();

	cartesian_planner->setMaxVelocityScalingFactor(1.0);
	cartesian_planner->setMaxAccelerationScalingFactor(1.0);
	cartesian_planner->setStepSize(.01);

	auto stage_open_hand = std::make_unique<mtc::stages::MoveTo>("open hand", interpolation_planner);
	stage_open_hand->setGroup(hand_group_name);
	stage_open_hand->setGoal("open");
	task.add(std::move(stage_open_hand));

	return task;
}

int main(int argc, char** argv) {
	rclcpp::init(argc, argv);
	rclcpp::NodeOptions options;
	MTCTaskNode node(options);
	node.setupPlanningScene();
	node.doTask();
	rclcpp::shutdown();
	return 0;
}
```

#### Python示例
创建一个Python节点，使用MoveIt任务构造器进行抓取和放置任务：

```python
import rclpy
from rclpy.node import Node
from moveit.planning_scene import PlanningScene
from moveit.planning_scene_interface import PlanningSceneInterface
from moveit.task_constructor import Task, Stages, Solvers
from moveit.task_constructor import stages, solvers
from geometry_msgs.msg import Pose
from shape_msgs.msg import SolidPrimitive
from moveit_msgs.msg import CollisionObject

class MTCTaskNode(Node):
	def __init__(self):
		super().__init__("mtc_node")
		self.task_ = Task()
		self.setup_planning_scene()

	def setup_planning_scene(self):
		object = CollisionObject()
		object.id = "object"
		object.header.frame_id = "world"
		object.primitives.append(SolidPrimitive(type=SolidPrimitive.CYLINDER, dimensions=[0.1, 0.02]))
		pose = Pose()
		pose.position.x = 0.5
		pose.position.y = -0.25
		pose.orientation.w = 1.0
		object.pose = pose
		psi = PlanningSceneInterface()
		psi.apply_collision_object(object)

	def do_task(self):
		self.task_ = self.create_task()
		try:
			self.task_.init()
		except Exception as e:
			self.get_logger().error(str(e))
			return
		if not self.task_.plan(5):
			self.get_logger().error("Task planning failed")
			return
		self.task_.introspection().publish_solution(self.task_.solutions()[0])
		result = self.task_.execute(self.task_.solutions()[0])
		if result.val != 0:
			self.get_logger().error("Task execution failed")
			return

	def create_task(self):
		task = Task()
		task.stages().set_name("demo task")
		task.load_robot_model(self)
		arm_group_name = "panda_arm"
		hand_group_name = "hand"
		hand_frame = "panda_hand"
		task.set_property("group", arm_group_name)
		task.set_property("eef", hand_group_name)
		task.set_property("ik_frame", hand_frame)

		stage_state_current = stages.CurrentState("current")
		task.add(stage_state_current)

		sampling_planner = solvers.PipelinePlanner(self)
		interpolation_planner = solvers.JointInterpolationPlanner()
		cartesian_planner = solvers.CartesianPath()

		cartesian_planner.set_max_velocity_scaling_factor(1.0)
		cartesian_planner.set_max_acceleration_scaling_factor(1.0)
		cartesian_planner.set_step_size(0.01)

		stage_open_hand = stages.MoveTo("open hand", interpolation_planner)
		stage_open_hand.set_group(hand_group_name)
		stage_open_hand.set_goal("open")
		task.add(stage_open_hand)

		return task

def main(args=None):
	rclpy.init(args=args)
	node = MTCTaskNode()
	node.do_task()
	rclpy.shutdown()

if __name__ == "__main__":
	main()
```


## 简述MoveIt的运动规划过程

MoveIt的运动规划过程涉及多个步骤，从设置规划场景到执行规划路径，每一步都至关重要。以下是详细的运动规划过程：
### （一）初始化规划环境
#### 1. 创建规划场景（Planning Scene）
规划场景是机器人环境的表示，包括机器人模型、碰撞对象、静态障碍物等。它为运动规划提供了必要的上下文信息。在ROS中，可以使用`moveit::planning_interface::PlanningSceneInterface`来管理规划场景。例如，添加一个碰撞对象到规划场景中：

```cpp
moveit::planning_interface::PlanningSceneInterface psi;
moveit_msgs::msg::CollisionObject object;
object.id = "object";
object.header.frame_id = "world";
object.primitives.resize(1);
object.primitives[0].type = shape_msgs::msg::SolidPrimitive::BOX;
object.primitives[0].dimensions = {0.1, 0.1, 0.1};
object.pose.position.x = 0.5;
object.pose.position.y = 0.0;
object.pose.position.z = 0.5;
object.pose.orientation.w = 1.0;
psi.applyCollisionObject(object);
```
#### 2. 创建MoveGroup接口
`moveit::planning_interface::MoveGroupInterface`是MoveIt提供的高级接口，用于控制机械臂的运动。它封装了规划和执行的复杂性，提供了简单易用的API。例如，创建一个MoveGroup接口：

```cpp
moveit::planning_interface::MoveGroupInterface move_group("panda_arm");
```
### （二）设置目标姿态
#### 1. 设置目标位置和姿态
 通过`setPoseTarget`方法设置机械臂的目标位置和姿态。目标姿态可以是一个`geometry_msgs::msg::Pose`消息，包含位置和四元数表示的姿态。例如，设置目标姿态：

```cpp
geometry_msgs::msg::Pose target_pose;
target_pose.position.x = 0.5;
target_pose.position.y = 0.0;
target_pose.position.z = 0.5;
target_pose.orientation.x = 0.0;
target_pose.orientation.y = 0.0;
target_pose.orientation.z = 0.0;
target_pose.orientation.w = 1.0;
move_group.setPoseTarget(target_pose);
```
#### 2. 设置目标关节位置
也可以通过`setJointValueTarget`方法设置目标关节位置。目标关节位置可以是一个`std::vector<double>`，包含每个关节的目标角度。例如，设置目标关节位置：

```cpp
std::vector<double> joint_positions = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7};
move_group.setJointValueTarget(joint_positions);
```
### （三）规划路径
#### 1. 生成规划请求
通过`plan`方法生成规划请求。该方法会返回一个`moveit::planning_interface::MoveGroupInterface::Plan`对象，包含规划路径的信息。 例如，生成规划请求：

```cpp
moveit::planning_interface::MoveGroupInterface::Plan plan;
bool success = (move_group.plan(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
if (success) {
	// 规划成功
} else {
	// 规划失败
}
```
#### 2. 检查规划结果
检查规划结果是否成功。如果规划成功，`plan`对象将包含规划路径的详细信息，包括关节轨迹、时间戳等。例如，检查规划结果：

```cpp
if (success) {
	// 规划成功，可以执行路径
	move_group.execute(plan);
} else {
	// 规划失败，输出错误信息
	RCLCPP_ERROR_STREAM(LOGGER, "Planning failed");
}
```
### （四）执行路径
#### 1. 执行规划路径
通过`execute`方法执行规划路径。该方法会将规划路径发送给机器人控制器，控制机械臂按照规划路径运动。例如，执行规划路径：

```cpp
move_group.execute(plan);
```
#### 2. 监控执行过程
可以通过`moveit::planning_interface::MoveGroupInterface`的回调函数监控执行过程，获取执行状态和反馈信息。 例如，监控执行过程：

```cpp
move_group.execute(plan, moveit::planning_interface::MoveGroupInterface::ExecuteTrajectoryGoal::DONE, 
				   [](const actionlib::SimpleClientGoalState& state, const moveit_msgs::msg::ExecuteTrajectoryResultConstPtr& result) {
					   if (state.state_ == actionlib::SimpleClientGoalState::SUCCEEDED) {
						   RCLCPP_INFO_STREAM(LOGGER, "Execution succeeded");
					   } else {
						   RCLCPP_ERROR_STREAM(LOGGER, "Execution failed: " << state.toString());
					   }
				   });
```
### （五）处理碰撞和约束
#### 1. 处理碰撞
在规划过程中，MoveIt会自动处理碰撞检测。可以通过规划场景添加和移除碰撞对象，确保机械臂在运动过程中不会与环境中的障碍物发生碰撞。例如，移除碰撞对象：

```cpp
psi.removeCollisionObject("object");
```

#### 2. 设置约束
可以通过`setPathConstraints`方法设置路径约束，如关节角度范围、姿态约束等。这些约束可以确保机械臂在运动过程中满足特定的条件。例如，设置关节角度范围约束：

```cpp
moveit_msgs::msg::Constraints constraints;
constraints.name = "joint_constraints";
moveit_msgs::msg::JointConstraint joint_constraint;
joint_constraint.joint_name = "panda_joint1";
joint_constraint.position = 0.0;
joint_constraint.tolerance_above = 0.1;
joint_constraint.tolerance_below = 0.1;
joint_constraint.weight = 1.0;
constraints.joint_constraints.push_back(joint_constraint);
move_group.setPathConstraints(constraints);
```
### （六）使用MoveIt任务构造器
#### 1. 创建任务
MoveIt任务构造器（MoveIt Task Constructor）是一个更高级的工具，用于构建复杂的任务流程。它可以将多个规划阶段组合成一个任务，并支持条件分支、循环等控制结构。例如，创建一个任务：

```cpp
mtc::Task task;
task.stages()->setName("demo task");
task.loadRobotModel(node_);
const auto& arm_group_name = "panda_arm";
const auto& hand_group_name = "hand";
const auto& hand_frame = "panda_hand";
task.setProperty("group", arm_group_name);
task.setProperty("eef", hand_group_name);
task.setProperty("ik_frame", hand_frame);

auto stage_state_current = std::make_unique<mtc::stages::CurrentState>("current");
task.add(std::move(stage_state_current));

auto sampling_planner = std::make_shared<mtc::solvers::PipelinePlanner>(node_);
auto interpolation_planner = std::make_shared<mtc::solvers::JointInterpolationPlanner>();
auto cartesian_planner = std::make_shared<mtc::solvers::CartesianPath>();

cartesian_planner->setMaxVelocityScalingFactor(1.0);
cartesian_planner->setMaxAccelerationScalingFactor(1.0);
cartesian_planner->setStepSize(0.01);

auto stage_open_hand = std::make_unique<mtc::stages::MoveTo>("open hand", interpolation_planner);
stage_open_hand->setGroup(hand_group_name);
stage_open_hand->setGoal("open");
task.add(std::move(stage_open_hand));
```
#### 2. 执行任务
通过`init`、`plan`和`execute`方法执行任务。这些方法会依次执行任务中的每个阶段，确保任务的顺利完成。例如，执行任务：

```cpp
try {
	task.init();
} catch (mtc::InitStageException& e) {
	RCLCPP_ERROR_STREAM(LOGGER, e);
	return;
}
if (!task.plan(5)) {
	RCLCPP_ERROR_STREAM(LOGGER, "Task planning failed");
	return;
}
task.introspection().publishSolution(*task.solutions().front());
auto result = task.execute(*task.solutions().front());
if (result.val != moveit_msgs::msg::MoveItErrorCodes::SUCCESS) {
	RCLCPP_ERROR_STREAM(LOGGER, "Task execution failed");
	return;
}
```

## MoveIt检查碰撞
MoveIt使用多种方法进行碰撞检测，以确保机器人在运动过程中不会与环境中的障碍物发生碰撞。以下是MoveIt碰撞检测的主要机制和流程：
### （一）碰撞检测库
MoveIt支持多种碰撞检测库，包括FCL（Flexible Collision Library）和Bullet。FCL是MoveIt默认的碰撞检测库，而Bullet提供了连续碰撞检测（CCD）功能。
### （二）碰撞检测流程
#### 1. 设置规划场景（Planning Scene）
规划场景是机器人环境的表示，包括机器人模型、碰撞对象、静态障碍物等。它为运动规划提供了必要的上下文信息。例如，添加一个碰撞对象到规划场景中：

```cpp
moveit::planning_interface::PlanningSceneInterface psi;
moveit_msgs::msg::CollisionObject object;
object.id = "object";
object.header.frame_id = "world";
object.primitives.resize(1);
object.primitives[0].type = shape_msgs::msg::SolidPrimitive::BOX;
object.primitives[0].dimensions = {0.1, 0.1, 0.1};
object.pose.position.x = 0.5;
object.pose.position.y = 0.0;
object.pose.position.z = 0.5;
object.pose.orientation.w = 1.0;
psi.applyCollisionObject(object);
```
#### 2. 创建MoveGroup接口
`moveit::planning_interface::MoveGroupInterface`是MoveIt提供的高级接口，用于控制机械臂的运动。它封装了规划和执行的复杂性，提供了简单易用的API。例如，创建一个MoveGroup接口：

```cpp
moveit::planning_interface::MoveGroupInterface move_group("panda_arm");
```
#### 3. 设置碰撞检测器
可以通过规划场景设置不同的碰撞检测器。例如，使用Bullet作为碰撞检测器：

```cpp
g_planning_scene->setActiveCollisionDetector(collision_detection::CollisionDetectorAllocatorBullet::create());
```
#### 4. 执行碰撞检测
通过`checkCollision`方法执行碰撞检测。该方法会检查机器人当前状态是否与环境中的障碍物发生碰撞。例如，执行碰撞检测：

```cpp
collision_detection::CollisionRequest req;
collision_detection::CollisionResult res;
req.contacts = true;
g_planning_scene->checkCollision(req, res);
if (res.collision) {
	ROS_INFO("In collision.");
} else {
	ROS_INFO("Not in collision.");
}
```
### （三）连续碰撞检测（CCD）
Bullet支持连续碰撞检测，可以保证在两个离散机器人状态与环境之间的过渡期间不会发生碰撞。例如，使用两个离散姿势之间的机器人模型执行CCD：

```cpp
res.clear();
planning_scene->getCollisionEnv()->checkRobotCollision(req, res, state, state_before);
ROS_INFO_STREAM_NAMED("bullet_tutorial", (res.collision ? "In collision." : "Not in collision."));
```
### （四）碰撞检测结果可视化
MoveIt可以通过RViz可视化碰撞检测结果。例如，将碰撞接触点显示为标记：

```cpp
if (c_res.collision) {
    ROS_INFO("COLLIDING contact_point_count=%d", (int)c_res.contact_count);
    if (c_res.contact_count > 0) {
        std_msgs::ColorRGBA color;
        color.r = 1.0;
        color.g = 0.0;
        color.b = 1.0;
        color.a = 0.5;
        visualization_msgs::MarkerArray markers;
        collision_detection::getCollisionMarkersFromContacts(markers, "panda_link0", c_res.contacts, color, ros::Duration(), 0.01);
        publishMarkers(markers);
    }
}
```

通过以上步骤，MoveIt可以有效地进行碰撞检测，确保机器人在运动过程中不会与环境中的障碍物发生碰撞。


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