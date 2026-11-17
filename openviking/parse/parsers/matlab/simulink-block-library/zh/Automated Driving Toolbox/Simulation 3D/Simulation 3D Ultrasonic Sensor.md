---
type: simulink-block
title: 'Simulation 3D Ultrasonic Sensor'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dultrasonicsensor'
documentation_source_path: 'ref/simulation3dultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ultrasonic Sensor

## 端口
```yaml
ports:
- name: Detections
  summary: 目标检测 标量
  direction: output
- name: Has object
  summary: 传感器视场内存在可检测目标 标量
  direction: output
- name: Has range
  summary: 传感器视场内存在的目标可进行距离测量 标量
  direction: output
- name: Range
  summary: 到最近目标的距离测量值 标量
  direction: output
- name: Translation
  summary: 传感器位置 实值 1×3 向量
  direction: output
  data_types: double
- name: Rotation
  summary: 传感器方向 实值 1×3 向量
  direction: output
  data_types: double
```

### 输出

### **Detections** — 目标检测 标量

目标检测，返回为包含 MATLAB® 结构体的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器，例如 Multi-Object Tracker 模块，并生成航迹。

该结构体包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 到最近目标的距离测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数使用的参数 |

下表描述了 `ObjectAttributes` 字段中的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的 actor 的标识符，返回为该 actor 的 `ActorID` 属性值。对于虚警，该值为负数。 |
| `PointOnTarget` | 传感器用于计算距离测量的被检测目标上的点的坐标，位于车辆坐标系中。用于在 Bird's-Eye Scope 应用中可视化检测。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。父坐标系为自车车身。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 指示用于报告测量值的坐标系的枚举类型。如果检测来自 Ultrasonic Detection Generator 模块，Simulation 3D Ultrasonic Sensor 以球坐标报告它们，且 `Frame` 的值为 `'spherical'`。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的三维向量偏移。 |
| `OriginVelocity` | 传感器坐标系相对于父坐标系的速度。 |
| `IsParentToChild` | 逻辑标量，指示 `Orientation` 是否执行从父坐标系到子坐标系的坐标系旋转。当 `IsParentToChild` 为 `false` 时，`Orientation` 执行从子坐标系到父坐标系的坐标系旋转。 |
| `HasAzimuth` | 指示测量值是否包含方位角分量。 |
| `HasRange` | 指示测量值是否包含距离分量。对于 Ultrasonic Detection Generator 始终为 `true`。 |
| `HasElevation` | 指示测量值是否包含仰角分量。对于 Ultrasonic Detection Generator 始终为 `false`。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。对于 Ultrasonic Detection Generator 始终为 `false`。 |
| `FieldOfView` | 包含传感器方位角和仰角视场值的二维向量。 |

#### 依赖关系

要启用此端口，请选中 **Use bus output** 参数。

### **Has object** — 传感器视场内存在可检测目标 标量

传感器视场内存在可检测目标，返回为布尔标量。如果目标到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小仅检测距离，则该目标被视为可检测。

#### 依赖关系

要启用此端口，请清除 **Use bus output** 参数。

### **Has range** — 传感器视场内存在的目标可进行距离测量 标量

传感器视场内存在的目标可进行距离测量，返回为布尔标量。对于视场内的任何目标，如果其到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小距离范围，则可以进行距离测量。

#### 依赖关系

要启用此输出端口，请清除 **Use bus output** 参数。

### **Range** — 到最近目标的距离测量值 标量

到最近目标的距离测量值，返回为非负标量，单位为米。

#### 依赖关系

要启用此端口，请清除 **Use bus output** 参数。

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标系中。在此坐标系中，*Z* 轴从地面向上指向。单位为米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选中 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。**Rotation** 值位于场景的世界坐标系中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位为弧度。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选中 **Output location (m) and orientation (rad)**。

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
- name: Detection ranges (m)
  summary: 超声波传感器的检测范围向量 (m) [0.03 0.15 5.5]（默认）| 形式为 [minDetOnlyRange minDistRange maxDistRange] 的 1×3 非负实值向量
  group: 传感器参数
- name: Horizontal field of view (deg)
  summary: 超声波传感器的水平视场 70（默认）| 正实标量
  group: 传感器参数
- name: Vertical field of view (deg)
  summary: 超声波传感器的垂直视场 35（默认）| 正实标量
  group: 传感器参数
- name: Use bus output
  summary: 将输出信号作为总线一起输出 on（默认）| off
  group: 传感器参数
- name: Output location (m) and orientation (rad)
  summary: 输出传感器的位置和方向 off（默认）| on
  group: Ground Truth
```

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父车辆名称 `Scene Origin`（默认）| 车辆名称

传感器安装到的父对象名称，指定为 `Scene Origin` 或模型中车辆的名称。您可以选择的车俩名称对应于模型中仿真 3D 车辆模块的 **Name** 参数。如果选择 `Scene Origin`，该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器相对于场景或车辆原点放置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点。您只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的预定义安装位置之一。在仿真期间，传感器随车辆移动。

| 安装位置 | 描述 | 相对于车辆原点的方向 [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且位于车辆的几何中心（请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox） 传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器，安装到前保险杠 传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠 传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器，安装到右侧后视镜 传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器，安装到左侧后视镜 传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器，安装到车内后视镜 传感器安装在后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器，安装到引擎盖中心 传感器安装在引擎盖中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器，安装到车顶中心 传感器安装在车顶中心的车辆 | [0, 0, 0] |

当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针方向为正。当从上方观察车辆时，偏航角（方向角）为逆时针方向为正，因为您是沿该轴的负方向观察的。

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您安装传感器的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器在世界坐标系中的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选中 **Output location (m) and orientation (rad)** 参数，并检查来自 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认）| `on`

选中此参数以使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。单位为米。

如果您通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，如沿车辆前方观察时所见。
- *Z* 轴向上指向。

原点为 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选中 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。横滚、俯仰和偏航分别是绕 *X* 轴、*Y* 轴和 *Z* 轴的旋转角。单位为度。

如果您通过将 **Parent name** 设置为该车辆的名称来将传感器安装到车辆，则 *X*、*Y* 和 *Z* 位于车辆坐标系中，其中：

- *X* 轴从车辆向前指向。
- *Y* 轴指向车辆左侧，如沿车辆前方观察时所见。
- *Z* 轴向上指向。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，横滚、俯仰和偏航为顺时针方向为正。如果您从二维俯视角度观察场景，则偏航角（也称为方向角）为逆时针方向为正，因为您是沿 *Z* 轴的负方向观察场景的。

原点为 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。

如果您通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标系中。

有关车辆和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选中 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境帧率为采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 传感器参数

### **Detection ranges (m)** — 超声波传感器的检测范围向量 (m) `[0.03 0.15 5.5]`（默认）| 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量

超声波传感器的检测范围向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为米。这些值决定超声波传感器返回的检测和目标距离值。

- 当被检测目标位于 `minDistRange` 和 `maxDistRange` 之间的距离时，传感器返回正距离值。
- 当被检测目标位于 `minDetOnlyRange` 和 `minDistRange` 之间的距离时，传感器检测到目标，但无法确定距离并返回值 `0`。
- 当目标位于 `minDetOnlyRange` 以下或 `maxDistRange` 以上的距离时，传感器返回空元胞数组。

### **Horizontal field of view (deg)** — 超声波传感器的水平视场 `70`（默认）| 正实标量

超声波传感器的水平视场，指定为正实标量。该视场定义传感器在水平方向上跨越的总角度范围。您必须在 (0, 180) 范围内指定水平视场 `horizontalFOV`。单位为度。

### **Vertical field of view (deg)** — 超声波传感器的垂直视场 `35`（默认）| 正实标量

超声波传感器的垂直视场，指定为正实标量。该视场定义传感器在垂直方向上跨越的总角度范围。您必须在 (0, 180) 范围内指定垂直视场。单位为度。

### **Use bus output** — 将输出信号作为总线一起输出 `on`（默认）| `off`

选中以使用 **Detections** 端口将检测输出为总线信号。清除 **Use bus output** 以改为启用 **Has object**、**Has range** 和 **Range** 输出端口。

### Ground Truth

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选中此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。
## 所属库

Automated Driving Toolbox / Simulation 3D Aerospace Blockset / Animation / Simulation 3D UAV Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Ultrasonic Sensor 模块仿真模型需要 Simulink 3D Animation。

### R2023b：添加了 ground truth 参数

Simulation 3D Ultrasonic Sensor 模块现在具有 ground truth 参数，您可以启用该参数以输出传感器的位置和方向

## 描述

3D 仿真环境中的超声波传感器模型

**注意**

使用 Simulation 3D Ultrasonic Sensor 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Ultrasonic Sensor 模块根据安装在自车上的超声波传感器在由 Epic Games® 的 Unreal Engine® 渲染的 3D 仿真环境中进行的距离测量来生成检测结果。该模块根据传感器与检测到的物体上最近点之间的距离来计算距离测量值。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含一个 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Ultrasonic Sensor 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Ultrasonic Sensor 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Sensor — `1`

有关执行顺序的详细信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
