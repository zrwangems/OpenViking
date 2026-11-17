---
type: simulink-block
title: 'Centrifugal Pump (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Fluid Machines'
documentation_page: 'centrifugalpump2p'
documentation_source_path: 'ref/centrifugalpump2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Centrifugal Pump (2P)

## 端口
```yaml
ports:
- name: A
  summary: 泵入口两相流体
  direction: conserving
- name: B
  summary: 泵出口两相流体
  direction: conserving
- name: R
  summary: 叶轮轴机械旋转
  direction: conserving
- name: C
  summary: 泵壳体机械旋转
  direction: conserving
```

### 守恒端口

### **A** — 泵入口两相流体

与流体相关的两相流体守恒端口。

### **B** — 泵出口两相流体

与流体相关的两相流体守恒端口。

### **R** — 叶轮轴机械旋转

与叶轮轴相关的机械旋转守恒端口。

### **C** — 泵壳体机械旋转

与壳体相关的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Pump parameterization
  summary: 扬程和制动功率参数化 Capacity, head, and brake power at reference shaft speed（默认）| 1D 表格数据 - 参考轴转速下的扬程与制动功率对比流量 speed | 2D
    表格数据 - 扬程与制动功率对比流量与轴转速 speed
  group: ''
- name: Nominal capacity
  summary: 泵体积流量 45 lpm（默认）| 正标量
  group: ''
- name: Nominal head
  summary: 泵扬程 40 m（默认）| 正标量
  group: ''
- name: Nominal brake power
  summary: 泵功率 0.85 kW（默认）| 正标量
  group: ''
- name: Maximum head at zero capacity
  summary: 零流量时的最大泵扬程 60 m（默认）| 正标量
  group: ''
- name: Maximum capacity at zero head
  summary: 零扬程时的最大流量 80 lpm（默认）| 正标量
  group: ''
- name: Reference shaft speed
  summary: 用于相似定律计算的参考轴角速度 1770 rpm | 3500 rpm | 正标量
  group: ''
- name: Minimum shaft speed threshold as fraction of reference
  summary: 最小轴转速阈值 1e-2（默认）| 正标量
  group: ''
- name: Reference capacity vector
  summary: 体积流量 [16.67, 30, 40, 53.33, 66.67, 83.33] lpm（默认）| 向量
  group: ''
- name: Reference head vector
  summary: 泵扬程向量 [50, 47.5, 45, 40, 35, 25] m（默认）| 向量
  group: ''
- name: Reference brake power vector
  summary: 泵制动功率向量 [.6, .75, .85, .93, .98, .99] kW（默认）| 向量
  group: ''
- name: Capacity vector, q
  summary: 体积排量向量 [16.67, 23.33, 30, 40, 53.33, 60] lpm（默认）| 向量
  group: ''
- name: Shaft speed vector, w
  summary: 角速度向量 [2450, 2800, 3150, 3500] rpm（默认）| 向量
  group: ''
- name: Head table, H(q,w)
  summary: 泵扬程矩阵 [25, 32.7, 42.5, 50; 24, 31.7, 41, 49; 22.7, 30.5, 39, 47.5; 20, 28, 36, 45; 15.7, 24, 32, 40; 12.5, 21,
    29.5, 37.5] m（默认）| *M*×*N* 矩阵
  group: ''
- name: Brake power table, Wb(q,w)
  summary: 泵制动功率矩阵 [.28, .38, .5, .6; .31, .41, .55, .68; .33, .44, .6, .75; .36, .48, .65, .83; .38, .53, .72, .93; .39,
    .55, .75, .97] kW（默认）| *M*×*N* 矩阵
  group: ''
- name: Reference density
  summary: 所列泵性能数据的流体密度 998 kg/m^3（默认）| 正标量
  group: ''
- name: Impeller diameter scale factor
  summary: 用于相似定律计算的模型直径与参考直径之比 1（默认）| 正标量
  group: ''
- name: Mechanical orientation
  summary: 轴正常旋转方向 Positive angular velocity of port R relative to port C corresponds to normal pump operation（默认）| Negative
    angular velocity of port R relative to port C corresponds to normal pump operation
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 泵入口和出口处的流通面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Report when fluid is not fully liquid
  summary: 流体非完全液体时的通知 Warning（默认）| None | Error
  group: ''
- name: Check if operating beyond normal pump operation
  summary: 当模块超出运行边界时通知的选项 None（默认）| Warning | Error
  group: ''
```

### **Pump parameterization** — 扬程和制动功率参数化 `Capacity, head, and brake power at reference shaft speed`（默认）| `1D 表格数据 - 参考轴转速下的扬程与制动功率对比流量 speed` | `2D 表格数据 - 扬程与制动功率对比流量与轴转速 speed`

泵扬程和制动功率的参数化方式，指定为：

- `Capacity, head, and brake power at reference
  shaft speed` — 使用解析公式对泵压升和轴扭矩进行参数化。
- `一维表格数据 - 扬程与制动功率对比
  capacity at reference shaft speed` —
  根据给定流量下的扬程和制动功率表格数据对扬程和制动功率进行参数化。
- `二维表格数据 - 扬程与制动功率对比
  capacity and shaft speed` — 根据给定流量和轴转速下的扬程和制动功率表格数据对扬程和制动功率进行参数化。

### **Nominal capacity** — 泵体积流量 `45` `lpm`（默认）| 正标量

参考轴角速度下的额定泵体积流量。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
brake power at reference shaft speed`。

### **Nominal head** — 泵扬程 `40` `m`（默认）| 正标量

参考轴角速度下的额定泵压差，已按重力和流体密度归一化。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
brake power at reference shaft speed`。

### **Nominal brake power** — 泵功率 `0.85` `kW`（默认）| 正标量

参考角速度下的额定机械轴功率。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
brake power at reference shaft speed`。

### **Maximum head at zero capacity** — 零流量时的最大泵扬程 `60` `m`（默认）| 正标量

参考角速度下零流量时的最大泵扬程。此参数确定泵的参考压差，模块除使用 **Nominal capacity**、**Nominal
head** 和 **Maximum capacity at zero head**
参数外，还使用该压差拟合压力的二次方程。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
brake power at reference shaft speed`。

### **Maximum capacity at zero head** — 零扬程时的最大流量 `80` `lpm`（默认）| 正标量

参考角速度下零扬程时的最大流体负载。此参数确定泵的参考压差，模块除使用 **Nominal capacity**、**Nominal
head** 和 **Maximum head at zero capacity**
参数外，还使用该压差拟合压力的二次方程。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
brake power at reference shaft speed`。

### **Reference shaft speed** — 用于相似定律计算的参考轴角速度 `1770` `rpm` | `3500` `rpm` | 正标量

用于相似定律计算的参考角速度。默认值取决于 **Pump parameterization**
设置。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
break power at reference shaft speed` 或
`一维表格数据 – 扬程与制动功率对比流量
at reference shaft speed`。

### **Minimum shaft speed threshold as fraction of reference** — 最小轴转速阈值 `1e-2`（默认）| 正标量

最小轴转速相对于参考轴转速的分数阈值。模块使用此值防止轴转速变为零，从而导致
*qref* 表达式中的除零错误。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `Capacity, head, and
break power at reference shaft speed` 或
`一维表格数据 – 扬程与制动功率对比流量
at reference shaft speed`。

### **Reference capacity vector** — 体积流量 `[16.67, 30, 40, 53.33, 66.67, 83.33]` `lpm`（默认）| 向量

用于泵扬程或制动功率表格参数化的体积流量向量。此向量中的元素与
**Reference head vector** 和
**Reference brake power vector** 参数中的元素一一对应。在正常工作条件下，此参数中的元素为非负值，但模块也接受负值。负流量是一种非正常工作条件，可能在某些情况下出现。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `1D tabulated data - head
and brake power vs. capacity at reference shaft
speed`。

### **Reference head vector** — 泵扬程向量 `[50, 47.5, 45, 40, 35, 25] m`（默认）| 向量

用于泵扬程和制动功率一维表格参数化的泵扬程值向量。此参数与
**Reference capacity vector** 参数一一对应。在正常工作条件下，此参数中的元素为非负值，但模块也接受负值。在向量末端的非正常工作条件下，可能出现负扬程或压降。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `1D tabulated data - head
and brake power vs. capacity at reference shaft
speed`。

### **Reference brake power vector** — 泵制动功率向量 `[.6, .75, .85, .93, .98, .99]` `kW`（默认）| 向量

用于泵扬程和制动功率一维表格参数化的泵制动功率值向量。此参数与
**Reference capacity vector** 参数一一对应。在正常工作条件下，此参数中的元素为非负值，但模块也接受负值。在向量末端的非正常工作条件下，可能出现负制动功率。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `1D tabulated data - head
and brake power vs. capacity at reference shaft
speed`。

### **Capacity vector, q** — 体积排量向量 `[16.67, 23.33, 30, 40, 53.33, 60]` `lpm`（默认）| 向量

用于泵扬程表格参数化的体积流量向量。此向量与 **Shaft
speed vector, w** 参数构成独立轴，用于二维 **Head table,
H (q,w)** 和 **Brake power table, Wb(q,w)**
参数。向量元素必须按升序排列。在正常工作条件下，此参数中的元素为非负值，但模块也接受负值。负流量是一种非正常工作条件，可能在某些情况下出现。

#### 依赖关系

要启用此参数，请将 **Pump
parameterization** 设置为 `2D tabulated data - head
and brake power vs. capacity and shaft speed`。

### **Shaft speed vector, w** — 角速度向量 `[2450, 2800, 3150, 3500]` `rpm`（默认）| 向量

用于泵扬程表格参数化的轴角速度值向量。此向量与
**Capacity vector, q** 参数构成独立轴，用于二维
**Head table, H (q,w)** 和 **Brake power
table, Wb(q,w)** 参数。向量元素必须按升序排列，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D 表格数据 - 扬程与制动功率对比流量与轴转速 speed`。

### **Head table, H(q,w)** — 泵扬程矩阵 `[25, 32.7, 42.5, 50; 24, 31.7, 41, 49; 22.7, 30.5, 39, 47.5; 20, 28, 36, 45; 15.7, 24, 32, 40; 12.5, 21, 29.5, 37.5]` `m`（默认）| *M*×*N* 矩阵

在指定体积流量和角速度下的泵扬程值的 *M*×*N* 矩阵。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负扬程（即压降）在表格底部的非正常工作条件下是可能的。模块在表格元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Capacity vector, q** 参数中的元素个数。
- *N* 是 **Shaft speed vector, w** 参数中的元素个数。所有行必须严格按升序排列。

如果表格中有未知数据点，请使用 `NaN` 代替这些值。模块根据泵曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人为的数值，因为这些值会在该区域运行时扭曲泵的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须是连续的。
- **Head table, H(q,w)** 和 **Brake power table, Wb(q,w)** 参数中 `NaN` 元素的位置必须匹配。
- `NaN` 元素必须位于表格的左下部分，这对应于最高容量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D 表格数据 - 扬程与制动功率对比流量与轴转速 speed`。

### **Brake power table, Wb(q,w)** — 泵制动功率矩阵 `[.28, .38, .5, .6; .31, .41, .55, .68; .33, .44, .6, .75; .36, .48, .65, .83; .38, .53, .72, .93; .39, .55, .75, .97]` `kW`（默认）| *M*×*N* 矩阵

在指定体积流量和角速度下的泵制动功率值的 *M*×*N* 矩阵。在正常工作条件下这些值为非负值，但模块确实接受负值。表格元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Capacity vector, q** 参数中的向量元素个数。
- *N* 是 **Shaft speed vector, w** 参数中的向量元素个数。所有行必须严格按升序排列。

如果表格中有未知数据点，请使用 `NaN` 代替这些值。模块根据泵曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人为的数值，因为这些值会在该区域运行时扭曲泵的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须是连续的。
- **Head table, H(q,w)** 和 **Brake power table, Wb(q,w)** 参数中 `NaN` 元素的位置必须匹配。
- `NaN` 元素必须位于表格的左下部分，这对应于最高容量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `2D 表格数据 - 扬程与制动功率对比流量与轴转速 speed`。

### **Reference density** — 所列泵性能数据的流体密度 `998` `kg/m^3`（默认）| 正标量

泵性能数据的参考流体密度。参考值或数据表通常会指定此值。此参数在不同流体之间缩放泵性能。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `1D 表格数据 - 参考轴转速下的扬程与制动功率对比流量 speed` 或 `2D 表格数据 - 扬程与制动功率对比流量与轴转速 speed`。

### **Impeller diameter scale factor** — 用于相似定律计算的模型直径与参考直径之比 `1`（默认）| 正标量

用于相似定律计算的模型直径与参考直径之比。如果参考叶轮直径与系统叶轮直径之间存在差异（例如在测试泵缩放时），请修改此值。对于小于参考泵的系统泵，使用小于一的值。对于大于参考泵的系统泵，使用大于一的值。模块不建模因泵尺寸变化引起的泵效率变化。

### **Mechanical orientation** — 轴正常旋转方向 `Positive angular velocity of port R relative to port C corresponds to normal pump operation`（默认）| `Negative angular velocity of port R relative to port C corresponds to normal pump operation`

从端口 **A** 流向 **B** 时的轴旋转方向。

### **Cross-sectional area at ports A and B** — 泵入口和出口处的流通面积 `0.01` `m^2`（默认）| 正标量

泵入口和出口处的流通面积。模块假定这些面积相等。

### **Report when fluid is not fully liquid** — 流体非完全液体时的通知 `Warning`（默认）| `None` | `Error`

当蒸汽质量分数大于 0（表示流体非完全液体）时，模块是不执行任何操作、生成警告还是生成错误。

### **Check if operating beyond normal pump operation** — 当模块超出运行边界时通知的选项 `None`（默认）| `Warning` | `Error`

当模块在正常泵边界之外运行时通知的选项。这种情况发生在通过泵的流量为负值或超出泵的最大容量时。

#### 依赖关系

要启用此参数，请将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed`。
## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

两相流体网络中的离心泵

Centrifugal Pump (2P) 模块表示一个离心泵，它将能量从轴传递到两相流体网络中的流体。压差和机械扭矩是泵扬程和制动功率的函数，而泵扬程和制动功率取决于泵容量。您可以通过解析方式或通过对表格数据进行线性插值来参数化泵。泵相似定律定义了模块的核心物理特性，它通过当前值与参考值的比值来缩放泵性能，这些参考值包括泵角速度和叶轮直径。

默认情况下，流量和压力增益从端口 **A** 到端口 **B**。端口 **C** 表示泵壳体，端口 **R** 表示泵轴。您可以在 **Mechanical orientation** 参数中指定正常的轴运行方向。如果轴开始反向旋转，泵两端的压差降至零。

离心泵示意图

### 解析参数化

当您将 **Pump parameterization** 设置为 `Capacity, head,
and brake power at reference shaft speed` 时，模块根据泵相似定律和参考压差计算泵的压力增益

pB−pA=ΔHrefρg(ωωref)2(DDref)2，

其中：

- *ΔHref* 是参考泵扬程，模块通过 **Maximum head at zero
  capacity**、**Nominal head** 和
  **Maximum capacity at zero head**
  参数值之间的泵压差二次拟合得出。
- *ω* 是轴角速度，其中
  *ω* = *ωR*
  – *ωC*。
- *ωref* 是
  **Reference shaft speed** 参数的值。
- DDref 是 **Impeller diameter scale
  factor** 参数的值。模块不反映因泵尺寸变化引起的泵效率变化。
- *ρ* 是网络流体密度。

轴扭矩为

τ=Wbrake,refω2ωref3(DDref)5。

模块将参考制动功率
*Wbrake,ref* 计算为容量·扬程/效率。泵效率曲线为二次曲线，其峰值对应
**Nominal brake power** 参数。当容量为零或最大时，泵效率曲线降为零。

模块将参考容量计算为

qref=m˙ρωrefω(DrefD)3。

如果 **Check if operating beyond normal pump
operation** 参数为 `Warning`，当模块流量变为负值或超过最大泵容量时，模块返回警告。

### 一维表格数据参数化

当您将 **Pump parameterization** 设置为 `1D
表格数据 - 参考轴转速下的扬程与制动功率对比流量
speed` 时，泵的压力增益是
**Reference head vector** 参数
*ΔHref* 的函数，而该参数是参考容量 *qref* 的函数

Δp=ρgΔHref(qref)(ωωref)2(DDref)2，

其中 *g* 是重力加速度。

模块将轴扭矩基于 **Reference brake power
vector** 参数 *Wref*，
该参数是参考容量的函数

τ=Wref(qref)ω2ωref3(ρρref)(DDref)5，

其中 *ρref* 是
**Reference density** 参数的值。参考容量为

qref=m˙ρ(ωrefω)(DrefD)3，

模块使用该值对
**Reference capacity vector**、**Reference head
vector** 和 **Reference brake power vector**
参数的值进行插值，作为 *qref* 的函数。

当仿真超出所提供表格的范围时，模块根据泵曲线的平均斜率和制动功率外推扬程至最近点。

### 二维表格数据参数化

当您将 **Pump parameterization** 设置为 `2D
表格数据 - 扬程与制动功率对比流量与轴转速
speed` 时，泵的压力增益是
**Head table, H(q,w)** 参数
*ΔHref* 的函数，而该参数是参考容量 *qref* 和轴速度 *ω* 的函数

Δp=ρgΔHref(qref,ω)(DDref)2。

轴扭矩是 **Brake power
table, Wb(q,w)** 参数
*Wref* 的函数，而该参数是参考容量 *qref* 和轴速度 *ω* 的函数

τ=Wref(qref,ω)ω(ρρref)(DDref)5。

参考容量为

qref=m˙ρ(DrefD)3。

当仿真超出所提供表格的范围时，模块根据泵曲线的平均斜率和制动功率外推扬程至最近点。

**缺失数据**

如果表格中有未知数据点，请在 **Head
table, H(q,w)** 和 **Brake power table,
Wb(q,w)** 参数中使用 `NaN` 代替这些值。模块通过根据泵曲线的平均斜率外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲泵行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Head table, H(q,w)** 和 **Brake
  power table, Wb(q,w)** 参数中 `NaN` 元素的位置必须匹配。
- `NaN` 元素必须位于表格的左下部分，这对应于最高容量和最低轴速度。

### 可视化泵曲线

您可以通过绘制扬程、功率、效率和扭矩随流量变化的曲线来检查参数化的泵性能。要生成当前泵设置的图，请右键单击模块并选择 **Fluids** > **Plot Pump Characteristics**。如果您更改了设置或数据，请单击模块参数上的 **Apply**，然后单击泵曲线图上的 **Reload Data**。

默认模块参数化会生成以下图：

泵特性曲线图

### 能量平衡

机械功是轴与流体之间能量交换的结果。控制能量平衡方程为

ϕA+ϕB+Phydro=0，

其中：

- *ΦA* 是端口 **A** 处的能量流率。
- *ΦB* 是端口 **B** 处的能量流率。

泵液压功率是泵端口之间压差的函数

Phydro=Δpm˙ρ。

### 假设和限制

- 如果轴旋转方向与 **Mechanical
  orientation** 参数的设置相反，模块两端的压差降为零，结果可能不准确。
- 模块不考虑泵中的动压。模块仅考虑静压引起的泵扬程。
