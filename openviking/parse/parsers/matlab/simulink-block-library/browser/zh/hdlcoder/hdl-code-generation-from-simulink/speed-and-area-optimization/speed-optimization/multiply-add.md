---
type: simulink-block
title: 'Multiply-Add'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Speed and Area Optimization / Speed Optimization'
documentation_page: 'multiplyadd'
documentation_source_path: 'ref/multiplyadd.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiply-Add

## 端口

### 输入

### **a** — 输入信号 `scalar` | `vector` | `matrix`

要与端口
`b` 的输入相乘的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **b** — 输入信号 `scalar` | `vector` | `matrix`

要与端口
`a` 的输入相乘的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **c** — 输入信号 `scalar` | `vector` | `matrix`

根据 **函数** 设置，与
`a` 和 `b` 的乘积相加或相减的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Port\_1** — 输出信号 `scalar` | `vector` | `matrix`

乘加运算的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### **函数** — 指定函数 `c+(a.*b)` (默认) | `c-(a.*b)` | `(a.*b)-c`

指定要执行组合乘法加法还是乘法减法操作的函数。

#### 程序化使用

|  |
| --- |
| **参数:**`Function` |
| **类型:**  string scalar | character vector |
| **值:**`"c+(a.*b)"` | `"c-(a.*b)"` |`"(a.*b)-c"` |
| **默认:**  `'c+(a.*b)'` |

### **输出数据类型** — 指定输出数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出数据类型。此参数设置加法运算的输出数据类型。您可以将输出数据类型设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **显示数据类型助手** 按钮
以显示数据类型助手对话框，该对话框可帮助您设置 **输出数据类型** 参数。

有关详细信息，请参阅 控制信号的数据类型。

### **整数舍入模式** — 指定定点运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式为以下之一：

`Ceiling`
:   将正数和负数朝正无穷方向舍入。等效于 MATLAB
    `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现结值，则舍入到最接近的偶数整数。等效于
    Fixed-Point Designer™
    `convergent` 函数。

`Floor`
:   将正数和负数朝负无穷方向舍入。等效于 MATLAB
    `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现结值，则朝正无穷方向舍入。等效于
    Fixed-Point Designer
    `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现结值，则正数朝正无穷方向舍入，
    负数朝负无穷方向舍入。等效于
    Fixed-Point Designer
    `round` 函数。

`Simplest`
:   在朝负无穷方向舍入和朝零方向舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字朝零方向舍入。等效于 MATLAB
    `fix` 函数。

#### 程序化使用

|  |
| --- |
| **参数:**`RndMeth` |
| **类型:**  string scalar | character vector |
| **值:**`"Ceiling"` | `"Convergent"` |`"Floor"` | `"Nearest"` | `"Round"` | `"Simplest"` | `"Zero"` |
| **默认:**  `'Floor'` |

#### 另请参阅

有关详细信息，请参阅 舍入模式。

### **对整数溢出饱和** — 指定溢出是否饱和 **Off** (默认) | **On**

On
:   溢出饱和到该数据类型可以表示的最小值或最大值。

    例如，与有符号 8 位整数关联的溢出可以饱和到 -128 或 127。

Off
:   溢出回绕到该数据类型可以表示的适当值。

    例如，数字 130 不适合有符号 8 位整数，并回绕到 -126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护时，请考虑选中此复选框。
- 当您希望优化生成代码的效率时，请考虑清除此复选框。

  清除此复选框还有助于避免过度指定模块处理越界信号的方式。有关详细信息，请参阅 排查信号范围错误。
- 选中此复选框时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **参数:**`SaturateOnIntegerOverflow` |
| **类型:**  string scalar | character vector |
| **值:**  `"off"` | `"on"` |
| **默认:**  `'off'` |

## 所属库

HDL Coder / HDL Operations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **PipelineDepth** | 流水线级数。默认值为 `auto`，这意味着代码生成器根据您的综合工具确定流水线级数。要插入自适应流水线，当 **PipelineDepth** 设置为 `auto` 时，您必须指定综合工具并输入大于零的目标频率值。  您可以输入 0 到 3 之间的整数。对于 Altera® 硬件目标，最大流水线深度为 2。 |

| 常规 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于最小浮点数的数，该浮点数可在尾数没有前导零的情况下表示。默认值为 `inherit`。另请参阅 HandleDenormals。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 器件上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

- 当模块具有浮点输入时，HDL Coder 会忽略 **PipelineDepth** 参数，并且不插入流水线寄存器。
- 如果模块位于反馈环路中，并且模块输出处没有足够的延迟，代码生成器会降低 **PipelineDepth** 以防止延迟平衡失败。对于足够的延迟，请在 Multiply-Add 模块的输出处添加 Delay 模块。
- 要将组合乘加运算映射到 DSP 单元，对于 Altera，第三输入 *c* 的宽度必须小于 64 位；对于 Xilinx®，必须小于 48 位。
- **函数** 设置 `(a.*b)-c` 中的减法运算不会映射到 Altera FPGA 库中的 DSP 单元。

## 版本历史

**在 R2015b 中引入**

## 描述

乘加组合运算

Multiply-Add 模块计算前两个输入 a 和 b 的乘积，并将结果与第三个输入 c 相加。输入可以是向量或标量。

无论输出类型如何，乘法运算均为全精度。**整数舍入模式**、**输出数据类型** 和 **对整数溢出饱和** 设置仅适用于加法运算。加法运算默认使用累加器数据类型设置 `Inherit : Inherit via internal rule`。

使用 Multiply-Add 模块将组合乘加或乘法减法运算映射到目标硬件中的 DSP 单元。您可以在 Multiply-Add 模块的“模块参数”对话框中选择 **函数** 设置。

要映射到 DSP 单元，请为您的模型指定 `SynthesisTool` 属性。当您为模型生成 HDL 代码时，HDL Coder™ 会配置乘加运算，以便您的综合工具可以映射到 DSP 单元。

**注意**

某些 DSP 单元不具备乘加能力。要查看您的硬件是否具备乘加能力，请参阅硬件文档。
