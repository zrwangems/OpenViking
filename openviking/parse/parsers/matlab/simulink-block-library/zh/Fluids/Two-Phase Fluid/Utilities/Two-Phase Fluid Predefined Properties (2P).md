---
type: simulink-block
title: 'Two-Phase Fluid Predefined Properties (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Utilities'
documentation_page: 'twophasefluidpredefinedproperties2p'
documentation_source_path: 'ref/twophasefluidpredefinedproperties2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Phase Fluid Predefined Properties (2P)

## 端口

### 守恒

### **A** — 两相流体连接端口

两相流体守恒端口，用于将模块连接到网络。该端口可连接到框图内两相连接线上的任意点。当您将 Two-Phase Fluid Predefined Properties (2P) 模块连接到网络管线时，流体属性会传播到回路中的所有模块。

## 参数

### **Two-phase fluid** — 工作流体 `Water (R-718)`（默认）| `Ammonia (R-717)` | `Carbon dioxide (R-744)` | `Isobutane (R-600a)` | `Propane (R-290)` | `R-1233zd(E)` | `R-1234yf` | `R-134a` | `R-22` | `R-32` | `R-404A` | `R-407C` | `R-410A`

预定义工作流体选项。

### **Atmospheric pressure** — 环境压力 `0.101325` MPa（默认）| 正标量

系统的环境压力。

### **Pressure and specific internal energy outside valid range** — 是否在压力或比内能超出有效范围时发出通知 `Error`（默认）| `Warning` | `None`

选择当仿真期间流体压力或比内能超出有效范围时的行为：

- `None` ― 如果属性超出范围，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

### **Dynamic pressure threshold for flow reversal** — 设置应用数值平滑的区域 `0.01` Pa（默认）| 正标量

设置应用数值平滑的区域。在 **Dynamic pressure threshold for flow reversal** 的正值和负值之间，围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算得到的属性会进行调整，以确保平滑过渡。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2024b：使用新的预定义两相流体

您现在可以在两相域中将 Propane (R-290)、R-32 和 R-1233zd(E) 建模为预定义流体。

### R2023a：在仿真期间流体属性超出范围时控制模块行为

以前，如果仿真期间流体属性超出有效范围，模块会返回错误。您现在可以使用新的 **Pressure and specific internal energy outside valid range** 参数来控制仿真期间流体属性超出范围时的模块行为。

## 描述

两相网络的预定义工作流体

Two-Phase Fluid Predefined Properties (2P) 模块用于设置两相系统的工作流体属性。可用的预定义流体包括：

- Water (R-718)
- R-134a
- R-1234yf
- R-1233zd(E)
- R-404A
- R-410A
- R-407C
- R-22
- R-32
- Ammonia (R-717)
- Carbon dioxide (R-744)
- Isobutane (R-600a)
- Propane (R-290)

如果您想指定自己的工作流体属性，请使用 Foundation Library 的 Two-Phase Fluid Properties (2P) 模块。如果您未指定流体，将应用系统默认值。有关更多详细信息，请参阅 Specify Fluid Properties。

### 流体属性范围

**Water (R-718)**

流体属性提供的压力范围为 0.001 至 95 MPa，温度范围（在 1 个大气压下）为 273.16 至 1,245.8 K。

**R-134a**

流体属性提供的压力范围为 0.001 至 5.5 MPa，温度范围（在 1 个大气压下）为 177.08 至 424.4 K。

**R-1234yf**

流体属性提供的压力范围为 0.04 至 3.2 MPa，温度范围（在 1 个大气压下）为 223.52 至 387.45 K。

**R-1233zd(E)**

流体属性提供的压力范围为 0.001 至 9 MPa，温度范围（在 1 个大气压下）为 202.29 至 500.24 K。

**R-404A**

流体属性提供的压力范围为 0.003 至 12 MPa，温度范围（在 1 个大气压下）为 171.6 至 550.94 K。

**R-410A**

流体属性提供的压力范围为 0.001 至 6 MPa，温度范围（在 1 个大气压下）为 146.19 至 427.25 K。

**R-407C**

流体属性提供的压力范围为 0.001 至 6 MPa，温度范围（在 1 个大气压下）为 158.85 至 427.92 K。

**R-22**

流体属性提供的压力范围为 0.001 至 8 MPa，温度范围（在 1 个大气压下）为 120.77 至 519.49 K。

**R-32**

流体属性提供的压力范围为 0.0001 至 7 MPa，温度范围（在 1 个大气压下）为 138.91 至 375.55 K。

**Ammonia (R-717)**

流体属性提供的压力范围为 0.008 至 95 MPa，温度范围（在 1 个大气压下）为 195.5 至 543.9 K。

**Carbon dioxide (R-744)**

流体属性提供的压力范围为 0.55 至 50 MPa，温度范围（在 1 MPa 下）为 216.94 至 1,389.4 K。请注意，二氧化碳的三相点高于大气压，因此最小有效压力会相应调整。使用二氧化碳作为工作流体时，请确保具有初始压力参数的连接模块（例如 Reservoir (2P) 模块）等于或大于此最小压力。

**Isobutane (R-600a)**

流体属性提供的压力范围为 0.0001 至 15 MPa，温度范围（在 1 个大气压下）为 121.02 至 516.64 K。

**Propane (R-290)**

流体属性提供的压力范围为 0.0001 至 18 MPa，温度范围（在 1 个大气压下）为 94.21 至 554.92 K。

### 可视化流体属性

要可视化网络流体的以下属性随比内能或比焓与压力的变化关系：

- 比容
- 比熵
- 温度
- 运动黏度
- 热导率
- 普朗特数

请右键单击模块并选择 **Fluids** > **Plot Fluid Properties (3D)**：

或 **Fluids** > **Plot Fluid Properties (Contours)**：

每当流体选择或流体参数发生变化时，使用 **Reload Data** 按钮重新生成绘图。
