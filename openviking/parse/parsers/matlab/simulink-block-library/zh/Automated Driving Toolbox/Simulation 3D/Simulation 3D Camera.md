---
type: simulink-block
title: 'Simulation 3D Camera'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dcamera'
documentation_source_path: 'ref/simulation3dcamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Camera

## 端口
```yaml
ports:
- name: Rel Translation
  summary: 传感器相对于安装点的相对平移 (m) [0 0 0]（默认）| 形式为 [*X* *Y* *Z*] 的实值 1×3 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Rel Rotation
  summary: 传感器相对于安装点的相对旋转 (deg) [0 0 0]（默认）| 形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Image
  summary: 3D 输出相机图像 *m*×*n*×3 的 RGB 三元组值数组
  direction: output
  data_types: int8 | uint8
- name: Depth
  summary: 从 0 m 到 1000 m 的物体深度 *m*×*n* 的物体深度数组
  direction: output
  data_types: double
- name: Labels
  summary: 标签标识符 *m*×*n* 的标签标识符数组
  direction: output
  data_types: uint8
- name: Translation
  summary: 传感器位置 实值 1×3 向量
  direction: output
  data_types: double
- name: Rotation
  summary: 传感器方向 实值 1×3 向量
  direction: output
  data_types: double
```

### 输入

### **Rel Translation** — 传感器相对于安装点的相对平移 (m) `[0 0 0]`（默认）| 形式为 [*X* *Y* *Z*] 的实值 1×3 向量

传感器相对于车辆上安装点的相对平移，以米为单位，指定为形式为 [*X*
*Y*
*Z*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请选择 **Relative
translation [X, Y, Z] (m)** 参数旁边的 **Input** 参数。有关更多详细信息，请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rel Rotation** — 传感器相对于安装点的相对旋转 (deg) `[0 0 0]`（默认）| 形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量

传感器相对于车辆上安装点的相对旋转，以度为单位，指定为形式为 [*Roll*
*Pitch*
*Yaw*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请选择 **Relative
rotation [Roll, Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数。有关更多详细信息，
请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Image** — 3D 输出相机图像 *m*×*n*×3 的 RGB 三元组值数组

3D 输出相机图像，以 *m*×*n*×3 的 RGB 三元组值数组形式返回。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`

### **Depth** — 从 0 m 到 1000 m 的物体深度 *m*×*n* 的物体深度数组

图像中每个像素的物体深度，以
*m*×*n* 数组形式输出。*m* 是图像的
垂直分辨率，*n* 是图像的
水平分辨率。深度范围为 0 到 1000 米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择
**Output depth**。

**数据类型：** `double`

### **Labels** — 标签标识符 *m*×*n* 的标签标识符数组

图像中每个像素的标签标识符，以
*m*×*n* 数组形式输出。*m* 是图像的
垂直分辨率，*n* 是图像的
水平分辨率。

下表显示了可从 Simulation 3D Scene Configuration 模块选择的默认场景中使用的物体 ID。如果您使用的是自定义场景，
在 Unreal® Editor 中，您可以将新的物体类型分配给未使用的 ID。有关更多详细信息，请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果
场景包含未分配 ID 的物体，则该物体被分配
ID `0`。不支持车道标记的检测。

| ID | 类型 |
| --- | --- |
| `0` | 无/默认 |
| `1` | 建筑物 |
| `2` | *未使用* |
| `3` | 其他 |
| `4` | 行人 |
| `5` | 杆 |
| `6` | 车道标记 |
| `7` | 道路 |
| `8` | 人行道 |
| `9` | 植被 |
| `10` | 车辆 |
| `11` | *未使用* |
| `12` | 通用交通标志 |
| `13` | 停车标志 |
| `14` | 让行标志 |
| `15` | 限速标志 |
| `16` | 限重标志 |
| `17-18` | *未使用* |
| `19` | 左右箭头警告标志 |
| `20` | 左向箭头警告标志 |
| `21` | 右向箭头警告标志 |
| `22` | *未使用* |
| `23` | 右单行道标志 |
| `24` | *未使用* |
| `25` | 仅校车标志 |
| `26-38` | *未使用* |
| `39` | 人行横道标志 |
| `40` | *未使用* |
| `41` | 交通信号灯 |
| `42` | 右弯警告标志 |
| `43` | 左弯警告标志 |
| `44` | 右上箭头警告标志 |
| `45-47` | *未使用* |
| `48` | 铁路道口标志 |
| `49` | 街道标志 |
| `50` | 环岛警告标志 |
| `51` | 消防栓 |
| `52` | 出口标志 |
| `53` | 自行车道标志 |
| `54-56` | *未使用* |
| `57` | 天空 |
| `58` | 路缘 |
| `59` | 立交匝道 |
| `60` | 道路护栏 |
| 61 | 骑自行车者 |
| `62-66` | *未使用* |
| `67` | 鹿 |
| `68-70` | *未使用* |
| `71` | 路障 |
| `72` | 摩托车 |
| `73-255` | *未使用* |

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择
**Output semantic segmentation**。

**数据类型：** `uint8`

**注意**

启用 `Labels` 需要将带有标签 `SemanticSegmentationSensor<N>` 的 `Sim 3D Semantic` actor
放置在同一位置。N 是传感器标识符。当启用
`Labels` 输出时，Simulation 3D Camera 模块会实例化
`Sim 3D Camera` 和 `Sim 3d Semantic`。

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴
和 *Z* 轴的位置。**Translation** 值位于场景的
世界坐标中。在此坐标系中，*Z* 轴从
地面向上指向。单位为米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择
**Output location
(m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、
*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。
**Rotation** 值位于场景的世界
坐标中。当沿这些轴的正方向观察时，这些值在顺时针方向上
为正。
单位为弧度。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上
选择 **Output
location (m) and orientation (rad)**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Sensor identifier
  summary: 唯一传感器标识符 1（默认）| 正整数
  group: 安装
- name: Parent name
  summary: 父车辆名称 Scene Origin（默认）| 车辆名称
  group: 安装
- name: Mounting location
  summary: 传感器安装位置 Origin（默认）| Front bumper | Rear bumper | Right mirror | Left mirror | Rearview mirror | Hood center | Roof
    center | ...
  group: 安装
- name: Specify offset
  summary: 指定相对于安装位置的偏移 off（默认）| on
  group: 安装
- name: Relative translation [X, Y, Z] (m)
  summary: 相对于安装位置的平移偏移 [0, 0, 0]（默认）| 实值 1×3 向量
  group: 安装
- name: Relative rotation [Roll, Pitch, Yaw] (deg)
  summary: 相对于安装位置的旋转偏移 [0, 0, 0]（默认）| 实值 1×3 向量
  group: 安装
- name: Sample time
  summary: 采样时间 -1（默认）| 正标量
  group: 安装
- name: Focal length (pixels)
  summary: 相机焦距 [1109, 1109]（默认）| 1×2 正整数向量
  group: 参数
- name: Optical center (pixels)
  summary: 相机光学中心 [640, 360]（默认）| 1×2 正整数向量
  group: 参数
- name: Image size (pixels)
  summary: 相机生成的图像大小 [720, 1280]（默认）| 1×2 正整数向量
  group: 参数
- name: Radial distortion coefficients
  summary: 径向畸变系数 [0, 0]（默认）| 实数值 2 元素向量 | 实数值 3 元素向量 | 实数值 6 元素向量
  group: 参数
- name: Tangential distortion coefficients
  summary: 切向畸变系数 [0, 0]（默认）| 实数值 2 元素向量
  group: 参数
- name: Axis skew
  summary: 相机轴的倾斜角 0（默认）| 非负实数值标量
  group: 参数
- name: Visualize field of view
  summary: 可视化相机视场的选项 off（默认）| on
  group: 参数
- name: Field of view range (m)
  summary: 可视化范围 61（默认）| 正实数值标量
  group: 参数
- name: Output depth
  summary: 输出深度图 off（默认）| on
  group: Ground Truth
- name: Output semantic segmentation
  summary: 输出标签 ID 的语义分割图 off（默认）| on
  group: Ground Truth
- name: Output location (m) and orientation (rad)
  summary: 输出传感器的位置和方向 off（默认）| on
  group: Ground Truth
```

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符
使您能够区分传感器。当您向模型添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N*
+ 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier**
值。

**示例：** `2`

### **Parent name** — 父车辆名称 `Scene Origin`（默认）| 车辆名称

传感器安装到的父对象名称，指定为 `Scene
Origin` 或模型中车辆的名称。您可以选择
的车辆名称对应于模型中
仿真 3D 车辆模块的 **Name** 参数。如果您选择 `Scene
Origin`，该模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name**
参数将传感器相对于场景或车辆原点放置。

- 当 **Parent name** 为 `Scene
  Origin` 时，该模块将传感器安装到场景
  原点。您只能将 **Mounting location** 设置为
  `Origin`。在仿真期间，传感器
  保持静止。
- 当 **Parent name** 为车辆名称时，该模块
  将传感器安装到表中描述的某个预定义安装位置。
  在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且位于车辆的几何中心（参见 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox）  传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装到前保险杠  传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠  传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 下向传感器，安装到右侧后视镜  传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 下向传感器，安装到左侧后视镜  传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装到车内后视镜  传感器安装在后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装到引擎盖中心  传感器安装在引擎盖中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装到车顶中心  传感器安装在车顶中心的车辆 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针方向为正。当
从上方观察车辆时，偏航角（方向角）为
逆时针方向为正，因为您是沿轴的负方向
观察的。

传感器相对于车辆的
*X*-*Y*-*Z* 安装
位置取决于车辆类型。要指定
车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with
Ground Following 的 **Type** 参数。要获取
某车辆类型的
*X*-*Y*-*Z* 安装
位置，请参阅该车辆的参考页。

要确定传感器在世界坐标中的位置，请打开传感器模块。然后，
在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation
(rad)** 参数并检查来自
**Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）| `on`

选择此参数可通过 **Relative
translation [X, Y, Z] (m)** 和 **Relative
rotation [Roll, Pitch, Yaw] (deg)**
参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为
形式为 [*X*, *Y*,
*Z*] 的实值 1×3 向量。单位为
米。

如果您通过将 **Parent name** 设置为某车辆的名称来将传感器安装到
该车辆，则
*X*、*Y* 和 *Z* 位于
车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，
  当沿车辆的前进方向观察时。
- *Z* 轴向上指向。

原点是 **Mounting
location** 参数中指定的安装位置。此原点不同于车辆原点，
车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene
Origin` 来将传感器安装到
场景原点，则 *X*、*Y* 和
*Z* 位于场景的世界坐标中。

有关车辆和
世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,0.01]`

#### 在仿真期间调整相对平移

要在仿真期间调整传感器的相对平移，请通过选择
**Relative translation [X,
Y, Z] (m)** 参数旁边的 **Input** 参数来启用
**Rel Translation** 输入端口。有关此传感器的相对平移和
旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为
形式为 [*Roll*,
*Pitch*, *Yaw*] 的实值 1×3 向量。横滚、俯仰和偏航分别是
绕 *X* 轴、*Y* 轴和
*Z* 轴的旋转角。单位为
度。

如果您通过将 **Parent name** 设置为某车辆的名称来将传感器安装到
该车辆，则
*X*、*Y* 和 *Z* 位于
车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，
  当沿车辆的前进方向观察时。
- *Z* 轴向上指向。
- 当分别沿 *X* 轴、*Y* 轴
  和 *Z* 轴的前进方向观察时，横滚、俯仰和偏航为顺时针方向为正。如果您从 2D
  俯视视角观察场景，则偏航角（也称为方向角）
  为逆时针方向为正，因为您是沿 *Z* 轴的
  负方向观察场景的。

原点是 **Mounting
location** 参数中指定的安装位置。此原点不同于车辆原点，
车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene
Origin` 来将传感器安装到
场景原点，则 *X*、*Y* 和
*Z* 位于场景的世界坐标中。

有关车辆和世界
坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,10]`

#### 在仿真期间调整相对旋转

要在仿真期间调整传感器的相对旋转，请通过选择
**Relative rotation [Roll,
Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数来启用
**Rel Rotation** 输入端口。有关此传感器的相对
平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真
环境帧率是采样时间的倒数。

如果您将采样时间设置为 `-1`，则该模块从
Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

这些固有相机参数等效于 `cameraIntrinsics` 对象的属性。要获取相机的固有参数，请使用
Camera Calibrator 应用程序。固有相机
参数的任意组合都会产生无效图像。Simulation 3D Camera 模块支持最大 95 度且带畸变的视场角。有关不同
相机模型的最大视场角列表，请参阅 Fisheye Calibration Basics。

有关相机标定过程的详细信息，请参阅 Using the Single Camera Calibrator App 和
What Is Camera Calibration?。

### **Focal length (pixels)** — 相机焦距 `[1109, 1109]`（默认）| 1×2 正整数向量

将相机的焦距指定为形式为
[*fx*, *fy*] 的 1×2 正整数向量。单位为像素。

*fx* = *F* ×
*sx*

*fy* = *F* ×
*sy*

其中：

- *F* 是以世界单位表示的焦距，通常
  为毫米。
- [*sx*, *sy*] 分别是 *x* 和 *y* 方向上每
  世界单位的像素数。

此参数等效于 `cameraIntrinsics` 对象的 `FocalLength`
属性。

### **Optical center (pixels)** — 相机光学中心 `[640, 360]`（默认）| 1×2 正整数向量

将相机的光学中心指定为形式为
[*cx*,*cy*] 的 1×2 正整数向量。单位为像素。

此参数等效于 `cameraIntrinsics`
对象的 `PrincipalPoint` 属性。

### **Image size (pixels)** — 相机生成的图像大小 `[720, 1280]`（默认）| 1×2 正整数向量

将相机生成的图像大小指定为形式为
[*mrows*,*ncols*] 的 1×2 正整数向量。单位为像素。
您可以指定的最大图像大小为 `[1080,1920]`。

此参数等效于 `cameraIntrinsics` 对象的 `ImageSize`
属性。

### **Radial distortion coefficients** — 径向畸变系数 `[0, 0]`（默认）| 实数值 2 元素向量 | 实数值 3 元素向量 | 实数值 6 元素向量

将径向畸变系数指定为实数值 2 元素、3 元素或 6 元素向量。径向畸变是图像点沿从主点延伸的径向线的位移。

- 当图像点远离主点（正径向位移）时，图像放大率减小，图像上出现枕形畸变。
- 当图像点向主点移动（负径向位移）时，图像放大率增大，图像上出现桶形畸变。

相机传感器使用双系数、三系数或六系数公式计算点的 (*x*d,*y*d) 径向畸变位置。下表显示了各种公式，其中：

- (*x*,*y*) = 未畸变像素位置
- *k*1,*k*2,*k*3,*k*4,*k*5,*k*6 = 镜头的径向畸变系数
- *r*2 = *x*2 + *y*2

|  |  |  |
| --- | --- | --- |
| **系数** | **公式** | **描述** |
| `[k1, k2]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` 属性所使用的双系数模型。 |
| `[k1, k2, k3]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` 属性所使用的三系数模型。 |
| `[k1, k2, k3, k4, k5, k6]` | xd=x×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6yd=y×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6 | 六系数模型基于 OpenCV 径向畸变模型。  **注意**  Camera Calibrator 应用不支持此模型。要使用此模型校准相机，请参阅 OpenCV 文档中的 Camera Calibration and 3D Reconstruction。 |

### **Tangential distortion coefficients** — 切向畸变系数 `[0, 0]`（默认）| 实数值 2 元素向量

将切向畸变系数指定为实数值 2 元素向量。当镜头与图像平面不平行时，会发生切向畸变。

零切向畸变与切向畸变的比较。

相机传感器使用以下公式计算点的切向畸变位置 (*x*d, *y*d)：

*x*d = *x* + [2*p*1*xy* + *p*2 × (*r*2 + 2*x*2)]

*y*d = *y* + [*p*1 × (*r*2 + 2*y*2) + 2*p*2*xy*]

其中：

- *x*, *y* = 未畸变像素位置
- *p*1, *p*2 = 镜头的切向畸变系数
- *r*2 = *x*2 + *y*2

未畸变像素位置以归一化图像坐标表示，原点位于光学中心。坐标以世界单位表示。

此参数等效于 `cameraIntrinsics` 对象的 `TangentialDistortion` 属性。

### **Axis skew** — 相机轴的倾斜角 `0`（默认）| 非负实数值标量

将相机轴的倾斜角指定为非负实数值标量。如果 *X* 轴和 *Y* 轴完全垂直，则倾斜角必须为 `0`。单位为无量纲。

此参数等效于 `cameraIntrinsics` 对象的 `Skew` 属性。

### **Visualize field of view** — 可视化相机视场的选项 `off`（默认）| `on`

*自 R2025a 起*

选择此参数以在 3D 环境中可视化相机覆盖范围。此参数可使用分段球体可视化视场，以标注视场的边界和范围。

### **Field of view range (m)** — 可视化范围 `61`（默认）| 正实数值标量

*自 R2025a 起*

指定相机覆盖范围的可视化范围。此参数设置分段球体的半径。单位为米。

#### 依赖关系

要启用此参数，请选择 **Visualize field of view** 参数。

### Ground Truth

### **Output depth** — 输出深度图 `off`（默认）| `on`

选择此参数以在 **Depth** 端口输出深度图。

### **Output semantic segmentation** — 输出标签 ID 的语义分割图 `off`（默认）| `on`

选择此参数以在 **Labels** 端口输出标签 ID 的语义分割图。

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。
## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2025a: 可视化相机视场

使用 **Parameters** 选项卡中的这些参数可在 3D 环境中可视化相机视场并设置相机覆盖范围的可视化范围。

- **Visualize field of view**
- **Field of view range (m)**

### R2025a: 性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧率和模型执行时间。

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Camera 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中带镜头的相机传感器模型

**注意**

使用 Simulation 3D Camera 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Camera 模块提供与 3D 仿真环境中带镜头相机的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该传感器基于理想针孔相机模型，并添加了镜头以表示完整的相机模型，包括镜头畸变。此相机模型支持高达 150 度的视场且无畸变。有关更多详细信息，请参阅 Algorithms。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含 Simulation 3D Scene Configuration 模块。

该模块输出仿真期间相机捕获的图像。您可以使用这些图像来可视化和验证您的驾驶算法。此外，在 **Ground Truth** 选项卡上，您可以选择选项来输出用于开发深度估计和语义分割算法的真值数据。您还可以输出相机在场景世界坐标系中的位置和方向。图中显示了启用所有端口时的模块。

启用所有端口时的 Simulation 3D Camera 模块

下表总结了端口以及如何启用它们。

| 端口 | 描述 | 用于启用端口的参数 | 示例可视化 |
| --- | --- | --- | --- |
| **Image** | 输出相机捕获的 RGB 图像 | 不适用 | 城市场景的示例图像输出 |
| **Depth** | 输出值为 0 m 到 1000 米的深度图 | **Output depth** | 城市场景的示例深度输出 |
| **Labels** | 输出与场景中对象对应的标签 ID 的语义分割图 | **Output semantic segmentation** | 城市场景的示例图像语义分割 |
| **Translation** | 输出相机在世界坐标系中的位置 | **Output location (m) and orientation (rad)** | 不适用 |
| **Rotation** | 输出相机在世界坐标系中的方向 | **Output location (m) and orientation (rad)** | 不适用 |

**注意**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Camera 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Camera 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
