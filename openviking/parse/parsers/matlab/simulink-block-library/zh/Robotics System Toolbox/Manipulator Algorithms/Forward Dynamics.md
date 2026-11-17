---
type: simulink-block
title: 'Forward Dynamics'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'forwarddynamics'
documentation_source_path: 'ref/forwarddynamics.html'
language: zh-CN
chinese_source: worker-translation
---

# Forward Dynamics

## 端口

### 输入

### **Config** — 机器人配置向量

机器人配置，指定为机器人模型中所有非固定关节位置的向量，由 **Rigid body tree** 参数设定。你也可以在 Constant 或 MATLAB Function 模块中使用 `homeConfiguration` 或 `randomConfiguration` 函数为复杂机器人生成该向量。

### **JointVel** — 关节速度向量

关节速度，指定为向量。关节速度的数量等于机器人的自由度（非固定关节的数量）。

### **JointTorq** — 关节力矩向量

关节力矩，指定为向量。每个元素对应于施加在特定关节上的力矩。关节力矩的数量等于机器人的自由度（非固定关节的数量）。

### **FExt** — 外部力矩阵 6×*n* 矩阵

外部力矩阵，指定为 6×*n* 矩阵，其中 *n* 是机器人模型中刚体的数量。该矩阵在对应于特定刚体的行中包含非零值。每一行是作用于该特定刚体的力和力矩向量，作为该刚体的力螺旋。使用 `externalForce` 配合 MATLAB Function 模块生成该矩阵。

### 输出

### **JointAccel** — 关节加速度向量

关节加速度，以向量形式返回。关节加速度的数量等于机器人的自由度。

## 参数

### **Rigid body tree** — 机器人模型 `twoJointRigidBodyTree`（默认）| `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。你也可以使用 `importrobot` 从 URDF（统一机器人描述格式）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，你可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

给定关节力矩和状态的关节加速度

Forward Dynamics 模块在给定由关节力矩、关节状态和外部力组成的机器人状态的情况下，计算机器人模型的关节加速度。要获得关节加速度，请指定机器人配置（关节位置）、关节速度、施加的力矩和外部力。

在 **Rigid body tree** 参数中将机器人模型指定为 `rigidBodyTree` 对象，并设置该对象的 Gravity 属性。你也可以使用 `importrobot` 从 URDF（统一机器人描述格式）文件导入机器人模型。
