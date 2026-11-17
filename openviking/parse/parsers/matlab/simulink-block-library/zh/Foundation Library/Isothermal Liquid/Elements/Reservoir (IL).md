---
type: simulink-block
title: 'Reservoir (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'reservoiril'
documentation_source_path: 'ref/reservoiril.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (IL)

## 端口

### 输入

### **P** — 压力控制信号，Pa 物理信号

提供储液器压力控制信号的物理信号端口。当该信号的值低于连接到回路的等温液体属性 (IL) 模块所指定的最小有效压力时，信号饱和。

#### 依赖关系

仅当将 **Reservoir type** 参数设置为 `Controlled` 时，此端口才可见。

### 守恒

### **A** — 储液器入口等温液体

与储液器入口关联的等温液体守恒端口。

## 参数

### **Reservoir type** — 指定储液器压力是否可以在仿真期间变化 `Constant`（默认）| `Controlled`

选择储液器压力是否可以在仿真期间变化：

- `Constant` — 储液器压力在仿真期间保持恒定。端口 **P** 隐藏。
- `Controlled` — 端口 **P** 处的输入物理信号指定储液器压力，该压力可以在仿真期间变化。

### **Reservoir pressure specification** — 储液器压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

储液器压力的指定方法：

- `Atmospheric pressure` — 使用连接到回路的等温液体属性 (IL) 模块所指定的大气压力。
- `Specified pressure` — 使用 **Reservoir pressure** 参数指定一个值。

#### 依赖关系

当 **Reservoir type** 参数设置为 `Constant` 时启用。

### **Reservoir pressure** — 储液器中的压力 `0.101325 MPa`（默认）| 正标量

储液器中的期望压力。该压力在仿真期间保持恒定。指定的压力不能大于连接到回路的等温液体属性 (IL) 模块所指定的大气压力。

#### 依赖关系

当 **Reservoir pressure specification** 参数设置为 `Specified pressure` 时启用。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

恒定压力或时变压力下的等温液体储液器

Reservoir (IL) 模块表示一个无限等温液体储液器。使用此模块设置等温液体网络中的边界条件。储液器中的液体可以处于恒定压力下，该压力可以是大气压力或由模块参数指定。您还可以使用物理信号输入端口 **P** 控制储液器内部的压力。端口 **A** 是一个等温液体守恒端口，表示储液器入口。

模块图标根据 **Reservoir type** 和 **Reservoir pressure specification** 参数的值而变化。

| 储液器类型 | 储液器压力指定 | 模块图标 |
| --- | --- | --- |
| `Constant` | `Atmospheric pressure` |  |
| `Specified pressure` |  |
| `Controlled` | |  |

### 假设和限制

- 假设储液器内部的液体体积为无限大。因此，假设流动为准稳态。
- 端口 **A** 与储液器内部之间没有流动阻力。
