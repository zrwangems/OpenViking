---
type: simulink-block
title: 'Vehicle To World'
family: 'driving-scenario-and-sensor-modeling'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'vehicletoworld'
documentation_source_path: 'ref/vehicletoworld.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle To World

## 端口

### 输入

### **Actors** — 车辆坐标中的 actor 位姿 Simulink® bus containing MATLAB® structure

车辆坐标中的 actor 位姿，指定为包含 MATLAB structure 的 Simulink bus。

该结构体必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | actor 数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | actor 位姿 | `NumActors`-length array of actor pose structures |

`Actors` 中的每个 actor 位姿结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的 actor 标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位是 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | actor 的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | actor 在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Roll` | actor 的横滚角，指定为 real-valued scalar。单位是 degrees。 |
| `Pitch` | actor 的俯仰角，指定为 real-valued scalar。单位是 degrees。 |
| `Yaw` | actor 的偏航角，指定为 real-valued scalar。单位是 degrees。 |
| `AngularVelocity` | actor 在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |

### **Ego Vehicle** — Ego vehicle 位姿 Simulink bus containing MATLAB structure

Ego vehicle 位姿，指定为包含 MATLAB structure 的 Simulink bus。

该结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的 actor 标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位是 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | actor 的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | actor 在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Roll` | actor 的横滚角，指定为 real-valued scalar。单位是 degrees。 |
| `Pitch` | actor 的俯仰角，指定为 real-valued scalar。单位是 degrees。 |
| `Yaw` | actor 的偏航角，指定为 real-valued scalar。单位是 degrees。 |
| `AngularVelocity` | actor 在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |

### 输出

### **Actors** — 世界坐标中的 actor 位姿 Simulink bus containing MATLAB structure

世界坐标中的 actor 位姿，返回为包含 MATLAB structure 的 Simulink bus。

该结构体具有以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | actor 数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | actor 位姿 | `NumActors`-length array of actor pose structures |

`Actors` 中的每个 actor 位姿结构体具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的 actor 标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位是 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | actor 的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | actor 在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Roll` | actor 的横滚角，指定为 real-valued scalar。单位是 degrees。 |
| `Pitch` | actor 的俯仰角，指定为 real-valued scalar。单位是 degrees。 |
| `Yaw` | actor 的偏航角，指定为 real-valued scalar。单位是 degrees。 |
| `AngularVelocity` | actor 在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |

## 参数

### **Source of actors bus name** — actor 位姿 bus 名称的来源 `Auto` (default) | `Property`

**Actors** 输出端口中返回的 actor 位姿 bus 名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建 actor 位姿 bus 名称。
- `Property` — 使用 **Actors bus name** 参数指定 actor 位姿 bus 名称。

### **Actors bus name** — actor 位姿 bus 的名称 valid bus name

**Actors** 输出端口中返回的 actor 位姿 bus 的名称，指定为有效的 bus 名称。

#### 依赖关系

要启用此参数，请将 **Source of actors bus name** 设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器对模型进行仿真。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码对模型进行仿真。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

将 actors 从 ego vehicle 坐标转换为世界坐标

Vehicle To World 模块将 actor 位姿从输入 ego vehicle 的车辆坐标转换为世界坐标。使用此模块可将由 Scenario Reader 模块输出的 non-ego actor 位姿转换为世界坐标，以用于 3D 仿真环境。在使用这些输出位姿在 3D 环境中指定车辆位置之前，请先使用 Cuboid To 3D Simulation 模块将它们从 cuboid 转换为 3D 仿真世界坐标系。有关此工作流的示例，请参阅 Visualize Sensor Data from Unreal Engine Simulation Environment 示例。
