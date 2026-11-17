---
type: simulink-block
title: 'Gravity Torque'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'gravitytorque'
documentation_source_path: 'ref/gravitytorque.html'
language: zh-CN
chinese_source: worker-translation
---

# Gravity Torque

## 端口
```yaml
ports:
- name: Config
  summary: 机器人配置向量
  direction: input
- name: JointTorq
  summary: 关节力矩向量
  direction: output
```

### 输入

### **Config** — 机器人配置向量

机器人配置，指定为机器人模型中所有非固定关节位置的向量，由 **Rigid body tree** 参数设置。您还可以在 Constant 或 MATLAB Function 模块内使用 `homeConfiguration` 或 `randomConfiguration` 函数为复杂机器人生成此向量。

### 输出

### **JointTorq** — 关节力矩向量

关节力矩，指定为向量。每个元素对应于施加到特定关节的力矩。关节力矩的数量等于机器人的自由度（非固定关节的数量）。
## 参数
```yaml
parameters:
- name: Rigid body tree
  summary: 机器人模型 twoJointRigidBodyTree（默认）| RigidBodyTree 对象
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Rigid body tree** — 机器人模型 `twoJointRigidBodyTree`（默认）| `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。您还可以使用 `importrobot` 从 URDF（Unified Robot Description Formation）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

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

补偿重力的关节力矩

Gravity Torque 模块返回在 **Rigid body tree** 机器人模型上使用当前 Gravity 设置将机器人保持在给定配置所需的关节力矩。
