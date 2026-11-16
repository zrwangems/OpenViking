---
type: simulink-block
title: 'Joint Space Mass Matrix'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'jointspacemassmatrix'
documentation_source_path: 'ref/jointspacemassmatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Joint Space Mass Matrix

## 端口

### 输入

### **Config** — 机器人配置向量

机器人配置，指定为机器人模型中所有非固定关节的位置向量，由 **刚体树** 参数设置。您还可以在 Constant 或 MATLAB Function 模块内使用 `homeConfiguration` 或 `randomConfiguration` 函数为复杂机器人生成此向量。
### 输出

### **MassMatrix** — 配置的关节空间质量矩阵，正定对称矩阵

给定机器人配置的关节空间质量矩阵，返回为正定对称矩阵。

## 参数

### **刚体树** — 机器人模型 `twoJointRigidBodyTree`（默认）| `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。您还可以使用 `importrobot` 从 URDF（Unified Robot Description Formation）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，该 C 代码会复用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调:** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

机器人配置的关节空间质量矩阵

Joint Space Mass Matrix 模块返回 **刚体树** 机器人模型在给定机器人配置（关节位置）下的关节空间质量矩阵。
