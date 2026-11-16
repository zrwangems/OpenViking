---
type: simulink-block
title: 'Pressure Source (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sources'
documentation_page: 'pressuresourceg'
documentation_source_path: 'ref/pressuresourceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Source (G)

## 端口

### 输入

### **P** — 压差控制信号，Pa 物理信号

输入物理信号，用于指定源两端的压差。

#### 依赖项

要启用此端口，请将**源类型**参数设置为 `Controlled`。
### 守恒

### **A** — 源进口气体

气体守恒端口。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

### **B** — 源出口气体

气体守恒端口。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

## 参数

### **源类型** — 选择压差是否可在仿真期间变化 `Controlled`（默认）| `Constant`

选择源生成的压差是否可在仿真期间变化：

- `Controlled` — 压差可变，由输入物理信号控制。选择此选项会显示输入端口 **P**。
- `Constant` — 压差在仿真期间恒定，由模块参数指定。选择此选项会启用**压差**参数。

### **压差** — 源两端的恒定压差 0 MPa（默认）| 标量

源端口两端的气体压差。

#### 依赖项

要启用此参数，请将**源类型**设置为 `Constant`。

### **添加的功率** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对气体流做功：

- `Isentropic` — 源对气体做等熵功，以保持指定的压差。使用此选项可表示理想化的泵或压缩机，并正确计入能量输入和输出，尤其是在闭环系统中。
- `None` — 源对流动不做功，既不添加也不移除功率，无论源产生的压差如何。使用此选项可在系统上游设置所需的流动条件，而不影响流动的温度。

### **端口 A 的横截面积** — 端口 A 处垂直于流路的面积 0.01 m^2（默认）| 正标量

端口 **A** 处垂直于流路的面积。

### **端口 B 的横截面积** — 端口 B 处垂直于流路的面积 0.01 m^2（默认）| 正标量

端口 **B** 处垂直于流路的面积。

## 所属库

Simscape / Foundation Library / Gas / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2016b 中引入**

### R2023b：气体源的可用性增强

在 R2023b 中，单独的 Pressure Source (G) 和 Controlled Pressure Source (G) 模块已合并为单个 Pressure Source (G) 模块，您可在生成恒定压差或时变压差之间进行选择。

当您在模型中使用这些 Foundation 库模块时，此更改不会影响兼容性。打开现有模型时，Controlled Pressure Source (G) 模块会自动替换为带暴露输入端口的 Pressure Source (G) 模块。

但是，如果在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Pressure Source (G) | `source = foundation.gas.sources.controlled_pressure_source;` | `source = foundation.gas.sources.pressure_source;` |
| Pressure Source (G) | `source = foundation.gas.sources.pressure_source;` | `source = foundation.gas.sources.pressure_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

生成恒定或时变压差

Pressure Source (G) 模块表示气体网络中的理想机械能源。无论通过源的流量如何，该源都能在其端口两端保持恒定压差。无流动阻力，也无与环境的热交换。

端口 **A** 和 **B** 表示源的进口和出口。端口 **P** 处的输入物理信号指定压差。或者，您可以将恒定压差指定为模块参数。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

您可以选择源是否对气体流做功：

- 如果源为等熵（**添加的功率**参数设置为 `Isentropic`），则等熵关系取决于气体属性模型。

  | 气体模型 | 方程 |
  | --- | --- |
  | Perfect gas | (pA)Z⋅R/cpTA=(pB)Z⋅R/cpTB |
  | Semiperfect gas | ∫0TAcp(T)TdT−Z⋅R⋅ln(pA)=∫0TBcp(T)TdT−Z⋅R⋅ln(pB) |
  | Real gas | s(TA,pA)=s(TB,pB) |

  输送到气体流的功率基于与等熵过程相关的比总焓。

  Φwork=−m˙A(hA+wA22)−m˙B(hB+wB22)
- 如果源不做功（**添加的功率**参数设置为 `None`），则定义方程表明源两侧的比总焓相等。对于所有三种气体属性模型，该式都相同。

  hA+wA22=hB+wB22

  输送到气体流的功率 *Φ*work = 0。

这些方程使用以下符号：

|  |  |
| --- | --- |
| *c*p | 定压比热容 |
| *h* | 比焓 |
| m˙ | 质量流率（与端口关联的流量在流入模块时为正） |
| *p* | 压力 |
| *R* | 比气体常数 |
| *s* | 比熵 |
| *T* | 温度 |
| *w* | 流速 |
| *Z* | 压缩因子 |
| Φwork | 通过源输送到气体流的功率 |

下标 A 和 B 表示相应的端口。

### 假设和限制

- 无不可逆损失。
- 无与环境的热交换。
