---
type: simulink-block
title: 'Simulation 3D Pedestrian'
family: 'simulation-3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Actors'
documentation_page: 'simulation3dpedestrian'
documentation_source_path: 'simulation3dpedestrian.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Pedestrian

## 端口

### 输入

### **Y** — 行人横向位置 标量

行人沿场景 *Y* 轴的横向位置。

**初始位置 [X, Y, Z]** 参数的 *Y* 值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **Y** 指定多个位置，请先在 MATLAB® 中定义 *Y* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Y**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### **X** — 行人纵向位置 标量

行人沿场景 *X* 轴的纵向位置。

**初始位置 [X, Y, Z]** 参数的 *X* 值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **X** 指定多个位置，请先在 MATLAB 中定义 *X* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **X**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### **Yaw** — 行人偏航姿态角 标量

行人沿场景 *Z* 轴的偏航姿态角。

**初始旋转 [Roll, Pitch, Yaw]** 参数的偏航值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **Yaw** 指定多个姿态角，请先在 MATLAB 中定义偏航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Yaw**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### 输出

### **Location** — 行人的位置 实数值 1-by-3 向量

行人在场景中的 (*X*, *Y*, *Z*) 位置，以实数值 1-by-3 向量形式返回。此位置基于行人原点，该原点位于地面上，处于行人的几何中心。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **输出位置和方向**。

**数据类型：** `double`

### **Orientation** — 行人的姿态 实数值 1-by-3 向量

行人分别绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚姿态角，以实数值 1-by-3 向量形式返回。此姿态基于行人原点，该原点位于地面上，处于行人的几何中心。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **输出位置和方向**。

**数据类型：** `double`

## 参数

### 行人参数

### **类型** — 行人类型 `Male 1` (default) | `Male 2` | `Male 3` | `Female 1` | `Female 2` | `Female 3` | `Child`

行人类型，指定为以下选项之一：

- `Male 1`
- `Male 2`
- `Male 3`
- `Female 1`
- `Female 2`
- `Female 3`
- `Child`

### **缩放** — 行人的缩放因子 `[1, 1, 1]` (default) | 实数值 1-by-3 向量

行人沿 *X* 轴、*Y* 轴和 *Z* 轴的缩放因子。

### **坐标系** — 用于 actor 变换的坐标系 `ISO8855` (default) | `Default` | `MATLAB` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定 actor 在 3D 环境中用于平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `MATLAB`

### **初始位置 [X, Y, Z]** — 行人初始位置 `[0, 0, 0]` (default) | 实数值 1-by-3 向量

行人沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时 **X** 和 **Y** 输入端口的值匹配。

### **初始偏航角** — 行人旋转的初始角度 `0` (default) | 实数值标量

行人旋转的初始偏航角。

将此参数的偏航值设置为与仿真开始时 **Yaw** 输入端口的值匹配。

### **名称** — 行人名称 `SimulinkPedestrian1` (default) | 行人名称

行人名称。默认情况下，当您在模型中使用该模块时，该模块会将 **名称** 参数设置为 `SimulinkPedestrianX`。`X` 的值取决于模型中 Simulation 3D Pedestrian 模块的数量。

行人名称会作为选择项出现在与行人同一模型中的任何 Simulation 3D 传感器模块的 **父级名称** 参数中。使用 **父级名称** 参数，您可以选择要在其上安装传感器的行人。

### **采样时间** — 采样时间 `-1` (default) | 正标量

采样时间 *Ts*，以秒为单位。图形帧速率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### 真值

### **输出位置和方向** — 输出行人的位置和方向 `off` (default) | `on`

选择此参数以分别在 **Location** 和 **Orientation** 端口输出行人的位置和方向。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：设置坐标系参数

设置 Simulation 3D Pedestrian 模块中的 **坐标系** 参数，以表示 3D 环境中 actor 变换的坐标系。

## 描述

在 3D 环境中实现行人

Simulation 3D Pedestrian 模块在 3D 仿真环境中实现行人。该模块使用行人的输入 (*X*, *Y*) 位置和偏航角来调整高程、横滚角和俯仰角，从而使行人遵循地面地形。该模块确定行人的速度和朝向，并相应地调整运动为 idle、walk 或 run。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Pedestrian 模块的 **采样时间** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块的 **坐标系** 参数指定 actor 变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。
