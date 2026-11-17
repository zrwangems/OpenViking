---
type: simulink-block
title: 'Cuboid To 3D Simulation'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'cuboidto3dsimulation'
documentation_source_path: 'ref/cuboidto3dsimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# Cuboid To 3D Simulation

## 端口

### 输入

### **Actor** — 世界坐标系中的长方体 actor 位姿 包含 MATLAB® 结构的 Simulink® 总线

世界坐标系中的长方体 actor 位姿，指定为包含 MATLAB 结构的 Simulink 总线。

要获取此结构体输入，请使用 Scenario Reader 模块从场景中读取 actor。默认情况下，Scenario Reader 模块以自车坐标系输出 actor。要将这些位姿从自车坐标转换为世界坐标，请使用 Vehicle To World 模块。

此总线中的结构体可以包含单个 actor 位姿或多个 actor 位姿。

#### 单一位姿结构体

要指定单个 actor 位姿，结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的 actor 标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | actor 的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | actor 在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | actor 的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | actor 的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | actor 的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | actor 在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

#### 多个位姿结构体

要指定多个 actor 位姿，结构体必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | actor 数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | actor 位姿 | 长度为 `NumActors` 的 actor 位姿结构体数组 |

`Actors` 中的每个 actor 位姿结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的 actor 标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | actor 的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | actor 在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | actor 的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | actor 的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | actor 的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | actor 在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

该模块仅转换 `Actors` 数组中的一个位姿。要指定要转换的位姿，请选择 **Specify Actor ID**，然后使用 **ActorID used for conversion** 参数指定 actor 的 `ActorID`。
### 输出

### **X** — 3D 仿真坐标中 actor 的纵向位置 数值标量

3D 仿真坐标中 actor 的纵向位置，返回为数值标量。单位为米。

在此坐标系中，当沿 *X* 轴正方向观察时，*Y* 轴正方向指向左侧，*Z* 轴指向上方。

要在 3D 仿真环境中指定车辆的 *X* 位置，请将此端口连接到 Simulation 3D Vehicle with Ground Following 模块的 **X** 输入端口。

### **Y** — 3D 仿真坐标中 actor 的横向位置 数值标量

3D 仿真坐标中 actor 的横向位置，返回为数值标量。单位为米。

在此坐标系中，当沿 *X* 轴正方向观察时，*Y* 轴正方向指向左侧，*Z* 轴指向上方。

要在 3D 仿真环境中指定车辆的 *Y* 位置，请将此端口连接到 Simulation 3D Vehicle with Ground Following 模块的 **Y** 输入端口。

### **Yaw** — 3D 仿真坐标中 actor 的偏航方向角 数值标量

3D 仿真坐标中 actor 绕 *Z* 轴的偏航方向角，返回为数值标量。单位为度。

在此坐标系中，当沿 *Z* 轴正方向观察时，偏航为顺时针正方向。但是，如果从 2D 俯视视角查看仿真，则偏航为逆时针正方向，因为您是沿 *Z* 轴负方向观察场景的。

要在 3D 仿真环境中指定车辆的偏航方向角，请将此端口连接到 Simulation 3D Vehicle with Ground Following 模块的 **Yaw** 输入端口。

## 参数

### **Specify Actor ID** — 启用长方体 actor 的 ID 指定 `off`（默认）| `on`

选择此参数以启用 **ActorID used for conversion** 参数，您可以在其中指定要转换为 3D 仿真坐标的长方体 actor 位姿的 `ActorID`。

如果清除此参数，则该模块转换输入 **Actor** 总线中的第一个 actor 位姿。

### **ActorID used for conversion** — 长方体 actor 的 `ActorID` 值 `1`（默认）| 正整数

要转换为 3D 仿真坐标的长方体 actor 的 `ActorID` 值，指定为正整数。此参数必须是输入 **Actor** 总线中的有效 `ActorID`。

#### 依赖关系

要启用此参数，请选择 **Specify Actor ID**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不更改，C 代码就会在后续仿真中重复使用。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

将 actor 从长方体坐标转换为 3D 仿真坐标

Cuboid To 3D Simulation 模块将世界坐标系中的长方体 actor 位姿转换为 Simulation 3D Vehicle with Ground Following 模块所使用的 **X**、**Y** 和 **Yaw** 坐标。使用转换后的值为 Driving Scenario Designer 应用程序创建的 actor 设置 3D 仿真环境中的车辆位置。场景的地形决定了车辆的横滚（*x* 轴旋转）、俯仰（*y* 轴旋转）和高程（*z* 轴位置）。

您可以指定包含单个 actor 位姿或多个 actor 位姿的总线。默认情况下，该模块转换总线中第一个 actor 的位姿。要指定要转换其位姿的 actor，请指定该 actor 的 `ActorID`。

在长方体和 3D 仿真驾驶场景中，坐标系相同，但车辆原点不同。在长方体驾驶场景中，车辆原点位于地面上后轴中心下方。该模块将此原点转换为 3D 仿真环境中使用的原点，即车辆几何中心下方。下表显示了两种环境之间的原点差异。您必须使用 Scenario Reader 模块读取长方体驾驶场景。

| 长方体车辆原点 | 3D 仿真车辆原点 |
| --- | --- |
| 蓝色长方体车辆，原点位于后轴中心 | 红色 3D 仿真车辆，原点位于车辆几何中心 |
