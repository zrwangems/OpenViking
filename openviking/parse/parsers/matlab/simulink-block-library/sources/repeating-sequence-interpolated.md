---
type: simulink-block
title: 'Repeating Sequence Interpolated'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequenceinterpolated'
---

# Repeating Sequence Interpolated

Output discrete-time sequence and repeat, interpolating between data points

## 中文

输出离散时间序列并重复，从而在数据点之间插值

### 所属库

Simulink / Sources

### 描述

Repeating Sequence Interpolated 模块根据**时间值的向量**和**输出值的向量**参数中的值输出周期性离散序列。在数据点之间，该模块使用您为**查找方法**参数指定的方法来确定输出。

### 端口

#### 输出

#### **Port\_1** — 周期性输出信号 标量

根据**时间值的向量**和**输出值的向量**参数中的值生成的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **输出值的向量** — 输出值的向量 `[3 1 4 2 1].'` (默认) | 向量

输出值的向量，用于指定输出波形。每个元素对应于**时间值的向量**参数中的时间值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutValues` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[3 1 4 2 1].''` |

#### **时间值的向量** — 时间值的向量 `[0 0.1 0.5 0.6 1].'` (默认) | 向量

指定包含时间值的列向量。时间值必须严格递增，并且向量的大小必须与输出值向量的大小相同。

##### 编程用法

|  |
| --- |
| **模块参数**：`TimeValues` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[0 0.1 0.5 0.6 1].''` |

#### **查找方法** — 输出的查找方法 **插值 - 使用最终值** (默认) | **取最邻近的输入值** | **向下取输入值** | **向上取输入值**

指定查找方法以确定数据点之间的输出。

##### 编程用法

|  |
| --- |
| **模块参数**：`LookUpMeth` |
| **类型**：字符向量 |
| **值**：`'Interpolation-Use End Values'` | `'Use Input Nearest'` | `'Use Input Below'` | `'Use Input Above'` |
| **默认值**：`'Interpolation-Use End Values'` |

#### **采样时间** — 采样时间间隔 `0.01` (默认) | 标量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`tsamp` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.01'` |

#### 信号属性

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
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | **fixdt(1,16,2^0,0)** | `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
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

不能在触发子系统层次结构中使用。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Repeating Sequence Interpolated block outputs a periodic discrete-time
sequence based on the values in **Vector of time values** and
**Vector of output values** parameters. Between data points, the
block uses the method you specify for the **Lookup Method** parameter
to determine the output.

## Ports

### Output

### **Port\_1** — Periodic output signal scalar

Output signal generated based on the values in the **Vector of time
values** and **Vector of output values**
parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Vector of output values** — Vector of output values `[3 1 4 2 1].'` (default) | vector

Vector of output values that specify the output waveform. Each element corresponds to
the time value in the **Vector of time values**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutValues` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'[3 1 4 2 1].''` |

### **Vector of time values** — Vector of time values `[0 0.1 0.5 0.6 1].'` (default) | vector

Specify the column vector containing time values. The time values must
be strictly increasing, and the vector must have the same size as the
vector of output values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TimeValues` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `'[0 0.1 0.5 0.6 1].''` |

### **Lookup Method** — Lookup method for output `Interpolation-Use End Values` (default) | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

Specify the lookup method to determine the output between data
points.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LookUpMeth` |
| **Type**: character vector |
| **Values**: `'Interpolation-Use End Values'` | `'Use Input Nearest'` | `'Use Input Below'` | `'Use Input Above'` |
| **Default**: `'Interpolation-Use End Values'` |

### **Sample time** — Time interval between samples `0.01` (default) | scalar

Specify the time interval between samples. To inherit the sample time,
set this parameter to `-1`. See Specify Sample Time
for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `tsamp` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.01'` |

### Signal Attributes

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
| **Values**: `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
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

Cannot be used inside a triggered subsystem hierarchy.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
