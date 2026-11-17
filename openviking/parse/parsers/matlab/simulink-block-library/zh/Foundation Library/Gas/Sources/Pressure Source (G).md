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

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为 `Controlled`。
### 守恒

### **A** — 源入口气体

气体守恒端口。正压差使端口 **B** 处的压力大于端口 **A** 处的压力。

### **B** — 源出口气体

气体守恒端口。正压差使端口 **B** 处的压力大于端口 **A** 处的压力。

## 参数

### **Source type** — 选择压差是否可以在仿真期间变化 `Controlled`（默认）| `Constant`

选择源产生的压差是否可以在仿真期间变化：

- `Controlled` — 压差是可变的，由输入物理信号控制。选择此选项将暴露输入端口 **P**。
- `Constant` — 压差在仿真期间是恒定的，由模块参数指定。选择此选项将启用 **Pressure differential** 参数。

### **Pressure differential** — 源两端的恒定压差 0 MPa（默认）| 标量

源端口两端的气体压差。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`。

### **Power added** — 选择源是否对气体做功 `Isentropic`（默认）| `None`

选择源是否对气体流做功：

- `Isentropic` — 源对气体执行等熵功以维持指定的压差。使用此选项可表示理想化的泵或压缩机，并正确考虑能量输入和输出，尤其是在闭环系统中。
- `None` — 源不对流体做功，无论源产生的压差如何，既不添加也不移除功率。使用此选项可在系统上游设置所需的流动条件，而不影响流体温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流路的面积 0.01 m^2（默认）| 正标量

端口 **A** 处垂直于流路的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流路的面积 0.01 m^2（默认）| 正标量

端口 **B** 处垂直于流路的面积。

## 所属库

Simscape / Foundation Library / Gas / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023b：气体源可用性增强

在 R2023b 中，单独的 Pressure Source (G) 和 Controlled Pressure Source (G) 模块已合并为一个 Pressure Source (G) 模块，允许您在生成恒定或时变压差之间进行选择。

当您在模型中使用这些 Foundation 库模块时，此更改没有兼容性影响。当您打开现有模型时，Controlled Pressure Source (G) 模块会自动替换为带有暴露输入端口的 Pressure Source (G) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Pressure Source (G) | `source = foundation.gas.sources.controlled_pressure_source;` | `source = foundation.gas.sources.pressure_source;` |
| Pressure Source (G) | `source = foundation.gas.sources.pressure_source;` | `source = foundation.gas.sources.pressure_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

生成恒定或时变压差

Pressure Source (G) 模块表示气体网络中的理想机械能源。该源可以在其端口两端维持恒定压差，而不受通过源流量的影响。没有流动阻力，也没有与环境的热交换。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **P** 处的输入物理信号指定压差。或者，您可以将恒定压差指定为模块参数。正压差使端口 **B** 处的压力大于端口 **A** 处的压力。

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

方程使用以下符号：

|  |  |
| --- | --- |
| *c*p | 定压比热 |
| *h* | 比焓 |
| m˙ | 质量流量（与端口相关的流量在流入模块时为正） |
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
- 没有与环境的热交换。
