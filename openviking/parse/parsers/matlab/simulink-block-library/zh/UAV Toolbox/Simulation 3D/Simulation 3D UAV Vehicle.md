---
type: simulink-block
title: 'Simulation 3D UAV Vehicle'
family: 'simulation-3d'
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

### **Translation** — UAV 向量的平移位置

UAV 的平移位置，指定为 1-by-3 向量

如果禁用了 **Use geospatial coordinates for inputs and initial values** 参数，请将输入指定为 UAV 在 Unreal Engine 世界坐标系中的 *X*、*Y* 和 *Z* 位置。单位为 meter。

如果启用了 **Use geospatial coordinates for inputs and initial values**，请将输入指定为 UAV 的 latitude、longitude 和 altitude，单位为 meter。该模块通过计算相对于您指定的 `GeoOrigin` 的平移，将 UAV 放置在 Unreal Engine 中。

有关坐标系的更多信息，请参阅 UAV Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**数据类型：** `double`

### **Rotation** — UAV 的旋转，向量 | 矩阵

UAV 的旋转，指定为 1-by-3 向量或 17-by-3 矩阵。对于 **Type** 参数的任何值，您都可以将此输入指定为 1-by-3 向量，但如果 Type 为 `Custom`，您也可以将 Rotation 指定为 17-by-3 矩阵。

- 1-by-3 向量

  包含 UAV 机体的 yaw、pitch 和 roll 角，单位为 radians。UAV 旋翼以 250 RPM（1500 deg/sec）的固定角速度旋转。
- 17-by-3 矩阵

  下表总结了旋转矩阵的各行。

  - 每个角速度行包含对应 `UAV_RotorN` 网格绕 X、Y 和 Z 轴的角速度，该网格是您在将网格导出到 Unreal Engine 时设置的。单位为 revolutions per minute (RPM)。
  - 每个旋转角行包含对应 UAV 网格部件的 yaw、pitch 和 roll 角，单位为 radians。

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

如果清除 **Use geospatial coordinates for inputs and initial values** 参数，则 UAV 机体旋转角相对于 Unreal Engine 世界坐标系。

如果选中 **Use geospatial coordinates for inputs and initial values** 参数，则 UAV 机体旋转角相对于 UAV 当前位置处的局部 ENU 坐标系。

有关坐标系的更多信息，请参阅 UAV Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**数据类型：** `double`

### **GeoOrigin** — Unreal Engine 世界原点的地理空间坐标向量

Unreal Engine 世界原点的地理空间坐标，以 [*latitude* *longitude* *altitude*] 形式指定。*latitude* 和 *longitude* 的单位为 degrees，*altitude* 的单位为 meters。

#### 依赖关系

要启用此端口，请选中 **Use geospatial coordinates for inputs and initial values** 参数。

**数据类型：** `double`

## 参数

### 车辆参数

### **Type** — 车辆类型 `Quadcopter`（默认） | `Fixed wing` | `Custom`

选择车辆类型。要获取每种车辆类型的尺寸，请参阅以下参考页：

- `Quadcopter` — Quadrotor
- `Fixed wing` — Fixed Wing Aircraft
- `Custom` — Custom UAV。有关自定义 UAV 网格的更多详细信息，请访问 Prepare Custom UAV Vehicle Mesh for the Unreal Editor

### **Path to custom mesh** — 自定义 UAV 网格资产的引用路径 `/MathWorksUAVContent/UAVs/HexaRotorUAV/HexaRotor.HexaRotor`（默认） | 有效的资产引用路径

自定义 UAV 网格资产的引用路径。

有关如何从 Unreal® editor 获取此路径的示例，请访问 Visualize VTOL UAV Mission Over Urban Environment。

#### 依赖关系

要启用此参数，请将 **Type** 参数设置为 `Custom`。

### **Color** — 车辆颜色 `Black`（默认） | `Orange` | `Yellow` | `Green` | `Blue` | `Red` | `White` | `Silver`

选择车辆的颜色。

#### 依赖关系

要启用此参数，请将 **Type** 参数设置为 `Quadcopter` 或 `Fixed wing`。

### **Name** — 车辆名称 `SimulinkVehicle1`（默认） | 车辆名称

车辆名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D UAV Vehicle 模块的数量。

车辆名称会作为同一模型中任何 UAV Toolbox Simulation 3D 传感器模块的 **Parent name** 参数中的一个选项出现。使用 **Parent name** 参数，您可以选择要在其上安装传感器的车辆。

### **Use geospatial coordinates for inputs and initial values** — 为端口输入和初始值使用地理空间坐标 `off`（默认） | `on`

选中此参数，以便对端口输入和初始值使用地理空间坐标形式。

### 初始值

### **Initial Translation (m)** — 初始车辆位置 `[0 0 0]`（默认） | 向量

使用以下形式之一指定车辆的初始位置：

- 当清除 **Use geospatial coordinates for inputs and initial values** 参数时，为 [*X* *Y* *Z*]。*X*、*Y* 和 *Z* 分别是在惯性 *Z*-down 坐标系中沿 *X* 轴、*Y* 轴和 *Z* 轴的平移，单位为 meters。
- 当启用 **Use geospatial coordinates for inputs and initial values** 参数时，为 [*latitude* *longitude* *altitude*]。必须指定 *latitude* 和 *longitude*，单位为 degrees，*altitude* 单位为 meters。

### **Initial Georeference Origin (LLA)** — 初始地理参考原点 `[0 0 0]`（默认） | 向量

以 [*latitude* *longitude* *altitude*] 形式指定初始地理参考原点。必须指定 *latitude* 和 *longitude*，单位为 degrees，*altitude* 单位为 meters。

#### 依赖关系

要启用此参数，请选中 **Use geospatial coordinates for inputs and initial values** 参数。

### **Initial Rotation (rad)** — 车辆旋转的初始角度 `[0 0 0]`（默认） | 向量 | 矩阵

UAV 的初始旋转。此参数的维度取决于 **Type** 参数的值。对于 **Type** 参数的任何值，您都可以将此参数指定为 1-by-3 向量，但如果 Type 为 `Custom`，您也可以将此参数指定为 17-by-3 矩阵。

有关如何指定此值的更多详细信息，请参阅 **Rotation** 输入。

### 采样时间

### **Sample time** — 采样时间 `-1`（默认） | 标量

采样时间 *Ts*，指定为以 seconds 为单位的正标量。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

## 所属库

UAV Toolbox / Simulation 3D

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a: 自定义 UAV Type 的 Rotation 输入

当您将 **Type** 参数设置为 `Custom` 时，Simulation 3D UAV Vehicle 模块现在接受 17-by-3 矩阵作为 rotation 输入。

第一行指定 UAV 机体的旋转角。之后，每个偶数行指定 UAV 电机 1 到 8 的旋转角，而每个奇数行指定对应旋翼的角速度。

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D UAV Vehicle 模块仿真模型需要 Simulink 3D Animation。

### R2023a: 支持指定地理空间坐标

您可以选择 **Use geospatial coordinates for inputs and initial values** 参数，以使用地理空间坐标指定输入和初始值。

## 描述

在 3D 可视化中放置 UAV 车辆

**注意**

使用 Simulation 3D UAV Vehicle 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D UAV Vehicle 模块在 3D 仿真环境中实现无人驾驶航空器（UAV）。该环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块使用仿真中 UAV 的输入 (*X*, *Y*, *Z*) 位置和输入 (*roll*, *pitch*, *yaw*) 姿态。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D UAV Vehicle 模块的 **Sample time** 参数设置为 `-1`，该模块将继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

**提示**

Simulation 3D UAV Vehicle 模块必须在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D UAV Vehicle 模块会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好这些数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle — `-1`

有关执行顺序的更多信息，请参阅 Block Execution Order。
