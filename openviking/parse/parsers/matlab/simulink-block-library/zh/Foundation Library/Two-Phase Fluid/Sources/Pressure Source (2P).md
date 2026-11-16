---
type: simulink-block
title: 'Pressure Source (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sources'
documentation_page: 'pressuresource2p'
documentation_source_path: 'ref/pressuresource2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Source (2P)

## 端口

### 输入

### **P** — 压差控制信号，Pa 物理信号

输入物理信号，用于指定源两端的压差。

#### 依赖关系

要启用此端口，请将 **源类型** 参数设置为 `Controlled`。

### 守恒

### **A** — 源入口两相流体

两相流体守恒端口。正流率使流体从端口 **A** 流向端口 **B**。

### **B** — 源出口两相流体

两相流体守恒端口。正流率使流体从端口 **A** 流向端口 **B**。

## 参数

### **源类型** — 选择压差在仿真期间是否可以变化 `Controlled`（默认）| `Constant`

选择源产生的压差在仿真期间是否可以变化：

- `Controlled` — 压差是可变的，由输入物理信号控制。选择此选项会暴露输入端口 **P**。
- `Constant` — 压差在仿真期间恒定，由模块参数指定。选择此选项会启用 **压差** 参数。

### **压差** — 源两端的恒定压差 `0 Pa`（默认）| 标量

源端口两端的所需压差。

#### 依赖关系

要启用此参数，请将 **源类型** 设置为 `Constant`。

### **添加的功率** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对流体流做功：

- `Isentropic` — 源对流体执行等熵功，以维持指定的压差。使用此选项可表示理想化泵或压缩机，并正确考虑能量输入和输出，尤其是在闭环系统中。
- `None` — 源不对流做功，既不添加也不移除功率，无论源产生的压差如何。使用此选项可在系统上游设置所需流动条件，而不影响流的温度。

### **端口 A 处的横截面积** — 端口 A 处垂直于流路的面积 0.01 m^2（默认）| 正标量

端口 **A** 处垂直于流路的面积。

### **端口 B 处的横截面积** — 端口 B 处垂直于流路的面积 0.01 m^2（默认）| 正标量

端口 **B** 处垂直于流路的面积。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023b：两相流体源的易用性增强

在 R2023b 中，单独的 Pressure Source (2P) 和 Controlled Pressure Source (2P) 模块已合并为单个 Pressure Source (2P) 模块，允许你选择生成恒定压差还是时变压差。

当你在模型中使用这些 Foundation library 模块时，此更改没有兼容性影响。打开现有模型时，Controlled Pressure Source (2P) 模块会自动替换为具有暴露的输入端口的 Pressure Source (2P) 模块。

但是，如果你在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Pressure Source (2P) | `source = foundation.two_phase_fluid.sources.controlled_pressure_source;` | `source = foundation.two_phase_fluid.sources.pressure_source;` |
| Pressure Source (2P) | `source = foundation.two_phase_fluid.sources.pressure_source;` | `source = foundation.two_phase_fluid.sources.pressure_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

生成恒定或时变压差

Pressure Source (2P) 模块表示两相流体网络中的理想机械能源。无论通过源的流率如何，源都可以在其端口两端维持恒定压差。没有流动阻力，也不与环境进行热交换。

端口 **A** 和 **B** 表示源入口和出口。端口 **P** 处的输入物理信号指定压差。或者，你可以将恒定压差指定为模块参数。正压差使端口 **B** 处的压力大于端口 **A** 处的压力。

### 质量平衡

源中流体的体积被视为可忽略，并在模型中忽略。端口之间没有流体累积，因此进入源的所有质量流率之和必须等于零：

m˙A+​m˙B=0,

其中 m˙ 表示通过某一端口进入源的质量流率。该模块接受端口 **A** 处的质量流率作为输入。当指定值为正时，流动从端口 **A** 指向端口 **B**。

### 能量平衡

默认情况下，源通过对进入的流体执行等熵功来维持指定的流率，不过该模块提供了忽略此项的选项。如果模型中考虑源做功，则源做功的速率必须等于通过端口的能量流率之和：

ϕA+​ϕB+​ϕWork=0,

其中 *ϕ* 表示通过某一端口或通过做功进入源的能量流率。做功导致的能量流率等于源产生的功率。其值根据端口处的比总焓计算：

ϕWork=m˙A(hA−hB)。

比总焓 *h* 定义为：

h\*=u\*+p\*v\*+12(m˙\*v\*S)2,

其中星号表示某一端口（**A** 或 **B**），并且：

- *u* 是比内能。
- *p* 是压力。
- *S* 是流通面积。

方程中的比内能来自 Two-Phase Fluid Properties (2P) 模块的表格数据。其值由源所做功为等熵这一约束唯一确定。比熵是比内能的函数，因此在端口 **A** 和 **B** 处必须具有相同的值：

sA(pA,uA)=sB(pB,uB),

其中 *s* 是比熵。如果将 **添加的功率** 参数设置为 `None`，则端口处的比总焓具有相同值（hA=hB），并且源所做功降为零（ϕWork=0）。

### 假设和限制

- 没有不可逆损失。
- 不与环境进行热交换。
