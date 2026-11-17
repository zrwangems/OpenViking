---
type: simulink-block
title: 'Get Transform'
family: 'manipulator-algorithms'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'gettransformblock'
documentation_source_path: 'ref/gettransformblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Get Transform

## 端口

### 输入

### **Config** — 机器人配置向量

机器人配置，指定为机器人模型中所有非固定关节的位置向量，由 **Rigid body tree** 参数设置。你还可以在 Constant 或 MATLAB Function 模块内使用 `homeConfiguration` 或 `randomConfiguration` 函数为复杂机器人生成此向量。

### 输出

### **Transform** — 齐次变换 4×4 矩阵

齐次变换，返回为 4×4 矩阵。

## 参数

### **Rigid body tree** — 机器人模型 `twoJointRigidBodyTree`（默认）| `RigidBodyTree` 对象

机器人模型，指定为 `rigidBodyTree` 对象。你也可以使用 `importrobot` 从 URDF（Unified Robot Description Formation）文件导入机器人模型。

默认机器人模型 `twoJointRigidBodyTree` 是一个具有旋转关节和两个自由度的机器人。

### **Target body** — 目标机体名称 机体名称

目标机体名称，指定为 **Rigid body tree** 中指定的机器人模型中的机体名称。要从机器人模型访问机体名称，请点击 **Select body**。目标坐标系是你希望将点变换到的坐标系。

### **Source body** — 源机体名称 机体名称

源机体名称，指定为 **Rigid body tree** 中指定的机器人模型中的机体名称。要从机器人模型访问机体名称，请点击 **Select body**。源坐标系是你希望从其中变换点的坐标系。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

获取机体坐标系之间的变换

Get Transform 模块返回 **Rigid body tree** 机器人模型上机体坐标系之间的齐次变换。为机器人模型指定一个 `rigidBodyTree` 对象，并在模块中选择源机体和目标机体。

该模块使用 **Config**，即机器人配置（关节位置）输入，来计算从源机体到目标机体的变换。此变换用于将坐标从源机体转换到目标机体。要转换到基座坐标，请使用基座机体名称作为 **Target body** 参数。
