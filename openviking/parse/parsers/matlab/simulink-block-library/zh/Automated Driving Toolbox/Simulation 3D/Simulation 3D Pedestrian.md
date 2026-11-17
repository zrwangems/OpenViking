---
type: simulink-block
title: 'Simulation 3D Pedestrian'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dpedestrian'
documentation_source_path: 'ref/simulation3dpedestrian.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Pedestrian

## 端口

### 输入

### **Y** — 行人的横向位置 标量

行人沿场景 *Y* 轴的横向位置。**Y** 位于惯性 *Z* 轴向上的坐标系中。单位为米。

**Initial position [X, Y, Z] (m)** 参数的 *Y* 值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **Y** 处指定多个位置，请先在 MATLAB® 中定义 *Y* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Y**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **X** — 行人的纵向位置 标量

行人沿场景 *X* 轴的纵向位置。**X** 位于惯性 *Z* 轴向上的坐标系中。单位为米。

**Initial position [X, Y, Z] (m)** 参数的 *X* 值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **X** 处指定多个位置，请先在 MATLAB 中定义 *X* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **X**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Yaw** — 行人的偏航方向角 标量

行人沿场景 *Z* 轴的偏航方向角。**Yaw** 位于惯性 *Z* 轴向上的坐标系中。

**Initial rotation [Roll, Pitch, Yaw] (deg)** 参数的偏航值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **Yaw** 处指定多个方向角，请先在 MATLAB 中定义偏航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Yaw**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。
### 输出

### **Location** — 行人的位置 实数值 1×3 向量

行人在场景中的 (*X*, *Y*, *Z*) 位置，以实数值 1×3 向量形式返回。此位置基于行人原点，该原点位于地面上，处于行人的几何中心。**Location** 值位于惯性 *Z* 轴向上的世界坐标系中。单位为米。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Orientation** — 行人的方向 实数值 1×3 向量

行人分别绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚方向角，以实数值 1×3 向量形式返回。此方向基于行人原点，该原点位于地面上，处于行人的几何中心。**Orientation** 值位于惯性 *Z* 轴向上的坐标系中。单位为弧度。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上，选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 行人参数

### **Type** — 行人类型 `Male 1`（默认）| `Male 2` | `Male 3` | `Female 1` | `Female 2` | `Female 3` | `Child`

行人类型，指定为以下选项之一：

- `Male 1`
- `Male 2`
- `Male 3`
- `Female 1`
- `Female 2`
- `Female 3`
- `Child`

### **Scale** — 行人的缩放因子 `[1, 1, 1]`（默认）| 实数值 1×3 向量

行人沿 *X* 轴、*Y* 轴和 *Z* 轴的缩放因子。

### **Initial position [X, Y, Z] (m)** — 行人初始位置 `[0, 0, 0]`（默认）| 实数值 1×3 向量

行人沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。此位置位于惯性 *Z* 轴向上的坐标系中。单位为米。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时的 **X** 和 **Y** 输入端口值匹配。

### **Initial yaw (deg)** — 行人旋转的初始角度 `0`（默认）| 实数值标量

行人旋转的初始偏航角。单位为度。

将此参数的偏航值设置为与仿真开始时的 **Yaw** 输入端口值匹配。

### **Name** — 行人名称 `SimulinkPedestrian1`（默认）| 行人名称

行人名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkPedestrianX`。`X` 的值取决于模型中 Simulation 3D Pedestrian 模块的数量。

行人名称会作为与行人位于同一模型中的任何 Simulation 3D 传感器模块的 **Parent name** 参数中的一个选项出现。使用 **Parent name** 参数，您可以选择要在其上安装传感器的行人。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

采样时间 *Ts*，以秒为单位。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### Ground Truth

### **Output location (m) and orientation (rad)** — 输出行人的位置和方向 `off`（默认）| `on`

选择此参数可分别在 **Location** 和 **Orientation** 端口输出行人的位置和方向。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Pedestrian 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现行人

**注意**

使用 Simulation 3D Pedestrian 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Pedestrian 模块在 3D 仿真环境中实现行人。该模块使用行人的输入 (*X*, *Y*) 位置和偏航角来调整高程、横滚角和俯仰角，使行人跟随地面地形。该模块确定行人的速度和朝向，并相应地调整运动为空闲、行走或奔跑。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Pedestrian 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J670 [1] 和 ISO 8855 [2] 中定义的、行人 *Z* 轴向上的右手 (RH) 笛卡尔坐标系。该坐标系是惯性的，并且初始与行人双脚对齐：

- *X* 轴沿行人的纵轴，指向正前方。
- *Y* 轴沿行人的横轴，指向左侧。
- *Z* 轴指向上方。

分别绕 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚角，当沿这些轴的正方向观察时，在顺时针方向上为正。行人被放置在场景的世界坐标系中。有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。
