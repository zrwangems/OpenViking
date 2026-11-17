---
type: simulink-block
title: 'Fluid Inertia'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'fluidinertia'
documentation_source_path: 'ref/fluidinertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Fluid Inertia

## 端口

该模块具有以下端口：

`A`
:   与通道入口关联的液压守恒端口。

`B`
:   与通道出口关联的液压守恒端口。

## 参数

**Passage area**
:   流体通道横截面积。默认值为 `8e-5` m^2。

**Passage length**
:   流体通道长度。默认值为 `1` m。

**Initial flow rate**
:   通过通道的初始流量。该参数指定用于在仿真运行开始时计算模块初始状态的初始条件。有关详细信息，请参阅 Initial Conditions Computation。默认值为 `0`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a: 将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）由于流体速度变化而在管或通道两端产生的压差

Fluid Inertia 模块对恒定横截面积的流体通道两端因流体速度变化而产生的压差进行建模。压差根据以下方程确定：

p=ρLAdqdt

其中

|  |  |
| --- | --- |
| *p* | 压差 |
| *ρ* | 流体密度 |
| *L* | 通道长度 |
| *A* | 通道面积 |
| *q* | 流量 |
| *t* | 时间 |

在需要考虑流体惯性的各种管道或通道模型中使用此模块。

模块正方向为从端口 A 到端口 B。这意味着如果流量从 A 流向 B，则流量为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
