---
type: simulink-block
title: 'Reservoir (IL)'
family: 'isothermal-liquid'
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

物理信号端口，提供储液罐压力控制信号。当该信号的值降至连接到回路的 Isothermal Liquid Properties (IL) 模块指定的最小有效压力以下时，信号饱和。

#### 依赖关系

仅当您将 **Reservoir type** 参数设置为 `Controlled` 时，此端口才可见。

### 守恒

### **A** — 储液罐入口等温液体

与储液罐入口关联的等温液体守恒端口。

## 参数

### **Reservoir type** — 指定储液罐压力是否可以在仿真期间变化 `Constant` (default) | `Controlled`

选择储液罐压力是否可以在仿真期间变化：

- `Constant` — 储液罐压力在仿真期间保持恒定。端口 **P** 隐藏。
- `Controlled` — 端口 **P** 处的输入物理信号指定储液罐压力，该压力可以在仿真期间变化。

### **Reservoir pressure specification** — 储液罐压力的指定方法 `Atmospheric pressure` (default) | `Specified pressure`

储液罐压力的指定方法：

- `Atmospheric pressure` — 使用连接到回路的 Isothermal Liquid Properties (IL) 模块指定的大气压。
- `Specified pressure` — 通过使用 **Reservoir pressure** 参数指定一个值。

#### 依赖关系

当 **Reservoir type** 参数设置为 `Constant` 时启用。

### **Reservoir pressure** — 储液罐中的压力 `0.101325 MPa` (default) | positive scalar

储液罐中的所需压力。该压力在仿真期间保持恒定。指定的压力不能大于连接到回路的 Isothermal Liquid Properties (IL) 模块指定的大气压。

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

恒压或时变压力的等温液体储液罐

Reservoir (IL) 模块表示等温液体的无限储液罐。使用此模块可设置等温液体网络中的边界条件。储液罐中的液体可处于恒定压力，该压力可以是大气压，也可以由模块参数指定。您还可以通过使用物理信号输入端口 **P** 控制储液罐内的压力。端口 **A** 是等温液体守恒端口，表示储液罐入口。

模块图标会根据 **Reservoir type** 和 **Reservoir pressure specification** 参数的值而变化。

| Reservoir Type | Reservoir Pressure Specification | 模块图标 |
| --- | --- | --- |
| `Constant` | `Atmospheric pressure` |  |
| `Specified pressure` |  |
| `Controlled` | |  |

### 假设和限制

- 假设储液罐内液体的体积无限大。因此，假设流动为准稳态。
- 端口 **A** 与储液罐内部之间没有流动阻力。
