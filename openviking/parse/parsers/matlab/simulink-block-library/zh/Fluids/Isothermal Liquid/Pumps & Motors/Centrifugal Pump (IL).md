---
type: simulink-block
title: 'Centrifugal Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'centrifugalpumpil'
documentation_source_path: 'ref/centrifugalpumpil.html'
language: zh-CN
chinese_source: worker-translation
---

# Centrifugal Pump (IL)

## 端口

### 守恒

### **A** — 泵入口等温液体

与流体入口关联的等温液体守恒端口。

### **B** — 泵出口等温液体

与流体出口关联的热液体守恒端口。

### **R** — 叶轮轴机械旋转

与轴关联的机械旋转守恒端口。

### **C** — 泵壳体机械旋转

与壳体关联的机械旋转守恒端口。

## 参数

### **泵参数化** — 扬程和制动功率参数化 `Capacity, head, and brake power at reference shaft speed` （默认） | `1D tabulated data - head and brake power vs. capacity at reference shaft speed` | `2D tabulated data - head and brake power vs. capacity and shaft speed`

泵扬程和制动功率的参数化，指定为：

- `Capacity, head, and brake power at reference shaft speed`：使用解析公式对泵压力增益和轴转矩进行参数化。
- `1D tabulated data - head and brake power vs. capacity at reference shaft speed`：根据给定流量下的扬程和制动功率表格数据，对扬程和制动功率进行参数化。
- `2D tabulated data - head and brake power vs. capacity and shaft speed`：根据给定流量和轴转速下的扬程和制动功率表格数据，对扬程和制动功率进行参数化。

### **额定流量** — 泵体积流量 `45` `lpm` （默认） | 正标量

参考轴角速度下的额定泵体积流量。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **额定扬程** — 泵扬程 `40` `m` （默认） | 正标量

参考轴角速度下的额定泵压差，已按重力和流体密度归一化。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **额定制动功率** — 泵功率 `0.85` `kW` （默认） | 正标量

参考角速度下的额定机械轴功率。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **零流量时的最大扬程** — 无流量时的最大泵扬程 `60` `m` （默认） | 正标量

参考角速度下无流量时的最大泵扬程。除 **额定流量**、**额定扬程** 和 **零扬程时的最大流量** 参数外，此参数还确定泵上的参考压差，模块使用该压差拟合压力的二次方程。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **零扬程时的最大流量** — 零扬程时的最大流量 `80` `lpm` （默认） | 正标量

参考角速度下零扬程时的最大流体负载。除 **额定流量**、**额定扬程** 和 **零流量时的最大扬程** 参数外，此参数还确定泵上的参考压差，模块使用该压差拟合压力的二次方程。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and brake power at reference shaft speed`。

### **参考轴转速** — 用于相似定律计算的参考轴角速度 `1770` `rpm` | `3500` `rpm` | 正标量

用于相似定律计算的参考角速度。默认值取决于 **泵参数化** 设置。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为以下之一：

- `Capacity, head, and brake power at reference shaft speed`。
- `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **最小轴转速阈值（作为参考值的分数）** — 最小轴转速的阈值 `1e-2` （默认） | 正标量

最小轴转速阈值，表示为参考轴转速的分数。模块使用此值防止轴转速变为零，从而避免在 *qref* 表达式中产生除零错误。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and break power at reference shaft speed` 或 `1D tabulated data – head and break power vs. capacity at reference shaft speed`。

### **参考流量向量** — 体积流量 `[16.67, 30, 40, 53.33, 66.67, 83.33]` `lpm` （默认） | 向量

用于泵扬程或制动功率表格参数化的体积流量向量。此向量中的元素与 **参考扬程向量** 和 **参考制动功率向量** 参数中的元素一一对应。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负流量是一种非正常工况，可能在某些情况下出现。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **参考扬程向量** — 泵扬程向量 `[50, 47.5, 45, 40, 35, 25] m` （默认） | 向量

用于泵扬程和制动功率一维表格参数化的泵扬程值向量。此参数与 **参考流量向量** 参数一一对应。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。在非正常工况下，向量末端可能出现负扬程（即压力下降）。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **参考制动功率向量** — 泵制动功率向量 `[.6, .75, .85, .93, .98, .99]` `kW` （默认） | 向量

用于泵扬程和制动功率一维表格参数化的泵制动功率值向量。此参数与 **参考流量向量** 参数一一对应。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。在非正常工况下，向量末端可能出现负制动功率。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed`。

### **流量向量, q** — 体积排量向量 `[16.67, 23.33, 30, 40, 53.33, 60]` `lpm` （默认） | 向量

用于泵扬程表格参数化的体积流量向量。此向量与 **轴转速向量, w** 参数一起为二维 **扬程表, H (q,w)** 和 **制动功率表, Wb(q,w)** 参数构成独立轴。向量元素必须按升序列出。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。负流量是一种非正常工况，可能在某些情况下出现。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **轴转速向量, w** — 角速度向量 `[2450, 2800, 3150, 3500]` `rpm` （默认） | 向量

用于泵扬程表格参数化的轴角速度值向量。此向量与 **流量向量, q** 参数一起为二维 **扬程表, H (q,w)** 和 **制动功率表, Wb(q,w)** 参数构成独立轴。向量元素必须按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **扬程表, H(q,w)** — 泵扬程矩阵 `[25, 32.7, 42.5, 50; 24, 31.7, 41, 49; 22.7, 30.5, 39, 47.5; 20, 28, 36, 45; 15.7, 24, 32, 40; 12.5, 21, 29.5, 37.5]` `m` （默认） | *M*×*N* 矩阵

在指定体积流量和角速度下的泵扬程值 *M*×*N* 矩阵。在正常工作条件下，此参数中的元素为非负值，但模块确实接受负值。在非正常工况下，表底部可能出现负扬程（即压力下降）。模块在表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **流量向量, q** 参数中的元素数量。
- *N* 是 **轴转速向量, w** 参数中的元素数量。所有行必须按严格升序排列。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。模块基于泵曲线的平均斜率进行外推，以填充 `NaN` 元素。不要使用人为数值，因为这些值会扭曲该区域运行时的泵行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **扬程表, H(q,w)** 和 **制动功率表, Wb(q,w)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的左下部分，这对应于最高流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **制动功率表, Wb(q,w)** — 泵制动功率矩阵 `[.28, .38, .5, .6; .31, .41, .55, .68; .33, .44, .6, .75; .36, .48, .65, .83; .38, .53, .72, .93; .39, .55, .75, .97]` `kW` （默认） | *M*×*N* 矩阵

在指定体积流量和角速度下的泵制动功率值 *M*×*N* 矩阵。在正常工作条件下，这些值为非负值，但模块确实接受负值。模块在表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **流量向量, q** 参数中的向量元素数量。
- *N* 是 **轴转速向量, w** 参数中的向量元素数量。所有行必须按严格升序排列。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。模块基于泵曲线的平均斜率进行外推，以填充 `NaN` 元素。不要使用人为数值，因为这些值会扭曲该区域运行时的泵行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **扬程表, H(q,w)** 和 **制动功率表, Wb(q,w)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的左下部分，这对应于最高流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **参考密度** — 给定泵性能数据的流体密度 `998` `kg/m^3` （默认） | 正标量

参考流体密度。参考文档或数据表通常会指定此值。此参数用于在不同流体之间缩放泵性能。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed` 或 `2D tabulated data - head and brake power vs. capacity and shaft speed`。

### **叶轮直径比例因子** — 用于相似定律计算的模型直径与参考直径之比 `1` （默认） | 正标量

用于相似定律计算的模型直径与参考直径之比。如果参考叶轮直径与系统叶轮直径之间存在差异（例如测试泵缩放时），请修改此值。对于小于参考泵的系统泵，使用小于 1 的值。对于大于参考泵的系统泵，使用大于 1 的值。模块不反映因泵尺寸变化而引起的泵效率变化。

### **机械方向** — 轴正常旋转方向 `Positive angular velocity of port R relative to port C corresponds to normal pump operation` （默认） | `Negative angular velocity of port R relative to port C corresponds to normal pump operation`

从端口 **A** 流向 **B** 时的轴旋转方向。

### **检查是否超出正常泵运行范围** — 当模块超出运行边界时通知的选项 `None` （默认） | `Warning` | `Error`

用于在模块超出正常泵边界时发出通知的选项。当通过泵的流量为负或超过泵的最大流量时，会出现这种情况。

#### 依赖关系

要启用此参数，请将 **泵参数化** 设置为 `Capacity, head, and brake power at reference shaft speed`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：公开低轴转速阈值

使用 **最小轴转速阈值（作为参考值的分数）** 参数，将最小轴转速阈值控制为参考轴转速的分数。当 **泵参数化** 参数为 `Capacity, head, and break power at reference shaft speed` 或 `1D tabulated data – head and break power vs. capacity at reference shaft speed` 时，模块中提供 **最小轴转速阈值（作为参考值的分数）** 参数。

### R2022b：将性能扩展到正常工作条件之外

一维和二维参数化现在都允许负值。当仿真超出所提供表的范围时，模块基于泵曲线的平均斜率外推泵扬程。

现在可以在泵数据不可用处使用 `NaN` 元素。以下二维表格参数支持表的左下部分中的连续 `NaN` 元素：

- **扬程表 H(q,w)**
- **制动功率表, Wb(q,w)**

对于每个模块，如果轴沿与指定机械方向相反的方向旋转，则模块两端的压差降为零，结果可能不准确。

## 描述

等温液体网络中的离心泵

Centrifugal Pump (IL) 模块表示一个离心泵，它将能量从轴传递到等温液体网络中的流体。压差和机械转矩是泵扬程和制动功率的函数，而这些量取决于泵流量。您可以通过解析方式或通过对表格数据进行线性插值来参数化泵。泵相似定律定义了模块的核心物理特性，这些定律将泵性能按当前值与参考值的比值进行缩放，所述值包括泵角速度和叶轮直径。

默认情况下，流量和压力增益从端口 **A** 到端口 **B**。端口 **C** 表示泵壳体，端口 **R** 表示泵轴。您可以在 **机械方向** 参数中指定正常工作轴方向。如果轴开始沿相反方向旋转，则模块两端的压差降为零。

**端口配置**

该图显示了典型离心泵上模块端口的位置。

### 解析参数化：容量、扬程和制动功率

当您将 **Pump parameterization** 设置为 `Capacity, head, and brake power at reference shaft speed` 时，模块根据泵相似定律和参考压差计算泵的压升：

pB−pA=ΔHrefρg(ωωref)2(DDref)2,

其中：

- *g* 是重力加速度。
- *ΔHref* 是参考泵扬程，模块通过 **Maximum head at zero capacity**、**Nominal head** 和 **Maximum capacity at zero head** 参数值之间的泵压差二次拟合得到该值。
- *ω* 是轴角速度，*ω*R – *ω*C。
- *ω*ref 是 **Reference shaft speed** 参数的值。
- DDref 是 **Impeller diameter scale factor** 参数的值。此模块不反映因泵尺寸引起的泵效率变化。
- *ρ* 是网络流体密度。

轴扭矩为：

τ=Wbrake,refω2ωref3(DDref)5.

参考制动功率 *W*brake,ref 按容量·扬程/效率计算。泵效率曲线为二次曲线，其峰值对应于 **Nominal brake power** 参数；如泵曲线图所示，当容量为零或最大时，效率降至零。

模块按下式计算参考容量：

qref=m˙ρωrefω(DrefD)3.

您可以通过将 **Check if operating beyond normal pump operation** 设置为 `On`，选择在模块流量变为负值或超过最大泵容量时收到警告。

### 1-D 表格数据参数化：扬程和制动功率随容量的函数

当您将 **Pump parameterization** 设置为 `1D tabulated data - head and brake power vs. capacity at reference shaft speed` 时，泵的压升由 **Reference head vector** 参数 *ΔH*ref 决定，该参数是参考容量 *qref* 的函数：

Δp=ρgΔHref(qref)(ωωref)2(DDref)2,

其中 *g* 是重力加速度。

模块基于 **Reference brake power vector** 参数 *W*ref 计算轴扭矩，该参数是参考容量的函数：

τ=Wref(qref)ω2ωref3(ρρref)(DDref)5,

其中 *ρref* 是 **Reference density** 参数。参考容量为：

qref=m˙ρ(ωrefω)(DrefD)3,

模块使用该值根据 *qref* 对 **Reference capacity vector**、**Reference head vector** 和 **Reference brake power vector** 参数的值进行插值。

当仿真超出所提供表格的范围时，模块根据泵曲线的平均斜率外推扬程，并将制动功率外推到最近点。

### 2-D 表格数据参数化：扬程和制动功率随容量和轴转速的函数

当您将 **Pump parameterization** 设置为 `2D tabulated data - head and brake power vs. capacity and shaft speed` 时，泵的压升是 **Head table, H(q,w)** 参数 *ΔHref* 的函数，而该参数是参考容量 *qref* 和轴转速 *ω* 的函数：

Δp=ρgΔHref(qref,ω)(DDref)2.

轴扭矩是 **Brake power table, Wb(q,w)** 参数 *Wref* 的函数，而该参数是参考容量 *qref* 和轴转速 *ω* 的函数：

τ=Wref(qref,ω)ω(ρρref)(DDref)5.

参考容量为：

qref=m˙ρ(DrefD)3.

当仿真超出所提供表格的范围时，模块根据泵曲线的平均斜率外推扬程，并将制动功率外推到最近点。

**缺失数据**

如果您的表格包含未知数据点，请在这些值的位置使用 `NaN`。模块通过基于泵曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲泵行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Head table, H(q,w)** 和 **Brake power table, Wb(q,w)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表格的左下部分，这对应于最高容量和最低轴转速。

### 可视化泵曲线

您可以通过绘制扬程、功率、效率和扭矩随流量的变化来检查参数化泵性能。要生成当前泵设置的图，请右键单击模块，然后选择 **Fluids** > **Plot Pump Characteristics**。如果更改设置或数据，请单击模块参数上的 **Apply**，然后单击泵曲线图上的 **Reload Data**。

默认模块参数化会生成以下图：

泵特性曲线图

### 预定义参数化

您可以使用预参数化的制造商数据填充模块，这允许您对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以在 Block Parameterization Manager 窗口中选择一个部件，并查看 **Compare selected part with block** 部分中的数据，从而将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用数据源提供参数值。模块对缺失数据采用工程判断和简化假设进行替代。因此，预计仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。

### 假设和限制

- 如果轴按与指定机械方向相反的方向旋转，则模块两端的压差降至零，结果可能不准确。
- 模块不考虑泵中的动态压力。模块仅考虑由静压产生的泵扬程。
- 预定义参数化使用可用数据，模块会在必要时填充缺失数据。请根据预期结果验证您的模型。
