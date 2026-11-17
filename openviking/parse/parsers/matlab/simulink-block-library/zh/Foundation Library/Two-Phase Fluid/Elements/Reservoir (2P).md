---
type: simulink-block
title: 'Reservoir (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'reservoir2p'
documentation_source_path: 'ref/reservoir2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (2P)

## 端口

### 守恒端口

### **A** — 储液器入口两相流体

与储液器入口关联的两相流体守恒端口。

## 参数

### **Reservoir pressure specification** — 储液器压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure` | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

储液器压力的指定方法：

- `Atmospheric pressure` — 使用连接到回路的两相流体属性 (2P) 模块所指定的大气压。
- `Specified pressure` — 通过 **Reservoir pressure** 参数指定一个值。
- `Saturation pressure at specified condensing temperature` — 使用液体饱和曲线上与 **Reservoir condensing temperature** 参数所指定温度对应的压力。
- `Saturation pressure at specified evaporating temperature` — 使用蒸气饱和曲线上与 **Reservoir evaporating temperature** 参数所指定温度对应的压力。

### **Reservoir pressure** — 储液器中的压力 `0.101325 MPa`（默认）| 正标量

储液器内部的绝对压力。该压力在仿真过程中保持恒定。默认值对应于平均海平面处的大气压。

#### 依赖关系

要启用此参数，请将 **Reservoir pressure specification** 设置为 `Specified pressure`。

### **Reservoir condensing temperature** — 以冷凝温度指定饱和压力 `373.15 K`（默认）| 正标量

储液器内流体的压力等于液体饱和曲线上与该冷凝温度对应的饱和压力。冷凝温度必须低于临界温度，因为饱和曲线在临界点以上未定义。

#### 依赖关系

要启用此参数，请将 **Reservoir pressure specification** 设置为 `Saturation pressure at specified condensing temperature`。

### **Reservoir evaporating temperature** — 以蒸发温度指定饱和压力 `373.15 K`（默认）| 正标量

储液器内流体的压力等于蒸气饱和曲线上与该蒸发温度对应的饱和压力。蒸发温度必须低于临界温度，因为饱和曲线在临界点以上未定义。

#### 依赖关系

要启用此参数，请将 **Reservoir pressure specification** 设置为 `Saturation pressure at specified evaporating temperature`。

### **Reservoir energy specification** — 用于定义储液器条件的热力学变量 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy` | `Degree of subcooling` | `Degree of superheating`

用于能量指定的热力学变量：

- `Temperature` — 通过 **Reservoir temperature** 参数指定储液器内部的绝对温度。您可以指定过冷液体或过热蒸气状态。您不能指定液-气混合物，因为在液-气混合物区域温度是恒定的。
- `Vapor quality` — 通过 **Reservoir vapor quality** 参数指定储液器中蒸气的质量分数。仅当压力低于临界压力时才能使用此选项，因为该量在临界点以上不存在。您可以指定液-气混合物状态。您不能指定过冷液体或过热蒸气，因为在整个区域内蒸气干度分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 通过 **Reservoir void fraction** 参数指定储液器中蒸气的体积分数。仅当压力低于临界压力时才能使用此选项，因为该量在临界点以上不存在。您可以指定液-气混合物状态。您不能指定过冷液体或过热蒸气，因为在整个区域内蒸气干度分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 通过 **Reservoir specific enthalpy** 参数指定储液器中流体的比焓。此选项不限制流体状态。
- `Specific internal energy` — 通过 **Reservoir specific internal energy** 参数指定储液器中流体的比内能。此选项不限制流体状态。
- `Degree of subcooling` — 通过 **Reservoir subcooling** 参数指定储液器中流体的过冷度。仅当压力低于临界压力时才能使用此选项，因为饱和曲线在临界点以上未定义。
- `Degree of superheating` — 通过 **Reservoir superheating** 参数指定储液器中流体的过热度。仅当压力低于临界压力时才能使用此选项，因为饱和曲线在临界点以上未定义。

### **Reservoir temperature** — 储液器中的温度 `293.15 K`（默认）| 正标量

储液器内部的绝对温度。该温度在仿真期间保持恒定。指定的温度映射到过冷液体区域或过热蒸气区域中的特定比焓。对于大多数流体，P-H 图中液-气混合物区域的温度是恒定的，因此温度值在液-气混合物区域内与比焓值并非一一对应。

#### 依赖关系

要启用此参数，请将 **Reservoir energy specification** 设置为 `Temperature`。

### **Reservoir vapor quality** — 储液器中蒸气的质量分数 `0.5`（默认）| 范围 [0 1] 内的标量

储液器中蒸气的质量分数。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **Reservoir energy specification** 设置为 `Vapor quality`。

### **Reservoir vapor void fraction** — 储液器中蒸气的体积分数 `0.5`（默认）| 范围 [0 1] 内的标量

储液器中蒸气的体积分数。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **储液器能量规格** 设置为 `Vapor void fraction`。

### **储液器比焓** — 储液器中流体的比焓 `1500 kJ/kg`（默认）| 正标量

储液器中流体的比焓。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **储液器能量规格** 设置为 `Specific enthalpy`。

### **储液器比内能** — 储液器中流体的比内能 `1500 kJ/kg`（默认）| 正标量

储液器中流体的比内能。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **储液器能量规格** 设置为 `Specific internal energy`。

### **储液器过冷度** — 储液器中的过冷度 `5 deltaK`（默认）| 正标量

储液器中流体的过冷度，即液体饱和温度与流体温度之间的差值。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **储液器能量规格** 设置为 `Degree of subcooling`。

### **储液器过热度** — 储液器中的过热度 `5 deltaK`（默认）| 正标量

储液器中流体的过热度，即流体温度与蒸汽饱和温度之间的差值。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **储液器能量规格** 设置为 `Degree of superheating`。

### **端口 A 处的横截面积** — 储液器入口处垂直于流路的面积 `0.01 m^2`（默认）| 正标量

储液器入口的流通面积，由端口 **A** 表示。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

恒温恒压两相流体储液器

Reservoir (2P) 模块在两相流体网络中设置压力和温度边界条件。储液器假定为无限大，使其压力和比内能保持恒定。

端口 **A** 表示储液器入口。端口 **A** 与储液器内部之间的流动阻力假定可忽略不计。因此，端口 **A** 处的压力等于储液器内部的压力。

储液器入口处的比焓和比内能取决于流动方向。流体以储液器压力和比内能离开储液器。流体以储液器压力进入储液器，但比内能由上游的两相流体网络决定。

该模块通过 **储液器压力规格** 和 **储液器能量规格** 参数提供压力规格和能量规格的独立选择。根据所选选项，模块会公开附加参数以指定所选量的值。

该模块还用作 Pressure & Internal Energy Sensor (2P) 模块的参考连接。在这种情况下，测得的压力和比内能相对于储液器压力和比内能。

### 假设和限制

- 假定储液器中流体的压力和比内能恒定。
- 端口 **A** 与储液器内部之间的流动阻力可忽略不计。端口 **A** 处的压力与储液器内部的压力相同。
