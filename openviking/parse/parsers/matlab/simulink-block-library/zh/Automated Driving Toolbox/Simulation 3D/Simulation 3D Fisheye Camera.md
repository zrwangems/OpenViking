---
type: simulink-block
title: 'Simulation 3D Fisheye Camera'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dfisheyecamera'
documentation_source_path: 'ref/simulation3dfisheyecamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Fisheye Camera

## 端口

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
rotation [Roll, Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数。有关更多详细信息，请参阅 Sensor Position Transformation。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Image** — 3D 输出相机图像 *m*×*n*×3 的 RGB 三元组值数组

3D 输出相机图像，以 *m*×*n*×3 的 RGB 三元组值数组形式返回。*m* 是图像的垂直分辨率，*n* 是图像的水平分辨率。

**数据类型：** `int8` | `uint8`

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标系中。在此坐标系中，*Z* 轴从地面向上指向。单位为米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location
(m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。**Rotation** 值位于场景的世界坐标系中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位为弧度。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output
location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型添加新传感器模块时，该模块的 **Sensor identifier** 为 *N*
+ 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父车辆名称 `Scene Origin`（默认）| 车辆名称

传感器安装到的父对象名称，指定为 `Scene
Origin` 或模型中车辆的名称。您可以选择车辆名称对应于模型中 Simulation 3D Vehicle 模块的 **Name** 参数。如果选择 `Scene
Origin`，该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器相对于场景或车辆原点放置。

- 当 **Parent name** 为 `Scene
  Origin` 时，该模块将传感器安装到场景原点。您只能将 **Mounting location** 设置为
  `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的预定义安装位置之一。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且位于车辆的几何中心（请参阅 Automated Driving Toolbox 中 Unreal Engine 仿真的坐标系） 传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装到前保险杠 传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠 传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装到右侧后视镜 传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装到左侧后视镜 传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装到车内后视镜 传感器安装在车内后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装到引擎盖中心 传感器安装在引擎盖中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装到车顶中心 传感器安装在车顶中心的车辆 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针方向为正。当从上方观察车辆时，偏航角（方向角）为逆时针方向为正，因为您是沿轴的负方向观察的。

传感器相对于车辆的
*X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with
Ground Following 的 **Type** 参数。要获取车辆类型的
*X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器在世界坐标系中的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation
(rad)** 参数，并检查来自 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）| `on`

选择此参数以通过使用 **Relative
translation [X, Y, Z] (m)** 和 **Relative
rotation [Roll, Pitch, Yaw] (deg)**
参数来指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*,
*Z*] 的实值 1×3 向量。单位为米。

如果您通过将 **Parent name** 设置为车辆名称来将传感器安装到该车辆，则
*X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，如沿车辆前方方向观察时所见。
- *Z* 轴向上指向。

原点是 **Mounting
location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene
Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和
*Z* 位于场景的世界坐标系中。

有关车辆和世界坐标系的更多详细信息，请参阅 Automated Driving Toolbox 中 Unreal Engine 仿真的坐标系。

**示例：** `[0,0,0.01]`

#### 在仿真期间调整相对平移

要在仿真期间调整传感器的相对平移，请通过选择 **Relative translation [X,
Y, Z] (m)** 参数旁边的 **Input** 参数来启用 **Rel Translation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*,
*Pitch*, *Yaw*] 的实值 1×3 向量。横滚、俯仰和偏航分别是绕 *X* 轴、*Y* 轴和
*Z* 轴的旋转角度。单位为度。

如果您通过将 **Parent name** 设置为车辆名称来将传感器安装到该车辆，则
*X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，如沿车辆前方方向观察时所见。
- *Z* 轴向上指向。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针方向为正。如果您从 2D 俯视视角观察场景，则偏航角（也称为方向角）为逆时针方向为正，因为您是沿 *Z* 轴的负方向观察场景的。

原点是 **Mounting
location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene
Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和
*Z* 位于场景的世界坐标系中。

有关车辆和世界坐标系的更多详细信息，请参阅 Automated Driving Toolbox 中 Unreal Engine 仿真的坐标系。

**示例：** `[0,0,10]`

#### 在仿真期间调整相对旋转

要在仿真期间调整传感器的相对旋转，请通过选择 **Relative rotation [Roll,
Pitch, Yaw] (deg)** 参数旁边的 **Input** 参数来启用 **Rel Rotation** 输入端口。有关此传感器的相对平移和旋转的更多详细信息，请参阅 Sensor Position Transformation。

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

这些固有相机参数等效于 `fisheyeIntrinsics`
对象的属性。要获取相机的固有参数，请使用 Camera
Calibrator 应用程序。

有关鱼眼相机标定过程的详细信息，请参阅 Using the Single Camera Calibrator App 和
Fisheye Calibration Basics。

### **Distortion center (pixels)** — 畸变中心 `[640, 360]`（默认）| 实值 1×2 向量

畸变中心，指定为实值 2 元素向量。单位为像素。

### **Image size (pixels)** — 相机生成的图像大小 `[720, 1280]`（默认）| 正整数的实值 1×2 向量

相机生成的图像大小，指定为形式为 [*mrows*,*ncols*] 的正整数实值 1×2 向量。单位为像素。

### **Mapping coefficients** — 投影函数的多项式系数 `[320, 0, 0, 0]`（默认）| 实值 1×4 向量

由 Scaramuzza 的泰勒模型 [1] 描述的投影函数的多项式系数，指定为形式为 `[a0 a2 a3 a4]` 的实值
1×4 向量。

**示例：** `[320, -0.001, 0, 0]`

### **Stretch matrix** — 将点从传感器平面变换到相机平面 `[1, 0; 0, 1]`（默认）| 实值 2×2 矩阵

将点从传感器平面变换到相机图像平面中的像素。当镜头不平行于传感器时，在数字化过程中会发生未对准。

**示例：** `[0, 1; 0, 1]`

### Ground Truth

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Translation** 和
**Rotation** 端口输出传感器的平移和旋转。

## 所属库

UAV Toolbox / Simulation 3D Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2025a：性能优化

Unreal Engine 可执行文件中的传感器模型现在以 Simulation 3D 模块中设置的相同采样率运行。此软件更新提高了帧速率和模型执行时间。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Fisheye Camera 模块仿真模型需要
Simulink
3D Animation。

## 描述

3D 仿真环境中的鱼眼相机传感器模型

**注意**

使用 Simulation 3D Fisheye Camera 模块仿真模型需要
Simulink®
3D Animation™ 和 Computer Vision Toolbox™。

Simulation 3D Fisheye Camera 模块提供与 3D 仿真环境中带有鱼眼镜头的相机的接口。此环境使用 Epic Games® 的
Unreal Engine® 渲染。该传感器基于 Scaramuzza [1] 提出的鱼眼相机模型。此模型支持高达 195 度的视场。该模块输出具有指定相机畸变和大小的图像。您还可以输出相机在场景世界坐标系中的位置和方向。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration
模块必须在 Simulation 3D Fisheye Camera 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D
Fisheye Camera 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General**
选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Fisheye Camera — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
