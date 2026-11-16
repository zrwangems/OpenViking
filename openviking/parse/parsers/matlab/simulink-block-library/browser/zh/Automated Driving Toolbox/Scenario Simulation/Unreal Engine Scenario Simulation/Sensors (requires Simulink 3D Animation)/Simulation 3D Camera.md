---
type: simulink-block
title: 'Simulation 3D Camera'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Sensors (requires Simulink 3D Animation)'
documentation_page: 'simulation3dcamera'
documentation_source_path: 'ref/simulation3dcamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Camera

## 端口

### 输入

### **Rel Translation** — 传感器相对于安装点的相对平移 (m) `[0 0 0]` (默认) | 形式为 [*X* *Y* *Z*] 的实值 1×3 向量

传感器相对于车辆上安装点的相对平移，以米为单位，指定为形式为 [*X* *Y* *Z*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请在 **相对平移 [X, Y, Z] (m)** 参数旁边选择 **输入** 参数。有关更多详细信息，请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rel Rotation** — 传感器相对于安装点的相对旋转 (deg) `[0 0 0]` (默认) | 形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量

传感器相对于车辆上安装点的相对旋转，以度为单位，指定为形式为 [*Roll* *Pitch* *Yaw*] 的实值 1×3 向量。

#### 依赖关系

要启用此端口，请在 **相对旋转 [Roll, Pitch, Yaw] (deg)** 参数旁边选择 **输入** 参数。有关更多详细信息，请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Image** — 3D 输出相机图像 *m*×*n*×3 RGB 三元组值数组

3D 输出相机图像，返回为 *m*×*n*×3 RGB 三元组值数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`

### **Depth** — 从 0 m 到 1000 m 的对象深度 *m*×*n* 对象深度数组

图像中每个像素的对象深度，输出为 *m*×*n* 数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。深度范围为 0 到 1000 米。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **输出深度**。

**数据类型：** `double`

### **Labels** — 标签标识符 *m*×*n* 标签标识符数组

图像中每个像素的标签标识符，输出为 *m*×*n* 数组。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

下表显示了可从 Simulation 3D Scene Configuration 模块选择的默认场景中使用的对象 ID。如果您使用的是自定义场景，则可以在 Unreal® Editor 中为未使用的 ID 分配新的对象类型。有关更多详细信息，请参阅 Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection。如果场景包含未分配 ID 的对象，则该对象会被分配 ID `0`。不支持车道标记的检测。

| ID | 类型 |
| --- | --- |
| `0` | None/default |
| `1` | Building |
| `2` | *未使用* |
| `3` | Other |
| `4` | Pedestrians |
| `5` | Pole |
| `6` | Lane Markings |
| `7` | Road |
| `8` | Sidewalk |
| `9` | Vegetation |
| `10` | Vehicle |
| `11` | *未使用* |
| `12` | Generic traffic sign |
| `13` | Stop sign |
| `14` | Yield sign |
| `15` | Speed limit sign |
| `16` | Weight limit sign |
| `17-18` | *未使用* |
| `19` | Left and right arrow warning sign |
| `20` | Left chevron warning sign |
| `21` | Right chevron warning sign |
| `22` | *未使用* |
| `23` | Right one-way sign |
| `24` | *未使用* |
| `25` | School bus only sign |
| `26-38` | *未使用* |
| `39` | Crosswalk sign |
| `40` | *未使用* |
| `41` | Traffic signal |
| `42` | Curve right warning sign |
| `43` | Curve left warning sign |
| `44` | Up right arrow warning sign |
| `45-47` | *未使用* |
| `48` | Railroad crossing sign |
| `49` | Street sign |
| `50` | Roundabout warning sign |
| `51` | Fire hydrant |
| `52` | Exit sign |
| `53` | Bike lane sign |
| `54-56` | *未使用* |
| `57` | Sky |
| `58` | Curb |
| `59` | Flyover ramp |
| `60` | Road guard rail |
| 61 | Bicyclist |
| `62-66` | *未使用* |
| `67` | Deer |
| `68-70` | *未使用* |
| `71` | Barricade |
| `72` | Motorcycle |
| `73-255` | *未使用* |

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **输出语义分割**。

**数据类型：** `uint8`

**注意**

启用 `Labels` 需要将带有标签 `SemanticSegmentationSensor<N>` 的 `Sim 3D Semantic` actor 放置在相同位置。N 是传感器标识符。当启用 `Labels` 输出时，Simulation 3D Camera 模块会实例化 `Sim 3D Camera` 和 `Sim 3d Semantic`。

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标中。在此坐标系中，*Z* 轴从地面向上指向。单位是米。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **输出位置 (m) 和方向 (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的滚转角、俯仰角和偏航角方向。**Rotation** 值位于场景的世界坐标中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位是弧度。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **输出位置 (m) 和方向 (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **传感器标识符** — 唯一传感器标识符 `1` (默认) | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型添加新的传感器模块时，该模块的 **传感器标识符** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **传感器标识符** 值。

**示例：** `2`

### **父级名称** — 父级车辆名称 `Scene Origin` (默认) | 车辆名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择车辆名称对应于模型中仿真 3D 车辆模块的 **Name** 参数。如果选择 `Scene Origin`，则该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **安装位置** — 传感器安装位置 `Origin` (默认) | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **父级名称** 参数将传感器放置在相对于场景或车辆原点的位置。

- 当 **父级名称** 为 `Scene Origin` 时，该模块将传感器安装到场景的原点。您只能将 **安装位置** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **父级名称** 为车辆名称时，该模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器安装在车辆原点，该原点位于地面上且位于车辆的几何中心（请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox） 传感器安装在原点处的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器安装在前保险杠 传感器安装在前保险杠处的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器安装在后保险杠 传感器安装在后保险杠处的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器安装在右侧后视镜 传感器安装在右侧后视镜处的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器安装在左侧后视镜 传感器安装在左侧后视镜处的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器安装在车内后视镜 传感器安装在车内后视镜处的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器安装在发动机罩中心 传感器安装在发动机罩中心处的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器安装在车顶中心 传感器安装在车顶中心处的车辆 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，滚转角、俯仰角和偏航角在顺时针方向为正。当从上方观察车辆时，偏航角（方向角）在逆时针方向为正，因为您是沿该轴的负方向观察的。

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器在世界坐标中的位置，请打开传感器模块。然后，在 **真值** 选项卡上，选择 **输出位置 (m) 和方向 (rad)** 参数，并检查 **Translation** 输出端口的数据。

### **指定偏移** — 指定相对于安装位置的偏移 `off` (默认) | `on`

选择此参数以使用 **相对平移 [X, Y, Z] (m)** 和 **相对旋转 [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **相对平移 [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]` (默认) | 实值 1×3 向量

传感器相对于安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。单位是米。

如果您通过将 **父级名称** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧（沿车辆前进方向观察时）。
- *Z* 轴指向上方。

原点是在 **安装位置** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **父级名称** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,0.01]`

#### 在仿真期间调整相对平移

要在仿真期间调整传感器的相对平移，请在 **相对平移 [X, Y, Z] (m)** 参数旁边选择 **输入** 参数以启用 **Rel Translation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **指定偏移**。

### **相对旋转 [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]` (默认) | 实值 1×3 向量

传感器相对于安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。滚转角、俯仰角和偏航角分别是绕 *X*、*Y* 和 *Z* 轴的旋转角度。单位是度。

如果您通过将 **父级名称** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧（沿车辆前进方向观察时）。
- *Z* 轴指向上方。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，滚转角、俯仰角和偏航角在顺时针方向为正。如果您从 2D 俯视视角观察场景，则偏航角（也称为方向角）在逆时针方向为正，因为您是沿 *Z* 轴的负方向观察场景。

原点是在 **安装位置** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **父级名称** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,10]`

#### 在仿真期间调整相对旋转

要在仿真期间调整传感器的相对旋转，请在 **相对旋转 [Roll, Pitch, Yaw] (deg)** 参数旁边选择 **输入** 参数以启用 **Rel Rotation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **指定偏移**。

### **采样时间** — 采样时间 `-1` (默认) | 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境帧速率是采样时间的倒数。

如果设置采样时间为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

这些固有相机参数等效于 `cameraIntrinsics` 对象的属性。要获取相机的固有参数，请使用 Camera Calibrator 应用。固有相机参数的任意组合会产生无效图像。Simulation 3D Camera 模块在存在畸变时支持最大 95 度视场。有关不同相机模型的最大视场列表，请参阅 Fisheye Calibration Basics。

有关相机标定过程的详细信息，请参阅 Using the Single Camera Calibrator App 和 What Is Camera Calibration?。

### **焦距 (pixels)** — 相机焦距 `[1109, 1109]` (默认) | 1×2 正整数向量

将相机焦距指定为形式为 [*fx*, *fy*] 的 1×2 正整数向量。单位是像素。

*fx* = *F* × *sx*

*fy* = *F* × *sy*

其中：

- *F* 是以世界单位表示的焦距，通常为毫米。
- [*sx*, *sy*] 分别是 *x* 和 *y* 方向上每世界单位的像素数。

此参数等效于 `cameraIntrinsics` 对象的 `FocalLength` 属性。

### **光学中心 (pixels)** — 相机光学中心 `[640, 360]` (默认) | 1×2 正整数向量

将相机光学中心指定为形式为 [*cx*,*cy*] 的 1×2 正整数向量。单位是像素。

此参数等效于 `cameraIntrinsics` 对象的 `PrincipalPoint` 属性。

### **图像大小 (pixels)** — 相机生成的图像大小 `[720, 1280]` (默认) | 1×2 正整数向量

将相机生成的图像大小指定为形式为 [*mrows*,*ncols*] 的 1×2 正整数向量。单位是像素。您可以指定的最大图像大小为 `[1080,1920]`。

此参数等效于 `cameraIntrinsics` 对象的 `ImageSize` 属性。

### **径向畸变系数** — 径向畸变系数 `[0, 0]` (默认) | 实值 2 元素向量 | 实值 3 元素向量 | 实值 6 元素向量

将径向畸变系数指定为实值 2 元素、3 元素或 6 元素向量。径向畸变是图像点沿从主点延伸的径向线的位移。

- 当图像点远离主点移动（正径向位移）时，图像放大率降低，图像上会出现枕形畸变。
- 当图像点向主点移动（负径向位移）时，图像放大率增加，图像上会出现桶形畸变。

相机传感器使用双系数、三系数或六系数公式计算某点的 (*x*d,*y*d) 径向畸变位置。下表显示了各种公式，其中：

- (*x*,*y*) = 未畸变像素位置
- *k*1,*k*2,*k*3,*k*4,*k*5,*k*6 = 镜头的径向畸变系数
- *r*2 = *x*2 + *y*2

|  |  |  |
| --- | --- | --- |
| **系数** | **公式** | **描述** |
| `[k1, k2]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` 属性使用的双系数模型。 |
| `[k1, k2, k3]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6) | 此模型等效于 `cameraIntrinsics` 对象的 `RadialDistortion` 属性使用的三系数模型。 |
| `[k1, k2, k3, k4, k5, k6]` | xd=x×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6yd=y×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6 | 六系数模型基于 OpenCV 径向畸变模型。  **注意**  Camera Calibrator 应用不支持此模型。要使用此模型标定相机，请参阅 OpenCV 文档中的 Camera Calibration and 3D Reconstruction。 |

### **切向畸变系数** — 切向畸变系数 `[0, 0]` (默认) | 实值 2 元素向量

将切向畸变系数指定为实值 2 元素向量。当镜头和图像平面不平行时，会发生切向畸变。

零切向畸变与切向畸变的比较。

相机传感器使用以下公式计算某点的切向畸变位置 (*x*d, *y*d)：

*x*d = *x* + [2*p*1*xy* + *p*2 × (*r*2 + 2*x*2)]

*y*d = *y* + [*p*1 × (*r*2 + 2*y*2) + 2*p*2*xy*]

其中：

- *x*, *y* = 未畸变像素位置
- *p*1, *p*2 = 镜头的切向畸变系数
- *r*2 = *x*2 + *y*2

未畸变像素位置出现在归一化图像坐标中，原点位于光学中心。坐标以世界单位表示。

此参数等效于 `cameraIntrinsics` 对象的 `TangentialDistortion` 属性。

### **轴倾斜** — 相机轴的倾斜角 `0` (默认) | 非负实值标量

将相机轴的倾斜角指定为非负实值标量。如果 *X* 轴和 *Y* 轴完全垂直，则倾斜角必须为 `0`。单位为无量纲。

此参数等效于 `cameraIntrinsics` 对象的 `Skew` 属性。

### **可视化视场** — 可视化相机视场的选项 `off` (默认) | `on`

*自 R2025a 起*

选择此参数以在 3D 环境中可视化相机覆盖范围。此参数支持使用分段球体可视化视场，以标注视场的边界和范围。

### **视场范围 (m)** — 可视化范围 `61` (默认) | 正实标量

*自 R2025a 起*

指定相机覆盖范围的可视化范围。此参数设置分段球体的半径。单位是米。

#### 依赖关系

要启用此参数，请选择 **可视化视场** 参数。

### 真值

### **输出深度** — 输出深度图 `off` (默认) | `on`

选择此参数以在 **Depth** 端口输出深度图。

### **输出语义分割** — 输出标签 ID 的语义分割图 `off` (默认) | `on`

选择此参数以在 **Labels** 端口输出标签 ID 的语义分割图。

### **输出位置 (m) 和方向 (rad)** — 输出传感器的位置和方向 `off` (默认) | `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2025a：可视化相机视场

使用 **参数** 选项卡中的这些参数可在 3D 环境中可视化相机视场，并设置相机覆盖范围的可视化范围。

- **可视化视场**
- **视场范围 (m)**

### R2025a：性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新改进了帧速率和模型执行时间。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Camera 模块仿真模型需要 Simulink 3D Animation。

## 描述

3D 仿真环境中带镜头的相机传感器模型

**注意**

使用 Simulation 3D Camera 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Camera 模块提供与 3D 仿真环境中带镜头的相机的接口。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该传感器基于理想针孔相机模型，并添加了镜头以表示完整的相机模型，包括镜头畸变。此相机模型在无畸变时支持高达 150 度的视场。有关更多详细信息，请参阅 Algorithms。

如果将 **采样时间** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含 Simulation 3D Scene Configuration 模块。

该模块输出仿真期间相机捕获的图像。您可以使用这些图像来可视化和验证您的驾驶算法。此外，在 **真值** 选项卡上，您可以选择选项以输出用于开发深度估计和语义分割算法的真值数据。您还可以输出相机在场景世界坐标系中的位置和方向。下图显示了启用所有端口的模块。

启用所有端口的 Simulation 3D Camera 模块

下表总结了端口以及如何启用它们。

| 端口 | 描述 | 用于启用端口的参数 | 示例可视化 |
| --- | --- | --- | --- |
| **Image** | 输出相机捕获的 RGB 图像 | 不适用 | 城市场景的示例图像输出 |
| **Depth** | 输出值从 0 m 到 1000 米的深度图 | **输出深度** | 城市场景的示例深度输出 |
| **Labels** | 输出与场景中对象对应的标签 ID 的语义分割图 | **输出语义分割** | 城市场景的示例图像语义分割 |
| **Translation** | 输出相机在世界坐标系中的位置 | **输出位置 (m) 和方向 (rad)** | 不适用 |
| **Rotation** | 输出相机在世界坐标系中的方向 | **输出位置 (m) 和方向 (rad)** | 不适用 |

**注意**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Camera 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Camera 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
