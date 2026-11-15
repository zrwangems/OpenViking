---
type: simulink-block
title: 'Display'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'display'
---

# Display

Show value of input

## 中文

显示输入的值

### 所属库

Simulink / Sinks HDL Coder / Sinks

### 描述

Display 模块显示输入数据的值。您可以指定显示的频率。对于数值输入数据，您还可以指定显示的格式。

如果模块输入是数组，则您可以纵向或横向调整模块大小以显示更多元素，而不是只显示第一个元素。如果模块输入是向量，则模块从左到右、从上到下依次添加显示字段。模块会显示尽可能多的值。实心三角形表示模块并未显示所有的输入数组元素。

Display 模块显示向量信号的前 200 个元素，显示矩阵信号的前 20 行和前 10 列。

**注意**

如果您指定的数值显示格式不够大，无法显示值的所有位数，则显示的值可能会损失精度。结果取决于您的计算机硬件和操作系统。

#### 显示缩写词

Display 模块上显示下列缩写词，以帮助您确定值的格式。

| 当您看到... | 显示的值为... |
| --- | --- |
| `(SI)` | 存储的整数值  **注意**  当信号是整数数据类型时，不显示 `(SI)`。 |
| `hex` | 十六进制格式 |
| `bin` | 二进制格式 |
| `oct` | 八进制格式 |

#### 显示字符串

使用字符串时，Display 模块显示：

- 带双引号的字符串。
- 将特殊字符显示为转义序列，例如换行符显示为 `'\n'`。
- 将不可显示的字符显示为转义八进制数，例如 `'\201'`。

如果输入信号是字符串类型，则**数值显示格式**参数的选择不影响字符串的显示。

### 端口

#### 输入

#### **Port\_1** — 输入数据 标量 | 向量

要显示的输入数据。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated`

### 参数

#### **数值显示格式** — 数值输入数据的显示格式 **short** (默认) | **long** | **short\_e** | **long\_e** | **货币格式** | **十六进制(存储整数)** | **二进制(存储整数)** | **十进制(存储整数)** | **八进制(存储整数)**

指定数值数据的显示格式。

| 如果您选择... | 模块显示... |
| --- | --- |
| `short` | 具有固定十进制小数点的 5 位数定标值 |
| `long` | 具有固定十进制小数点的 15 位数定标值 |
| `short_e` | 具有浮动小数点的 5 位数值 |
| `long_e` | 具有浮动小数点的 16 位数值 |
| `bank` | 具有固定美元和美分格式的值（但没有 $ 或逗号） |
| `hex (Stored Integer)` | 以十六进制格式存储的定点输入整数值 |
| `binary (Stored Integer)` | 以二进制格式存储的定点输入整数值 |
| `decimal (Stored Integer)` | 以十进制格式存储的定点输入整数值 |
| `octal (Stored Integer)` | 以八进制格式存储的定点输入整数值 |

如果 Display 模块的数值输入具有 `single`、`double` 或 `half` 数据类型，并且显示格式是存储整数，则输出使用 `long` 格式显示。

如果 Display 模块的数值输入具有枚举数据类型（请参阅Simulink 枚举和定义 Simulink 枚举）：

- 模块将显示枚举值，而非基础整数值。
- 将**数值显示格式**设置为任一 `Stored Integer` 设置将导致错误。

如果输入信号是字符串类型，则**数值显示格式**参数的选择不影响字符串的显示。

##### 编程用法

|  |
| --- |
| **模块参数**：`Format` |
| **类型：**字符向量 |
| **值：**`'short'` | `'long'` | `'short_e'` | `'long_e'` | `'bank'` | `'hex (Stored Integer)'` | `'binary (Stored Integer)'` | `'decimal (Stored Integer)'` | `'octal (Stored Integer)'` |
| **默认值：**`'short'` |

#### **抽取** — 显示速率 `1` (默认) | `integer`

指定显示数据的频率。

显示的数据量和显示数据的时间步取决于**抽取**模块参数和 `SampleTime` 属性。

- **抽取**参数允许您显示间隔为 *n* 的每个样本数据，其中 *n* 是抽取因子。默认抽取因子 `1` 在每个时间步显示数据。

  **注意**

  Display 模块在初始时间更新显示，即使**抽取**值大于一也是如此。
- `SampleTime` 属性（可以使用 `set_param` 来设置）允许您指定显示点的采样间隔。使用时间步间隔不同的变步长求解器时，此属性很有用。默认采样时间 `-1` 导致模块在确定要显示的点时忽略采样间隔。

  **注意**

  如果模块继承采样时间 `Inf`，**抽取**参数将被忽略。

##### 编程用法

|  |
| --- |
| **模块参数**：`Decimation` |
| **类型：**字符向量 |
| **值：**`'1'` | 整数 |
| **默认值：**`'1'` |

#### **浮动显示** — 浮动显示 `off` (默认) | `on`

要将模块用作浮动显示，请选择**浮动显示**。模块输入端口消失，模块显示选定信号线上的信号值。

如果您选择**浮动显示**：

- 关闭模型的信号存储重用。有关详细信息，请参阅 信号存储重用 (Simulink Coder)。
- 不要将多维信号连接到浮动显示。

##### 编程用法

|  |
| --- |
| **模块参数**：`Floating` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

在代码生成中将被忽略。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Description

The Display block shows the value of the input data. You can specify the
frequency of the display. For numeric input data, you can also specify the format of
display.

If the block input is an array, you can resize the block vertically or horizontally to
show more than just the first element. If the block input is a vector, the block
sequentially adds display fields from left to right and top to bottom. The block
displays as many values as possible. A black triangle indicates that the block is not
displaying all input array elements.

The Display block shows the first 200 elements of a vector signal and the
first 20 rows and 10 columns of a matrix signal.

**Note**

If you specify a numeric display format that is not large enough to display all
the digits of a value, the displayed values may lose precision. The result depends
on your computer hardware and operating system.

### Display Abbreviations

The following abbreviations appear on the Display block to help you identify
the format of the value.

| When You See... | The Value That Appears Is... |
| --- | --- |
| `(SI)` | The stored integer value  **Note**  `(SI)` does not appear when the signal is of an integer data type. |
| `hex` | In hexadecimal format |
| `bin` | In binary format |
| `oct` | In octal format |

### Displaying Strings

When working with strings, the Display block displays:

- Strings with double quotes.
- Special characters such as newline are shown as escaped sequences, for
  example `'\n'`.
- Non-displayable characters as escaped octal number, for example
  `'\201'`.

If the incoming signal is of type string, the **Numeric display
format** parameter selection does not affect the display of the
string.

## Ports

### Input

### **Port\_1** — Input data scalar | vector

Input data to display.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Numeric display format** — Format to display numeric input data `short` (default) | `long` | `short_e` | `long_e` | `bank` | `hex (Stored Integer)` | `binary (Stored Integer)` | `decimal (Stored Integer)` | `octal (Stored Integer)`

Specify the format of the numeric data that appears.

| If You Select... | The Block Displays... |
| --- | --- |
| `short` | A 5-digit scaled value with fixed decimal point |
| `long` | A 15-digit scaled value with fixed decimal point |
| `short_e` | A 5-digit value with a floating decimal point |
| `long_e` | A 16-digit value with a floating decimal point |
| `bank` | A value in fixed dollars and cents format (but with no $ or commas) |
| `hex (Stored Integer)` | The stored integer value of a fixed-point input in hexadecimal format |
| `binary (Stored Integer)` | The stored integer value of a fixed-point input in binary format |
| `decimal (Stored Integer)` | The stored integer value of a fixed-point input in decimal format |
| `octal (Stored Integer)` | The stored integer value of a fixed-point input in octal format |

If the numeric input to a Display block has a
`single`, `double`, or
`half` data type, and the display format is a
stored-integer, the output displays using the `long`
format.

If the numeric input to a Display block has an enumerated
data type (see Simulink Enumerations and Define Simulink Enumerations):

- The block displays enumerated values, not the values of underlying
  integers.
- Setting **Numeric display format** to any of the
  `Stored Integer` settings causes an
  error.

If the incoming signal is of type string, the selection of the
**Numeric display format** parameter does not affect
the display of the string.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character vector |
| **Values:** `'short'` | `'long'` | `'short_e'` | `'long_e'` | `'bank'` | `'hex (Stored Integer)'` | `'binary (Stored Integer)'` | `'decimal (Stored Integer)'` | `'octal (Stored Integer)'` |
| **Default:** `'short'` |

### **Decimation** — Display rate `1` (default) | `integer`

Specify how often to display data.

The amount of data that appears and the time steps at which the data
appears depend on the **Decimation** block parameter and
the `SampleTime` property.

- The **Decimation** parameter enables you to
  display data at every *n*th sample, where
  *n* is the decimation factor. The default
  decimation, `1`, displays data at every time
  step.

  **Note**

  The Display block updates its display at the initial time,
  even when the **Decimation** value is greater
  than one.
- The `SampleTime` property, which you can set with
  `set_param`,
  enables you to specify a sampling interval at which to display
  points. This property is useful when you are using a variable-step
  solver where the interval between time steps is not the same. The
  default sample time, `-1`, causes the block to
  ignore the sampling interval when determining the points to display.

  **Note**

  If the block inherits a sample time of
  `Inf`, the
  **Decimation** parameter is
  ignored.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decimation` |
| **Type:** character vector |
| **Values:** `'1'` | integer |
| **Default:** `'1'` |

### **Floating display** — Floating display `off` (default) | `on`

To use the block as a floating display, select **Floating display**.
The block input port disappears and the block displays the value of the
signal on a selected line.

If you select **Floating display**:

- Turn off signal storage reuse for your model. See Signal storage reuse (Simulink Coder) for more information.
- Do not connect a multidimensional signal to a floating display.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Floating` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Ignored for code generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
