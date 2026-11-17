---
type: simulink-block
title: 'Raised Cosine Transmit Filter'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Filters'
documentation_page: 'raisedcosinetransmitfilter'
documentation_source_path: 'ref/raisedcosinetransmitfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Raised Cosine Transmit Filter

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 列向量 | 矩阵
  direction: input
  data_types: double | single | fixed point
- name: Out
  summary: 输出信号 标量 | 列向量 | 矩阵
  direction: output
  data_types: double | single | fixed point
```

### 输入

### **In** — 输入信号 标量 | 列向量 | 矩阵

输入信号，指定为标量、列向量或
*K*i×*N*
矩阵。*K*i 是每个信号通道的
输入样本数，*N* 是信号
通道数。

**数据类型：** `double` | `single` | `fixed point`
### 输出

### **Out** — 输出信号 标量 | 列向量 | 矩阵

输出信号，返回为标量、列向量或矩阵。该模块对每个
通道随时间进行滤波，并生成一个
*K*o×*N*
输出矩阵。输出信号的数据类型与输入信号相同。

- *K*o =
  *K*i ×
  *L*。
- *N* 是信号
  通道数。
- *K*i 是每个信号通道的
  输入样本数。
- *L* 是您在
  **Output samples per symbol** 参数中指定的值。

**数据类型：** `double` | `single` | `fixed point`
## 参数
```yaml
parameters:
- name: Filter shape
  summary: 滤波器形状 Square root（默认）| Normal
  group: ''
- name: Rolloff factor
  summary: 滚降因子 0.2（默认）| 标量
  group: ''
- name: Filter span in symbols
  summary: 以符号为单位的滤波器跨度 10（默认）| 偶数正整数
  group: ''
- name: Output samples per symbol
  summary: 每个符号的输出样本数 8（默认）| 大于 1 的整数
  group: ''
- name: Linear amplitude filter gain
  summary: 线性滤波器增益 1（默认）| 正标量
  group: ''
- name: Input processing
  summary: 输入处理控制 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
- name: Rate options
  summary: 模块处理速率 Enforce single-rate processing（默认）| Allow multirate processing
  group: ''
- name: Export filter coefficients to workspace
  summary: 导出滤波器系数 off（默认）| on
  group: ''
- name: Coefficient variable name
  summary: 系数变量名称 rcTxFilt（默认）
  group: ''
- name: View Filter Response
  summary: 打开滤波器可视化工具 按钮
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
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
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

### **Filter shape** — 滤波器形状 `Square root`（默认）| `Normal`

滤波器形状，指定为 `Square root` 或
`Normal`。有关详细信息，请参阅滤波器特性。

### **Rolloff factor** — 滚降因子 `0.2`（默认）| 标量

滤波器的滚降因子，指定为 [`0`,
`1`] 范围内的标量。

### **Filter span in symbols** — 以符号为单位的滤波器跨度 `10`（默认）| 偶数正整数

以符号为单位的滤波器跨度，指定为偶数正整数。该模块
将理想升余弦滤波器的无限冲激响应长度截断为
长度等于此参数值的 FIR。

### **Output samples per symbol** — 每个符号的输出样本数 `8`（默认）| 大于 `1` 的整数

每个符号的输出样本数，指定为大于
`1` 的整数值。升余弦滤波器的抽头数
等于此参数的值乘以 **Filter
span in symbols** 参数的值。

### **Linear amplitude filter gain** — 线性滤波器增益 `1`（默认）| 正标量

线性滤波器增益，指定为正标量。该模块将归一化
滤波器系数乘以您指定的线性滤波器增益值。

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
  选择此选项时，该模块保持输入采样率，并通过
  将输出帧大小增加 *N* 倍来处理
  信号。
- `Allow multirate processing` — 当您选择
  此选项时，该模块处理信号，使得输出采样率
  比输入采样率快 *N* 倍。

#### 依赖关系

要使用 `Enforce single-rate processing`，您必须将
**Input processing** 设置为 `Columns as channels
(frame based)`。

### **Export filter coefficients to workspace** — 导出滤波器系数 `off`（默认）| `on`

选择此参数可将滤波器系数保存为 MATLAB® 工作区变量，变量名在 **Coefficient variable name** 参数中指定。

### **Coefficient variable name** — 系数变量名称 `rcTxFilt`（默认）

要在 MATLAB 工作区中创建的系数变量的名称。

#### 依赖关系

此参数在您选择 **Export
filter coefficients to workspace** 时显示。

### **View Filter Response** — 打开滤波器可视化工具 按钮

要分析升余弦滤波器响应，请点击 **View
Filter Response** 按钮。MATLAB 会打开一个滤波器可视化窗口。当您更改模块封装参数设置时，再次点击该按钮可打开该窗口的新实例
并查看新的滤波器特性。之前的滤波器
可视化窗口保持打开状态，并反映您之前的封装设置。
滤波器可视化窗口的实例在您关闭
模型后仍保持打开状态。

#### 数据类型

### **Rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。当定点计算的结果无法
精确映射到数据类型可表示的数字时，该模块使用
舍入模式。滤波器系数
不受此参数约束；它们始终舍入为
`Nearest`。有关详细信息，请参阅舍入模式
或舍入模式：Simplest（Fixed-Point Designer）。

### **Saturate on integer overflow** — 定点运算的溢出模式 `off`（默认）| `on`

选择定点运算的溢出模式。滤波器
系数不受此参数约束；它们始终饱和。

### **Coefficients** — 系数数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `fixdt(1,16,0)`

指定滤波器系数（分子和分母）的字长和小数
长度。

此模块是一个包含 FIR Interpolation 模块的子系统。有关
显示此模块中系数数据类型使用的图示，请参阅
Discrete FIR Filter (Simulink)
模块的滤波器结构图。

当您选择 `Inherit: Same word length as input` 时，滤波器系数的字
长与模块输入的字长匹配。在此
模式下，系数的小数长度自动设置为
二进制点定标，在给定系数值和字长的情况下为您提供最佳精度。

滤波器系数不受 **Rounding
mode** 和 **Saturate
on integer overflow** 参数约束；它们始终饱和
并舍入为 `Nearest`。

有关指定数据类型的信息，请参阅数据类型助手。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出的字长和小数长度。有关显示
此模块中乘积输出数据类型使用的图示，请参阅
Discrete FIR Filter (Simulink) 模块的滤波器
结构图和乘法数据类型。

- 当您选择 `Inherit via internal
  rule` 时，该模块根据
  内部规则继承数据类型。有关此规则的详细信息，请参阅
  通过内部规则继承。
- 当您选择 `Inherit: Same as
  input` 时，这些特性与模块
  输入的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器的字长和小数长度。有关显示
此模块中累加器数据类型使用的图示，请参阅
Discrete FIR Filter (Simulink) 模块的滤波器结构
图和乘法数据类型。

- 当您选择 `Inherit: Inherit via internal
  rule` 时，该模块根据
  内部规则继承数据类型。有关此规则的详细信息，请参阅
  通过内部规则继承。
- 当您选择 `Inherit: Same as
  input` 时，这些特性与模块
  输入的特性匹配。
- 当您选择 `Inherit: Same as product
  output` 时，这些特性与乘积
  输出的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出的字长和小数长度。

- 当您选择 `Inherit: Same as
  input` 时，这些特性与模块
  输入的特性匹配。
- 当您选择 `Inherit: Same as
  accumulator` 时，这些特性与累加器的
  特性匹配。
- 当您选择 `Inherit: Same as product
  output` 时，这些特性与乘积
  输出的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的
数据类型。有关详细信息，
请参阅 Fixed-Point Tool (Fixed-Point Designer)。
## 所属库

Communications Toolbox / Comm Filters Communications Toolbox HDL Support / Comm Filters

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

生成的代码在某些条件下依赖 `memcpy` 或
`memset` 函数（`string.h`）。

此模块在这些条件下支持使用 Intel® AVX2 技术进行 SIMD 代码生成：

- **Input processing** 设置为 `Columns
  as channels (frame based)`。
- **Rate options** 设置为 `Enforce
  single-rate processing`。
- 输入信号为实值且滤波器系数为实数。
- 输入信号为复值且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single` 或
  `double`。

SIMD 技术显著提高了生成代码的性能。有关详细信息，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

此模块是一个包含 FIR Interpolation 模块的子系统。您可以
在子系统上设置 **HDL Properties**，也可以查看掩码下方并在滤波器模块上设置 **HDL Properties**。有关属性列表，请参阅 Subsystem, Atomic Subsystem, CodeReuse
Subsystem (Simulink) 和 FIR Interpolation 模块参考页面的“HDL
代码生成”部分。

要保存掩码下的设置更改，您必须断开库链接。要断开
库链接，请选择 Raised Cosine Transmit Filter 模块并运行
以下命令。

```
set_param(gcb,'LinkStatus','inactive')
```

## 版本历史

**在 R2006a 之前推出**

## 描述

通过使用升余弦 FIR 滤波器对信号进行插值来应用脉冲整形

Raised Cosine Transmit Filter 模块通过使用升余弦有限冲激响应（FIR）滤波器对输入信号进行插值来应用脉冲整形。该 FIR 滤波器具有
（**Filter span in
symbols** × **Output samples per
symbol** + 1）个抽头系数。模块图标显示滤波器的冲激响应。有关详细信息，请参阅算法。
