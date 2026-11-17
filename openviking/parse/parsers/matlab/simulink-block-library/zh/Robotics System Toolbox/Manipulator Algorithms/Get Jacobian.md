---
type: simulink-block
title: 'Get Jacobian'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'getjacobian'
documentation_source_path: 'ref/getjacobian.html'
language: zh-CN
chinese_source: worker-translation
---

# Get Jacobian

## 端口

### 输入

### **Config** — 机器人配置向量

机器人配置，指定为机器人模型中所有非固定关节位置的向量，由 **Rigid body tree** 参数设置。您还可以在 Constant 或 MATLAB Function 模块内使用 `homeConfiguration` 或 `randomConfiguration` 函数为复杂机器人生成此向量。

### 输出

### **Jacobian** — 末端执行器的几何雅可比 6-by-*n* 矩阵

具有指定配置 **Config** 的末端执行器的几何雅可比，返回为 6-by-*n* 矩阵，其中 *n* 是末端执行器的自由度数量。雅可比将关节空间速度映射到相对于基座坐标系的末端执行器速度。末端执行器速度等于：

使用雅可比和关节速度计算末端执行器线速度的方程

*ω* 是角速度，*υ* 是线速度， 是关节空间速度。

## 参数

### **Rigid body tree** — 机器人模型 `twoJointRigidBodyTree`（默认）| `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。您还可以使用 `importrobot` 从 URDF（统一机器人描述格式）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **End effector** — 雅可比的末端执行器 刚体名称

`Jacobian` 的末端执行器，指定为 **Rigid body tree** 机器人模型中的刚体名称。要从机器人模型访问刚体名称，请点击 **Select body**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。只要模型不更改，C 代码将复用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**Tunable:** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

机器人配置的几何雅可比

Get Jacobian 模块返回 `rigidBodyTree` 机器人模型在给定配置下指定末端执行器相对于基座的几何雅可比。

雅可比将关节空间速度映射到相对于基座坐标系的末端执行器速度。末端执行器速度等于：

使用雅可比和关节速度计算末端执行器线速度的方程

*ω* 是角速度，*υ* 是线速度， 是关节空间速度。
