---
type: simulink-block
title: 'Multi-Instance Guidance Model'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'multiinstanceguidancemodel'
documentation_source_path: 'ref/multiinstanceguidancemodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Multi-Instance Guidance Model

## 端口

### 输入

### **Control** — 控制输入总线

UAV 的控制输入，指定为总线。将总线的每个元素指定为 1×*N* 向量，其中 *N* 是您要仿真的 UAV 数量。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则必须指定包含以下元素的总线：

- `Roll` — 每个 UAV 的滚转角，单位为弧度。
- `Pitch` — 每个 UAV 的俯仰角，单位为弧度。
- `YawRate` — 每个 UAV 的偏航角速率，单位为弧度每秒。
- `Thrust` — 每个 UAV 的垂直推力，单位为牛顿。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则必须指定包含以下元素的总线：

- `Height` — 每个 UAV 离地高度，单位为米。
- `Airspeed` — 每个 UAV 的空速，单位为米每秒。
- `RollAngle` — 每个 UAV 的滚转角，单位为弧度。

使用 **Control Bus Name** 属性指定控制输入总线的名称。

### **Environment** — 环境输入总线

环境输入，指定为总线。将总线的每个元素指定为 1×*N* 向量，其中 *N* 是您要仿真的 UAV 数量。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则必须指定包含 `Gravity` 元素的总线，该元素包含每个 UAV 在惯性坐标系 z 轴方向上的重力加速度，单位为米每二次方秒。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则必须指定包含以下元素的总线：

- `WindNorth` — 每个 UAV 在北方向上的风速，单位为米每秒。
- `WindEast` — 每个 UAV 在东方向上的风速，单位为米每秒。
- `WindDown` — 每个 UAV 在向下方向上的风速，单位为米每秒。
- `Gravity` — 每个 UAV 在惯性坐标系 z 轴方向上的重力加速度，单位为米每二次方秒。

使用 **Environment Bus Name** 属性指定环境输入总线的名称。

**数据类型：** `bus`
### 输出

### **State** — 仿真的无人机状态总线

仿真的无人机状态，以总线形式返回。总线中的每个元素都是一个矩阵或向量，具有 *N* 列，其中 *N* 是您仿真的无人机数量。

如果您将 **Model Type** 属性设置为 `MultirotorGuidance`，该模块将状态输出作为包含以下元素的八元素总线返回：

- `<WorldPosition>` — 无人机位置的 3×*N* 矩阵。矩阵的每一列包含一架无人机的 *xyz* 位置，单位为米。
- `<WorldVelocity>` — 无人机速度的 3×*N* 矩阵。矩阵的每一列包含一架无人机的 *xyz* 速度，单位为米每秒。
- `<EulerZYX>` — 无人机欧拉角的 3×*N* 矩阵。矩阵的每一列包含一架无人机在 *z-*、*y-*、*x-* 轴（偏航-俯仰-滚转）旋转序列下的欧拉角。
- `<BodyAngularRateRPY>` — 无人机角速率的 3×*N* 矩阵。矩阵的每一列包含一架无人机相对于 *x-*、*y-* 和 *z-* 轴的角速率（分别为滚转速率、俯仰速率和偏航速率），单位为弧度每秒。
- `<Thrust>` — 无人机推力的 1×*N* 向量。向量的每个元素包含一架无人机的推力，单位为牛顿。

如果您将 **Model Type** 属性设置为 `FixedWingGuidance`，该模块将状态输出作为包含八个元素的总线返回，其中每个元素都是一个 1×*N* 向量。该总线包含以下元素：

- `<North>` — 每架无人机在北向的位置，单位为米。
- `<East>` — 每架无人机在东向的位置，单位为米。
- `<Height>` — 每架无人机离地高度，单位为米。
- `<AirSpeed>` — 每架无人机相对于风的空速，单位为米每秒。
- `<HeadingAngle>` — 每架无人机地速与北向之间的夹角，单位为弧度。
- `<FlightPathAngle>` — 每架无人机地速与东北平面之间的夹角，单位为弧度。
- `<RollAngle>` — 每架无人机沿机体 *x* 轴的旋转角度，单位为弧度每秒。
- `<RollAngleRate>` — 每架无人机沿机体 *x* 轴的旋转角速度，单位为弧度每秒。

使用 **State Bus Name** 属性指定状态输出总线的名称。

**Data Types:** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Model Type** — 无人机制导模型类型 `MultirotorGuidance`（默认）| `FixedWingGuidance`

所有无人机的制导模型类型。选择 `MultirotorGuidance` 以仿真多旋翼无人机，或选择 `FixedWingGuidance` 以仿真固定翼无人机。

### **Number of Instances** — 要仿真的无人机数量 `5`（默认）| 正整数

将要仿真的无人机数量指定为正整数。

### **Data Type** — 输入和输出数值数据类型 `double`（默认）| `single`

将输入和输出数值数据类型指定为 `double` 或 `single`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

### **Initial State** — 初始 UAV 状态选项卡多个表条目

初始 UAV 状态选项卡，指定为多个表条目。在所有初始状态描述中，*N* 是您正在仿真的 UAV 数量。

对于多旋翼 UAV，您必须指定以下初始状态：

- **World Position** — 3×*N* 矩阵。将矩阵的每一列指定为一架 UAV 的初始 *xyz* 位置，单位为米。每架 UAV 的默认值为 `[0;0;0]`。
- **World Velocity** — 3×*N*。将矩阵的每一列指定为一架 UAV 的初始 *xyz* 速度，单位为米每秒。每架 UAV 的默认值为 `[0;0;0]`。
- **Euler Angles (ZYX)** — 3×*N* 矩阵。将矩阵的每一列指定为一架 UAV 的初始 Euler 角，采用 *z-*、*y-*、*x-* 轴（yaw-pitch-roll）旋转顺序。每架 UAV 的默认值为 `[0;0;0]`。
- **Body Angular Rates** — 3×*N* 矩阵。将矩阵的每一列指定为一架 UAV 相对于 *x-*、*y-* 和 *z-* 轴的初始角速率（分别为 roll rate、pitch rate 和 yaw rate），单位为弧度每秒。每架 UAV 的默认值为 `[0;0;0]`。
- **Thrust** — 1×*N* 向量。将向量的每个元素指定为一架 UAV 的初始推力，单位为牛顿。每架 UAV 的默认值为 `0`。

对于固定翼 UAV，您必须将这些初始状态指定为 1×*N* 向量：

- **North Position** — 每架 UAV 在北方向上的初始位置，单位为米。每架 UAV 的默认值为 `0`。
- **East Position** — 每架 UAV 在东方向上的初始位置，单位为米。每架 UAV 的默认值为 `0`。
- **Height** — 每架 UAV 的初始离地高度，单位为米。每架 UAV 的默认值为 `0`。
- **Air Speed** — 每架 UAV 相对于风的初始速度，单位为米每秒。每架 UAV 的默认值为 `0`。
- **Heading Angle** — 每架 UAV 的地速与北方向之间的初始角度，单位为弧度。每架 UAV 的默认值为 `0`。
- **Flight Path Angle** — 每架 UAV 的地速与东北平面之间的初始角度，单位为弧度。每架 UAV 的默认值为 `0`。
- **Roll Angle** — 每架 UAV 沿机体 *x* 轴的初始旋转角度，单位为弧度每秒。每架 UAV 的默认值为 `0`。
- **Roll Angle Rate** — 每架 UAV 沿机体 *x* 轴的初始旋转角速度，单位为弧度每秒。每架 UAV 的默认值为 `0`。

**Tunable:** No

### **Configuration** — UAV 控制器配置选项卡多个表项

UAV 控制器配置选项卡，指定为多个表项。在所有控制器配置描述中，*N* 是您正在仿真的 UAV 数量。

对于多旋翼 UAV，指定以下参数：

- **PD Roll** — *N*×2 矩阵。将矩阵的每一行指定为 UAV 的滚转角控制器的比例和微分增益。每个 UAV 的默认值为 `[3402.97
  116.67]`。
- **PD Pitch** — *N*×2 矩阵。将矩阵的每一行指定为 UAV 的俯仰角控制器的比例和微分增益。每个 UAV 的默认值为 `[3402.97
  116.67]`。
- **P YawRate** — *N*×1 向量。将向量的每个元素指定为 UAV 的偏航角速率控制器的比例增益。每个 UAV 的默认值为 `1950`。
- **P Thrust** — *N*×1 向量。将向量的每一行指定为 UAV 的推力控制器的比例增益。每个 UAV 的默认值为 `3900`。
- **Mass** — *N*×1 向量。将向量的每个元素指定为 UAV 的质量，单位为 Kg。每个 UAV 的默认值为 `0.1`。

对于固定翼 UAV，指定以下参数：

- **P Height** — *N*×1 向量。将向量的每个元素指定为 UAV 的高度控制器的比例增益。每个 UAV 的默认值为 `3.9`。
- **P Flight Path Angle** — *N*×1 向量。将向量的每个元素指定为 UAV 的飞行航迹角控制器的比例增益。每个 UAV 的默认值为 `39`。
- **PD Roll** — *N*×2 矩阵。将矩阵的每个元素指定为 UAV 的俯仰角控制器的比例和微分增益。每个 UAV 的默认值为 `[3402.97
  116.67]`。
- **P Air Speed** — *N*×1 向量。将向量的每个元素指定为 UAV 的空速控制器的比例增益。每个 UAV 的默认值为 `1`。
- **Min/Max Flight Path Angle** — *N*×2 矩阵。将矩阵的每个元素指定为 UAV 的最小和最大飞行航迹角，单位为弧度。每个 UAV 的默认值为 `[-pi/2
  pi/2]`

### **Input/Output Bus Names** — Simulink 总线信号名称选项卡总线名称

此选项卡包含 **State Bus Name**、**Control Bus Name** 和 **Environment Bus Name** 参数，分别指定输出状态总线、输入控制总线和输入环境总线的名称。每个总线都有一个基于 UAV 模型和输入类型的默认名称。

| 模型类型参数 | 默认状态总线名称 | 默认控制总线名称 | 默认环境总线名称 |
| --- | --- | --- | --- |
| `FixedWingGuidance` | `FixedWingGuidanceStateBus` | `FixedWingGuidanceControlBus` | `FixedWingGuidanceEnvironmentBus` |
| `MultirotorGuidance` | `MultirotorGuidanceStateBus` | `MultirotorGuidanceControlBus` | `MultirotorGuidanceEnvironmentBus` |

要在同一个 Simulink 模型中使用多个制导模型，请为每个 Multi-Instance Guidance Model 模块指定彼此不相交的总线名称。

## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

多个 UAV 的降阶模型

Multi-Instance Guidance Model 模块通过使用降阶固定翼 [1] 或多旋翼 [2] 运动学模型和自动驾驶仪控制器来仿真多个小型 UAV。
