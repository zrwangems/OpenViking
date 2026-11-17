---
type: simulink-block
title: 'Local Resistance (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'localresistanceil'
documentation_source_path: 'ref/localresistanceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Resistance (IL)

## 端口

### 守恒

### **A** — 液体端口（isothermal liquid）

管道段的液体入口或出口端口。从端口 **A** 到端口 **B** 的流动为正。

### **B** — 液体端口（isothermal liquid）

管道段的液体入口或出口端口。从端口 **A** 到端口 **B** 的流动为正。

## 参数

### **局部损失参数化** — 损失因子计算方法 `Constant`（默认） | `Tabulated data - loss coefficient vs. Reynolds number`

计算管道段损失因子的方法。损失因子通过管段压降与恒定损失因子之间的线性关系，或通过用户提供的损失因子和 Reynolds 数数据进行插值来参数化。

### **正向流动损失系数（从 A 到 B）** — 从 A 到 B 流动的损失系数 `1`（默认） | positive scalar

与从端口 **A** 到端口 **B** 的流动的压力损失相关联的损失系数。

#### 依赖关系

要启用此参数，请将 **局部损失参数化** 设置为 `Constant`。

### **反向流动损失系数（从 B 到 A）** — 从 B 到 A 流动的损失系数 `1`（默认） | positive scalar

与从端口 **B** 到端口 **A** 的流动的压力损失相关联的损失系数。

#### 依赖关系

要启用此参数，请将 **局部损失参数化** 设置为 `Constant`。

### **Reynolds 数向量** — 用于表格化参数化的 Reynolds 数向量 `[-500, -200, -100, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]`（默认） | 1-by-*n* vector

用于损失系数表格化参数化的 Reynolds 数向量。向量元素必须与 **损失系数向量** 参数中的元素一一对应。元素按升序列出。

#### 依赖关系

要启用此参数，请将 **局部损失参数化** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **损失系数向量** — 用于表格化参数化的损失系数向量 `[.65, .75, .9, 1.15, 1.35, 1.65, 2.3, 3.1, 4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]`（默认） | 1-by-*n* vector

用于损失系数表格化参数化的损失系数向量。向量元素必须与 **Reynolds 数向量** 参数中的元素一一对应。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **局部损失参数化** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **流通面积** — 管段横截面积 `1e-3 m^2`（默认） | positive scalar

管道段的横截面积。

### **临界 Reynolds 数** — 层流的上限 Reynolds 数 `150`（默认） | positive scalar

通过阀门的层流的上限 Reynolds 数。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的管道阻力

Local Resistance (IL) 模块对等温液体系统中由用户定义的管道阻力引起的压力损失进行建模。您可以为通过管道段的正向流动和反向流动指定不同的损失系数。对于管道弯管，您还可以选择使用 Isothermal Liquid 库模块 Pipe Bend (IL) 和 Elbow (IL)；对于面积变化，可使用 Area Change (IL) 模块。

损失因子通过以下任一方式参数化：基于管道压力的恒定关系，或基于 Reynolds 数的用户提供损失系数表格数据。

### 恒定损失因子

对于在一系列流速范围内损失因子保持恒定的管段，按如下公式计算：

kloss=kloss,BA+(kloss,AB−kloss,BA)2[tanh(3ΔpΔpcrit)+1],

其中：

- *k*loss,AB 和
  *k*loss,BA 分别是
  **正向流动损失系数（从 A 到 B）** 和
  **反向流动损失系数（从 B 到 A）**
  参数。
- *Δp* 是压差
  *p*A –
  *p*B。

临界压差
*Δp*crit 是与 **临界 Reynolds 数**
*Re*crit 相关联的压差，*Re*crit 是层流与湍流之间的流态转变点：

Δpcrit=ρ¯2kloss,crit(νRecritDh)2,

其中：

- *k*loss,crit 是与临界压力相关联的损失因子，基于正向和反向损失系数的平均值。
- *ν* 是流体运动黏度。
- ρ¯ 是平均流体密度。
- *D*h 是管段水力直径，即非圆形横截面管道的等效直径：Dh=4Aflowπ，其中 *A*flow 是 **流通面积**。

### 表格化损失系数

损失系数也可以根据用户提供的 Reynolds 数和损失系数数据进行插值。Reynolds 数向量可同时包含正值和负值，分别表示正向流动和反向流动：kloss=TLU(Re)。

### 质量流量

通过阀门的质量守恒：

m˙A+m˙B=0.

通过阀门的质量流量计算如下：

m˙=Aflow2ρ¯klossΔp[Δp2+Δpcrit2]1/4,

其中 *k*loss 是流动损失系数，根据模块流动方向在 **正向流动损失系数（从 A 到 B）** 和 **反向流动损失系数（从 B 到 A）** 之间选择。
