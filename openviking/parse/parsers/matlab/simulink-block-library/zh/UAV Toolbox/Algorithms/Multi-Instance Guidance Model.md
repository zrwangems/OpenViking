---
type: simulink-block
title: 'Multi-Instance Guidance Model'
family: 'algorithms'
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

UAV 的控制输入，指定为 bus。将 bus 的每个元素指定为 1-by-*N* 向量，其中 *N* 是您要仿真的 UAV 数量。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则必须指定包含以下元素的 bus：

- `Roll` — 每个 UAV 的滚转角，单位为 radians。
- `Pitch` — 每个 UAV 的俯仰角，单位为 radians。
- `YawRate` — 每个 UAV 的偏航角速率，单位为 radians per second。
- `Thrust` — 每个 UAV 的垂直推力，单位为 Newtons。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则必须指定包含以下元素的 bus：

- `Height` — 每个 UAV 离地面的高度，单位为 meters。
- `Airspeed` — 每个 UAV 的空速，单位为 meters per second。
- `RollAngle` — 每个 UAV 的滚转角，单位为 radians。

使用 **Control Bus Name** 属性指定控制输入 bus 的名称。

### **Environment** — 环境输入总线

环境输入，指定为 bus。将 bus 的每个元素指定为 1-by-*N* 向量，其中 *N* 是您要仿真的 UAV 数量。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则必须指定包含 `Gravity` 元素的 bus，该元素包含每个 UAV 在惯性坐标系 z-axis 方向上的重力加速度，单位为 meters per second squared。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则必须指定包含以下元素的 bus：

- `WindNorth` — 每个 UAV 在北向的风速，单位为 meters per second。
- `WindEast` — 每个 UAV 在东向的风速，单位为 meters per second。
- `WindDown` — 每个 UAV 在向下方向的风速，单位为 meters per second。
- `Gravity` — 每个 UAV 在惯性坐标系 z-axis 方向上的重力加速度，单位为 meters per second squared。

使用 **Environment Bus Name** 属性指定环境输入 bus 的名称。

**数据类型：** `bus`
### 输出

### **State** — 仿真的 UAV 状态总线

仿真的 UAV 状态，以 bus 形式返回。bus 中的每个元素都是具有 *N* 列的矩阵或向量，其中 *N* 是您仿真的 UAV 数量。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则该模块将状态输出作为包含八个元素的 bus 返回，这些元素为：

- `<WorldPosition>` — UAV 位置的 3-by-*N* 矩阵。矩阵的每一列包含一个 UAV 的 *xyz*-位置，单位为 meters。
- `<WorldVelocity>` — UAV 速度的 3-by-*N* 矩阵。矩阵的每一列包含一个 UAV 的 *xyz*-速度，单位为 meters per second。
- `<EulerZYX>` — UAV 欧拉角的 3-by-*N* 矩阵。矩阵的每一列包含一个 UAV 的欧拉角，采用 *z-*,*y-*,*x-*axis（yaw-pitch-roll）旋转顺序。
- `<BodyAngularRateRPY>` — UAV 角速率的 3-by-*N* 矩阵。矩阵的每一列包含一个 UAV 相对于 *x-*,*y-*, 和 *z-* axes 的角速率（分别为滚转角速率、俯仰角速率和偏航角速率），单位为 radians per second。
- `<Thrust>` — UAV 推力的 1-by-*N* 向量。向量的每个元素包含一个 UAV 的推力，单位为 newtons。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则该模块将状态输出作为包含八个元素的 bus 返回，其中每个元素都是 1-by-*N* 向量。该 bus 包含以下元素：

- `<North>` — 每个 UAV 在北向的位置，单位为 meters。
- `<East>` — 每个 UAV 在东向的位置，单位为 meters。
- `<Height>` — 每个 UAV 离地面的高度，单位为 meters。
- `<AirSpeed>` — 每个 UAV 相对于风的速度，单位为 meters per second。
- `<HeadingAngle>` — 每个 UAV 的地面速度与北向之间的角度，单位为 radians。
- `<FlightPathAngle>` — 每个 UAV 的地面速度与 north-east plane 之间的角度，单位为 radians。
- `<RollAngle>` — 每个 UAV 沿机体 *x*-axis 的旋转角度，单位为 radians per second。
- `<RollAngleRate>` — 每个 UAV 沿机体 *x*-axis 的旋转角速度，单位为 radians per second。

使用 **State Bus Name** 属性指定状态输出 bus 的名称。

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，从 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### **Model Type** — UAV 制导模型类型 `MultirotorGuidance` (default) | `FixedWingGuidance`

所有 UAV 的制导模型类型。选择 `MultirotorGuidance` 以仿真多旋翼 UAV，或选择 `FixedWingGuidance` 以仿真固定翼 UAV。

### **Number of Instances** — 要仿真的 UAV 数量 `5` (default) | positive integer

将要仿真的 UAV 数量指定为正整数。

### **Data Type** — 输入和输出数值数据类型 `double` (default) | `single`

将输入和输出数值数据类型指定为 `double` 或 `single`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

### **Initial State** — 初始 UAV 状态选项卡，多个表条目

初始 UAV 状态选项卡，指定为多个表条目。在所有初始状态描述中，*N* 是您要仿真的 UAV 数量。

对于多旋翼 UAV，必须指定以下初始状态：

- **World Position** — 3-by-*N* 矩阵。将矩阵的每一列指定为一个 UAV 的初始 *xyz*-位置，单位为 meters。每个 UAV 的默认值为 `[0;0;0]`。
- **World Velocity** — 3-by-*N*。将矩阵的每一列指定为一个 UAV 的初始 *xyz*-速度，单位为 meters per second。每个 UAV 的默认值为 `[0;0;0]`。
- **Euler Angles (ZYX)** — 3-by-*N* 矩阵。将矩阵的每一列指定为一个 UAV 的初始欧拉角，采用 *z-*,*y-*,*x-*axis（yaw-pitch-roll）旋转顺序。每个 UAV 的默认值为 `[0;0;0]`。
- **Body Angular Rates** — 3-by-*N* 矩阵。将矩阵的每一列指定为一个 UAV 相对于 *x-*,*y-*, 和 *z-*axes 的初始角速率（分别为滚转角速率、俯仰角速率和偏航角速率），单位为 radians per second。每个 UAV 的默认值为 `[0;0;0]`。
- **Thrust** — 1-by*-N* 向量。将向量的每个元素指定为一个 UAV 的初始推力，单位为 newtons。每个 UAV 的默认值为 `0`。

对于固定翼 UAV，必须将以下初始状态指定为 1-by-*N* 向量：

- **North Position** — 每个 UAV 在北向的初始位置，单位为 meters。每个 UAV 的默认值为 `0`。
- **East Position** — 每个 UAV 在东向的初始位置，单位为 meters。每个 UAV 的默认值为 `0`。
- **Height** — 每个 UAV 的初始离地高度，单位为 meters。每个 UAV 的默认值为 `0`。
- **Air Speed** — 每个 UAV 相对于风的初始速度，单位为 meters per second。每个 UAV 的默认值为 `0`。
- **Heading Angle** — 每个 UAV 的地面速度与北向之间的初始角度，单位为 radians。每个 UAV 的默认值为 `0`。
- **Flight Path Angle** — 每个 UAV 的地面速度与 north-east plane 之间的初始角度，单位为 radians。每个 UAV 的默认值为 `0`。
- **Roll Angle** — 每个 UAV 沿机体 *x*-axis 的初始旋转角度，单位为 radians per second。每个 UAV 的默认值为 `0`。
- **Roll Angle Rate** — 每个 UAV 沿机体 *x*-axis 的初始旋转角速度，单位为 radians per second。每个 UAV 的默认值为 `0`。

**可调：** No

### **Configuration** — UAV 控制器配置选项卡，多个表条目

UAV 控制器配置选项卡，指定为多个表条目。在所有控制器配置描述中，*N* 是您要仿真的 UAV 数量。

对于多旋翼 UAV，指定以下参数：

- **PD Roll** — *N*-by-2 矩阵。将矩阵的每一行指定为一个 UAV 的滚转角控制器的比例增益和微分增益。每个 UAV 的默认值为 `[3402.97 116.67]`。
- **PD Pitch** — *N*-by-2 矩阵。将矩阵的每一行指定为一个 UAV 的俯仰角控制器的比例增益和微分增益。每个 UAV 的默认值为 `[3402.97 116.67]`。
- **P YawRate** — *N*-by-1 向量。将向量的每个元素指定为一个 UAV 的偏航角速率控制器的比例增益。每个 UAV 的默认值为 `1950`。
- **P Thrust** — *N*-by-1 向量。将向量的每一行指定为一个 UAV 的推力控制器的比例增益。每个 UAV 的默认值为 `3900`。
- **Mass** — *N*-by-1 向量。将向量的每个元素指定为一个 UAV 的质量，单位为 Kg。每个 UAV 的默认值为 `0.1`。

对于固定翼 UAV，指定以下参数：

- **P Height** — *N*-by-1 向量。将向量的每个元素指定为一个 UAV 的高度控制器的比例增益。每个 UAV 的默认值为 `3.9`。
- **P Flight Path Angle** — *N*-by-1 向量。将向量的每个元素指定为一个 UAV 的航迹角控制器的比例增益。每个 UAV 的默认值为 `39`。
- **PD Roll** — *N*-by-2 矩阵。将矩阵的每个元素指定为一个 UAV 的俯仰角控制器的比例增益和微分增益。每个 UAV 的默认值为 `[3402.97 116.67]`。
- **P Air Speed** — *N*-by-1 向量。将向量的每个元素指定为一个 UAV 的空速控制器的比例增益。每个 UAV 的默认值为 `1`。
- **Min/Max Flight Path Angle** — *N*-by-2 矩阵。将矩阵的每个元素指定为一个 UAV 的最小和最大航迹角，单位为 radians。每个 UAV 的默认值为 `[-pi/2 pi/2]`

### **Input/Output Bus Names** — Simulink bus 信号名称选项卡 bus 名称

此选项卡包含 **State Bus Name**、**Control Bus Name** 和 **Environment Bus Name** 参数，它们分别指定输出状态 bus、输入控制 bus 和输入环境 bus 的名称。每个 bus 都具有基于 UAV 模型和输入类型的默认名称。

| Model Type 参数 | 默认 State Bus Name | 默认 Control Bus Name | 默认 Environment Bus Name |
| --- | --- | --- | --- |
| `FixedWingGuidance` | `FixedWingGuidanceStateBus` | `FixedWingGuidanceControlBus` | `FixedWingGuidanceEnvironmentBus` |
| `MultirotorGuidance` | `MultirotorGuidanceStateBus` | `MultirotorGuidanceControlBus` | `MultirotorGuidanceEnvironmentBus` |

若要在同一 Simulink 模型中使用多个制导模型，请为每个 Multi-Instance Guidance Model 模块指定互不重叠的 bus 名称。

## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2025a 中引入**

## 描述

多个 UAV 的降阶模型

Multi-Instance Guidance Model 模块使用降阶固定翼 [1] 或多旋翼 [2] 运动学模型和自动驾驶仪控制器来仿真多个小型 UAV。
