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

### **Actor** — 世界坐标中的长方体参与者位姿，包含 MATLAB® structure 的 Simulink® bus

世界坐标中的长方体参与者位姿，指定为包含 MATLAB structure 的 Simulink bus。

要获取此 structure 输入，请使用 Scenario Reader 模块从场景中读取参与者。默认情况下，Scenario Reader 模块以自车坐标输出参与者。要将这些位姿从自车坐标转换为世界坐标，请使用 Vehicle To World 模块。

此 bus 中的 structure 可以包含单个参与者位姿或多个参与者位姿。

#### 单一位姿 Structure

要指定单个参与者位姿，该 structure 必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位为 meters。  **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位为 meters。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度（*v*），指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位为 degrees。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度（*ω*），指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位为 degrees per second。 |

#### 多个位姿 Structure

要指定多个参与者位姿，该 structure 必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | 参与者位姿 | `NumActors`-length array of actor pose structures |

`Actors` 中的每个 actor pose structure 必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位为 meters。  **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位为 meters。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度（*v*），指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位为 degrees。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度（*ω*），指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位为 degrees per second。 |

该模块仅转换 `Actors` 数组中的一个位姿。要指定转换哪个位姿，请选择 **Specify Actor ID**，然后使用 **ActorID used for conversion** 参数指定参与者的 `ActorID`。

### 输出

### **X** — 3D 仿真坐标中参与者的纵向位置 numeric scalar

3D 仿真坐标中参与者的纵向位置，以 numeric scalar 形式返回。单位为 meters。

在此坐标系中，当沿 *X* 轴正方向观察时，正 *Y* 轴指向左侧，*Z* 轴指向上方。

要在 3D 仿真环境中指定车辆的 *X* 位置，请将此端口连接到 Simulation 3D Vehicle with Ground Following 模块的 **X** 输入端口。

### **Y** — 3D 仿真坐标中参与者的横向位置 numeric scalar

3D 仿真坐标中参与者的横向位置，以 numeric scalar 形式返回。单位为 meters。

在此坐标系中，当沿 *X* 轴正方向观察时，正 *Y* 轴指向左侧，*Z* 轴指向上方。

要在 3D 仿真环境中指定车辆的 *Y* 位置，请将此端口连接到 Simulation 3D Vehicle with Ground Following 模块的 **Y** 输入端口。

### **Yaw** — 3D 仿真坐标中参与者的偏航姿态角 numeric scalar

3D 仿真坐标中参与者绕 *Z* 轴的偏航姿态角，以 numeric scalar 形式返回。单位为 degrees。

在此坐标系中，当沿 *Z* 轴正方向观察时，偏航角以顺时针为正。然而，如果从 2D 俯视视角查看仿真，则偏航角以逆时针为正，因为你是沿负 *Z* 轴查看场景。

要在 3D 仿真环境中指定车辆的偏航姿态角，请将此端口连接到 Simulation 3D Vehicle with Ground Following 模块的 **Yaw** 输入端口。

## 参数

### **Specify Actor ID** — 启用长方体参与者的 ID 指定 `off`（默认）| `on`

选择此参数可启用 **ActorID used for conversion** 参数，你可以在其中指定要转换为 3D 仿真坐标的长方体参与者位姿的 `ActorID`。

如果清除此参数，则该模块转换输入 **Actor** 总线中的第一个参与者位姿。

### **ActorID used for conversion** — 长方体参与者的 `ActorID` 值 `1`（默认）| positive integer

要转换为 3D 仿真坐标的长方体参与者的 `ActorID` 值，指定为 positive integer。此参数必须是输入 **Actor** 总线中的有效 `ActorID`。

#### 依赖项

要启用此参数，请选择 **Specify Actor ID**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，你可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，C 代码会在后续仿真中重用。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

将参与者从长方体坐标转换为 3D 仿真坐标

Cuboid To 3D Simulation 模块将世界坐标中的长方体参与者位姿转换为 Simulation 3D Vehicle with Ground Following 模块使用的 **X**、**Y** 和 **Yaw** 坐标。使用转换后的值可在 3D 仿真环境中为使用 Driving Scenario Designer app 创建的参与者设置车辆位置。场景的地面地形决定车辆的横滚（*x* 轴旋转）、俯仰（*y* 轴旋转）和高程（*z* 轴位置）。

你可以指定包含单个参与者位姿或多个参与者位姿的总线。默认情况下，该模块转换总线中第一个参与者的位姿。要指定要转换其位姿的参与者，请指定该参与者的 `ActorID`。

在长方体驾驶场景和 3D 仿真驾驶场景中，坐标系相同，但车辆的原点不同。在长方体驾驶场景中，车辆原点位于地面上，在后轴中心下方。该模块将此原点转换为 3D 仿真环境中使用的原点，即车辆几何中心下方。下表显示两个环境之间的原点差异。你必须使用 Scenario Reader 模块读取长方体驾驶场景。

| 长方体车辆原点 | 3D 仿真车辆原点 |
| --- | --- |
| 蓝色长方体车辆，原点位于后轴中心 | 红色 3D 仿真车辆，原点位于车辆几何中心 |
