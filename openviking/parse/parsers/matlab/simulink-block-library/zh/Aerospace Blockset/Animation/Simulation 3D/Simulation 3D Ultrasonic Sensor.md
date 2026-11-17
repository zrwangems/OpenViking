---
type: simulink-block
title: 'Simulation 3D Ultrasonic Sensor'
family: 'animation'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dultrasonicsensor'
documentation_source_path: 'simulation3dultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ultrasonic Sensor

## 端口

### 输出

### **Has object** — 传感器视场内存在可检测对象，标量

传感器视场内存在可检测对象，以 Boolean 标量形式返回。如果对象到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小仅检测范围，则该对象被视为可检测。

### **Has range** — 传感器视场内存在的对象可以进行距离测量，标量

对于传感器视场内存在的对象，可以进行距离测量，以 Boolean 标量形式返回。对于视场中的任何对象，如果其到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小距离范围，则可以进行距离测量。

### **Range** — 到最近对象的距离测量，标量

到最近对象的距离测量值，以非负标量形式返回，单位为 meters。

### **Translation** — 传感器位置，实值 1-by-3 向量

传感器在场景 *X*-轴、*Y*-轴和 *Z*-轴上的位置。**Translation** 值位于场景的世界坐标中。在此坐标系中，*Z*-轴从地面向上指向。单位为 meters。

#### 依赖项

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向，实值 1-by-3 向量

传感器关于场景 *X*-轴、*Y*-轴和 *Z*-轴的横滚、俯仰和偏航方向。**Rotation** 值位于场景的世界坐标中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位为 radians。

#### 依赖项

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。将新传感器模块添加到模型时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin`（默认）| 车辆名称

传感器所安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择车辆名称，这些名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，该模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器放置在相对于场景或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的一个预定义安装位置。在仿真期间，传感器随车辆移动。

当分别沿 *X*-轴、*Y*-轴和 *Z*-轴的正方向观察时，横滚、俯仰和偏航为顺时针正。从上方观察车辆时，偏航角（方向角）为逆时针正，因为您是沿该轴的负方向观察。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）

选择此参数可通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1-by-3 向量

相对于传感器安装位置的平移偏移，指定为 [*X*, *Y*, *Z*] 形式的实值 1-by-3 向量。单位为 meters。

如果通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X*-轴从车辆向前指向。
- *Y*-轴指向车辆左侧（当沿车辆前进方向观察时）。
- *Z*-轴向上指向。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅基本坐标系概念。

**示例：** `[0,0,0.01]`

#### 依赖项

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移，实值 1-by-3 向量

相对于传感器安装位置的旋转偏移，指定为 [*Roll*, *Pitch*, *Yaw*] 形式的实值 1-by-3 向量。横滚、俯仰和偏航分别是绕 *X*-轴、*Y*-轴和 *Z*-轴的旋转角度。单位为 degrees。

如果通过将 **Parent name** 设置为车辆名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X*-轴从车辆向前指向。
- *Y*-轴指向车辆左侧（当沿车辆前进方向观察时）。
- *Z*-轴向上指向。
- 当分别沿 *X*-轴、*Y*-轴和 *Z*-轴的正方向观察时，横滚、俯仰和偏航为顺时针正。如果从 2D 俯视视角观察场景，则偏航角（也称为方向角）为逆时针正，因为您是沿 *Z*-轴的负方向观察场景。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆和世界坐标系的更多详细信息，请参阅基本坐标系概念。

**示例：** `[0,0,10]`

#### 依赖项

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以 seconds 为单位，指定为正标量。3D 仿真环境的帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 传感器参数

### **Detection ranges (m)** — 超声波传感器的检测范围向量 (m) `[0.03 0.15 5.5]`（默认）| 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1-by-3 非负实值向量

超声波传感器的检测范围向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1-by-3 非负实值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为 meters。这些值决定超声波传感器返回的检测和距离值。

- 当检测到的对象距离介于 `minDistRange` 和 `maxDistRange` 之间时，传感器返回正的距离值。
- 当检测到的对象距离介于 `minDetOnlyRange` 和 `minDistRange` 之间时，传感器检测到该对象，但无法确定距离并返回值 `0`。
- 当对象距离低于 `minDetOnlyRange` 或高于 `maxDistRange` 时，传感器返回空 cell array。

### **Horizontal field of view (deg)** — 超声波传感器的水平视场 `70`（默认）| 正实标量

超声波传感器的水平视场，指定为正实标量。此视场定义传感器在水平方向上跨越的总角度范围。必须在范围 (0, 180) 内指定水平视场 `horizontalFOV`。单位为 degrees。

### **Vertical field of view (deg)** — 超声波传感器的垂直视场 `35`（默认）| 正实标量

超声波传感器的垂直视场，指定为正实标量。此视场定义传感器在垂直方向上跨越的总角度范围。必须在范围 (0, 180) 内指定垂直视场。单位为 degrees。

### Ground Truth

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Automated Driving Toolbox / Simulation 3D Aerospace Blockset / Animation / Simulation 3D UAV Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Ultrasonic Sensor 模块仿真模型需要 Simulink 3D Animation。

### R2023b：新增 ground truth 参数

Simulation 3D Ultrasonic Sensor 模块现在具有 ground truth 参数，您可以启用该参数以输出传感器的位置和方向。

## 描述

3D 仿真环境中的超声波传感器模型

**注意**

使用 Simulation 3D Ultrasonic Sensor 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Ultrasonic Sensor 模块根据安装在自车上的超声波传感器在由 Epic Games® 的 Unreal Engine® 渲染的 3D 仿真环境中进行的距离测量生成检测。该模块基于传感器与检测对象上最近点之间的距离来计算距离测量值。

如果将 **Sample time** 设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您的模型中必须包含一个 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Ultrasonic Sensor 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Ultrasonic Sensor 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Sensor — `1`

有关执行顺序的更多信息，请参阅 Aerospace Blockset 的 3D 仿真工作原理。
