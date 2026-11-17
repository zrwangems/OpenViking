---
type: simulink-block
title: 'Simulation 3D Vehicle with Ground Following'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dvehiclewithgroundfollowing'
documentation_source_path: 'ref/simulation3dvehiclewithgroundfollowing.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Vehicle with Ground Following

## 端口
```yaml
ports:
- name: X
  summary: 车辆的纵向位置 标量
  direction: input
- name: Y
  summary: 车辆的横向位置 标量
  direction: input
- name: Yaw
  summary: 车辆的偏航方向角 标量
  direction: input
- name: Light controls
  summary: 车辆灯光控制 1×6 向量
  direction: input
  data_types: Boolean
- name: Location
  summary: 车辆的位置 实数值 1×3 向量
  direction: output
  data_types: double
- name: Orientation
  summary: 车辆的方向 实数值 1×3 向量
  direction: output
  data_types: double
```

### 输入

### **X** — 车辆的纵向位置 标量

车辆沿场景 *X* 轴的纵向位置。**X** 位于惯性 *Z* 轴向上的坐标系中。单位为米。

**Initial position [X, Y, Z] (m)** 参数的 *X* 值必须与仿真开始时此端口的值匹配。

若要沿整个车辆路径在端口 **X** 处指定多个位置，请先在 MATLAB® 中定义 *X* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **X**。若要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Y** — 车辆的横向位置 标量

车辆沿场景 *Y* 轴的横向位置。**Y** 位于惯性 *Z* 轴向上的坐标系中。单位为米。

**Initial position [X, Y, Z] (m)** 参数的 *Y* 值必须与仿真开始时此端口的值匹配。

若要沿整个车辆路径在端口 **Y** 处指定多个位置，请先在 MATLAB 中定义 *Y* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Y**。若要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Yaw** — 车辆的偏航方向角 标量

车辆沿场景 *Z* 轴的偏航方向角。**Yaw** 位于惯性 *Z* 轴向上的坐标系中。单位为度。

**Initial rotation [Roll, Pitch, Yaw] (deg)** 参数的偏航值必须与仿真开始时此端口的值匹配。

若要沿整个车辆路径在端口 **Yaw** 处指定多个方向角，请先在 MATLAB 中定义偏航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Yaw**。若要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Light controls** — 车辆灯光控制 1×6 向量

灯光控制输入信号，指定为 1×6 布尔向量。向量的每个元素按照下表打开或关闭特定的车辆灯光。值为 1 时打开灯光；值为 0 时关闭灯光。

| 向量元素 | 车辆灯光 |
| --- | --- |
| (1,1) | 远光灯 |
| (1,2) | 近光灯 |
| (1,3) | 制动灯 |
| (1,4) | 倒车灯 |
| (1,5) | 左转向灯 |
| (1,6) | 右转向灯 |

#### 依赖关系

若要创建此端口，请在 **Light Controls** 选项卡上选择 **Enable light controls**。

**数据类型：** `Boolean`
### 输出

### **Location** — 车辆的位置 实数值 1×3 向量

车辆在场景中的 (*X*, *Y*, *Z*) 位置，以实数值 1×3 向量形式返回。此位置基于车辆原点，该原点位于地面上、车辆几何中心处。**Location** 值位于惯性 *Z* 轴向上的世界坐标系中。单位为米。

#### 依赖关系

若要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Orientation** — 车辆的方向 实数值 1×3 向量

车辆分别绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚方向角，以实数值 1×3 向量形式返回。此方向基于车辆原点，该原点位于地面上、车辆几何中心处。**Orientation** 值位于惯性 *Z* 轴向上的坐标系中。单位为弧度。

#### 依赖关系

若要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Type
  summary: 车辆类型 Muscle car（默认）| Sedan | Sport utility vehicle | Small pickup truck | Hatchback | Box truck | Custom
  group: 车辆参数
- name: Path to custom mesh
  summary: 自定义网格的路径 /MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar（默认）| 有效路径
  group: 车辆参数
- name: Track width in custom mesh (m)
  summary: 轮距 1.9（默认）| 标量
  group: 车辆参数
- name: Wheel base in custom mesh (m)
  summary: 轴距 3（默认）| 标量
  group: 车辆参数
- name: Wheel radius in custom mesh (m)
  summary: 车轮半径 0.35（默认）| 标量
  group: 车辆参数
- name: Color
  summary: 车辆颜色 Red（默认）| Orange | Yellow | Green | Blue | Black | White | Silver
  group: 车辆参数
- name: Initial position [X, Y, Z] (m)
  summary: 车辆初始位置 [0, 0, 0]（默认）| 实数值 1×3 向量
  group: 车辆参数
- name: Initial rotation [Roll, Pitch, Yaw] (deg)
  summary: 车辆初始旋转角度 [0, 0, 0]（默认）| 实数值 1×3 向量
  group: 车辆参数
- name: Name
  summary: 车辆名称 SimulinkVehicle1（默认）| 车辆名称
  group: 车辆参数
- name: Sample time
  summary: 采样时间 -1（默认）| 正标量
  group: 车辆参数
- name: Enable light controls
  summary: 控制车辆灯光 off（默认）| on
  group: 灯光控制
- name: Headlight color [R,G,B]
  summary: 前照灯颜色 [1,1,1]（默认）| 1×3 RGB 三元组值数组
  group: 灯光控制
- name: High beam intensity (cd)
  summary: 远光灯强度 100000（默认）| 正标量
  group: 灯光控制
- name: Low beam intensity (cd)
  summary: 近光灯强度 60000（默认）| 正标量
  group: 灯光控制
- name: High beam cone half angle (deg)
  summary: 远光灯锥半角 70（默认）| 小于或等于 90 的正标量
  group: 灯光控制
- name: Low beam cone half angle (deg)
  summary: 近光灯锥半角 70（默认）| 小于或等于 90 的正标量
  group: 灯光控制
- name: Left headlight beam orientation [Pitch, Yaw] (deg)
  summary: 左前照灯光束方向 [Pitch, Yaw] (deg) [0,0]（默认）| 值介于 -180 和 180 之间的 1×2 数组
  group: 灯光控制
- name: Right headlight beam orientation [Pitch, Yaw] (deg)
  summary: 右前照灯光束方向 [0,0]（默认）| 值介于 -180 和 180 之间的 1×2 数组
  group: 灯光控制
- name: Brake light intensity (cd/m^2)
  summary: 强度 500（默认）| 正标量
  group: 灯光控制
- name: Reverse light intensity (cd/m^2)
  summary: 强度 500（默认）| 正标量
  group: 灯光控制
- name: Turn signal light intensity (cd/m^2)
  summary: 强度 500（默认）| 正标量
  group: 灯光控制
- name: Period (s)
  summary: 转向信号灯周期 1（默认）| 正标量
  group: 灯光控制
- name: Pulse width (% of period)
  summary: 脉冲宽度 50（默认）| 小于 100 的正标量
  group: 灯光控制
- name: Output location (m) and orientation (rad)
  summary: 输出车辆的位置和方向 off（默认）| on
  group: 地面真值
```

### 车辆参数

### **Type** — 车辆类型 `Muscle car`（默认）| `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Custom`

选择车辆类型。若要获取每种车辆类型的尺寸，请参阅以下参考页面：

- `Muscle car` — Muscle Car
- `Sedan` — Sedan
- `Sport utility vehicle` — Sport Utility Vehicle
- `Small pickup truck` — Small Pickup Truck
- `Hatchback` — Hatchback
- `Box truck` —Box Truck

#### 依赖关系

选择 `Custom` 会启用允许您为车辆导入自定义网格的参数。

### **Path to custom mesh** — 自定义网格的路径 `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar`（默认）| 有效路径

自定义网格的路径。

若要创建自定义车辆网格，请参阅 Prepare Custom Vehicle Mesh for the Unreal Editor。

**示例：** `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_Sedan.SK_Sedan`

#### 依赖关系

若要启用此参数，请将 **Type** 设置为 `Custom`。

### **Track width in custom mesh (m)** — 轮距 `1.9`（默认）| 标量

自定义网格中的轮距，单位为 m。

#### 依赖关系

若要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel base in custom mesh (m)** — 轴距 `3`（默认）| 标量

自定义网格中的轴距，单位为 m。

#### 依赖关系

若要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel radius in custom mesh (m)** — 车轮半径 `0.35`（默认）| 标量

自定义网格中的车轮半径，单位为 m。

#### 依赖关系

若要启用此参数，请将 **Type** 设置为 `Custom`。

### **Color** — 车辆颜色 `Red`（默认）| `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver`

选择车辆的颜色。

### **Initial position [X, Y, Z] (m)** — 车辆初始位置 `[0, 0, 0]`（默认）| 实数值 1×3 向量

车辆沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。此位置位于惯性 *Z* 轴向上的坐标系中。单位为米。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时的 **X** 和 **Y** 输入端口值匹配。

### **Initial rotation [Roll, Pitch, Yaw] (deg)** — 车辆初始旋转角度 `[0, 0, 0]`（默认）| 实数值 1×3 向量

车辆初始旋转角度。旋转角度由车辆的横滚、俯仰和偏航定义。单位为度。

将此参数的偏航值设置为与仿真开始时的 **Yaw** 输入端口值匹配。

### **Name** — 车辆名称 `SimulinkVehicle1`（默认）| 车辆名称

车辆名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D Vehicle with Ground Following 模块的数量。

车辆名称会作为与车辆位于同一模型中的任何 Automated Driving Toolbox™ Simulation 3D 传感器模块的 **Parent name** 参数中的一个选项出现。使用 **Parent name** 参数，您可以选择要在其上安装传感器的车辆。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

采样时间 *Ts*，单位为秒。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### 灯光控制

### **Enable light controls** — 控制车辆灯光 `off`（默认）| `on`

选择是否控制车辆前照灯。使用启用的参数设置灯光参数，包括前照灯强度。

#### 依赖关系

选择此参数：

- 创建输入端口 `Light controls`
- 启用以下灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **Headlights** | - **Headlight color** - **High beam intensity** - **Low beam intensity** - **High beam cone half angle** - **Low beam cone half angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **Brake lights** | **Brake light intensity** |
  | **Reverse lights** | **Reverse light intensity** |
  | **Turn signal lights** | - **Turn signal light intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B]** — 前照灯颜色 `[1,1,1]`（默认）| 1×3 RGB 三元组值数组

前照灯颜色，指定为归一化的 1×3 RGB 三元组值数组。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `int8` | `uint8`

### **High beam intensity (cd)** — 远光灯强度 `100000`（默认）| 正标量

远光灯强度，单位为 cd。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam intensity (cd)** — 近光灯强度 `60000`（默认）| 正标量

近光灯强度，单位为 cd。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **High beam cone half angle (deg)** — 远光灯锥半角 `70`（默认）| 小于或等于 90 的正标量

远光灯锥半角，单位为度。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam cone half angle (deg)** — 近光灯锥半角 `70`（默认）| 小于或等于 90 的正标量

近光灯锥半角，单位为度。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Left headlight beam orientation [Pitch, Yaw] (deg)** — 左前照灯光束方向 [Pitch, Yaw] (deg) `[0,0]`（默认）| 值介于 -180 和 180 之间的 1×2 数组

左前照灯光束方向在 *Z* 轴向上的坐标系中的俯仰和偏航方向，指定为 1×2 数组，单位为度。数组的第一个元素 `[1,1]` 是俯仰角。数组的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Right headlight beam orientation [Pitch, Yaw] (deg)** — 右前照灯光束方向 `[0,0]`（默认）| 值介于 -180 和 180 之间的 1×2 数组

右前照灯光束方向在 *Z* 轴向上的坐标系中的俯仰和偏航方向，指定为 1×2 数组，单位为度。数组的第一个元素 `[1,1]` 是俯仰角。数组的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

#### 制动灯

### **Brake light intensity (cd/m^2)** — 强度 `500`（默认）| 正标量

制动灯强度，单位为 cd/m^2。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 倒车灯

### **Reverse light intensity (cd/m^2)** — 强度 `500`（默认）| 正标量

倒车灯强度，单位为 cd/m^2。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 转向信号灯

### **Turn signal light intensity (cd/m^2)** — 强度 `500`（默认）| 正标量

转向信号灯强度，单位为 cd/m^2。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Period (s)** — 转向信号灯周期 `1`（默认）| 正标量

转向信号灯周期，单位为 s。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Pulse width (% of period)** — 脉冲宽度 `50`（默认）| 小于 100 的正标量

转向信号灯脉冲宽度，以周期的百分比表示。

#### 依赖关系

若要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### 地面真值

### **Output location (m) and orientation (rad)** — 输出车辆的位置和方向 `off`（默认）| `on`

选择此参数可分别在 **Location** 和 **Orientation** 端口输出车辆的位置和方向。
## 所属库

Automated Driving Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Vehicle with Ground Following 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现跟随地面的车辆

**注意**

使用 Simulation 3D Vehicle with Ground Following 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Vehicle with Ground Following 模块在 3D 仿真环境中实现一辆带四个车轮的车辆。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块使用车辆的输入 (*X*, *Y*) 位置和偏航角来调整车辆的高程、横滚角和俯仰角，使其跟随地面地形。该模块确定车辆的速度和航向，并调整每个车轮的转向角和旋转。请将此模块用于自动驾驶应用。

若要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Vehicle with Ground Following 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J670 [1] 和 ISO 8855 [2] 中定义的车辆 *Z* 轴向上右手 (RH) 笛卡尔坐标系。该坐标系是惯性的，并且初始与车辆几何中心对齐：

- *X* 轴沿车辆的纵轴并指向前方。
- *Y* 轴沿车辆的横轴并指向左侧。
- *Z* 轴指向上方。

分别绕 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚角，当沿这些轴的正方向观察时，在顺时针方向上为正。车辆放置在场景的世界坐标系中。有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

**提示**

Simulation 3D Vehicle with Ground Following 模块必须在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Vehicle with Ground Following 模块会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好信号数据。若要检查模块执行顺序，请右键点击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- 带地面跟随的仿真三维车辆 — `-1`

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。

您可以配置 Simulation 3D Vehicle with Ground Following 模块以导入自定义网格并控制车辆灯光。
