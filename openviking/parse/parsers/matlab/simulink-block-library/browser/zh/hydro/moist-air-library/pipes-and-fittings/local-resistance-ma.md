---
type: simulink-block
title: 'Local Resistance (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Pipes and Fittings'
documentation_page: 'localresistancema'
documentation_source_path: 'ref/localresistancema.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Resistance (MA)

## 端口

### 守恒

### **A** — 液体端口湿空气

与管段的入口或出口端口相关联的湿空气守恒端口。流动从端口 **A** 到端口 **B** 为正。

### **B** — 液体端口湿空气

与管段的入口或出口端口相关联的湿空气守恒端口。流动从端口 **A** 到端口 **B** 为正。

## 参数

### **Local loss parametrization** — 损失因子计算方法 `Constant`（默认）| `Tabulated data - loss coefficient vs. Reynolds number`

计算管段损失因子的方法。您可以将损失因子参数化为管段压降与恒定损失因子之间的线性关系，或通过指定损失因子和 Reynolds 数数据进行参数化。

### **Forward flow loss coefficient (from A to B)** — 从端口 A 到 B 流动的损失系数 `1`（默认）| positive scalar

与从端口 **A** 到端口 **B** 的流动的压力损失相关联的损失系数。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Constant`。

### **Reverse flow loss coefficient (from B to A)** — 从端口 B 到 A 流动的损失系数 `1`（默认）| positive scalar

与从端口 **B** 到端口 **A** 的流动的压力损失相关联的损失系数。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Constant`。

### **Reynolds number vector** — 用于表格参数化的 Reynolds 数 `[-500, -200, -100, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]`（默认）| 1-by-*n* vector

用于损失系数表格参数化的 Reynolds 数向量。向量元素必须与 **Loss coefficient vector** 参数中的元素一一对应。按升序列出元素。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Loss coefficient vector** — 用于表格参数化的损失系数 `[.65, .75, .9, 1.15, 1.35, 1.65, 2.3, 3.1, 4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]`（默认）| 1-by-*n* vector

用于损失系数表格参数化的损失系数向量。向量元素必须与 **Reynolds number vector** 参数中的元素一一对应。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Flow area** — 管段横截面积 `1e-3 m^2`（默认）| positive scalar

管段的横截面积。

### **Critical Reynolds number** — 层流的上限 Reynolds 数 `150`（默认）| positive scalar

通过阀门的层流的上限 Reynolds 数。

## 所属库

Simscape / Fluids / Moist Air / Pipes & Fittings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：在湿空气流中模拟悬浮水滴

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的管道阻力

Local Resistance (MA) 模块对湿空气网络中由用户定义的管道阻力引起的压力损失进行建模。您可以为通过管段的正向和反向流动指定不同的损失系数。

您可以将损失因子参数化为基于管道压力的恒定关系，或通过基于 Reynolds 数指定损失系数的表格数据。

### 恒定损失因子

当您将 **Local loss parameterization** 设置为 `Constant` 时，损失在流速范围内保持恒定。损失因子为

kloss=kloss,BA+(kloss,AB−kloss,BA)2[tanh(3ΔpΔpcrit)+1],

其中：

- *kloss,AB* 和
  *kloss,BA* 分别是
  **Forward flow loss coefficient (from A to B)** 和
  **Reverse flow loss coefficient (from B to A)** 参数的值。
- *Δp* 是压差，即 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** 参数 *Recrit* 相关联的压差，该参数是层流和湍流之间的流态转捩点，

Δpcrit=ρ¯2kloss,crit(νRecritDh)2,

其中：

- *kloss,crit* 是与临界压力相关联的损失因子。该值基于正向和反向损失系数的平均值。
- *ν* 是流体运动粘度。
- ρ¯ 是平均流体密度。
- *Dh* 是管段水力直径，即非圆形截面管道的等效直径，Dh=4Aflowπ，其中 *Aflow* 是 **Flow area** 参数的值。

### 表格损失系数

当您将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number` 时，您可以根据 Reynolds 数和损失系数数据插值损失系数。Reynolds 数向量可以同时包含正值和负值，分别表示正向和反向流动：kloss=TLU(Re)。

### 质量流量

该模块守恒质量，使得

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中：

- m˙*B* 是端口 **B** 处的混合物质量流量。
- m˙*wA* 和 m˙*wB* 分别是端口 **A** 和 **B** 处的水蒸气质量流量。
- m˙*gA* 和 m˙*gB* 分别是端口 **A** 和 **B** 处的微量气体质量流量。
- m˙*dA* 和 m˙*dB* 分别是端口 **A** 和 **B** 处的水滴质量流量。

通过阀门的质量流量为

m˙=Aflow2ρ¯klossΔp[Δp2+Δpcrit2]1/4,

其中 *kloss* 是流动损失系数。

### 能量平衡

该模块平衡能量，使得

ΦA+ΦB=0,

其中：

- *ϕA* 是端口 **A** 处的能量流量。
- *ϕB* 是端口 **B** 处的能量流量。
