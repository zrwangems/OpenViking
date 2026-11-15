---
type: simulink-block
title: 'Two-Phase Fluid Predefined Properties (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Utilities'
documentation_page: 'twophasefluidpredefinedproperties2p'
documentation_source_path: 'ref/twophasefluidpredefinedproperties2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Phase Fluid Predefined Properties (2P)

## 端口

### 守恒

### **A** — 两相流体连接端口

两相流体守恒端口，将模块连接到网络。该端口连接到框图中两相连接线上的任意点。当您将 Two-Phase Fluid Predefined Properties (2P) 模块连接到网络管线时，流体属性会传播到回路中的所有模块。

## 参数

### **两相流体** — 工作流体 `Water (R-718)`（默认） | `Ammonia (R-717)` | `Carbon dioxide (R-744)` | `Isobutane (R-600a)` | `Propane (R-290)` | `R-1233zd(E)` | `R-1234yf` | `R-134a` | `R-22` | `R-32` | `R-404A` | `R-407C` | `R-410A`

预定义工作流体选项。

### **大气压力** — 环境压力 `0.101325` MPa（默认） | positive scalar

系统的环境压力。

### **压力与比内能超出有效范围** — 是否在压力或比内能超出有效范围时发出通知 `Error`（默认） | `Warning` | `None`

选择当流体压力或比内能在仿真期间超出有效范围时发生的情况：

- `None` ― 如果属性超出范围，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

### **流动反向的动态压力阈值** — 设置应用数值平滑的区域 `0.01` Pa（默认） | positive scalar

设置应用数值平滑的区域。在 **流动反向的动态压力阈值** 的正值和负值之间围绕 0 MPa 定义一个过渡区域。在此过渡区域内，调整计算得到的属性以确保平滑过渡。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2024b：使用新的预定义两相流体

现在可以在两相域中将 Propane (R-290)、R-32 和 R-1233zd(E) 建模为预定义流体。

### R2023a：在仿真期间流体属性超出范围时控制模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在，您可以使用新的 **压力与比内能超出有效范围** 参数来控制流体属性在仿真期间超出范围时的模块行为。

## 描述

用于两相网络的预定义工作流体

Two-Phase Fluid Predefined Properties (2P) 模块设置两相系统的工作流体属性。可用的预定义流体包括：

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

如果您想指定自己的工作流体属性，请使用 Foundation Library Two-Phase Fluid Properties (2P) 模块。如果未指定流体，将应用系统默认值。有关更多详细信息，请参阅指定流体属性。

### 流体属性范围

**Water (R-718)**

流体属性针对 0.001 至 95 MPa 的压力范围以及（在 1 个大气压下的）273.16 至 1,245.8 K 的温度范围提供。

**R-134a**

流体属性针对 0.001 至 5.5 MPa 的压力范围以及（在 1 个大气压下的）177.08 至 424.4 K 的温度范围提供。

**R-1234yf**

流体属性针对 0.04 至 3.2 MPa 的压力范围以及（在 1 个大气压下的）223.52 至 387.45 K 的温度范围提供。

**R-1233zd(E)**

流体属性针对 0.001 至 9 MPa 的压力范围以及（在 1 个大气压下的）202.29 至 500.24 K 的温度范围提供。

**R-404A**

流体属性针对 0.003 至 12 MPa 的压力范围以及（在 1 个大气压下的）171.6 至 550.94 K 的温度范围提供。

**R-410A**

流体属性针对 0.001 至 6 MPa 的压力范围以及（在 1 个大气压下的）146.19 至 427.25 K 的温度范围提供。

**R-407C**

流体属性针对 0.001 至 6 MPa 的压力范围以及（在 1 个大气压下的）158.85 至 427.92 K 的温度范围提供。

**R-22**

流体属性针对 0.001 至 8 MPa 的压力范围以及（在 1 个大气压下的）120.77 至 519.49 K 的温度范围提供。

**R-32**

流体属性针对 0.0001 至 7 MPa 的压力范围以及（在 1 个大气压下的）138.91 至 375.55 K 的温度范围提供。

**Ammonia (R-717)**

流体属性针对 0.008 至 95 MPa 的压力范围以及（在 1 个大气压下的）195.5 至 543.9 K 的温度范围提供。

**Carbon dioxide (R-744)**

流体属性针对 0.55 至 50 MPa 的压力范围以及（在 1 MPa 下的）216.94 至 1,389.4 K 的温度范围提供。请注意，二氧化碳的三相点高于大气压力，因此最小有效压力会相应调整。当使用二氧化碳作为工作流体时，请确保具有初始压力参数的连接模块（例如 Reservoir (2P) 模块）等于或大于此最小压力。

**Isobutane (R-600a)**

流体属性针对 0.0001 至 15 MPa 的压力范围以及（在 1 个大气压下的）121.02 至 516.64 K 的温度范围提供。

**Propane (R-290)**

流体属性针对 0.0001 至 18 MPa 的压力范围以及（在 1 个大气压下的）94.21 至 554.92 K 的温度范围提供。

### 可视化流体属性

要可视化网络流体的以下内容（作为比内能或比焓与压力的函数）：

- 比体积
- 比熵
- 温度
- 运动黏度
- 导热系数
- 普朗特数

请右键单击模块并选择 **Fluids** > **Plot Fluid Properties (3D)**：

或 **Fluids** > **Plot Fluid Properties (Contours)**：

使用 **Reload Data** 按钮，在流体选择或流体参数发生变化时重新生成绘图。
