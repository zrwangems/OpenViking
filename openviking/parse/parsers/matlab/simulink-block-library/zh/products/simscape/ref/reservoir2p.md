---
type: simulink-block
title: 'Reservoir (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'reservoir2p'
documentation_source_path: 'ref/reservoir2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (2P)

## 端口

### 守恒

### **A** — 储液器入口两相流体

与储液器入口关联的两相流体守恒端口。

## 参数

### **Reservoir pressure specification** — 储液器压力的指定方法 `Atmospheric pressure`（默认） | `Specified pressure` | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

用于储液器压力的指定方法：

- `Atmospheric pressure` — 使用连接到回路的两相流体属性 Two-Phase Fluid Properties (2P) 模块所指定的大气压。
- `Specified pressure` — 使用 **Reservoir pressure** 参数指定值。
- `Saturation pressure at specified condensing temperature` — 使用液相饱和曲线上与 **Reservoir condensing temperature** 参数指定的温度相对应的压力。
- `Saturation pressure at specified evaporating temperature` — 使用气相饱和曲线上与使用 **Reservoir evaporating temperature** 参数指定的温度相对应的压力。

### **Reservoir pressure** — 储液器中的压力 `0.101325 MPa`（默认） | positive scalar

储液器内部的绝对压力。该压力在仿真期间保持恒定。默认值对应于平均海平面处的大气压。

#### 依赖项

要启用此参数，请将 **Reservoir pressure specification** 设置为 `Specified pressure`。

### **Reservoir condensing temperature** — 以冷凝温度表示饱和压力 `373.15 K`（默认） | positive scalar

储液器内流体的压力等于液相饱和曲线上与此冷凝温度相对应的饱和压力。冷凝温度必须低于临界温度，因为饱和曲线在临界点以上未定义。

#### 依赖项

要启用此参数，请将 **Reservoir pressure specification** 设置为 `Saturation pressure at specified condensing temperature`。

### **Reservoir evaporating temperature** — 以蒸发温度表示饱和压力 `373.15 K`（默认） | positive scalar

储液器内流体的压力等于气相饱和曲线上与此蒸发温度相对应的饱和压力。蒸发温度必须低于临界温度，因为饱和曲线在临界点以上未定义。

#### 依赖项

要启用此参数，请将 **Reservoir pressure specification** 设置为 `Saturation pressure at specified evaporating temperature`。

### **Reservoir energy specification** — 用于定义储液器条件的热力学变量 `Temperature`（默认） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy` | `Degree of subcooling` | `Degree of superheating`

用于能量指定的热力学变量：

- `Temperature` — 使用 **Reservoir temperature** 参数指定储液器内部的绝对温度。可以指定过冷液体或过热蒸汽状态。无法指定液-汽混合物，因为温度在液-汽混合物区域中是恒定的。
- `Vapor quality` — 使用 **Reservoir vapor quality** 参数指定储液器中蒸汽的质量分数。仅当压力低于临界压力时才能使用此选项，因为该量在临界点以上不存在。可以指定液-汽混合物状态。无法指定过冷液体或过热蒸汽，因为在整个区域内蒸汽干度分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 使用 **Reservoir void fraction** 参数指定储液器中蒸汽的体积分数。仅当压力低于临界压力时才能使用此选项，因为该量在临界点以上不存在。可以指定液-汽混合物状态。无法指定过冷液体或过热蒸汽，因为在整个区域内蒸汽干度分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 使用 **Reservoir specific enthalpy** 参数指定储液器中流体的比焓。此选项不限制流体状态。
- `Specific internal energy` — 使用 **Reservoir specific internal energy** 参数指定储液器中流体的比内能。此选项不限制流体状态。
- `Degree of subcooling` — 使用 **Reservoir subcooling** 参数指定储液器中流体的过冷度。仅当压力低于临界压力时才能使用此选项，因为饱和曲线在临界点以上未定义。
- `Degree of superheating` — 使用 **Reservoir superheating** 参数指定储液器中流体的过热度。仅当压力低于临界压力时才能使用此选项，因为饱和曲线在临界点以上未定义。

### **Reservoir temperature** — 储液器中的温度 `293.15 K`（默认） | positive scalar

储液器内部的绝对温度。该温度在仿真期间保持恒定。指定温度映射到过冷液体区域或过热蒸汽区域中的比焓。对于大多数流体，P-H 图中的液-汽混合物区域温度是恒定的，因此温度值在液-汽混合物区域内与比焓值并非一一对应。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Temperature`。

### **Reservoir vapor quality** — 储液器中蒸汽的质量分数 `0.5`（默认） | scalar in range [0 1]

储液器中蒸汽的质量分数。该值在仿真期间保持恒定。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Vapor quality`。

### **Reservoir vapor void fraction** — 储液器中蒸汽的体积分数 `0.5`（默认） | scalar in range [0 1]

储液器中蒸汽的体积分数。该值在仿真期间保持恒定。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Vapor void fraction`。

### **Reservoir specific enthalpy** — 储液器中流体的比焓 `1500 kJ/kg`（默认） | positive scalar

储液器中流体的比焓。该值在仿真期间保持恒定。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Specific enthalpy`。

### **Reservoir specific internal energy** — 储液器中流体的比内能 `1500 kJ/kg`（默认） | positive scalar

储液器中流体的比内能。该值在仿真期间保持恒定。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Specific internal energy`。

### **Reservoir subcooling** — 储液器中的过冷度 `5 deltaK`（默认） | positive scalar

储液器中流体的过冷度，即液体饱和温度与流体温度之差。该值在仿真期间保持恒定。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Degree of subcooling`。

### **Reservoir superheating** — 储液器中的过热度 `5 deltaK`（默认） | positive scalar

储液器中流体的过热度，即流体温度与蒸汽饱和温度之差。该值在仿真期间保持恒定。

#### 依赖项

要启用此参数，请将 **Reservoir energy specification** 设置为 `Degree of superheating`。

### **Cross-sectional area at port A** — 储液器入口处垂直于流道的面积 `0.01 m^2`（默认） | positive scalar

储液器入口的流通面积，由端口 **A** 表示。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

Reservoir (2P) 模块在两相流体网络中设置压力和温度边界条件。储液器假定为无限大，使其压力和比内能保持恒定。

端口 **A** 表示储液器入口。端口 **A** 与储液器内部之间的流阻假定可忽略。因此，端口 **A** 处的压力等于储液器内部的压力。

储液器入口处的比焓和比内能取决于流动方向。流体在储液器压力和比内能下离开储液器。流体在储液器压力下进入储液器，但比内能由上游的两相流体网络确定。

该模块通过 **Reservoir pressure specification** 和 **Reservoir energy specification** 参数，提供压力指定和能量指定的独立选择。根据所选选项，该模块会公开其他参数，用于为所选量指定值。

该模块还用作 Pressure & Internal Energy Sensor (2P) 模块的参考连接。在这种情况下，测得的压力和比内能相对于储液器压力和比内能。

### 假设和限制

- 假定储液器内流体的压力和比内能保持恒定。
- 端口 **A** 与储液器内部之间的流阻可忽略。端口 **A** 处和储液器内部的压力相同。
