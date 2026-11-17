---
type: simulink-block
title: 'Flow Rate Source (TL)'
family: 'thermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Sources'
documentation_page: 'flowratesourcetl'
documentation_source_path: 'ref/flowratesourcetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Source (TL)

## 端口

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过源的质量流量。

#### 依赖关系

要启用此端口，请将 **源类型** 参数设置为 `Controlled`，并将 **流量类型** 设置为 `Mass flow rate`。

### **V** — 体积流量控制信号，m^3/s 物理信号

输入物理信号，用于指定通过源的体积流量。

#### 依赖关系

要启用此端口，请将 **源类型** 参数设置为 `Controlled`，并将 **流量类型** 设置为 `Volumetric flow rate`。

### 守恒

### **A** — 源入口热液体

热液体守恒端口。正流量使流体从端口 **A** 流向端口 **B**。

### **B** — 源出口热液体

热液体守恒端口。正流量使流体从端口 **A** 流向端口 **B**。

## 参数

### **源类型** — 选择仿真期间流量是否可以变化 `Controlled` (默认) | `Constant`

选择源生成的流量在仿真期间是否可以变化：

- `Controlled` — 流量是可变的，由输入物理信号控制。选择此选项会暴露输入端口 **M** 或 **V**，具体取决于 **流量类型** 参数的值。
- `Constant` — 流量在仿真期间恒定，由模块参数指定。选择此选项会启用 **质量流量** 或 **体积流量** 参数，具体取决于 **流量类型** 参数的值。

### **流量类型** — 选择源生成质量流量还是体积流量 `Mass flow rate` (默认) | `Volumetric flow rate`

选择流量类型：`Mass flow rate` 或 `Volumetric flow rate`。

### **质量流量** — 通过源的恒定质量流量 `0 kg/s` (默认)

期望通过源的流体质量流量。

#### 依赖关系

要启用此参数，请将 **源类型** 设置为 `Constant`，并将 **流量类型** 设置为 `Mass flow rate`。

### **体积流量** — 通过源的恒定体积流量 `0 m^3/s` (默认)

期望通过源的流体体积流量。

#### 依赖关系

要启用此参数，请将 **源类型** 设置为 `Constant`，并将 **流量类型** 设置为 `Volumetric flow rate`。

### **添加的功率** — 选择源是否做功 `Isentropic` (默认) | `None`

选择源是否对流体流动做功：

- `Isentropic` — 源对流体做等熵功，以维持指定的质量流量。使用此选项可表示理想化的泵或压缩机，并正确计入能量输入和输出，尤其是在闭环系统中。
- `None` — 源对流动不做功，既不增加也不移除功率，无论源产生的质量流量是多少。使用此选项可在系统上游设置所需的流动条件，而不影响流动的温度。

### **端口 A 和 B 处的横截面积** — 入口和出口处垂直于流道的面积 `0.01 m^2` (默认)

源入口和出口处垂直于流道的面积。假定这两个横截面积相同。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2023b: 热液体源的可用性增强

在 R2023b 中，单独的 Mass Flow Rate Source (TL)、Controlled Mass Flow Rate Source (TL)、Volumetric Flow Rate Source (TL) 和 Controlled Volumetric Flow Rate Source (TL) 模块已合并为一个 Flow Rate Source (TL) 模块，您可以在生成恒定或时变的质量流量或体积流量之间进行选择。新模块允许您使用模块参数配置模块，并仅暴露特定模型中所需的输入端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改没有兼容性影响。打开现有模型时，旧模块会自动替换为采用相应配置的 Flow Rate Source (TL) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Mass Flow Rate Source (TL) | `source = foundation.thermal_liquid.sources.controlled_mass_flow_source;` | `source = foundation.thermal_liquid.sources.flow_source;` |
| Mass Flow Rate Source (TL) | `source = foundation.thermal_liquid.sources.mass_flow_source;` | `source = foundation.thermal_liquid.sources.flow_source(source_type=foundation.enum.constant_controlled.constant);` |
| Controlled Volumetric Flow Rate Source (TL) | `source = foundation.thermal_liquid.sources.controlled_volumetric_flow_source;` | `source = foundation.thermal_liquid.sources.flow_source(flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |
| Volumetric Flow Rate Source (TL) | `source = foundation.thermal_liquid.sources.volumetric_flow_source;` | `source = foundation.thermal_liquid.sources.flow_source(source_type=foundation.enum.constant_controlled.constant,flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |

### R2023a: 配置流动条件而不影响温度

该模块包含 **添加的功率** 参数，它允许您指定源是否对流体流动做功。默认选项 `Isentropic power` 等效于之前版本中的模块行为。使用新的 `None` 选项可在系统上游设置所需的流动条件，而不影响流动的温度。

## 描述

在热液体网络中生成恒定或时变的质量流量或体积流量

Flow Rate Source (TL) 模块表示热液体网络中的理想机械能源。无论压差如何，该源都能维持指定的质量流量或体积流量。没有流动阻力，也没有与环境的热交换。您可以使用 **流量类型** 参数指定流量类型。

模块图标会根据 **源类型** 和 **流量类型** 参数的值而变化。

端口 **A** 和 **B** 表示源的入口和出口。端口 **M** 或 **V** 处的输入物理信号（取决于流量类型）指定流量。或者，您可以将固定流量指定为模块参数。正流量使气体从端口 **A** 流向端口 **B**。

体积流量和质量流量通过以下表达式关联

m˙={ρBV˙当 V˙≥0ρAV˙当 V˙<0

其中：

- *m˙* 是从端口 **A** 到端口 **B** 的质量流量。
- *ρ*A 和 *ρ*B 分别是端口 **A** 和 **B** 处的密度。
- *V˙* 是体积流量。

源处的能量平衡是流经端口 **A** 和 **B** 的能量流率以及对流体所做功的函数：

ϕA+ϕB+ϕwork=0,

其中：

- *ϕ*A 是通过端口 **A** 流入源的能量流率。
- *ϕ*B 是通过端口 **B** 流入源的能量流率。
- *ϕ*work 是对流体所做的等熵功。

等熵功项为

ϕwork=m˙(pB−pA)ρavg,

其中：

- *ϕ*work 是对热液体所做的等熵功。
- *p*A 是端口 **A** 处的压力。
- *p*B 是端口 **B** 处的压力。
- *ρ*avg 是平均液体密度，

  ρavg=ρA+ρB2.

### 假设和限制

- 不存在不可逆损失。
- 与环境没有热交换。
