---
type: simulink-block
title: 'Simulation 3D Ultrasonic Array'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Sensors (requires Simulink 3D Animation)'
documentation_page: 'simulation3dultrasonicarray'
documentation_source_path: 'ref/simulation3dultrasonicarray.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ultrasonic Array

## 端口

### 输出

### **Detections** — 包含 MATLAB® 结构的对象检测 Simulink 总线

对象检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以将来自这些传感器和其他传感器的对象检测传递给跟踪器，例如 Multi-Object Tracker 模块，并生成航迹。

该结构必须包含以下字段。

| 属性 | 描述 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 到最近对象的距离测量 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 对象分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性 Kalman 跟踪滤波器的初始化函数所使用的参数 |

下表描述 `ObjectAttributes` 属性中的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的参与者 `ActorID` 的标识符。对于虚警，该值为负。 |
| `PointOnTarget` | 传感器用于计算距离测量的被检测对象上的点坐标。它位于车辆坐标系中。使用此值可在 Bird's-Eye Scope 应用中可视化检测。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。父坐标系是自车车身。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。对于 Ultrasonic Detection Generator，`Frame` 始终设置为 `'spherical'`，并且检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `OriginVelocity` | 传感器坐标系相对于父坐标系的速度。 |
| `IsParentToChild` | 逻辑标量，指示 `Orientation` 是否执行从父坐标系到子坐标系的坐标系旋转。当 `IsParentToChild` 为 false 时，`Orientation` 执行从子坐标系到父坐标系的坐标系旋转。 |
| `HasAzimuth` | 指示测量值是否包含方位角分量。 |
| `HasRange` | 指示测量值是否包含距离分量。对于 Ultrasonic Detection Generator，始终为 `true`。 |
| `HasElevation` | 指示测量值是否包含俯仰角分量。对于 Ultrasonic Detection Generator，始终为 `false`。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。对于 Ultrasonic Detection Generator，始终为 `false`。 |
| `FieldOfView` | 包含传感器方位角和俯仰角视场值的 2-D 向量。 |

#### 依赖关系

要启用此输出端口，请在 **参数** 选项卡上选中 **Use bus output** 参数。

### **Has object** — 指示传感器视场内是否存在任何可检测对象的标志 `true` | `false`

指示传感器视场内是否存在任何可检测对象的标志，返回为 logical scalar。如果对象到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小仅检测距离，则该对象被视为可检测。

#### 依赖关系

要启用此输出端口，请在 **参数** 选项卡上清除 **Use bus output** 参数。

### **Has range** — 指示对于传感器视场内存在的任何对象是否可以进行距离测量的标志 `true` | `false`

指示对于传感器视场内存在的任何对象是否可以进行距离测量的标志，返回为 logical scalar。对于视场内的任何对象，如果其到传感器的最近距离大于 `Detection Ranges (m)` 参数中指定的最小距离范围，则可以进行距离测量。

#### 依赖关系

要启用此输出端口，请在 **参数** 选项卡上清除 **Use bus output** 参数。

### **Range** — 到最近对象的距离测量 nonnegative scalar

到最近对象的距离测量，返回为 nonnegative scalar。

#### 依赖关系

要启用此输出端口，请在 **参数** 选项卡上清除 **Use bus output** 参数。

### **Translation** — 传感器位置 real-valued 1-by-3 vector

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标中。在此坐标系中，*Z* 轴从地面向上指向。单位是 meters。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器姿态 real-valued 1-by-3 vector

传感器围绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航姿态。**Rotation** 值位于场景的世界坐标中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位为 radians。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认） | positive integer

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父车辆名称 `Scene Origin`（默认） | 车辆名称

安装传感器的父对象名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择的车 辆名称对应于模型中 simulation 3D vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，该模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认） | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器放置在相对于场景或车辆原点的位置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点。只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的姿态 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 朝前传感器，安装到车辆原点；该原点位于地面上并处于车辆的几何中心（请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox） 车辆，其传感器安装在原点 | [0, 0, 0] |
| `Front bumper` `Front center` | 朝前传感器，安装到前保险杠 车辆，其传感器安装在前保险杠 | [0, 0, 0] |
| `Rear bumper` `Rear center` | 朝后传感器，安装到后保险杠 车辆，其传感器安装在后保险杠 | [0, 0, 180] |
| `Right mirror` | 朝下传感器，安装到右侧外后视镜 车辆，其传感器安装在右侧外后视镜 | [0, –90, 0] |
| `Left mirror` | 朝下传感器，安装到左侧外后视镜 车辆，其传感器安装在左侧外后视镜 | [0, –90, 0] |
| `Rearview mirror` | 朝前传感器，安装到车内后视镜 车辆，其传感器安装在车内后视镜 | [0, 0, 0] |
| `Hood center` | 朝前传感器，安装到发动机舱盖中心 车辆，其传感器安装在发动机舱盖中心 | [0, 0, 0] |
| `Roof center` | 朝前传感器，安装到车顶中心 车辆，其传感器安装在车顶中心 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针正。当从上方观察车辆时，偏航角（姿态角）为逆时针正，因为您是沿该轴的负方向观察。

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您安装传感器的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器在世界坐标中的位置，请打开传感器模块。然后，在 **真值** 选项卡上，选择 **Output location (m) and orientation (rad)** 参数，并检查来自 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认） | `on`

选择此参数以通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认） | real-valued 1-by-3 vector

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的 real-valued 1-by-3 vector。单位为 meters。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆前进方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认） | real-valued 1-by-3 vector

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的 real-valued 1-by-3 vector。横滚、俯仰和偏航分别是围绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角度。单位为 degrees。

如果通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- 当沿车辆前进方向观察时，*Y* 轴指向车辆左侧。
- *Z* 轴向上指向。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针正。如果从 2D 俯视视角观察场景，则偏航角（也称为姿态角）为逆时针正，因为您是沿 *Z* 轴的负方向观察场景。

原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关车辆坐标系和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认） | positive scalar

模块的采样时间，以秒为单位，指定为 positive scalar。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块将从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 传感器参数

#### 固有参数

### **Relative mounting locations (m)** — 超声波阵列中各个传感器的相对安装位置 `[[0, -0.67, 0]; [0, -0.22, 0]; [0, 0.22, 0]; [0, 0.67, 0]]`（默认） | real-valued *N*-by-`3` array

超声波阵列中各个传感器的相对安装位置，指定为 real-valued *N*-by-`3` array。*N* 是超声波阵列中的传感器数量，这些位置相对于 `Mounting Location` 参数指定的传感器安装位置。数组的每一行必须是形式为 [*X*, *Y*, *Z*] 的 1-by-3 vector。单位为 meters。

### **Relative mounting rotations (deg)** — 超声波阵列中各个传感器的相对安装旋转 `zeros(4,3)`（默认） | real-valued *N*-by-`3` array

超声波阵列中各个传感器的相对安装旋转，指定为 real-valued *N*-by-`3` array。*N* 是超声波阵列中的传感器数量，这些旋转相对于 `Mounting Location` 参数指定的传感器安装姿态。数组的每一行必须是形式为 [*roll*, *pitch*, *yaw*] 的 1-by-3 vector。单位为 degrees。

### **Horizontal Field of view (deg)** — 超声波阵列的水平视场 `70`（默认） | positive real scalar

超声波阵列的水平视场，指定为 positive real scalar。此视场定义超声波阵列所有传感器相对于其姿态在水平方向上跨越的总角度范围。您必须在 (0, 360] 范围内指定水平视场 `horizontalFOV`。单位为 degrees。

### **Vertical field of view (deg)** — 超声波阵列的垂直视场 `35`（默认） | positive real scalar

超声波阵列的垂直视场，指定为 positive real scalar。此视场定义超声波阵列所有传感器相对于其姿态在垂直方向上跨越的总角度范围。您必须在 (0, 180] 范围内指定垂直视场。单位为 degrees。

### **Detection ranges (m)** — 超声波阵列的检测距离向量 (m) `[0.03 0.15 5.5]`（默认） | 1-by-3 nonnegative real-valued vector of form `[minDetOnlyRange minDistRange maxDistRange]`

超声波阵列的检测距离向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1-by-3 nonnegative real-valued vector，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为 meters。这些值确定超声波阵列返回的检测和距离值。

- 当检测到的对象位于 `minDistRange` 与 `maxDistRange` 之间的距离时，传感器返回正的距离值。
- 当检测到的对象位于 `minDetOnlyRange` 与 `minDistRange` 之间的距离时，传感器检测到对象，但无法确定距离并返回 `0`。
- 当对象位于低于 `minDetOnlyRange` 或高于 `maxDistRange` 的距离时，传感器返回空元胞数组。

#### 信号参数

### **Acoustic frequency (kHz)** — 超声波阵列中所有传感器发射器使用的声波频率 `50`（默认） | positive real scalar

超声波阵列中所有传感器发射器使用的声波频率，指定为 positive real scalar。单位为 kHz。

### **Sampling frequency (kHz)** — 超声波阵列中所有传感器接收器的采样频率 `500`（默认） | positive real scalar

超声波阵列中所有传感器接收器的采样频率，指定为 positive real scalar。要对给定频率的信号进行采样，接收器的采样频率必须至少是该频率的两倍。单位为 kHz。

### **Pulse width (s)** — 超声波阵列中所有传感器使用的超声波脉冲宽度 `1e-6`（默认） | positive real scalar

超声波阵列中所有传感器使用的超声波脉冲宽度，指定为 positive real scalar。

### **Gain** — 超声波阵列中传感器使用的声音信号的向量增益 `[1, 0]`（默认） | real-valued scalar | real-valued `1`-by-`2` vector

超声波阵列中传感器使用的声音信号的向量增益，为 real-valued scalar 或形式为 `[a, b]` 的 `1`-by-`2` vector。该模块将标量增益作为常数与超声波信号相乘，并将向量增益作为形式为 `a + b*t` 的时间信号与超声波信号相乘。

### **Sound speed (m/s)** — 环境中的声速 `330`（默认） | positive real scalar

环境中的声速，指定为 positive real scalar。单位为 m/s。

### **Use bus output** — 选择以将信号一起输出为总线信号 `on`（默认） | `off`

选择此项以使用 **Detections** 端口将检测输出为总线信号。清除 **Use bus output** 以改为启用 **Has object**、**Has range** 和 **Range** 输出端口。

### 真值

### **Output location (m) and orientation (rad)** — 输出传感器的位置和姿态 `off`（默认） | `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Ultrasonic Array 模块仿真模型需要 Simulink 3D Animation。

### R2024a：真值参数

在 **真值** 选项卡上，选择 **Output location (m) and orientation (rad)** 以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 描述

3D 仿真环境中具有可调声学参数的超声波传感器模型

**注意**

使用 Simulation 3D Ultrasonic Array 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Ultrasonic Array 模块根据安装在 3D 仿真环境中自车上的、具有可调声学参数的超声波传感器阵列所进行的距离测量来生成检测。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块基于传感器与被检测对象上最近点之间的距离来计算距离测量。该模块还提供参数以控制传感器用于计算距离测量的超声波信号波形。

如果将 **Sample time** 设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Ultrasonic Array 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Ultrasonic Array 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Array — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
