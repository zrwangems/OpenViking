---
type: simulink-block
title: 'Flow Rate Source (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sources'
documentation_page: 'flowratesourcema'
documentation_source_path: 'ref/flowratesourcema.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Rate Source (MA)

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
  summary: 源入口湿空气
  direction: conserving
- name: B
  summary: 源出口湿空气
  direction: conserving
```

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过该源的湿空气质量流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`，并将 **Flow rate type** 设置为
`Mass flow rate`。

### **V** — 体积流量控制信号，m^3/s 物理信号

输入物理信号，用于指定通过该源的湿空气体积流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为
`Controlled`，并将 **Flow rate type** 设置为
`Volumetric flow rate`。
### 守恒端口

### **A** — 源入口湿空气

湿空气守恒端口。正流量使湿空气从端口 **A** 流向端口 **B**。

### **B** — 源出口湿空气

湿空气守恒端口。正流量使湿空气从端口 **A** 流向端口 **B**。
## 参数
```yaml
parameters:
- name: Source type
  summary: 选择流量在仿真期间是否可以变化 Controlled（默认）| Constant
  group: ''
- name: Flow rate type
  summary: 选择源生成质量流量还是体积流量 Mass flow rate（默认）| Volumetric flow rate
  group: ''
- name: Mixture mass flow rate
  summary: 通过源的恒定质量流量 0 kg/s（默认）
  group: ''
- name: Mixture volumetric flow rate
  summary: 通过源的恒定体积流量 0 m^3/s（默认）
  group: ''
- name: Specified flow rate conditions
  summary: 选择在标准工况还是实际工况下计算体积流量 Actual conditions（默认）| Standard conditions
  group: ''
- name: Standard pressure
  summary: 标准工况下的湿空气压力 0.10132 MPa（默认）
  group: ''
- name: Standard temperature
  summary: 标准工况下的湿空气温度 20 degC（默认）
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

### **Flow rate type** — 选择源生成质量流量还是体积流量 `Mass flow rate`（默认）| `Volumetric flow rate`

选择流量类型，`Mass flow rate` 或
`Volumetric flow rate`。

### **Mixture mass flow rate** — 通过源的恒定质量流量 `0 kg/s`（默认）

通过源的湿空气混合物的期望质量流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`，并将 **Flow rate type** 设置为
`Mass flow rate`。

### **Mixture volumetric flow rate** — 通过源的恒定体积流量 `0 m^3/s`（默认）

通过源的湿空气混合物的期望体积流量。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`，并将 **Flow rate type** 设置为
`Volumetric flow rate`。

### **Specified flow rate conditions** — 选择在标准工况还是实际工况下计算体积流量 `Actual conditions`（默认）| `Standard conditions`

选择源是在实际工况下还是在标准压力和温度下计算流量：

- `Actual conditions` — 源使用系统实际工况下的
  湿空气密度来计算体积流量。
- `Standard conditions` — 源使用标准工况下的
  湿空气密度来计算体积流量。当您选择此选项时，将提供额外参数，以便您指定
  标准压力、温度和相对湿度。

#### 依赖关系

要启用此参数，请将 **Flow rate type** 设置为
`Volumetric flow rate`。

### **Standard pressure** — 标准工况下的湿空气压力 `0.10132 MPa`（默认）

标准工况下的湿空气压力。

#### 依赖关系

要启用此参数，请将 **Specified flow rate conditions**
设置为 `Standard conditions`。

### **Standard temperature** — 标准工况下的湿空气温度 `20 degC`（默认）

标准工况下的湿空气温度。

#### 依赖关系

要启用此参数，请将 **Specified flow rate conditions**
设置为 `Standard conditions`。

### **Power added** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对湿空气流做功：

- `Isentropic` — 源对湿空气做等熵功，以维持指定的质量流量。使用此选项可表示理想化的泵或压缩机，并正确考虑能量输入和输出，尤其是在闭环系统中。
- `None` — 源不对流做功，无论源产生的质量流量如何，既不添加也不移除功率。使用此选项可在系统上游设置所需的流动条件，而不影响流的温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **A** 处垂直于流动路径的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **B** 处垂直于流动路径的面积。
## 所属库

Simscape / Foundation Library / Moist Air / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2024b：对湿空气流中悬浮的水滴进行建模

湿空气域中的模块现在可以对湿空气流中悬浮的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties
(MA) 模块中选择 **Enable entrained water droplets**。

### R2023b：湿空气源可用性增强

在 R2023b 中，单独的 Mass Flow Rate Source (MA)、Controlled Mass
Flow Rate Source (MA)、Volumetric Flow Rate Source (MA) 和
Controlled Volumetric Flow Rate Source (MA) 模块已合并为单个 Flow Rate Source (MA) 模块，允许您选择生成恒定或时变的质量流量或体积流量。新模块允许您使用模块参数来配置模块，并仅暴露特定模型中所需的输入端口，这有助于减少杂乱并改善模块图布局。

当您在模型中使用这些 Foundation 库模块时，此更改不会产生兼容性影响。当您打开现有模型时，旧模块会自动替换为具有适当配置的 Flow Rate Source (MA) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Mass Flow Rate Source (MA) | `source = foundation.moist_air.sources.controlled_mass_flow_source;` | `source = foundation.moist_air.sources.flow_source;` |
| Mass Flow Rate Source (MA) | `source = foundation.moist_air.sources.mass_flow_source;` | `source = foundation.moist_air.sources.flow_source(source_type=foundation.enum.constant_controlled.constant);` |
| Controlled Volumetric Flow Rate Source (MA) | `source = foundation.moist_air.sources.controlled_volumetric_flow_source;` | `source = foundation.moist_air.sources.flow_source(flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |
| Volumetric Flow Rate Source (MA) | `source = foundation.moist_air.sources.volumetric_flow_source;` | `source = foundation.moist_air.sources.flow_source(source_type=foundation.enum.constant_controlled.constant,flow_type=foundation.enum.mass_volumetric_flow.volumetric);` |

## 描述

在湿空气网络中生成恒定或时变的质量流量或体积流量

Flow Rate Source (MA) 模块表示湿空气网络中的理想机械能源。无论压差如何，该源都可以维持指定的质量流量或体积流量。没有流动阻力，也没有与环境的热交换。您可以通过 **Flow rate type** 参数指定流量类型。

模块图标根据 **Source type** 和 **Flow rate type** 参数的值而变化。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **M** 或 **V** 上的输入物理信号（取决于流量类型）指定流量。或者，您可以将固定流量指定为模块参数。正流量使气体从端口 **A** 流向端口 **B**。

体积流量和质量流量通过以下表达式相关联

m˙={ρBV˙for V˙≥0ρAV˙for V˙<0

其中：

- *m˙* 是从端口 **A** 到端口 **B** 的质量流量。
- *ρ*A 和 *ρ*B 分别是端口 **A** 和 **B** 处的密度。
- *V˙* 是体积流量。

描述该源的方程使用以下符号。

|  |  |
| --- | --- |
| *c*p | 定压比热 |
| *h* | 比焓 |
| *h*t | 比总焓 |
| m˙ | 质量流量（当流量流入模块时，与端口相关的流量为正） |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *s* | 比熵 |
| *T* | 温度 |
| *Φ*work | 通过源传递给湿空气流的功率 |

下标 A 和 B 表示相应的端口。下标 `a`、`w`、`d` 和 `g` 分别表示干空气、水蒸气、水滴和微量气体的属性。

质量平衡：

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

能量平衡：

ΦA+ΦB+Φwork=0

如果源不做功（**Power added** 参数设置为 `None`），则 Φwork=0。

如果源是等熵的（**Power added** 参数设置为 `Isentropic`），则

Φwork=m˙A(htB−htA)

其中

htA=hA+12(m˙AρASA)2htB=hB+12(m˙BρBSB)2

混合物比焓 *h*A = *h*(*T*A) 和 *h*B = *h*(*T*B) 受等熵关系约束，即熵没有变化：

∫TATB1Tdh(T)=Rln(pBpA)

当您将 **Flow rate type** 参数设置为 `Mass flow rate` 时，由 **Mixture mass flow rate** 参数或端口 **M** 上的输入信号指定的量为

m˙A=m˙specified

### 假设和限制

- 没有不可逆损失。
- 与环境没有热交换。
