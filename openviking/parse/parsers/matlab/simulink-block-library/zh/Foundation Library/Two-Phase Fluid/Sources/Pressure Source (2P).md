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

要启用此端口，请将 **Source type** 参数设置为
`Controlled`。
### 守恒

### **A** — 源入口两相流体

两相流体守恒端口。正流量使流体从端口 **A** 流向
端口 **B**。

### **B** — 源出口两相流体

两相流体守恒端口。正流量使流体从端口 **A** 流向
端口 **B**。

## 参数

### **Source type** — 选择压差是否可以在仿真期间变化 `Controlled`（默认）| `Constant`

选择源产生的压差是否可以在仿真期间变化：

- `Controlled` — 压差是
  可变的，由输入物理信号控制。选择此选项将显示
  输入端口 **P**。
- `Constant` — 压差在仿真期间
  恒定，由模块参数指定。选择此选项
  将启用 **Pressure differential** 参数。

### **Pressure differential** — 源两端的恒定压差 `0 Pa`（默认）| 标量

源端口两端所需的压差。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为
`Constant`。

### **Power added** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对流体流动做功：

- `Isentropic` — 源对流体执行等熵
  功以维持指定的压差。使用此选项
  来表示理想化的泵或压缩机，并正确考虑能量
  输入和输出，尤其是在闭环系统中。
- `None` — 源不对
  流动做功，既不添加也不移除功率，无论源
  产生的压差如何。使用此选项来设置
  系统上游所需的流动条件，而不影响
  流动的温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流动路径的面积 0.01 m^2（默认）| 正标量

端口 **A** 处垂直于流动路径的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流动路径的面积 0.01 m^2（默认）| 正标量

端口 **B** 处垂直于流动路径的面积。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023b：两相流体源可用性增强

在 R2023b 中，单独的 Pressure Source (2P) 和 Controlled Pressure
Source (2P) 模块已合并为单个 Pressure Source
(2P) 模块，允许您选择生成恒定或时变
压差。

当您在模型中使用这些 Foundation 库模块时，此更改没有兼容性影响。当您打开现有模型时，Controlled Pressure Source
(2P) 模块会自动替换为具有暴露输入端口的 Pressure Source (2P)
模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新
复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Pressure Source (2P) | `source = foundation.two_phase_fluid.sources.controlled_pressure_source;` | `source = foundation.two_phase_fluid.sources.pressure_source;` |
| Pressure Source (2P) | `source = foundation.two_phase_fluid.sources.pressure_source;` | `source = foundation.two_phase_fluid.sources.pressure_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

生成恒定或时变压力差

Pressure Source (2P) 模块表示两相流体网络中的理想机械能源。无论通过源的流量如何，该源都能在其端口之间维持恒定的压力差。没有流动阻力，也没有与环境的热交换。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **P** 处的输入物理信号指定压力差。或者，您可以将恒定压力差指定为模块参数。正压力差会导致端口 **B** 处的压力大于端口 **A** 处的压力。

### 质量平衡

源中流体的体积被视为可忽略不计，并在模型中忽略。端口之间没有流体积累，因此流入源的所有质量流率之和必须等于零：

m˙A+​m˙B=0，

其中 m˙ 表示通过端口流入源的质量流率。该模块接受端口 **A** 处的质量流率作为输入。当指定值为正时，流动方向为从端口 **A** 到端口 **B**。

### 能量平衡

默认情况下，源通过对流入流体执行等熵功来维持指定的流率，不过该模块提供了忽略此项的选项。如果在模型中考虑源做功的速率，则其必须等于通过端口的能量流率之和：

ϕA+​ϕB+​ϕWork=0，

其中 *ϕ* 表示通过端口或通过做功流入源的能量流率。做功引起的能量流率等于源产生的功率。其值由端口处的比总焓计算得出：

ϕWork=m˙A(hA−hB)。

比总焓 *h* 定义为：

h\*=u\*+p\*v\*+12(m˙\*v\*S)2，

其中星号表示端口（**A** 或 **B**），并且：

- *u* 是比内能。
- *p* 是压力。
- *S* 是流通面积。

方程中的比内能来自 Two-Phase Fluid Properties (2P) 模块的表格数据。其值由源所做的功为等熵这一约束唯一确定。比熵是比内能的函数，因此在端口 **A** 和 **B** 处必须具有相同的值：

sA(pA,uA)=sB(pB,uB)，

其中 *s* 是比熵。如果 **Power added** 参数设置为 `None`，则端口处的比总焓具有相同的值（hA=hB），并且源所做的功降为零（ϕWork=0）。

### 假设和限制

- 没有不可逆损失。
- 没有与环境的热交换。
