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

行人在场景 *Y* 轴上的横向位置。**Y** 处于惯性 *Z*-up 坐标系中。单位为 meters。

**Initial position [X, Y, Z] (m)** 参数的 *Y* 值必须与此端口在仿真开始时的值匹配。

若要沿整条行人路径在端口 **Y** 指定多个位置，请先在 MATLAB® 中定义 *Y* 航点的时间序列。然后，通过使用 From Workspace (Simulink) 模块将这些航点馈送到 **Y**。若要了解如何选择和指定航点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **X** — 行人的纵向位置 标量

行人在场景 *X* 轴上的纵向位置。**X** 处于惯性 *Z*-up 坐标系中。单位为 meters。

**Initial position [X, Y, Z] (m)** 参数的 *X* 值必须与此端口在仿真开始时的值匹配。

若要沿整条行人路径在端口 **X** 指定多个位置，请先在 MATLAB 中定义 *X* 航点的时间序列。然后，通过使用 From Workspace (Simulink) 模块将这些航点馈送到 **X**。若要了解如何选择和指定航点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### **Yaw** — 行人的偏航姿态角 标量

行人在场景 *Z* 轴上的偏航姿态角。**Yaw** 处于惯性 *Z*-up 坐标系中。

**Initial rotation [Roll, Pitch, Yaw] (deg)** 参数的偏航角值必须与此端口在仿真开始时的值匹配。

若要沿整条行人路径在端口 **Yaw** 指定多个姿态角，请先在 MATLAB 中定义 yaw 航点的时间序列。然后，通过使用 From Workspace (Simulink) 模块将这些航点馈送到 **Yaw**。若要了解如何选择和指定航点，请参阅 Select Waypoints for Unreal Engine Simulation 示例。

### 输出

### **Location** — 行人的位置 实值 1×3 向量

行人在场景中的 (*X*, *Y*, *Z*) 位置，返回为实值 1×3 向量。此位置基于行人原点，该原点位于地面上，在行人的几何中心。**Location** 值处于惯性 *Z*-up 世界坐标系中。单位为 meters。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

### **Orientation** — 行人的姿态 实值 1×3 向量

行人分别绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚姿态角，返回为实值 1×3 向量。此姿态基于行人原点，该原点位于地面上，在行人的几何中心。**Orientation** 值处于惯性 *Z*-up 坐标系中。单位为 radians。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location (m) and orientation (rad)**。

**数据类型：** `double`

## 参数

### 行人参数

### **Type** — 行人的类型 `Male 1`（默认） | `Male 2` | `Male 3` | `Female 1` | `Female 2` | `Female 3` | `Child`

行人的类型，指定为以下选项之一：

- `Male 1`
- `Male 2`
- `Male 3`
- `Female 1`
- `Female 2`
- `Female 3`
- `Child`

### **Scale** — 行人的缩放因子 `[1, 1, 1]`（默认） | 实值 1×3 向量

行人沿 *X* 轴、*Y* 轴和 *Z* 轴的缩放因子。

### **Initial position [X, Y, Z] (m)** — 行人的初始位置 `[0, 0, 0]`（默认） | 实值 1×3 向量

行人在场景 *X* 轴、*Y* 轴和 *Z* 轴上的初始位置。此位置处于惯性 *Z*-up 坐标系中。单位为 meters。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时的 **X** 和 **Y** 输入端口值匹配。

### **Initial yaw (deg)** — 行人旋转的初始角度 `0`（默认） | 实值标量

行人旋转的初始偏航角。单位为 degrees。

将此参数的偏航角值设置为与仿真开始时的 **Yaw** 输入端口值匹配。

### **Name** — 行人的名称 `SimulinkPedestrian1`（默认） | 行人名称

行人的名称。默认情况下，当您在模型中使用该模块时，该模块会将 **Name** 参数设置为 `SimulinkPedestrianX`。`X` 的值取决于模型中具有的 Simulation 3D Pedestrian 模块的数量。

行人名称会作为选择项出现在与行人在同一模型中的任何 Simulation 3D sensor 模块的 **Parent name** 参数中。使用 **Parent name** 参数，您可以选择要在其上安装传感器的行人。

### **Sample time** — 采样时间 `-1`（默认） | 正标量

采样时间 *Ts*，单位为 seconds。图形帧速率是采样时间的倒数。

如果您将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### Ground Truth

### **Output location (m) and orientation (rad)** — 行人的输出位置和姿态 `off`（默认） | `on`

选择此参数以在 **Location** 和 **Orientation** 端口分别输出行人的位置和姿态。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Pedestrian 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现行人

**注意**

使用 Simulation 3D Pedestrian 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Pedestrian 模块在 3D 仿真环境中实现一个行人。该模块使用行人的输入 (*X*, *Y*) 位置和偏航角来调整高程、横滚角和俯仰角，使行人跟随地面地形。该模块确定行人的速度和朝向，并相应地将移动调整为 idle、walk 或 run。

要使用此模块，请确保您的模型中包含 Simulation 3D Scene Configuration 模块。如果您将 Simulation 3D Pedestrian 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J670 [1] 和 ISO 8855 [2] 中定义的行人 *Z*-up 右手 (RH) 笛卡尔坐标系。该坐标系是惯性的，并且最初与行人的脚部对齐：

- *X* 轴沿行人的纵轴，指向正前方。
- *Y* 轴沿行人的横轴，指向左侧。
- *Z* 轴指向上方。

*Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚角分别在沿这些轴的正方向观察时，在顺时针方向上为正。行人被放置在场景的世界坐标系中。有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。
