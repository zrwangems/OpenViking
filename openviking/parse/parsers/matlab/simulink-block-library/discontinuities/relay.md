---
type: simulink-block
title: 'Relay'
family: discontinuities
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'relay'
---

# Relay

Switch output between two constants

## 中文

在两个常量输出之间进行切换

### 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

### 描述

Relay 模块的输出在两个指定值之间切换。打开中继时，它会一直保持打开，直到输入低于**关闭点**参数的值为止。关闭中继时，它会一直保持关闭，直到输入高于**开启点**参数的值为止。此模块接受一个输入并生成一个输出。

**注意**

如果初始输入*介于* **开启点**与**关闭点**值之间，则初始输出是中继关闭时的值。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量

输入信号，用于打开或关闭中继。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量

输出信号在由参数**打开时的输出**和**关闭时的输出**确定的两个值之间切换。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### **开启点** — 用于打开中继的输入值 `'eps'` (默认) | 标量

当输入超过此阈值时，中继打开。**开启点**值必须大于或等于**关闭点**。指定的**开启点**值大于**关闭点**可构建磁滞模型，指定两个值相等则可构建以该值为阈值的开关模型。

**开启点**参数会通过舍入到最邻近整数和饱和处理方法自动转换为输入数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OnSwitchValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'eps'` |

#### **关闭点** — 用于关闭中继的输入值 `'eps'` (默认) | 标量

当输入超过此阈值时，中继关闭。**关闭点**的值必须小于或等于**开启点**。**关闭点**参数会通过舍入到最邻近整数和饱和处理自动转换为输入数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OffSwitchValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'eps'` |

#### **打开时的输出** — 当中继打开时的输出值 `1` (默认) | 标量

当中继打开时的输出值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OnOutputValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **关闭时的输出** — 当中继关闭时的输出值 `0` (默认) | 标量

当中继关闭时的输出值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OffOutputValue` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **输入处理** — 指定基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理：

- **列作为通道(基于帧)** - 将输入信号的每一列视为一个单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。
- **元素作为通道(基于采样)** - 将输入信号的每个元素视为一个单独的通道（基于采样的处理）。

可以使用**输入处理**指定模块是执行基于采样的处理还是基于帧的处理。有关这两种处理模式的详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

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

#### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出数据类型** — 输出信号的数据类型 **继承: 所有端口都具有相同数据类型** (默认) | **继承: 通过反向传播继承** | **double** | **single** | **int8** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>** | ...

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 通过反向传播继承**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

点击**显示数据类型助手**按钮  可以显示**数据类型助手**，这有助于您设置**输出数据类型**参数。

有关详细信息，请参阅 控制信号的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: All ports same datatype'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `'Enum: <class name>'` | `'<data type expression>'` |
| **默认值**：`'Inherit: All ports same datatype'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您对此模块指定的数据类型。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**限制**

该模块不支持使用浮点数据类型进行 HDL 代码生成。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Description

The output for the Relay block switches between two specified values. When the relay is on,
it remains on until the input drops below the value of the **Switch off
point** parameter. When the relay is off, it remains off until the input
exceeds the value of the **Switch on point** parameter. The block
accepts one input and generates one output.

**Note**

When the initial input falls *between* the **Switch off point** and **Switch on point** values, the initial output is the value when the relay is off.

## Ports

### Input

### **Port\_1** — Input signal scalar

The input signal that switches the relay on or off.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar

The output signal switches between two values determined by the
parameters **Output when on** and **Output when
off**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Switch on point** — Input value which switches the relay on `'eps'` (default) | scalar

When the input crosses this threshold, the relay switches on. The
**Switch on point** value must be greater than or equal
to the **Switch off point**. Specifying a **Switch
on point** value greater than the **Switch off
point** models hysteresis, whereas specifying equal values
models a switch with a threshold at that value.

The **Switch on point** parameter is converted to the input data type
offline using round-to-nearest and saturation methods.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OnSwitchValue` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'eps'` |

### **Switch off point** — Input value which switches the relay off `'eps'` (default) | scalar

When the input crosses this threshold the relay switches off. The value of
**Switch off point** must be less than or equal to
**Switch on point**. The **Switch off
point** parameter is converted to the input data type offline
using round-to-nearest and saturation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OffSwitchValue` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'eps'` |

### **Output when on** — Output value when the relay is on `1` (default) | scalar

The output value when the relay is on.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OnOutputValue` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1'` |

### **Output when off** — Output value when the relay is off `0` (default) | scalar

The output value when the relay is off.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OffOutputValue` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

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

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Data type of output signal `Inherit: All ports same datatype` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via back
  propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Output data
type** parameter.

See Control Data Types of Signals for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: All ports same datatype'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `'Enum: <class name>'` | `'<data type expression>'` |
| **Default**: `'Inherit: All ports same datatype'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Limitations**

The block does not support floating-point data types for HDL code
generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
