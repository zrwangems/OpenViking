---
type: simulink-block
title: 'Centrifugal Pump (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Pumps and Motors'
documentation_page: 'centrifugalpumptl'
documentation_source_path: 'ref/centrifugalpumptl.html'
language: zh-CN
chinese_source: worker-translation
---

# Centrifugal Pump (TL)

## 端口

### 守恒

### **A** — 泵入口热液体

与流体关联的热液体守恒端口。

### **B** — 泵出口热液体

与流体关联的热液体守恒端口。

### **R** — 叶轮轴机械旋转

与叶轮轴关联的机械旋转守恒端口。

### **C** — 泵外壳机械旋转

与外壳关联的机械旋转守恒端口。

## 参数

### **Pump parameterization** — 扬程和制动功率参数化 `Capacity, head, and brake power at reference shaft speed`（默认） | `1D tabulated data - head and brake power vs. capacity at reference shaft speed` | `2D tabulated data - head and brake power vs. capacity and shaft speed`

泵扬程和制动功率的参数化，指定为：

- `Capacity, head, and brake power at reference shaft speed` — 使用解析公式参数化泵的增压和轴转矩。
- `1D tabulated data - head and brake power vs. capacity at reference shaft speed` — 根据给定流量下的扬程和制动功率的表格数据来参数化扬程和制动功率。
- `2D tabulated data - head and brake power vs. capacity and shaft speed` — 根据给定流量和轴转速下的扬程和制动功率的表格数据来参数化扬程和制动功率。

### **Nominal capacity** — 泵体积流量 `45` `lpm`（默认） | positive scalar

在参考轴角速度下的额定泵体积流量。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **Nominal head** — 泵扬程 `40` `m`（默认） | positive scalar

在参考轴角速度下，由重力与流体密度归一化的额定泵压差。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **Nominal brake power** — 泵功率 `0.85` `kW`（默认） | positive scalar

在参考角速度下的额定机械轴功率。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **Maximum head at zero capacity** — 无流量时的最大泵扬程 `60` `m`（默认） | positive scalar

在参考角速度下无流量时的最大泵扬程。此参数确定泵上的参考压差，除了 **Nominal capacity**、**Nominal head** 和 **Maximum capacity at zero head** 参数外，模块还使用该压差拟合压力的二次方程。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **Maximum capacity at zero head** — 零扬程时的最大流量 `80` `lpm`（默认） | positive scalar

在参考角速度下零扬程时的最大流体负载。此参数确定泵上的参考压差，除了 **Nominal capacity**、**Nominal head** 和 **Maximum head at zero capacity** 参数外，模块还使用该压差拟合压力的二次方程。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **Reference shaft speed** — 用于相似定律计算的参考轴角速度 `1770` `rpm` | `3500` `rpm` | positive scalar

用于相似定律计算的参考角速度。默认值取决于 **Pump parameterization** 设置。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and break power at reference shaft speed` 或 `1D tabulated data – head and break power vs. capacity at reference shaft speed`。

### **Minimum shaft speed threshold as fraction of reference** — 最小轴转速的阈值 `1e-2`（默认） | positive scalar

最小轴转速相对于参考轴转速的分数形式的阈值。模块使用此值来防止轴转速变为零，从而避免在 *qref* 表达式中出现除以零错误。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and break power at reference shaft speed` 或 `1D tabulated data – head and break power vs. capacity at reference shaft speed`。

### **Reference capacity vector** — 体积流量 `[16.67, 30, 40, 53.33, 66.67, 83.33]` `lpm`（默认） | vector

用于泵扬程或制动功率表格参数化的体积流量向量。此向量中的元素与 **Reference head vector** 和 **Reference brake power vector** 参数中的元素一一对应。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负流量是一种非正常工作条件，可能在某些情况下出现。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **Reference head vector** — 泵扬程向量 `[50, 47.5, 45, 40, 35, 25] m`（默认） | vector

用于泵扬程和制动功率的一维表格参数化的泵扬程值向量。此参数与 **Reference capacity vector** 参数一一对应。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负扬程（即压降）在向量末端处的非正常工作条件下可能出现。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **Reference brake power vector** — 泵制动功率向量 `[.6, .75, .85, .93, .98, .99]` `kW`（默认） | vector

用于泵扬程和制动功率的一维表格参数化的泵制动功率值向量。此参数与 **Reference capacity vector** 参数一一对应。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负制动功率在向量末端处的非正常工作条件下可能出现。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **Capacity vector, q** — 体积排量向量 `[16.67, 23.33, 30, 40, 53.33, 60]` `lpm`（默认） | vector

用于泵扬程表格参数化的体积流量向量。此向量与 **Shaft speed vector, w** 参数一起为二维 **Head table, H (q,w)** 和 **Brake power table, Wb(q,w)** 参数构成一个独立轴。向量元素必须按升序列出。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负流量是一种非正常工作条件，可能在某些情况下出现。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **Shaft speed vector, w** — 角速度向量 `[2450, 2800, 3150, 3500]` `rpm`（默认） | vector

用于泵扬程表格参数化的轴角速度值向量。此向量与 **Capacity vector, q** 参数一起为二维 **Head table, H (q,w)** 和 **Brake power table, Wb(q,w)** 参数构成一个独立轴。向量元素必须按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **Head table, H(q,w)** — 泵扬程矩阵 `[25, 32.7, 42.5, 50; 24, 31.7, 41, 49; 22.7, 30.5, 39, 47.5; 20, 28, 36, 45; 15.7, 24, 32, 40; 12.5, 21, 29.5, 37.5]` `m`（默认） | *M*-by-*N* matrix

指定体积流量和角速度下的泵扬程值的 *M*-by-*N* 矩阵。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负扬程（即压降）在表格底部处的非正常工作条件下可能出现。模块在表格元素之间采用线性插值。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Capacity vector, q** 参数中的元素数量。
- *N* 是 **Shaft speed vector, w** 参数中的元素数量。所有行必须严格按升序排列。

如果您的表格中有未知数据点，请在这些值的位置使用 `NaN`。模块通过基于泵曲线平均斜率的推断来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲泵行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Head table, H(q,w)** 和 **Brake power table, Wb(q,w)** 参数中 `NaN` 元素的位置必须匹配。
- `NaN` 元素必须位于表格的左下部分，这对应于最高流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **Brake power table, Wb(q,w)** — 泵制动功率矩阵 `[.28, .38, .5, .6; .31, .41, .55, .68; .33, .44, .6, .75; .36, .48, .65, .83; .38, .53, .72, .93; .39, .55, .75, .97]` `kW`（默认） | *M*-by-*N* matrix

指定体积流量和角速度下的泵制动功率值的 *M*-by-*N* 矩阵。在正常工作条件下，这些值为非负值，但模块确实接受负值。在表格元素之间采用线性插值。*M* 和 *N* 是对应向量的长度：

- *M* 是 **Capacity vector, q** 参数中的向量元素数量。
- *N* 是 **Shaft speed vector, w** 参数中的向量元素数量。所有行必须严格按升序排列。

如果您的表格中有未知数据点，请在这些值的位置使用 `NaN`。模块通过基于泵曲线平均斜率的推断来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲泵行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Head table, H(q,w)** 和 **Brake power table, Wb(q,w)** 参数中 `NaN` 元素的位置必须匹配。
- `NaN` 元素必须位于表格的左下部分，这对应于最高流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **Reference density** — 所列泵性能数据的流体密度 `998` `kg/m^3`（默认） | positive scalar

泵性能数据的参考流体密度。参考文档或数据表通常会指定此值。此参数用于在不同流体之间缩放泵性能。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed` 或 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **Impeller diameter scale factor** — 用于相似定律计算的模型直径与参考直径之比 `1`（默认） | positive scalar

用于相似定律计算的模型直径与参考直径之比。如果您的参考叶轮直径与系统叶轮直径不同（例如测试泵缩放时），请修改此值。对于小于参考泵的系统泵，使用小于 1 的值。对于大于参考泵的系统泵，使用大于 1 的值。模块不会对因泵尺寸变化引起的泵效率变化进行建模。

### **Mechanical orientation** — 轴正常旋转方向 `Positive angular velocity of port R relative to port C corresponds to normal pump operation`（默认） | `Negative angular velocity of port R relative to port C corresponds to normal pump operation`

从端口 **A** 流向 **B** 的轴旋转方向。

### **Check if operating beyond normal pump operation** — 当模块超出运行边界时发出通知的选项 `None`（默认） | `Warning` | `Error`

用于在模块运行于正常泵边界之外时发出通知的选项。当通过泵的流量为负或超过泵的最大流量时，会出现这种情况。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **Cross-sectional area at ports A and B** — 泵入口和出口处的流通面积 `0.01` `m^2`（默认） | positive scalar

泵入口和出口处的流通面积。模块假定这些面积相等。

## 所属库

Simscape / Fluids / Thermal Liquid / Pumps & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023a: 公开低轴转速阈值

使用 **Minimum shaft speed threshold as fraction of reference** 参数以参考轴转速的分数形式控制最小轴转速阈值。当 **Pump parameterization** 参数为 `Capacity, head, and break power at reference shaft speed` 或 `1D tabulated data – head and break power vs. capacity at reference shaft speed` 时，模块中提供 **Minimum shaft speed threshold as fraction of reference** 参数。

### R2022b: 将性能扩展到正常工作条件之外

一维和二维参数化现在都允许负值。当仿真超出所提供表格的范围时，模块会基于泵曲线的平均斜率外推泵扬程。

现在可以在泵数据不可用的位置使用 `NaN` 元素。以下二维表格参数支持表格左下部分的连续 `NaN` 元素：

- **Head table H(q,w)**
- **Brake power table, Wb(q,w)**

对于每个模块，如果轴按与指定机械方向相反的方向旋转，则模块两端的压差降至零，结果可能不准确。

## 描述

热液体网络中的离心泵

Centrifugal Pump (TL) 模块表示离心泵，它将能量从轴传递到热液体网络中的流体。压差和机械转矩是泵扬程和制动功率的函数，而泵扬程和制动功率取决于泵流量。您可以通过解析方式或通过表格数据的线性插值来参数化泵。泵相似定律定义了模块的核心物理特性，它按泵角速度和叶轮直径的当前值与参考值之比来缩放泵性能。

默认情况下，流动和压力增益从端口 **A** 到端口 **B**。端口 **C** 表示泵外壳，端口 **R** 表示泵轴。您可以在 **Mechanical orientation** 参数中指定正常运行轴方向。如果轴开始沿相反方向旋转，则泵两端的压差降至零。

离心泵示意图

### 解析参数化

当您将 **Pump parameterization** 设置为
`Capacity, head, and brake power at reference shaft
speed` 时，模块根据泵相似定律和参考压差计算泵上的压力增益

pB−pA=ΔHrefρg(ωωref)2(DDref)2,

其中：

- *ΔHref* 是参考泵扬程，模块通过对 **Maximum head at zero
  capacity**、**Nominal head** 和
  **Maximum capacity at zero head**
  参数的值之间的泵压差进行二次拟合得到该值。
- *ω* 是轴角速度，其中
  *ω* = *ωR*
  – *ωC*。
- *ωref* 是
  **Reference shaft speed** 参数的值。
- DDref 是 **Impeller diameter scale
  factor** 参数的值。模块不反映因泵尺寸变化而引起的泵效率变化。
- *ρ* 是网络流体密度。

轴转矩为

τ=Wbrake,refω2ωref3(DDref)5.

模块将参考制动功率
*Wbrake,ref* 计算为流量·扬程/效率。泵效率曲线为二次曲线，其峰值对应于
**Nominal brake power** 参数。当流量为零或最大时，泵效率曲线降至零。

模块将参考流量计算为

qref=m˙ρωrefω(DrefD)3.

如果 **Check if operating beyond normal pump
operation** 参数为 `Warning`，则当模块流量变为负值或超过最大泵流量时，模块返回警告。

### 1-D 表格数据参数化

当您将 **Pump parameterization** 设置为 `1D
tabulated data - head and brake power vs. capacity at reference shaft
speed` 时，泵上的压力增益是
**Reference head vector** 参数
*ΔHref* 的函数，而 *ΔHref* 是
参考流量 *qref* 的函数

Δp=ρgΔHref(qref)(ωωref)2(DDref)2,

其中 *g* 是重力加速度。

模块将轴转矩基于 **Reference brake power
vector** 参数 *Wref*，
该参数是参考流量的函数

τ=Wref(qref)ω2ωref3(ρρref)(DDref)5,

其中 *ρref* 是
**Reference density** 参数的值。参考流量为

qref=m˙ρ(ωrefω)(DrefD)3,

模块使用该值来插值
**Reference capacity vector**、**Reference head
vector** 和 **Reference brake power vector**
参数的值，作为 *qref* 的函数。

当仿真超出所提供表格的范围时，模块基于泵曲线的平均斜率和制动功率外推扬程至最近点。

### 2-D 表格数据参数化

当您将 **Pump parameterization** 设置为 `2D
tabulated data - head and brake power vs. capacity and shaft
speed` 时，泵上的压力增益是
**Head table, H(q,w)** 参数
*ΔHref* 的函数，而 *ΔHref* 是
参考流量 *qref* 和轴转速 *ω*
的函数

Δp=ρgΔHref(qref,ω)(DDref)2.

轴转矩是 **Brake power
table, Wb(q,w)** 参数
*Wref* 的函数，而 *Wref* 是
参考流量 *qref* 和轴转速 *ω*
的函数

τ=Wref(qref,ω)ω(ρρref)(DDref)5.

参考流量为

qref=m˙ρ(DrefD)3.

当仿真超出所提供表格的范围时，模块基于泵曲线的平均斜率和制动功率外推扬程至最近点。

**缺失数据**

如果您的表格中有未知数据点，请在
**Head table, H(q,w)** 和 **Brake power table,
Wb(q,w)** 参数中使用 `NaN` 代替这些值。模块通过基于泵曲线平均斜率进行外推来填充
`NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲泵行为。使用未知数据时：

- 表格中的 `NaN` 元素必须
  连续。
- **Head table, H(q,w)** 和 **Brake
  power table, Wb(q,w)** 参数中
  `NaN` 元素的位置必须匹配。
- `NaN` 元素必须位于表格的
  左下部分，这对应于最高
  流量和最低轴转速。

### 可视化泵曲线

您可以通过绘制扬程、功率、效率和转矩随流量变化的曲线来检查参数化后的泵性能。要生成当前泵设置的图，请右键单击模块并选择 **Fluids** > **Plot Pump Characteristics**。如果您更改了设置或数据，请在模块参数上点击 **Apply**，并在泵曲线图上点击 **Reload Data**。

默认模块参数化会创建这些图：

泵特性曲线图

### 能量平衡

机械功是能量从轴交换到流体的结果。控制能量平衡方程为

ϕA+ϕB+Phydro=0,

其中：

- *ΦA* 是端口 **A** 处的能量流率。
- *ΦB* 是端口 **B** 处的能量流率。

泵液压功率是泵端口之间压差的函数

Phydro=Δpm˙ρ.

### 假设和限制

- 如果轴旋转方向与 **Mechanical
  orientation** 参数的设置相反，则模块两端的压差降至零，结果可能不准确。
- 模块不考虑泵中的动压。模块仅考虑由静压产生的泵扬程。
