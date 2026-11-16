---
type: simulink-block
title: 'Local Resistance (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'localresistancetl'
documentation_source_path: 'ref/localresistancetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Resistance (TL)

## 端口

### 守恒

### **A** — 液体端口 thermal liquid

与管段入口或出口关联的 Thermal liquid 守恒端口。流动从端口 **A** 到端口 **B** 为正。

### **B** — 液体端口 thermal liquid

与管段入口或出口关联的 Thermal liquid 守恒端口。流动从端口 **A** 到端口 **B** 为正。

## 参数

### **Local loss parametrization** — 损失因子计算方法 `Constant`（默认） | `Tabulated data - loss coefficient vs. Reynolds number`

计算管段损失因子的方法。损失因子通过管段压降与恒定损失因子之间的线性关系进行参数化，或通过用户提供的损失因子和 Reynolds 数数据进行插值参数化。

### **Forward flow loss coefficient (from A to B)** — 从 A 到 B 流动的损失系数 `1`（默认） | positive scalar

与从端口 **A** 到端口 **B** 的流动压力损失相关的损失系数。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Constant`。

### **Reverse flow loss coefficient (from B to A)** — 从 B 到 A 流动的损失系数 `1`（默认） | positive scalar

与从端口 **B** 到端口 **A** 的流动压力损失相关的损失系数。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Constant`。

### **Reynolds number vector** — 用于表格化参数化的 Reynolds 数向量 `[-500, -200, -100, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]`（默认） | 1-by-*n* vector

用于损失系数表格化参数化的 Reynolds 数向量。向量元素必须与 **Loss coefficient vector** 参数中的元素一一对应。元素按升序列出。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Loss coefficient vector** — 用于表格化参数化的损失系数向量 `[.65, .75, .9, 1.15, 1.35, 1.65, 2.3, 3.1, 4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]`（默认） | 1-by-*n* vector

用于损失系数表格化参数化的损失系数向量。向量元素必须与 **Reynolds number vector** 参数中的元素一一对应。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Flow area** — 管段横截面积 `1e-3 m^2`（默认） | positive scalar

管段的横截面积。

### **Critical Reynolds number** — 层流的上限 Reynolds 数 `150`（默认） | positive scalar

通过阀门的层流的上限 Reynolds 数。

## 所属库

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

热液体网络中的管道阻力

Local Resistance (TL) 模块表示热液体网络中由用户定义的管道阻力导致的压力损失。可以为通过管段的正向和反向流动指定不同的损失系数。对于管道弯头，也可以选择使用 Thermal Liquid 库模块 Pipe Bend (TL) 和 Elbow (TL)，或者对于面积变化，使用 Sudden Area Change (TL) 模块。

损失因子可以通过基于管道压力的恒定关系进行参数化，或者通过基于 Reynolds 数的用户提供损失系数表格数据进行参数化。

### 恒定损失因子

对于损失因子在一系列流速范围内保持恒定的管段，按下式计算：

kloss=kloss,BA+(kloss,AB−kloss,BA)2[tanh(3ΔpΔpcrit)+1],

其中：

- *k*loss,AB 和 *k*loss,BA 分别是 **Forward flow loss coefficient (from A to B)** 和 **Reverse flow loss coefficient (from B to A)** 参数。
- *Δp* 是压力差 *p*A – *p*B。

临界压力差 *Δp*crit 是与 **Critical Reynolds number**、*Re*crit 相关的压力差，其中 *Re*crit 是层流和湍流之间的流态转捩点：

Δpcrit=ρ¯2kloss,crit(νRecritDh)2,

其中：

- *k*loss,crit 是与临界压力相关的损失因子，并基于正向和反向损失系数的平均值。
- *ν* 是流体运动黏度。
- ρ¯ 是平均流体密度。
- *D*h 是管段水力直径，即非圆形截面管道的等效直径：Dh=4Aflowπ，其中 *A*flow 是 **Flow area**。

### 表格化损失系数

损失系数也可以根据用户提供的 Reynolds 数和损失系数数据进行插值。Reynolds 数向量可以同时包含正值和负值，分别表示正向和反向流动：kloss=TLU(Re)。

### 质量流量

通过阀门的质量守恒：

m˙A+m˙B=0.

通过阀门的质量流量按下式计算：

m˙=Aflow2ρ¯klossΔp[Δp2+Δpcrit2]1/4,

其中 *k*loss 是流动损失系数，根据模块流动方向在 **Forward flow loss coefficient (from A to B)** 和 **Reverse flow loss coefficient (from B to A)** 之间选择。

### 能量平衡

该模块对能量进行平衡，使得

ΦA+ΦB=0,

其中：

- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。
