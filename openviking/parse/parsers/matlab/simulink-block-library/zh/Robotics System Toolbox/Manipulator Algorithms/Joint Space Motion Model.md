---
type: simulink-block
title: 'Joint Space Motion Model'
family: 'manipulator-algorithms'
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

### 输入

### **qRef** — 关节位置 *n*-element vector

*n*-element vector，表示所需的关节位置，单位为 radians，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖关系

要启用此端口，请将 `Motion Type` 参数设置为 `Computed Torque Control`、`PD Control` 或 `Independent Joint Motion`。

### **qRefDot** — 关节速度 *n*-element vector

*n*-element vector，表示所需的关节速度，单位为 radians per second，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖关系

要启用此端口，请将 `Motion Type` 参数设置为 `Computed Torque Control` 或 `Independent Joint Motion`。

### **qRefDDot** — 关节加速度 *n*-element vector

*n*-element vector，表示所需的关节加速度，单位为 radians per second squared，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖关系

要启用此端口，请将 `Motion Type` 参数设置为 `Computed Torque Control`、`PD Control` 或 `Independent Joint Motion`。

### **FExt** — 作用于系统的外部力 6-by-*m* matrix

一个 6-by-*m* matrix，表示用于 `Rigid body tree` 参数的 `rigidBodyTree` 对象中 *m* 个物体的外部力。

#### 依赖关系

要启用此端口，请将 `Show external force input` 参数设置为 `on`。

### 输出

### **q** — 关节位置 *n*-element vector

关节位置，输出为 *n*-element vector，单位为 radians 或 meters，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

### **qd** — 关节速度 *n*-element vector

关节速度，输出为 *n*-element vector，单位为 radians per second 或 meters per second，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量

### **qdd** — 关节加速度 *n*-element vector

关节加速度，输出为 *n*-element vector，单位为 radians per second squared 或 meters per second squared，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量

## 参数

### **刚体树** — 机器人模型 `twoJointRigidBodyTree`（默认） | `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。还可以使用 `importrobot` 从 URDF (Unified Robot Description Formation) 文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机械臂。

### **运动类型** — 运动模型计算的运动类型 `Computed Torque Control`（默认） | `Independent Joint Motion` | `PD Control` | `Open Loop Dynamics`

运动类型，指定为 string scalar 或 character vector，用于定义对象所建模的闭环关节空间行为。选项包括：

- `Computed Torque Control` — 补偿全身动力学，并分配由 `Natural frequency` 和 `Damping ratio` 参数指定的误差动力学。
- `Independent Joint Motion` — 使用由 `Natural frequency` 和 `Damping ratio` 参数指定的误差动力学，将每个关节建模为独立的二阶系统。
- `PD Control` — 基于指定的 `Proportional gain` 和 `Derivative gain` 参数对关节使用比例-微分 (PD) 控制。
- `Open Loop Dynamics` — 如果启用了 `Show external force input`，则禁用除 `FExt` 以外的输入。这是开环配置。

### **设定格式** — 用于控制机器人的输入 `Damping Ratio / Natural Frequency`（默认） | `Step Response`

用于控制机器人系统的输入。选项包括：

- `Damping Ratio / Natural Frequency` — 使用系统的 `Natural frequency` 参数以 Hz 设置自然频率，并使用 `Damping ratio` 参数设置阻尼比。
- `Step Response` — 使用 `Settling time` 和 `Overshoot` 参数，以固定稳定时间和超调量对离散时间步进行建模。

#### 依赖关系

要启用此参数，请将 `Motion Type` 参数设置为 `Computed Torque Control` 或 `Independent Joint Motion`。

### **阻尼比** — 系统的阻尼比 `1`（默认） | numeric scalar

用于衰减系统振荡的阻尼比。值为 `1` 时不提供阻尼，而 `0` 会完全阻尼系统。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Damping Ratio / Natural Frequency`。

### **自然频率** — 系统的自然频率 `10`（默认） | numeric scalar

系统在无阻碍时的振荡频率，以 Hz 指定。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Damping Ratio / Natural Frequency`。

### **稳定时间** — 系统的稳定时间 `0.59`（默认） | numeric scalar

每个关节达到稳态所需的时间，以 seconds 为单位。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Step Response`。

### **超调量** — 系统超调量 `0.0`（默认） | numeric scalar

系统超出目标位置的最大值。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `Step Response`。

### **比例增益** — PD Control 的比例增益 `100`（默认） | *n*-by-*n* matrix | scalar

比例-微分 (PD) 控制的比例增益，指定为 scalar 或 *n*-by-*n* matrix，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量。

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `PD Control`。

### **微分增益** — PD 控制的微分增益 `10`（默认） | *n*-by-*n* matrix | scalar

比例-微分 (PD) 控制的微分增益，指定为 scalar 或 *n*-by-*n* matrix，其中 *n* 是 `Rigid body tree` 参数的 `rigidBodyTree` 对象中非固定关节的数量

#### 依赖关系

要启用此参数，请将 `Specification format` 参数设置为 `PD Control`。

### **显示外力输入** — 显示 `FExt` 端口 `off`（默认） | `on`

启用此参数以使用 `FExt` 端口输入外部力。

#### 依赖关系

要启用此参数，请将 `Motion Type` 参数设置为 `Computed Torque Control`、`PD Control` 或 `Open Loop Dynamics`。

### **初始关节配置** — 初始关节位置 `0`（默认） | *n*-element vector | scalar

初始关节位置，指定为 *n*-element vector 或 scalar，单位为 radians。*n* 是 `Rigid body tree` 参数中的 `rigidBodyTree` 对象中非固定关节的数量。

### **初始关节速度** — 初始关节速度 `0`（默认） | *n*-element vector | scalar

初始关节速度，指定为 *n*-element vector 或 scalar，单位为 radians per second。*n* 是 `Rigid body tree` 参数中的 `rigidBodyTree` 对象中非固定关节的数量。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。

**可调：** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a: 静态内存分配支持

Joint Space Motion Model 现在支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的详细信息，请参阅 Set Dynamic Memory Allocation Threshold (MATLAB Coder)。

## 描述

给定关节空间输入，对刚体树运动进行建模

Joint Space Motion Model 模块对机械臂机器人的闭环关节空间运动进行建模，该机器人指定为 `rigidBodyTree` 对象。运动模型行为由 `Motion Type` 参数定义。

有关运动方程的更多详细信息，请参阅 Joint-Space Motion Model。
