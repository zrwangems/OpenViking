---
type: simulink-block
title: 'Magnitude-Angle to Complex'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'magnitudeangletocomplex'
---

# Magnitude-Angle to Complex

Convert magnitude and/or a phase angle signal to complex signal

## 中文

将幅值和/或相位角信号转换为复信号

### 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations

### 描述

#### 支持的运算

Magnitude-Angle to Complex 模块可将幅值和相位角输入转换为复数输出。角度输入必须以弧度为单位。

当有两个模块输入时，模块支持输入维度的以下组合：

- 两个输入具有相同的维度
- 一个输入为标量，另一个为 n 维数组

如果模块输入为数组，则输出是复信号数组。幅值输入向量的元素映射到对应的复数输出元素的幅值。同样，角度输入向量的元素映射到对应的复数输出元素的角度。如果一个输入是标量，它将映射到所有复数输出信号的对应分量（幅值或角度）。

#### 超出范围的输入对 CORDIC 逼近方法的影响

如果使用 CORDIC 逼近方法 [1]，相位角的模块输入有以下限制：

- 对于有符号定点类型，角度输入必须在 [–2π, 2π) 弧度范围内。
- 对于无符号定点类型，角度输入必须在 [0, 2π) 弧度范围内。

下表总结了超出范围的输入的影响：

| 模块用法 | 输入超出范围时的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 发生未定义的行为。 |

当您使用 CORDIC 逼近方法时，请确保 Magnitude-Angle to Complex 模块的输入在规定的范围内。对于生成的代码或加速模式，避免依赖未定义的行为。

### 端口

#### 输入

#### **|u|** — 幅值 标量 | 向量 | 矩阵

幅值，指定为实数值标量、向量或矩阵。

##### 依赖关系

- 要启用此端口，请将**输入**设置为**幅值和角度**。

##### 限制

- 如果一个输入具有浮点数据类型，则另一个输入也必须使用相同的数据类型。例如，两个信号都必须为 `double` 或 `single`。
- 仅当**逼近方法**设置为 **CORDIC** 时才支持定点数据类型。当一个输入具有定点数据类型时，另一个输入也必须具有定点数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **∠u** — 相位角弧度 标量 | 向量 | 矩阵

相位角弧度，指定为实数值标量、向量或矩阵。要计算 CORDIC 逼近，角度输入必须满足以下条件：

- 对于有符号定点类型，弧度必须介于 [–2π, 2π) 之间
- 对于无符号定点类型，弧度必须介于 [0, 2π) 之间

有关详细信息，请参阅超出范围的输入对 CORDIC 逼近方法的影响。

##### 依赖关系

- 要启用此端口，请将**输入**设置为**幅值和角度**。

##### 限制

- 如果一个输入具有浮点数据类型，则另一个输入也必须使用相同的数据类型。例如，两个信号都必须为 `double` 或 `single`。
- 仅当**逼近方法**设置为 **CORDIC** 时才支持定点数据类型。如果一个输入具有定点数据类型，另一个输入也必须具有定点数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **Port\_1** — 幅值或相位角弧度 标量 | 向量 | 矩阵

幅值或相位角弧度，指定为实数值标量、向量或矩阵。

- 将**输入**设置为**幅值**时，请在输入端口上指定幅值，在对话框中指定角度。
- 将**输入**设置为**角度**时，请在输入端口上指定角度，在对话框中指定幅值。

##### 依赖关系

要启用此端口，请将**输入**设置为**幅值**或**角度**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 复信号 标量 | 向量 | 矩阵

复信号，由您指定的幅值和相位角构成。

如果模块输入为数组，则输出是复信号数组。幅值输入向量的元素映射到对应的复数输出元素的幅值。同样，角度输入向量的元素映射到对应的复数输出元素的角度。如果一个输入是标量，它将映射到所有复数输出信号的对应分量（幅值或角度）。

**数据类型:** `single` | `double` | `fixed point`

### 参数

#### **输入** — 输入类型 **幅值** (默认) | **角度** | **幅值和角度**

指定输入的类型：幅值输入、角度输入或者同时输入幅值和角度。

##### 编程用法

|  |
| --- |
| **模块参数**：`Input` |
| **类型：**字符向量 |
| **值：**`'Magnitude' | 'Angle' | 'Magnitude and angle'` |
| **默认值：**`'Magnitude and angle'` |

#### **角度** — 输出的相位角 `0` (默认) | 实数值标量、向量或矩阵

输出信号的常量相位角，以弧度为单位。要计算 CORDIC 逼近，角度输入必须满足以下条件：

- 对于有符号定点类型，弧度必须介于 [–2π, 2π) 之间
- 对于无符号定点类型，弧度必须介于 [0, 2π) 之间

有关详细信息，请参阅超出范围的输入对 CORDIC 逼近方法的影响。

##### 依赖关系

要启用此参数，请将**输入**设置为**幅值**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ConstantPart` |
| **类型：**字符向量 |
| **值：**常量标量 |
| **默认值：**`'0'` |

#### **幅值** — 输出的幅值 `0` (默认) | 实数值标量、向量或矩阵

输出信号的常量幅值，指定为实数值标量、向量或矩阵。

##### 依赖关系

要启用此参数，请将**输入**设置为**角度**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ConstantPart` |
| **类型：**字符向量 |
| **值：**实数值标量、向量或矩阵 |
| **默认值：**`'0'` |

#### **逼近方法** — CORDIC 或无 **无** (默认) | **CORDIC**

指定计算输出的逼近方法类型。

| 逼近方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| **无**（默认值） | 浮点 | 您想使用默认的泰勒级数算法。 |
| **CORDIC** | 浮点和定点 | 您需要快速的近似计算时。 |

使用 CORDIC 逼近时，角度输入需满足以下原则：

- 对于有符号定点类型，角度输入必须在 [–2π, 2π) 弧度范围内。
- 对于无符号定点类型，角度输入必须在 [0, 2π) 弧度范围内。

此模块使用以下数据类型传播规则：

| 幅值输入的数据类型 | 逼近方法 | 复数输出的数据类型 |
| --- | --- | --- |
| 浮点 | **无**或 **CORDIC** | 与输入相同 |
| 有符号、定点 | **CORDIC** | `fixdt`(1, *`WL`* +2, *`FL`*)  其中 *`WL`* 和 *`FL`* 是幅值的字长和小数长度 |
| 无符号、定点 | **CORDIC** | `fixdt`(1, *`WL`* +3, *`FL`*)  其中 *`WL`* 和 *`FL`* 是幅值的字长和小数长度 |

##### 编程用法

|  |
| --- |
| **模块参数**：`ApproximationMethod` |
| **类型：**字符向量 |
| **值：**`'None' | 'CORDIC'` |
| **默认值：**`'None'` |

#### **迭代次数** — CORDIC 算法的迭代次数 `11` (默认) | 正整数，小于或等于定点输入的字长

要执行 CORDIC 算法的迭代次数。可能值的范围取决于输入的数据类型：

| 模块输入的数据类型 | 您可以指定的值 |
| --- | --- |
| 浮点 | 正整数 |
| 定点 | 不超过幅值输入字长或相位角输入字长（二者中取较小值）的正整数 |

##### 依赖关系

要启用此参数，请将**逼近方法**设置为 **CORDIC**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfIterations` |
| **类型：**字符向量 |
| **值：**正整数，小于等于定点输入的字长 |
| **默认值：**`'11'` |

#### **按增益因子的倒数缩放输出** — 缩放复数输出的实部和虚部 `on` (默认) | `off`

选中此复选框，以便按缩放因子 `(1/CORDIC gain)` 缩放复数输出的实部和虚部。此值取决于您指定的迭代次数。随着迭代次数的增加，值将接近于 1.647。

此复选框默认处于选中状态，从而使得复数输出 `X + iY` 得到数值意义上更为精确的结果。但是，缩放输出增加了两个额外的乘法运算，一个针对 `X`，另一个针对 `Y`。

##### 依赖关系

要启用此参数，请将**逼近方法**设置为 **CORDIC**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ScaleReciprocalGainFactor` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有多周期实现，这会在生成的代码中引入额外的延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅Generated Model and Validation Model (HDL Coder)。

**HDL 模块属性**

**通用**

| HDL 属性 | 描述 |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 对于定点和浮点类型，指定是将设计中的模块映射到 `MAX`、`Min`、`CUSTOM` 还是 `ZERO` 延迟。默认值为 **MAX**。另请参阅LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅LatencyStrategy (HDL Coder)。 |

**原生浮点**

| HDL 属性 | 描述 |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **InputRangeReduction** | 指定输入范围是有界还是无界。如果您的输入范围是无界的，请为 HDL Coder 启用此属性，以插入额外的逻辑来缩小 `[-pi, pi]` 的输入范围。默认值为 **on**。另请参阅InputRangeReduction (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同设置，您可以控制目标 FPGA 设备上 DSP 的使用。默认值为 **inherit**。另请参阅MantissaMultiplyStrategy (HDL Coder)。 |

**定点支持**

您可以使用定点数据类型作为输入，为 Magnitude-Angle to Complex 模块生成代码。要为模块生成具有定点数据类型的代码，请将**输入**设置为**幅值和角度**，并将**逼近方法**设置为 **CORDIC**。使用 CORDIC 逼近方法时，模块会增加额外的延迟周期，如下表所示。

| 架构 | 参数 | 额外的延迟周期 |
| --- | --- | --- |
| **Pol2CartCordic** | **迭代次数**  **按增益因子的倒数缩放输出** | 当**按增益因子的倒数缩放输出**参数为 **off** 时，  *最大延迟* = **迭代次数** + 1。  当**按增益因子的倒数缩放输出**参数为 **on** 时，  *最大延迟* = **迭代次数** + 6。 |

**限制**

当您将**输入**设置为**幅值**或**角度**时，不支持定点数据类型。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

将**逼近方法**设置为 **CORDIC** 时，Magnitude-Angle to Complex 模块支持定点和基整数数据类型。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024a: 生成具有定点数据类型的 HDL 代码

从 R2024a 开始，您可以为使用定点数据类型作为输入的 Magnitude-Angle to Complex 模块生成 HDL 代码。要生成具有定点数据类型的代码，请将**输入**模块参数设置为**幅值和角度**，并将**逼近方法**参数设置为 **CORDIC**。使用 CORDIC 逼近方法时，您还可以启用**按增益因子的倒数缩放输出**以按增益因子缩放复数输出的实部和虚部。

## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations

## Description

### Supported Operations

The Magnitude-Angle to Complex block converts magnitude and phase angle
inputs to a complex output. The angle input must be in rad.

When there are two block inputs, the block supports these combinations of input
dimensions:

- Two inputs of equal dimensions
- One scalar input and the other an n-dimensional array

If the block input is an array, the output is an array of complex signals. The elements of a magnitude input vector map to the magnitudes of the corresponding complex output elements. Similarly, the elements of an angle input vector map to the angles of the corresponding complex output elements. If one input is a scalar, it maps to the corresponding component (magnitude or angle) of all the complex output signals.

### Effect of Out-of-Range Input on CORDIC Approximations

If you use the CORDIC approximation method [1],
the block input for phase angle has these restrictions:

- For signed fixed-point types, the input angle must fall within the range
  [–2π, 2π) rad.
- For unsigned fixed-point types, the input angle must fall within the range
  [0, 2π) rad.

This table summarizes the effects of an out-of-range input:

| Block Usage | Effect of Out-of-Range Input |
| --- | --- |
| Simulation modes | An error appears. |
| Generated code | Undefined behavior occurs. |

When you use the CORDIC approximation, ensure that you use an in-range input for the
Magnitude-Angle to Complex block. Avoid relying on undefined
behavior for generated code or accelerator modes.

## Ports

### Input

### **|u|** — Magnitude scalar | vector | matrix

Magnitude, specified as a real-valued scalar, vector, or matrix.

#### Dependencies

- To enable this port, set **Input** to
  `Magnitude and angle`.

#### Limitations

- If one input has a floating-point data type, the other
  input must use the same data type. For example, both signals
  must be `double` or
  `single`.
- Fixed-point data types are supported only when you set the
  **Approximation method** to
  `CORDIC`. When one input has a
  fixed-point data type, the other input must also have a
  fixed-point data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **∠u** — Radian phase angle scalar | vector | matrix

Radian phase angle, specified as a real-valued scalar, vector, or
matrix. To compute the CORDIC approximation, the input angle must be
between:

- [–2π, 2π) rad, for signed fixed-point types
- [0, 2π) rad, for unsigned fixed-point types

For more information, see Effect of Out-of-Range Input on CORDIC Approximations.

#### Dependencies

- To enable this port, set **Input** to
  `Magnitude and angle`.

#### Limitations

- If one input has a floating-point data type, the other
  input must use the same data type. For example, both signals
  must be `double` or
  `single`.
- Fixed-point data types are supported only when you set the
  **Approximation method** to
  `CORDIC`. If one input has a
  fixed-point data type, the other input must also have a
  fixed-point data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1** — Magnitude or radian phase angle scalar | vector | matrix

Magnitude, or radian phase angle, specified as a real-valued scalar,
vector, or matrix.

- When you set **Input** to
  `Magnitude`, you specify the
  magnitude at the input port, and the angle on the dialog
  box.
- When you set **Input** to
  `Angle`, you specify the angle at
  the input port, and the magnitude on the dialog box.

#### Dependencies

To enable this port, set **Input** to
`Magnitude` or
`Angle`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Complex signal scalar | vector | matrix

Complex signal, formed from the magnitude and phase angle you
specify.

If the block input is an array, the output is an array of complex
signals. The elements of a magnitude input vector map to the magnitudes
of the corresponding complex output elements. Similarly, the elements of
an angle input vector map to the angles of the corresponding complex
output elements. If one input is a scalar, it maps to the corresponding
component (magnitude or angle) of all the complex output signals.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Input** — Type of input `Magnitude` (default) | `Angle` | `Magnitude and angle`

Specify the kind of input: a magnitude input, an angle input, or
both.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Input` |
| **Type:** character vector |
| **Values:** `'Magnitude' | 'Angle' | 'Magnitude and angle'` |
| **Default:** `'Magnitude and angle'` |

### **Angle** — Phase angle of output `0` (default) | real-valued scalar, vector, or matrix

Constant phase angle of the output signal, in rad. To compute the CORDIC approximation,
the input angle must be between:

- [–2π, 2π) rad, for signed fixed-point types
- [0, 2π) rad, for unsigned fixed-point types

For more information, see Effect of Out-of-Range Input on CORDIC Approximations.

#### Dependencies

To enable this parameter, set **Input** to
`Magnitude`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:** constant scalar |
| **Default:** `'0'` |

### **Magnitude** — Magnitude of output `0` (default) | real-valued scalar, vector, or matrix

Constant magnitude of the output signal, specified as a real-valued
scalar, vector, or matrix.

#### Dependencies

To enable this parameter, set **Input** to
`Angle`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConstantPart` |
| **Type:** character vector |
| **Values:**real-valued scalar, vector, or matrix |
| **Default:** `'0'` |

### **Approximation method** — CORDIC or none `None` (default) | `CORDIC`

Specify the type of approximation for computing output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating point | You want to use the default Taylor series algorithm. |
| `CORDIC` | Floating point and fixed point | You want a fast, approximate calculation. |

When you use the CORDIC approximation, follow these guidelines for the input angle:

- For signed fixed-point types, the input angle must fall within the range [–2π, 2π) rad.
- For unsigned fixed-point types, the input angle must fall within the range [0, 2π) rad.

The block uses the following data type propagation rules:

| Data Type of Magnitude Input | Approximation Method | Data Type of Complex Output |
| --- | --- | --- |
| Floating point | `None` or `CORDIC` | Same as input |
| Signed, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*)  where *`WL`* and *`FL`* are the word length and fraction length of the magnitude |
| Unsigned, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*)  where *`WL`* and *`FL`* are the word length and fraction length of the magnitude |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'None' | 'CORDIC'` |
| **Default:** `'None'` |

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | positive integer, less than or equal to word length of fixed-point input

Number of iterations to perform the CORDIC algorithm. The range of
possible values depends on the data type of the input:

| Data Type of Block Inputs | Value You Can Specify |
| --- | --- |
| Floating point | A positive integer |
| Fixed point | A positive integer that does not exceed the word length of the magnitude input or the word length of the phase angle input, whichever value is smaller |

#### Dependencies

To enable this parameter, set **Approximation
method** to `CORDIC`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfIterations` |
| **Type:** character vector |
| **Values:** positive integer, less than or equal to word length of fixed-point input |
| **Default:** `'11'` |

### **Scale output by reciprocal of gain factor** — Scale real and imaginary parts of complex output `on` (default) | `off`

Select this check box to scale the real and imaginary parts of the complex
output by a factor of `(1/CORDIC gain)`. This value depends
on the number of iterations you specify. As the number of iterations goes
up, the value approaches 1.647.

This check box is selected by default, which leads to a more numerically
accurate result for the complex output, `X + iY`. However,
scaling the output adds two extra multiplication operations, one for
`X` and one for `Y`.

#### Dependencies

To enable this parameter, set **Approximation
method** to `CORDIC`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleReciprocalGainFactor` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

**HDL Block Properties**

**General**

| HDL Property | Description |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `MAX`, `Min`, `CUSTOM`, or `ZERO` latency for fixed-point and floating-point types. The default is `MAX`. See also LatencyStrategy (HDL Coder). |
| **CustomLatency** | When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |

**Native Floating Point**

| HDL Property | Description |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **InputRangeReduction** | Specify whether your input range is bounded or unbounded. If your input range is unbounded, enable this property for HDL Coder to insert additional logic to reduce the range of inputs to `[-pi, pi]`. The default is `on`. See also InputRangeReduction (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Fixed-Point Support**

You can generate code for Magnitude-Angle to Complex block with fixed-point
data types as input. To generate the code with fixed-point data types for the
block, set **Input** to `Magnitude and
angle` and the **Approximation method** to
`CORDIC`. When using the CORDIC approximation
method, the block adds additional cycles of latency as given in table
below.

| Architecture | Parameter | Additional cycles of latency |
| --- | --- | --- |
| `Pol2CartCordic` | **Number of iterations**  **Scale output by reciprocal of gain factor** | When **Scale output by reciprocal of gain factor** parameter is `off`,  *Max Latency* = **Number of iterations** + 1.  When **Scale output by reciprocal of gain factor** parameter is `on`,  *Max Latency* = **Number of iterations** + 6. |

**Restrictions**

Fixed-point data types are not supported when you set
**Input** to `Magnitude` or
`Angle`.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

The Magnitude-Angle to Complex block supports fixed-point and base integer data
types when you set **Approximation method** to
`CORDIC`.

## Version History

**Introduced before R2006a**

### R2024a: Generate HDL code with fixed-point data types

Starting in R2024a, you can generate HDL code for Magnitude-Angle to Complex block
that uses fixed-point data types as inputs. To generate code with fixed-point data
types, set the **Input** block parameter to `Magnitude
and angle` and the **Approximation method**
parameter to `CORDIC`. When using the CORDIC approximation
method, you can also enable **Scale output by reciprocal of gain
factor** to scale the real and imaginary parts of the complex output by
a gain factor.
