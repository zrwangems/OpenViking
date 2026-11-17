---
type: simulink-block
title: 'Isothermal Liquid Predefined Properties (IL)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 连接端口等温液体
  direction: unspecified
```

### 守恒

### **A** — 连接端口等温液体

等温液体守恒端口，用于将模块连接到网络。将此端口连接到框图中等温液体连接线上的任意点。当您将 Isothermal Liquid Predefined Properties (IL) 模块连接到网络线时，液体属性会传播到回路中的所有模块。
## 参数
```yaml
parameters:
- name: Isothermal liquid
  summary: 流体选择 Water（默认）| Seawater (MIT model) | Ethylene glycol and water mixture | Propylene glycol and water mixture |
    Glycerol and water mixture | Aviation fuel Jet-A | Diesel fuel | SAE 5W-30 | SAE 30 Oil | SAE 50 Oil | 10W Oil | 30W Oil
    | 50W Oil | Skydrol LD-4 | Skydrol 500B-4 | Skydrol 5 | HyJet-IVA | Fluid MIL-F-83282 | Fluid MIL-F-5606 | Fluid MIL-F-87257
    | ATF (Dexron III) | ISO VG 22 (ESSO UNIVIS N 22) | ISO VG 32 (ESSO UNIVIS N 32) | ISO VG 46 (ESSO UNIVIS N 46) | ISO
    VG 68 | Brake fluid DOT 3 | Brake fluid DOT 4 | Brake fluid DOT 5 | Gasoline
  group: 液体
- name: Dissolved salt mass fraction (salinity)
  summary: 盐浓度 3.5e-3（默认）| (0, 0.12] 之间的正标量
  group: 液体
- name: Concentration type
  summary: 按质量或体积计的浓度 Volume fraction（默认）| Mass fraction
  group: 液体
- name: Ethylene glycol volume fraction
  summary: 乙二醇的体积浓度 0.1（默认）| (0, 1.0] 之间的正标量
  group: 液体
- name: Ethylene glycol mass fraction
  summary: 乙二醇的质量浓度 0.1（默认）| (0, 0.6] 之间的正标量
  group: 液体
- name: Isothermal bulk modulus at atmospheric pressure (no entrained air)
  summary: 体积模量 2.1791 GPa（默认）| 正标量
  group: 液体
- name: Minimum valid pressure
  summary: 压力下限 0.01（默认）| 正标量
  group: 液体
- name: Propylene glycol volume fraction
  summary: 丙二醇的体积浓度 0.1（默认）| [0.1, 0.6] 之间的正标量
  group: 液体
- name: Propylene glycol mass fraction
  summary: 丙二醇的质量浓度 0.1（默认）| (0, 0.6] 之间的正标量
  group: 液体
- name: Glycerol mass fraction
  summary: 甘油的质量浓度 0.1（默认）| (0, 0.6] 之间的正标量
  group: 液体
- name: System temperature
  summary: 网络温度 300 K（默认）| 正标量
  group: 液体
- name: Viscosity derating factor
  summary: 粘度修正系数 1（默认）| 正标量
  group: 液体
- name: Atmospheric pressure
  summary: 用户定义的环境压力 0.101325 MPa（默认）| 正标量
  group: 液体
- name: Pressure below minimum valid value
  summary: 压力低于最小有效值时是否通知 Error（默认）| Warning | None
  group: 液体
- name: Volumetric fraction of air that is entrained at atmospheric pressure
  summary: 大气压下的系统空气夹带量 0.005（默认）| 正标量
  group: 夹带空气
- name: Air polytropic index
  summary: 多变过程指数 1.0（默认）| [0, 1] 之间的正标量
  group: 夹带空气
- name: Air density at atmospheric condition
  summary: 空气密度 1.225 kg/m^3（默认）| 正标量
  group: 夹带空气
- name: Model air dissolution
  summary: 是否对空气夹带建模 off（默认）| on
  group: 夹带空气
- name: Pressure at which all entrained air is dissolved
  summary: 空气夹带压力上限 3 MPa（默认）| 正标量
  group: 夹带空气
```

### 液体

### **Isothermal liquid** — 流体选择 `Water`（默认）| `Seawater (MIT model)` | `Ethylene glycol and water mixture` | `Propylene glycol and water mixture` | `Glycerol and water mixture` | `Aviation fuel Jet-A` | `Diesel fuel` | `SAE 5W-30` | `SAE 30 Oil` | `SAE 50 Oil` | `10W Oil` | `30W Oil` | `50W Oil` | `Skydrol LD-4` | `Skydrol 500B-4` | `Skydrol 5` | `HyJet-IVA` | `Fluid MIL-F-83282` | `Fluid MIL-F-5606` | `Fluid MIL-F-87257` | `ATF (Dexron III)` | `ISO VG 22 (ESSO UNIVIS N 22)` | `ISO VG 32 (ESSO UNIVIS N 32)` | `ISO VG 46 (ESSO UNIVIS N 46)` | `ISO VG 68` | `Brake fluid DOT 3` | `Brake fluid DOT 4` | `Brake fluid DOT 5` | `Gasoline`

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

对于其余流体，模块使用近似方法计算流体属性。对于这些近似流体，在极端温度下或流体显著偏离大气压时，模块可能会输出意外结果。

### **Dissolved salt mass fraction (salinity)** — 盐浓度 `3.5e-3`（默认）| (0, 0.12] 之间的正标量

水中盐的质量浓度。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为 `Seawater
(MIT)`。

### **Concentration type** — 按质量或体积计的浓度 `Volume fraction`（默认）| `Mass fraction`

溶质在水中按质量还是按体积计量。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为：

- `Ethylene glycol and water
  mixture`。
- `Propylene glycol and water
  mixture`。

### **Ethylene glycol volume fraction** — 乙二醇的体积浓度 `0.1`（默认）| (0, 1.0] 之间的正标量

乙二醇在水中的体积分数。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为 `Ethylene glycol and water
mixture`，并将 **Concentration
type** 设置为 `Volume
fraction`。

### **Ethylene glycol mass fraction** — 乙二醇的质量浓度 `0.1`（默认）| (0, 0.6] 之间的正标量

乙二醇在水中的质量分数。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为 `Ethylene glycol and water
mixture`，并将 **Concentration
type** 设置为 `Mass
fraction`。

### **Isothermal bulk modulus at atmospheric pressure (no entrained air)** — 体积模量 `2.1791 GPa`（默认）| 正标量

大气压下的溶液体积模量。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为：

- `Ethylene glycol and water
  mixture`。
- `Propylene glycol and water
  mixture`。
- `Glycerol and water
  mixture`。

### **Minimum valid pressure** — 压力下限 `0.01`（默认）| 正标量

仿真期间的压力下限。**Atmospheric
pressure** 必须大于或等于
**Minimum valid pressure**。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为：

- `Ethylene glycol and water
  mixture`。
- `Propylene glycol and water
  mixture`。
- `Glycerol and water
  mixture`。

### **Propylene glycol volume fraction** — 丙二醇的体积浓度 `0.1`（默认）| [0.1, 0.6] 之间的正标量

丙二醇在水中的体积分数。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为 `Propylene glycol and water
mixture`，并将 **Concentration
type** 设置为 `Volume
fraction`。

### **Propylene glycol mass fraction** — 丙二醇的质量浓度 `0.1`（默认）| (0, 0.6] 之间的正标量

丙二醇在水中的质量分数。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为 `Propylene glycol and water
mixture`，并将 **Concentration
type** 设置为 `Mass
fraction`。

### **Glycerol mass fraction** — 甘油的质量浓度 `0.1`（默认）| (0, 0.6] 之间的正标量

甘油在水中的质量分数。

#### 依赖关系

要启用此参数，请将 **Isothermal
liquid** 设置为 `Glycerol and water
mixture`。

### **System temperature** — 网络温度 `300 K`（默认）| 正标量

等温液体网络温度。

### **Viscosity derating factor** — 粘度修正系数 `1`（默认）| 正标量

用于修正偏离清洁流体标准粘度的流体的修正系数。

### **Atmospheric pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

系统的环境压力。

### **Pressure below minimum valid value** — 压力低于最小有效值时是否通知 `Error`（默认）| `Warning` | `None`

选择当流体压力在仿真期间低于最小有效值时的行为：

- `None` ― 如果属性低于最小有效值，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

### 夹带空气

### **Volumetric fraction of air that is entrained at atmospheric pressure** — 大气压下的系统空气夹带量 `0.005`（默认）| 正标量

大气压下流体网络中的空气夹带量。

### **Air polytropic index** — 多变过程指数 `1.0`（默认）| [0, 1] 之间的正标量

描述流体压力与体积之间多变过程的方程指数。

### **Air density at atmospheric condition** — 空气密度 `1.225 kg/m^3`（默认）| 正标量

在 **Atmospheric
pressure** 参数所定义压力下的空气密度。

### **Model air dissolution** — 是否对空气夹带建模 `off`（默认）| `on`

是否考虑空气溶解到流体网络中。空气溶解到液体中的过程在 **Atmospheric pressure** 参数值与 **Pressure at which all entrained air is
dissolved** 参数值之间按亨利定律建模。

### **Pressure at which all entrained air is dissolved** — 空气夹带压力上限 `3 MPa`（默认）| 正标量

空气夹带到流体中的压力上限。

#### 依赖关系

要启用此参数，请选择 **Model air dissolution**。
## 所属库

Simscape / Fluids / Isothermal Liquid / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：新增预定义流体

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

### R2024a：压力超出有效范围参数已重命名

为清晰起见，**Pressure outside valid range** 参数已重命名为
**Pressure below minimum valid value**。该参数的行为未发生变化。

### R2023a：SAE 5W-30 的数值调整

当 **Isothermal liquid** 参数为 `SAE
5W-30` 时，模块包含对密度、体积模量、热膨胀系数和比内能的数值调整，以使数据更接近实验数据。

### R2023a：在仿真期间流体属性超出范围时控制模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在您可以使用新的 **Pressure outside
valid range** 参数来控制流体属性在仿真期间超出范围时的模块行为

## 描述

为等温液体网络设置工作流体属性

Isothermal Liquid Predefined Properties (IL) 模块将等温液体网络的工作流体液体属性设置为预定义流体的属性。

您还可以将系统中溶解的空气建模为压力的函数。要指定您自己的工作流体属性，请使用 Foundation Library Isothermal Liquid Properties (IL) 模块。如果未指定流体，则应用系统默认值。有关更多详细信息，请参阅 Specify Fluid Properties。

### 流体属性范围

您可以使用 **Isothermal liquid** 参数将模块设置为对多种预定义不同液体的属性进行建模。

**Water**

模块提供水在三相点（流体温度和压力分别达到 `273.160 K` 和 `611.657
Pa` 时）与临界点（流体温度达到
`647.096 K` 时）之间的属性。*Pmin*
由三相点或饱和压力中较大者设定。

**Ethylene-、Propylene- 和 Glycerol-Water Mixtures**

模块提供乙二醇、丙二醇和甘油在高于溶液凝固点温度下的属性。当您可视化属性时，显示的最低温度可能低于流体凝固点。模块不会显示不同混合物浓度的更新温度。

当您指定混合物时，可以使用 **Concentration type** 参数按质量分数或体积分数定义乙二醇、丙二醇或甘油在水中的浓度。

模块提供以下范围的属性：

- 乙二醇的质量浓度在 0 到 0.6 之间，体积浓度在 0
  到 1 之间。
- 丙二醇的质量浓度在 0 到 0.6 之间，体积浓度在 0.1
  到 0.6 之间。
- 甘油的质量浓度在 0 到 0.6 之间。您不能
  按体积对甘油浓度建模。

模块将属性存储为温度和浓度的函数。除密度和热膨胀系数 *α* 外，模块在一定的压力范围内将所有属性保持为常数。

**Seawater**

模块提供海水在 `273.15
K` 到 `393.15 K` 温度之间以及高于系统饱和压力的属性。盐度浓度按质量计可在
`0` 到 `0.12` 之间。

模块将属性存储为关于压力和温度的表格数据。模块的数据来源于 MIT 网站上的海水热物理性质软件。

**Aviation Fuel Jet-A**

模块提供基于 Jet-A-4658 和 Jet-A-3638 替代物的通用代表性燃料混合物在 `222.22
K` 到 `645.61 K` 温度之间以及高于饱和点的压力下的属性。

模块将属性存储为关于压力和温度的表格数据。

**Diesel Fuel**

模块提供柴油在 `238.20 K`
到 `690.97 K` 温度之间以及高于饱和点的压力下的属性。

**SAE 5W-30**

模块提供 SAE 5W-30 在 `235.15
K` 到 `473.15 K` 温度之间以及高于
`0.01 MPa` 压力下的属性。模块基于系统温度和大气压测量值来确定 `29.85 °C` 到 `74.85 °C`（`303
K` 到  `348 K`）温度之间以及 `7
MPa` 到 `87 MPa` 压力之间的属性。模块使用曲线拟合来定义外推区域中的属性。

**Lubricating Oils and Hydraulic Fluids**

模块使用数值近似来计算这些液体的流体属性：

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

模块使用 Walther 方程来近似速度
*v* 随温度 *T* 的变化

log10(log10(v+a))=b−dlog10(T)，

其中 *a*、*b* 和
*d* 是每种流体特有的常数。

模块假设密度 *ρ* 随温度线性变化，

ρ=ρref+α(Tref−T)，

其中：

- *α* 是每种流体特有的常数。
- *ρref* 是参考温度
  *Tref* 下的流体密度。

体积模量 *β* 为

β=ρc2，

其中 *c* 是声速。模块使用 *c*
`= 1460 m/s` 作为液压油中的声速。

**Gasoline**

模块使用与润滑油和液压油相同的近似方法来计算汽油密度和体积模量。在汽油中，声速为 `1250 m/s`。

Vogel-Fulcher-Tammann 方程计算汽油的流体粘度，

v=v0eBT−T0，

其中 *v0*、
*B* 和 *T0* 是常数。

### 溶解空气

您可以选择对溶解到液体系统中的空气建模。如果选择
**Model air dissolution**，模块将使用亨利定律在 **Atmospheric pressure** 参数值与
**Pressure at which all entrained air is dissolved** 参数值之间对溶解过程建模。有关更多信息，请参阅 Fluid Models with Entrained Air。

### 可视化流体属性

要可视化网络中的流体密度和体积模量，请右键单击 Isothermal
Liquid Predefined Properties (IL) 模块并选择 **Fluids** > **Plot Fluid Properties**。

当流体选择或流体参数发生变化时，使用 **Reload Data** 按钮重新生成绘图。
