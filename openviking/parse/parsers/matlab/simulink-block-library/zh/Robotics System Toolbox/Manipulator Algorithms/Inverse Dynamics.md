---
type: simulink-block
title: 'Inverse Dynamics'
family: 'manipulator-algorithms'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'inversedynamics'
documentation_source_path: 'ref/inversedynamics.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Dynamics

## 端口

### 输入

### **Config** — 机器人配置向量

机器人配置，指定为机器人模型中所有非固定关节的位置向量，由 **Rigid body tree** 参数设置。还可以在 Constant 或 MATLAB Function 模块内使用 `homeConfiguration` 或 `randomConfiguration` 函数为复杂机器人生成此向量。

### **JointVel** — 关节速度向量

关节速度，指定为向量。关节速度数等于机器人的自由度（非固定关节数）。

### **JointAccel** — 关节加速度向量

关节加速度，指定为向量。关节加速度数等于机器人的自由度。

### **FExt** — 外部力矩阵 6×*n* 矩阵

外部力矩阵，指定为 6×*n* 矩阵，其中 *n* 是机器人模型中的刚体数。该矩阵在对应于特定刚体的行中包含非零值。每一行是一个所施加的力和力矩向量，用作该特定刚体的力旋量。使用 `externalForce` 与 MATLAB Function 模块生成此矩阵
### 输出

### **JointTorq** — 关节力矩向量

关节力矩，返回为向量。每个元素对应于施加到特定关节的力矩。关节力矩数等于机器人的自由度（非固定关节数）。

## 参数

### **Rigid body tree** — 机器人模型 `twoJointRigidBodyTree`（默认） | `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。还可以使用 `importrobot` 从 URDF（Unified Robot Description Format）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

给定运动所需的关节力矩

Inverse Dynamics 模块返回机器人维持指定机器人状态所需的关节力矩。要获取所需的关节力矩，请指定机器人配置（关节位置）、关节速度、关节加速度和外部力。
