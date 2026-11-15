---
type: simulink-block
title: 'Raised Cosine Transmit Filter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Filtering'
documentation_page: 'raisedcosinetransmitfilter'
documentation_source_path: 'ref/raisedcosinetransmitfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Raised Cosine Transmit Filter

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量 | 矩阵

输入信号，指定为标量、列向量或
*Ki*×*N*
矩阵。*Ki* 是每个信号通道的输入采样数，*N* 是信号通道数。

**数据类型：** `double` | `single` | `fixed point`
### 输出

### **Out** — 输出信号 标量 | 列向量 | 矩阵

输出信号，返回为标量、列向量或矩阵。该模块随时间对每个通道进行滤波，并生成
*Ko*×*N*
输出矩阵。输出信号的数据类型与输入信号相同。

- *Ko* =
  *Ki* ×
  *L*。
- *N* 是信号通道数。
- *Ki* 是每个信号通道的输入采样数。
- *L* 是您在
  **每个符号的输出采样数** 参数中指定的值。

**数据类型：** `double` | `single` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的
**准备** 库中，选择 **属性
检查器**。

#### 主要

### **滤波器形状** — 滤波器形状 `Square root` (默认) | `Normal`

滤波器形状，指定为 `Square root` 或
`Normal`。有关详细信息，请参阅滤波器特性。

### **滚降因子** — 滚降因子 `0.2` (默认) | 标量

滤波器的滚降因子，指定为 [`0`,
`1`] 范围内的标量。

### **以符号为单位的滤波器跨度** — 以符号为单位的滤波器跨度 `10` (默认) | 偶数正整数

以符号为单位的滤波器跨度，指定为偶数正整数。该模块
将理想升余弦滤波器的无限冲激响应长度截断为长度等于此参数值的 FIR。

### **每个符号的输出采样数** — 每个符号的输出采样数 `8` (默认) | 大于 `1` 的整数

每个符号的输出采样数，指定为大于
`1` 的整数值。升余弦滤波器的抽头数
等于此参数的值乘以 **以符号为单位的滤波器
跨度** 参数的值。

### **线性幅度滤波器增益** — 线性滤波器增益 `1` (默认) | 正标量

线性滤波器增益，指定为正标量。该模块按您指定的线性滤波器增益值缩放归一化
滤波器系数。

### **输入处理** — 输入处理控制 `Columns as channels (frame based)` (默认) | `Elements as channels (sample based)`

输入处理控制，指定为以下选项之一：

- `Columns as channels (frame based)` — 该模块
  将输入的每一列视为单独通道。
- `Elements as channels (sample based)` — 该模块
  将输入的每个元素视为单独通道。

### **速率选项** — 模块处理速率 `Enforce single-rate processing` (默认) | `Allow multirate processing`

用于输入信号上采样和滤波的模块处理速率，指定为以下
选项之一：

- `Enforce single-rate processing` — 当您
  选择此选项时，该模块保持输入采样率，并通过
  将输出帧大小增加
  *N* 倍来处理信号。
- `Allow multirate processing` — 当您选择
  此选项时，该模块处理信号，使得输出采样率
  比输入采样率快 *N* 倍。

#### 依赖关系

要使用 `Enforce single-rate processing`，必须将
**输入处理** 设置为 `Columns as channels
(frame based)`。

### **将滤波器系数导出到工作区** — 导出滤波器系数 `off` (默认) | `on`

选择此参数可将滤波器系数保存为在 **系数变量名称** 参数中指定的 MATLAB® 工作区变量。

### **系数变量名称** — 系数变量的名称 `rcTxFilt` (默认)

要在 MATLAB 工作区中创建的系数变量的名称。

#### 依赖关系

当您选择 **将
滤波器系数导出到工作区** 时，此参数出现。

### **查看滤波器响应** — 打开滤波器可视化工具按钮

要分析升余弦滤波器响应，请点击 **查看
滤波器响应** 按钮。MATLAB 会打开一个滤波器可视化窗口。当您更改模块
掩码参数设置时，再次点击该按钮可打开窗口的新实例
并查看新的滤波器特性。以前的滤波器
可视化窗口保持打开，并反映您以前的掩码设置。
关闭模型后，滤波器可视化窗口的实例保持打开。

#### 数据类型

### **舍入模式** — 定点运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。当定点计算的结果无法
精确映射到该数据类型可表示的数字时，模块使用
舍入模式。滤波器系数
不受此参数影响；它们始终舍入到
`Nearest`。有关详细信息，请参阅舍入模式
或舍入模式: Simplest (Fixed-Point Designer)。

### **对整数溢出进行饱和处理** — 定点运算的溢出模式 `off` (默认) | `on`

选择定点运算的溢出模式。滤波器
系数不受此参数影响；它们始终饱和。

### **系数** — 系数数据类型 `Inherit: Same word length as input` (默认) | `fixdt(1,16)` | `fixdt(1,16,0)`

指定滤波器系数
（分子和分母）的字长和小数长度。

此模块是一个包含 FIR Interpolation 模块的子系统。关于
显示此模块中系数数据类型用法的图，请参阅
Discrete FIR Filter (Simulink)
模块的滤波器结构图。

当您选择 `Inherit: Same word length as input` 时，滤波器系数的字长
与模块输入的字长匹配。在
此模式下，系数的小数长度自动设置为
仅二进制点定标，从而在给定系数值和字长的情况下为您提供
尽可能高的精度。

滤波器系数不受 **舍入
模式** 和 **对整数溢出
进行饱和处理** 参数影响；它们始终饱和
并舍入到 `Nearest`。

有关指定数据类型的信息，请参阅数据类型助手。

### **乘积输出** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出的字长和小数长度。关于显示
此模块中乘积输出数据类型用法的图，请参阅
Discrete FIR Filter (Simulink) 模块的滤波器
结构图和乘法数据类型。

- 当您选择 `Inherit via internal
  rule` 时，该模块基于
  内部规则继承数据类型。有关此规则的详细信息，请参阅
  Inherit via Internal Rule。
- 当您选择 `Inherit: Same as
  input` 时，这些特性与
  模块输入的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器的字长和小数长度。关于显示
此模块中累加器数据类型用法的图，请参阅 Discrete FIR Filter (Simulink) 模块的滤波器结构
图和乘法数据类型。

- 当您选择 `Inherit: Inherit via internal
  rule` 时，该模块基于
  内部规则继承数据类型。有关此规则的详细信息，请参阅
  Inherit via Internal Rule。
- 当您选择 `Inherit: Same as
  input` 时，这些特性与
  模块输入的特性匹配。
- 当您选择 `Inherit: Same as product
  output` 时，这些特性与
  乘积输出的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **输出** — 输出数据类型 `Inherit: Same as accumulator` (默认) | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定输出的字长和小数长度。

- 当您选择 `Inherit: Same as
  input` 时，这些特性与
  模块输入的特性匹配。
- 当您选择 `Inherit: Same as
  accumulator` 时，这些特性与
  累加器的特性匹配。
- 当您选择 `Inherit: Same as product
  output` 时，这些特性与
  乘积输出的特性匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的
数据类型。有关详细信息，请参阅
定点工具 (Fixed-Point Designer)。

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

在某些条件下，生成的代码依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

此模块在以下条件下支持使用 Intel® AVX2 技术生成 SIMD 代码：

- **输入处理** 设置为 `Columns
  as channels (frame based)`。
- **速率选项** 设置为 `Enforce
  single-rate processing`。
- 输入信号为实值且具有实滤波器系数。
- 输入信号为复值且具有实或复滤波器
  系数。
- 输入信号的数据类型为 `single` 或
  `double`。

SIMD 技术显著提高生成代码的性能。有关详细信息，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL
实现和综合逻辑的附加配置选项。

此模块是一个包含 FIR Interpolation 模块的子系统。您可以在
子系统上设置 **HDL 属性**，或者查看掩码下并在滤波器模块上设置 **HDL 属性**。有关属性列表，请参阅
Subsystem、Atomic Subsystem、CodeReuse
Subsystem (Simulink) 和 FIR Interpolation 模块参考页的 "HDL
Code Generation" 部分。

要保存掩码下的设置更改，必须断开库链接。要断开
库链接，请选择 Raised Cosine Transmit Filter 模块并运行
以下
命令。

```
set_param(gcb,'LinkStatus','inactive')
```

## 版本历史

**Introduced before R2006a**

## 描述

使用升余弦 FIR 滤波器对信号进行插值来应用脉冲整形

Raised Cosine Transmit Filter 模块通过使用升余弦有限冲激响应 (FIR) 滤波器对输入信号进行插值来应用脉冲整形。该 FIR 滤波器具有
(**以符号为单位的滤波器
跨度** × **每个符号的输出
采样数** + 1) 个抽头系数。模块图标显示滤波器的冲激响应。
有关详细信息，请参阅算法。
