---
type: simulink-block
title: 'Isothermal Liquid Predefined Properties (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Utilities'
documentation_page: 'isothermalliquidpredefinedpropertiesil'
documentation_source_path: 'ref/isothermalliquidpredefinedpropertiesil.html'
language: zh-CN
chinese_source: worker-translation
---

# Isothermal Liquid Predefined Properties (IL)

## 端口

### 守恒

### **A** — 等温液体连接端口

等温液体守恒端口，用于将模块连接到网络。在框图中，将此端口连接到等温液体连接线上的任意点。当您将 Isothermal Liquid Predefined Properties (IL) 模块连接到网络线时，液体属性会传播到回路中的所有模块。

## 参数

### 液体

### **等温液体** — 流体选择 `Water`（默认） | `Seawater (MIT model)` | `Ethylene glycol and water mixture` | `Propylene glycol and water mixture` | `Glycerol and water mixture` | `Aviation fuel Jet-A` | `Diesel fuel` | `SAE 5W-30` | `SAE 30 Oil` | `SAE 50 Oil` | `10W Oil` | `30W Oil` | `50W Oil` | `Skydrol LD-4` | `Skydrol 500B-4` | `Skydrol 5` | `HyJet-IVA` | `Fluid MIL-F-83282` | `Fluid MIL-F-5606` | `Fluid MIL-F-87257` | `ATF (Dexron III)` | `ISO VG 22 (ESSO UNIVIS N 22)` | `ISO VG 32 (ESSO UNIVIS N 32)` | `ISO VG 46 (ESSO UNIVIS N 46)` | `ISO VG 68` | `Brake fluid DOT 3` | `Brake fluid DOT 4` | `Brake fluid DOT 5` | `Gasoline`

系统中工作流体的选择。

**注意**

对于这些流体，模块通过插值实验数据来计算流体属性：

- `Water`
- `Seawater (MIT model)`
- `Ethylene glycol and water
  mixture`
- `Propylene glycol and water
  mixture`
- `Glycerol and water
  mixture`
- `Aviation fuel Jet-A`
- `Diesel fuel`
- `SAE 5W-30`

对于其余流体，模块使用近似值来计算流体属性。对于这些近似流体，在极端温度下或流体显著偏离大气压力时，模块可能会输出意外结果。

### **溶解盐质量分数（盐度）** — 盐浓度 `3.5e-3`（默认） | 正标量，范围 (0, 0.12]

水中盐按质量计的浓度。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为 `Seawater (MIT)`。

### **浓度类型** — 按质量或体积计的浓度 `Volume fraction`（默认） | `Mass fraction`

溶质在水中是按质量还是体积计量。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为：

- `Ethylene glycol and water mixture`。
- `Propylene glycol and water mixture`。

### **乙二醇体积分数** — 乙二醇的体积浓度 `0.1`（默认） | 正标量，范围 (0, 1.0]

乙二醇在水中按体积计的分数。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为 `Ethylene glycol and water mixture`，并将 **浓度类型** 设置为 `Volume fraction`。

### **乙二醇质量分数** — 乙二醇的质量浓度 `0.1`（默认） | 正标量，范围 (0, 0.6]

乙二醇在水中按质量计的分数。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为 `Ethylene glycol and water mixture`，并将 **浓度类型** 设置为 `Mass fraction`。

### **大气压下等温体积模量（无夹带空气）** — 体积模量 `2.1791 GPa`（默认） | 正标量

大气压下的溶液体积模量。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为：

- `Ethylene glycol and water mixture`。
- `Propylene glycol and water mixture`。
- `Glycerol and water mixture`。

### **最小有效压力** — 压力下限 `0.01`（默认） | 正标量

仿真期间的压力下限。**大气压力** 必须大于或等于 **最小有效压力**。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为：

- `Ethylene glycol and water mixture`。
- `Propylene glycol and water mixture`。
- `Glycerol and water mixture`。

### **丙二醇体积分数** — 丙二醇的体积浓度 `0.1`（默认） | 正标量，范围 [0.1, 0.6]

丙二醇在水中按体积计的分数。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为 `Propylene glycol and water mixture`，并将 **浓度类型** 设置为 `Volume fraction`。

### **丙二醇质量分数** — 丙二醇的质量浓度 `0.1`（默认） | 正标量，范围 (0, 0.6]

丙二醇在水中按质量计的分数。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为 `Propylene glycol and water mixture`，并将 **浓度类型** 设置为 `Mass fraction`。

### **甘油质量分数** — 甘油的质量浓度 `0.1`（默认） | 正标量，范围 (0, 0.6]

甘油在水中按质量计的分数。

#### 依赖项

要启用此参数，请将 **等温液体** 设置为 `Glycerol and water mixture`。

### **系统温度** — 网络温度 `300 K`（默认） | 正标量

等温液体网络温度。

### **黏度降额因子** — 黏度修正因子 `1`（默认） | 正标量

用于修正偏离清洁流体标准黏度的流体的修正因子。

### **大气压力** — 用户定义的环境压力 `0.101325 MPa`（默认） | 正标量

系统的环境压力。

### **压力低于最小有效值** — 当压力低于最小有效值时是否通知 `Error`（默认） | `Warning` | `None`

选择当流体压力在仿真期间低于最小有效值时的行为：

- `None` ― 如果属性低于最小有效值，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

### 夹带空气

### **大气压下夹带空气的体积分数** — 大气压下系统空气夹带量 `0.005`（默认） | 正标量

流体网络在大气压下的空气夹带量。

### **空气多变指数** — 多变过程指数 `1.0`（默认） | 正标量，范围 [0, 1]

控制流体压力与体积之间多变过程的方程的指数。

### **大气条件下的空气密度** — 空气密度 `1.225 kg/m^3`（默认） | 正标量

在 **大气压力** 参数所定义压力下的空气密度。

### **模拟空气溶解** — 是否模拟空气夹带 `off`（默认） | `on`

是否考虑空气溶解到流体网络中。液体中的空气溶解通过亨利定律在 **大气压力** 参数和 **所有夹带空气均溶解时的压力** 参数的值之间建模。

### **所有夹带空气均溶解时的压力** — 空气夹带压力上限 `3 MPa`（默认） | 正标量

流体中空气夹带的压力上限。

#### 依赖项

要启用此参数，请选择 **模拟空气溶解**。

## 所属库

Simscape / Fluids / Isothermal Liquid / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：新的预定义流体

该模块现在包含以下预定义等温流体：

- `SAE 30 Oil`
- `SAE 50 Oil`
- `10W Oil`
- `30W Oil`
- `50W Oil`
- `Skydrol LD-4`
- `Skydrol 500B-4`
- `Skydrol 5`
- `HyJet-IVA`
- `Fluid MIL-F-83282`
- `Fluid MIL-F-5606`
- `Fluid MIL-F-87257`
- `ATF (Dexron III)`
- `ISO VG 22 (ESSO UNIVIS N 22)`
- `ISO VG 32 (ESSO UNIVIS N 32)`
- `ISO VG 46 (ESSO UNIVIS N 46)`
- `ISO VG 68`
- `Brake fluid DOT 3`
- `Brake fluid DOT 4`
- `Brake fluid DOT 5`
- `Gasoline`

### R2024a：有效范围之外的压强参数已重命名

为清晰起见，**有效范围之外的压强** 参数已重命名为 **压力低于最小有效值**。该参数的行为未更改。

### R2023a：SAE 5W-30 的数值调整

当 **等温液体** 参数为 `SAE 5W-30` 时，模块会对密度、体积模量、热膨胀系数和比内能进行数值调整，以使数据更接近实验数据。

### R2023a：控制在仿真期间流体属性超出范围时的模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在，您可以使用新的 **有效范围之外的压强** 参数来控制当流体属性在仿真期间超出范围时的模块行为。

## 描述

设置等温液体网络的工作流体属性

Isothermal Liquid Predefined Properties (IL) 模块将等温液体网络的工作流体液体属性设置为预定义流体的属性。

您还可以将系统中的溶解空气建模为压力的函数。要指定自己的工作流体属性，请使用 Foundation Library Isothermal Liquid Properties (IL) 模块。如果未指定流体，则应用系统默认值。有关更多详细信息，请参阅“指定流体属性”。

### 流体属性范围

您可以使用 **等温液体** 参数将模块设置为对多种预定义不同液体的属性进行建模。

**水**

该模块提供从三相点到临界点的水属性；在三相点，流体温度和压力达到 `273.160 K` 和 `611.657 Pa`，在临界点，流体温度达到 `647.096 K`。*Pmin* 由三相点或饱和压力中较大者设定。

**乙二醇-、丙二醇-和甘油-水混合物**

该模块提供乙二醇、丙二醇和甘油在溶液凝固点以上温度下的属性。当您可视化属性时，显示的最低温度可能低于流体凝固点。对于不同的混合物浓度，该模块不显示更新后的温度。

指定混合物时，您可以使用 **浓度类型** 参数按质量分数或体积分数定义乙二醇、丙二醇或甘油与水的浓度。

该模块提供以下属性：

- 乙二醇：质量浓度介于 0 和 0.6 之间，体积浓度介于 0 和 1 之间。
- 丙二醇：质量浓度介于 0 和 0.6 之间，体积浓度介于 0.1 和 0.6 之间。
- 甘油：质量浓度介于 0 和 0.6 之间。不能按体积对甘油浓度建模。

该模块将属性存储为温度和浓度的函数。对于一定压力范围，该模块将除密度和热膨胀系数 *α* 之外的所有属性保持为常数。

**海水**

该模块提供温度介于 `273.15 K` 和 `393.15 K` 之间、压力高于系统饱和压力的海水属性。盐度浓度按质量计可在 `0` 到 `0.12` 范围内。

该模块将属性存储为关于压力和温度的表格数据。该模块的数据来自 MIT 网站上的 Thermophysical properties of seawater 软件。

**航空燃油 Jet-A**

该模块提供基于 Jet-A-4658 和 Jet-A-3638 替代物的通用代表性燃料混合物的属性，温度介于 `222.22 K` 和 `645.61 K` 之间，压力高于饱和点。

该模块将属性存储为关于压力和温度的表格数据。

**柴油**

该模块提供温度介于 `238.20 K` 和 `690.97 K` 之间、压力高于饱和点的柴油属性。

**SAE 5W-30**

该模块提供温度介于 `235.15 K` 和 `473.15 K` 之间、压力高于 `0.01 MPa` 的 SAE 5W-30 属性。该模块基于系统温度以及 `29.85 °C` 到 `74.85 °C`（`303 K` 到 `348 K`）温度和 `7 MPa` 到 `87 MPa` 压力下的大气压测量值来确定属性。该模块使用曲线拟合来定义外推区域中的属性。

**润滑油和液压油**

该模块使用数值近似来计算这些液体的流体属性：

- `SAE 30 Oil`
- `SAE 50 Oil`
- `10W Oil`
- `30W Oil`
- `50W Oil`
- `Skydrol LD-4`
- `Skydrol 500B-4`
- `Skydrol 5`
- `HyJet-IVA`
- `Fluid MIL-F-83282`
- `Fluid MIL-F-5606`
- `Fluid MIL-F-87257`
- `ATF (Dexron III)`
- `ISO VG 22 (ESSO UNIVIS N 22)`
- `ISO VG 32 (ESSO UNIVIS N 32)`
- `ISO VG 46 (ESSO UNIVIS N 46)`
- `ISO VG 68`
- `Brake fluid DOT 3`
- `Brake fluid DOT 4`
- `Brake fluid DOT 5`

该模块使用 Walther 方程近似黏度 *v* 随温度 *T* 的变化

log10(log10(v+a))=b−dlog10(T),

其中 *a*、*b* 和 *d* 是每种流体特有的常数。

该模块假定密度 *ρ* 随温度线性变化，

ρ=ρref+α(Tref−T),

其中：

- *α* 是每种流体特有的常数。
- *ρref* 是参考温度 *Tref* 下的流体密度。

体积模量 *β* 为

β=ρc^2,

其中 *c* 是声速。该模块使用 *c* `= 1460 m/s` 作为液压油中的声速。

**汽油**

该模块使用与润滑油和液压油相同的近似来计算汽油密度和体积模量。在汽油中，声速为 `1250 m/s`。

Vogel-Fulcher-Tammann 方程计算汽油的流体黏度，

v=v0e^(B/(T−T0)),

其中 *v0*、*B* 和 *T0* 是常数。

### 溶解空气

您可以选择对溶解到液体系统中的空气建模。如果选择 **模拟空气溶解**，模块会使用亨利定律在 **大气压力** 参数和 **所有夹带空气均溶解时的压力** 参数的值之间对溶解进行建模。有关更多信息，请参阅“夹带空气的流体模型”。

### 可视化流体属性

要可视化网络中的流体密度和体积模量，请右键单击 Isothermal Liquid Predefined Properties (IL) 模块，然后选择 **流体** > **绘制流体属性**。

当流体选择或流体参数发生变化时，使用 **重新加载数据** 按钮重新生成绘图。
