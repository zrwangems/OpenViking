---
type: simulink-block
title: 'Fuse'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Switches and Breakers / Switches and Breakers'
documentation_page: 'fuse'
documentation_source_path: 'ref/fuse.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuse

## 端口

### 守恒

### **+** — 正极端子电气

与熔断器正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与熔断器负极端子关联的电气守恒端口。
### 输出

### **x** — 熔断器状态物理信号

将熔断器状态输出为无量纲物理信号。如果熔断器完好，该端口输出 0；如果熔断器已熔断，则输出 1。

#### 依赖项

当 **PS output for fuse state** 参数设置为 `Visible` 时显示。

## 参数

### **Parameterization** — 断开时间对电流的模型依赖性 `Opening time is independent of current`（默认） | `Opening time depends on I^2*t` | `Opening time is tabulated`

选择断开时间是否取决于电流：

- `Opening time is independent of current`
  — 当流过熔断器的电流连续超过阈值电流的时间长于指定时间时，熔断器断开。
- `Opening time depends on I^2*t` —
  使熔断器断开取决于熔断器中耗散的能量。
  在操作的高电流范围使用此选项。
- `Opening time is tabulated` —
  使熔断器断开取决于平均时间-电流表格数据。对小电流使用此选项。

### **Rated current, I\_rated** — 标称工作电流 1 A（默认）

来自数据手册的熔断器额定值，或标称工作电流。

#### 依赖项

当 **Parameterization** 参数设置为 `Opening time is independent of current`
或 `Opening time depends on I^2*t` 时启用。

### **Ratio of minimum melting current to rated current, I\_melt/I\_rated** — 定义的熔化阈值电流 1（默认）

最小熔化电流定义熔断器工作阈值。如果流过熔断器的电流不超过此阈值，熔断器保持低欧姆状态。使用默认参数值 `1` 时，阈值电流与额定电流相同。在大多数情况下，此参数值应大于 1。也可以将其设置为小于 1 的值，适用于熔断器可能在低于额定电流的电流水平下熔断的情况（例如，由于高温或由于重复脉冲）。参数值必须大于 0。

#### 依赖项

当 **Parameterization** 参数设置为 `Opening time is independent of current`
或 `Opening time depends on I^2*t` 时启用。

### **Time to fuse** — 熔断器熔断所需的时间 0 s（默认）

熔断器熔断所需的时间。如果流过熔断器的电流连续超过阈值电流的时间长于该时间，熔断器进入高欧姆状态并断开电路。如果在时间耗尽前电流降至阈值以下，熔断器保持低欧姆状态。如果电流再次超过阈值，时间计数器重新开始。使用默认参数值 `0` 时，一旦电流超过最小熔化电流，熔断器立即熔断。参数值必须大于或等于 0。

#### 依赖项

当 **Parameterization** 参数设置为 `Opening time is independent of
current` 时启用。

### **Nominal melting, I^2\*t** — 熔断器熔断所需的耗散能量 1 s\*A^2（默认）

使熔断器熔断所需的在熔断器中耗散的能量。这是数据手册中的标称熔化值，或 I2t 参数。该值必须大于或等于 0。

#### 依赖项

当 **Parameterization** 参数设置为 `Opening time depends on I^2*t` 时启用。

### **Tabulated currents** — 来自时间-电流曲线的电流数据 [1.9, 2, 2.5, 30] A（默认）

来自制造商数据手册时间-电流曲线的表格电流值。此向量中的每个元素必须大于 0，并且向量必须严格递增。

#### 依赖项

当 **Parameterization** 参数设置为 `Opening time is tabulated` 时启用。

### **Tabulated opening times** — 来自时间-电流曲线的时间数据 [10000, 1, 0.3, 0.001] s（默认）

来自制造商数据手册时间-电流曲线的表格时间值。此向量中的每个元素必须大于或等于 0，并且向量必须严格递减。该向量必须与 **Tabulated currents** 向量大小相同。

#### 依赖项

当 **Parameterization** 参数设置为 `Opening time is tabulated` 时启用。

### **Fuse resistance R** — 熔断器电阻 0.01 Ω（默认）

低欧姆状态下的熔断器电阻。参数值必须大于 0。

### **Open-circuit conductance G** — 开路熔断器电导 1e-8 1/Ω（默认）

熔断器已熔断时，高欧姆状态下的开路熔断器电导。参数值必须大于 0。

### **PS output for fuse state** — 控制熔断器状态输出端口的可见性 `Hidden`（默认） | `Visible`

当设置为 `Visible` 时，模块图标上会出现一个 PS 输出端口 **x**。如果熔断器完好，该端口输出 0；如果熔断器已熔断，则输出 1。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

## 描述

用于防止过电流的 Fuse

Fuse 模块会断开电路，以保护电路免受过大电流的影响。该模块提供以下建模选项：

- `Opening time is independent of current` — 当流过熔断器的电流连续超过阈值电流的时间长于指定时间时，熔断器断开。此选项假设断开时间与电流无关。它还隐含假设一旦电流降至某个阈值以下，熔断器中的热量立即耗散。
- `Opening time depends on I^2*t` — 使熔断器断开取决于熔断器中耗散的能量。标称熔化值（I^2\*t）通常可在制造商数据手册中找到。如果选择此选项，熔断器在以下情况下熔断：

  ∫toverti2dt≥I2t

  其中 *t*over 是电流越过阈值电流的时间，*i* 是流过熔断器的瞬时电流，*I2t* 是数据手册中的标称熔化值。在操作的高电流范围使用此选项。
- `Opening time is tabulated` — 使熔断器断开取决于平均时间-电流表格数据。此数据表示在给定电流下熔断器断开所需的时间，并在制造商数据手册中以时间-电流曲线形式提供。

  例如，这些是 Littelfuse® 218 Series 熔断器数据手册中的时间-电流曲线。

  选择相应的曲线，并将对应的电流值和时间值分别输入到 **Tabulated currents** 和 **Tabulated opening time** 参数向量中。对小电流使用此选项。
