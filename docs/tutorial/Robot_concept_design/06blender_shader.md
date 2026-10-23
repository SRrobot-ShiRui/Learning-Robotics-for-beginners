# 材质与纹理基础
## 一、材质节点的使用与理解
### （一）材质节点的基本概念
#### 1. 节点编辑器
材质节点是Blender中用于创建复杂材质和纹理的工具。通过节点编辑器，可以将不同的节点连接起来，创建出各种效果。节点编辑器位于Blender界面的底部编辑器区域，可以通过选择“Shader Editor”（着色器编辑器）来打开。
#### 2. 常用节点
- **Principled BSDF**：这是Blender中最常用的材质节点，可以模拟各种真实世界的材质效果，如塑料、金属、玻璃等。它包含多个参数，如基础颜色、粗糙度、金属度等。

- **Material Output**：这是材质输出节点，所有材质节点的最终输出都连接到这个节点。

- **Texture Coordinate**：提供纹理坐标，用于控制纹理在模型上的映射方式。

- **Mapping**：用于调整纹理的缩放、旋转和平移。

- **Image Texture**：用于加载和显示图像纹理。

- **Bump**：用于创建凹凸效果，使模型表面看起来更加真实。
### （二）创建和连接节点
#### 1. 创建节点
在节点编辑器中，点击“Shift + A”键，弹出添加节点菜单。可以选择需要的节点类型，如“Shader”“Texture”“Vector”等。
 例如，创建一个“Principled BSDF”节点和一个“Material Output”节点。
#### 2. 连接节点
选中一个节点，将鼠标指针移动到节点的输出端（通常是节点的右侧），按住鼠标左键不放，拖动鼠标到另一个节点的输入端（通常是节点的左侧），松开鼠标左键，完成连接。
例如，将“Principled BSDF”节点的“BSDF”输出端连接到“Material Output”节点的“Surface”输入端。
### （三）调整节点参数
#### 1. 调整Principled BSDF参数
- **基础颜色（Base Color）**：设置材质的基本颜色。可以点击颜色选择框，弹出颜色选择器，选择所需的颜色。

- **粗糙度（Roughness）**：控制材质表面的粗糙程度。数值越高，表面越粗糙，反射越模糊。

- **金属度（Metallic）**：控制材质的金属属性。数值越高，材质越接近金属效果。

- **透明度（Transmission）**：控制材质的透明度。数值越高，材质越透明。
#### 2. 调整Mapping节点参数
- **缩放（Scale）**：控制纹理的缩放比例。

- **旋转（Rotation）**：控制纹理的旋转角度。

- **平移（Location）**：控制纹理的平移位置。

## 二、基本纹理的创建与应用
### （一）创建图像纹理
#### 1. 加载图像纹理
- 在节点编辑器中，点击“Shift + A”键，添加一个“Image Texture”节点。

- 在“Image Texture”节点的属性面板中，点击“打开”按钮，选择需要的图像文件。
#### 2. 连接纹理节点
将“Image Texture”节点的“Color”输出端连接到“Principled BSDF”节点的“Base Color”输入端。
例如，加载一张木纹图像纹理，连接到“Principled BSDF”节点的“Base Color”输入端，可以使模型表面显示木纹效果。
### （二）创建程序纹理
#### 1. 添加程序纹理节点
 在节点编辑器中，点击“Shift + A”键，添加一个程序纹理节点，如“Noise Texture”“Voronoi Texture”等。例如，添加一个“Noise Texture”节点。
#### 2. 连接程序纹理节点
 将程序纹理节点的“Color”或“Fac”输出端连接到“Principled BSDF”节点的相应输入端。例如，将“Noise Texture”节点的“Fac”输出端连接到“Principled BSDF”节点的“Roughness”输入端，可以创建带有噪声效果的粗糙表面。

## 三、UV展开与贴图坐标
### （一）UV展开
#### 1. 概念
UV展开是将3D模型的表面展开成2D平面的过程，用于将2D纹理映射到3D模型上。UV展开的质量直接影响纹理在模型上的显示效果。
#### 2. UV展开操作
- 选中模型对象，按“Tab”键进入编辑模式。

- 在3D视图的工具栏中，点击“UV”菜单，选择“展开”选项。

- 选择合适的UV展开算法，如“智能投影”“展开”等。智能投影适用于简单的模型，展开适用于复杂的模型。
### （二）UV编辑器
#### 1. 打开UV编辑器
在Blender界面的底部编辑器区域，选择“UV Editor”（UV编辑器）。
#### 2. 调整UV岛
在UV编辑器中，可以看到模型的UV展开图。UV展开图由多个UV岛组成，每个UV岛对应模型的一个部分。可以使用鼠标左键点击并拖动UV岛，调整其位置。按“S”键可以缩放UV岛，按“R”键可以旋转UV岛。
### （三）贴图坐标
#### 1. 使用Texture Coordinate节点
- 在节点编辑器中，点击“Shift + A”键，添加一个“Texture Coordinate”节点。

- “Texture Coordinate”节点提供多种坐标类型，如“UV”“Object”“Generated”等。

- **UV坐标**：使用UV展开图的坐标，适用于大多数纹理映射。

- **Object坐标**：使用模型的局部坐标，适用于不需要UV展开的简单纹理映射。

- **Generated坐标**：自动生成的坐标，适用于一些程序纹理。
#### 2. 连接Texture Coordinate节点
将“Texture Coordinate”节点的“UV”输出端连接到“Mapping”节点的“Vector”输入端，再将“Mapping”节点的“Vector”输出端连接到“Image Texture”节点的“Vector”输入端。
例如，使用UV坐标将图像纹理映射到模型上，通过“Mapping”节点调整纹理的缩放、旋转和平移。

## 四、绘制贴图（配合代码）
### （一）、准备模型
#### 1. 创建或导入模型
首先，你需要一个3D模型。可以使用Blender自带的建模工具创建模型，或者导入外部模型文件（如OBJ、FBX等）。

```python
import bpy
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
```
### （二）、设置UV映射
#### 1. 进入编辑模式
选中模型，按`Tab`键进入编辑模式。
#### 2. 选择UV映射方式
在3D视图的工具栏中，点击“UV”菜单，选择合适的UV展开方式。常用的UV展开方式有“智能投影”“展开”等。

```python
bpy.ops.uv.smart_project()
```
#### 3. 调整UV岛
打开UV编辑器（在Blender界面的底部编辑器区域，选择“UV Editor”）。在UV编辑器中，可以看到模型的UV展开图。UV展开图由多个UV岛组成，每个UV岛对应模型的一个部分。使用鼠标左键点击并拖动UV岛，调整其位置。按`S`键可以缩放UV岛，按`R`键可以旋转UV岛。

```python
bpy.ops.uv.select_all(action='SELECT')
bpy.ops.transform.translate(value=(0.1, 0.1, 0.0))
bpy.ops.transform.resize(value=(1.1, 1.1, 1.0))
```
### （三）、绘制纹理
#### 1. 创建纹理图像
在UV编辑器中，点击“新建”按钮，创建一个新的纹理图像。设置图像的尺寸和格式。

```python
bpy.ops.image.new(name="Texture", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False)
```
#### 2. 进入纹理绘制模式
在3D视图中，按`Tab`键切换到绘制模式（Texture Paint模式）。
#### 3. 选择绘制工具
在工具栏中，选择绘制工具，如“画笔”“橡皮擦”等。可以调整画笔的大小、强度和颜色。

```python
bpy.context.scene.tool_settings.image_paint.brush.size = 50
bpy.context.scene.tool_settings.image_paint.brush.strength = 0.5
bpy.context.scene.tool_settings.image_paint.brush.color = (1.0, 0.0, 0.0)  # 红色
```
#### 4. 绘制纹理
在3D视图中，使用鼠标左键在模型表面绘制纹理。可以按住`Shift`键进行精细绘制。
### （四）、应用纹理到模型上
#### 1. 创建材质
选中模型，进入材质属性面板（图标是一个小球）。点击“新建”按钮，创建一个新的材质。
#### 2. 添加纹理节点
在节点编辑器中，点击`Shift + A`键，添加一个“Image Texture”节点。选择刚才创建的纹理图像：

```python
bpy.data.images['Texture'].filepath = 'D:/Path/To/Your/Texture.png'
```
#### 3. 连接节点
将“Image Texture”节点的“Color”输出端连接到“Principled BSDF”节点的“Base Color”输入端。

```python
bpy.data.materials['Material'].node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (1.0, 0.0, 0.0, 1.0)
bpy.data.materials['Material'].node_tree.links.new(
bpy.data.materials['Material'].node_tree.nodes['Principled BSDF'].inputs['Base Color'],
bpy.data.materials['Material'].node_tree.nodes['Image Texture'].outputs['Color']
)
```
#### 4. 设置UV坐标
在节点编辑器中，点击`Shift + A`键，添加一个“Texture Coordinate”节点。

将“Texture Coordinate”节点的“UV”输出端连接到“Mapping”节点的“Vector”输入端，再将“Mapping”节点的“Vector”输出端连接到“Image Texture”节点的“Vector”输入端。

```python
bpy.data.materials['Material'].node_tree.links.new(
bpy.data.materials['Material'].node_tree.nodes['Mapping'].inputs['Vector'],
bpy.data.materials['Material'].node_tree.nodes['Texture Coordinate'].outputs['UV']
)
bpy.data.materials['Material'].node_tree.links.new(
bpy.data.materials['Material'].node_tree.nodes['Image Texture'].inputs['Vector'],
bpy.data.materials['Material'].node_tree.nodes['Mapping'].outputs['Vector']
)
```
### （五）、渲染和输出
#### 1. 渲染设置
 在渲染属性面板中，设置渲染的分辨率、帧范围、采样次数和输出路径。选择合适的渲染引擎（如Eevee或Cycles），进行渲染。

```python
bpy.context.scene.render.resolution = 1920
bpy.context.scene.render.resolution_y = 1080
```
#### 2. 输出设置
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