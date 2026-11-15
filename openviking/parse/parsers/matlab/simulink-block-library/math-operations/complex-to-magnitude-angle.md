---
type: simulink-block
title: 'Complex to Magnitude-Angle'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complextomagnitudeangle'
---

# Complex to Magnitude-Angle

Compute magnitude and/or phase angle of complex signal

## 中文

计算复信号的幅值和/或相位角

### 所属库

Simulink / Math Operations

### 描述

Complex to Magnitude-Angle 模块输出输入信号的幅值和/或相位角，具体取决于**输出**参数的设置。输出是与模块输入具有相同数据类型的实数值。输入可以是复信号数组，这种情况下，输出信号也是数组。幅值信号数组包含对应的复数输入元素的幅值。同样，角度输出包含输入元素的角度。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

模块计算并输出幅值和/或相位角的复输入信号。

##### 限制

仅当**逼近方法**设置为 **CORDIC** 时才支持定点数据类型。

**数据类型:** `single` | `double`
#### 输出

#### **Port\_1** — 幅值 标量 | 向量 | 矩阵

输出信号，即输入信号的幅值和/或相位角。要选择输出，请设置**输出**参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **Port\_2** — 相位角弧度 标量 | 向量 | 矩阵

相位角弧度，以实数值标量、向量或矩阵形式返回。

##### 依赖关系

- 要启用此端口，请将**输出**设置为**幅值和角度**或**角度**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **输出** — 幅值和/或相位角输出设定 **幅值和角度** (默认) | **幅值** | **角度**

指定输出是输入信号的幅值和/或相位角（弧度）。

##### 编程用法

|  |
| --- |
| **参数：**`Output` |
| **类型：**字符向量 |
| **值：**`'Magnitude and angle'` | `'Magnitude'` | `'Angle'` |
| **默认值：**`'Magnitude and angle'` |

#### **逼近方法** — 逼近方法 **无** (默认) | **CORDIC**

指定计算输出的逼近方法类型。

| 逼近方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| **无**（默认值） | 浮点 | 您想使用默认的泰勒级数算法。 |
| **CORDIC** | 浮点和定点 | 您需要快速的近似计算时。 |

模块使用以下数据类型传播规则。

| 复数输入的数据类型 | 逼近方法 | 幅值输出的数据类型 | 角度输出的数据类型 |
| --- | --- | --- | --- |
| 浮点 | **无**或 **CORDIC** | 与输入相同 | 与输入相同 |
| 有符号、定点 | **CORDIC** | `fixdt`(1, *`WL`* +2, *`FL`*)  其中：  - *`WL`* = 幅值的输入字长 + 2 + 1 - *`FL`* = 幅值的输入小数长度 | `fixdt`(1, *`WL`* +2, *`FL`*)  其中：  - *`WL`* = 幅值的输入字长 -3，以获得 [`-pi, pi`] 的最佳精度 - *`FL`* = 角度的输入小数长度 |
| 无符号、定点 | **CORDIC** | `fixdt`(1, *`WL`* +3, *`FL`*)  其中：  - *`WL`* = 幅值的输入字长 + 2 - *`FL`* = 幅值的输入小数长度 | `fixdt`(1, *`WL`* +3, *`FL`*)  其中：  - *`WL`* = 角度的输入字长 - 2，以获得范围 [0, pi/2] 的最佳精度小数长度 - *`FL`* = 角度的输入小数长度 |

##### 编程用法

|  |
| --- |
| **模块参数**：`ApproximationMethod` |
| **类型：**字符向量 |
| **值：**`'None' | 'CORDIC'` |
| **默认值：**`'None'` |

#### **迭代次数** — CORDIC 算法的迭代次数 `11` (默认) | 正整数，小于或等于定点输入的字长

CORDIC 算法执行的迭代次数，指定为正整数值标量。增加迭代次数可以得出更准确的结果，但会增加计算开销和延迟。

| 模块输入的数据类型 | 您可以指定的值 |
| --- | --- |
| 浮点 | 正整数。最大值是 52（对于双精度）或 23（对于单精度）。 |
| 定点 | 不超过幅值输入字长或相位角输入字长（二者中取较小值）的正整数。 |

##### 依赖关系

要启用此参数，请将**逼近方法**设置为 **CORDIC**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumberOfIterations` |
| **类型：**字符向量 |
| **值：**正整数，小于等于定点输入的字长 |
| **默认值：**`'11'` |

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

### 版本历史记录

**在 R2006a 之前推出**

#### R2024b: Complex to Magnitude-Angle 模块支持定点输入

Complex to Magnitude-Angle 模块现在支持 CORDIC 逼近方法。此方法允许在输入 **Port\_1** 处使用定点输入。要选择 CORDIC 方法，请将新**逼近方法**参数设置为 **CORDIC**。

选择 CORDIC 方法时，模块图标会更新。新参数“迭代次数”允许您定义 CORDIC 算法的迭代次数。

Complex to Magnitude-Angle block icon with CORDIC approximation method input

## Libraries

Simulink / Math Operations

## Description

The Complex to Magnitude-Angle block outputs the magnitude and/or phase angle of the
input signal, depending on the setting of the **Output** parameter. The
outputs are real values of the same data type as the block input. The input can be an
array of complex signals, in which case the output signals are also arrays. The
magnitude signal array contains the magnitudes of the corresponding complex input
elements. The angle output similarly contains the angles of the input elements.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Complex input signal that the block computes and outputs the magnitude
and/or the phase angle.

#### Limitations

Fixed-point data types are supported only when you set the
**Approximation method** to
`CORDIC`.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Magnitude scalar | vector | matrix

Output signal that is the magnitude and/or phase angle of the input
signal. To choose the output, set the **Output**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — Radian phase angle scalar | vector | matrix

Radian phase angle, returned as a real-valued scalar, vector, or
matrix.

#### Dependencies

- To enable this port, set **Output** to
  `Magnitude and angle` or
  `Angle`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Output** — Magnitude and/or phase angle output specification `Magnitude and angle` (default) | `Magnitude` | `Angle`

Specify if the output is the magnitude and/or the phase angle in radians
of the input signal.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `Output` |
| **Type:** character vector |
| **Values:** `'Magnitude and angle'` | `'Magnitude'` | `'Angle'` |
| **Default:** `'Magnitude and angle'` |

### **Approximation method** — Approximation method `None` (default) | `CORDIC`

Specify the type of approximation for computing output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating-point | You want to use the default Taylor series algorithm. |
| `CORDIC` | Floating-point and fixed-point | You want a fast, approximate calculation. |

The block uses these data type propagation rules.

| Data Type of Complex Input | Approximation Method | Data Type of Magnitude Output | Data Type of Angle Output |
| --- | --- | --- | --- |
| Floating point | `None` or `CORDIC` | Same as input | Same as input |
| Signed, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*)  where:  - *`WL`* = input word   length of the magnitude + 2 + 1 - *`FL`* = input fraction   length of the magnitude | `fixdt`(1, *`WL`* + 2, *`FL`*)  where:  - *`WL`* = input word   length of the magnitude -3, for best precision for   [`-pi, pi`) - *`FL`* = input fraction   length of the angle |
| Unsigned, fixed point | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*)  where:  - *`WL`* = input word   length of the magnitude + 2 - *`FL`* = input fraction   length of the magnitude | `fixdt`(1, *`WL`* + 3, *`FL`*)  where:  - *`WL`* = input word   length of the angle - 2, for best precision   fraction length for range [0, pi/2] - *`FL`* = input fraction   length of the angle |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'None' | 'CORDIC'` |
| **Default:** `'None'` |

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | positive integer, less than or equal to word length of fixed-point input

Number of iterations the CORDIC algorithm performs, specified as a
positive integer-valued scalar. Increasing the number of iterations can
produce more accurate results but also increases the expense of the
computation and adds latency.

| Data Type of Block Inputs | Value You Can Specify |
| --- | --- |
| Floating-point | A positive integer. The maximum value is 52 for double or 23 for single. |
| Fixed-point | A positive integer that does not exceed the word length of the magnitude input or the word length of the phase angle input, whichever value is smaller. |

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

## Version History

**Introduced before R2006a**

### R2024b: Complex to Magnitude-Angle block supports fixed-point inputs

Complex to Magnitude-Angle block now
supports the CORDIC approximation method. This method allows fixed-point inputs at
input **Port\_1**. To select the CORDIC method, set the new
**Approximation method** parameter to
`CORDIC`.

When you select the CORDIC method, the block icon updates. The new parameter,
Number of iterations, lets you define the number of iterations for the CORDIC
algorithm.

Complex to Magnitude-Angle block icon with CORDIC approximation method input
