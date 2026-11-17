---
type: simulink-block
title: 'Simulation 3D Ultrasonic Sensor'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3dultrasonicsensor'
documentation_source_path: 'simulation3dultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ultrasonic Sensor

## 端口

### 输出

### **Has object** — 传感器视场内存在可检测对象 标量

传感器视场内存在可检测对象，以布尔标量形式返回。如果对象到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小仅检测距离，则该对象被视为可检测。

### **Has range** — 传感器视场内存在的对象可进行距离测量 标量

传感器视场内存在的对象可进行距离测量，以布尔标量形式返回。对于视场内的任何对象，如果其到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小距离范围，则可以进行距离测量。

### **Range** — 到最近对象的距离测量值 标量

到最近对象的距离测量值，以非负标量形式返回，单位为米。

### **Translation** — 传感器位置 实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上，选择 **Output location and orientation**。

**数据类型：** `double`

### **Rotation** — 传感器方向 实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上，选择 **Output location and orientation**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当您向模型中添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中最高的 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级载具名称 `Scene Origin`（默认）| 载具名称

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中载具的名称。您可以选择载具名称对应于模型中仿真 3D 载具模块的 **Name** 参数。如果选择 `Scene Origin`，该模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Coordinate system** — 用于 actor 变换的坐标系 `Default`（默认）| `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

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

### **Mounting location** — 传感器安装位置 `Origin`（默认）| `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

传感器安装位置。默认情况下，该模块根据 **Parent name** 参数将传感器相对于场景或车辆原点放置。

- 当 **Parent name** 为 `Scene Origin` 时，该模块将传感器安装到场景原点。您只能将 **Mounting location** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **Parent name** 为车辆名称时，该模块将传感器安装到表中描述的某个预定义安装位置。在仿真期间，传感器随车辆移动。例如，该表提供了 ISO 8855 标准坐标系中的安装位置。

| Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | 前向传感器安装在车辆原点，该原点位于地面上且处于车辆的几何中心（参见 Simulink 3D Animation 中的 Coordinate Systems） 传感器安装在原点的车辆 | [0, 0, 0] |
| `Front bumper`  `Front center` | 前向传感器安装在前保险杠上 传感器安装在前保险杠的车辆 | [0, 0, 0] |
| `Rear bumper`  `Rear center` | 后向传感器安装在后保险杠上 传感器安装在后保险杠的车辆 | [0, 0, 180] |
| `Right mirror` | 向下传感器安装在右侧后视镜上 传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
| `Left mirror` | 向下传感器安装在左侧后视镜上 传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
| `Rearview mirror` | 前向传感器安装在车内后视镜上 传感器安装在车内后视镜的车辆 | [0, 0, 0] |
| `Hood center` | 前向传感器安装在引擎盖中心 传感器安装在引擎盖中心的车辆 | [0, 0, 0] |
| `Roof center` | 前向传感器安装在车顶中心 传感器安装在车顶中心的车辆 | [0, 0, 0] |

传感器相对于车辆的 *X*-*Y*-*Z* 安装位置取决于车辆类型。要指定车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with Ground Following 的 **Type** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

要确定传感器的位置，请打开传感器模块。然后，在 **Ground Truth** 选项卡上，选择 **Output location and orientation** 参数，并检查 **Translation** 输出端口的数据。

### **Specify offset** — 指定相对于安装位置的偏移

选择此参数可通过 **Relative translation [X, Y, Z]** 和 **Relative rotation [Roll, Pitch, Yaw]** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。

您可以通过将 **Parent name** 设置为某车辆的名称，将传感器安装到该车辆。原点是 **Mounting location** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。您还可以通过将 **Parent name** 设置为 `Scene Origin`，将传感器安装到场景原点。

有关坐标系的更多详细信息，请参见 Simulink 3D Animation 中的 Coordinate Systems。

**Example:** `[0,0,0.01]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置的旋转偏移，实数值 1×3 向量

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实数值 1×3 向量。Roll、pitch 和 yaw 分别是绕 *X*、*Y* 和 *Z* 轴的旋转角度。单位为度。

您可以通过将 **Parent name** 设置为该载具的名称来将传感器安装到载具上。原点是 **Mounting location** 参数中指定的安装位置。该原点不同于载具原点，载具原点是载具的几何中心。您也可以通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点。

有关坐标系的更多详细信息，请参阅 Simulink 3D Animation 中的坐标系。

**示例：** `[0,0,10]`

#### 依赖关系

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境的帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，模块将从 Simulation 3D Scene Configuration 模块继承采样时间。

### 传感器参数

### **Detection ranges (m)** — 超声波传感器的检测范围向量（m） `[0.03 0.15 5.5]`（默认）| 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实数值向量

超声波传感器的检测范围向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实数值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为米。这些值决定超声波传感器返回的检测结果和距离值。

- 当被检测物体处于 `minDistRange` 和 `maxDistRange` 之间的距离时，传感器返回正的距离值。
- 当被检测物体处于 `minDetOnlyRange` 和 `minDistRange` 之间的距离时，传感器检测到物体，但无法确定距离并返回值 `0`。
- 当物体处于低于 `minDetOnlyRange` 或高于 `maxDistRange` 的距离时，传感器返回空元胞数组。

### **Horizontal field of view (deg)** — 超声波传感器的水平视场 `70`（默认）| 正实标量

超声波传感器的水平视场，指定为正实标量。该视场定义了传感器在水平方向上所跨越的总角度范围。您必须在 (0, 180) 范围内指定水平视场 `horizontalFOV`。单位为度。

### **Vertical field of view (deg)** — 超声波传感器的垂直视场 `35`（默认）| 正实标量

超声波传感器的垂直视场，指定为正实标量。该视场定义了传感器在垂直方向上所跨越的总角度范围。您必须在 (0, 180) 范围内指定垂直视场。单位为度。

### 真值

### **Output location and orientation** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Automated Driving Toolbox / Simulation 3D Aerospace Blockset / Animation / Simulation 3D UAV Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：设置坐标系参数

在 Simulation 3D Ultrasonic Sensor 模块中设置 **Coordinate system** 参数，以表示 3D 环境中执行者变换的坐标系。

## 描述

3D 仿真环境中的超声波传感器模型

Simulation 3D Ultrasonic Sensor 模块根据安装在自车上的超声波传感器在由 Epic Games® 的 Unreal Engine® 渲染的 3D 仿真环境中进行的距离测量生成检测结果。该模块基于传感器与检测到的物体上最近点之间的距离计算距离测量值。

如果将 **Sample time** 设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，您必须在模型中包含一个 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Ultrasonic Sensor 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Ultrasonic Sensor 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Sensor — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order (Simulink)。

该模块的 **Coordinate system** 参数指定了在 3D 环境中如何应用 actor 变换。该模块的输出也遵循指定的坐标系。
