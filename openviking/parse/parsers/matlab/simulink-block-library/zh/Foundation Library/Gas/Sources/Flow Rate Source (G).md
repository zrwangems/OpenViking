---
type: simulink-block
title: 'Flow Rate Source (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sources'
documentation_page: 'flowratesourceg'
documentation_source_path: 'ref/flowratesourceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Source (G)

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
  summary: 源入口气体
  direction: conserving
- name: B
  summary: 源出口气体
  direction: conserving
```

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过该源的气体质量流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`，并将 **Flow rate type** 设置为
`Mass flow rate`。

### **V** — 体积流量控制信号，m^3/s 物理信号

输入物理信号，用于指定通过该源的气体体积流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`，并将 **Flow rate type** 设置为
`Volumetric flow rate`。
### 守恒端口

### **A** — 源入口气体

气体守恒端口。正流量使气体从端口
**A** 流向端口 **B**。

### **B** — 源出口气体

气体守恒端口。正流量使气体从端口
**A** 流向端口 **B**。
## 参数
```yaml
parameters:
- name: Source type
  summary: 选择流量在仿真期间是否可以变化 Controlled（默认）| Constant
  group: ''
- name: Flow rate type
  summary: 选择源产生质量流量还是体积流量 Mass flow rate（默认）| Volumetric flow rate
  group: ''
- name: Mass flow rate
  summary: 通过源的恒定质量流量 0 kg/s（默认）
  group: ''
- name: Volumetric flow rate
  summary: 通过源的恒定体积流量 0 m^3/s（默认）
  group: ''
- name: Specified flow rate conditions
  summary: 选择在标准工况还是实际工况下计算体积流量 Actual conditions（默认）| Standard conditions
  group: ''
- name: Standard pressure
  summary: 标准工况下的气体压力 0.10132 MPa（默认）
  group: ''
- name: Standard temperature
  summary: 标准工况下的气体温度 20 degC（默认）
  group: ''
- name: Power added
  summary: 选择源是否对气体做功 Isentropic（默认）| None
  group: ''
- name: Cross-sectional area at port A
  summary: 端口 A 处垂直于流动路径的面积 0.01 m^2（默认）
  group: ''
- name: Cross-sectional area at port B
  summary: 端口 B 处垂直于流动路径的面积 0.01 m^2（默认）
  group: ''
```

### **Source type** — 选择流量在仿真期间是否可以变化 `Controlled`（默认）| `Constant`

选择源产生的流量在仿真期间是否可以变化：

- `Controlled` — 流量是可变的，
  由输入物理信号控制。选择此选项将暴露输入端口
  **M** 或 **V**，具体取决于
  **Flow rate type** 参数的值。
- `Constant` — 流量在仿真期间是恒定的，
  由模块参数指定。选择此选项将启用
  **Mass flow rate** 或 **Volumetric flow rate**
  参数，具体取决于 **Flow rate type**
  参数的值。

### **Flow rate type** — 选择源产生质量流量还是体积流量 `Mass flow rate`（默认）| `Volumetric flow rate`

选择流量类型，`Mass flow rate` 或
`Volumetric flow rate`。

### **Mass flow rate** — 通过源的恒定质量流量 `0 kg/s`（默认）

通过源的气体期望质量流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`，并将 **Flow rate type** 设置为
`Mass flow rate`。

### **Volumetric flow rate** — 通过源的恒定体积流量 `0 m^3/s`（默认）

通过源的气体期望体积流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`，并将 **Flow rate type** 设置为
`Volumetric flow rate`。

### **Specified flow rate conditions** — 选择在标准工况还是实际工况下计算体积流量 `Actual conditions`（默认）| `Standard conditions`

选择源是在实际工况下还是在标准压力和温度下计算流量：

- `Actual conditions` — 源使用系统实际工况下的
  气体密度来计算体积流量。
- `Standard conditions` — 源使用标准工况下的
  气体密度来计算体积流量。当您
  选择此选项时，将提供额外参数，以便您指定
  标准压力和温度。

#### 依赖关系

要启用此参数，请将 **Flow rate type** 设置为
`Volumetric flow rate`。

### **Standard pressure** — 标准工况下的气体压力 `0.10132 MPa`（默认）

标准工况下的气体压力。

#### 依赖关系

要启用此参数，请将 **Specified flow rate conditions**
设置为 `Standard conditions`。

### **Standard temperature** — 标准工况下的气体温度 `20 degC`（默认）

标准工况下的气体温度。

#### 依赖关系

要启用此参数，请将 **Specified flow rate conditions**
设置为 `Standard conditions`。

### **Power added** — 选择源是否对气体做功 `Isentropic`（默认）| `None`

选择源是否对气体流做功：

- `Isentropic` — 源对气体做等熵功以维持指定的质量流量。使用此选项可表示理想化的泵或压缩机，并正确计入能量输入和输出，尤其是在闭环系统中。
- `None` — 源不对流动做功，无论源产生的质量流量如何，既不添加也不移除功率。使用此选项可在系统上游设置所需的流动条件，而不影响流动的温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **A** 处垂直于流动路径的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **B** 处垂直于流动路径的面积。
## 所属库

Simscape / Foundation Library / Gas / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2023b：气体源的可用性增强

在 R2023b 中，单独的 Mass Flow Rate Source (G)、Controlled Mass
Flow Rate Source (G)、Volumetric Flow Rate Source (G) 和
Controlled Volumetric Flow Rate Source (G) 模块已合并为一个
Flow Rate Source (G) 模块，允许您在生成恒定或时变质量流量或体积流量之间进行选择。新模块允许您使用模块参数来配置模块，并仅公开特定模型中所需的输入端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改不会产生兼容性影响。当您打开现有模型时，旧模块会自动替换为具有适当配置的 Flow Rate Source (G) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Mass Flow Rate Source (G) | `source = foundation.gas.sources.controlled_mass_flow_source;` | `source = foundation.gas.sources.flow_source;` |
| Mass Flow Rate Source (G) | `source = foundation.gas.sources.mass_flow_source;` | `source = foundation.gas.sources.flow_source(source_type=foundation.enum.constant_controlled.constant);` |
| Controlled Volumetric Flow Rate Source (G) | `source = foundation.gas.sources.controlled_volumetric_flow_source;` | `source = foundation.gas.sources.flow_source(flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |
| Volumetric Flow Rate Source (G) | `source = foundation.gas.sources.volumetric_flow_source;` | `source = foundation.gas.sources.flow_source(source_type=foundation.enum.constant_controlled.constant,flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |

### R2023a：使用标准压力和温度下的密度计算体积流量

在生成体积流量时，模块允许您选择是使用标准压力和温度下的密度还是系统实际工作条件下的密度来计算体积流量。在以前的版本中，您只能使用实际工作条件。

## 描述

在气体网络中生成恒定或时变的质量流量或体积流量

Flow Rate Source (G) 模块表示气体网络中的理想机械能源。无论压差如何，该源都可以维持指定的质量流量或体积流量。没有流动阻力，也没有与环境的热交换。您可以通过 **Flow rate type** 参数指定流量类型。

模块图标根据 **Source type** 和 **Flow rate type** 参数的值而变化。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **M** 或 **V** 上的输入物理信号（取决于流量类型）指定流量。或者，您可以将固定流量指定为模块参数。正流量使气体从端口 **A** 流向端口 **B**。

体积流量和质量流量通过以下表达式相关联

m˙={ρBV˙for V˙≥0ρAV˙for V˙<0

其中：

- *m˙* 是从端口 **A** 到端口 **B** 的质量流量。
- *ρ*A 和 *ρ*B 分别是端口 **A** 和 **B** 处的密度。
- *V˙* 是体积流量。

您可以选择源是否对气体流做功：

- 如果源是等熵的（**Power added** 参数设置为 `Isentropic`），则等熵关系取决于气体属性模型。

  | 气体模型 | 方程 |
  | --- | --- |
  | 理想气体 | (pA)Z⋅R/cpTA=(pB)Z⋅R/cpTB |
  | 半理想气体 | ∫0TAcp(T)TdT−Z⋅R⋅ln(pA)=∫0TBcp(T)TdT−Z⋅R⋅ln(pB) |
  | 真实气体 | s(TA,pA)=s(TB,pB) |

  传递给气体流的功率基于与等熵过程相关的比总焓。

  Φwork=−m˙A(hA+wA22)−m˙B(hB+wB22)
- 如果源不做功（**Power added** 参数设置为 `None`），则定义方程表明源两侧的比总焓相等。对于所有三种气体属性模型都是相同的。

  hA+wA22=hB+wB22

  传递给气体流的功率 *Φ*work = 0。

这些方程使用以下符号：

|  |  |
| --- | --- |
| *c*p | 定压比热 |
| *h* | 比焓 |
| m˙ | 质量流量（当流量流入模块时，与端口相关的流量为正） |
| *p* | 压力 |
| *R* | 比气体常数 |
| *s* | 比熵 |
| *T* | 温度 |
| *w* | 流速 |
| *Z* | 压缩因子 |
| Φwork | 通过源传递给气体流的功率 |

下标 A 和 B 表示相应的端口。

### 假设和限制

- 没有不可逆损失。
- 与环境没有热交换。
