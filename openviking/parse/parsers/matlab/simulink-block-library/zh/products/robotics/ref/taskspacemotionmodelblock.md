---
type: simulink-block
title: 'Task Space Motion Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Manipulator Modeling'
documentation_page: 'taskspacemotionmodelblock'
documentation_source_path: 'ref/taskspacemotionmodelblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Task Space Motion Model

## 端口

### 输入

### **refPose** — 期望的末端执行器位姿 4-by-4 矩阵

齐次变换矩阵，表示期望的末端执行器位姿，以 meters 为单位指定。

### **refVel** — 期望的末端执行器速度 6-element 向量

6-element 向量，表示末端执行器的期望线速度和角速度，以 meters per second 和 radians per second 为单位指定。

### **FExt** — 外部力 6-by-*m* 矩阵

6-by-*m* 矩阵，表示外部力，其中每列都是形式为 `[Fx; Fy; Fz; Tx; Ty; Tz]` 的力旋量。
`Fx`、`Fy` 和 `Fz` 是沿 *x*-、*y*- 和 *z*- 轴的力，以 Newtons 为单位。`Tx`、`Ty` 和 `Tz` 是绕 *x*-、*y*- 和 *z*- 轴的力矩，以 Newton-meters 为单位。
*m* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的刚体数量。*m* 个力旋量中的每一个作用在刚体树中对应索引的刚体坐标系上。例如，`FExt` 的第三列指定作用在刚体树中第三个刚体上的力旋量。

#### 依赖项

要启用此端口，将 `Show external force input` 参数设置为 `on`。

### 输出

### **q** — 关节位置 *n*-element 向量

关节位置输出为 *n*-element 向量，以 radians 或 meters 为单位，其中 *n* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的非固定关节数量。

### **qd** — 关节速度 *n*-element

关节速度输出为 *n*-element 向量，以 radians per second 或 meters per second 为单位，其中 *n* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的非固定关节数量。

### **qdd** — 关节加速度 *n*-element

关节加速度输出为 *n*-element，以 radians per second squared 或 meters per second squared 为单位，其中 *n* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的非固定关节数量。

## 参数

### **Rigid body tree** — 刚体树 `twoJointRigidBodyTree` object (default) | `RigidBodyTree` object

机器人模型，指定为 `RigidBodyTree` 对象。还可以使用 `importrobot` 从 URDF (Unified Robot Description Formation) 文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **End effector** — 末端执行器刚体 `tool` (default)

此参数定义将用作末端执行器的刚体，并为其定义任务空间运动。该属性必须对应于该属性的 `rigidBodyTree` 对象中的刚体名称。单击 **Select body** 以从 `rigidBodyTree` 中选择刚体。如果更新了 `rigidBodyTree` 而未同时更新末端执行器，则默认分配索引最高的刚体。

### **Proportional gain** — PD 控制的比例增益 `500*eye(6)` (default) | 6-by-6 矩阵

比例-微分 (PD) 控制的比例增益，指定为 6-by-6 矩阵。

### **Derivative gain** — PD 控制的微分增益 `100*eye(6)` (default) | 6-by-6 矩阵

比例-微分 (PD) 控制的微分增益，指定为 6-by-6 矩阵。

### **Joint damping** — 阻尼比 `[1 1]` (default) | *n*-element 向量 | 标量

每个关节上的阻尼比，指定为标量或 *n*-element 向量，其中 *n* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的非固定关节数量。

### **Show external force input** — 显示 `FExt` 端口 `off` (default) | `on`

单击复选框以启用此参数，从而使用 `FExt` 端口输入外部力。

### **Initial joint configuration** — 初始关节位置 `0` (default) | *n*-element 向量 | 标量

初始关节位置，指定为 *n*-element 向量或标量，以 radians 为单位。*n* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的非固定关节数量。

### **Initial joint velocities** — 初始关节速度 `0` (default) | *n*-element 向量 | 标量

初始关节速度，指定为 *n*-element 向量或标量，以 radians per second 为单位。*n* 是 **Rigid body tree** 参数中 `rigidBodyTree` 对象中的非固定关节数量。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关更多信息，请参见 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会在后续仿真中重用。

**可调：** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：静态内存分配支持

Task Space Motion Model 现在支持在禁用动态内存分配的情况下进行代码生成。有关禁用动态内存分配的更多信息，请参见 Set Dynamic Memory Allocation Threshold (MATLAB Coder)。

## 描述

根据任务空间输入对刚体树运动进行建模

Task Space Motion Model 模块对机械臂的闭环任务空间运动进行建模，该机械臂指定为 `rigidBodyTree` 对象。运动模型行为使用比例-微分 (PD) 控制定义。

有关运动方程的更多详细信息，请参见 Task-Space Motion Model。
