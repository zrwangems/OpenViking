---
type: simulink-block
title: 'Simulation 3D Camera'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dcamera'
documentation_source_path: 'ref/simulation3dcamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Camera

## 端口

### 输入

### **Rel Translation** — 传感器相对于安装点的相对平移 (m) `[0 0 0]` (default) | 形式为 [*X* *Y* *Z*] 的实值 1×3 向量

传感器相对于其在车辆上安装点的相对平移，以 meters 为单位，指定为形式为 [*X* *Y* *Z*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请选择 **Relative translation [X, Y, Z] (m)** 参数旁边的 **Input** 参数。有关更多详细信息，请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rel Rotation** — 传感器相对于安装点的相对旋转 (deg) `[0 0 0]` (default) | 形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量

传感器相对于其在车辆上安装点的相对旋转，以 degrees 为单位，指定为形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请选择 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数。有关更多详细信息，请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出

### **Image** — 3D 输出相机图像，*m*×*n*×3 的 RGB 三元组值数组

3D 输出相机图像，返回为 *m*×*n*×3 的 RGB 三元组值数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`

### **Depth** — 对象深度，从 0 m 到 1000 m，*m*×*n* 的对象深度数组

图像中每个像素的对象深度，输出为 *m*×*n* 数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。深度范围为 0 到 1000 meters。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output depth**。

**数据类型：** `double`

### **Labels** — 标签标识符，*m*×*n* 的标签标识符数组

图像中每个像素的标签标识符，输出为 *m*×*n* 数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

下表显示了可从 Simulation 3D Scene Configuration 模块中选择的默认场景中使用的对象 ID。如果您使用的是自定义场景，则可在 Unreal® Editor 中为未使用的 ID 分配新的对象类型.. 如果场景包含未分配 ID 的对象，则该对象会被分配 ID `0`。不支持检测车道标记。

| ID | 类型 |
| --- | --- |
| `0` | None/default |
| `1` | Building |
| `2` | *Not used* |
| `3` | Other |
| `4` | Pedestrians |
| `5` | Pole |
| `6` | Lane Markings |
| `7` | Road |
| `8` | Sidewalk |
| `9` | Vegetation |
| `10` | Vehicle |
| `11` | *Not used* |
| `12` | Generic traffic sign |
| `13` | Stop sign |
| `14` | Yield sign |
| `15` | Speed limit sign |
| `16` | Weight limit sign |
| `17-18` | *Not used* |
| `19` | Left and right arrow warning sign |
| `20` | Left chevron warning sign |
| `21` | Right chevron warning sign |
| `22` | *Not used* |
| `23` | Right one-way sign |
| `24` | *Not used* |
| `25` | School bus only sign |
| `26-38` | *Not used* |
| `39` | Crosswalk sign |
| `40` | *Not used* |
| `41` | Traffic signal |
| `42` | Curve right warning sign |
| `43` | Curve left warning sign |
| `44` | Up right arrow warning sign |
| `45-47` | *Not used* |
| `48` | Railroad crossing sign |
| `49` | Street sign |
| `50` | Roundabout warning sign |
| `51` | Fire hydrant |
| `52` | Exit sign |
| `53` | Bike lane sign |
| `54-56` | *Not used* |
| `57` | Sky |
| `58` | Curb |
| `59` | Flyover ramp |
| `60` | Road guard rail |
| 61 | Bicyclist |
| `62-66` | *Not used* |
| `67` | Deer |
| `68-70` | *Not used* |
| `71` | Barricade |
| `72` | Motorcycle |
| `73-255` | *Not used* |

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output semantic segmentation**。

**数据类型：** `uint8`

**注意**

启用 `Labels` 要求将带有标签 `SemanticSegmentationSensor<N>` 的 `Sim 3D Semantic` actor 放置在相同位置。N 是传感器标识符。当启用 `Labels` 输出时，Simulation 3D Camera 模块会实例化 `Sim 3D Camera` 和 `Sim 3d Semantic`。

### **Translation** — 传感器位置，实值 1×3 向量

传感器沿场景的 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标中。在该坐标系中，*Z* 轴从地面指向上方。单位为 meters。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器姿态，实值 1×3 向量

Roll、pitch 和 yaw 传感器姿态，围绕场景的 *X* 轴、*Y* 轴和 *Z* 轴。**Rotation** 值位于场景的世界坐标中。当沿这些轴的正方向观察时，这些值为顺时针正。单位为 radians。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1` (default) | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin` (default) | 车辆名称

传感器所安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择的车辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin` (default) | ...

传感器安装位置。默认情况下，模块根据 **Parent name** 参数将传感器放置在相对于场景原点或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，模块将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。

| Robot 安装位置 | 描述 | 相对于 Robot 原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到 Robot 原点，该原点位于地面上，即 Robot 车辆的几何中心，传感器安装在原点 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、pitch 和 yaw 为顺时针正。当从上方查看车辆时，yaw 角（方向角）为逆时针正，因为您沿轴的负方向查看。

传感器相对于 robot 的 (*X*, *Y*, *Z*) 安装位置取决于 robot 类型。要指定车辆类型，请使用您所安装到的 Simulation 3D Robot 模块的 **Type** 参数。要获取某 robot 类型的 (*X*, *Y*, *Z*) 安装位置，请参阅 Simulation 3D Robot 模块。

### **Specify offset** — 指定相对于安装位置的偏移 `off` (default) | `on`

选择此参数以通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]` (default) | 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。单位为 meters。

如果通过将 **Parent name** 设置为某车辆的名称来将传感器安装到该车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，如沿车辆前进方向查看时所见。
- *Z* 轴指向上方。

原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅 How Unreal Engine Simulation for Robots Works。

**示例：** `[0,0,0.01]`

#### 在仿真期间调整相对平移

要在仿真期间调整传感器的相对平移，请通过选择 **Relative translation [X, Y, Z] (m)** 参数旁边的 **Input** 参数来启用 **Rel Translation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]` (default) | 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。Roll、pitch 和 yaw 分别是绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。单位为 degrees。

如果通过将 **Parent name** 设置为某车辆的名称来将传感器安装到该车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，如沿车辆前进方向查看时所见。
- *Z* 轴指向上方。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、pitch 和 yaw 为顺时针正。如果从 2D 自上而下的视角观察场景，则 yaw 角（也称为方向角）为逆时针正，因为您是沿 *Z* 轴的负方向观察场景。

原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅 How Unreal Engine Simulation for Robots Works。

**示例：** `[0,0,10]`

#### 在仿真期间调整相对旋转

要在仿真期间调整传感器的相对旋转，请通过选择 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数来启用 **Rel Rotation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1` (default) | 正标量

模块的采样时间，以 seconds 为单位，指定为正标量。3D 仿真环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，模块将从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

这些相机内参等同于 `cameraIntrinsics` (Computer Vision Toolbox) 对象的属性。要获取相机的内参，请使用 Camera Calibrator app。任意组合的相机内参会产生无效图像。Simulation 3D Camera 模块支持带畸变的最大视场角 95 degrees。有关不同相机模型的最大视场角列表，请参阅 Fisheye Calibration Basics (Computer Vision Toolbox)。

有关相机校准过程的详细信息，请参阅 Using the Single Camera Calibrator App (Computer Vision Toolbox) 和 What Is Camera Calibration? (Computer Vision Toolbox)。

### **Focal length (pixels)** — 相机焦距 `[1109, 1109]` (default) | 1×2 正整数向量

将相机焦距指定为形式为 [*fx*, *fy*] 的 1×2 正整数向量。单位为 pixels。

*fx* = *F* ×
*sx*

*fy* = *F* ×
*sy*

其中：

- *F* 是焦距，以世界单位计，通常为 millimeters。
- [*sx*, *sy*] 分别是 *x* 和 *y* 方向上每个世界单位的像素数。

此参数等同于 `cameraIntrinsics` 对象的 `FocalLength` (Computer Vision Toolbox) 属性。

### **Optical center (pixels)** — 相机光学中心 `[640, 360]` (default) | 1×2 正整数向量

将相机光学中心指定为形式为 [*cx*,*cy*] 的 1×2 正整数向量。单位为 pixels。

此参数等同于 `cameraIntrinsics` 对象的 `PrincipalPoint` (Computer Vision Toolbox) 属性。

### **Image size (pixels)** — 相机产生的图像大小 `[720, 1280]` (default) | 1×2 正整数向量

将相机产生的图像大小指定为形式为 [*mrows*,*ncols*] 的 1×2 正整数向量。单位为 pixels。您可以指定的最大图像大小为 `[1080,1920]`。

此参数等同于 `cameraIntrinsics` 对象的 `ImageSize` (Computer Vision Toolbox) 属性。

### **径向畸变系数** — 径向畸变系数 `[0, 0]`（默认）| 实值 2 元素向量 | 实值 3 元素向量 | 实值 6 元素向量

将径向畸变系数指定为实值 2 元素、3 元素或 6 元素向量。径向畸变是图像点沿从主点延伸的径向线的位移。

- 当图像点远离主点（正径向位移）时，图像放大率减小，图像上会出现枕形畸变。
- 当图像点朝向主点移动（负径向位移）时，图像放大率增大，图像上会出现桶形畸变。

相机传感器使用双系数、三系数或六系数公式计算点的 (*x*d,*y*d) 径向畸变位置。下表显示了各种公式，其中：

- (*x*,*y*) = 无畸变像素位置
- *k*1,*k*2,*k*3,*k*4,*k*5,*k*6 = 镜头的径向畸变系数
- *r*2 = *x*2 + *y*2

|  |  |  |
| --- | --- | --- |
| **系数** | **公式** | **描述** |
| `[k1, k2]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` (Computer Vision Toolbox) 属性所使用的双系数模型。 |
| `[k1, k2, k3]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` (Computer Vision Toolbox) 属性所使用的三系数模型。 |
| `[k1, k2, k3, k4, k5, k6]` | xd=x×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6yd=y×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6 | 六系数模型基于 OpenCV 径向畸变模型。  **注意**  Camera Calibrator 应用程序不支持此模型。要使用此模型标定相机，请参阅 OpenCV 文档中的 Camera Calibration and 3D Reconstruction。 |

### **切向畸变系数** — 切向畸变系数 `[0, 0]`（默认）| 实值 2 元素向量

将切向畸变系数指定为实值 2 元素向量。当镜头与图像平面不平行时，会发生切向畸变。

零切向畸变与切向畸变的比较。

相机传感器使用以下公式计算点的切向畸变位置 (*x*d, *y*d)：

*x*d = *x* + [2*p*1*xy* + *p*2 × (*r*2 + 2*x*2)]

*y*d = *y* + [*p*1 × (*r*2 + 2*y*2) + 2*p*2*xy*]

其中：

- *x*, *y* = 无畸变像素位置
- *p*1, *p*2 = 镜头的切向畸变系数
- *r*2 = *x*2 + *y*2

无畸变像素位置出现在归一化图像坐标中，原点位于光学中心。坐标以世界单位表示。

此参数等效于 `cameraIntrinsics` 对象的 `TangentialDistortion` (Computer Vision Toolbox) 属性。

### **轴偏斜** — 相机坐标轴的偏斜角 `0`（默认）| 非负实值标量

将相机坐标轴的偏斜角指定为非负实值标量。如果 *X* 轴和 *Y* 轴完全垂直，则偏斜必须为 `0`。单位为无量纲。

此参数等效于 `cameraIntrinsics` 对象的 `Skew` (Computer Vision Toolbox) 属性。

### **可视化视场** — 用于可视化相机视场的选项 `off`（默认）| `on`

*自 R2025a 起*

选择此参数可在 3D 环境中可视化相机覆盖范围。此参数支持使用分段球体可视化视场，以标注视场的边界和范围。

### **视场范围 (m)** — 可视化范围 `61`（默认）| 正实数标量

*自 R2025a 起*

指定相机覆盖范围的可视化范围。此参数设置分段球体的半径。单位为米。

#### 依赖关系

要启用此参数，请选择 **可视化视场** 参数。

### 真值

### **输出深度** — 输出深度图 `off`（默认）| `on`

选择此参数可在 **Depth** 端口输出深度图。

### **输出语义分割** — 输出标签 ID 的语义分割图 `off`（默认）| `on`

选择此参数可在 **Labels** 端口输出标签 ID 的语义分割图。

### **输出位置 (m) 和方向 (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数可分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：可视化相机视场

使用 **参数** 选项卡中的这些参数，可在 3D 环境中可视化相机视场并设置相机覆盖范围的可视化范围。

- **可视化视场**
- **视场范围 (m)**

### R2025a：性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧率和模型执行时间。

## 描述

3D 仿真环境中带镜头的相机传感器模型

**注意**

使用 Simulation 3D Camera 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Camera 模块提供与 3D 仿真环境中带镜头相机的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该传感器基于理想针孔相机模型，并添加了镜头以表示完整的相机模型，包括镜头畸变。此相机模型支持高达 150 度的无畸变视场。有关更多详细信息，请参阅算法。

如果将 **采样时间** 设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，必须在模型中包含 Simulation 3D Scene Configuration 模块。

该模块输出仿真期间相机捕获的图像。可以使用这些图像来可视化和验证您的驾驶算法。此外，在 **真值** 选项卡上，您可以选择选项以输出真值数据，用于开发深度估计和语义分割算法。还可以输出相机在场景世界坐标系中的位置和方向。图中显示了启用所有端口的该模块。

启用所有端口的 Simulation 3D Camera 模块

下表汇总了端口以及如何启用它们。

| 端口 | 描述 | 用于启用端口的参数 | 示例可视化 |
| --- | --- | --- | --- |
| **Image** | 输出相机捕获的 RGB 图像 | n/a | 城市场景的示例图像输出 |
| **Depth** | 输出值为 0 m 到 1000 米的深度图 | **输出深度** | 城市场景的示例深度输出 |
| **Labels** | 输出与场景中对象相对应的标签 ID 的语义分割图 | **输出语义分割** | 城市场景的示例图像语义分割 |
| **Translation** | 输出相机在世界坐标系中的位置 | **输出位置 (m) 和方向 (rad)** | n/a |
| **Rotation** | 输出相机在世界坐标系中的方向 | **输出位置 (m) 和方向 (rad)** | n/a |

**注意**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Camera 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Camera 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Robots Works。
