---
type: simulink-block
title: 'Interface (TL-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interfacetlil'
documentation_source_path: 'ref/interfacetlil.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (TL-IL)

## 端口

### 守恒

### **TL** — 热液体端口

热液体网络的入口或出口端口。

### **IL** — 等温液体端口

等温液体网络的入口或出口端口。

#### 依赖关系

要启用此端口，请将 **流体域接口** 设置为 `Thermal Liquid (TL) - Isothermal Liquid (IL)`。

### **H** — 液压（等温）液体端口

液压（等温）液体网络的入口或出口端口。

#### 依赖关系

要启用此端口，请将 **流体域接口** 设置为 `Thermal Liquid (TL) - Hydraulic (H)`。

## 参数

### **流体域接口** — 连接库类型 `Thermal Liquid (TL) - Isothermal Liquid (IL)`（默认） | `Thermal Liquid (TL) - Hydraulic (H)`

指定连接的库类型。

### **温度指定** — 等温网络温度 `Constant`（默认） | `Controlled`

设置等温网络温度。在 `Constant` 设置下，您可以在 **液压温度** 参数中指定等温网络温度。在 `Controlled` 设置下，等温网络中的温度由热网络设置。

### **接口温度** — 等温网络温度 `293.15 K`（默认） | 正标量

指定从热液体网络传递到液压或等温液体网络的流体温度。

#### 依赖关系

要启用此参数，请将 **温度指定** 设置为 `Constant`。

### **端口 TL 处的横截面积** — 热液体端口面积 `0.01 m^2`（默认） | 正标量

热液体端口的横截面积。

## 所属库

Simscape / Fluids / Fluid Network Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

热网络与等温网络之间的连接

Interface 模块是热流体网络与等温流体网络之间的连接器。流体质量流量和压力在两个网络之间匹配，但流体属性不会在两个网络之间传递。为了在模型的热组件和等温组件之间保持流体属性，请将具有所需属性的 Isothermal Liquid Predefined Properties (IL) 模块连接到等温网络侧。

您可以将 Thermal Liquid 库模块与 Isothermal Liquid 库或 Hydraulics (Isothermal) 库模块连接。等温系统中设置的温度可以是 `Constant` 或 `Controlled`。对于 `Controlled` 温度系统，等温网络温度由热液体温度设置。在 `Constant` 温度设置下，您可以直接指定等温网络温度。

### Thermal Liquid - Isothermal Liquid

当 **流体域接口** 设置为 `Thermal Liquid (TL) - Isothermal Liquid (IL)` 时，质量流量在两个基于质量流量的网络之间守恒：

m˙TL+m˙IL=0,

其中：

- m˙TL 是热液体接口处的质量流量。
- m˙IL 是等温液体接口处的质量流量。

流体的绝对压力在 Interface 模块的热、内部和等温部分之间保持相等：

pTL=pIL.

### Thermal Liquid - Hydraulics (Isothermal)

Hydraulics (Isothermal) Liquid 库基于体积流量。为了保持接口两侧的流量连续性，体积流量乘以流体密度：

m˙TL+qHρH=0,

其中：

- *q*H 是 Hydraulics (Isothermal) 体积流量。
- *ρ*H 是局部 Hydraulics (Isothermal) 流体密度。

Hydraulics (Isothermal) Liquid 库模块基于表压构造。压力在内部转换为绝对压力，以匹配热网络压力：

pH+patm=pTL.
