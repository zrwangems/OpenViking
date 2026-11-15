---
type: simulink-block
title: 'Flow Rate Source (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Sources'
documentation_page: 'flowratesource2p'
documentation_source_path: 'ref/flowratesource2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Source (2P)

## 端口

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过源的质量流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为 `Controlled`，并将 **Flow rate type** 设置为 `Mass flow rate`。

### **V** — 体积流量控制信号，m^3/s 物理信号

输入物理信号，用于指定通过源的体积流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为 `Controlled`，并将 **Flow rate type** 设置为 `Volumetric flow rate`。

### 守恒

### **A** — 源入口两相流体

两相流体守恒端口。正流量导致流体从端口 **A** 流向端口 **B**。

### **B** — 源出口两相流体

两相流体守恒端口。正流量导致流体从端口 **A** 流向端口 **B**。

## 参数

### **Source type** — 选择流量是否可在仿真期间变化 `Controlled`（默认）| `Constant`

选择源生成的流量是否可以在仿真期间变化：

- `Controlled` — 流量是可变的，由输入物理信号控制。选择此选项会显示输入端口 **M** 或 **V**，具体取决于 **Flow rate type** 参数的值。
- `Constant` — 流量在仿真期间恒定，由模块参数指定。选择此选项会启用 **Mass flow rate** 或 **Volumetric flow rate** 参数，具体取决于 **Flow rate type** 参数的值。

### **Flow rate type** — 选择源生成质量流量还是体积流量 `Mass flow rate`（默认）| `Volumetric flow rate`

选择流量类型，`Mass flow rate` 或 `Volumetric flow rate`。

### **Mass flow rate** — 通过源的恒定质量流量 `0 kg/s`（默认）

期望通过源的流体质量流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`，并将 **Flow rate type** 设置为 `Mass flow rate`。

### **Volumetric flow rate** — 通过源的恒定体积流量 `0 m^3/s`（默认）

期望通过源的流体体积流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`，并将 **Flow rate type** 设置为 `Volumetric flow rate`。

### **Power added** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对流体流动做功：

- `Isentropic` — 源对流体执行等熵功，以维持指定的质量流量。使用此选项表示理想化的泵或压缩机，并正确考虑能量输入和输出，尤其是在闭环系统中。
- `None` — 源不对流动做功，既不添加也不移除功率，无论源产生的质量流量如何。使用此选项可在系统上游设置所需的流动条件，而不影响流动的温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **A** 处垂直于流动路径的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **B** 处垂直于流动路径的面积。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2023b: 两相流体源的可用性增强

在 R2023b 中，单独的 Mass Flow Rate Source (2P)、Controlled Mass Flow Rate Source (2P)、Volumetric Flow Rate Source (2P) 和 Controlled Volumetric Flow Rate Source (2P) 模块已合并为一个 Flow Rate Source (2P) 模块，允许您选择生成恒定或时变的质量流量或体积流量。新模块允许您使用模块参数配置模块，并仅公开特定模型中所需的输入端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改没有兼容性影响。当您打开现有模型时，旧模块会自动替换为具有相应配置的 Flow Rate Source (2P) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Mass Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.controlled_mass_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source;` |
| Mass Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.mass_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source(source_type=foundation.enum.constant_controlled.constant);` |
| Controlled Volumetric Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.controlled_volumetric_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source(flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |
| Volumetric Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.volumetric_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source(source_type=foundation.enum.constant_controlled.constant,flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |

## 描述

在两相流体网络中生成恒定或时变的质量流量或体积流量

Flow Rate Source (2P) 模块表示两相流体网络中的理想机械能源。该源可以维持指定的质量流量或体积流量，而不受压差影响。没有流动阻力，也不与环境进行热交换。您使用 **Flow rate type** 参数指定流量类型。

模块图标根据 **Source type** 和 **Flow rate type** 参数的值而变化。

端口 **A** 和 **B** 表示源的入口和出口。端口 **M** 或 **V**（取决于流量类型）处的输入物理信号指定流量。或者，您可以将固定流量指定为模块参数。正流量导致气体从端口 **A** 流向端口 **B**。

### 质量平衡

源中流体的体积被视为可忽略，并且在模型中被忽略。端口之间没有流体积累，因此流入源的所有质量流量之和必须等于零：

m˙A+​m˙B=0,

其中 m˙ 表示通过端口流入源的质量流量。

当您将 **Flow rate type** 参数设置为 `Volumetric flow rate` 时，端口 **A** 处的质量流量根据体积流量计算：

mA.={V˙vB,if V˙≥0V˙vA,otherwise,

其中 V˙ 是体积流量，*v* 是比体积。

### 能量平衡

默认情况下，源通过对流入流体执行等熵功来维持指定的流量，不过该模块提供了忽略此项的选项。如果在模型中考虑源做功的速率，则该速率必须等于通过端口的能量流量之和：

ϕA+​ϕB+​ϕWork=0,

其中 *ϕ* 表示通过端口或通过做功进入源的能量流量。由做功引起的能量流量等于源产生的功率。其值根据端口处的比总焓计算：

ϕWork=m˙A(hA−hB).

比总焓 *h* 定义为：

h\*=u\*+p\*v\*+12(m˙\*v\*S)2,

其中星号表示端口（**A** 或 **B**），并且：

- *u* 是比内能。
- *p* 是压力。
- *S* 是流通面积。

方程中的比内能来自 Two-Phase Fluid Properties (2P) 模块的表格数据。其值由源所做功为等熵这一约束唯一确定。于是，作为比内能函数的比熵在端口 **A** 和 **B** 处必须具有相同的值：

sA(pA,uA)=sB(pB,uB),

其中 *s* 是比熵。如果 **Power added** 参数设置为 `None`，则端口处的比总焓具有相同的值 (hA=hB)，并且源所做的功降为零 (ϕWork=0)。

### 假设和限制

- 没有不可逆损失。
- 与环境没有热交换。
