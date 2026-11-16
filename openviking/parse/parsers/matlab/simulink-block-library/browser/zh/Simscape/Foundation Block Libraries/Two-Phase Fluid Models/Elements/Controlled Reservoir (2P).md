---
type: simulink-block
title: 'Controlled Reservoir (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'controlledreservoir2p'
documentation_source_path: 'ref/controlledreservoir2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Reservoir (2P)

## 端口

### 输入

### **P** — 压力控制信号，MPa 物理信号

提供储液器压力控制信号的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir pressure specification**
设置为 `Specified pressure`。

### **Tc** — 储液器冷凝温度控制信号，K 物理信号

提供储液器冷凝温度控制信号的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir pressure specification**
设置为 `Saturation pressure at specified condensing
  temperature`。

### **Te** — 储液器蒸发温度控制信号，K 物理信号

提供储液器蒸发温度控制信号的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir pressure specification**
设置为 `Saturation pressure at specified evaporating
  temperature`。

### **T** — 温度控制信号，K 物理信号

根据 **Reservoir energy specification** 参数设置，提供过冷液体温度或过热蒸气温度控制信号的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Subcooled liquid temperature` 或
`Superheated vapor temperature`。

### **X** — 蒸气质量分数控制信号，无量纲物理信号

指定储液器中蒸气质量分数的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Vapor quality`。

### **a** — 蒸气体积分数控制信号，无量纲物理信号

指定储液器中蒸气体积分数的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Vapor void fraction`。

### **H** — 流体比焓控制信号，kJ/kg 物理信号

指定储液器中流体比焓的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Specific enthalpy`。

### **U** — 流体比内能控制信号，kJ/kg 物理信号

指定储液器中流体比内能的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Specific internal energy`。

### **SC** — 流体过冷度控制信号，deltaK 物理信号

指定储液器中流体过冷度的物理信号端口，即液体饱和温度与流体温度之差。

此输入信号指定的是温度差，单位为
`deltaK`，而不是绝对温度。因此，如果将 Simulink-PS Converter 模块直接连接到此端口，请勿选中 **Apply affine conversion** 复选框。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Degree of subcooling`。

### **SH** — 流体过热度控制信号，deltaK 物理信号

指定储液器中流体过热度的物理信号端口，即流体温度与蒸气饱和温度之差。

此输入信号指定的是温度差，单位为
`deltaK`，而不是绝对温度。因此，如果将 Simulink-PS Converter 模块直接连接到此端口，请勿选中 **Apply affine conversion** 复选框。

#### 依赖关系

要启用此端口，请将 **Reservoir energy specification** 设置为
`Degree of superheating`。

### 守恒

### **A** — 储液器入口两相流体

与储液器入口关联的两相流体守恒端口。

## 参数

### **Reservoir pressure specification** — 储液器压力的指定方法 `Specified pressure`（默认）| `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

储液器压力的指定方法：

- `Specified pressure` — 使用端口 **P** 处的控制信号指定一个值。
- `Saturation pressure at specified condensing
  temperature` — 使用液体饱和曲线上与端口 **Tc** 处控制信号所指定温度对应的压力。选择此选项时，此模块将压力限制为小于或等于临界压力。
- `Saturation pressure at specified evaporating
  temperature` — 使用蒸气饱和曲线上与端口 **Te** 处控制信号所指定温度对应的压力。选择此选项时，此模块将压力限制为小于或等于临界压力。

### **Reservoir energy specification** — 用于定义储液器条件的热力学变量 `Subcooled liquid temperature`（默认）| `Superheated vapor temperature` | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy` | `Degree of subcooling` | `Degree of superheating`

用于能量指定的热力学变量：

- `Subcooled liquid temperature` — 使用端口 **T** 处的控制信号指定储液器内部过冷液体的温度。选择此选项时，此模块将压力限制为小于或等于临界压力。此模块还会将端口 **T** 处的输入限制在最低温度与液体饱和温度之间的范围内，以避免输入温度跨越饱和温度时相应比内能或比焓出现不连续。
- `Superheated vapor temperature` — 使用端口 **T** 处的控制信号指定储液器内部过热蒸气的温度。选择此选项时，此模块将压力限制为小于或等于临界压力。此模块还会将端口 **T** 处的输入限制在蒸气饱和温度与最高温度之间的范围内，以避免输入温度跨越饱和温度时相应比内能或比焓出现不连续。
- `Vapor quality` — 使用端口 **X** 处的控制信号指定储液器中蒸气的质量分数。选择此选项时，此模块将压力限制为小于或等于临界压力。您可以指定液-蒸气混合物的状态。您不能指定过冷液体或过热蒸气，因为在整个区域内蒸气质量分数分别为 0 和 1。此外，此模块将压力限制为低于临界压力。
- `Vapor void fraction` — 使用端口 **a** 处的控制信号指定储液器中蒸气的体积分数。选择此选项时，此模块将压力限制为小于或等于临界压力。您可以指定液-蒸气混合物的状态。您不能指定过冷液体或过热蒸气，因为在整个区域内蒸气质量分数分别为 0 和 1。此外，此模块将压力限制为低于临界压力。
- `Specific enthalpy` — 使用端口 **H** 处的控制信号指定储液器中流体的比焓。此选项不限制流体状态。
- `Specific internal energy` — 使用端口 **U** 处的控制信号指定储液器中流体的比内能。此选项不限制流体状态。
- `Degree of subcooling` — 使用端口 **SC** 处的控制信号指定储液器中流体的过冷度。过冷度是液体饱和温度与流体温度之差。选择此选项时，此模块将压力限制为小于或等于临界压力。
- `Degree of superheating` — 使用端口 **SH** 处的控制信号指定储液器中流体的过热度。过热度是流体温度与蒸气饱和温度之差。选择此选项时，此模块将压力限制为小于或等于临界压力。

### **Cross-sectional area at port A** — 储液器入口处垂直于流动路径的面积 `0.01 m^2`（默认）| 正标量

储液器入口的流动面积，由端口 **A** 表示。

### **Reservoir pressure above critical** — 定义当储液器压力超过临界压力时的操作 `Warn and limit to critical pressure`（默认）| `Limit to critical pressure` | `Error`

定义当储液器压力超过临界压力时的操作：

- `Warn and limit to critical pressure` — 此模块发出警告并将压力限制为临界压力。
- `Limit to critical pressure` — 此模块将压力限制为临界压力，但仿真会继续且不发出警告。
- `Error` — 仿真因错误而停止。

#### 依赖关系

当您选择要求储液器内部压力小于临界压力的压力指定和能量指定选项组合时，会自动显示此参数。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

可变压力和温度下的两相流体储液器

Reservoir (2P) 模块在两相流体网络中设置边界条件。储液器假定为无限大。

端口 **A** 表示储液器入口。端口 **A** 与储液器内部之间的流动阻力假定可忽略不计。因此，端口 **A** 处的压力等于储液器内部的压力。

储液器入口处的比焓和比内能取决于流动方向。流体以储液器压力和比内能离开储液器。流体以储液器压力进入储液器，但比内能由上游的两相流体网络决定。

此模块通过 **Reservoir pressure specification** 和 **Reservoir energy specification** 参数，提供压力指定和能量指定的独立选择。根据所选选项，此模块会显示相关输入端口，以提供所选量的控制信号。

对于某些选项组合，储液器内部的压力必须小于临界压力，因为饱和曲线在临界点以上未定义。如果选择此类组合，**Reservoir pressure above critical** 参数允许您决定当流体压力超过临界压力时发生的情况。

此模块还充当 Pressure & Internal Energy Sensor (2P) 模块的参考连接。在这种情况下，测得的压力和比内能相对于储液器压力和比内能。
