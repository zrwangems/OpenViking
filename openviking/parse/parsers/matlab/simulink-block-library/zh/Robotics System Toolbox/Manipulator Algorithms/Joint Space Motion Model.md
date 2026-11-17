---
type: simulink-block
title: 'Joint Space Motion Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'jointspacemotionmodelblock'
documentation_source_path: 'ref/jointspacemotionmodelblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Joint Space Motion Model

## 端口
```yaml
ports:
- name: qRef
  summary: 关节位置 *n* 元向量
  direction: input
- name: qRefDot
  summary: 关节速度 *n* 元向量
  direction: input
- name: qRefDDot
  summary: 关节加速度 *n* 元向量
  direction: input
- name: FExt
  summary: 作用在系统上的外力 6×*m* 矩阵
  direction: input
- name: q
  summary: 关节位置 *n* 元向量
  direction: output
- name: qd
  summary: 关节速度 *n* 元向量
  direction: output
- name: qdd
  summary: 关节加速度 *n* 元向量
  direction: output
```

### 输入

### **qRef** — 关节位置 *n* 元向量

*n* 元向量，表示期望的关节位置，单位为弧度，其中 *n* 是 `Rigid body
tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖

要启用此端口，请将 `Motion
Type` 参数设置为 `Computed Torque Control`、
`PD Control` 或 `Independent Joint
Motion`。

### **qRefDot** — 关节速度 *n* 元向量

*n* 元向量，表示期望的关节速度，单位为弧度每秒，其中 *n* 是
`Rigid body
tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖

要启用此端口，请将 `Motion
Type` 参数设置为 `Computed Torque Control`
或 `Independent Joint Motion`。

### **qRefDDot** — 关节加速度 *n* 元向量

*n* 元向量，表示期望的关节速度，单位为弧度每二次方秒，其中 *n* 是
`Rigid body
tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖

要启用此端口，请将 `Motion
Type` 参数设置为 `Computed Torque Control`、
`PD Control` 或 `Independent Joint
Motion`。

### **FExt** — 作用在系统上的外力 6×*m* 矩阵

一个 6×*m* 矩阵，表示 `Rigid body
tree` 参数的 `rigidBodyTree` 对象中 *m*
个物体所受的外力。

#### 依赖

要启用此端口，请将 `Show external
force input` 参数设置为 `on`。
### 输出

### **q** — 关节位置 *n* 元向量

关节位置输出，为 *n* 元向量，单位为弧度或米，其中 *n* 是 `Rigid body
tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

### **qd** — 关节速度 *n* 元向量

关节速度输出，为 *n* 元向量，单位为弧度每秒或米每秒，其中 *n* 是
`Rigid body
tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量

### **qdd** — 关节加速度 *n* 元向量

关节加速度输出，为 *n* 元向量，单位为弧度每二次方秒或米每二次方秒，其中 *n* 是
`Rigid body
tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量
## 参数
```yaml
parameters:
- name: Rigid body tree
  summary: 机器人模型 twoJointRigidBodyTree（默认）| RigidBodyTree 对象
  group: ''
- name: Motion Type
  summary: 运动模型计算的运动类型 Computed Torque Control（默认）| Independent Joint Motion | PD Control | Open Loop Dynamics
  group: ''
- name: Specification format
  summary: 用于控制机器人的输入 Damping Ratio / Natural Frequency（默认）| Step Response
  group: ''
- name: Damping ratio
  summary: 系统阻尼比 1（默认）| 数值标量
  group: ''
- name: Natural frequency
  summary: 系统自然频率 10（默认）| 数值标量
  group: ''
- name: Settling time
  summary: 系统调节时间 0.59（默认）| 数值标量
  group: ''
- name: Overshoot
  summary: 系统超调 0.0（默认）| 数值标量
  group: ''
- name: Proportional gain
  summary: PD 控制的比例增益 100（默认）| *n*×*n* 矩阵 | 标量
  group: ''
- name: Derivative gain
  summary: PD 控制的微分增益 10（默认）| *n*×*n* 矩阵 | 标量
  group: ''
- name: Show external force input
  summary: 显示 FExt 端口 off（默认）| on
  group: ''
- name: Initial joint configuration
  summary: 初始关节位置 0（默认）| *n* 元素向量 | 标量
  group: ''
- name: Initial joint velocities
  summary: 初始关节速度 0（默认）| *n* 元素向量 | 标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Rigid body tree** — 机器人模型 `twoJointRigidBodyTree`（默认）| `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。您还可以使用 `importrobot` 从 URDF（Unified Robot Description Formation）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机械臂。

### **Motion Type** — 运动模型计算的运动类型 `Computed Torque Control`（默认）| `Independent Joint Motion` | `PD Control` | `Open Loop Dynamics`

运动类型，指定为字符串标量或字符向量，用于定义对象所建模的闭环关节空间行为。选项包括：

- `Computed Torque Control` — 补偿全身动力学，并指定 `Natural
  frequency` 和 `Damping
  ratio` 参数中指定的误差动力学。
- `Independent Joint Motion` — 使用 `Natural
  frequency` 和 `Damping
  ratio` 参数指定的误差动力学，将每个关节建模为独立的二阶系统。
- `PD Control` — 基于指定的 `Proportional
  gain` 和 `Derivative
  gain` 参数对关节使用比例-微分（PD）控制。
- `Open Loop Dynamics` — 如果启用了 `Show external
  force input`，则禁用除
  `FExt`
  之外的输入。这是一种开环配置。

### **Specification format** — 用于控制机器人的输入 `Damping Ratio / Natural Frequency`（默认）| `Step Response`

用于控制机器人系统的输入。选项包括：

- `Damping Ratio / Natural Frequency` — 使用系统的 `Natural frequency` 参数以 Hz 为单位设置自然频率，并使用 `Damping ratio` 参数设置阻尼比。
- `Step Response` — 使用 `Settling time` 和 `Overshoot` 参数，在具有固定调节时间和超调的离散时间步长下建模。

#### 依赖关系

要启用此参数，请将 `Motion Type` 参数设置为 `Computed Torque Control` 或 `Independent Joint Motion`。

### **Damping ratio** — 系统阻尼比 `1`（默认）| 数值标量

用于衰减系统振荡的阻尼比。值为 `1` 时不会产生阻尼，而 `0` 会完全阻尼系统。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Damping Ratio / Natural Frequency`。

### **Natural frequency** — 系统自然频率 `10`（默认）| 数值标量

系统在无阻碍情况下的振荡频率，以 Hz 为单位指定。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Damping Ratio / Natural Frequency`。

### **Settling time** — 系统调节时间 `0.59`（默认）| 数值标量

每个关节达到稳态所需的时间，以秒为单位。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Step Response`。

### **Overshoot** — 系统超调 `0.0`（默认）| 数值标量

系统超过目标位置的最大值。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Step Response`。

### **Proportional gain** — PD 控制的比例增益 `100`（默认）| *n*×*n* 矩阵 | 标量

比例-微分（PD）控制的比例增益，指定为标量或 *n*×*n* 矩阵，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `PD Control`。

### **Derivative gain** — PD 控制的微分增益 `10`（默认）| *n*×*n* 矩阵 | 标量

比例-微分（PD）控制的微分增益，指定为标量或 *n*×*n* 矩阵，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `PD Control`。

### **Show external force input** — 显示 `FExt` 端口 `off`（默认）| `on`

启用此参数以使用 `FExt` 端口输入外力。

#### 依赖关系

要启用此参数，请将 `Motion Type` 参数设置为 `Computed Torque Control`、`PD Control` 或 `Open Loop Dynamics`。

### **Initial joint configuration** — 初始关节位置 `0`（默认）| *n* 元素向量 | 标量

初始关节位置，指定为 *n* 元素向量或以弧度表示的标量。*n* 是 `Rigid body tree` 参数中 `rigidBodyTree` 对象内非固定关节的数量。

### **Initial joint velocities** — 初始关节速度 `0`（默认）| *n* 元素向量 | 标量

初始关节速度，指定为 *n* 元素向量或以弧度每秒表示的标量。*n* 是 `Rigid body tree` 参数中 `rigidBodyTree` 对象内非固定关节的数量。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重复使用。

**可调：** 否
## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：静态内存分配支持

Joint Space Motion Model 现在支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的详细信息，请参阅 Set Dynamic Memory Allocation Threshold (MATLAB Coder)。

## 描述

根据关节空间输入对刚体树运动进行建模

Joint Space Motion Model 模块对机械臂的闭环关节空间运动进行建模，该机械臂指定为 `rigidBodyTree` 对象。运动模型行为由 `Motion Type` 参数定义。

有关运动方程的更多详细信息，请参阅 Joint-Space Motion Model。
