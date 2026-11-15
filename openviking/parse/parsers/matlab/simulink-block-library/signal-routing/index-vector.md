---
type: simulink-block
title: 'Index Vector'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'indexvector'
---

# Index Vector

Switch output between different inputs based on value of first input

## 中文

基于第一个输入的值在不同输入之间切换输出

### 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

### 描述

Index Vector 模块是特殊配置的 Multiport Switch 模块，需要指定一个数据输入，控制输入从 0 开始。模块输出是其索引与控制输入匹配的输入向量的元素。例如，如果输入向量为 `[18 15 17 10]`，控制输入为 `3`，则与索引 3（从 0 开始）匹配的元素为 10，它将成为输出值。

Index Vector 和 Multiport Switch 模块是同一模块的替代配置。

- Index Vector - 基于第一个输入的值在不同输入之间切换输出。
- Multiport Switch - 基于控制信号选择输出信号。

要将 Multiport Switch 模块配置为 Index Vector 模块，请将**数据端口数量**设置为 **1** 且**数据端口顺序**设置为**从 0 开始连续**。

### 端口

#### 输入

#### **Port\_1** — 控制信号 标量

控制信号，指定为标量。当控制输入不是整数值时，模块通过向零舍入将值截断为整数。

有关枚举类型的控制信号的信息，请参阅 Multiport Switch 模块参考页上的枚举控制端口的参数设置原则。

##### 限制

- 如果控制信号为数值，则控制信号不能为复数。
- 如果控制信号为枚举信号，模块将使用基础整数值来选择数据端口。
- 如果基础整数没有对应的数据输入，将出现错误。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **0 or 1** — 第一个数据输入 标量 | 向量

第一个数据输入，指定为标量或向量。当**数据端口顺序**设置为**从 0 开始连续**时，端口标签为 **0**；当**数据端口顺序**设置为**从 1 开始连续**时，端口标签为 **1**。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus` | `enumerated` | `string`
#### 输出

#### **Port\_1** — 所选数据输入，基于控制信号值 标量

模块根据控制信号值从输入数据向量中输出所选值。输出是标量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### 常设

#### **数据端口顺序** — 数据输入端口的排序类型 **从 0 开始连续** (默认) | **从 1 开始连续** | **指定索引**

指定数据输入端口的排序类型。

- **从 0 开始连续** - 模块使用从 0 开始的索引方式为连续数据端口排序。这是 Index Vector 模块的默认值。
- **从 1 开始连续** - 模块使用从 1 开始的索引方式为连续数据端口排序。这是 Multiport Switch 模块的默认值。
- **指定索引** - 模块使用不连续的索引方式为数据端口排序。只有具有两个或更多输入数据端口的配置才支持此值。

##### 提示

- 当控制端口为枚举类型时，请选择**指定索引**。
- 如果选择**从 0 开始连续**或**从 1 开始连续**，请确认控制端口不是枚举类型。此配置已弃用，如果使用将会生成错误。您可以在模型上运行升级顾问，将此配置中的每个 Multiport Switch 模块替换为显式指定数据端口索引的模块。请参阅模型升级。
- 在仿真或代码生成中，应避免出现模块包含未使用的数据端口的情况。当控制端口为定点或内置数据类型时，请确认所有数据端口索引都可用该类型表示。否则，将发生以下模块行为：

  | 如果模块具有未使用的数据端口且数据端口顺序为： | 该模块产生： |
  | --- | --- |
  | **从 0 开始连续**或**从 1 开始连续** | 警告 |
  | **指定索引** | 错误 |

##### 依赖关系

选择**从 0 开始连续**或**从 1 开始连续**将启用**数据端口数量**参数。

选择**指定索引**将启用**数据端口索引**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataPortOrder` |
| **类型：**字符向量 |
| **值：**`'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **默认值：**`'Zero-based contiguous'` |

#### **数据端口数量** — 数据输入端口的个数 `1` (默认) | 在 1 和 65536 之间的整数

指定模块的数据输入端口数。

##### 依赖关系

要启用此参数，请将**数据端口顺序**设置为**从 0 开始连续**或**从 1 开始连续**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**1 和 65536 之间的整数 |
| **默认值：**`'1'` |

#### 信号属性

#### **要求所有数据端口输入具有相同的数据类型** — 要求所有输入具有相同的数据类型 `off` (默认) | `on`

选中此复选框将要求所有数据输入端口具有相同的数据类型。清除此复选框时，模块允许数据端口输入具有不同数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

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

#### **输出数据类型** — 指定输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **继承: 与第一个数据输入相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **字符串** | **Simulink.ImageType(480,640,3)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - Simulink® 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。如果更改了嵌入式目标的设置，则依内部规则选择的数据类型可能会发生变化。有时软件不能同时满足优化代码效率和保证数值准确性这两个需求。如果内部规则不能满足您对数值准确性或性能的特定需求，请使用下列选项之一：

  - 显式指定输出数据类型。
  - 显式指定默认数据类型（例如 `fixdt(1,32,16)`），然后使用定点工具为您的模型提供数据类型建议。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用**继承: 通过反向传播继承**，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例说明，请参阅 Signal Attributes 模块库中的 Data Type Propagation Examples 模块。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。
- **继承: 与第一个数据输入相同** - 使用第一个数据输入端口的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选中此选项将锁定此模块的输出数据类型设置，从而防止通过定点工具和定点顾问进行更改。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **整数舍入模式** — 指定定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

选择下列舍入模式之一。

**向上**
:   将正值和负值朝正无穷方向舍入。等同于 MATLAB® `ceil` 函数。

**收敛**
:   将数值舍入到最邻近的可表示值。如果出现结值，则舍入到最邻近的偶数整数。等同于 Fixed-Point Designer™ `convergent` 函数。

**向下**
:   将正值和负值朝负无穷方向舍入。等同于 MATLAB `floor` 函数。

**最邻近值**
:   将数值舍入到最邻近的可表示值。如果出现结值，则朝正无穷方向舍入。等同于 Fixed-Point Designer `nearest` 函数。

**舍入**
:   将数值舍入到最邻近的可表示值。如果出现结值，则将正数朝正无穷方向舍入，将负数朝负无穷方向舍入。等同于 Fixed-Point Designer `round` 函数。

**最简**
:   自动选择是向负无穷大方向舍入还是向零舍入，以生成尽可能有效的舍入代码。

**零**
:   将数值向零舍入。等同于 MATLAB `fix` 函数。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

##### 另请参阅

有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

#### **允许不同数据输入大小(产生可变大小的输出信号)** — 允许不同大小的输入信号 `off` (默认) | `on`

选中此复选框将允许输入信号具有不同大小。

- `On` - 允许输入信号具有不同大小，并将输入信号的大小传播给输出信号。在此模式下，模块产生可变大小的输出信号。
- `Off` - 要求所有非标量数据输入信号的大小相同。

##### 编程用法

|  |
| --- |
| **参数：**`AllowDiffInputSizes` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

Index Vector 模块是一个 Multiport Switch 模块，其**数据端口数量**设置为 1。有关 HDL 代码生成的信息，请参阅 Multiport Switch。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The Index Vector block is a special configuration of the Multiport Switch block in which you specify one data input and the control
input is zero-based. The block output is the element of the input vector whose index
matches the control input. For example, if the input vector is `[18 15 17
10]` and the control input is `3`, the element that
matches the index of 3 (zero-based) is 10, and that becomes the output value.

The Index Vector and Multiport Switch blocks are alternative configurations of the same
block.

- Index Vector — Switch output between different inputs based on value of first
  input.
- Multiport Switch — Select output signal based on control
  signal.

To configure a Multiport Switch block to work as an Index
Vector block set **Number of data ports** to
`1` and **Data port order** to
`Zero-based contiguous`.

## Ports

### Input

### **Port\_1** — Control signal scalar

Control signal, specified as a scalar. When the control input is not an integer value,
the block truncates the value to an integer by rounding to zero.

For information on control signals of enumerated type, see Guidelines on Setting Parameters for Enumerated Control Port on the Multiport
Switch block ref page.

#### Limitations

- If the control signal is numeric, the control signal
  cannot be complex.
- If the control signal is an enumerated signal, the block
  uses the value of the underlying integer to select a data
  port.
- If the underlying integer does not correspond to a data
  input, an error occurs.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **0 or 1** — First data input scalar | vector

First data input, specified as a scalar or vector. The port is labeled
**0** when you set **Data port
order** to `Zero-based
contiguous`, and labeled **1** when you
set **Data port order** to `One-based
contiguous`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus` | `enumerated` | `string`
### Output

### **Port\_1** — Selected data input, based on control signal value scalar

The block outputs the selected value from the input data vector, according to the
control signal value. The output is a scalar.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### Main

### **Data port order** — Type of ordering for data input ports `Zero-based contiguous` (default) | `One-based contiguous` | `Specify indices`

Specify the type of ordering for your data input ports.

- `Zero-based contiguous` — Block uses
  zero-based indexing for ordering contiguous data ports. This is
  the default value of the Index Vector
  block.
- `One-based contiguous` — Block uses
  one-based indexing for ordering contiguous data ports. This is
  the default value of the Multiport Switch
  block.
- `Specify indices` — Block uses
  noncontiguous indexing for ordering data ports. This value is
  supported only for configurations with two or more input data
  ports.

#### Tips

- When the control port is of enumerated type, select
  `Specify indices`.
- If you select `Zero-based
  contiguous` or `One-based
  contiguous`, verify that the control port
  is not of enumerated type. This configuration is deprecated
  and produces an error. You can run the Upgrade Advisor on
  your model to replace each Multiport Switch
  block of this configuration with a block that explicitly
  specifies data port indices. See Model Upgrades.
- Avoid situations where the block contains unused data
  ports for simulation or code generation. When the control
  port is of fixed-point or built-in data type, verify that
  all data port indices are representable with that type.
  Otherwise, the following block behavior occurs:

  | If the block has unused data ports and data port order is: | The block produces: |
  | --- | --- |
  | `Zero-based contiguous` or `One-based contiguous` | A warning |
  | `Specify indices` | An error |

#### Dependencies

Selecting `Zero-based contiguous` or
`One-based contiguous` enables the
**Number of data ports** parameter.

Selecting `Specify indices` enables the
**Data port indices** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortOrder` |
| **Type:** character vector |
| **Values:** `'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **Default:** `'Zero-based contiguous'` |

### **Number of data ports** — Number of data input ports `1` (default) | integer between 1 and 65536

Specify the number of data input ports to the block.

#### Dependencies

To enable this parameter, set **Data port order**
to `Zero-based contiguous` or
`One-based contiguous`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** integer between 1 and 65536 |
| **Default:** `'1'` |

### Signal Attributes

### **Require all data port inputs to have the same data type** — Require all inputs to have the same data type `off` (default) | `on`

Select this check box to require that all data input ports have the same data
type. When you clear this check box, the block allows data port inputs to have
different data types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first data input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Simulink.ImageType(480,640,3)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal
  rule`—Simulink® chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware. If you change the embedded
  target settings, the data type selected by the internal rule might
  change. It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the internal rule
  doesn’t meet your specific needs for numerical accuracy or performance,
  use one of the following options:

  - Specify the output data type explicitly.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your model. For more
    information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use this block
    are available in the Signal Attributes library Data Type
    Propagation Examples block.
- `Inherit: Inherit via back propagation` —
  Uses the data type of the driving block.
- `Inherit: Same as first data input` — Uses
  the data type of the first data input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Integer rounding mode** — Specify the rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Choose one of these rounding modes.

`Ceiling`
:   Rounds both positive and negative numbers
    toward positive infinity. Equivalent to the
    MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds to the nearest even
    integer. Equivalent to the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds both positive and negative numbers
    toward negative infinity. Equivalent to the
    MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds toward positive
    infinity. Equivalent to the Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds positive numbers
    toward positive infinity and rounds negative
    numbers toward negative infinity. Equivalent to
    the Fixed-Point Designer
    `round` function.

`Simplest`
:   Automatically chooses between round toward
    floor and round toward zero to generate rounding
    code that is as efficient as possible.

`Zero`
:   Rounds number toward zero. Equivalent to the
    MATLAB
    `fix` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RndMeth` |
| **Type**: character vector |
| **Values**: `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **Default**: `'Floor'` |

#### See Also

For more information, see Rounding Modes (Fixed-Point Designer).

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### **Allow different data input sizes (Results in variable-size output signal)** — Allow input signals with different sizes `off` (default) | `on`

Select this check box to allow input signals with different sizes.

- `On` — Allows input signals with different sizes, and
  propagate the input signal size to the output signal. In this mode, the
  block produces a variable-size output signal.
- `Off` — Requires that all nonscalar data input signals be
  the same size.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowDiffInputSizes` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

The Index Vector block is a Multiport Switch block with **Number of data
ports** set to 1. For HDL code generation information, see Multiport Switch.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
