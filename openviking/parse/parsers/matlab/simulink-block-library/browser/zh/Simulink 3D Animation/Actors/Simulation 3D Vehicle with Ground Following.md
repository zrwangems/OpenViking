---
type: simulink-block
title: 'Simulation 3D Vehicle with Ground Following'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Actors'
documentation_page: 'simulation3dvehiclewithgroundfollowing'
documentation_source_path: 'simulation3dvehiclewithgroundfollowing.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Vehicle with Ground Following

## 端口

### 输入

### **X** — 车辆纵向位置 标量

车辆沿场景 *X* 轴的纵向位置。

**Initial position [X, Y, Z]** 参数的 *X* 值必须与此端口在仿真开始时的值匹配。

### **Y** — 车辆横向位置 标量

车辆沿场景 *Y* 轴的横向位置。

**Initial position [X, Y, Z]** 参数的 *Y* 值必须与此端口在仿真开始时的值匹配。

### **Yaw** — 车辆偏航方向角 标量

车辆沿场景 *Z* 轴的偏航方向角。
.

**Initial rotation [Roll, Pitch, Yaw]** 参数的 yaw 值必须与此端口在仿真开始时的值匹配。

### **Light controls** — 车辆灯光控制 1-by-6 向量

Light controls 输入信号，指定为 1-by-6 Boolean 向量。向量的每个元素打开或关闭特定的车辆灯，如下表所示。值 1 打开灯；值 0 关闭灯。

| 向量元素 | 车辆灯 |
| --- | --- |
| (1,1) | 前照灯远光 |
| (1,2) | 前照灯近光 |
| (1,3) | 制动 |
| (1,4) | 倒车 |
| (1,5) | 左转向信号 |
| (1,6) | 右转向信号 |

#### 依赖关系

要创建此端口，请在 **Light Controls** 选项卡上，选择 **Enable light controls**。

**数据类型：** `Boolean`

### 输出

### **Location** — 车辆位置 实值 1-by-3 向量

(*X*, *Y*, *Z*) 车辆在场景中的位置，以实值 1-by-3 向量返回。此位置基于车辆原点，该原点位于地面上、车辆几何中心处。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上，选择 **Output location and orientation**。

**数据类型：** `double`

### **Orientation** — 车辆朝向 实值 1-by-3 向量

车辆绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚方向角，分别以实值 1-by-3 向量返回。此朝向基于车辆原点，该原点位于地面上、车辆几何中心处。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上，选择 **Output location and orientation**。

**数据类型：** `double`

## 参数

### 车辆参数

### **Type** — 车辆类型 `Muscle car` (默认) | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Custom`

选择车辆类型。要获取每种车辆类型的尺寸，请参阅以下参考页：

- `Muscle car` — Muscle Car (Automated Driving Toolbox)
- `Sedan` — Sedan (Automated Driving Toolbox)
- `Sport utility vehicle` — Sport Utility Vehicle (Automated Driving Toolbox)
- `Small pickup truck` — Small Pickup Truck (Automated Driving Toolbox)
- `Hatchback` — Hatchback (Automated Driving Toolbox)
- `Box truck` —Box Truck (Automated Driving Toolbox)

#### 依赖关系

选择 `Custom` 会启用允许您为车辆导入自定义网格的参数。

### **Path to custom mesh** — 自定义网格的路径 `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar` (默认) | 有效路径

自定义网格的路径。

要创建自定义车辆网格，请参阅 Prepare Custom Vehicle Mesh for the Unreal Editor (Automated Driving Toolbox)。

**示例：** `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_Sedan.SK_Sedan`

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Track width in custom mesh (m)** — 轮距 `1.9` (默认) | 标量

自定义网格中的轮距，以 m 为单位。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel base in custom mesh (m)** — 轴距 `3` (默认) | 标量

自定义网格中的轴距，以 m 为单位。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Wheel radius in custom mesh (m)** — 车轮半径 `0.35` (默认) | 标量

自定义网格中的车轮半径，以 m 为单位。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Color** — 车辆颜色 `Red` (默认) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver`

选择车辆的颜色。

### **Coordinate system** — 用于 actor 变换的坐标系 `ISO8855` (默认) | `Default` | `MATLAB` | `AERO` | `VRML` | `SAE`

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

### **Initial position [X, Y, Z]** — 初始车辆位置 `[0, 0, 0]` (默认) | 实值 1-by-3 向量

车辆沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时的 **X** 和 **Y** 输入端口值匹配。

### **Initial rotation [Roll, Pitch, Yaw]** — 车辆旋转的初始角度 `[0, 0, 0]` (默认) | 实值 1-by-3 向量

车辆旋转的初始角度。旋转角度由车辆的 roll、pitch 和 yaw 定义。

将此参数的 yaw 值设置为与仿真开始时的 **Yaw** 输入端口值匹配。

### **Name** — 车辆名称 `SimulinkVehicle1` (默认) | 车辆名称

车辆名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D Vehicle with Ground Following 模块的数量。

车辆名称会在与车辆同一模型中的任何 Automated Driving Toolbox™ Simulation 3D 传感器模块的 **Parent name** 参数中显示为选项。使用 **Parent name** 参数，您可以选择要在其上安装传感器的车辆。

### **Sample time** — 采样时间 `-1` (默认) | 正标量

采样时间，*Ts*，以秒为单位。图形帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### 灯光控制

### **Enable light controls** — 控制车辆灯 `off` (默认) | `on`

选择是否控制车辆前照灯。使用启用的参数设置灯光参数，包括前照灯强度。

#### 依赖关系

选择此参数：

- 创建输入端口 `Light controls`
- 启用这些灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **前照灯** | - **Headlight color** - **High beam intensity** - **Low beam intensity** - **High beam cone half angle** - **Low beam cone half angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **制动灯** | **Brake light intensity** |
  | **倒车灯** | **Reverse light intensity** |
  | **转向信号灯** | - **Turn signal light intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B]** — 前照灯颜色 `[1,1,1]` (默认) | 1-by-3 的 RGB 三元组值数组

前照灯颜色，指定为归一化 1-by-3 的 RGB 三元组值数组。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `int8` | `uint8`

### **High beam intensity (cd)** — 远光强度 `100000` (默认) | 正标量

远光强度，以 cd 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam intensity (cd)** — 近光强度 `60000` (默认) | 正标量

近光强度，以 cd 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **High beam cone half angle (deg)** — 远光锥半角 `70` (默认) | 小于或等于 90 的正标量

远光锥半角，以 deg 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam cone half angle (deg)** — 近光锥半角 `70` (默认) | 小于或等于 90 的正标量

近光锥半角，以 deg 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Left headlight beam orientation [Pitch, Yaw] (deg)** — 左前照灯光束方向 [Pitch, Yaw] (deg) `[0,0]` (默认) | 值介于 -180 和 180 之间的 1-by-2 数组

在 *Z*-up 坐标系中左前照灯光束方向的俯仰和偏航方向，指定为 1-by-2 数组，以 deg 为单位。数组的第一个元素 `[1,1]` 是俯仰角。数组的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Right headlight beam orientation [Pitch, Yaw] (deg)** — 右前照灯光束方向 `[0,0]` (默认) | 值介于 -180 和 180 之间的 1-by-2 数组

在 *Z*-up 坐标系中右前照灯光束方向的俯仰和偏航方向，指定为 1-by-2 数组，以 deg 为单位。数组的第一个元素 `[1,1]` 是俯仰角。数组的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

#### 制动灯

### **Brake light intensity (cd/m^2)** — 强度 `500` (默认) | 正标量

制动灯强度，以 cd/m^2 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 倒车灯

### **Reverse light intensity (cd/m^2)** — 强度 `500` (默认) | 正标量

倒车灯强度，以 cd/m^2 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 转向信号灯

### **Turn signal light intensity (cd/m^2)** — 强度 `500` (默认) | 正标量

转向信号灯强度，以 cd/m^2 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Period (s)** — 转向信号灯周期 `1` (默认) | 正标量

转向信号灯周期，以 s 为单位。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Pulse width (% of period)** — 脉冲宽度 `50` (默认) | 小于 100 的正标量

转向信号灯脉冲宽度，以周期的百分比表示。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### 地面真值

### **Output location and orientation** — 输出车辆的位置和朝向 `off` (默认) | `on`

选择此参数以分别在 **Location** 和 **Orientation** 端口输出车辆的位置和朝向。

## 所属库

Automated Driving Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：设置 coordinate system 参数

设置 Simulation 3D Vehicle with Ground Following 模块中的 **Coordinate system** 参数，以表示 3D 环境中 actor 变换的坐标系。

## 描述

在 3D 环境中实现跟随地面的车辆

Simulation 3D Vehicle with Ground Following 模块在 3D 仿真环境中实现具有四个车轮的车辆。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块使用车辆的输入 (*X*, *Y*) 位置和偏航角来调整车辆的高程、横滚角和俯仰角，使其跟随地面地形。该模块确定车辆速度和航向，并调整每个车轮的转向角和旋转。将此模块用于自动驾驶应用。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Vehicle with Ground Following 模块的 **Sample time** 参数设置为 `-1`，该模块将继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块的 **Coordinate system** 参数指定 actor 变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。

**提示**

Simulation 3D Vehicle with Ground Following 模块必须在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Vehicle with Ground Following 模块会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle with Ground Following — `-1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order (Simulink)。

您可以配置 Simulation 3D Vehicle with Ground Following 模块以导入自定义网格并控制车辆灯。
