---
type: simulink-block
title: 'Lookup Table Dynamic'
family: lookup-tables
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'lookuptabledynamic'
---

# Lookup Table Dynamic

Approximate a one-dimensional function using dynamic table

## 中文

使用动态表逼近一维函数

### 所属库

Simulink / Lookup Tables

### 描述

#### 此模块与其他 Lookup Table 模块的不同之处

Lookup Table Dynamic 模块使用 `xdat` 和 `ydat` 向量计算函数 `y = f(x)` 的逼近值。查找方法可以使用内插、外插或原始输入值。

使用 Lookup Table Dynamic 模块，您可以更改表数据而无需停止仿真。例如，如果您正在仿真的物理系统发生变化，您可以加入新的表数据。

有关替代 Lookup Table Dynamic 模块的信息，请参阅 n-D Lookup Table。

#### 断点和表数据的输入

`xdat` 向量是断点数据，它必须*严格单调递增*。在转换为定点数据类型后，该向量中的下一个元素的值必须大于上一个元素的值。由于量化的原因，`xdat` 对于浮点数据类型可以严格单调，但在转换为定点数据类型之后，则不能严格单调。

`ydat` 向量是表数据，是函数在断点值处的计算结果。

**注意**

`xdat` 和 `ydat` 的输入不能是标量（一元数组）值。如果您为其中任一输入提供了标量值，您会在仿真时看到错误消息。为 `xdat` 和 `ydat` 输入都提供 1×n 向量。

#### 查找表定义

您通过将 `xdat` 和 `ydat` 作为 1×n 向量馈送给模块来定义查找表。要减少为此模块生成的代码中使用的 ROM，您可以为 `xdat` 和 `ydat` 使用不同的数据类型。

**提示**

均匀分布的断点可使 Simulink® Coder™ 生成的代码无分割。有关详细信息，请参阅 Simulink 文档中的 `fixpt_evenspace_cleanup` 和 Simulink Coder 文档中的Identify questionable fixed-point operations (Embedded Coder)。

#### 模块如何生成输出

此模块采用您为**查找方法**选择的方法使用输入值生成输出：

| 查找方法 | 模块操作 |
| --- | --- |
| **内插-外插** | 对输入执行线性内插和外插。  - 如果输入与断点匹配，则输出表数据中的对应元素。 - 如果输入与断点不匹配，模块将通过在表的两个元素之间执行线性内插来确定输出。如果输入不在断点值的范围内，模块将使用前两个或最后两个点进行外插。  **注意**  如果您选择此查找方法，Simulink Coder 软件将无法为此模块生成代码。 |
| **插值 - 使用最终值**（默认值） | 执行线性内插，但不会在断点数据的端点外进行外插，而是会转而使用端点值。 |
| **取最邻近的输入值** | 查找 `xdat` 中最接近当前输入的元素。输出 `ydat` 中的对应元素。 |
| **向下取输入值** | 查找 `xdat` 中最接近并且低于当前输入的元素。输出 `ydat` 中的对应元素。如果 `xdat` 中没有任何元素低于当前输入，模块将查找最邻近的元素。 |
| **向上取输入值** | 查找 `xdat` 中最接近并且高于当前输入的元素。输出 `ydat` 中的对应元素。如果 `xdat` 中没有任何元素高于当前输入，模块将查找最邻近的元素。 |

**注意**

当输入 `x` 与断点值匹配时，`Use Input Nearest`、`Use Input Below` 和 `Use Input Above` 方法执行相同的操作。

有些连续求解器将仿真时间细分为主时间步和子时间步。子时间步是对主时间步的细分。求解器在每个主时间步生成结果，并使用子时间步的结果提高主时间步结果的准确性。对于连续求解器，Lookup Table Dynamic 模块的输出可能像一个楼梯，因为信号在子时间步是固定的，以免生成不正确的结果。有关求解器如何影响模块输出的详细信息，请参阅 Simulink 文档中的比较求解器。

### 端口

#### 输入

#### **x** — 输入向量 标量 | 向量 | 二维数组

模块接受实数值或复数值输入。

**示例:** `2:12`

##### 依赖关系

`x` 输入向量和 `xdat` 断点数据必须具有相同的符号、偏置和小数斜率。此外，`x` 的精度和范围必须大于或等于 `xdat` 的精度和范围。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

#### **xdat** — 断点数据 由严格单调递增值组成的 1×n 向量

`xdat` 向量是断点数据，它必须严格单调递增。在转换为定点数据类型后，该向量中的下一个元素的值必须大于上一个元素的值。由于量化的原因，`xdat` 对于浮点数据类型可以严格单调，但在转换为定点数据类型之后，则不能严格单调。

**提示**

均匀分布的断点可使 Simulink Coder 生成的代码无分割。有关详细信息，请参阅 Simulink 文档中的 `fixpt_evenspace_cleanup` 和 Simulink Coder 文档中的Identify questionable fixed-point operations (Embedded Coder)。

**示例:** `1:10`

##### 依赖关系

`xdat` 断点数据和 `x` 输入向量必须具有相同的符号、偏置和小数斜率。此外，`x` 的精度和范围必须大于或等于 `xdat` 的精度和范围。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

#### **ydat** — 表数据 1×n 向量

`ydat` 输入是实数值或复数值表数据的 1×n 向量，它是函数在断点值处的计算结果。

**示例:**  `[0 3 12 27 48 75 108 147 192 243 300]`

##### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和小数斜率。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
#### 输出

#### **y** — 使用动态表数据计算 `y = f(x)` 的逼近值 1×n 向量

该模块使用 `xdat` 和 `ydat` 输入向量来计算函数 `y = f(x)` 的逼近值。查找方法可以使用内插、外插或原始输入值。

##### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和小数斜率。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### “常设”选项卡

#### **查找方法** — 指定查找方法 **插值 - 使用最终值** (默认) | **内插-外插** | **取最邻近的输入值** | **向下取输入值** | **向上取输入值**

该模块通过将您选择的**查找方法**应用于断点数据 (`xdat`) 和表数据 (`ydat`) 的输入向量来计算输出。有关详细信息，请参阅模块如何生成输出。

##### 编程用法

|  |
| --- |
| **模块参数**：`LookUpMeth` |
| **类型：**字符向量 |
| **值：**`'Interpolation-Extrapolation' | 'Interpolation-Use End Values' | 'Use Input Nearest' | 'Use Input Below' | 'Use Input Above'` |
| **默认值：**`'Interpolation-Use End Values'` |

#### “信号属性”选项卡

#### **输出数据类型** — 输出数据类型 **double** (默认) | **'继承:通过反向传播继承'** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定输出信号 `y` 的数据类型。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和小数斜率。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | <data type expression>` |
| **默认值：**`'double'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

#### **发生溢出时饱和处理为最大值或最小值** — 溢出操作的方法 `off` (默认) | `on`

当您选中此复选框时，溢出将饱和处理为数据类型可表示的最大值或最小值。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

当**查找方法**参数设置为**内插-外插**时，Lookup Table Dynamic 模块不生成代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

Simulink PLC Coder™ 软件不支持 Simulink Lookup Table Dynamic 模块。为方便起见，plclib/Simulink/Lookup Tables 库包含使用 Prelookup 和 Interpolation Using Prelookup 模块的动态表查找模块的实现。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Lookup Tables

## Description

### How This Block Differs from Other Lookup Table Blocks

The Lookup Table Dynamic block computes an approximation of a function
`y = f(x)` using `xdat` and
`ydat` vectors. The lookup method can use interpolation,
extrapolation, or the original values of the input.

Using the Lookup Table Dynamic block, you can change the table data without
stopping the simulation. For example, you can incorporate new table data if the
physical system you are simulating changes.

As an alternative to Lookup Table Dynamic block, see n-D Lookup Table.

### Inputs for Breakpoint and Table Data

The `xdat` vector is the breakpoint data, which must be
*strictly monotonically increasing*. The value of the next
element in the vector must be greater than the value of the preceding element after
conversion to a fixed-point data type. Due to quantization, `xdat`
can be strictly monotonic for a floating-point data type, but not after conversion
to a fixed-point data type.

The `ydat` vector is the table data, which is an evaluation of
the function at the breakpoint values.

**Note**

The inputs to `xdat` and `ydat` cannot be
scalar (one-element array) values. If you provide a scalar value to either of
these inputs, you see an error upon simulation. Provide a 1-by-n vector to both
the `xdat` and `ydat` inputs.

### Lookup Table Definition

You define the lookup table by feeding `xdat` and `ydat`
as 1-by-n vectors to the block. To reduce ROM usage in the generated code for this
block, you can use different data types for `xdat` and
`ydat`.

**Tip**

Breakpoints with even spacing can make Simulink®
Coder™ generated code division-free. For more information, see `fixpt_evenspace_cleanup` in
the Simulink documentation and Identify questionable fixed-point operations (Embedded Coder) in the Simulink
Coder documentation.

### How the Block Generates Output

The block uses the input values to generate output using the method you select for
**Lookup Method**:

| Lookup Method | Block Action |
| --- | --- |
| `Interpolation-Extrapolation` | Performs linear interpolation and extrapolation of the inputs.  - If the input matches a breakpoint, the output is the   corresponding element in the table data. - If the input does not match a breakpoint, the block   performs linear interpolation between two elements of   the table to determine the output. If the input falls   outside the range of breakpoint values, the block   extrapolates using the first two or last two   points.  **Note**  If you select this lookup method, Simulink Coder software cannot generate code for this block. |
| `Interpolation-Use End Values` (default) | Performs linear interpolation but does not extrapolate outside the end points of the breakpoint data. Instead, the block uses the end values. |
| `Use Input Nearest` | Finds the element in `xdat` nearest the current input. The corresponding element in `ydat` is the output. |
| `Use Input Below` | Finds the element in `xdat` nearest and below the current input. The corresponding element in `ydat` is the output. If there is no element in `xdat` below the current input, the block finds the nearest element. |
| `Use Input Above` | Finds the element in `xdat` nearest and above the current input. The corresponding element in `ydat` is the output. If there is no element in `xdat` above the current input, the block finds the nearest element. |

**Note**

The `Use Input Nearest`, `Use Input Below`,
and `Use Input Above` methods perform the same action when the
input `x` matches a breakpoint value.

Some continuous solvers subdivide the simulation time span into major and minor time steps.
A minor time step is a subdivision of the major time step. The solver produces a
result at each major time step and uses results at minor time steps to improve the
accuracy of the result at the major time step. For continuous solvers, the output of
the Lookup Table Dynamic block can appear like a stair step because
the signal is fixed in minor time step to avoid incorrect results. For more
information about the effect of solvers on block output, see Compare Solvers in the Simulink documentation.

## Ports

### Input

### **x** — input vector scalar | vector | 2-D array

The block accepts real-valued or complex-valued inputs.

**Example:** `2:12`

#### Dependencies

The `x` input vector and the
`xdat` breakpoint data must have the same sign,
bias, and fractional slope. Also, the precision and range for
`x` must be greater than or equal to the
precision and range for `xdat`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **xdat** — breakpoint data 1-by-n vector of strictly monotonically increasing values

The `xdat` vector is the breakpoint data, which must
be strictly monotonically increasing. The value of the next element in
the vector must be greater than the value of the preceding element after
conversion to a fixed-point data type. Due to quantization,
`xdat` can be strictly monotonic for a
floating-point data type, but not after conversion to a fixed-point data
type.

**Tip**

Breakpoints with even spacing can make Simulink
Coder generated code division-free. For more information,
see `fixpt_evenspace_cleanup` in the Simulink documentation and Identify questionable fixed-point operations (Embedded Coder) in the
Simulink
Coder documentation.

**Example:** `1:10`

#### Dependencies

The `xdat` breakpoint data and the
`x` input vector must have the same sign, bias,
and fractional slope. Also, the precision and range for
`x` must be greater than or equal to the
precision and range for `xdat`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **ydat** — table data 1-by-n vector

The `ydat` input is a 1-by-n vector of real-valued or
complex-valued table data, which is an evaluation of the function at the
breakpoint values.

**Example:**
`[0 3 12 27 48 75 108 147 192 243 300]`

#### Dependencies

The `ydat` table data and the
`y` output vector must have the same sign,
bias, and fractional slope.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### Output

### **y** — Approximation of `y = f(x)` using dynamic table data 1-by-n vector

The block computes an approximation of a function `y =
f(x)` using the `xdat` and
`ydat` input vectors. The lookup method can use
interpolation, extrapolation, or the original values of the
input.

#### Dependencies

The `ydat` table data and the
`y` output vector must have the same sign,
bias, and fractional slope.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main Tab

### **Lookup Method** — Specify the lookup method `Interpolation-Use End Values` (default) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

The block computes output by applying the **Lookup
Method** you select to the input vectors of breakpoint data
(`xdat`) and table data (`ydat`).
For details, see How the Block Generates Output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LookUpMeth` |
| **Type:** character vector |
| **Values:** `'Interpolation-Extrapolation' | 'Interpolation-Use End Values' | 'Use Input Nearest' | 'Use Input Below' | 'Use Input Above'` |
| **Default:** `'Interpolation-Use End Values'` |

### Signal Attributes Tab

### **Output data type** — Output data type `double` (default) | `'Inherit: Inherit via back propagation'` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the output signal
`y`.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

The `ydat` table data and the
`y` output vector must have the same sign,
bias, and fractional slope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | <data type expression>` |
| **Default:** `'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or minimum value
that the data type can represent. Otherwise, overflows wrap.

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. In general, the code generation process can detect
when overflow is not possible. In this case, the code generator does not produce
saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Lookup Table Dynamic block does not generate code when the **Lookup
Method** parameter is set to
`Interpolation-Extrapolation`.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

The Simulink
PLC Coder™ software does not support the Simulink
Lookup Table Dynamic block. For your convenience, the
plclib/Simulink/Lookup Tables library contains an implementation of a dynamic table
lookup block using the Prelookup and Interpolation Using
Prelookup blocks.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
