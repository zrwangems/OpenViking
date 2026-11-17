---
type: simulink-block
title: 'Simulation 3D Ultrasonic Sensor'
family: 'simulation-3d'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dultrasonicsensor'
documentation_source_path: 'ref/simulation3dultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Ultrasonic Sensor

## 端口

### 输出

### **Has object** — 传感器视场内存在可检测对象，标量

传感器视场内存在可检测对象，以 Boolean 标量形式返回。如果对象到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的仅检测最小距离，则认为该对象可检测。

### **Has range** — 对于传感器视场内存在的对象可以进行距离测量，标量

对于传感器视场内存在的对象，可以进行距离测量，以 Boolean 标量形式返回。对于视场内的任何对象，如果其到传感器的最近距离大于 **Detection ranges (m)** 参数中指定的最小距离范围，则可以进行距离测量。

### **Range** — 到最近对象的距离测量值，标量

到最近对象的距离测量值，以非负标量形式返回，单位为 m。

### **Translation** — 传感器位置，实值 1×3 向量

传感器沿场景 *X* 轴、*Y* 轴和 *Z* 轴的位置。**Translation** 值位于场景的世界坐标中。在此坐标系中，*Z* 轴从地面向上指向。单位为 m。

#### 依赖

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Rotation** — 传感器方向，实值 1×3 向量

传感器绕场景 *X* 轴、*Y* 轴和 *Z* 轴的横滚、俯仰和偏航方向。**Rotation** 值位于场景的世界坐标中。当沿这些轴的正方向观察时，这些值在顺时针方向为正。单位为 rad。

#### 依赖

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 安装

### **Sensor identifier** — 唯一传感器标识符 `1`（默认）| 正整数

指定传感器的唯一标识符。在多传感器系统中，传感器标识符使您能够区分传感器。当向模型添加新的传感器模块时，该模块的 **Sensor identifier** 为 *N* + 1，其中 *N* 是模型中现有传感器模块中的最高 **Sensor identifier** 值。

**示例：** `2`

### **Parent name** — 父级载具名称 `Scene Origin`（默认）| 载具名称

传感器所安装到的父级名称，指定为 `Scene Origin` 或模型中载具的名称。可选择的载具名称对应于模型中 Simulation 3D Vehicle 模块的 **Name** 参数。如果选择 `Scene Origin`，模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **Mounting location** — 传感器安装位置 `Origin`（默认）| ...

传感器安装位置。默认情况下，模块根据 **Parent name** 参数将传感器相对于场景或载具原点放置。

- 当 **Parent name** 为 `Scene Origin` 时，模块将传感器相对于场景原点安装，并且在仿真期间，传感器保持静止。
- 当 **Parent name** 为载具名称时，模块将传感器相对于载具原点安装，并且在仿真期间，传感器随载具移动。

要指定传感器相对于场景或载具原点的相对位置和方向，请使用 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数。

载具原点的位置取决于载具类型。要选择载具类型，请指定您要将传感器安装到的 Simulation 3D UAV Vehicle 模块的 **Type** 参数。有关载具尺寸和载具原点位置的更多信息，请访问每种载具类型的参考页。

### **Specify offset** — 指定相对于安装位置的偏移 `on`（默认）| `off`

选择此参数以通过 **Relative translation [X, Y, Z] (m)** 和 **Relative rotation [Roll, Pitch, Yaw] (deg)** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z] (m)** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认）| 实值 1×3 向量

传感器相对于安装位置的平移偏移，指定为形式为 [*X*, *Y*, *Z*] 的实值 1×3 向量。单位为 m。

如果通过将 **Parent name** 设置为载具名称来将传感器安装到载具，则 *X*、*Y* 和 *Z* 位于载具坐标系中，其中：

- *X* 轴从载具指向前方。
- *Y* 轴指向载具左侧，即从载具前方观察时。
- *Z* 轴指向上方。

原点是在 **Mounting location** 参数中指定的安装位置。此原点与载具原点不同，载具原点是载具的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关载具和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in UAV Toolbox。

**示例：** `[0,0,0.01]`

#### 依赖

要启用此参数，请选择 **Specify offset**。

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于安装位置的旋转偏移 `[0, 90, 0]`（默认）| 实值 1×3 向量

传感器相对于安装位置的旋转偏移，指定为形式为 [*Roll*, *Pitch*, *Yaw*] 的实值 1×3 向量。Roll、Pitch 和 Yaw 分别是绕 *X*、*Y* 和 *Z* 轴的旋转角度。单位为 deg。

如果通过将 **Parent name** 设置为载具名称来将传感器安装到载具，则 *X*、*Y* 和 *Z* 位于载具坐标系中，其中：

- *X* 轴从载具指向前方。
- *Y* 轴指向载具左侧，即从载具前方观察时。
- *Z* 轴指向上方。
- 当分别沿 *X* 轴、*Y* 轴和 *Z* 轴的正方向观察时，Roll、Pitch 和 Yaw 在顺时针方向为正。如果从 2D 俯视视角查看场景，则 yaw 角（也称为方向角）在逆时针方向为正，因为您沿 *Z* 轴的负方向查看场景。

原点是在 **Mounting location** 参数中指定的安装位置。此原点与载具原点不同，载具原点是载具的几何中心。

如果通过将 **Parent name** 设置为 `Scene Origin` 来将传感器安装到场景原点，则 *X*、*Y* 和 *Z* 位于场景的世界坐标中。

有关载具和世界坐标系的更多详细信息，请参阅 Coordinate Systems for Unreal Engine Simulation in UAV Toolbox。

**示例：** `[0,0,10]`

#### 依赖

要启用此参数，请选择 **Specify offset**。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，模块将从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 传感器参数

### **Detection ranges (m)** — 超声传感器的检测范围向量 (m) `[0.03 0.15 5.5]`（默认）| 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量

超声传感器的检测范围向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为 m。这些值决定超声传感器返回的检测和距离值。

- 当检测到的对象距离在 `minDistRange` 和 `maxDistRange` 之间时，传感器返回正距离值。
- 当检测到的对象距离在 `minDetOnlyRange` 和 `minDistRange` 之间时，传感器检测到对象，但无法确定距离并返回值 `0`。
- 当对象距离低于 `minDetOnlyRange` 或高于 `maxDistRange` 时，传感器返回空元胞数组。

### **Horizontal field of view (deg)** — 超声传感器的水平视场 `70`（默认）| 正实标量

超声传感器的水平视场，指定为正实标量。此视场定义传感器在水平方向上跨越的总角度范围。必须将水平视场 `horizontalFOV` 指定在范围 (0, 180) 内。单位为 deg。

### **Vertical field of view (deg)** — 超声传感器的垂直视场 `35`（默认）| 正实标量

超声传感器的垂直视场，指定为正实标量。此视场定义传感器在垂直方向上跨越的总角度范围。必须将垂直视场指定在范围 (0, 180) 内。单位为 deg。

### 真值

### **Output location (m) and orientation (rad)** — 输出传感器的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Translation** 和 **Rotation** 端口输出传感器的平移和旋转。

## 所属库

Automated Driving Toolbox / Simulation 3D Aerospace Blockset / Animation / Simulation 3D UAV Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Ultrasonic Sensor 模块对模型进行仿真需要 Simulink 3D Animation。

### R2023b：添加真值参数

Simulation 3D Ultrasonic Sensor 模块现在具有真值参数，您可以启用该参数以输出传感器的位置和方向。

## 描述

3D 仿真环境中的超声传感器模型

**注意**

使用 Simulation 3D Ultrasonic Sensor 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Ultrasonic Sensor 模块从安装于自车上的超声传感器在由 Epic Games® 的 Unreal Engine® 渲染的 3D 仿真环境中进行的距离测量生成检测。该模块基于传感器与检测对象上最近点之间的距离计算距离测量值。

如果将 **Sample time** 设置为 `-1`，模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。要使用此传感器，模型中必须包含 Simulation 3D Scene Configuration 模块。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Ultrasonic Sensor 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Ultrasonic Sensor 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Sensor — `1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for UAVs Works。
