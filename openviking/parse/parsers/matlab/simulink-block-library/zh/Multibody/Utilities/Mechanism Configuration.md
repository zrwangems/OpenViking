---
type: simulink-block
title: 'Mechanism Configuration'
family: 'sm'
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
```yaml
ports:
- name: C
  summary: 用于连接机构框架的端口
  direction: input
- name: g
  summary: 均匀重力物理信号
  direction: input
```

### Frame

### **C** — 用于连接机构框架的端口

用于连接机构的端口。Mechanism Configuration 模块的设置仅适用于该模块所连接的机构。

### 输入

### **g** — 均匀重力物理信号

Mechanism Configuration 模块所连接机构的均匀重力。

#### 依赖关系

要启用此端口，请将 **Uniform Gravity** 设置为 `Time-Varying`。
## 参数
```yaml
parameters:
- name: Uniform Gravity
  summary: 指定重力加速度矢量的方法 Constant（默认）| Time-Varying | None
  group: ''
- name: Gravity
  summary: 恒定重力加速度矢量 [0 0 –9.80665] m/s^2（默认）| 1×3 矢量
  group: ''
- name: Linearization Delta
  summary: 用于线性化的扰动值 0.001（默认）| 正标量
  group: ''
- name: Nonlinear Iterations
  summary: 关节从分离模式过渡到正常模式时的牛顿迭代次数 2（默认）| 正整数
  group: ''
```

#### Uniform Gravity

### **Uniform Gravity** — 指定重力加速度矢量的方法 `Constant`（默认）| `Time-Varying` | `None`

用于计算 Mechanism Configuration 模块所连接机构的均匀重力的方法，指定为以下选项之一：

| 方法 | 描述 |
| --- | --- |
| `Constant` | 使用 **Gravity** 参数指定在空间和时间上保持恒定的重力加速度矢量。 |
| `Time-Varying` | 使用物理端口 **g** 指定在空间上保持恒定但在时间上变化的重力加速度矢量。 |
| `None` | 为机构指定零均匀重力。如果 Simscape Multibody 网络包含 Gravitational Field 模块，则必须使用此选项。 |

### **Gravity** — 恒定重力加速度矢量 [0 0 –9.80665] `m/s^2`（默认）| 1×3 矢量

恒定重力加速度矢量，指定为 1×3 矢量，[*gx* *gy* *gz*]。该模块在机械系统的世界坐标系中解析该矢量。

#### 依赖关系

要启用此参数，请将 **Uniform Gravity** 指定为 `Constant`。

### **Linearization Delta** — 用于线性化的扰动值 0.001（默认）| 正标量

用于在线性化过程中计算数值偏导数的扰动值，指定为正标量。有关线性化的详细信息，请参阅 Linearize Nonlinear Models (Simulink Control Design) 和 `linmod`。

#### Joint Mode Transition

### **Nonlinear Iterations** — 关节从分离模式过渡到正常模式时的牛顿迭代次数 2（默认）| 正整数

当机构具有一个或多个从分离模式过渡到正常模式的关节时，用于求解机构中所有关节位置的牛顿迭代次数，指定为正整数。

当关节从分离模式过渡到正常模式时，如果该关节的位置和方向存在较大偏差，Simscape Multibody 网络可能需要更多的迭代次数来计算机构中所有关节的所需位置，以满足该过渡关节的运动学约束。
## 所属库

Simscape / Multibody / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

机构范围的仿真参数和重力

Mechanism Configuration 模块指定该模块所连接机构的仿真参数和重力。仿真参数包括用于在线性化过程中计算数值偏导数的扰动值以及关节模式过渡的迭代次数。

一个 Simscape™ Multibody™ 网络最多只能有一个 Mechanism Configuration 模块实例。如果模型没有 Mechanism Configuration 模块，则施加到机构上的均匀重力为零。

如果 Simscape Multibody 网络包含 Gravitational Field 模块，请将 Mechanism Configuration 模块的 **Uniform Gravity** 参数设置为 `None`。
