---
type: simulink-block
title: 'Simulation 3D Vehicle with Ground Following'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dvehiclewithgroundfollowing'
documentation_source_path: 'ref/simulation3dvehiclewithgroundfollowing.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Vehicle with Ground Following

## 端口

### 输入

### **X** — 车辆纵向位置 标量

车辆沿场景 *X* 轴的纵向位置。**X** 位于惯性 *Z*-down 坐标系中。单位为 meters。

### **Y** — 车辆横向位置 标量

车辆沿场景 *Y* 轴的横向位置。**Y** 位于惯性 *Z*-down 坐标系中。单位为 meters。

### **Yaw** — 车辆偏航方向角 标量

车辆沿场景 *Z* 轴的偏航方向角。**Yaw** 位于惯性 *Z*-down 坐标系中。单位为 radians。

### **Light controls** — 车辆灯光控制 1×6 向量

灯光控制输入信号，指定为 1×6 Boolean 向量。向量的每个元素打开或关闭特定的车辆灯光，如下表所示。值为 1 时打开灯光；值为 0 时关闭灯光。

| 向量元素 | 车辆灯光 |
| --- | --- |
| (1,1) | 前照灯远光 |
| (1,2) | 前照灯近光 |
| (1,3) | 制动 |
| (1,4) | 倒车 |
| (1,5) | 左转向信号 |
| (1,6) | 右转向信号 |

#### 依赖关系

要创建此端口，请在 **灯光控制** 选项卡上，选择 **Enable light controls**。

**数据类型:** `Boolean`

## 参数

### 车辆参数

### **Type** — 车辆类型 `Muscle car` (default) | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Formula Student Vehicle` | `Custom`

选择车辆类型。要获取每种车辆类型的尺寸，请参阅以下参考页面：

- `Muscle car` — Muscle Car
- `Sedan` — Sedan
- `Sport utility vehicle` — Sport Utility Vehicle
- `Small pickup truck` — Small Pickup Truck
- `Hatchback` — Hatchback
- `Box truck` —
  Box Truck
- `Formula student vehicle` — Formula
  Student Vehicle

#### 依赖关系

选择 `Custom` 会启用允许您为车辆导入自定义网格的参数。

### **Path to custom mesh, MeshPath** — 自定义网格的路径 `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar` (default) | 有效路径

自定义网格的路径。

要创建自定义车辆网格，请参阅为 Unreal Editor 准备自定义车辆网格。

**示例：** `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_Sedan.SK_Sedan`

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Custom`。

### **Track width in custom mesh, TrackWidth** — 轮距 `1.9` (default) | 标量

自定义网格中的轮距，单位为 m。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Custom`。

### **Wheel base in custom mesh, WheelBase** — 轴距 `3` (default) | 标量

自定义网格中的轴距，单位为 m。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Custom`。

### **Wheel radius in custom mesh, WheelRadius** — 车轮半径 `0.35` (default) | 标量

自定义网格中的车轮半径，单位为 m。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Custom`。

### **Color** — 车辆颜色 `Red` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver`

选择车辆的颜色。

### **Initial position [X, Y, Z], InitialPos (m)** — 初始车辆位置 `[0, 0, 0]` (default) | 实数值 1×3 向量

车辆沿惯性 *Z*-down 坐标系中 *X* 轴、*Y* 轴和 *Z* 轴的初始位置，单位为 m。

### **Initial rotation [Roll, Pitch, Yaw], InitialRot (rad)** — 车辆旋转初始角度 `[0, 0, 0]` (default) | 实数值 1×3 向量

车辆旋转初始角度，单位为 rad。旋转角度由车辆的横滚、俯仰和偏航定义。

### **Name, ActorName** — 车辆名称 `SimulinkVehicle1` (default) | 车辆名称

车辆名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为
`SimulinkVehicleX`。`X` 的值取决于您模型中 Simulation 3D Vehicle with Ground Following 模块的数量。

### **Sample time, SampleTime** — 采样时间 `-1` (default) | 正标量

采样时间，*Ts*。图形帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### 灯光控制

### **Enable light controls** — 控制车辆灯光的选项 `off` (default) | `on`

选择是否控制车辆前照灯。使用启用的参数来设置灯光参数，包括前照灯强度。

#### 依赖关系

选择此参数：

- 创建输入端口 `Light
  controls`。
- 启用这些灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **前照灯** | - **Headlight color** - **High beam   intensity** - **Low beam   intensity** - **High beam cone half   angle** - **Low beam cone half   angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **制动灯** | **Brake light intensity** |
  | **倒车灯** | **Reverse light intensity** |
  | **转向信号灯** | - **Turn signal light   intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B], HeadlightColor** — 前照灯颜色 `[1,1,1]` (default) | RGB 三元组值的 1×3 向量

前照灯颜色，指定为归一化的 RGB 三元组值 1×3 向量。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `int8` | `uint8`

### **High beam intensity, HighBeamIntensity** — 远光强度 `100000` (default) | 正标量

远光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Low beam intensity, LowBeamIntensity** — 近光强度 `60000` (default) | 正标量

近光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **High beam cone half angle, HighBeamConeAngle** — 远光锥半角 `1.22` (default) | 小于 pi/2 的正标量

远光锥半角，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Low beam cone half angle, LowBeamConeAngle** — 近光锥半角 `1.22` (default) | 小于 pi/2 的正标量

近光锥半角，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — 左前照灯光束方向 `[0,0]` (default) | 值介于 -pi 和 pi 之间的 1×2 向量

左前照灯光束方向在 *Z*-down 坐标系中的俯仰和偏航方向，指定为 1×2 向量，单位为 rad。向量的第一个元素 `[1,1]` 是俯仰角。向量的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — 右前照灯光束方向 `[0,0]` (default) | 值介于 -pi 和 pi 之间的 1×2 向量

右前照灯光束方向在 *Z*-down 坐标系中的俯仰和偏航方向，指定为 1×2 向量，单位为 rad。向量的第一个元素 `[1,1]` 是俯仰角。向量的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

#### 制动灯

### **Brake light intensity, BrakelightIntensity** — 制动灯强度 `500` (default) | 正标量

制动灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

#### 倒车灯

### **Reverse light intensity, ReverselightIntensity** — 倒车灯强度 `500` (default) | 正标量

倒车灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

#### 转向信号灯

### **Turn signal light intensity, SignallightIntensity** — 转向信号灯强度 `500` (default) | 正标量

转向信号灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Period, SignallightPeriod** — 转向信号灯周期 `1` (default) | 正标量

转向信号灯周期，单位为 s。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

### **Pulse width, SignalPulseWidth** — 脉冲宽度 `50` (default) | 小于 100 的正标量

转向信号灯脉冲宽度，指定为周期的百分比。

#### 依赖关系

要启用此参数，请选择 **Enable light
controls**。

**数据类型:** `double`

## 所属库

Automated Driving Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Vehicle with Ground Following 模块模拟模型需要 Simulink
3D Animation。

## 描述

在 3D 环境中实现跟随地面的车辆

**注意**

使用 Simulation 3D Vehicle with Ground Following 模块模拟模型需要 Simulink®
3D Animation™。

Simulation 3D Vehicle with Ground Following 模块在 3D 仿真环境中实现具有四个车轮的车辆。此环境使用 Epic Games® 的 Unreal Engine® 渲染。该模块使用车辆的输入 (*X*, *Y*) 位置和偏航角来调整车辆的高程、横滚角和俯仰角，使其跟随地面地形。该模块确定车辆速度和航向，并调整每个车轮的转向角和旋转。将此模块用于自动驾驶应用。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Vehicle with Ground Following 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J6701 中定义的车辆 Z-down *right-handed* (RH) *Cartesian* 坐标系。该坐标系为惯性坐标系，并且初始与车辆几何中心对齐：

- *X* 轴 — 沿车辆纵轴，指向前方
- *Y* 轴 — 沿车辆横轴，指向右侧
- *Z* 轴 — 指向下方

**提示**

Simulation 3D Vehicle with Ground Following 模块必须在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Vehicle with Ground Following 模块会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好这些数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认这些 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle with Ground Following —
  `-1`

有关执行顺序的详细信息，请参阅控制并显示执行顺序。

您可以配置 Simulation 3D Vehicle with Ground Following 模块以导入自定义网格并控制车辆灯光。
