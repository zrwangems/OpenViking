---
type: simulink-block
title: 'Waveform Generator'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'waveformgenerator'
---

# Waveform Generator

Output waveforms using signal notations

## 中文

使用信号符号输出波形

### 所属库

Simulink / Sources

### 描述

Waveform Generator 模块根据您在**波形定义**表中输入的信号符号输出波形。

此模块支持下列用于信号符号的语法：

- 函数语法 - 以信号语法的特定顺序指定所有参量（请参阅算法）。
- 名称-值语法 - 指定可选的、以逗号分隔的 `Name,Value` 对组参量。`Name` 为参量名称，`Value` 为对应的值。`Name` 必须显示在单引号 (`' '`) 内。您可采用任意顺序指定多个名称-值对组参量，如 `Name1,Value1,...,NameN,ValueN`。有关详细信息，请参阅算法。

此模块支持普通、快速和快速加速模式以及快速重启。

#### 支持的运算符

| 运算 | 运算符 |
| --- | --- |
| 绝对值 | `abs()` |
| 加法 | `+` |
| 除法 | `/` |
| 乘法 | `*` |
| 括号 | `()` |
| 减法 | `-` |
| 一元减法 | `-` |

Waveform 模块遵循以下运算符优先规则：

1. `( )`
2. `+ -` （一元）
3. `* /`
4. `+ -`

#### 支持的运算

Waveform Generator 模块一次输出一个信号。您可以更改此输出信号。以弧度表示频率和相位偏移量参数。您还可以：

- 嵌套信号符号，例如：

  ```
  sin('Amplitude',sin('Amplitude',1,'Frequency',1,'Phase',0),'Frequency',1,'Phase',1)
  ```
- 在基础工作区或模型工作区中引用实数标量变量，例如：

  ```
  sin('Amplitude',x,'Frequency',y,'Phase',z)
  ```

  *x*、*y* 和 *z* 存在于基础工作区中。

有关波形的详细信息，请参阅算法。

要快速确定系统对不同类型输入的响应，您可以在仿真过程中更改 Waveform Generator 模块的输出信号。

### 端口

#### 输出

#### **Port\_1** — 生成的输出信号 标量 | 向量

由**波形定义**表中的条目指定的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### 参数

#### 常设

#### **输出信号** — 输出信号的波形 1 (默认) | 整数

选择波形定义以指定输出信号。该数字对应于**波形定义**表中的行项。您可以在仿真运行时更改此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`SelectedSignal` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **波形定义** — 波形信号符号 常量 | `gaussian(mean,variance,seed)` | `pulse(amplitude,trigger_time,duration)` | `sawtooth(amplitude,frequence,phase_offset)` | `sin(amplitude,frequence,phase_offset)` | `square(amplitude,frequence,phase_offset)` | `step(step_time,initial_value,final_value)`

在**波形定义**表中输入信号符号，每行一个波形定义。有关语法的详细信息，请参阅算法。

#### 信号属性

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

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

#### **输出数据类型** — 指定输出数据类型 **double** (默认) | **继承: 通过反向传播继承** | **single** | **int8** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>** | ...

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | **fixdt(1,16,2^0,0)** | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **默认值**：`'double'` |

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

#### **采样时间** — 采样时间间隔 `0.1` (默认) | 标量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.1'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2015b 中推出**

## Libraries

Simulink / Sources

## Description

The Waveform Generator block outputs waveforms based on signal
notations that you enter in the **Waveform Definition** table.

This block supports these syntaxes for the signal notations:

- Function syntax — Specify all arguments in the specific order for the
  signal syntax (see Algorithms).
- Name-value syntax — Specify optional comma-separated pairs of
  `Name,Value` arguments. `Name` is the
  argument name and `Value` is the corresponding value.
  `Name` must appear inside single quotes (`'
  '`). You can specify several name and value pair arguments in any
  order as `Name1,Value1,...,NameN,ValueN`. For more information,
  see Algorithms.

This block supports normal, accelerator, and rapid accelerator modes and fast restart.

### Supported Operators

| Operation | Operator |
| --- | --- |
| Absolute value | `abs()` |
| Addition | `+` |
| Division | `/` |
| Multiplication | `*` |
| Parentheses | `()` |
| Subtraction | `-` |
| Unary minus | `-` |

The Waveform block observes the following rules of operator precedence:

1. `( )`
2. `+ -` (unary)
3. `* /`
4. `+ -`

### Supported Operations

The Waveform Generator block outputs one signal at a time. You can change
this output signal. Express frequency and phase offset parameters in radians. You
can also:

- Nest signal notations, for example:

  ```
  sin('Amplitude',sin('Amplitude',1,'Frequency',1,'Phase',0),'Frequency',1,'Phase',1)
  ```
- Reference real scalar variables in the base or model workspace, for
  example:

  ```
  sin('Amplitude',x,'Frequency',y,'Phase',z)
  ```

  *x*, *y*, and *z* exist
  in the base workspace.

For more information on waveforms, see Algorithms.

To quickly determine the response of a system to different types of inputs, you can vary
the output signal of the Waveform Generator block while a simulation
is in progress.

## Ports

### Output

### **Port\_1** — Generated output signal scalar | vector

Output signal specified by an entry in the **Waveform Definition**
table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

## Parameters

### Main

### **Output Signal** — Waveform for output signal 1 (default) | integer

Select waveform definition to specify the output signal. The number
corresponds to the line item in the **Waveform
Definition** table. You can change this parameter while a
simulation is running.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SelectedSignal` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1'` |

### **Waveform Definition** — Waveform signal notations constant | `gaussian(mean,variance,seed)` | `pulse(amplitude,trigger_time,duration)` | `sawtooth(amplitude,frequence,phase_offset)` | `sin(amplitude,frequence,phase_offset)` | `square(amplitude,frequence,phase_offset)` | `step(step_time,initial_value,final_value)`

Enter signal notations in the **Waveform Definition** table, one
waveform definition per line. For syntax details, see Algorithms.

### Signal Attributes

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

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

### **Output data type** — Specify the output data type `double` (default) | `Inherit: Inherit via back propagation` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **Default**: `'double'` |

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

### **Sample time** — Time interval between samples `0.1` (default) | scalar

Specify the time interval between samples. To inherit the sample time,
set this parameter to `-1`. See Specify Sample Time
for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.1'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2015b**
