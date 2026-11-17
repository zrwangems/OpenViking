---
type: simulink-block
title: 'Mechanism Configuration'
family: 'utilities'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'mechanismconfiguration'
documentation_source_path: 'ref/mechanismconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Mechanism Configuration

## 端口

### 坐标系

### **C** — 用于连接机构坐标系的端口

用于连接机构的端口。Mechanism Configuration 模块的设置仅适用于该模块所连接的机构。

### 输入

### **g** — 均匀重力物理信号

Mechanism Configuration 模块所连接机构的均匀重力。

#### 依赖关系

要启用此端口，请将 **Uniform Gravity** 设置为 `Time-Varying`。

## 参数

#### Uniform Gravity

### **Uniform Gravity** — 用于指定重力加速度向量的方法 `Constant`（默认）| `Time-Varying` | `None`

用于计算 Mechanism Configuration 模块所连接机构的均匀重力的方法，指定为以下选项之一：

| 方法 | 描述 |
| --- | --- |
| `Constant` | 使用 **Gravity** 参数指定在空间和时间上保持恒定的重力加速度向量。 |
| `Time-Varying` | 使用物理端口 **g** 指定在空间上保持恒定但随时间变化的重力加速度向量。 |
| `None` | 为机构指定零均匀重力。如果 Simscape Multibody 网络包含 Gravitational Field 模块，则必须使用此选项。 |

### **Gravity** — 恒定重力加速度向量 [0 0 –9.80665] `m/s^2`（默认）| 1×3 向量

恒定重力加速度向量，指定为 1×3 向量 [*gx* *gy* *gz*]。该模块在机械系统的世界坐标系中解析该向量。

#### 依赖关系

要启用此参数，请将 **Uniform Gravity** 指定为 `Constant`。

### **Linearization Delta** — 用于线性化的扰动值 0.001（默认）| 正标量

用于在线性化期间计算数值偏导数的扰动值，指定为正标量。有关线性化的详细信息，请参阅线性化非线性模型 (Simulink Control Design) 和 `linmod`。

#### 关节模式转换

### **Nonlinear Iterations** — 对于从 disengaged 模式转换到 normal 模式的关节的牛顿迭代次数 2（默认）| 正整数

当机构具有一个或多个从 disengaged 模式转换到 normal 模式的关节时，用于求解机构中所有关节位置的牛顿迭代次数，指定为正整数。

当关节从 disengaged 模式转换到 normal 模式时，如果该关节在其位置和方向上有较大偏差，则 Simscape Multibody 网络可能需要更多迭代次数，才能计算机构中所有关节的所需位置，以满足该转换关节的运动学约束。

## 所属库

Simscape / Multibody / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2012a 中引入**

## 描述

机构范围的重力和仿真参数

Mechanism Configuration 模块指定该模块所连接机构的重力和仿真参数。仿真参数包括用于在线性化期间计算数值偏导数的扰动值以及关节模式转换的迭代次数。

一个 Simscape™ Multibody™ 网络最多可以有一个 Mechanism Configuration 模块实例。如果模型没有 Mechanism Configuration 模块，则施加到该机构的均匀重力为零。

如果 Simscape Multibody 网络包含 Gravitational Field 模块，请将 Mechanism Configuration 模块的 **Uniform Gravity** 参数设置为 `None`。
