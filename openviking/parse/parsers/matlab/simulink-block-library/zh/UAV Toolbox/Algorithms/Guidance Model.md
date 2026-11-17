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
```yaml
ports:
- name: Control
  summary: 控制指令总线
  direction: input
- name: Environment
  summary: 环境输入总线
  direction: input
  data_types: bus
- name: State
  summary: 仿真的 UAV 状态总线
  direction: output
  data_types: bus
```

### 输入

### **Control** — 控制指令总线

发送至 UAV 模型的控制指令，指定为总线。

对于多旋翼 UAV，该模型近似为针对每条指令的独立 PD 控制器。总线的元素为控制指令：

- `Roll` - 横滚角，单位为弧度。
- `Pitch` - 俯仰角，单位为弧度。
- `YawRate` - 偏航角速率，单位为弧度每秒。（D = 0。仅 P 控制器）
- `Thrust` - UAV 的垂直推力，单位为牛顿。（D = 0。仅 P 控制器）

对于固定翼 UAV，该模型假设 UAV 在协调转弯条件下飞行。制导模型方程假设侧滑为零。总线的元素为：

- `Height` - 离地高度，单位为米。
- `AirSpeed` - UAV 相对于风的速度，单位为米每秒。
- `RollAngle` - 沿机体前向轴的横滚角，单位为弧度。由于协调转弯条件，航向角速率基于横滚角。

使用 **Control Bus Name** 属性指定控制输入总线的名称。

### **Environment** — 环境输入总线

环境输入，指定为总线。该模型在尝试实现指令控制时会补偿这些环境输入。

如果将 **Model Type** 属性设置为 `MultirotorGuidance`，则必须指定一个包含 `Gravity` 元素的总线，该元素包含 UAV 在惯性坐标系 z 轴方向上的重力加速度，单位为米每秒平方。

如果将 **Model Type** 属性设置为 `FixedWingGuidance`，则必须指定一个包含以下元素的总线：

- `WindNorth` — UAV 在北方向上的风速，单位为米每秒。
- `WindEast` — UAV 在东方向上的风速，单位为米每秒。
- `WindDown` — UAV 在向下方向上的风速，单位为米每秒。
- `Gravity` — UAV 在惯性坐标系 z 轴方向上的重力加速度，单位为米每秒平方。

使用 **Environment Bus Name** 属性指定环境输入总线的名称。

**数据类型：** `bus`
### 输出

### **State** — 仿真的 UAV 状态总线

仿真的 UAV 状态，以总线形式返回。该模块使用 `Control` 和 `Environment` 输入以及制导模型方程来仿真 UAV 状态。

对于多旋翼 UAV，状态是包含五个元素的总线：

- **WorldPosition** - `[x y z]`，单位为米。
- **WorldVelocity** - `[vx vy vz]`，单位为米每秒。
- **EulerZYX** - `[psi theta phi]` 欧拉角，单位为弧度。
- **BodyAngularRateRPY** - `[r p q]`，沿 UAV 的 `xyz` 轴，单位为弧度每秒。
- **Thrust** - `F`，单位为牛顿。

对于固定翼 UAV，状态是包含八个元素的总线：

- **North** - 北方向上的位置，单位为米。
- **East** - 东方向上的位置，单位为米。
- **Height** - 离地高度，单位为米。
- **AirSpeed** - 相对于风的速度，单位为米每秒。
- **HeadingAngle** - 地面速度与北方向之间的夹角，单位为弧度。
- **FlightPathAngle** - 地面速度与东北平面之间的夹角，单位为弧度。
- **RollAngle** - 沿机体 *x* 轴的旋转角，单位为弧度每秒。
- **RollAngleRate** - 沿机体 *x* 轴的旋转角速度，单位为弧度每秒。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: ModelType
  summary: UAV 制导模型类型 MultirotorGuidance（默认）| FixedWingGuidance
  group: ''
- name: DataType
  summary: 输入和输出数值数据类型 double（默认）| single
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
- name: Initial State
  summary: 初始 UAV 状态选项卡 多个表项
  group: ''
- name: Configuration
  summary: UAV 控制器配置选项卡 多个表项
  group: ''
- name: Input/Output Bus Names
  summary: Simulink 总线信号名称选项卡 多个字符向量条目
  group: ''
```

### **ModelType** — UAV 制导模型类型 `MultirotorGuidance`（默认）| `FixedWingGuidance`

UAV 制导模型类型，指定为 `MultirotorGuidance` 或 `FixedWingGuidance`。模型类型决定 UAV `State` 的元素以及所需的 `Control` 和 `Environment` 输入。

**可调：** 否

### **DataType** — 输入和输出数值数据类型 `double`（默认）| `single`

输入和输出数值数据类型，指定为 `double` 或 `single`。根据可能的软件或硬件限制选择数据类型。

**可调：** 否

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，该 C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

**Tunable:** No

### **Initial State** — 初始 UAV 状态选项卡 多个表项

初始 UAV 状态选项卡，指定为多个表项。此选项卡上的所有条目均不可调。

对于多旋翼 UAV，初始状态为：

- **World Position** - `[x y z]`，单位为米。
- **World Velocity** - `[vx vy vz]`，单位为米每秒。
- **Euler Angles (ZYX)** - `[psi theta phi]`，单位为弧度。
- **Body Angular Rates** - `[p q r]`，单位为弧度每秒。
- **Thrust** - `F`，单位为牛顿。

对于固定翼 UAV，初始状态为：

- **North** - 北向位置，单位为米。
- **East** - 东向位置，单位为米。
- **Height** - 离地高度，单位为米。
- **Air Speed** - 相对于风的速度，单位为米每秒。
- **Heading Angle** - 地速与北向之间的夹角，单位为弧度。
- **Flight Path Angle** - 地速与东北平面之间的夹角，单位为弧度。
- **Roll Angle** - 沿机体 *x* 轴的旋转角度，单位为弧度每秒。
- **Roll Angle Rate** - 沿机体 *x* 轴的旋转角速度，单位为弧度每秒。

**Tunable:** No

### **Configuration** — UAV 控制器配置选项卡 多个表项

UAV 控制器配置选项卡，指定为多个表项。此选项卡允许您配置 UAV 内部控制行为的参数。为动态模型指定比例（P）和微分（D）增益，以及 UAV 质量（以千克为单位，适用于多旋翼）。

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
- **Min/Max Flight Path Angle**（`[min max]` 角度，单位为弧度）

**Tunable:** No

### **Input/Output Bus Names** — Simulink 总线信号名称选项卡 多个字符向量条目

Simulink 总线信号名称选项卡，指定为多个字符向量条目。这些总线具有基于 UAV 模型和输入类型的默认名称。要在同一 Simulink 模型中使用多个制导模型，请指定互不相同的总线名称。此选项卡上的所有条目均不可调。
## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

UAV 的降阶模型

Guidance Model 模块表示小型无人机（UAV）固定翼[1]和多旋翼[2]制导模型，该模型基于控制输入和环境输入估计 UAV 状态。该模型近似描述了由自动驾驶仪控制器和固定翼或多旋翼三维运动运动学模型组成的闭环系统的行为。将此模块用作降阶制导模型来仿真您的固定翼或多旋翼 UAV。指定 **ModelType** 以选择您的 UAV 类型。使用 **Initial State** 选项卡根据模型类型指定 UAV 的初始状态。**Configuration** 选项卡定义 UAV 的控制参数和物理参数。
