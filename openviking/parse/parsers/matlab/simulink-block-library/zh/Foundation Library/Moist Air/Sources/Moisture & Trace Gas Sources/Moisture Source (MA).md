---
type: simulink-block
title: 'Moisture Source (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sources / Moisture & Trace Gas Sources'
documentation_page: 'moisturesourcema'
documentation_source_path: 'ref/moisturesourcema.html'
language: zh-CN
chinese_source: worker-translation
---

# Moisture Source (MA)

## 端口

### 输入

### **M** — 质量流量控制信号，kg/s 物理信号

输入物理信号，用于指定通过该源的蒸汽或水滴质量流量。

#### 依赖

要启用此端口，请将 **Source type** 参数设置为 `Controlled`。

### **T** — 添加水分的温度，K 物理信号

输入物理信号，用于指定添加水分的温度。该模块仅使用此值来计算添加水分的比焓。去除水分的比焓基于所连接的湿空气容积的温度。

#### 依赖

要启用此端口，请将 **Source type** 参数设置为 `Controlled`。
### 守恒

### **S** — 注入或提取湿度或水滴 湿空气源

将此端口连接到具有有限湿空气容积的模块的端口 **S**，以通过该模块添加或去除湿度或水滴。

## 参数

### **Source type** — 选择水分质量流量和温度是否可以在仿真期间变化 `Controlled`（默认）| `Constant`

选择水分质量流量和温度是否可以在仿真期间变化：

- `Controlled` — 水分质量流量和温度是可变的，由输入物理信号控制。选择此选项将显示输入端口 **M** 和 **T**。
- `Constant` — 水分质量流量和温度在仿真期间是恒定的，由模块参数指定。选择此选项将启用这些参数。

### **Moisture added or removed** — 选择模块是以水蒸气还是水滴的形式添加或去除水分 `Water vapor`（默认）| `Water droplets`

选择模块是以水蒸气还是水滴的形式添加或去除水分。

### **Water vapor evaporated from liquid or condensed to liquid** — 模块如何添加或去除水蒸气 `off`（默认）| `on`

选择模块如何添加或去除水蒸气。如果清除此复选框，则添加或去除的水分的焓对应于水蒸气的焓，其大于液态水的焓。

如果选中此复选框，则添加或去除的水分的焓对应于液态水的焓，其小于水蒸气的焓。当添加水蒸气时，它从液体中蒸发，潜热由所连接的流体容积提供。当去除水蒸气时，它凝结为液体，潜热释放到所连接的流体容积中。

#### 依赖

要启用此参数，请将 **Moisture added or removed** 设置为 `Water vapor`。

### **Rate of moisture added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的蒸汽或水滴质量流量。正值向所连接的湿空气容积添加水分。负值从该容积中提取水分。

#### 依赖

要启用此参数，请将 **Source type** 设置为 `Constant`。

### **Added moisture temperature specification** — 选择添加水分温度的指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择水分温度的指定方法：

- `Atmospheric temperature` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **Temperature of added moisture** 参数指定一个值。

#### 依赖

要启用此参数，请将 **Source type** 设置为 `Constant`。

### **Temperature of added moisture** — 水分温度 `293.15 K`（默认）

输入所需的添加水分温度。此温度在仿真期间保持恒定。该模块仅使用此值来计算添加水分的比焓。去除水分的比焓基于所连接的湿空气容积的温度。

#### 依赖关系

要启用此参数，请将 **Source type** 设置为 `Constant`，并将 **Added moisture temperature specification** 设置为 `Specified temperature`。

## 所属库

Simscape / Foundation Library / Moist Air / Sources / Moisture & Trace Gas Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：对潮湿空气流中悬浮水滴进行建模

潮湿空气域中的模块现在可以对潮湿空气流中悬浮的水滴进行建模。要对水滴进行建模，请在连接到潮湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2023b：潮湿空气源可用性增强

在 R2023b 中，单独的 Moisture Source (MA) 和 Controlled Moisture Source (MA) 模块已合并为一个 Moisture Source (MA) 模块，允许您在恒定或时变的湿气源或汇之间进行选择。

当您在模型中使用这些 Foundation 库模块时，此更改不会产生兼容性影响。当您打开现有模型时，Controlled Moisture Source (MA) 模块会自动替换为带有暴露输入端口的 Moisture Source (MA) 模块。

但是，如果您在自定义复合组件中使用这些模块，则需要更新复合组件代码。

| 要更新的源模块 | 旧语法 | 新语法 |
| --- | --- | --- |
| Controlled Moisture Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source_controlled;` | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source;` |
| Moisture Source (MA) | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source;` | `source = foundation.moist_air.sources.moisture_trace_gas.moisture_source(source_type=foundation.enum.constant_controlled.constant);` |

## 描述

以恒定或时变速率注入或提取水分

Moisture Source (MA) 模块表示所连接湿空气体积的恒定或时变湿度或液滴源或汇。正的或负的水分质量流量分别导致水分被添加或移除。

对于时变源，两个物理信号输入端口 **M** 和 **T** 分别提供质量流量和温度值。或者，您可以将恒定质量流量和温度指定为模块参数。

当 **Moisture added or removed** 参数为 `Water vapor` 时，**Water vapor evaporated from liquid or condensed to liquid** 参数控制蒸汽如何离开或进入模块。当您清除 **Water vapor evaporated from liquid or condensed to liquid** 时，模块以指定速率从流体体积中移除水蒸气。当您选择 **Water vapor evaporated from liquid or condensed to liquid** 时，模块假定进入流体体积的蒸汽来源于蒸发的水，而离开体积的蒸汽凝结为液体。在这种情况下，模块还会对任一过程引起的潜热变化进行建模。

当您清除 **Water vapor evaporated from liquid or condensed to liquid** 复选框时，与添加或移除的蒸汽相关的能量为

Φs={m˙specified⋅hw(Tspecified),if m˙specified≥0m˙specified⋅hw(Ts),if m˙specified<0

其中：

- m˙specified 是由端口 **M** 处的输入物理信号或 **Rate of added moisture** 参数指定的水蒸气质量流量。
- *h*w 是水蒸气比焓。
- *T*specified 是添加水分的温度，由端口 **T** 处的输入物理信号或模块参数指定。模块仅使用此值来计算添加水分的比焓。移除水分的比焓基于所连接湿空气体积的温度。
- *T*s 是端口 **S** 处的温度，与所连接湿空气体积的温度相同。

当您选择 **Water vapor evaporated from liquid or condensed to liquid** 时，与添加或移除的蒸汽相关的能量为

Φs={m˙specified⋅(hw(Tspecified)−Δhvap(Tspecified)),if m˙specified≥0m˙specified⋅(hw(Ts)−Δhvap(Ts)),if m˙specified<0

其中 *Δh*vap 是水的比汽化焓。

端口 **S** 是湿空气源守恒端口。将此端口连接到具有有限湿空气体积的模块的端口 **S**，以通过该模块添加或移除水分。有关详细信息，请参阅 Using Moisture and Trace Gas Sources。
