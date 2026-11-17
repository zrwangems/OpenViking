---
type: simulink-block
title: 'Flow Rate Source (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sources'
documentation_page: 'flowratesource2p'
documentation_source_path: 'ref/flowratesource2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Source (2P)

## 端口
```yaml
ports:
- name: M
  summary: 质量流量控制信号，kg/s 物理信号
  direction: input
- name: V
  summary: 体积流量控制信号，m^3/s 物理信号
  direction: input
- name: A
  summary: 源入口两相流体
  direction: input
- name: B
  summary: 源出口两相流体
  direction: input
```

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过源的 mass flow rate。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`，并将 **Flow rate type** 设置为
`Mass flow rate`。

### **V** — 体积流量控制信号，m^3/s 物理信号

输入物理信号，用于指定通过源的 volumetric flow rate。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`，并将 **Flow rate type** 设置为
`Volumetric flow rate`。
### 守恒

### **A** — 源入口两相流体

两相流体守恒端口。正流量使流体从端口 **A** 流向端口 **B**。

### **B** — 源出口两相流体

两相流体守恒端口。正流量使流体从端口 **A** 流向端口 **B**。
## 参数
```yaml
parameters:
- name: Source type
  summary: 选择流量在仿真期间是否可以变化 Controlled（默认）| Constant
  group: ''
- name: Flow rate type
  summary: 选择源生成质量流量还是体积流量 Mass flow rate（默认）| Volumetric flow rate
  group: ''
- name: Mass flow rate
  summary: 通过源的恒定质量流量 0 kg/s（默认）
  group: ''
- name: Volumetric flow rate
  summary: 通过源的恒定体积流量 0 m^3/s（默认）
  group: ''
- name: Power added
  summary: 选择源是否做功 Isentropic（默认）| None
  group: ''
- name: Cross-sectional area at port A
  summary: 端口 A 处垂直于流动路径的面积 0.01 m^2（默认）
  group: ''
- name: Cross-sectional area at port B
  summary: 端口 B 处垂直于流动路径的面积 0.01 m^2（默认）
  group: ''
```

### **Source type** — 选择流量在仿真期间是否可以变化 `Controlled`（默认）| `Constant`

选择源生成的流量在仿真期间是否可以变化：

- `Controlled` — 流量是可变的，
  由输入物理信号控制。选择此选项将显示输入端口
  **M** 或 **V**，具体取决于
  **Flow rate type** 参数的值。
- `Constant` — 流量在仿真期间是恒定的，
  由模块参数指定。选择此选项将启用
  **Mass flow rate** 或 **Volumetric flow rate**
  参数，具体取决于 **Flow rate type**
  参数的值。

### **Flow rate type** — 选择源生成质量流量还是体积流量 `Mass flow rate`（默认）| `Volumetric flow rate`

选择流量类型，`Mass flow rate` 或
`Volumetric flow rate`。

### **Mass flow rate** — 通过源的恒定质量流量 `0 kg/s`（默认）

通过源的流体的期望质量流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`，并将 **Flow rate type** 设置为
`Mass flow rate`。

### **Volumetric flow rate** — 通过源的恒定体积流量 `0 m^3/s`（默认）

通过源的流体的期望体积流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`，并将 **Flow rate type** 设置为
`Volumetric flow rate`。

### **Power added** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对流体流动做功：

- `Isentropic` — 源对流体执行等熵
  功，以维持指定的质量流量。使用此选项可
  表示理想化的泵或压缩机，并正确考虑能量输入
  和输出，尤其是在闭环系统中。
- `None` — 源不对
  流动做功，无论源产生的质量流量如何，既不添加也不移除功率。使用此选项可在
  系统上游设置所需的流动条件，而不影响
  流动的温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **A** 处垂直于流动路径的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **B** 处垂直于流动路径的面积。
## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2023b: 两相流体源的可用性增强

在 R2023b 中，独立的 Mass Flow Rate Source (2P)、Controlled Mass
Flow Rate Source (2P)、Volumetric Flow Rate Source (2P) 和
Controlled Volumetric Flow Rate Source (2P) 模块已合并为单个 Flow Rate Source (2P) 模块，允许您在生成恒定或时变质量流量或体积流量之间进行选择。新模块允许您使用模块参数来配置模块，并仅暴露特定模型中所需的输入端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改不会产生兼容性影响。当您打开现有模型时，旧模块会自动替换为具有相应配置的 Flow Rate Source (2P) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Mass Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.controlled_mass_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source;` |
| Mass Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.mass_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source(source_type=foundation.enum.constant_controlled.constant);` |
| Controlled Volumetric Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.controlled_volumetric_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source(flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |
| Volumetric Flow Rate Source (2P) | `source = foundation.two_phase_fluid.sources.volumetric_flow_source;` | `source = foundation.two_phase_fluid.sources.flow_source(source_type=foundation.enum.constant_controlled.constant,flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |

## 描述

在两相流体网络中生成恒定或时变质量流量或体积流量

Flow Rate Source (2P) 模块表示两相流体网络中的理想机械能源。该源可以维持指定的质量流量或体积流量，而不受压差影响。没有流动阻力，也没有与环境的热交换。您可以使用 **Flow rate type** 参数指定流量类型。

模块图标会根据 **Source type** 和 **Flow rate type** 参数的值而变化。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **M** 或 **V** 处的输入物理信号（取决于流量类型）指定流量。或者，您可以将固定流量指定为模块参数。正流量使气体从端口 **A** 流向端口 **B**。

### 质量平衡

源中的流体体积被视为可忽略不计，并在模型中被忽略。端口之间没有流体积累，因此流入源的所有质量流量之和必须等于零：

m˙A+​m˙B=0,

其中 m˙ 表示通过端口流入源的质量流量。

当您将 **Flow rate type** 参数设置为 `Volumetric
flow rate` 时，端口 **A** 处的质量流量根据体积流量计算：

mA.={V˙vB,if V˙≥0V˙vA,otherwise,

其中 V˙ 是体积流量，*v* 是比体积。

### Energy Balance

默认情况下，源通过对流入流体执行等熵功来维持指定的流量，不过该模块提供了忽略此项的选项。如果在模型中考虑源做功的速率，则其必须等于通过各端口的能量流率之和：

ϕA+​ϕB+​ϕWork=0，

其中 *ϕ* 表示通过端口或以做功方式进入源的能量流率。由做功引起的能量流率等于源产生的功率。其值由各端口处的比总焓计算得到：

ϕWork=m˙A(hA−hB)。

比总焓 *h* 定义为：

h\*=u\*+p\*v\*+12(m˙\*v\*S)2，

其中星号表示端口（**A** 或 **B**），并且：

- *u* 是比内能。
- *p* 是压力。
- *S* 是流通面积。

方程中的比内能来自 Two-Phase Fluid Properties (2P) 模块的表格数据。其值由源所做的功为等熵这一约束唯一确定。比熵是比内能的函数，因此在端口 **A** 和 **B** 处必须具有相同的值：

sA(pA,uA)=sB(pB,uB)，

其中 *s* 是比熵。如果 **Power added** 参数设置为 `None`，则各端口处的比总焓具有相同的值（hA=hB），并且源所做的功降为零（ϕWork=0）。

### 假设和限制

- 不存在不可逆损失。
- 与环境之间没有热交换。
