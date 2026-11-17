---
type: simulink-block
title: 'Ideal Rectangular Pulse Filter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Filters'
documentation_page: 'idealrectangularpulsefilter'
documentation_source_path: 'ref/idealrectangularpulsefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Rectangular Pulse Filter

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 列向量 | 矩阵
  direction: input
  data_types: double | single | fixed point
- name: Out
  summary: 输出信号 列向量 | 矩阵
  direction: output
  data_types: double | single | fixed point
```

### 输入

### **In** — 输入信号 标量 | 列向量 | 矩阵

输入信号，指定为标量、列向量或
*K*i×*N*
矩阵。*K*i 是每个信号通道的输入样本数，*N* 是信号通道数。

**数据类型：** `double` | `single` | `fixed point`
### 输出

### **Out** — 输出信号 列向量 | 矩阵

输出信号，返回为标量、列向量或矩阵。该模块对每个通道随时间进行滤波，并生成
*K*o×*N*
输出矩阵。输出信号的数据类型与输入信号相同。

- *K*o =
  *K*i ×
  *L*。
- *N* 是信号通道数。
- *K*i 是每个信号通道的输入样本数。
- *L* 是您在
  **Pulse length (number of samples)**
  参数中指定的值。

**数据类型：** `double` | `single` | `fixed point`
## 参数
```yaml
parameters:
- name: Pulse length (number of samples)
  summary: 脉冲长度 8（默认）| 正整数
  group: ''
- name: Pulse delay (number of samples)
  summary: 脉冲延迟 0（默认）| 非负整数
  group: ''
- name: Input processing
  summary: 输入处理控制 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
- name: Rate options
  summary: 模块处理速率 Enforce single-rate processing（默认）| Allow multirate processing
  group: ''
- name: Normalize output signal
  summary: 归一化输出信号的选项 off（默认）| on
  group: ''
- name: Normalization method
  summary: 归一化方法 Sum of samples（默认）| Energy per pulse
  group: ''
- name: Linear amplitude gain
  summary: 线性增益 1（默认）| 正标量
  group: ''
- name: Rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: ''
- name: Saturate on integer overflow
  summary: 定点运算的溢出模式 off（默认）| on
  group: ''
- name: Coefficients
  summary: '系数数据类型 Inherit: Same word length as input（默认）| fixdt(1,16) | fixdt(1,16,0)'
  group: ''
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0)'
  group: ''
- name: Accumulator
  summary: '累加器数据类型 Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
  group: ''
- name: Output
  summary: '输出数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
  group: ''
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: ''
```

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

#### 主要

### **Pulse length (number of samples)** — 脉冲长度 `8`（默认）| 正整数

以样本为单位的脉冲长度，指定为正整数。该模块将每个输入
样本复制 *L* 次，其中 *L* 是您以样本为单位指定的脉冲
长度。

### **Pulse delay (number of samples)** — 脉冲延迟 `0`（默认）| 非负整数

以样本为单位的脉冲延迟，指定为非负整数。如果此参数非零，
则该模块在仿真开始时输出该数量的零，然后才开始复制任何输入值。

### **Input processing** — 输入处理控制 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

输入处理控制，指定为以下选项之一：

- `Columns as channels (frame based)` — 该模块
  将输入的每一列视为单独的通道。
- `Elements as channels (sample based)` — 该模块
  将输入的每个元素视为单独的通道。

### **Rate options** — 模块处理速率 `Enforce single-rate processing`（默认）| `Allow multirate processing`

用于输入信号上采样和滤波的模块处理速率，指定为以下
选项之一：

- `Enforce single-rate processing` — 当您
  选择此选项时，该模块保持输入样本率，并通过将输出帧大小增加
  *N* 倍来处理信号。
- `Allow multirate processing` — 当您选择
  此选项时，该模块处理信号，使输出样本率
  比输入样本率快 *N* 倍。

#### 依赖关系

要使用 `Enforce single-rate processing`，您必须将
**Input processing** 设置为 `Columns as channels
(frame based)`。

### **Normalize output signal** — 归一化输出信号的选项 `off`（默认）| `on`

选择此参数可在应用线性幅度增益之前
对复制值集合进行缩放。

### **Normalization method** — 归一化方法 `Sum of samples`（默认）| `Energy per pulse`

归一化方法，指定为 `Sum of samples` 或
`Energy per pulse`。此参数指定该模块在缩放复制值集合时
所考虑的量。有关详细信息，请参阅归一化方法。

#### 依赖关系

此参数在您选择 **Normalize output signal** 时显示。

### **Linear amplitude gain** — 线性增益 `1`（默认）| 正标量

线性增益，指定为正标量。该模块按您指定的
线性增益值缩放输出信号。有关详细信息，请参阅归一化方法。

#### 数据类型

### **Rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。当定点计算的结果无法
精确映射到该数据类型可表示的数字时，该模块使用
舍入模式。滤波器系数不遵循此参数；它们始终舍入为
`Nearest`。有关详细信息，请参阅舍入模式
或舍入模式：Simplest (Fixed-Point Designer)。

### **Saturate on integer overflow** — 定点运算的溢出模式 `off`（默认）| `on`

选择定点运算的溢出模式。滤波器
系数不遵循此参数；它们始终饱和。

### **Coefficients** — 系数数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `fixdt(1,16,0)`

指定滤波器系数（分子和
分母）的字长和小数长度。

当您选择 `Inherit: Same word length as input` 时，滤波器系数的字
长与模块输入的字长匹配。在此模式下，系数的小数长度自动设置为
仅二进制小数点缩放，在给定系数值和字长的情况下为您提供
尽可能最佳的精度。

有关此模块中系数数据类型使用的更多信息和图示，请参阅
Discrete FIR Filter (Simulink)
模块的滤波器结构图。

滤波器系数不遵循 **Rounding
mode** 和 **Saturate
on integer overflow** 参数；它们始终饱和
并舍入为 `Nearest`。

有关指定数据类型的信息，请参阅数据类型助手。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出的字长和小数长度。

- 当您选择 `Inherit: Inherit via internal
  rule` 时，该模块基于内部规则继承数据类型。有关此规则的更多信息，请参阅
  通过内部规则继承。
- 当您选择 `Inherit: Same as
  input` 时，这些特性与模块输入的特性匹配。

有关此模块中乘积输出数据类型使用的更多信息和图示，请参阅
Discrete FIR Filter (Simulink) 和 Multiplication Data Types 的滤波器结构图。

有关指定数据类型的信息，请参阅数据类型助手。

### **Accumulator** — 累加器数据类型 `Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器的字长和小数长度。

- 当您选择 `Inherit via internal
  rule` 时，该模块基于内部规则继承数据类型。有关此规则的更多信息，请参阅
  通过内部规则继承。
- 当您选择 `Inherit: Same as
  input` 时，这些特性与模块输入的特性匹配。
- 当您选择 `Inherit: Same as product
  output` 时，这些特性与乘积输出的特性匹配。

有关此模块中累加器输出数据类型使用的更多信息和图示，请参阅
Discrete FIR Filter (Simulink) 和 Multiplication Data Types 的滤波器结构图。

有关指定数据类型的信息，请参阅数据类型助手。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出的字长和小数长度。

- 当您选择 `Inherit: Same as
  input` 时，这些特性与模块输入的特性匹配。
- 当您选择 `Inherit: Same as
  accumulator` 时，这些特性与累加器的特性匹配。
- 当您选择 `Inherit: Same as product
  output` 时，这些特性与乘积输出的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的
数据类型。有关详细信息，
请参阅 Fixed-Point Tool (Fixed-Point Designer)。
## 所属库

Communications Toolbox / Comm Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用理想矩形脉冲对输入信号进行整形

Ideal Rectangular Pulse Filter 模块使用矩形
脉冲对输入信号进行上采样和整形。在复制输入样本后，该模块还可以对输出信号进行归一化
并应用线性幅度增益。
