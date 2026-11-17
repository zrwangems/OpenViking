---
type: simulink-block
title: 'Thermal Liquid Properties (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Utilities'
documentation_page: 'thermalliquidpropertiestl'
documentation_source_path: 'ref/thermalliquidpropertiestl.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermal Liquid Properties (TL)

## 端口

### 守恒

### **R** — 用于定义工作流体热液的热液网络

用于标识要为其定义必要流体属性的热液网络的节点。此模块中选择的流体应用于整个网络。不得将其他 Thermal Liquid Properties (TL) 或 Thermal Liquid Settings (TL) 模块连接到同一网络。

## 参数

### **Thermal liquid fluid list** — 可用工作流体 `Water`（默认）| `Seawater (MIT model)` | `Ethylene glycol and water mixture` | `Propylene glycol and water mixture` | `Glycerol and water mixture` | `Diesel Fuel` | `Aviation fuel Jet-A` | `SAE 5W-30`

设置液体网络的流体属性。可用流体包括纯水、水溶液混合物、机油和燃料。

### **Dissolved salt mass fraction (salinity)** — 盐的质量除以盐水混合物的总质量 `3.5e-3`（默认）| 0 到 1 之间的正无量纲标量

盐水混合物中存在的盐的质量与该混合物总质量的比值。

#### 依赖关系

此参数仅在选择 `Seawater (MIT model)` 作为工作流体时激活。

### **Concentration type** — 定义混合物浓度所依据的量 `Volume fraction`（默认）| `Mass fraction`

用于指定乙二醇在其水溶液混合物中浓度所依据的量。此参数仅在选择 `Ethylene glycol and water mixture` 或 `Propylene glycol and water mixture` 作为工作流体时激活。

### **Ethylene glycol volume fraction** — 乙二醇的体积除以水溶液混合物的体积 `0.1`（默认）| 0 到 1 之间的正无量纲标量

水溶液混合物中存在的乙二醇的体积与该混合物总体积的比值。

#### 依赖关系

此参数在选择 `Ethylene glycol and water mixture` 作为工作流体且选择 `Volume fraction` 作为浓度类型时激活。

### **Ethylene glycol mass fraction** — 乙二醇的质量除以水溶液混合物的质量 `0.1`（默认）| 0 到 1 之间的正无量纲标量

水溶液混合物中存在的乙二醇的质量与该混合物总质量的比值。

#### 依赖关系

此参数在选择 `Ethylene glycol and water mixture` 作为工作流体且选择 `Mass fraction` 作为浓度类型时激活。

### **Propylene glycol volume fraction** — 丙二醇的质量除以水溶液混合物的质量 `0.1`（默认）| 0 到 1 之间的正无量纲标量

水溶液混合物中存在的丙二醇的体积与该混合物总体积的比值。

#### 依赖关系

此参数在选择 `Propylene glycol and water mixture` 作为工作流体且选择 `Volume fraction` 作为浓度类型时激活。

### **Propylene glycol mass fraction** — 丙二醇的质量除以水溶液混合物的质量 `0.1`（默认）| 0 到 1 之间的正无量纲标量

水溶液混合物中存在的丙二醇的质量与该混合物总质量的比值。

#### 依赖关系

此参数在选择 `Propylene glycol and water mixture` 作为工作流体且选择 `Mass fraction` 作为浓度类型时激活。

### **Isothermal bulk modulus** — 在恒定温度下指定的流体可压缩性度量 `2.1791 GPa`（默认）| 带压力单位的正标量

水溶液混合物在恒定温度下的体积模量。体积模量衡量产生流体体积分数变化所需的压力变化。

#### 依赖关系

此参数在选择 `Ethylene glycol and water mixture`、`Propylene glycol and water mixture` 或 `Glycerol and water mixture` 作为工作流体时激活。

### **Minimum valid pressure** — 热液网络允许压力范围的下界 `0.01 MPa`（默认）| 带压力单位的正标量

连接到此模块的热液网络中允许的压力范围的下界。

#### 依赖关系

此参数在选择 `Ethylene glycol and water mixture`、`Propylene glycol and water mixture` 或 `Glycerol and water mixture` 作为工作流体时激活。

### **Maximum valid pressure** — 热液网络允许压力范围的上界 `50 MPa`（默认）| 带压力单位的正标量

连接到此模块的热液网络中允许的压力范围的上界。

#### 依赖关系

此参数在选择 `Ethylene glycol and water mixture`、`Propylene glycol and water mixture` 或 `Glycerol and water mixture` 作为工作流体时激活。

### **Atmospheric pressure** — 热液网络环境中的绝对压力 `0.101325 MPa`（默认）| 带压力单位的正标量

假定热液网络运行所在外部环境的绝对压力。默认值为在地球海平面测得的标准大气压。

### **Pressure and temperature outside valid range** — 当压力或温度超出有效范围时是否通知 `Error`（默认）| `Warning` | `None`

选择当流体压力或温度在仿真期间超出有效范围时会发生什么：

- `None` ― 如果属性超出范围，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

## 所属库

Simscape / Fluids / Thermal Liquid / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023a：SAE 5W-30 的数值调整

当 **Thermal liquid fluid** 参数为 `SAE 5W-30` 时，模块包含对密度、体积模量、热膨胀系数和比内能的数值调整，以使数据更接近实验数据。

### R2023a：在仿真期间流体属性超出范围时控制模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在，您可以使用新的 **Pressure and temperature outside valid range** 参数来控制当流体属性在仿真期间超出范围时的模块行为

## 描述

为热液体网络仿真预设流体属性

Thermal Liquid Properties (TL) 模块为热液体网络设置预定义的流体属性。可用的流体包括纯水、水溶液混合物、柴油、航空燃油 Jet A 和 SAE 5W-30。您可以将此模块用作 Thermal Liquid Settings (TL) 模块的预设替代方案。如果您的网络没有连接液体属性模块，则将应用液体默认值。有关更多详细信息，请参阅 Specify Fluid Properties。

预设流体属性以表格形式定义为温度和压力的函数。在仿真期间，网络属性通过数据点之间的线性插值来设置。水溶液混合物的表格数据按质量浓度或体积浓度提供。

Thermal Liquid Settings (TL) 模块中通常指定的所有流体属性都在此模块中定义。这些属性包括密度、体积模量和热膨胀系数、比内能和比热，以及运动粘度和热导率。这些属性在特定于所选流体的有限温度和压力区域内有效，对于混合物，还取决于指定的浓度。仅允许在此有效区域内进行仿真。

### 数据可视化

您可以可视化模块中定义的流体属性以及压力和温度的有效区域。要打开可视化工具，请右键单击模块并选择 **Fluids** > **Plot Fluid Properties**。从下拉列表中选择流体属性后，绘图会自动更新。每当流体选择或流体参数发生变化时，使用 **Reload Data** 按钮重新生成绘图。

**10% 甘油水溶液混合物的密度数据可视化**

### 有效区域

有效区域在模块中定义为由零和一组成的矩阵。每一行对应一个表格化的温度，每一列对应一个表格化的压力。零表示无效断点，一表示有效断点。这些有效性矩阵是模块内部的，无法修改；只能进行检查（使用模块的数据可视化工具）。

在大多数情况下，有效性矩阵直接从表格数据中提取。乙二醇和甘油混合物的压力边界无法从数据中获得，而是从模块参数中显式获取。下图显示了水的有效区域示例。阴影方块表示有效区域之外的温度和压力区域。

**`Water`**

水的属性在高于三相点值（`273.160 K`）直至临界点值（`647.096 K`）的温度范围内有效。在压力高于三相点值（`611.657 Pa`）和依赖于温度的饱和值两者中的较大值，直至临界点值（`22.064 MPa`）的范围内有效。对于给定温度行，低于饱和点的压力在有效性矩阵中被赋值为 `0`。

**`Seawater (MIT model)`**

海水的属性在高于 `0°C` 直至 `120°C`（`273.15 K` 至 `393.15 K`）的温度范围内有效；在压力高于饱和点直至最大值 `12 MPa` 的范围内有效。对于给定温度行（以及在指定浓度水平下），低于饱和点的压力在有效性矩阵中被赋值为 `0`。混合物浓度的质量分数范围可以从 `0` 到 `0.12`。

**`Ethylene glycol and water mixture`**

乙二醇水溶液混合物的属性在由混合物浓度确定的温度域内有效；在模块对话框中指定的最小和最大压力边界内有效（水平扩展以跨越温度行的宽度）。

温度下限始终是从可用数据中提取的最低温度和混合物凝固点中的较小值（混合物必须处于液态）。温度上限始终是从数据中提取的最高温度。如果使用质量分数基准，混合物浓度的范围可以从 `0` 到 `0.6`；如果使用体积分数基准，则范围可以从 `0` 到 `1`。

**`Propylene glycol and water mixture`**

丙二醇水溶液混合物的属性在 `Ethylene glycol and water mixture` 情况下描述的温度和压力范围内有效。如果使用质量分数基准，混合物浓度的范围可以从 `0` 到 `0.6`；如果使用体积分数基准，则范围可以从 `0.1` 到 `0.6`。

**`Glycerol and water mixture`**

甘油水溶液混合物的属性在 `Ethylene glycol and water mixture` 情况下描述的温度和压力范围内有效。混合物浓度的质量分数范围可以从 `0` 到 `0.6`。所有属性都按以下方式扩展到 `100 degC`：

- 密度 — 二次拟合
- Alpha（密度热导数）— 线性拟合
- 比热 — 线性拟合
- 比内能 — 线性拟合
- 运动粘度 — 基于原始温度范围上半部分的指数拟合
- 动力粘度 — 基于原始温度范围上半部分的指数拟合
- 普朗特数 — 基于原始温度范围上半部分的指数拟合

**`Aviation fuel Jet-A`**

Jet A 燃油的属性在高于 `-50.93°C` 直至 `372.46°C`（`222.22 K` 至 `645.61 K`）的温度范围内有效；在压力高于饱和点直至最大值 `2.41 MPa` 的范围内有效。对于给定温度行，低于饱和点的压力在有效性矩阵中被赋值为 `0`。

**`Diesel fuel`**

柴油的属性在高于 `-34.95°C` 直至 `417.82°C`（`238.20 K` 至 `690.97 K`）的温度范围内有效；在压力高于饱和点直至最大值 `2.29 MPa` 的范围内有效。对于给定温度行，低于饱和点的压力在有效性矩阵中被赋值为 `0`。

**`SAE 5W-30`**

SAE 5W-30 的属性来源于涵盖每种属性的温度和压力范围的数据。模块使用 `29.85°C` 至 `74.85°C`（`303 K` 至 `348 K`）以及 `7 MPa` 至 `82 MPa` 范围内的测量属性。模块将此区域之外的数据外推到 `-38°C` 和 `200°C`（`235.15 K` 和 `473.15 K`）以及 `0.01 MPa` 和 `100 MPa`。模块平滑和外推数据的方式取决于数据类型：

- 密度 — 模块使用二次拟合。模块将外推区域拟合到体积模量和 alpha 基本关系。
- 体积模量 — 模块使用基于密度二次拟合的密度基本关系。模块在外推区域使用线性外推。
- Alpha（密度热导数）— 模块使用基于密度二次拟合的密度基本关系。模块在外推区域使用线性外推。
- 比热 — 模块在外推区域使用线性外推。不依赖于压力。
- 热导率 — 模块在外推区域使用线性外推。不依赖于压力。
- 运动粘度 — 模块使用动力粘度和密度拟合的基本关系。
- 动力粘度 — 模块使用随温度的指数拟合和随压力的线性拟合。
- 普朗特数 — 模块使用比热、动力粘度和热导率拟合的基本关系。

### 计算属性

乙二醇和甘油化合物的水混合物的密度和热膨胀系数由模块参数获得。流体密度相对于压力和温度的计算公式为：

ρ(T,p)=ρ(T)exp(p−pRβ)，

其中：

- *T* 是网络温度。
- *p* 是网络压力。
- *ρ* 是流体密度。
- *p*R 是与流体属性表关联的参考压力。
- *ß* 是等温体积模量。

其中流体密度的变化量计算为：

(∂ρ(T,p)∂T)p=(∂ρ(T)∂T)Texp(p−pRβ)。

热膨胀系数计算为：

α(T,p)=−1ρ(T,p)(∂ρ(T)∂T)Texp(p−pRβ)。
