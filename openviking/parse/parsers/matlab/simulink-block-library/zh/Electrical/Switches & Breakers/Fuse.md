---
type: simulink-block
title: 'Fuse'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'fuse'
documentation_source_path: 'ref/fuse.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuse

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: output
- name: '-'
  summary: 负极端子电气
  direction: output
- name: x
  summary: 保险丝状态物理信号
  direction: output
```

### 守恒

### **+** — 正极端子电气

与保险丝正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与保险丝负极端子关联的电气守恒端口。
### 输出

### **x** — 保险丝状态物理信号

将保险丝状态输出为无量纲物理信号。如果保险丝完好，该端口输出
0；如果保险丝已熔断，则输出 1。

#### 依赖关系

当 **PS output for fuse state**
参数设置为 `Visible` 时暴露。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 开路时间对电流的模型依赖性 Opening time is independent of current（默认）| Opening time depends on I^2*t | Opening time is tabulated
  group: ''
- name: Rated current, I_rated
  summary: 额定工作电流 1 A（默认）
  group: ''
- name: Ratio of minimum melting current to rated current, I_melt/I_rated
  summary: 定义的熔断阈值电流 1（默认）
  group: ''
- name: Time to fuse
  summary: 保险丝熔断所需时间 0 s（默认）
  group: ''
- name: Nominal melting, I^2\*t
  summary: 保险丝熔断所需的耗散能量 1 s\*A^2（默认）
  group: ''
- name: Tabulated currents
  summary: 来自时间-电流曲线的电流数据 [1.9, 2, 2.5, 30] A（默认）
  group: ''
- name: Tabulated opening times
  summary: 来自时间-电流曲线的时间数据 [10000, 1, 0.3, 0.001] s（默认）
  group: ''
- name: Fuse resistance R
  summary: 保险丝电阻 0.01 Ω（默认）
  group: ''
- name: Open-circuit conductance G
  summary: 开路保险丝电导 1e-8 1/Ω（默认）
  group: ''
- name: PS output for fuse state
  summary: 控制保险丝状态输出端口的可见性 Hidden（默认）| Visible
  group: ''
```

### **Parameterization** — 开路时间对电流的模型依赖性 `Opening time is independent of current`（默认）| `Opening time depends on I^2*t` | `Opening time is tabulated`

选择开路时间是否取决于电流：

- `Opening time is independent of current`
  — 当流过保险丝的电流连续超过阈值电流的时间长于指定时间时，保险丝断开。
- `Opening time depends on I^2*t` —
  使保险丝的开路取决于保险丝中耗散的能量。
  将此选项用于大电流工作范围。
- `Opening time is tabulated` —
  使保险丝的开路取决于平均时间-电流表格数据。将此选项用于小电流。

### **Rated current, I\_rated** — 额定工作电流 1 A（默认）

来自数据手册的保险丝额定值，或额定工作电流。

#### 依赖关系

当 **Parameterization** 参数设置为
`Opening time is independent of current`
或 `Opening time depends on I^2*t` 时启用。

### **Ratio of minimum melting current to rated current, I\_melt/I\_rated** — 定义的熔断阈值电流 1（默认）

最小熔断电流定义保险丝的工作阈值。如果流过保险丝的电流不超过此阈值，保险丝保持低欧姆状态。使用默认参数值 `1` 时，
阈值电流与额定电流相同。在大多数情况下，此
参数值应大于 1。你也可以将其设置为小于 1 的值，
以应对保险丝可能在低于额定电流的电流水平下熔断的情况（例如，由于高温，或由于
重复脉冲）。参数值必须大于 0。

#### 依赖关系

当 **Parameterization** 参数设置为
`Opening time is independent of current`
或 `Opening time depends on I^2*t` 时启用。

### **Time to fuse** — 保险丝熔断所需时间 0 s（默认）

保险丝熔断所需的时间量。如果流过保险丝的
电流连续超过阈值电流的时间长于该时间量，
保险丝进入高欧姆状态并断开电路。如果
电流在时间耗尽之前降至阈值以下，保险丝保持
低欧姆状态。如果电流再次超过阈值，时间
计数器重新开始。使用默认参数值 `0` 时，
一旦电流超过最小
熔断电流，保险丝立即熔断。参数值必须大于或等于 0。

#### 依赖关系

当 **Parameterization** 参数设置为
`Opening time is independent of
current` 时启用。

### **Nominal melting, I^2\*t** — 保险丝熔断所需的耗散能量 1 s\*A^2（默认）

保险丝熔断所需的在保险丝中耗散的能量量。这是
数据手册中的标称熔断值，即 I2t 参数。该
值必须大于或等于 0。

#### 依赖关系

当 **Parameterization** 参数设置为
`Opening time depends on I^2*t` 时启用。

### **Tabulated currents** — 来自时间-电流曲线的电流数据 [1.9, 2, 2.5, 30] A（默认）

来自制造商数据手册上时间-电流曲线的表格
电流值。此向量中的每个元素都必须大于 0，并且
该向量必须严格递增。

#### 依赖关系

当 **Parameterization** 参数设置为
`Opening time is tabulated` 时启用。

### **Tabulated opening times** — 来自时间-电流曲线的时间数据 [10000, 1, 0.3, 0.001] s（默认）

来自制造商数据手册上时间-电流曲线的表格
时间值。此向量中的每个元素都必须大于或等于 0，
并且该向量必须严格递减。该向量的大小必须与
**Tabulated currents** 向量相同。

#### 依赖关系

当 **Parameterization** 参数设置为
`Opening time is tabulated` 时启用。

### **Fuse resistance R** — 保险丝电阻 0.01 Ω（默认）

低欧姆状态下的保险丝电阻。参数值必须
大于 0。

### **Open-circuit conductance G** — 开路保险丝电导 1e-8 1/Ω（默认）

保险丝已熔断时高欧姆状态下的开路保险丝电导。参数值必须大于 0。

### **PS output for fuse state** — 控制保险丝状态输出端口的可见性 `Hidden`（默认）| `Visible`

当设置为 `Visible` 时，模块图标上会出现一个 PS 输出端口
**x**。如果保险丝完好，该端口输出 0；
如果保险丝已熔断，则输出 1。
## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

## 描述

防止过电流的保险丝

Fuse 模块断开电路，以保护电路
免受过大电流的影响。该模块提供以下建模选项：

- `Opening time is independent of current` —
  当流过保险丝的电流连续超过阈值电流的时间长于指定时间量时，保险丝断开。此选项假定
  开路时间与电流无关。它还隐含地假定
  一旦电流降至某个阈值以下，保险丝中的热量会立即消散。
- `Opening time depends on I^2*t` — 使保险丝
  开路取决于保险丝中耗散的能量。标称熔断
  值（I^2\*t）通常可在制造商数据手册中找到。如果你选择
  此选项，保险丝会在以下情况下熔断：

  ∫toverti2dt≥I2t

  其中 *t*over 是
  电流越过阈值电流的时间，*i* 是
  流过保险丝的瞬时电流，*I2t* 是
  数据手册中的标称熔断值。将此选项用于大电流工作范围。
- `Opening time is tabulated` — 使保险丝
  开路取决于平均时间-电流表格数据。此数据
  表示给定某个电流时保险丝开路所需的时间，
  并以时间-电流曲线的形式提供在制造商数据手册中。

  例如，这些是
  Littelfuse® 218 系列保险丝数据手册中的时间-电流曲线。

  选择适当的曲线，并将相应的电流和时间
  值分别输入到 **Tabulated currents** 和 **Tabulated
  opening time** 参数向量中。将此选项用于
  小电流。
