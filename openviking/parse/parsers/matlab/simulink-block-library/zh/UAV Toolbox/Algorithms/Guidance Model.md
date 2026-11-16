---
type: simulink-block
title: 'Guidance Model'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'guidancemodel'
documentation_source_path: 'ref/guidancemodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Guidance Model

## 端口

### 输入

### **Control** — 控制指令总线

发送到 UAV 模型的控制指令，指定为总线。

对于多旋翼 UAV，该模型近似为针对每个指令的独立 PD 控制器。总线的元素为控制指令：

- `Roll` - 滚转角，单位为 radians。
- `Pitch` - 俯仰角，单位为 radians。
- `YawRate` - 偏航角速率，单位为 radians per second。（D = 0. 仅 P 控制器）
- `Thrust` - UAV 的垂直推力，单位为 Newtons。（D = 0. 仅 P 控制器）

对于固定翼 UAV，该模型假设 UAV 在协调转弯条件下飞行。制导模型方程假设零侧滑。总线的元素为：

- `Height` - 高于地面的高度，单位为 meters。
- `AirSpeed` - UAV 相对于风的速度，单位为 meters per second。
- `RollAngle` - 沿机体前向轴的滚转角，单位为 radians。由于协调转弯条件，航向角速率基于滚转角。

使用 **Control Bus Name** 属性指定控制输入总线的名称。

### **Environment** — 环境输入总线

环境输入，指定为总线。该模型在尝试实现指令控制时会补偿这些环境输入。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则必须指定一个包含 `Gravity` 元素的总线，该元素包含 UAV 在惯性坐标系 z 轴方向上的重力加速度，单位为 meters per second squared。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则必须指定一个包含以下元素的总线：

- `WindNorth` — UAV 在北方向上的风速，单位为 meters per second。
- `WindEast` — UAV 在东方向上的风速，单位为 meters per second。
- `WindDown` — UAV 在向下方向上的风速，单位为 meters per second。
- `Gravity` — UAV 在惯性坐标系 z 轴方向上的重力加速度，单位为 meters per second squared。

使用 **Environment Bus Name** 属性指定环境输入总线的名称。

**数据类型:** `bus`
### 输出

### **State** — 仿真的 UAV 状态总线

仿真的 UAV 状态，以总线形式返回。该模块使用 `Control` 和 `Environment` 输入以及制导模型方程来仿真 UAV 状态。

对于多旋翼 UAV，状态是一个五元素总线：

- **WorldPosition** - `[x y z]`，单位为 meters。
- **WorldVelocity** - `[vx vy vz]`，单位为 meters per second。
- **EulerZYX** - `[psi theta phi]` 欧拉角，单位为 radians。
- **BodyAngularRateRPY** - 沿 UAV 的 `xyz` 轴的 `[r p q]`，单位为 radians per second。
- **Thrust** - `F`，单位为 Newtons。

对于固定翼 UAV，状态是一个八元素总线：

- **North** - 北方向上的位置，单位为 meters。
- **East** - 东方向上的位置，单位为 meters。
- **Height** - 高于地面的高度，单位为 meters。
- **AirSpeed** - 相对于风的速度，单位为 meters per second。
- **HeadingAngle** - 地面速度与北方向之间的夹角，单位为 radians。
- **FlightPathAngle** - 地面速度与北东平面之间的夹角，单位为 radians。
- **RollAngle** - 沿机体 *x* 轴的旋转角，单位为 radians per second。
- **RollAngleRate** - 沿机体 *x* 轴的旋转角速度，单位为 radians per second。

**数据类型:** `bus`

## 参数

### **ModelType** — UAV 制导模型类型 `MultirotorGuidance` (default) | `FixedWingGuidance`

UAV 制导模型类型，指定为 `MultirotorGuidance` 或 `FixedWingGuidance`。模型类型决定 UAV `State` 的元素以及所需的 `Control` 和 `Environment` 输入。

**可调:** No

### **DataType** — 输入和输出数值数据类型 `double` (default) | `single`

输入和输出数值数据类型，指定为 `double` 或 `single`。根据可能的软件或硬件限制选择数据类型。

**可调:** No

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会复用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。

**可调:** No

### **Initial State** — 初始 UAV 状态选项卡，多个表项

初始 UAV 状态选项卡，指定为多个表项。此选项卡上的所有条目均不可调。

对于多旋翼 UAV，初始状态为：

- **World Position** - `[x y z]`，单位为 meters。
- **World Velocity** - `[vx vy vz]`，单位为 meters per second。
- **Euler Angles (ZYX)** - `[psi theta phi]`，单位为 radians。
- **Body Angular Rates** - `[p q r]`，单位为 radians per second。
- **Thrust** - `F`，单位为 Newtons。

对于固定翼 UAV，初始状态为：

- **North** - 北方向上的位置，单位为 meters。
- **East** - 东方向上的位置，单位为 meters。
- **Height** - 高于地面的高度，单位为 meters。
- **Air Speed** - 相对于风的速度，单位为 meters per second。
- **Heading Angle** - 地面速度与北方向之间的夹角，单位为 radians。
- **Flight Path Angle** - 地面速度与北东平面之间的夹角，单位为 radians。
- **Roll Angle** - 沿机体 *x* 轴的旋转角，单位为 radians per second。
- **Roll Angle Rate** - 沿机体 *x* 轴的旋转角速度，单位为 radians per second。

**可调:** No

### **Configuration** — UAV 控制器配置选项卡，多个表项

UAV 控制器配置选项卡，指定为多个表项。此选项卡允许您配置 UAV 内部控制行为的参数。为动态模型指定比例 (P) 和微分 (D) 增益，以及 UAV 质量，单位为 kilograms（对于多旋翼）。

对于多旋翼 UAV，参数为：

- **PD Roll**
- **PD Pitch**
- **P YawRate**
- **P Thrust**
- **Mass**(kg)

对于固定翼 UAV，参数为：

- **P Height**
- **P Flight Path Angle**
- **PD Roll**
- **P Air Speed**
- **Min/Max Flight Path Angle** (`[min max]` 角度，单位为 radians)

**可调:** No

### **Input/Output Bus Names** — Simulink 总线信号名称选项卡，多个字符向量条目

Simulink 总线信号名称选项卡，指定为多个字符向量条目。这些总线具有基于 UAV 模型和输入类型的默认名称。要在同一 Simulink 模型中使用多个制导模型，请指定互不重叠的不同总线名称。此选项卡上的所有条目均不可调。

## 所属库

UAV Toolbox / Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

用于 UAV 的降阶模型

Guidance Model 模块表示一个小型无人机 (UAV) 固定翼[1]和多旋翼[2]制导模型，该模型基于控制输入和环境输入估计 UAV 状态。该模型近似表示一个闭环系统的行为，该系统由自动驾驶仪控制器以及用于三维运动的固定翼或多旋翼运动学模型组成。将此模块用作降阶制导模型来仿真您的固定翼或多旋翼 UAV。指定 **ModelType** 以选择您的 UAV 类型。使用 **Initial State** 选项卡根据模型类型指定 UAV 的初始状态。**Configuration** 选项卡定义 UAV 的控制参数和物理参数。
