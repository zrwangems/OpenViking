---
type: simulink-block
title: 'Trace Gas Source (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sources / Moisture & Trace Gas Sources'
documentation_page: 'tracegassourcema'
documentation_source_path: 'ref/tracegassourcema.html'
language: zh-CN
chinese_source: worker-translation
---

# Trace Gas Source (MA)

## 端口

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过源的示踪气体质量流量。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为 `Controlled`。

### **T** — 添加的示踪气体温度，K 物理信号

输入物理信号，用于指定添加的示踪气体的温度。该模块仅使用此值来计算添加的示踪气体的比焓。移除的示踪气体的比焓基于所连接的湿空气容积的温度。

#### 依赖关系

要启用此端口，请将 **Source type** 参数设置为 `Controlled`。

### 守恒

### **S** — 注入或提取示踪气体湿空气源

将此端口连接到具有有限湿空气容积的模块的端口 **S**，以通过该模块添加或移除示踪气体。

## 参数

### **Source type** — 选择示踪气体质量流量和温度是否可以在仿真期间变化 `Controlled`（默认）| `Constant`

选择示踪气体质量流量和温度是否可以在仿真期间变化：

- `Controlled` — 示踪气体质量流量和温度是可变的，由输入物理信号控制。选择此选项将显示输入端口 **M** 和 **T**。
- `Constant` — 示踪气体质量流量和温度在仿真期间是恒定的，由模块参数指定。选择此选项将启用这些参数。

### **Rate of added trace gas** — 通过源的恒定质量流量 `0 kg/s`（默认）

通过源的示踪气体质量流量。正值向所连接的湿空气容积添加示踪气体。负值从该容积中提取示踪气体。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`。

### **Added trace gas temperature specification** — 选择添加的示踪气体温度的指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择示踪气体温度的指定方法：

- `Atmospheric temperature` — 使用大气温度，由连接到回路的 Moist Air Properties (MA) 模块指定。
- `Specified temperature` — 使用 **Temperature of added trace gas** 参数指定一个值。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`。

### **Temperature of added trace gas** — 示踪气体温度 `293.15 K`（默认）

输入添加的示踪气体的所需温度。此温度在仿真期间保持恒定。该模块仅使用此值来计算添加的示踪气体的比焓。移除的示踪气体的比焓基于所连接的湿空气容积的温度。

#### 依赖关系

要启用此参数，请将 **Added trace gas temperature specification** 设置为 `Specified temperature`。

## 所属库

Simscape / Foundation Library / Moist Air / Sources / Moisture & Trace Gas Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023b: 湿空气源的可用性增强

在 R2023b 中，单独的 Trace Gas Source (MA) 和 Controlled
Trace Gas Source (MA) 模块已合并为一个 Trace Gas Source (MA) 模块，允许您在恒定或时变的痕量气体源或汇之间进行选择。

当您在模型中使用这些 Foundation 库模块时，此更改不会影响兼容性。当您打开现有模型时，Controlled Trace
Gas Source (MA) 模块会自动替换为具有暴露输入端口的 Trace Gas
Source (MA) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Trace Gas Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source_controlled;` | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source;` |
| Trace Gas Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source;` | `source = foundation.moist_air.sources.moisture_trace_gas.trace_gas_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

以恒定或时变速率注入或提取痕量气体

Trace Gas Source (MA) 模块表示所连接湿空气体积的恒定或时变痕量气体源或汇。正的或负的痕量气体质量流量分别导致痕量气体水平增加或减少。

对于时变源，两个物理信号输入端口 **M** 和 **T** 分别提供质量流量和温度值。或者，您可以将恒定质量流量和温度指定为模块参数。

与添加或移除的痕量气体相关的能量为

Φs={m˙specified⋅hg(Tspecified),if m˙specified≥0m˙specified⋅hg(Ts),if m˙specified<0

其中：

- m˙specified 是由端口 **M** 处的输入物理信号或 **Trace gas
  mass flow rate** 参数指定的痕量气体质量流量。
- *h*g 是痕量气体比焓。
- *T*specified 是添加的痕量气体的温度，由端口
  **T** 处的输入物理信号或模块参数指定。该模块仅使用此值来计算添加的痕量气体的比焓。移除的痕量气体的比焓基于所连接湿空气体积的温度。
- *T*s 是端口
  **S** 处的温度，与所连接湿空气体积的温度相同。

端口 **S** 是湿空气源守恒端口。将此端口连接到具有有限湿空气体积的模块的端口 **S**，以通过该模块添加或移除痕量气体。有关详细信息，请参阅 Using Moisture and Trace Gas Sources。
