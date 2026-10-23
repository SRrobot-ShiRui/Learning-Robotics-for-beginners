# 建筑与环境建模
## 一、建筑元素的建模技巧
### （一）准备工作
#### 1. 确定建模目标和需求
 在开始建模之前，明确建筑模型的尺寸、比例和细节。收集参考图片或蓝图，了解设计的需求和约束条件。在Blender中，可以通过设置场景的单位和比例来确保模型在实际中的准确性。例如，设置场景单位为米：

```python
import bpy
bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.scale_length = 1.0
```
### （二）基础建模
#### 1. 创建基本结构
使用Blender的基本几何体（如立方体、圆柱体、平面等）创建建筑的基本结构。调整这些基本形状的大小和比例，使其与参考图或平面图匹配。例如，创建一个立方体作为建筑的基本结构：

```python
import bpy
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
```
#### 2. 添加细节
使用编辑工具（如挤出、拉伸、切割等）添加建筑的细节。例如，使用“Extrude”工具创建窗户和门的框架，使用“Bevel”工具创建圆角和棱角。 例如，使用细分操作添加细节：

```python
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.subdivide(number_cuts=2)
```
### （三）使用插件模型库（Archimesh为例）
 Blender有许多插件和模型库可以帮助加速建模过程。可以使用插件生成常见的建筑元素，如窗户、门、楼梯等。模型库则提供了各种室内和室外家具、植物等。这些资源可以节省时间和努力，并提高建模的质量。例如，使用插件Archimesh生成常见的建筑元素：

```python
import bpy
bpy.ops.mesh.archimesh_window()
```
### （四）优化模型
在建模过程中，需要进行模型的优化和细节处理，以提高模型的真实感和表现力。可以使用材质、纹理、渲染效果等技术来优化建筑模型的质量。

```python
material = bpy.data.materials.new(name="Brick")
material.diffuse_color = (1.0, 0.0, 0.0, 1.0)  # 红色
```

## 二、环境布局与场景构建
### （一）创建场景
打开Blender后，创建一个新的场景。点击顶部菜单栏中的“File”，选择“New”，然后选择“General”创建一个新的一般场景。
### （二）调整视图
 默认情况下，Blender的窗口初始布局是“3D Viewport”。可以通过鼠标右键点击窗口的分隔线，然后选择“Split Area”来调整窗口布局，添加额外的窗口来显示不同的视图。
### （三）添加基本元素
在场景搭建过程中，通常需要添加基本的元素，如地板、墙壁和家具等。点击左侧工具栏中的“Add”按钮，可以选择各种基本元素，例如平面、立方体、圆柱体等，然后将其添加到场景中。
### （四）编辑基本元素
一旦将基本元素添加到场景中，可以使用编辑工具对其进行进一步的调整和修改。选择一个基本元素，然后点击顶部菜单栏中的“Edit”按钮，进入编辑模式，进行调整。
### （五）整合元素
将主模型、背景和辅助元素整合在一起，调整它们的位置、大小和角度，确保它们在场景中看起来和谐统一。
### （六）设置灯光和摄像机
#### 1. 设置灯光
使用各种灯光类型和设置来照亮建筑场景。可以添加点光源、聚光灯、日光灯和区域光，调整灯光的强度、颜色和衰减。例如，添加一个点光源：

```python
bpy.ops.object.light_add(type='POINT', location=(0, 0, 5))
```
#### 2. 设置摄像机
调整摄像机的角度和位置，以模拟最终渲染时的视角。可以将建模软件的界面分割成左右两个窗口，左边窗口用于展示摄像机视角下的场景预览，右边窗口用于实际的操作和建模。
 例如，添加一个摄像机：

```python
bpy.ops.object.camera_add(location=(0, -10, 5), rotation=(1.0, 0.0, 0.0))
```
### （七）渲染和输出
#### 1. 渲染设置
在渲染属性面板中，设置渲染的分辨率、帧范围、采样次数和输出路径。选择合适的渲染引擎（如Eevee或Cycles），进行渲染。例如，设置渲染分辨率：

```python
bpy.context.scene.render.resolution = 1920
bpy.context.scene.render.resolution_y = 1080
```
#### 2. **输出设置**
设置输出文件的格式和路径。可以选择输出为图像文件（如PNG、JPEG）或视频文件（如MP4、AVI）。

```python
bpy.context.scene.render.filepath = 'D:/Render/MyProject/'
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