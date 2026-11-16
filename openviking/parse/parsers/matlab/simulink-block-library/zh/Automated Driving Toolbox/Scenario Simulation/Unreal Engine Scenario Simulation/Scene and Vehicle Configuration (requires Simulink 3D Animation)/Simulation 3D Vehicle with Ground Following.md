---
type: simulink-block
title: 'Simulation 3D Vehicle with Ground Following'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Scene and Vehicle Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dvehiclewithgroundfollowing'
documentation_source_path: 'ref/simulation3dvehiclewithgroundfollowing.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Vehicle with Ground Following

## 端口

### 输入

### **X** — 车辆纵向位置标量

车辆沿场景 *X* 轴的纵向位置。**X** 位于惯性 *Z*-up 坐标系中。单位是 meters。

**Initial position [X, Y, Z] (m)** 参数的 *X* 值必须与此端口在仿真开始时的值匹配。

若要沿整个车辆路径在端口 **X** 指定多个位置，请先在 MATLAB® 中定义 *X* waypoints 的时间序列。然后，使用 From Workspace (Simulink) 模块将这些 waypoints 提供给 **X**。要了解如何选择和指定 waypoints，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Y** — 车辆横向位置标量

车辆沿场景 *Y* 轴的横向位置。**Y** 位于惯性 *Z*-up 坐标系中。单位是 meters。

**Initial position [X, Y, Z] (m)** 参数的 *Y* 值必须与此端口在仿真开始时的值匹配。

若要沿整个车辆路径在端口 **Y** 指定多个位置，请先在 MATLAB 中定义 *Y* waypoints 的时间序列。然后，使用 From Workspace (Simulink) 模块将这些 waypoints 提供给 **Y**。要了解如何选择和指定 waypoints，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Yaw** — 车辆偏航姿态角标量

车辆沿场景 *Z* 轴的偏航姿态角。**Yaw** 位于惯性 *Z*-up 坐标系中。单位是 degrees。

**Initial rotation [Roll, Pitch, Yaw] (deg)** 参数的 yaw 值必须与此端口在仿真开始时的值匹配。

若要沿整个车辆路径在端口 **Yaw** 指定多个姿态角，请先在 MATLAB 中定义 yaw waypoints 的时间序列。然后，使用 From Workspace (Simulink) 模块将这些 waypoints 提供给 **Yaw**。要了解如何选择和指定 waypoints，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Light controls** — 车辆灯光控制 1-by-6 向量

Light controls 输入信号，指定为 1-by-6 Boolean 向量。向量的每个元素按照下表将特定车辆灯光设置为 on 或 off。值为 1 时将灯光置为 on；值为 0 时将灯光置为 off。

| 向量元素 | 车辆灯光 |
| --- | --- |
| (1,1) | 前照灯远光 |
| (1,2) | 前照灯近光 |
| (1,3) | 制动 |
| (1,4) | 倒车 |
| (1,5) | 左转向信号 |
| (1,6) | 右转向信号 |

#### 依赖关系

要创建此端口，请在 **Light Controls** 选项卡上选择 **Enable light controls**。

**Data Types:** `Boolean`

### 输出

### **Location** — 车辆位置实值 1-by-3 向量

场景中车辆的 (*X*, *Y*, *Z*) 位置，以实值 1-by-3 向量形式返回。此位置基于车辆原点，该原点位于地面上，在车辆的几何中心。**Location** 值位于惯性 *Z*-up 世界坐标系中。单位是 meters。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**Data Types:** `double`

### **Orientation** — 车辆姿态实值 1-by-3 向量

车辆围绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚姿态角，分别以实值 1-by-3 向量形式返回。此姿态基于车辆原点，该原点位于地面上，在车辆的几何中心。**Orientation** 值位于惯性 *Z*-up 坐标系中。单位是 radians。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**Data Types:** `double`

## 参数

### 车辆参数

### **Type** — 车辆类型 `Muscle car`（默认） | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Custom`

选择车辆类型。要获取每种车辆类型的尺寸，请参阅以下参考页：

- `Muscle car` — Muscle Car
- `Sedan` — Sedan
- `Sport utility vehicle` — Sport Utility Vehicle
- `Small pickup truck` — Small Pickup Truck
- `Hatchback` — Hatchback
- `Box truck` — Box Truck

#### 依赖关系

选择 `Custom` 会启用允许为车辆导入自定义网格的参数。

### **Path to custom mesh** — 自定义网格路径 `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar`（默认） | 有效路径

自定义网格的路径。

要创建自定义车辆网格，请参阅 Prepare Custom Vehicle Mesh for the Unreal Editor。

**示例：** `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_Sedan.SK_Sedan`

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Track width in custom mesh (m)** — 轮距 `1.9`（默认） | 标量

自定义网格中的轮距，单位为 m。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel base in custom mesh (m)** — 轴距 `3`（默认） | 标量

自定义网格中的轴距，单位为 m。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel radius in custom mesh (m)** — 车轮半径 `0.35`（默认） | 标量

自定义网格中的车轮半径，单位为 m。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Color** — 车辆颜色 `Red`（默认） | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver`

选择车辆的颜色。

### **Initial position [X, Y, Z] (m)** — 初始车辆位置 `[0, 0, 0]`（默认） | 实值 1-by-3 向量

车辆沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。此位置位于惯性 *Z*-up 坐标系中。单位是 meters。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时的 **X** 和 **Y** 输入端口值匹配。

### **Initial rotation [Roll, Pitch, Yaw] (deg)** — 车辆初始旋转角度 `[0, 0, 0]`（默认） | 实值 1-by-3 向量

车辆初始旋转角度。旋转角度由车辆的横滚、俯仰和偏航定义。单位是 degrees。

将此参数的 yaw 值设置为与仿真开始时的 **Yaw** 输入端口值匹配。

### **Name** — 车辆名称 `SimulinkVehicle1`（默认） | 车辆名称

车辆名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于您在模型中拥有的 Simulation 3D Vehicle with Ground Following 模块数量。

车辆名称会作为选择项出现在与该车辆同一模型中的任何 Automated Driving Toolbox™ Simulation 3D sensor 模块的 **Parent name** 参数中。使用 **Parent name** 参数，您可以选择要在其上安装传感器的车辆。

### **Sample time** — 采样时间 `-1`（默认） | 正标量

采样时间 *Ts*，单位为 seconds。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### 灯光控制

### **Enable light controls** — 控制车辆灯光 `off`（默认） | `on`

选择是否控制车辆前照灯。使用启用的参数设置灯光参数，包括前照灯强度。

#### 依赖关系

选择此参数：

- 创建输入端口 `Light controls`
- 启用以下灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **前照灯** | - **Headlight color** - **High beam intensity** - **Low beam intensity** - **High beam cone half angle** - **Low beam cone half angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **制动灯** | **Brake light intensity** |
  | **倒车灯** | **Reverse light intensity** |
  | **转向信号灯** | - **Turn signal light intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B]** — 前照灯颜色 `[1,1,1]`（默认） | RGB 三元组值的 1-by-3 数组

前照灯颜色，指定为归一化的 1-by-3 RGB 三元组值数组。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `int8` | `uint8`

### **High beam intensity (cd)** — 远光强度 `100000`（默认） | 正标量

远光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **Low beam intensity (cd)** — 近光强度 `60000`（默认） | 正标量

近光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **High beam cone half angle (deg)** — 远光锥半角 `70`（默认） | 小于或等于 90 的正标量

远光锥半角，单位为 deg。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **Low beam cone half angle (deg)** — 近光锥半角 `70`（默认） | 小于或等于 90 的正标量

近光锥半角，单位为 deg。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **Left headlight beam orientation [Pitch, Yaw] (deg)** — 左前照灯光束姿态 [Pitch, Yaw] (deg) `[0,0]`（默认） | 值介于 -180 和 180 之间的 1-by-2 数组

左前照灯光束在 *Z*-up 坐标系中的俯仰和偏航姿态，指定为 1-by-2 数组，单位为 deg。数组的第一个元素 `[1,1]` 是俯仰角。数组的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **Right headlight beam orientation [Pitch, Yaw] (deg)** — 右前照灯光束姿态 `[0,0]`（默认） | 值介于 -180 和 180 之间的 1-by-2 数组

右前照灯光束在 *Z*-up 坐标系中的俯仰和偏航姿态，指定为 1-by-2 数组，单位为 deg。数组的第一个元素 `[1,1]` 是俯仰角。数组的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

#### 制动灯

### **Brake light intensity (cd/m^2)** — 强度 `500`（默认） | 正标量

制动灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

#### 倒车灯

### **Reverse light intensity (cd/m^2)** — 强度 `500`（默认） | 正标量

倒车灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

#### 转向信号灯

### **Turn signal light intensity (cd/m^2)** — 强度 `500`（默认） | 正标量

转向信号灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **Period (s)** — 转向信号灯周期 `1`（默认） | 正标量

转向信号灯周期，单位为 s。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### **Pulse width (% of period)** — 脉冲宽度 `50`（默认） | 小于 100 的正标量

转向信号灯脉冲宽度，以周期的百分比表示。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**Data Types:** `double`

### 地面真值

### **Output location (m) and orientation (rad)** — 输出车辆位置和姿态 `off`（默认） | `on`

选择此参数以分别在 **Location** 和 **Orientation** 端口输出车辆的位置和姿态。

## 所属库

Automated Driving Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Vehicle with Ground Following 模块仿真模型需要 Simulink 3D Animation。

## 描述

实现在 3D 环境中跟随地面的车辆

**注意**

使用 Simulation 3D Vehicle with Ground Following 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Vehicle with Ground Following 模块在 3D 仿真环境中实现一辆四轮车辆。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块使用车辆的输入 (*X*, *Y*) 位置和偏航角来调整车辆的高程、横滚角和俯仰角，使其跟随地面地形。该模块确定车辆速度和航向，并调整每个车轮的转向角和旋转。请将此模块用于自动驾驶应用。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Vehicle with Ground Following 模块的 **Sample time** 参数设置为 `-1`，该模块将继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J670 [1] 和 ISO 8855 [2] 中定义的车辆 *Z*-up 右手 (RH) 笛卡尔坐标系。该坐标系是惯性的，并且初始与车辆几何中心对齐：

- *X* 轴沿车辆纵轴，并指向前方。
- *Y* 轴沿车辆横轴，并指向左侧。
- *Z* 轴指向上方。

当沿这些轴的正方向观察时，*Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚角分别在顺时针方向上为正。车辆放置在场景的世界坐标系中。有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**提示**

Simulation 3D Vehicle with Ground Following 模块必须在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Vehicle with Ground Following 模块会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle with Ground Following — `-1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。

您可以配置 Simulation 3D Vehicle with Ground Following 模块以导入自定义网格并控制车辆灯光。
