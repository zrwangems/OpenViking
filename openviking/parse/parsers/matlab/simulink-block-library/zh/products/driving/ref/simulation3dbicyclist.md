---
type: simulink-block
title: 'Simulation 3D Bicyclist'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Scene and Vehicle Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dbicyclist'
documentation_source_path: 'ref/simulation3dbicyclist.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Bicyclist

## 端口

### 输入

### **Y** — 骑行者的横向位置 scalar

骑行者沿场景 *Y* 轴的横向位置。**Y** 位于惯性 *Z*-up 坐标系中。单位为 meters。

**Initial position [X, Y, Z] (m)** 参数的 *Y* 值必须与仿真开始时此端口的值匹配。

要沿整个骑行者路径在端口 **Y** 指定多个位置，请先在 MATLAB® 中定义 *Y* 航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些航路点馈送到 **Y**。要了解如何选择和指定航路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **X** — 骑行者的纵向位置 scalar

骑行者沿场景 *X* 轴的纵向位置。**X** 位于惯性 *Z*-up 坐标系中。单位为 meters。

**Initial position [X, Y, Z] (m)** 参数的 *X* 值必须与仿真开始时此端口的值匹配。

要沿整个骑行者路径在端口 **X** 指定多个位置，请先在 MATLAB 中定义 *X* 航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些航路点馈送到 **X**。要了解如何选择和指定航路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Yaw** — 骑行者偏航方向角 scalar

骑行者沿场景 *Z* 轴的偏航方向角。**Yaw** 位于 *Z*-up 坐标系中。

**Initial rotation [Roll, Pitch, Yaw] (deg)** 参数的 yaw 值必须与仿真开始时此端口的值匹配。

要沿整个骑行者路径在端口 **Yaw** 指定多个方向角，请先在 MATLAB 中定义 yaw 航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些航路点馈送到 **Yaw**。要了解如何选择和指定航路点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### 输出

### **Location** — 骑行者位置 real-valued 1-by-3 vector

骑行者在地面场景中的 (*X*, *Y*, *Z*) 位置，以 real-valued 1-by-3 vector 形式返回。此位置基于骑行者原点，该原点位于地面上、骑行者的几何中心处。**Location** 值位于惯性 *Z*-up 世界坐标系中。单位为 meters。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Orientation** — 骑行者方向 real-valued 1-by-3 vector

骑行者分别围绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚方向角，以 real-valued 1-by-3 vector 形式返回。此方向基于骑行者原点，该原点位于地面上、骑行者的几何中心处。**Orientation** 值位于惯性 *Z*-up 坐标系中。单位为 radians。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### Bicyclist 参数

### **Scale** — 骑行者的缩放因子 `[1, 1, 1]`（默认）| real-valued 1-by-3 vector

骑行者沿 *X* 轴、*Y* 轴和 *Z* 轴的缩放因子。

### **Initial position [X, Y, Z] (m)** — 初始骑行者位置 `[0, 0, 0]`（默认）| real-valued 1-by-3 vector

骑行者沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。此位置位于惯性 *Z*-up 坐标系中。单位为 meters。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时 **X** 和 **Y** 输入端口值匹配。

### **Initial rotation [Roll, Pitch, Yaw] (deg)** — 骑行者旋转初始角度 `[0, 0, 0]`（默认）| real-valued 1-by-3 vector

骑行者旋转的初始角度。旋转角度由骑行者的横滚、俯仰和偏航定义。单位为 degrees。

将此参数的 yaw 值设置为与仿真开始时 **Yaw** 输入端口值匹配。

### **Name** — 骑行者名称 `SimulinkBicyclist1`（默认）| bicyclist name

骑行者名称。默认情况下，当您在模型中使用该模块时，该模块将 **Name** 参数设置为 `SimulinkBicyclistX`。`X` 的值取决于模型中拥有的 Simulation 3D Bicyclist 模块数量。

骑行者名称将作为 **Parent name** 参数中的一个选择出现，该参数位于与该骑行者相同的模型中的任何 Simulation 3D sensor 模块中。使用 **Parent name** 参数，您可以选择要在其上安装传感器的骑行者。

### **Sample time** — 采样时间 `-1`（默认）| positive scalar

采样时间 *Ts*，以 seconds 为单位。图形帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### Ground Truth

### **Output location (m) and orientation (rad)** — 行人的输出位置和方向 `off`（默认）| `on`

选择此参数可在 **Location** 和 **Orientation** 端口分别输出行人的位置和方向。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Bicyclist 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现骑行者

**注意**

使用 Simulation 3D Bicyclist 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Bicyclist 模块在 3D 仿真环境中实现骑行者。该模块使用骑行者的输入 (*X*, *Y*) 位置和偏航角来调整高程、横滚角和俯仰角，以使骑行者跟随地面地形。该模块确定骑行者速度和航向，并相应地将运动调整为空闲、踩踏或制动。

要使用此模块，请确保您的模型中有 Simulation 3D Scene Configuration 模块。如果您将 Simulation 3D Pedestrian 模块的 **Sample time** 参数设置为 `-1`，则该模块将继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用在 SAE J670 [1] 和 ISO 8855 [2] 中定义的骑行者 *Z*-up 右手 (RH) 笛卡尔坐标系。该坐标系是惯性的，并且最初与两个车轮之间的骑行者-地面接触线对齐：

- *X* 轴沿骑行者的纵轴，并指向前方。
- *Y* 轴沿骑行者的横轴，并指向左侧。
- *Z* 轴指向上方。

当沿这些轴的正方向观察时，*Z* 轴、*Y* 轴和 *X* 轴的偏航角、俯仰角和横滚角分别在顺时针方向上为正。骑行者放置在场景的世界坐标系中。有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。
