---
type: simulink-block
title: 'Biquad Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Single-Rate Filters / IIR'
documentation_page: 'biquadfilter'
documentation_source_path: 'ref/biquadfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Biquad Filter

## 端口

### 输入

### **In** — 数据输入向量 | 矩阵

模块的数据输入，指定为向量或矩阵。此模块支持可变大小输入信号，使您能够在仿真期间更改输入帧大小（行数）。但是，通道数（列数）必须保持不变。

如果输入为定点，则它必须为采用二进制小数点缩放的带符号定点。

除非将 **Coefficient source** 设置为 `Input port(s)`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是

### **Num** — 分子系数矩阵

双二阶滤波器的分子系数，指定为 3×*N* 矩阵，其中 *N* 是双二阶滤波器节的数量。

如果 **Num** 为定点，则它必须为采用二进制小数点缩放的带符号定点。

#### 依赖关系

仅当将 **Coefficient source** 设置为 `Input port(s)` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### **Den** — 分母系数矩阵

双二阶滤波器的分母系数，指定为 2×*N* 矩阵，其中 *N* 是双二阶滤波器节的数量。

如果 **Den** 为定点，则它必须为采用二进制小数点缩放的带符号定点。

#### 依赖关系

仅当将 **Coefficient source** 设置为 `Input port(s)` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### **g** — 缩放值行向量

双二阶滤波器的缩放值，指定为 1×(*N*+1) 向量，其中 *N* 是双二阶滤波器节的数量。

如果 **g** 为定点，则它必须为采用二进制小数点缩放的带符号定点。

#### 依赖关系

仅当将 **Coefficient source** 设置为 `Input port(s)` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### 输出

### **Out** — 滤波后的输出向量 | 矩阵

滤波后的输出，以向量或矩阵形式返回。

输出维度始终等于输入信号的维度。

如果 **Out** 为定点，则它必须为采用二进制小数点缩放的带符号定点。

除非将 **Coefficient source** 设置为 `Input port(s)`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **Coefficient source** — 操作模式 `Dialog parameters`（默认） | `Input port(s)` | `Filter object`

Biquad Filter 模块可以三种不同模式运行：

- `Dialog parameters` — 在模块封装中输入有关滤波器的信息，例如结构和系数。
- `Input port(s)` — 使用 **Filter structure** 参数在模块封装中输入有关滤波器结构的信息。滤波器系数通过出现在模块图标上的附加输入端口进入模块：

  - `Num` — 指定分子系数。
  - `Den` — 指定分母系数。
  - `g` — 指定缩放值。

  该模块假定每个节的第一个分母系数为 1。当 **Coefficient source** 设置为 `Input port(s)` 且 **Scale values mode** 设置为 `Specify via input port (g)` 时，此配置适用。
- `Filter object` — 使用 `dsp.BiquadFilter` System object™ 指定滤波器。

### **Filter** — 滤波器对象名称 `BQF`（默认） | `dsp.BiquadFilter System object` 名称

指定希望模块实现的离散时间滤波器的名称。必须将该滤波器指定为 `dsp.BiquadFilter` System object。

您可以在模块封装中或 MATLAB® 工作区变量中定义 System object。

有关创建 System object 的信息，请参阅 Define Basic System Objects。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Filter object` 时，此参数才可见。

### **Filter structure** — 滤波器结构 `Direct form II transposed`（默认） | `Direct form I` | `Direct form I transposed` | `Direct form II`

指定滤波器结构。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 时，此参数才可见。

### **SOS Matrix (Mx6)** — SOS 矩阵 `[1 0.3 0.4 1 0.1 0.2]`（默认） | *M*×6 矩阵

指定 *M*×6 矩阵，其中 *M* 是二阶节滤波器中的节数。SOS 矩阵的每一行包含滤波器中对应节的分子和分母系数（*bik* 和 *aik*）。

[b01b11b21a01a11a21b02b12b22a02a12a22⋮⋮⋮⋮⋮⋮b0Mb1Mb2Ma0Ma1Ma2M]

无论实际值如何，前导分母系数 [a01
a02 ... a0N] 均被视为 1。当 **a0** 不为 1 时，不对 SOS 矩阵应用缩放。

`ss2sos` 和 `tf2sos` 函数将滤波器的状态空间或传递函数描述转换为此模块使用的二阶节描述。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数才可见。

### **Scale values** — 缩放值 `1`（默认） | 标量 | 向量

指定要在 SOS 节之间使用的缩放值。您可以指定实数值标量或长度为 *M*+1 的向量：

- 输入标量时，该值指定二阶滤波器第一节之前的增益值。其余增益值默认为 1。
- 输入 *M*+1 个值的向量时，每个值指定滤波器的单独节。例如，第一个元素是第一个增益值，第二个元素是第二个增益值，依此类推。

当一个或多个缩放值等于 1 时，选中 **Optimize unity scale values** 复选框以优化仿真。选择此选项会移除单位增益，使这些值像 Simulink 线或连线一样处理。在某些具有单位缩放值的定点情况下，选择此参数还会省略某些强制转换。有关详细信息，请参阅定点数据类型部分。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数才可见。

### **Initial conditions** — 初始条件 `0`（默认） | 标量 | 向量

当 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed` 时，指定滤波器状态的初始条件。

**Direct form II**

**Direct form II transposed**

默认情况下，Biquad Filter 模块将内部滤波器状态初始化为零。要为滤波器延迟指定非零初始状态，请使用 **Initial conditions** 参数。

要确定必须指定的初始条件数量以及如何指定它们，请参阅下表中关于有效初始条件的内容。

**有效的初始条件**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵   （用于对每个通道应用不同的延迟元素） | 每个向量或矩阵元素为对应通道中的对应延迟元素指定唯一的初始条件。*M* 是节数，*N* 是输入通道数：  - 向量长度必须等于滤波器中的延迟元素数，2*M*。 - 矩阵的行数必须等于滤波器中的延迟元素数 2*M**N*。矩阵还必须为输入信号的每个通道包含一列。 |

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)`，且 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed` 时，此参数才可见。

### **Initial conditions on zeros side** — 零点侧初始条件 `0`（默认） | 标量 | 向量

指定滤波器结构中零点侧（*b0*、*b1*、*b2*、…）滤波器状态的初始条件。此参数仅当 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时适用。

**Direct form I**

**Direct form I transposed**

默认情况下，Biquad Filter 模块将内部滤波器状态初始化为零。要为滤波器延迟指定非零初始状态，请使用 **Initial conditions on zeros side** 参数。

要确定必须指定的初始条件数量以及如何指定它们，请参阅下表中关于有效初始条件的内容。

**有效的初始条件**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵   （用于对每个通道应用不同的延迟元素） | 每个向量或矩阵元素为对应通道中的对应延迟元素指定唯一的初始条件。其中 *M* 是节数，*N* 是输入通道数：  - 向量长度必须等于滤波器中的延迟元素数，2*M*。 - 矩阵的行数必须等于滤波器中的延迟元素数 2*M**N*。矩阵还必须为输入信号的每个通道包含一列。 |

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)`，且 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时，此参数才可见。

### **Initial conditions on poles side** — 极点侧初始条件 `0`（默认） | 标量 | 向量

指定滤波器结构中极点侧（*a1*、*a2*、...）滤波器状态的初始条件。此参数仅当 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时适用。

**Direct form I**

**Direct form I transposed**

默认情况下，Biquad Filter 模块将内部滤波器状态初始化为零。要为滤波器延迟指定非零初始状态，请使用 **Initial conditions on poles side** 参数。

要确定必须指定的初始条件数量以及如何指定它们，请参阅下表中关于有效初始条件的内容。

**有效的初始条件**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵   （用于对每个通道应用不同的延迟元素） | 每个向量或矩阵元素为对应通道中的对应延迟元素指定唯一的初始条件。其中 *M* 是节数，*N* 是输入通道数：  - 向量长度必须等于滤波器中的延迟元素数，2*M*。 - 矩阵的行数必须等于滤波器中的延迟元素数 2*M**N*。矩阵还必须为输入信号的每个通道包含一列。 |

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)`，且 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed` 时，此参数才可见。

### **Scale values mode** — 指定缩放值的模式 `Specify via input port (g)`（默认） | `Assume all are unity and optimize`

选择如何指定要在滤波器节之间使用的缩放值。选择 `Specify via input port (g)` 时，您在端口 **g** 处将缩放值输入为二维向量。选择 `Assume all are unity and optimize` 时，所有缩放值都会被移除，并像 Simulink 线或连线一样处理。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Input port(s)` 时，此参数才可见。

### **Action when the a0 values of the SOS matrix are not one** — 当 SOS 矩阵的 a0 值不为 1 时的操作 `Warning`（默认） | `None` | `Error`

指定当 SOS 矩阵 *a0j* 值不等于 1 时模块应执行的操作。该操作可以是 `Warning`、`Error` 或 `None`。

选择 `None` 时，无论实际值如何，前导系数 *a0j* 均被视为 1。当 **a0** 不为 1 时，不对 SOS 矩阵应用缩放。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数才可见。

### **Optimize unity scale values** — 优化单位缩放值 `on`（默认） | `off`

当一个或多个缩放值等于 1 时，选中此复选框以优化仿真。选择此选项会移除单位增益，使这些值像 Simulink 线或连线一样处理。在某些具有单位缩放值的定点情况下，选择此参数还会省略某些强制转换。有关详细信息，请参阅定点数据类型部分。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数才可见。

### **Input processing** — 输入处理 `Columns as channels (frame based)`（默认） | `Elements as channels (sample based)`

指定模块应如何处理输入。如果输入是 *M*×*N* 矩阵，则可以将此参数设置为：

- `Columns as channels (frame based)`（默认） — 模块将每一列视为单独的通道。在此模式下，模块创建同一滤波器的 *M* 个实例，每个实例都有自己的独立状态缓冲区。这 *M* 个滤波器中的每个滤波器在每个 Simulink 时间步处理 *N* 个输入样本。
- `Elements as channels (sample based)` — 模块将每个元素视为单独的通道。在此模式下，模块创建同一滤波器的 *M**N* 个实例，每个实例都有自己的独立状态缓冲区。每个滤波器在每个 Simulink 时间步处理一个输入样本。

### **View Filter Response** — 查看滤波器响应按钮

此按钮打开 Filter Visualization Tool (FVTool)，并显示对话框中指定的滤波器的滤波器响应。

**注意**

当您在模块对话框中更改滤波器参数后，必须先点击 **Apply** 按钮，然后才能使用 **View Filter Response** 按钮。

### 数据类型选项卡

**注意**

仅当将 **Coefficient source** 设置为 `Dialog parameters` 或 `Input port(s)` 时，此选项卡才会出现。当 **Coefficient source** 设置为 `Filter object` 时，模块使用滤波器对象属性中指定的数据类型。

### **Rounding mode** — 舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。

有关详细信息，请参阅舍入模式。滤波器系数不遵循此参数；相反，它们始终舍入到 `Nearest`。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认） | `on`

选中此参数时，模块对其定点运算结果进行饱和处理。清除此参数时，模块对其定点运算结果进行回绕。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

滤波器系数始终饱和，不遵循此参数。

### **Section input** — 节输入数据类型 `Same as input`（默认） | `Binary point scaling`

选择如何指定进入双二阶滤波器每个节的定点数据类型的字长和小数长度。有关描述此模块中节输入数据类型用法的图示，请参阅定点数据类型部分。选择以下项时：

- `Same as input` — **Section input** 数据类型的字长和小数长度特性与模块输入的字长和小数长度特性匹配。
- `Binary point scaling` — 以位为单位输入节输入的字长和小数长度。

### **Section output** — 节输出数据类型 `Same as section input`（默认） | `Binary point scaling`

选择如何指定从双二阶滤波器每个节输出的定点数据类型的字长和小数长度。有关描述此模块中节输出数据类型用法的图示，请参阅定点数据类型部分。选择以下项时：

- `Same as section input` — **Section output** 数据类型的字长和小数长度特性与模块输入的字长和小数长度特性匹配。
- `Binary point scaling` — 以位为单位输入节输出的字长和小数长度。

### **Multiplicand** — 被乘数数据类型 `Same as output`（默认） | `Binary point scaling`

选择如何指定 `Direct form I transposed` 滤波器结构的被乘数数据类型的字长和小数长度。有关描述此模块中被乘数数据类型用法的图示，请参阅定点数据类型部分。

选择以下项时：

- `Same as output` — **Multiplicand** 数据类型的字长和小数长度特性与模块输出的字长和小数长度特性匹配。
- `Binary point scaling` — 以位为单位输入被乘数的字长和小数长度。

#### 依赖关系

仅当 **Filter structure** 参数设置为 `Direct form I transposed` 时，此参数才可见。

### **Coefficients** — 系数数据类型 `Same word length as input`（默认） | `Specify word length` | `Binary point scaling`

当 **Coefficient source** 设置为 `Dialog parameters` 时，选择如何指定滤波器系数（分子、分母和缩放值）的字长和小数长度。有关描述此模块中系数数据类型用法的图示，请参阅定点数据类型部分。选择以下项时：

- `Same word length as input` — 滤波器系数的字长与模块输入的字长匹配。在此模式下，模块自动将系数的小数长度设置为仅二进制小数点缩放，从而在给定系数值和字长的情况下提供尽可能最佳的精度。
- `Specify word length` — 以位为单位输入系数的字长。在此模式下，模块自动将系数的小数长度设置为仅二进制小数点缩放，从而在给定系数值和字长的情况下提供尽可能最佳的精度。
- `Binary point scaling` — 以位为单位输入系数的字长和小数长度。如果适用，请分别为分子和分母系数输入不同的小数长度。

滤波器系数不遵循 **Rounding mode** 和 **Overflow mode** 参数；相反，它们始终饱和并舍入到 `Nearest`。

#### 依赖关系

仅当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数才可见。

### **Product output** — 乘积输出数据类型 `Same as input`（默认） | `Inherit via internal rule` | `Binary point scaling`

指定如何设定乘积输出的字长和小数长度。有关描述此模块中乘积输出数据类型用法的图示，请参阅 Multiplication Data Types 和定点数据类型部分。选择以下项时：

- `Same as input` — 乘积输出的字长和小数长度特性与模块输入的字长和小数长度特性匹配。
- `Inherit via internal rule` — 乘积输出的字长和小数长度根据全精度规则计算。这些规则防止模块内部发生量化。根据需要添加位，以便不发生舍入或溢出。有关详细信息，请参阅 Inherit via Internal Rule。
- `Binary point scaling` — 以位为单位输入乘积输出的字长和小数长度。如果适用，请分别为分子和分母乘积输出数据类型输入不同的小数长度。

### **Accumulator** — 累加器数据类型 `Same as product output`（默认） | `Same as input` | `Binary point scaling`

指定如何设定累加器的字长和小数长度。有关描述此模块中累加器数据类型用法的图示，请参阅 Multiplication Data Types 和定点数据类型部分。选择以下项时：

- `Same as input` — 累加器的字长和小数长度特性与模块输入的字长和小数长度特性匹配。
- `Same as product output` — 累加器的字长和小数长度特性与乘积输出的字长和小数长度特性匹配。
- `Binary point scaling` — 以位为单位输入累加器的字长和小数长度。如果适用，请分别为分子和分母累加器数据类型输入不同的小数长度。

### **States** — 状态数据类型 `Same as accumulator`（默认） | `Same as input` | `Binary point scaling`

当 **Coefficient source** 设置为 `Dialog parameters` 时，指定如何设定状态的字长和小数长度。有关描述此模块中状态数据类型用法的图示，请参阅定点数据类型部分。

选择以下项时：

- `Same as input` — 状态的字长和小数长度特性与模块输入的字长和小数长度特性匹配。
- `Same as accumulator` — 状态的字长和小数长度特性与累加器的字长和小数长度特性匹配。
- `Binary point scaling` — 以位为单位输入状态的字长和小数长度。如果适用，请分别为分子和分母状态数据类型输入不同的小数长度。

#### 依赖关系

仅当 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed` 时，此参数才可见。

### **Output** — 输出数据类型 `Same as accumulator`（默认） | `Same as input` | `Binary point scaling`

选择如何指定输出的字长和小数长度。有关描述此模块中输出数据类型用法的图示，请参阅定点数据类型部分。选择以下项时：

- `Same as input` — 输出的字长和小数长度特性与模块输入的字长和小数长度特性匹配。
- `Same as accumulator` — 输出的字长和小数长度特性与累加器的字长和小数长度特性匹配。
- `Binary point scaling` — 以位为单位输入输出的字长和小数长度。

### **Lock data type settings against changes by the fixed-point tools** — 锁定数据类型设置 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在模块封装中指定的数据类型。

## 所属库

DSP System Toolbox / Filtering / Filter Implementations DSP System Toolbox HDL Support / Filtering

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**注意**

对于具有硬件友好控制信号的 HDL 优化双二阶滤波器架构，请使用 Biquad Filter (DSP HDL Toolbox) 模块。DSP HDL Toolbox™ 模块在 Simulink 中仿真 HDL 算法的延迟。DSP HDL Toolbox 模块生成适合 FPGA 上 DSP 模块的 direct form II 或 direct form II transposed 流水线加法-乘法运算。它提供可选的流水线反馈架构，该架构使用更多乘法器，但缩短了关键路径并实现更高的时钟速率。DSP HDL Toolbox 模块不支持可编程系数。要执行多通道滤波，请将 DSP HDL Toolbox Biquad Filter 模块放入 For Each 子系统中。

**HDL 架构**

该模块将 `HDLDataPath` 作为默认架构。此架构提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenFilter** | 从生成的 HDL 代码中移除 Filter 子系统的层次结构。默认值为 `auto`。请参阅 FlattenHierarchy (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效资源数。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 要经时间复用以转换为串行标量数据路径的并行数据路径（或向量）数。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **MultiplerArchitecture** | 选择乘法器架构为 `linear` 或 `shiftadd`。默认值为 `linear`。有关详细信息，请参阅 Product, Matrix Multiply (Simulink) 中的 HDL Code Generation 部分。 |
| **MultiplierInputPipeline** | 指定要在滤波器乘法器输入处添加的流水线级数。另请参阅 MultiplierInputPipeline (HDL Coder)。 |
| **MultiplierOutputPipeline** | 指定要在滤波器乘法器输出处添加的流水线级数。另请参阅 MultiplierOutputPipeline (HDL Coder)。 |
| **SectionOutputPipeline** | 指定要为节输出添加的流水线级数。默认值为 `0`。 |
| **AdderOutputPipeline** | 要为加法运算在生成代码中插入的输出流水线级数。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量 向量 矩阵 | 是 | Half  Single  Double | 是 | 是 | 是 | 是 | 是 |

**模块参数配置**

以下模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制 |
| --- | --- |
| **Input processing** | 不支持参数值 `Columns as channels (frame based)`。 |

**优化**

该模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* 是一种面积优化，其中 HDL Coder 识别多个功能等效资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *Streaming* 是一种面积优化，其中 HDL Coder 将向量数据路径转换为标量数据路径（或转换为若干个较小大小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*，或寄存器重定时，是一种速度优化，它在保持功能行为的同时移动设计中的现有延迟以缩短关键路径。 |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* 是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* 优化创建带寄存器的模式或模块组合，通过向设计中的模块插入流水线寄存器，可提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能性最大的关键路径，请使用 *Critical Path Estimation*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制和注意事项**

该模块具有以下限制：

- HDL 代码生成不支持帧输入。对于基于帧的输入，请使用 Biquad Filter (DSP HDL Toolbox) 模块。
- 必须将 **Initial conditions** 设置为 `0`。HDL 代码生成不支持非零初始状态。
- 必须选中 **Optimize unity scale values**。

要将 Biquad Filter 模块配置为可编程滤波器或多通道滤波器，请使用以下模块设置：

| 滤波器情况 | 注意事项 |
| --- | --- |
| **可编程滤波器** | HDL Coder 支持 Biquad Filter 模块的可编程滤波器。 1. 在滤波器模块封装上，将 **Coefficient source** 设置为 **Input port(s)**。 2. 将向量信号连接到 **Num** 和 **Den** 系数端口。滤波器中每个二阶节必须使用一个 Biquad Filter 模块。对于具有 *M* 个二阶节的滤波器，请使用一系列 *M* 个 Biquad Filter 模块，每个模块的输入 **Num** 为 3×1 向量，输入 **Den** 为 2×1 向量。 |
| **多通道滤波器** | HDL Coder 支持将向量输入用于 Biquad Filter 模块。 1. 将向量信号连接到 Biquad Filter 模块输入端口。 2. 将 **Input processing** 指定为 `Elements as channels (sample based)`。 3. 要通过在通道之间共享滤波器内核来减少面积，请将模块的 **StreamingFactor** 参数设置为通道数。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2008b 中引入**

## 描述

对双二阶 IIR (SOS) 滤波器建模

Biquad Filter 模块使用指定的双二阶无限脉冲响应 (IIR) 滤波器独立地对输入信号的每个通道进行滤波。当您在对话框中指定滤波器系数时，模块实现具有固定系数的静态滤波器。当您通过输入端口提供滤波器系数时，可以在仿真期间调整系数。

Biquad Filter 模块支持 Simulink® 状态记录功能。有关详细信息，请参阅 State (Simulink)。

**注意**

Biquad Filter 和 Second-Order Section Filter 模块都在 Simulink 中实现二阶节滤波器的级联。但是，它们在滤波器可调性和定点信号支持等方面存在一些差异。

如果输入信号为 `single` 或 `double` 数据类型，请使用 Second-Order Section Filter 模块，因为它比 Biquad Filter 模块具有多项优势。如果输入信号为内置整数或定点运算，请使用 Biquad Filter 模块。您可以为定点算术运算自定义 Biquad Filter 模块。

有关这两个模块之间关键差异的详细信息，请参阅 Difference Between Biquad Filter and Second-Order Section Filter Blocks。
