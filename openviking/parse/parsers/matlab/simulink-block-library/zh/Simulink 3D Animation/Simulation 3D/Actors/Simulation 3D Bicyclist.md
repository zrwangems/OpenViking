---
type: simulink-block
title: 'Simulation 3D Bicyclist'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Actors'
documentation_page: 'simulation3dbicyclist'
documentation_source_path: 'simulation3dbicyclist.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Bicyclist

## 端口

### 输入

### **Y** — 骑车人的横向位置 标量

骑车人沿场景 *Y* 轴的横向位置。

**Initial position [X, Y, Z]** 参数的 *Y* 值必须与仿真开始时此端口的值匹配。

要沿整条骑车人路径在端口 **Y** 指定多个位置，请先在 MATLAB® 中定义 *Y* 航点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些航点馈送到 **Y**。要了解如何选择和指定航点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### **X** — 骑车人的纵向位置 标量

骑车人沿场景 *X* 轴的纵向位置。

**Initial position [X, Y, Z]** 参数的 *X* 值必须与仿真开始时此端口的值匹配。

要沿整条骑车人路径在端口 **X** 指定多个位置，请先在 MATLAB 中定义 *X* 航点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些航点馈送到 **X**。要了解如何选择和指定航点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### **Yaw** — 骑车人的偏航方向角 标量

骑车人沿场景 *Z* 轴的偏航方向角。

**Initial rotation [Roll, Pitch, Yaw]** 参数的偏航值必须与仿真开始时此端口的值匹配。

要沿整条骑车人路径在端口 **Yaw** 指定多个方向角，请先在 MATLAB 中定义偏航航点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些航点馈送到 **Yaw**。要了解如何选择和指定航点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### 输出

### **Location** — 骑车人的位置 实值 1×3 向量

骑车人在场景中的 (*X*, *Y*, *Z*) 位置，以实值 1×3 向量形式返回。此位置基于骑车人原点，该原点位于地面上，处于骑车人的几何中心。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

### **Orientation** — 骑车人的方向 实值 1×3 向量

骑车人分别绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚方向角，以实值 1×3 向量形式返回。此方向基于骑车人原点，该原点位于地面上，处于骑车人的几何中心。

#### 依赖关系

要启用此端口，请在 **真值** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

## 参数

### 骑车人参数

### **Scale** — 骑车人的缩放因子 `[1, 1, 1]`（默认）| 实值 1×3 向量

骑车人沿 *X* 轴、*Y* 轴和 *Z* 轴的缩放因子。

### **Coordinate system** — 用于角色变换的坐标系 `ISO8855`（默认）| `Default` | `MATLAB` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定角色在 3D 环境中用于平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `MATLAB`

### **Initial position [X, Y, Z]** — 骑车人的初始位置 `[0, 0, 0]`（默认）| 实值 1×3 向量

骑车人沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时 **X** 和 **Y** 输入端口的值匹配。

### **Initial rotation [Roll, Pitch, Yaw]** — 骑车人旋转的初始角度 `[0, 0, 0]`（默认）| 实值 1×3 向量

骑车人旋转的初始角度。旋转角度由骑车人的横滚、俯仰和偏航定义。

将此参数的偏航值设置为与仿真开始时 **Yaw** 输入端口的值匹配。

### **Name** — 骑车人的名称 `SimulinkBicyclist1`（默认）| 骑车人名称

骑车人的名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为 `SimulinkBicyclistX`。`X` 的值取决于模型中 Simulation 3D Bicyclist 模块的数量。

骑车人名称会作为同一模型中任何 Simulation 3D 传感器模块的 **Parent name** 参数中的一个选项出现。使用 **Parent name** 参数，您可以选择要在哪个骑车人上安装传感器。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

采样时间，*Ts*，单位为 seconds。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，该模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### 真值

### **Output location and orientation** — 行人的输出位置和方向 `off`（默认）| `on`

选择此参数可在 **Location** 和 **Orientation** 端口分别输出行人的位置和方向。

## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：设置 Coordinate system 参数

在 Simulation 3D Bicyclist 模块中设置 **Coordinate system** 参数，以表示 3D 环境中角色变换的坐标系。

## 描述

在 3D 环境中实现骑车人

Simulation 3D Bicyclist 模块在 3D 仿真环境中实现骑车人。该模块使用骑车人的输入 (*X*, *Y*) 位置和偏航角来调整高程、横滚角和俯仰角，以使骑车人跟随地面地形。该模块确定骑车人的速度和朝向，并相应地将运动调整为 idle、pedaling 或 braking。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Pedestrian 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块的 **Coordinate system** 参数指定角色变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。
