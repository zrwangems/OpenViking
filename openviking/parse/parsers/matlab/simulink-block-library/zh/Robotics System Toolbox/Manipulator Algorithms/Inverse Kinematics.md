---
type: simulink-block
title: 'Inverse Kinematics'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'inversekinematics'
documentation_source_path: 'ref/inversekinematics.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Kinematics

## 端口

### 输入

### **Pose** — 末端执行器位姿 4×4 齐次变换

末端执行器位姿，指定为 4×4 齐次变换。该变换定义 **End effector** 参数中指定的刚体的期望位置和姿态。

**数据类型：** `single` | `double`

### **Weights** — 位姿容差的权重 六元素向量

位姿容差的权重，指定为六元素向量。向量的前三个元素对应于期望位姿姿态误差的权重。向量的后三个元素对应于期望位姿 *xyz* 位置误差的权重。

**数据类型：** `single` | `double`

### **InitialGuess** — 机器人配置的初始猜测 向量

机器人配置的初始猜测，指定为关节位置向量。位置的数量等于 **Rigid body tree** 参数中非固定关节的数量。使用此初始猜测来帮助引导求解器找到期望的机器人配置。但是，解不保证接近此初始猜测。

**数据类型：** `single` | `double`
### 输出

### **Config** — 机器人配置解 向量

求解期望末端执行器位姿的机器人配置，指定为向量。机器人配置是刚体树模型的关节位置向量。位置的数量等于 **Rigid body tree** 参数中非固定关节的数量。

**数据类型：** `single` | `double`

### **Info** — 求解信息 总线

求解信息，以总线形式返回。求解信息总线包含以下元素：

- `Iterations` — 算法运行的迭代次数。
- `PoseErrorNorm` — 解中末端执行器位姿与期望末端执行器位姿之间误差的大小。
- `ExitFlag` — 提供有关算法执行及导致其返回原因的更多详细信息的代码。有关每种算法类型的退出标志，请参阅 Exit Flags。
- `Status` — 描述解是在容差范围内（`1`）还是算法所能找到的最佳可能解（`2`）的字符向量。

## 参数

### 模块参数

### **Rigid body tree** — 刚体树模型 `twoJointRigidBodyTree`（默认）| `rigidBodyTree` 对象

刚体树模型，指定为 `rigidBodyTree` 对象。在模块掩码中指定之前，请在 MATLAB® 工作区中创建机器人模型。

### **End effector** — 末端执行器名称 `'tool'` | `Select body`

期望位姿的末端执行器名称。要查看 `rigidBodyTree` 对象上的刚体列表，请指定 **Rigid body tree** 参数，然后单击 **Select body**。

### **Show solution diagnostic outputs** — 启用 info 端口 `on`（默认）| `off`

选择以启用 **Info** 端口并获取求解器解的诊断信息。

### 求解器参数

### **Solver** — 求解逆运动学的算法 `BFGS Gradient Projection`（默认）| `Levenberg-Marquardt` | `fminconsqp`

指定用于求解逆运动学的算法，可选 `BFGS Gradient Projection`、`Levenberg-Marquardt` 或 `fminconsqp`。有关每种算法的详细信息，请参阅 Inverse Kinematics Algorithms。

`fminconsqp` 算法需要 Optimization Toolbox™。

### **Enforce joint limits** — 强制刚体树关节限位 `on`（默认）| `off`

选择以强制 **Rigid body tree** 模型中指定的关节限位。

### **Maximum iterations** — 最大迭代次数 `1500`（默认）| 正整数

优化解的最大迭代次数，指定为正整数。增加迭代次数可以改善解，但会增加执行时间。

### **Maximum time** — 运行算法的最大秒数 `10`（默认）| 正标量

将算法运行超时前的最大秒数指定为正标量。增大最大时间可以改善解，但会增加执行时间。

#### 依赖关系

要启用此参数，请将 **Solver** 参数设置为 `BFGS Gradient Projection` 或 `Levenberg-Marquardt`。

### **Gradient tolerance** — 代价函数梯度的阈值 `1e-7`（默认）| 正标量

代价函数梯度的阈值，指定为正标量。如果梯度的幅值低于此阈值，算法将停止。较低的梯度幅值通常表示求解器已收敛到解。

### **Solution tolerance** — 位姿误差的阈值 `1e-6`（默认）| 正标量

由解生成的末端执行器位姿与期望位姿之间误差幅值的阈值，指定为正标量。为位姿的每个分量指定的 `Weights` 包含在此计算中。

### **Step tolerance** — 最小步长 `1e-14`（默认）| 正标量

求解器允许的最小步长，指定为正标量。较小的步长通常意味着解接近收敛。

### **Error change tolerance** — 位姿误差变化的阈值 `1e-12`（默认）| 正标量

迭代之间末端执行器位姿误差变化的阈值，指定为正标量。如果位姿误差所有元素的变化都小于此阈值，算法将返回。

#### 依赖关系

当 **Solver** 为 `Levenberg-Marquardt` 时，此参数启用。

### **Use error damping** — 启用误差阻尼 `on`（默认）| `off`

选中该复选框以启用误差阻尼，然后指定 `Damping bias` 参数。

#### 依赖关系

当 **Solver** 为 `Levenberg-Marquardt` 时，此参数启用。

### **Damping bias** — 代价函数上的阻尼 0.0025（默认）| 正标量

代价函数上的阻尼，指定为正标量。Levenberg-Marquardt 算法具有由该标量控制的阻尼特性，它与代价函数配合以控制收敛速率。

#### 依赖关系

当 **Solver** 为 `Levenberg-Marquardt` 且 **Use error damping** 为 `on` 时，此参数启用。

### **Constraint tolerance** — 约束违反的阈值 `1e-6`（默认）| 非负数值标量

将约束违反的阈值指定为非负数值标量。这表示求解器允许的关节位置限制违反程度。

#### 依赖关系

要启用此参数，请将 **Solver** 参数设置为 `fminconsqp`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码将复用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**Tunable:** No

## 所属库

Robotics System Toolbox / Manipulator Algorithms

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

如果 Inverse Kinematics 模块的 **Maximum time** 参数设置为有限值，则对于包含 Inverse Kinematics 模块的模型，某些硬件板生成的代码可能无法编译。要部署到这些板，请将 **Maximum time** 设置为 `Inf`。

## 版本历史

**在 R2018b 中引入**

### R2025a：`fmincon` 可用作逆运动学求解器算法

逆运动学模块现在支持使用 `fmincon` SQP 求解器作为逆运动学求解器。有关详细信息，请参阅 **Solver** 参数。

此算法需要 Optimization Toolbox。

## 描述

计算关节配置以实现末端执行器位姿

逆运动学模块使用逆运动学（IK）求解器，基于指定的刚体树模型，为期望的末端执行器位姿计算关节配置。使用 `rigidBodyTree` 类为您的机器人创建刚体树模型。刚体树模型定义了求解器强制执行的所有关节约束。

在模块掩码中指定 `RigidBodyTree` 参数和期望的末端执行器。您还可以在 **Solver Parameters** 选项卡中调整算法参数。

输入期望的末端执行器 **Pose**、位姿容差的 **Weights** 以及关节配置的 **InitialGuess**。求解器输出一个机器人配置 **Config**，该配置在 **Solver Parameters** 选项卡中指定的容差范围内满足末端执行器位姿。
