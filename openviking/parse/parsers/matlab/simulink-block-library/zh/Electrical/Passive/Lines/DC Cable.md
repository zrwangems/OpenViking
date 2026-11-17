---
type: simulink-block
title: 'DC Cable'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'dccable'
documentation_source_path: 'ref/dccable.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Cable

## 端口

### 守恒端口

### **c+** — 缆芯导体正极端子 电气

与电缆缆芯导体正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Single cable`。

### **c-** — 缆芯导体负极端子 电气

与电缆缆芯导体负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Single cable`。

### **s+** — 护套正极端子 电气

与电缆护套正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Single cable`。

### **s-** — 护套负极端子 电气

与电缆护套负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Single cable`。

### **a+** — 铠装正极端子 电气

与电缆铠装正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Single cable`。

### **a-** — 铠装负极端子 电气

与电缆护套负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Single cable`。

### **c1+** — 第一根电缆缆芯导体正极端子 电气

与第一根电缆缆芯导体正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **c1-** — 第一根电缆缆芯导体负极端子 电气

与第一根电缆缆芯导体负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **s1+** — 第一根电缆护套正极端子 电气

与第一根电缆护套正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **s1-** — 第一根电缆护套负极端子 电气

与第一根电缆护套负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **a1+** — 第一根电缆铠装正极端子 电气

与第一根电缆铠装正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **a1-** — 第一根电缆铠装负极端子 电气

与第一根电缆铠装负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **c2+** — 第二根电缆缆芯导体正极端子 电气

与第二根电缆缆芯导体正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **c2-** — 第二根电缆缆芯导体负极端子 电气

与第二根电缆缆芯导体负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **s2+** — 第二根电缆护套正极端子 电气

与第二根电缆护套正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **s2-** — 第二根电缆护套负极端子 电气

与第二根电缆护套负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **a2+** — 第二根电缆铠装正极端子 电气

与第二根电缆铠装正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

### **a2-** — 第二根电缆铠装负极端子 电气

与第二根电缆铠装负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为
`Double cable`。

## 参数

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### 主要

### **Configuration** — 用于对单根或双根电缆建模的选项 `Single cable`（默认）| `Double cable`

用于将该模块建模为单根直流电缆或双根直流电缆的选项。

### **Environmental resistivity** — 大地回路电阻 `100` `Ohm*m`（默认）| 正标量

大地回路的电阻。

### **Cable length** — 电缆长度 `100` `km`（默认）| 大于 `1` `m` 的标量

电缆的长度。

### 电气参数

### **Core conductor resistivity** — 缆芯导体电阻率 `2.1e-8` `Ohm*m`（默认）| 正标量

缆芯导体的电阻率。

### **Core conductor relative permeability** — 缆芯导体相对磁导率 `1`（默认）| 正标量

缆芯导体的相对磁导率。

### **Insulation relative permeability** — 绝缘层相对磁导率 `1`（默认）| 正标量

绝缘层的相对磁导率。

### **Insulation relative permittivity** — 绝缘层相对介电常数 `2.5`（默认）| 正标量

绝缘层的相对介电常数。

### **Sheath resistivity** — 护套电阻率 `2.2e-7` `Ohm*m`（默认）| 正标量

护套的电阻率。

### **Sheath relative permeability** — 护套相对磁导率 `1`（默认）| 正标量

护套的相对磁导率。

### **Inner jacket relative permeability** — 内护套相对磁导率 `1`（默认）| 正标量

内护套的相对磁导率。

### **Inner jacket relative permittivity** — 内护套相对介电常数 `2.4`（默认）| 正标量

内护套的相对介电常数。

### **Armor resistivity** — 铠装电阻率 `1.8e-7` `Ohm*m`（默认）| 正标量

铠装的电阻率。

### **Armor relative permeability** — 铠装相对磁导率 `10`（默认）| 正标量

铠装的相对磁导率。

### **Serving relative permeability** — 外被层相对磁导率 `1`（默认）| 正标量

外被层的相对磁导率。

### **Serving relative permittivity** — 外被层相对介电常数 `2.4`（默认）| 正标量

外被层的相对介电常数。

### 几何尺寸

### **Core conductor radial thickness** — 缆芯导体径向厚度 `25` `mm`（默认）| 正标量

缆芯导体的径向厚度。

### **Insulation radial thickness** — 绝缘层径向厚度 `20` `mm`（默认）| 正标量

绝缘层的径向厚度。

### **Sheath radial thickness** — 护套径向厚度 `3` `mm`（默认）| 正标量

护套的径向厚度。

### **Inner jacket radial thickness** — 内护套径向厚度 `5` `mm`（默认）| 正标量

内护套的径向厚度。

### **Armor radial thickness** — 铠装径向厚度 `6` `mm`（默认）| 正标量

铠装的径向厚度。

### **Serving radial thickness** — 外被层径向厚度 `5` `mm`（默认）| 正标量

外被层的径向厚度

### **Vertical depth of the cable** — 电缆垂直位置 `1` `m`（默认）| `[1, 1]` | 正标量或由两个正元素组成的向量

电缆的垂直位置 `y`，如下图所示：

电缆横截面及其垂直位置。

如果将 **Configuration** 参数设置为 `Double
cable`，则此参数值为由两个正元素组成的向量，
`y1` 和
`y2`，默认值为
`[1, 1]`，如下图所示：

两根电缆的横截面及其垂直和水平位置。

### **Horizontal position of the cable** — 电缆水平位置 `[0, 1]` `m`（默认）| 由两个元素组成的向量

电缆的水平位置。

下图显示了双电缆配置的水平位置：

两根电缆的横截面及其垂直和水平位置。

您需要相对于原点指定这些值。因此，
这些值可以为正或负。

#### 依赖关系

要启用此参数，请将 **Configuration** 设置为
`Double cable`。

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

高保真频率相关直流电缆

DC Cable 模块对直流电力电缆进行建模，可在高压直流（HVDC）输电应用中
以高精度仿真瞬态响应。

下图显示了电缆的横截面。共有六个同心层：缆芯
导体、绝缘层、护套、内护套、铠装和外被层。

电缆横截面。共有六个同心层：缆芯导体、绝缘层、护套、内护套、铠装和外被层。

### 方程

为了在仿真期间获得准确的瞬态响应，此模块使用频率相关建模方法对直流电缆
进行建模。有关线路频率相关建模的更多信息，请参阅
Frequency-Dependent Overhead Line (Three-Phase)
模块的方程部分。

要使用频率相关建模方法，该模块必须首先使用 Dommel 电磁暂态程序（EMTP）方程
计算频率相关电缆参数，例如串联阻抗和并联导纳
矩阵。有关这些方程的更多信息，请参阅 [1]。
