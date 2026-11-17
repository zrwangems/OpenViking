---
type: simulink-block
title: 'Pressure Source (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sources'
documentation_page: 'pressuresourcema'
documentation_source_path: 'ref/pressuresourcema.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Source (MA)

## 端口
```yaml
ports:
- name: P
  summary: 压差控制信号，Pa 物理信号
  direction: input
- name: A
  summary: 源入口湿空气
  direction: conserving
- name: B
  summary: 源出口湿空气
  direction: conserving
```

### 输入

### **P** — 压差控制信号，Pa 物理信号

输入物理信号，用于指定源两端的压差。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为 `Controlled`。

### 守恒端口

### **A** — 源入口湿空气

湿空气守恒端口。正压差使端口 **B** 处的压力大于端口 **A** 处的压力。

### **B** — 源出口湿空气

湿空气守恒端口。正压差使端口 **B** 处的压力大于端口 **A** 处的压力。
## 参数
```yaml
parameters:
- name: Source type
  summary: 选择压差是否可以在仿真期间变化 Controlled（默认）| Constant
  group: ''
- name: Pressure differential
  summary: 源两端的恒定压差 0 MPa（默认）| 标量
  group: ''
- name: Power added
  summary: 选择源是否做功 Isentropic（默认）| None
  group: ''
- name: Cross-sectional area at port A
  summary: 端口 A 处垂直于流动路径的面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Cross-sectional area at port B
  summary: 端口 B 处垂直于流动路径的面积 0.01 m^2（默认）| 正标量
  group: ''
```

### **Source type** — 选择压差是否可以在仿真期间变化 `Controlled`（默认）| `Constant`

选择源产生的压差是否可以在仿真期间变化：

- `Controlled` — 压差是可变的，由输入物理信号控制。选择此选项将暴露输入端口 **P**。
- `Constant` — 压差在仿真期间是恒定的，由模块参数指定。选择此选项将启用 **Pressure differential** 参数。

### **Pressure differential** — 源两端的恒定压差 `0 MPa`（默认）| 标量

源端口之间湿空气混合物的压差。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`。

### **Power added** — 选择源是否做功 `Isentropic`（默认）| `None`

选择源是否对湿空气流做功：

- `Isentropic` — 源对湿空气执行等熵功以维持指定的压差。使用此选项可表示理想化的泵或压缩机，并正确考虑能量输入和输出，尤其是在闭环系统中。
- `None` — 源不对流体做功，无论源产生的压差如何，既不添加也不移除功率。使用此选项可在系统上游设置所需的流动条件，而不影响流体的温度。

### **Cross-sectional area at port A** — 端口 A 处垂直于流动路径的面积 `0.01 m^2`（默认）| 正标量

端口 **A** 处垂直于流动路径的面积。

### **Cross-sectional area at port B** — 端口 B 处垂直于流动路径的面积 `0.01 m^2`（默认）| 正标量

端口 **B** 处垂直于流动路径的面积。
## 所属库

Simscape / Foundation Library / Moist Air / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2023b：湿空气源的可用性增强

在 R2023b 中，单独的 Pressure Source (MA) 和 Controlled Pressure Source (MA) 模块已合并为一个 Pressure Source (MA) 模块，允许您在生成恒定压差或时变压差之间进行选择。

当您在模型中使用这些 Foundation 库模块时，此更改不会产生兼容性影响。当您打开现有模型时，Controlled Pressure Source (MA) 模块会自动替换为带有暴露输入端口 Pressure Source (MA) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Pressure Source (MA) | `source = foundation.moist_air.sources.controlled_pressure_source;` | `source = foundation.moist_air.sources.pressure_source;` |
| Pressure Source (MA) | `source = foundation.moist_air.sources.pressure_source;` | `source = foundation.moist_air.sources.pressure_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

生成恒定或时变压差

Pressure Source (MA) 模块表示湿空气网络中的理想机械能源。无论通过源的流量如何，该源都可以在其端口之间维持恒定压差。没有流动阻力，也没有与环境的热交换。

端口 **A** 和 **B** 分别表示源的入口和出口。端口 **P** 处的输入物理信号指定压差。或者，您可以将恒定压差指定为模块参数。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

描述该源的方程使用以下符号。

|  |  |
| --- | --- |
| *c*p | 定压比热 |
| *h* | 比焓 |
| *h*t | 比总焓 |
| m˙ | 质量流量（与端口相关的流量在流入模块时为正） |
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

由源的 **Pressure differential** 参数指定的量为

pB−pA=Δpspecified

### 假设和限制

- 没有不可逆损失。
- 没有与环境的热交换。
