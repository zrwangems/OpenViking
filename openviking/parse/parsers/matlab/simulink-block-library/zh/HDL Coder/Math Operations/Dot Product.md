---
type: simulink-block
title: 'Dot Product'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'ALG'
documentation_page: 'dotproduct'
documentation_source_path: '../simulink/slref/dotproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# Dot Product

## 端口

### 输入

### **Port\_1** — 第一个操作数输入信号 标量 | 向量

表示点积计算的第一个操作数的信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 第二个操作数输入信号 标量 | 向量

表示点积计算的第二个操作数的信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 点积输出信号 标量 | 向量

由两个输入信号的点积计算得到的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Require all inputs to have the same data type** — 要求所有输入具有相同的数据类型 `on`（默认） | `off`

清除此复选框可使所有输入具有不同的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认） | 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（参见 Specify Signal Ranges and Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `OutMin` |
| **值**：| `'[]'`（默认） | 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认） | 标量

将 Simulink® 检查的输出范围的上限值指定为有限、实数、double 类型的标量值。

**注意**

如果为此模块的数据类型指定总线对象，请不要在模块上设置总线数据的最大值。Simulink 会忽略此设置。而应设置指定为数据类型的总线对象的总线元素的最大值。有关总线元素的 Maximum 参数的信息，请参见 `Simulink.BusElement`。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（参见 Specify Signal Ranges and Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[ ]'` |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。有关详细信息，请参见 Control Data Types of Signals。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule` — Simulink 选择一种数据类型，以在数值精度、性能和生成的代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。如果更改嵌入式目标设置，内部规则所选择的数据类型可能会改变。例如，如果模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 `ASIC/FPGA` 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定 `Unspecified (assume 32-bit Generic)`（即通用 32 位微处理器）作为目标硬件，则输出数据类型为 `int32`。如果目标微处理器提供的字长都无法容纳输出范围，Simulink 软件将在 Diagnostic Viewer 中显示错误。

  软件并不总是能够同时优化代码效率和数值精度。如果内部规则不能满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用 `Inherit: Same as input` 这一简单选择。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型提议数据类型。有关详细信息，请参见 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用 `Inherit: Inherit via back propagation`，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例，请参见 Signal Attributes 库中的 Data Type Propagation Examples 模块。

  **注意**

  当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。
- `Inherit: Same as first input` — 使用第一个输入信号的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此项可锁定此模块的输出数据类型设置，防止 Fixed-Point Tool 和 Fixed-Point Advisor 对其进行更改。有关详细信息，请参见 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参见 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `RndMeth` |
| **值**：| `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认） | `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型所能表示的最小值或最大值。
- `off` — 溢出回绕到数据类型所能表示的相应值。

例如，有符号 8 位整数 `int8` 所能表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出，并且您希望在生成的代码中显式提供饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参见 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认） | `'on'` |

## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Linear`（默认） | 生成用于计算乘积之和的线性加法器链。 |
| `Tree` | 生成用于计算乘积之和的树形加法器结构。 |

**HDL 模块属性**

| General | |
| --- | --- |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟而在输出端放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参见 ConstrainedOutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入额外逻辑来处理设计中的非规格化数。非规格化数是幅值小于尾数中没有前导零时可表示的最小浮点数的数。默认值为 `inherit`。另请参见 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是将设计中的模块映射为 `inherit`、`Max`、`Min` 还是 `Zero` 以用于浮点运算符。默认值为 `inherit`。另请参见 LatencyStrategy (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 器件上的 DSP 使用量。默认值为 `inherit`。另请参见 MantissaMultiplyStrategy (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成两个向量的点积

Dot Product 模块生成输入向量的点积。标量输出 `y` 等于 MATLAB® 运算

```
y = sum(conj(u1) .* u2 )
```

其中 `u1` 和 `u2` 表示输入向量。输入可以是向量、列向量（单列矩阵）或标量。如果两个输入都是向量或列向量，则它们必须具有相同的长度。如果 `u1` 和 `u2` 都是列向量，则模块输出的结果等效于 MATLAB 表达式 `u1'*u2`。

输入向量的元素可以是实值或复值信号。输出的信号类型（复数或实数）取决于输入的信号类型。

| 输入 1 | 输入 2 | 输出 |
| --- | --- | --- |
| real | real | real |
| real | complex | complex |
| complex | real | complex |
| complex | complex | complex |
