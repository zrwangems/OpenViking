---
type: simulink-block
title: 'Simulation 3D Ultrasonic Array'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3dultrasonicarray'
documentation_source_path: 'simulation3dultrasonicarray.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ultrasonic Array

## 端口

### 输出

### **Has object** — 指示传感器视场内是否存在任何可检测对象的标志 `true` | `false`

指示传感器视场内是否存在任何可检测对象的标志，返回为逻辑标量。如果对象到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小仅检测范围，则认为该对象可检测。

### **Has range** — 指示传感器视场内是否存在任何对象可以进行距离测量的标志 `true` | `false`

指示传感器视场内是否存在任何对象可以进行距离测量的标志，返回为逻辑标量。对于视场内的任何对象，如果其到传感器的最近距离大于 `Detection ranges (m)` 参数中指定的最小距离范围，则可以进行距离测量。

### **Range** — 到最近对象的距离测量值 非负标量

到最近对象的距离测量值，返回为非负标量。

### **Translation** — 传感器位置 实值 1×3 向量

传感器在场景 *X* 轴、*Y* 轴和 *Z* 轴上的位置。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1` （默认） | 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符可用于区分传感器。当向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级车辆名称 `Scene Origin` （默认） | 车辆名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中车辆的名称。可以选择的车辆名称对应于模型中 Simulation 3D 车辆模块的 **Name** 参数。如果选择 `Scene Origin`，该模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Coordinate system** — 执行器变换的坐标系 `Default` （默认） | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定 actor 在 3D 环境中用于平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB® 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `MATLAB`

### **Mounting location** — 传感器安装位置 `Origin` （默认） | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块会将传感器相对于场景原点或车辆原点放置，具体取决于 **Parent name** 参数。

- 当 **Parent name** 为 `Scene Origin` 时，该模块会将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块会将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。例如，下表提供了 ISO 8855 标准坐标系中的安装位置。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且处于车辆的几何中心（请参阅 Coordinate Systems in Simulink 3D Animation）  车辆传感器安装在原点 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装到前保险杠  车辆传感器安装在前保险杠 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠  车辆传感器安装在后保险杠 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装到右侧后视镜  车辆传感器安装在右侧后视镜 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装到左侧后视镜  车辆传感器安装在左侧后视镜 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装到车内后视镜  车辆传感器安装在车内后视镜 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装到发动机罩中心  车辆传感器安装在发动机罩中心 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装到车顶中心  车辆传感器安装在车顶中心 | [0, 0, 0] |

传感器的 *X*-*Y*-*Z* 安装位置相对于车辆取决于车辆类型。要指定车辆类型，请使用传感器所安装到的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器的位置，请打开传感器模块。然后，在 **真值** 选项卡上，选择 **Output location and orientation** 参数，并检查 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off` （默认） | `on`

选择此参数以使用 **Relative translation [X, Y, Z]** 和 **Relative rotation [Roll, Pitch, Yaw]** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移 `[0, 0, 0]` （默认） | 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。

你可以通过将 **Parent name** 设置为该车辆的名称，将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。你还可以通过将 **Parent name** 设置为 `Scene Origin`，将传感器安装到场景原点。

有关坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置的旋转偏移 `[0, 0, 0]` （默认） | 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。Roll、Pitch 和 Yaw 分别是绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。

你可以通过将 **Parent name** 设置为该车辆的名称，将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。你还可以通过将 **Parent name** 设置为 `Scene Origin`，将传感器安装到场景原点。

有关坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1` （默认） | 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块将从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 传感器参数

#### 固有参数

### **Relative mounting locations** — 超声波阵列中各个传感器的相对安装位置 `[[0, -0.67, 0]; [0, -0.22, 0]; [0, 0.22, 0]; [0, 0.67, 0]]` （默认） | 实值 *N*×`3` 数组

超声波阵列中各个传感器的相对安装位置，指定为实值 *N*×`3` 数组。*N* 是超声波阵列中的传感器数量，这些位置相对于 `Mounting Location` 参数指定的传感器安装位置。数组的每一行都必须是形式为 [*X*, *Y*, *Z*] 的 1×3 向量。单位为米。

### **Relative mounting rotations** — 超声波阵列中各个传感器的相对安装旋转 `zeros(4,3)` （默认） | 实值 *N*×`3` 数组

超声波阵列中各个传感器的相对安装旋转，指定为实值 *N*×`3` 数组。*N* 是超声波阵列中的传感器数量，这些旋转相对于 `Mounting Location` 参数指定的传感器安装方向。数组的每一行都必须是形式为 [*roll*, *pitch*, *yaw*] 的 1×3 向量。

### **Horizontal Field of view (deg)** — 超声波阵列的水平视场 `70` （默认） | 正实标量

超声波阵列的水平视场，指定为正实标量。此视场定义了超声波阵列所有传感器在水平方向上相对于其方向所跨越的总角度范围。必须指定水平视场 `horizontalFOV` 在 (0, 360] 范围内。单位为度。

### **Vertical field of view (deg)** — 超声波阵列的垂直视场 `35` （默认） | 正实标量

超声波阵列的垂直视场，指定为正实标量。此视场定义了超声波阵列所有传感器在垂直方向上相对于其方向所跨越的总角度范围。必须指定垂直视场在 (0, 180] 范围内。单位为度。

### **Detection ranges (m)** — 超声波阵列的检测范围向量 (m) `[0.03 0.15 5.5]` （默认） | 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量

超声波阵列的检测范围向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为米。这些值确定超声波阵列返回的检测结果和距离值。

- 当检测到的对象距离在 `minDistRange` 和 `maxDistRange` 之间时，传感器返回正距离值。
- 当检测到的对象距离在 `minDetOnlyRange` 和 `minDistRange` 之间时，传感器检测到该对象，但无法确定距离，并返回值 `0`。
- 当对象距离低于 `minDetOnlyRange` 或高于 `maxDistRange` 时，传感器返回空元胞数组。

#### 信号参数

### **Acoustic frequency (kHz)** — 超声波阵列中所有传感器发射器使用的声波频率 `50` （默认） | 正实标量

超声波阵列中所有传感器发射器使用的声波频率，指定为正实标量。单位为 kHz。

### **Sampling frequency (kHz)** — 超声波阵列中所有传感器接收器的采样频率 `500` （默认） | 正实标量

超声波阵列中所有传感器接收器的采样频率，指定为正实标量。要对给定频率的信号进行采样，接收器的采样频率必须至少为该频率的两倍。单位为 kHz。

### **Pulse width (s)** — 超声波阵列中所有传感器使用的超声波脉冲宽度 `1e-6` （默认） | 正实标量

超声波阵列中所有传感器使用的超声波脉冲宽度，指定为正实标量。

### **Gain** — 超声波阵列中传感器用于声音信号的向量增益 `[1, 0]` （默认） | 实值标量 | 实值 `1`×`2` 向量

超声波阵列中传感器用于声音信号的向量增益，指定为实值标量或形式为 `[a, b]` 的 `1`×`2` 向量。该模块将标量增益作为常数相乘，并将向量增益作为形式为 `a + b*t` 的时间信号与超声波信号相乘。

### **Sound speed (m/s)** — 环境中的声速 `330` （默认） | 正实标量

环境中的声速，指定为正实标量。单位为 m/s。

### 真值

### **Output location and orientation** — 传感器的输出位置和方向 `off` （默认） | `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：设置 **Coordinate system** 参数

在 Simulation 3D Ultrasonic Array 模块中设置 **Coordinate system** 参数，以表示 3D 环境中 actor 变换的坐标系。

## 描述

3D 仿真环境中具有可调声学参数的超声波传感器模型

Simulation 3D Ultrasonic Array 模块根据安装在 3D 仿真环境中自车上的、具有可调声学参数的超声波传感器阵列所进行的距离测量来生成检测结果。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块基于传感器与检测对象上最近点之间的距离来计算距离测量值。该模块还提供参数，用于控制传感器用于计算距离测量值的超声波信号的波形。

如果将 **Sample time** 设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，模型中必须包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Ultrasonic Array 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Ultrasonic Array 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Array — `1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order (Simulink)。

该模块的 **Coordinate system** 参数指定 actor 变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。
