---
type: simulink-block
title: 'Simulation 3D UAV Vehicle'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3duavvehicle'
documentation_source_path: 'ref/simulation3duavvehicle.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D UAV Vehicle

## 端口

### 输入

### **Translation** — UAV 的平移位置向量

UAV 的平移位置，指定为 1×3 向量

如果 **Use geospatial coordinates for inputs and initial values** 参数被禁用，则将输入指定为 UAV 在 Unreal Engine 世界坐标系中的 *X*、*Y* 和 *Z* 位置。单位为米。

如果 **Use geospatial coordinates for inputs and initial values** 被启用，则将输入指定为 UAV 的纬度、经度和海拔高度，单位为米。该模块通过计算相对于您指定的 `GeoOrigin` 的平移量，将 UAV 放置在 Unreal Engine 中。

有关坐标系的更多信息，请参阅 UAV Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**数据类型：** `double`

### **Rotation** — UAV 的旋转向量 | 矩阵

UAV 的旋转，指定为 1×3 向量或 17×3 矩阵。对于 **Type** 参数的任意值，您都可以将此输入指定为 1×3 向量，但如果 Type 为 `Custom`，您也可以将 Rotation 指定为 17×3 矩阵。

- 1×3 向量

  包含 UAV 机体的偏航角、俯仰角和横滚角，单位为弧度。UAV 旋翼以 250 RPM（1500 deg/sec）的固定角速度旋转。
- 17×3 矩阵

  下表总结了旋转矩阵的各行。

  - 每个角速度行包含围绕对应 `UAV_RotorN` 网格的 X、Y 和 Z 轴的角速度，该网格是您在将网格导出到 Unreal Engine 时设置的。单位为每分钟转数（RPM）。
  - 每个旋转角行包含对应 UAV 网格部件的偏航角、俯仰角和横滚角，单位为弧度。

  | 矩阵行 | UAV 网格部件 |
  | --- | --- |
  | 1 | `UAV_Body` 旋转角 |
  | 2 | `UAV_Motor1` 旋转角 |
  | 3 | `UAV_Rotor1` 角速度 |
  | 4 | `UAV_Motor2` 旋转角 |
  | 5 | `UAV_Rotor2` 角速度 |
  | 6 | `UAV_Motor3` 旋转角 |
  | 7 | `UAV_Rotor3` 角速度 |
  | 8 | `UAV_Motor4` 旋转角 |
  | 9 | `UAV_Rotor4` 角速度 |
  | 10 | `UAV_Motor5` 旋转角 |
  | 11 | `UAV_Rotor5` 角速度 |
  | 12 | `UAV_Motor6` 旋转角 |
  | 13 | `UAV_Rotor6` 角速度 |
  | 14 | `UAV_Motor7` 旋转角 |
  | 15 | `UAV_Rotor7` 角速度 |
  | 16 | `UAV_Motor8` 旋转角 |
  | 17 | `UAV_Rotor8` 角速度 |

如果您清除 **Use geospatial coordinates for inputs and initial values** 参数，则 UAV 机体旋转角相对于 Unreal Engine 世界坐标系。

如果您选中 **Use geospatial coordinates for inputs and initial values** 参数，则 UAV 机体旋转角相对于 UAV 当前位置的局部 ENU 坐标系。

有关坐标系的更多信息，请参阅 UAV Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**数据类型：** `double`

### **GeoOrigin** — Unreal Engine 世界原点的地理空间坐标向量

Unreal Engine 世界原点的地理空间坐标，以 [*latitude* *longitude* *altitude*] 形式指定。*latitude* 和 *longitude* 的单位为度，*altitude* 的单位为米。

#### 依赖关系

要启用此端口，请选中 **Use geospatial coordinates for inputs and initial values** 参数。

**数据类型：** `double`

## 参数

### 车辆参数

### **Type** — 车辆类型 `Quadcopter`（默认）| `Fixed wing` | `Custom`

选择车辆类型。要获取每种车辆类型的尺寸，请参阅以下参考页面：

- `Quadcopter` — Quadrotor
- `Fixed wing` — Fixed Wing Aircraft
- `Custom` — 自定义 UAV。有关自定义 UAV 网格的更多详细信息，请访问 Prepare Custom UAV Vehicle Mesh for the Unreal Editor

### **Path to custom mesh** — 自定义 UAV 网格资产的参考路径 `/MathWorksUAVContent/UAVs/HexaRotorUAV/HexaRotor.HexaRotor`（默认）| 有效的资产参考路径

自定义 UAV 网格资产的参考路径。

有关如何从 Unreal® 编辑器中获取此路径的示例，请访问 Visualize VTOL UAV Mission Over Urban Environment。

#### 依赖关系

要启用此参数，请将 **Type** 参数设置为
`Custom`。

### **Color** — 载具颜色 `Black`（默认）| `Orange` | `Yellow` | `Green` | `Blue` | `Red` | `White` | `Silver`

选择载具的颜色。

#### 依赖关系

要启用此参数，请将 **Type** 参数设置为
`Quadcopter` 或 `Fixed
wing`。

### **Name** — 载具名称 `SimulinkVehicle1`（默认）| 载具名称

载具名称。默认情况下，当您在模型中使用该模块时，模块会将
**Name** 参数设置为
`SimulinkVehicleX`。`X`
的值取决于模型中 Simulation 3D UAV Vehicle 模块的数量。

载具名称会作为选项出现在与载具同一模型中任何 UAV Toolbox Simulation 3D 传感器模块的 **Parent name**
参数中。通过
**Parent name** 参数，您可以选择要安装传感器的载具。

### **Use geospatial coordinates for inputs and initial values** — 对端口输入和初始值使用地理空间坐标 `off`（默认）| `on`

选择此参数以在表单中对端口输入和初始值使用地理空间坐标。

### Initial Values

### **Initial Translation (m)** — 载具初始位置 `[0 0 0]`（默认）| 向量

以以下形式之一指定载具的初始位置：

- 当您清除 **Use geospatial coordinates
  for inputs and initial values** 参数时，为 [*X*
  *Y*
  *Z*]。*X*、
  *Y* 和 *Z* 分别是在惯性
  *Z*-down 坐标系中沿
  *X* 轴、*Y* 轴和
  *Z* 轴的平移量，单位为米。
- 当您启用 **Use geospatial
  coordinates for inputs and initial values** 参数时，为 [*latitude*
  *longitude*
  *altitude*]。您必须以度为单位指定 *latitude* 和 *longitude*，
  并以米为单位指定 *altitude*。

### **Initial Georeference Origin (LLA)** — 初始地理参考原点 `[0 0 0]`（默认）| 向量

以 [*latitude*
*longitude*
*altitude*] 的形式指定初始地理参考原点。您必须以度为单位指定 *latitude* 和
*longitude*，并以米为单位指定 *altitude*。

#### 依赖关系

要启用此参数，请选择 **Use geospatial coordinates for
inputs and initial values** 参数。

### **Initial Rotation (rad)** — 载具初始旋转角度 `[0 0 0]`（默认）| 向量 | 矩阵

UAV 的初始旋转。此参数的维度取决于
**Type** 参数的值。对于 **Type** 参数的任意值，您都可以将此参数指定为 1×3
向量，但如果 Type 为
`Custom`，您也可以将此参数指定为 17×3
矩阵。

有关如何指定此值的更多详细信息，请参阅 **Rotation** 输入。

### Sample Time

### **Sample time** — 采样时间 `-1`（默认）| 标量

采样时间 *Ts*，指定为正
标量，单位为秒。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样
时间。

## 所属库

UAV Toolbox / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a：自定义 UAV Type 的旋转输入

当您将
**Type** 参数设置为 `Custom` 时，Simulation 3D UAV Vehicle 模块现在接受 17×3 矩阵作为旋转输入。

第一行指定 UAV 机体的旋转角度。之后，每个偶数行
分别指定 UAV 电机 1 到 8 的旋转角度，而每个奇数行指定
对应转子的角速度。

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D UAV Vehicle 模块仿真模型需要
Simulink
3D Animation。

### R2023a: 支持指定地理空间坐标

您可以选择 **Use geospatial coordinates for inputs and initial
values** 参数，以使用地理空间坐标指定输入和初始值。

## 描述

在 3D 可视化中放置 UAV 载具

**注意**

使用 Simulation 3D UAV Vehicle 模块仿真模型需要
Simulink®
3D Animation™。

Simulation 3D UAV Vehicle 模块在 3D 仿真环境中实现无人驾驶航空器
(UAV)。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块使用 UAV 在仿真中的输入 (*X*、*Y*、
*Z*) 位置和输入 (*roll*、
*pitch*、*yaw*) 姿态。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。
如果将 Simulation 3D UAV Vehicle 模块的 **Sample time** 参数设置为 `-1`，则该模块继承
Simulation 3D Scene Configuration 模块中指定的采样时间。

**提示**

Simulation 3D UAV Vehicle 模块必须在
Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D UAV Vehicle 模块会在
Unreal Engine 3D 可视化环境接收信号数据之前准备好该信号数据。要检查模块执行顺序，
请右键点击这些模块并选择 **Properties**。在
**General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle — `-1`

有关执行顺序的详细信息，请参阅 Block Execution Order。
