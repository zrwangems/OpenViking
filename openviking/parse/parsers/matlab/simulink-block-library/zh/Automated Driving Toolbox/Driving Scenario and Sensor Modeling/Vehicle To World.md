---
type: simulink-block
title: 'Vehicle To World'
family: 'driving'
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
```yaml
ports:
- name: Actors
  summary: 车辆坐标系中的参与者位姿 包含 MATLAB 结构的 Simulink® 总线
  direction: input
- name: Ego Vehicle
  summary: 自车位姿 包含 MATLAB 结构的 Simulink 总线
  direction: input
- name: Actors
  summary: 世界坐标系中的参与者位姿 包含 MATLAB 结构的 Simulink 总线
  direction: output
```

### 输入

### **Actors** — 车辆坐标系中的参与者位姿 包含 MATLAB 结构的 Simulink® 总线

车辆坐标系中的参与者位姿，指定为包含 MATLAB 结构的 Simulink 总线。

该结构必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | 参与者位姿 | 长度为 `NumActors` 的参与者位姿结构数组 |

`Actors` 中的每个参与者位姿结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

### **Ego Vehicle** — 自车位姿 包含 MATLAB 结构的 Simulink 总线

自车位姿，指定为包含 MATLAB 结构的 Simulink 总线。

该结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |
### 输出

### **Actors** — 世界坐标系中的参与者位姿 包含 MATLAB 结构的 Simulink 总线

世界坐标系中的参与者位姿，返回为包含 MATLAB 结构的 Simulink 总线。

该结构具有以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | 参与者位姿 | 长度为 `NumActors` 的参与者位姿结构数组 |

`Actors` 中的每个参与者位姿结构具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |
## 参数
```yaml
parameters:
- name: Source of actors bus name
  summary: 参与者位姿总线名称的来源 Auto（默认） | Property
  group: ''
- name: Actors bus name
  summary: 参与者位姿总线名称 有效总线名称
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认） | Code generation
  group: ''
```

### **Source of actors bus name** — 参与者位姿总线名称的来源 `Auto`（默认） | `Property`

**Actors** 输出端口返回的参与者位姿总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建参与者位姿总线名称。
- `Property` — 使用 **Actors bus name** 参数指定参与者位姿总线名称。

### **Actors bus name** — 参与者位姿总线名称 有效总线名称

**Actors** 输出端口返回的参与者位姿总线名称，指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **Source of actors bus name** 设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C/C++ 代码。只要模型不发生变化，C 代码将在后续仿真中重用。此选项需要额外的启动时间。
## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

将参与者从自车坐标系转换为世界坐标系

Vehicle To World 模块将参与者位姿从输入自车的车辆坐标系转换为世界坐标系。使用此模块可将 Scenario Reader 模块输出的非自车参与者位姿转换为世界坐标系，以便与 3D 仿真环境配合使用。在使用这些输出位姿指定 3D 环境中的车辆位置之前，请先使用 Cuboid To 3D Simulation 模块将它们从长方体坐标系转换为 3D 仿真世界坐标系。有关此工作流的示例，请参阅 Visualize Sensor Data from Unreal Engine Simulation Environment 示例。
