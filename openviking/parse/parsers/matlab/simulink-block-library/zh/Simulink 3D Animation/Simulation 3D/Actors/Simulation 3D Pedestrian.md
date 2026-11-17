---
type: simulink-block
title: 'Simulation 3D Pedestrian'
family: 'sl3d'
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
```yaml
ports:
- name: Y
  summary: 行人的横向位置 标量
  direction: input
- name: X
  summary: 行人的纵向位置 标量
  direction: input
- name: Yaw
  summary: 行人的偏航方向角 标量
  direction: input
- name: Location
  summary: 行人的位置 实数值 1×3 向量
  direction: output
  data_types: double
- name: Orientation
  summary: 行人的方向 实数值 1×3 向量
  direction: output
  data_types: double
```

### 输入

### **Y** — 行人的横向位置 标量

行人沿场景 *Y* 轴的横向位置。

**Initial position [X, Y, Z]** 参数的 *Y* 值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **Y** 指定多个位置，请先在 MATLAB® 中定义 *Y* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Y**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### **X** — 行人的纵向位置 标量

行人沿场景 *X* 轴的纵向位置。

**Initial position [X, Y, Z]** 参数的 *X* 值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **X** 指定多个位置，请先在 MATLAB 中定义 *X* 路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **X**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。

### **Yaw** — 行人的偏航方向角 标量

行人沿场景 *Z* 轴的偏航方向角。

**Initial rotation [Roll, Pitch, Yaw]** 参数的偏航值必须与仿真开始时此端口的值匹配。

要沿整条行人路径在端口 **Yaw** 指定多个方向角，请先在 MATLAB 中定义偏航路点的时间序列。然后，使用 From Workspace (Simulink) 模块将这些路点馈送到 **Yaw**。要了解如何选择和指定路点，请参阅 Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) 示例。
### 输出

### **Location** — 行人的位置 实数值 1×3 向量

行人在场景中的 (*X*, *Y*, *Z*) 位置，以实数值 1×3 向量形式返回。此位置基于行人原点，该原点位于地面上，处于行人的几何中心。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`

### **Orientation** — 行人的方向 实数值 1×3 向量

行人分别绕场景 *Z* 轴、*Y* 轴和 *X* 轴的偏航、俯仰和横滚方向角，以实数值 1×3 向量形式返回。此方向基于行人原点，该原点位于地面上，处于行人的几何中心。

#### 依赖关系

要启用此端口，请在 **Ground Truth** 选项卡上选择 **Output location and orientation**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Type
  summary: 行人类型 Male 1（默认）| Male 2 | Male 3 | Female 1 | Female 2 | Female 3 | Child
  group: 行人参数
- name: Scale
  summary: 行人的缩放因子 [1, 1, 1]（默认）| 实数值 1×3 向量
  group: 行人参数
- name: Coordinate system
  summary: 用于 actor 变换的坐标系 ISO8855（默认）| Default | MATLAB | AERO | VRML | SAE
  group: 行人参数
- name: Initial position [X, Y, Z]
  summary: 初始行人位置 [0, 0, 0]（默认）| 实值 1×3 向量
  group: 行人参数
- name: Initial yaw
  summary: 行人旋转的初始角度 0（默认）| 实值标量
  group: 行人参数
- name: Name
  summary: 行人名称 SimulinkPedestrian1（默认）| 行人名称
  group: 行人参数
- name: Sample time
  summary: 采样时间 -1（默认）| 正标量
  group: 行人参数
- name: Output location and orientation
  summary: 输出行人的位置和方向 off（默认）| on
  group: Ground Truth
```

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

### **Coordinate system** — 用于 actor 变换的坐标系 `ISO8855`（默认）| `Default` | `MATLAB` | `AERO` | `VRML` | `SAE`

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

### **Initial position [X, Y, Z]** — 初始行人位置 `[0, 0, 0]`（默认）| 实值 1×3 向量

行人沿场景 *X* 轴、*Y* 轴和 *Z* 轴的初始位置。

将此参数的 *X* 和 *Y* 值设置为与仿真开始时的 **X** 和 **Y* 输入端口值匹配。

### **Initial yaw** — 行人旋转的初始角度 `0`（默认）| 实值标量

行人旋转的初始偏航角。

将此参数的偏航值设置为与仿真开始时的 **Yaw** 输入端口值匹配。

### **Name** — 行人名称 `SimulinkPedestrian1`（默认）| 行人名称

行人名称。默认情况下，当您在模型中使用该模块时，模块将 **Name** 参数设置为 `SimulinkPedestrianX`。`X` 的值取决于模型中 Simulation 3D Pedestrian 模块的数量。

行人名称会作为与行人在同一模型中的任何 Simulation 3D 传感器模块的 **Parent name** 参数中的一个选项出现。通过 **Parent name** 参数，您可以选择要安装传感器的行人。

### **Sample time** — 采样时间 `-1`（默认）| 正标量

采样时间，*Ts*，以秒为单位。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，模块将使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

### Ground Truth

### **Output location and orientation** — 输出行人的位置和方向 `off`（默认）| `on`

选择此参数以分别在 **Location** 和 **Orientation** 端口输出行人的位置和方向。
## 所属库

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a: 设置坐标系参数

在 Simulation 3D Pedestrian 模块中设置 **Coordinate system** 参数，以表示 3D 环境中参与者变换的坐标系。

## 描述

在 3D 环境中实现行人

Simulation 3D Pedestrian 模块在 3D 仿真环境中实现一个行人。该模块使用行人的输入 (*X*, *Y*) 位置和偏航角来调整仰角、横滚角和俯仰角，使行人跟随地面地形。该模块确定行人的速度和朝向，并相应地调整运动为 idle、walk 或 run。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Pedestrian 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块的 **Coordinate system** 参数指定参与者变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。
