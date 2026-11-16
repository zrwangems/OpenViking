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

### **R** — 用于定义工作流体（热流体）的热流体网络

用于标识需要为其定义必要流体属性的热流体网络的节点。此模块中选择的流体将应用于整个网络。同一网络上不得连接其他 Thermal Liquid Properties (TL) 或 Thermal Liquid Settings (TL) 模块。

## 参数

### **Thermal liquid fluid list** — 可用工作流体 `Water`（默认）| `Seawater (MIT model)` | `Ethylene glycol and water mixture` | `Propylene glycol and water mixture` | `Glycerol and water mixture` | `Diesel Fuel` | `Aviation fuel Jet-A` | `SAE 5W-30`

设置液体网络的流体属性。可用流体包括纯水、水溶液、机油和燃料。

### **Dissolved salt mass fraction (salinity)** — 盐的质量除以盐水混合物的总质量 `3.5e-3`（默认）| 介于 0 和 1 之间的正无量纲标量

盐水混合物中存在的盐的质量与该混合物总质量的比值。

#### 依赖关系

仅当选择 `Seawater (MIT model)` 作为工作流体时，此参数才激活。

### **Concentration type** — 用于定义混合物浓度的量 `Volume fraction`（默认）| `Mass fraction`

用于指定乙二醇在其水溶液中浓度的量。仅当选择 `Ethylene glycol and water mixture` 或 `Propylene glycol and water mixture` 作为工作流体时，此参数才激活。

### **Ethylene glycol volume fraction** — 乙二醇体积除以水溶液的体积 `0.1`（默认）| 介于 0 和 1 之间的正无量纲标量

水溶液中存在的乙二醇体积与该混合物总体积之比。

#### 依赖关系

当选择 `Ethylene glycol and water mixture` 作为工作流体，并选择 `Volume fraction` 作为浓度类型时，此参数激活。

### **Ethylene glycol mass fraction** — 乙二醇质量除以水溶液的质量 `0.1`（默认）| 介于 0 和 1 之间的正无量纲标量

水溶液中存在的乙二醇质量与该混合物总质量之比。

#### 依赖关系

当选择 `Ethylene glycol and water mixture` 作为工作流体，并选择 `Mass fraction` 作为浓度类型时，此参数激活。

### **Propylene glycol volume fraction** — 丙二醇体积除以水溶液的体积 `0.1`（默认）| 介于 0 和 1 之间的正无量纲标量

水溶液中存在的丙二醇体积与该混合物总体积之比。

#### 依赖关系

当选择 `Propylene glycol and water mixture` 作为工作流体，并选择 `Volume fraction` 作为浓度类型时，此参数激活。

### **Propylene glycol mass fraction** — 丙二醇质量除以水溶液的质量 `0.1`（默认）| 介于 0 和 1 之间的正无量纲标量

水溶液中存在的丙二醇质量与该混合物总质量之比。

#### 依赖关系

当选择 `Propylene glycol and water mixture` 作为工作流体，并选择 `Mass fraction` 作为浓度类型时，此参数激活。

### **Isothermal bulk modulus** — 在恒定温度下指定的流体可压缩性度量 `2.1791 GPa`（默认）| 带压力单位的正标量

水溶液在恒温下的体积模量。体积模量衡量使流体体积产生分数变化所需的压力变化。

#### 依赖关系

当选择 `Ethylene glycol and water mixture`、`Propylene glycol and water mixture` 或 `Glycerol and water mixture` 作为工作流体时，此参数激活。

### **Minimum valid pressure** — 热流体网络允许压力范围的下界 `0.01 MPa`（默认）| 带压力单位的正标量

连接到此模块的热流体网络中允许压力范围的下界。

#### 依赖关系

当选择 `Ethylene glycol and water mixture`、`Propylene glycol and water mixture` 或 `Glycerol and water mixture` 作为工作流体时，此参数激活。

### **Maximum valid pressure** — 热流体网络允许压力范围的上界 `50 MPa`（默认）| 带压力单位的正标量

连接到此模块的热流体网络中允许压力范围的上界。

#### 依赖关系

当选择 `Ethylene glycol and water mixture`、`Propylene glycol and water mixture` 或 `Glycerol and water mixture` 作为工作流体时，此参数激活。

### **Atmospheric pressure** — 热流体网络环境中的绝对压力 `0.101325 MPa`（默认）| 带压力单位的正标量

假定热流体网络运行所处外部环境的绝对压力。默认值为地球海平面处测得的标准大气压。

### **Pressure and temperature outside valid range** — 当压力或温度超出有效范围时是否通知 `Error`（默认）| `Warning` | `None`

选择仿真期间流体压力或温度超出有效范围时发生的情况：

- `None` ― 如果属性超出范围，模块不会返回错误。
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

### R2023a: SAE 5W-30 的数值调整

当 **Thermal liquid fluid** 参数为 `SAE 5W-30` 时，模块会对密度、体积模量、热膨胀系数和比内能进行数值调整，以使数据更接近实验数据。

### R2023a: 控制仿真期间流体属性超出范围时的模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在，您可以使用新的 **Pressure and temperature outside valid range** 参数来控制当流体属性在仿真期间超出范围时模块的行为

## 描述

用于热流体网络仿真的预设流体属性

Thermal Liquid Properties (TL) 模块为热流体网络设置预定义流体属性。可用流体包括纯水、水溶液、柴油、航空燃料 Jet A 和 SAE 5W-30。您可以将此模块用作 Thermal Liquid Settings (TL) 模块的预设替代方案。如果您的网络没有连接液体属性模块，则将应用液体默认值。有关更多详细信息，请参阅 Specify Fluid Properties。

预设流体属性以表格形式定义为温度和压力的函数。在仿真期间，网络属性通过数据点之间的线性插值设置。水溶液的表格数据按质量或体积浓度提供。

通常在 Thermal Liquid Settings (TL) 模块中指定的所有流体属性都在此模块中定义。这些属性包括密度、体积模量和热膨胀系数、比内能和比热，以及运动黏度和热导率。这些属性在特定于所选流体的有限温度和压力区域内有效，对于混合物，还取决于指定的浓度。仅允许在此有效区域内进行仿真。

### 数据可视化

您可以可视化模块中定义的流体属性以及压力和温度有效区域。要打开可视化实用工具，请右键单击该模块，然后选择 **Fluids** > **Plot Fluid Properties**。从下拉列表中选择流体属性后，绘图会自动更新。当流体选择或流体参数更改时，使用 **Reload Data** 按钮重新生成绘图。

**10% 甘油水溶液的密度数据可视化**

### 有效区域

有效区域在模块中定义为由 0 和 1 组成的矩阵。每一行对应一个制表温度，每一列对应一个制表压力。0 表示无效断点，1 表示有效断点。这些有效性矩阵是模块内部的，无法修改；只能使用模块的数据可视化实用工具进行检查。

在大多数情况下，有效性矩阵直接从制表数据中提取。乙二醇和甘油混合物的压力边界无法从数据中获得，而是明确从模块参数获取。下图显示了水的有效区域示例。阴影方格表示有效区域之外的温度和压力区域。

**`Water`**

水的属性在高于三相点值 (`273.160 K`) 至临界点值 (`647.096 K`) 的温度下有效。其在压力高于三相点值 (`611.657 Pa`) 与温度相关饱和值两者中的较大值、直至临界点值 (`22.064 MPa`) 时有效。对于给定温度行，低于饱和点的压力在有效性矩阵中被赋值为 `0`。

**`Seawater (MIT model)`**

海水的属性在高于 `0°C` 至 `120°C`（`273.15 K` 至 `393.15 K`）的温度下有效；其在压力高于饱和点、直至最大值 `12 MPa` 时有效。对于给定温度行（以及在指定浓度水平下），低于饱和点的压力在有效性矩阵中被赋值为 `0`。混合物浓度按质量分数基准可在 `0` 至 `0.12` 范围内取值。

**`Ethylene glycol and water mixture`**

乙二醇水溶液混合物的属性在由混合物浓度确定的温度域内有效；其在模块对话框中指定的最小和最大边界内的压力下有效（水平延伸以跨越温度行的宽度）。

温度下界始终是从可用数据中提取的最低温度与混合物凝固点两者中的较小值（混合物必须处于液态）。温度上界始终是从数据中提取的最高温度。如果使用质量分数基准，混合物浓度可在 `0` 至 `0.6` 范围内取值；如果使用体积分数基准，则可在 `0` 至 `1` 范围内取值。

**`Propylene glycol and water mixture`**

丙二醇水溶液混合物的属性在针对 `Ethylene glycol and water mixture` 所述的温度和压力范围内有效。如果使用质量分数基准，混合物浓度可在 `0` 至 `0.6` 范围内取值；如果使用体积分数基准，则可在 `0.1` 至 `0.6` 范围内取值。

**`Glycerol and water mixture`**

甘油水溶液混合物的属性在针对 `Ethylene glycol and water mixture` 所述的温度和压力范围内有效。混合物浓度按质量分数基准可在 `0` 至 `0.6` 范围内取值。所有属性均按如下方式外推到 `100 degC`：

- 密度 — 二次拟合
- Alpha（密度热导数）— 线性拟合
- 比热 — 线性拟合
- 比内能 — 线性拟合
- 运动黏度 — 基于原始温度范围上半段的指数拟合
- 动力黏度 — 基于原始温度范围上半段的指数拟合
- 普朗特数 — 基于原始温度范围上半段的指数拟合

**`Aviation fuel Jet-A`**

Jet A 燃料的属性在高于 `-50.93°C` 至 `372.46°C`（`222.22 K` 至 `645.61 K`）的温度下有效；其在压力高于饱和点、直至最大值 `2.41 MPa` 时有效。对于给定温度行，低于饱和点的压力在有效性矩阵中被赋值为 `0`。

**`Diesel fuel`**

柴油燃料的属性在高于 `-34.95°C` 至 `417.82°C`（`238.20 K` 至 `690.97 K`）的温度下有效；其在压力高于饱和点、直至最大值 `2.29 MPa` 时有效。对于给定温度行，低于饱和点的压力在有效性矩阵中被赋值为 `0`。

**`SAE 5W-30`**

SAE 5W-30 燃料的属性源自涵盖每种属性的温度和压力范围的数据。模块使用 `29.85°C` 至 `74.85°C`（`303 K` 至 `348 K`）以及 `7 MPa` 至 `82 MPa` 之间的测量属性。模块将该区域之外的数据外推到 `-38°C` 和 `200°C`（`235.15 K` 和 `473.15 K`）以及 `0.01 MPa` 和 `100 MPa`。模块平滑和外推数据的方式取决于数据类型：

- 密度 — 模块使用二次拟合。模块将外推区域拟合到体积模量和 alpha 基本关系。
- 体积模量 — 模块使用与密度相关的基本关系，其中密度基于密度二次拟合。模块在外推区域使用线性外推。
- Alpha（密度热导数）— 模块使用与密度相关的基本关系，其中密度基于密度二次拟合。模块在外推区域使用线性外推。
- 比热 — 模块在外推区域使用线性外推。不依赖于压力。
- 热导率 — 模块在外推区域使用线性外推。不依赖于压力。
- 运动黏度 — 模块使用与动力黏度和密度拟合相关的基本关系。
- 动力黏度 — 模块使用随温度变化的指数拟合和随压力变化的线性拟合。
- 普朗特数 — 模块使用与比热、动力黏度和热导率拟合相关的基本关系。

### 计算所得属性

乙二醇和甘油化合物的水溶液的密度和热膨胀系数由模块参数获得。流体密度相对于压力和温度的计算公式为：

ρ(T,p)=ρ(T)exp(p−pRβ),

其中：

- *T* 是网络温度。
- *p* 是网络压力。
- *ρ* 是流体密度。
- *p*R 是与流体属性表关联的参考压力。
- *ß* 是等温体积模量。

其中，流体密度的变化计算为：

(∂ρ(T,p)∂T)p=(∂ρ(T)∂T)Texp(p−pRβ).

热膨胀系数计算为：

α(T,p)=−1ρ(T,p)(∂ρ(T)∂T)Texp(p−pRβ).
