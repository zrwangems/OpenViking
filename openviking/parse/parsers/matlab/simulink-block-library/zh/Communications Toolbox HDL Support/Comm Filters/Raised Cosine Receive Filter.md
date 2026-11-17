---
type: simulink-block
title: 'Raised Cosine Receive Filter'
family: 'comm-filters'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Comm Filters'
documentation_page: 'raisedcosinereceivefilter'
documentation_source_path: '../comm/ref/raisedcosinereceivefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Raised Cosine Receive Filter

## 端口

### 输入

### **In** — 输入信号 列向量 | 矩阵

输入信号，指定为列向量或 *K*i-by-*N* 矩阵。*K*i 是每个信号通道的输入样本数，*N* 是信号通道数。

对于 *K*i-by-*N* 矩阵输入，该对象将输入矩阵的各列作为 *N* 个独立通道处理。

**数据类型：** `single` | `double` | `fixed point`

### 输出

### **Out** — 输出信号 列向量 | 矩阵

输出信号，以列向量或 *K*o-by-*N* 矩阵形式返回。*K*o 等于 *K*i / **Decimation factor**。*K*i 是每个信号通道的输入样本数，*N* 是信号通道数。

该模块随时间对每个通道进行滤波，并生成 *K*o-by-*N* 输出矩阵。输出信号的数据类型与输入信号相同。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

#### 主要

### **Filter shape** — 滤波器形状 `Square root`（默认）| `Normal`

滤波器形状，指定为 `Square root` 或 `Normal`。有关详细信息，请参阅滤波器特性。

### **Rolloff factor** — 滚降因子 `0.2`（默认）| 标量

滤波器的滚降因子，指定为范围 [`0`, `1`] 内的标量。

### **Filter span in symbols** — 以符号为单位的滤波器跨度 `10`（默认）| 偶正整数

以符号为单位的滤波器跨度，指定为偶正整数。该模块将理想升余弦滤波器的无限冲激响应长度截断为长度等于此参数值的 FIR。

### **Input samples per symbol** — 每符号输入样本数 `8`（默认）| 大于 `1` 的整数

每符号输入样本数，指定为大于 `1` 的整数值。此参数定义输入信号中表示一个符号的输入样本数。

### **Decimation factor** — 输入信号的抽取因子 `8`（默认）| 正整数

该模块应用于输入信号的抽取因子，指定为正整数。每符号输出样本数等于每符号输入样本数除以抽取因子。如果抽取因子为 1，则该模块仅应用滤波，不进行抽取。

### **Decimation offset** — 以样本为单位的抽取偏移量 `0`（默认）

以样本为单位的抽取偏移量，指定为范围 [`0`, (**Decimation factor** – `1`)] 内的整数。

### **Linear amplitude filter gain** — 线性滤波器增益 `1`（默认）| 正标量

线性滤波器增益，指定为正标量。该模块按您指定的线性滤波器增益值缩放归一化滤波器系数。

### **Input processing** — 输入处理控制 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

输入处理控制，指定为以下选项之一：

- `Columns as channels (frame based)` — 该模块将输入的每一列视为单独的通道。
- `Elements as channels (sample based)` — 该模块将输入的每个元素视为单独的通道。

### **Rate options** — 模块处理速率 `Enforce single-rate processing`（默认）| `Allow multirate processing`

用于输入信号降采样和滤波的模块处理速率，指定为以下选项之一：

- `Enforce single-rate processing` — 当您选择此选项时，该模块保持输入样本率，并通过将输出帧大小减小 *K* 倍来处理信号。
- `Allow multirate processing` — 当您选择此选项时，该模块处理信号，使得输出样本率比输入样本率慢 *K* 倍。

#### 依赖关系

要使用 `Enforce single-rate processing`，您必须将 **Input processing** 设置为 `Columns as channels (frame based)`。

### **Export filter coefficients to workspace** — 导出滤波器系数 `off`（默认）| `on`

选择此参数可将滤波器系数保存为 **Coefficient variable name** 参数中指定的 MATLAB® 工作区变量。

### **Coefficient variable name** — 系数变量名称 `rcRxFilt`（默认）

要在 MATLAB 工作区中创建的系数变量名称。

#### 依赖关系

当您选择 **Export filter coefficients to workspace** 时，此参数出现。

### **View Filter Response** — 打开滤波器可视化工具按钮

要分析升余弦滤波器响应，请点击 **View Filter Response** 按钮。MATLAB 将打开一个滤波器可视化窗口。当您更改模块掩码参数设置时，再次点击该按钮可打开该窗口的新实例并查看新的滤波器特性。先前的滤波器可视化窗口保持打开并反映您先前的掩码设置。关闭模型后，滤波器可视化窗口的实例仍保持打开。

#### 数据类型

### **Rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。当定点计算的结果不能精确映射到数据类型可表示的数字时，该模块使用舍入模式。滤波器系数不遵循此参数；它们始终舍入到 `Nearest`。有关详细信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

### **Saturate on integer overflow** — 定点运算的溢出模式 `off`（默认）| `on`

选择定点运算的溢出模式。滤波器系数不遵循此参数；它们始终饱和。

### **Coefficients** — 系数数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `fixdt(1,16,0)`

指定滤波器系数（分子和分母）的字长和小数长度。

此模块是一个子系统，包含一个 FIR Decimation 模块。有关此模块中系数数据类型用法的图示，请参阅 Discrete FIR Filter (Simulink) 模块的滤波器结构图。

当您选择 `Inherit: Same word length as input` 时，滤波器系数的字长与模块输入的字长匹配。在此模式下，系数的小数长度自动设置为仅二进制小数点定标，从而在给定系数值和字长的情况下为您提供可能的最佳精度。

滤波器系数不遵循 **Rounding mode** 和 **Saturate on integer overflow** 参数；它们始终饱和并舍入到 `Nearest`。

有关指定数据类型的信息，请参阅 Data Type Assistant。

### **Product output** — 乘积输出数据类型 `Inherit: Same as input`（默认）| `fixdt(1,16,0)`

指定乘积输出的字长和小数长度。有关此模块中乘积输出数据类型用法的图示，请参阅 Discrete FIR Filter (Simulink) 模块的滤波器结构图和 Multiplication Data Types。

当您选择 `Inherit: Same as input` 时，这些特性与模块输入的特性匹配。

有关指定数据类型的信息，请参阅 Data Type Assistant。

### **Accumulator** — 累加器数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定累加器的字长和小数长度。有关此模块中累加器数据类型用法的图示，请参阅 Discrete FIR Filter (Simulink) 模块的滤波器结构图和 Multiplication Data Types。

- 当您选择 `Inherit: Same as input` 时，这些特性与模块输入的特性匹配。
- 当您选择 `Inherit: Same as product output` 时，这些特性与乘积输出的特性匹配。

有关指定数据类型的信息，请参阅 Data Type Assistant。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定输出的字长和小数长度。

- 当您选择 `Inherit: Same as input` 时，这些特性与模块输入的特性匹配。
- 当您选择 `Inherit: Same as accumulator` 时，这些特性与累加器的特性匹配。

有关指定数据类型的信息，请参阅 Data Type Assistant。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。有关详细信息，请参阅 Fixed-Point Tool (Fixed-Point Designer)。

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

此模块在以下条件下支持使用 Intel® AVX2 技术生成 SIMD 代码：

- **Input processing** 设置为 `Columns as channels (frame based)`。
- **Rate options** 设置为 `Enforce single-rate processing`。
- 输入信号为实数值，且滤波器系数为实数。
- 输入信号为复数值，且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single` 或 `double`。

SIMD 技术显著提高生成代码的性能。有关详细信息，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

此模块是一个子系统，包含一个 FIR Decimation 模块。您可以在子系统上设置 **HDL Properties**，也可以查看掩码下并在滤波器模块上设置 **HDL Properties**。有关属性列表，请参阅 Subsystem, Atomic Subsystem, CodeReuse Subsystem (Simulink) 和 FIR Decimation 模块参考页的“HDL Code Generation”部分。

要在掩码下保存设置更改，必须断开库链接。要断开库链接，请选择 Raised Cosine Receive Filter 模块并运行此命令。

```
set_param(gcb,'LinkStatus','inactive')
```

## 版本历史

**在 R2006a 之前引入**

## 描述

使用升余弦 FIR 滤波器应用匹配滤波

Raised Cosine Receive Filter 模块使用升余弦有限脉冲响应 (FIR) 滤波器对输入信号进行滤波，并可选择对滤波后的信号进行抽取。该 FIR 滤波器具有（**Filter span in symbols** × **Input samples per symbol** + 1）个抽头系数。模块图标显示滤波器的冲激响应。有关详细信息，请参阅 Algorithms。
