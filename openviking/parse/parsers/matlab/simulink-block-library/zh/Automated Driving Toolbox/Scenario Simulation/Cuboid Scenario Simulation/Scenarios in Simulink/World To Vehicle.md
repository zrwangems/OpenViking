---
type: simulink-block
title: 'World To Vehicle'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Cuboid Scenario Simulation / Scenarios in Simulink'
documentation_page: 'worldtovehicle'
documentation_source_path: 'ref/worldtovehicle.html'
language: zh-CN
chinese_source: worker-translation
---

# World To Vehicle

## 端口

### 输入

### **Actors** — 世界坐标中的参与者位姿，包含 MATLAB® structure 的 Simulink® bus

世界坐标中的参与者位姿，指定为包含 MATLAB structure 的 Simulink bus。

该 structure 必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | 参与者位姿 | `NumActors`-length array of actor pose structures |

`Actors` 中的每个 actor pose structure 必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位为 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位为 meters。 |
| `Velocity` | 参与者的速度 (*v*)，在 *x*-、*y*- 和 *z*-方向，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位为 degrees。 |
| `AngularVelocity` | 参与者的角速度 (*ω*)，在 *x*-、*y*- 和 *z*-方向，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位为 degrees per second。 |

### **Ego Vehicle** — 自车姿态，包含 MATLAB structure 的 Simulink bus

自车姿态，指定为包含 MATLAB structure 的 Simulink bus。

该 structure 必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位为 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位为 meters。 |
| `Velocity` | 参与者的速度 (*v*)，在 *x*-、*y*- 和 *z*-方向，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位为 degrees。 |
| `AngularVelocity` | 参与者的角速度 (*ω*)，在 *x*-、*y*- 和 *z*-方向，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位为 degrees per second。 |

### 输出

### **Actors** — 车辆坐标中的参与者位姿，包含 MATLAB structure 的 Simulink bus

车辆坐标中的参与者位姿，返回为包含 MATLAB structure 的 Simulink bus。

该 structure 具有以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | 参与者位姿 | `NumActors`-length array of actor pose structures |

`Actors` 中的每个 actor pose structure 具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的 three-element row vector。单位为 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位为 meters。 |
| `Velocity` | 参与者的速度 (*v*)，在 *x*-、*y*- 和 *z*-方向，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位为 degrees。 |
| `AngularVelocity` | 参与者的角速度 (*ω*)，在 *x*-、*y*- 和 *z*-方向，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位为 degrees per second。 |

## 参数

### **Source of actors bus name** — Actor 位姿总线的名称来源 `Auto` (default) | `Property`

**Actors** 输出端口中返回的参与者位姿总线的名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建参与者位姿总线名称。
- `Property` — 使用 **Actors bus name** 参数指定参与者位姿总线名称。

### **Actors bus name** — Actor 位姿总线的名称 valid bus name

**Actors** 输出端口中返回的参与者位姿总线的名称，指定为 valid bus name。

#### 依赖项

要启用此参数，请将 **Source of actors bus name** 设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C/C++ 代码。只要模型不变，后续仿真将重用 C 代码。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

将参与者从世界坐标转换为自车坐标

World To Vehicle 模块将参与者位姿从世界坐标转换为输入自车的车辆坐标。
