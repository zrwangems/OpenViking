---
type: simulink-block
title: 'Discrete-Time Integrator'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretetimeintegrator'
documentation_source_path: '../simulink/slref/discretetimeintegrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete-Time Integrator

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **External reset** — 外部复位信号 标量

外部复位信号，指定为标量。当指定的触发事件发生时，该模块将状态重置为其初始条件。

**提示**

此端口的图标会根据 **External reset** 参数的值而变化。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为
`rising`、
`falling`、
`either`、
`level` 或 `sampled
level`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **IC** — 状态的初始条件 标量 | 向量 | 矩阵

状态的初始条件，指定为有限标量、向量或矩阵。

#### 依赖关系

要启用此端口，请将 **Initial condition
source** 设置为 `external`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输入的离散时间积分或累加 标量 | 向量 | 矩阵

输入信号的离散时间积分或累加，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 饱和输出 标量 | 向量 | 矩阵

指示状态何时被限制的信号，指定为标量、向量或矩阵。该信号具有以下三个值之一：

- `1` 表示正在应用上限。
- `0` 表示积分未受限制。
- `-1` 表示正在应用下限。

#### 依赖关系

要启用此端口，请选中 **Show saturation
port** 复选框。

**数据类型：** `single` | `double` | `int8`

### **Port\_3** — 状态输出 标量 | 向量 | 矩阵

模块状态，以标量、向量或矩阵形式输出。默认情况下，该模块将此端口添加到模块图标的顶部。在以下情况下使用状态端口：

- 模块的输出通过复位端口或初始条件端口反馈回模块，从而导致代数环。有关示例，请参阅
  `sldemo_bounce_two_integrators`
  模型。
- 您希望将状态从一个条件执行子系统传递到另一个条件执行子系统，这可能导致时序问题。有关示例，请参阅 `sldemo_clutch` 模型。

有关详细信息，请参阅何时使用状态端口。

#### 依赖关系

要启用此端口，请选中 **Show state
port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Integrator method** — 累加方法 `Integration: Forward Euler`（默认）| `Integration: Backward Euler` | `Integration: Trapezoidal` | `Accumulation: Forward Euler` | `Accumulation: Backward Euler` | `Accumulation: Trapezoidal`

指定积分或累加方法。有关详细信息，请参阅输出方程以及积分和累加方法。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IntegratorMethod` |
| **类型：** 字符向量 |
| **值：** `'Integration: Forward Euler'` | `'Integration: Backward Euler'` | `'Integration: Trapezoidal'` | `'Accumulation: Forward Euler'` | `'Accumulation: Backward Euler'` | `'Accumulation: Trapezoidal'` |
| **默认值：** `'Integration: Forward Euler'` |

### **Gain value** — 与积分器输入相乘的值 `1.0`（默认）| 标量 | 向量

指定用于乘以积分器输入的标量、向量或矩阵。增益的每个元素必须为正实数。

- 指定非 1.0（默认值）的值在语义上等同于将 Gain 模块连接到积分器的输入。
- 有效条目包括：

  - `double(1.0)`
  - `single(1.0)`
  - `[1.1 2.2 3.3 4.4]`
  - `[1.1 2.2; 3.3 4.4]`

**提示**

使用此参数指定输入增益可消除生成代码中的乘法运算。但是，此参数必须不可调才能实现此优势。如果您希望调整输入增益，请将此参数设置为 1.0，并使用外部 Gain 模块指定输入增益。

#### 程序化使用

|  |
| --- |
| **模块参数：** `gainval` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'1.0'` |

### **External reset** — 选择何时将状态重置为初始条件 `none`（默认）| `rising` | `falling` | `either` | `level` | `sampled level`

选择将状态重置为其初始条件的触发事件类型：

- `none` — 不将状态重置为初始条件。
- `rising` — 当复位信号具有上升沿时重置状态。
- `falling` — 当复位信号具有下降沿时重置状态。
- `either` — 当复位信号上升或下降时重置状态。
- `level` — 当复位信号非零时，将输出重置并保持为初始条件。
- `sampled level` — 当复位信号非零时，将输出重置为初始条件。

有关详细信息，请参阅重置状态和复位触发类型。

#### 程序化使用

|  |
| --- |
| **模块参数：**  `ExternalReset` |
| **类型：**  字符向量 |
| **值：**  `'none'` | `'rising'` | `'falling'` | `'either'` | `'level'` | `'sampled level'` |
| **默认值：** `'none'` |

### **Initial condition source** — 使用外部信号设置初始条件的选项 `internal`（默认）| `external`

选择初始条件的来源：

- `internal` — 从 **Initial condition** 参数获取状态的初始条件。
- `external` — 从外部信号获取状态的初始条件。选择此选项时，模块上会出现一个输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：**`InitialConditionSource` |
| **类型：**  字符向量、字符串 |
| **值：**  `'internal'` | `'external'` |
| **默认值：**  `'internal'` |

### **Initial condition** — 状态的初始条件 `0`（默认）| 标量 | 向量 | 矩阵

指定模块状态的初始条件。最小值和最大值受 **Output minimum** 和 **Output maximum** 模块参数的约束。

**提示**

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

#### 依赖关系

要启用此参数，请将 **Initial condition source** 设置为 `internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

### **Initial condition setting** — 选择在何处应用初始条件 `Auto`（默认）| `Output` | `Compatibility`

选择是将 **Initial condition** 参数的值应用于模块状态还是模块输出。初始条件也是复位值。

- `Auto` — 模块选择在何处应用 **Initial condition** 参数。

  - 如果模块位于非触发子系统中，且 **Integrator method** 设置为积分方法，则设置初始条件：

    `x(0) = IC`

    复位时：

    `x(n) = IC`
  - 如果模块位于触发子系统或函数调用子系统中，且 **Integrator method** 设置为积分方法，则按照选择 `output` 的方式设置初始条件。
- `Output` — 当模块位于触发子系统或函数调用子系统中，且 **Integrator method** 设置为积分方法时，使用此选项。

  设置初始条件：

  `y(0) = IC`

  复位时：

  `y(n) = IC`
- `Compatibility` — 此选项用于提供向后兼容性。您无法为 Simulink 模型中的 Discrete-Time Integrator 模块选择此选项，但可以为库中的 Discrete-Time Integrator 模块选择此选项。使用此选项可保持与 R2014a 之前创建的 Simulink 模型的兼容性。

  在 R2014a 之前，选项 `Auto` 被称为 `State only (most
  efficient)`。选项 `Output` 被称为 `State and output`。使用选项 `Compatibility` 时模块的行为如下。

  - 如果 **Underspecified initialization detection** 设置为 `Classic`，则 **Initial condition setting** 参数的行为与 `Auto` 相同。
  - 如果 **Underspecified initialization detection** 设置为 `Simplified`，则 **Initial condition setting** 参数的行为与 `Output` 相同。

**注意**

在 R2014a 之前的 Simulink 中，此参数名为 **Use initial condition as initial and reset value for**。

#### 程序化使用

|  |
| --- |
| **模块参数：**  `InitialConditionSetting` |
| **类型：** 字符向量 |
| **值：**  `'Auto'` | `'Output'` | `'Compatibility'` |
| **默认值：**  `'Auto'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

输入步与步之间的离散时间间隔。

默认情况下，模块使用离散采样时间 `1`。要设置不同的采样时间，请输入另一个离散值，例如 0.1。

有关详细信息，请参阅指定采样时间。

#### 提示

- 不要指定采样时间为 0。此值指定连续采样时间，Discrete-Time Integrator 模块不支持该时间。
- 不要指定采样时间为 `inf` 或 `NaN`，因为这些值不是离散的。
- 如果指定 -1 以从上游模块继承采样时间，请验证上游模块使用离散采样时间。例如，Discrete-Time Integrator 模块无法继承采样时间 0。

#### 程序化使用

|  |
| --- |
| **模块参数：**  `SampleTime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：**  `'-1'` |

### **Limit output** — 将模块输出值限制在指定范围内 `off`（默认）| `on`

将模块的输出限制在 **Lower saturation limit** 和 **Upper saturation limit** 参数之间的值。

- 选中此复选框会将模块的输出限制在 **Lower saturation limit** 和 **Upper saturation limit** 参数之间的值。
- 清除此复选框不会限制模块的输出值。

#### 依赖关系

选择此参数会启用 **Lower saturation limit** 和 **Upper saturation limit** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**  `LimitOutput` |
| **类型：**  字符向量 |
| **值：**  `'off'` | `'on'` |
| **默认值：**  `'off'` |

### **Upper saturation limit** — 积分上限 `inf`（默认）| 标量 | 向量 | 矩阵

将积分上限指定为标量、向量或矩阵。您必须指定一个介于 **Output minimum** 和 **Output maximum** 参数值之间的值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UpperSaturationLimit` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'inf'` |

### **Lower saturation limit** — 积分下限 `-inf`（默认）| 标量 | 向量 | 矩阵

将积分下限指定为标量、向量或矩阵。您必须指定一个介于 **Output minimum** 和 **Output maximum** 参数值之间的值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LowerSaturationLimit` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'-inf'` |

### **Show saturation port** — 启用饱和输出端口 `off`（默认）| `on`

选中此复选框可向模块添加饱和输出端口。清除此复选框时，模块没有饱和输出端口。

#### 依赖关系

选择此参数会启用饱和输出端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowSaturationPort` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Show state port** — 启用状态输出端口 `off`（默认）| `on`

选中此复选框可向模块添加状态输出端口。清除此复选框时，模块没有状态输出端口。

#### 依赖关系

选择此参数会启用状态输出端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowStatePort` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Ignore limit and reset when linearizing** — 将模块视为不可复位 `off`（默认）| `on`

选中此复选框可使 Simulink 线性化命令将此模块视为不可复位，并且对其输出没有限制，无论模块复位和输出限制选项的设置如何。

**提示**

忽略限制和复位允许您围绕工作点对模型进行线性化。该点可能导致积分器复位或饱和。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IgnoreLimit` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 信号属性

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化（Embedded Coder）。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化（Embedded Coder）。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **数据类型** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。有关详细信息，请参阅 Control Data Types of Signals。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule` — Simulink 选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。如果更改嵌入式目标设置，内部规则所选择的数据类型可能会改变。例如，如果模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 `ASIC/FPGA` 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定 `Unspecified (assume 32-bit Generic)`（即通用 32 位微处理器）作为目标硬件，则输出数据类型为 `int32`。如果目标微处理器提供的字长都无法容纳输出范围，Simulink 软件将在 Diagnostic Viewer 中显示错误。

  软件并不总是能够同时优化代码效率和数值精度。如果内部规则不能满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用简单选项 `Inherit: Same as input`。
  - 显式指定默认数据类型（如
    `fixdt(1,32,16)`），然后使用定点
    工具为您的模型提议数据类型。有关详细信息，请参阅
    `fxptdlg` (Fixed-Point Designer)。
  - 要指定自己的继承规则，请使用 `Inherit: Inherit via back propagation`，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例，请参阅 Signal Attributes 库中的 Data Type Propagation Examples 模块。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的
**Output** 数据类型。有关更多
信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **整数舍入模式** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数
    向正无穷方向舍入。等效于
    MATLAB®
    `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示
    值。如果出现平局，则舍入到最接近的偶数
    整数。等效于 Fixed-Point Designer™
    `convergent` 函数。

`Floor`
:   将正数和负数
    向负无穷方向舍入。等效于
    MATLAB
    `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示
    值。如果出现平局，则向正无穷方向
    舍入。等效于 Fixed-Point Designer
    `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示
    值。如果出现平局，则将正数
    向正无穷方向舍入，将负数向负无穷方向舍入。等效于
    Fixed-Point Designer
    `round` 函数。

`Simplest`
:   自动在向负无穷方向舍入和向零方向舍入之间
    进行选择，以生成尽可能高效的舍入
    代码。

`Zero`
:   将数字向零方向舍入。等效于
    MATLAB
    `fix` 函数。

#### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

#### 另请参阅

有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型所能表示的
  最小值或最大值。
- `off` — 溢出回绕到数据类型所能表示的
  相应值。

例如，有符号 8 位整数 `int8`
所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致
8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。
  类似地，模块输出在最小输出值
  -128 处饱和。
- 清除此参数时，软件将导致溢出的
  值解释为 `int8`，这可能会产生非预期结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时为 -126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成代码中
  具有显式饱和保护时，请考虑选择此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于
  避免过度指定模块处理超出范围信号的方式。有关更多
  信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部
  运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。
  在这种情况下，代码生成器不会生成饱和
  代码。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **模式** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。
  选择 `Inherit` 会启用右侧的第二个菜单/文本框，
  您可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择
  `Built in` 会启用右侧的第二个菜单/文本框，
  您可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择
  `Fixed point` 会启用附加参数，
  您可以使用这些参数指定定点数据类型。
- `Expression` — 求值为数据
  类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，
  您可以在其中输入表达式。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请点击 **Show data type
assistant** 按钮。

### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据
  类型覆盖设置，即从使用该信号的模块、
  `Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型
  覆盖设置，并使用为该信号指定的定点数据类型。

有关更多信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built
in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您在使用数据类型覆盖时
可以更好地控制模型中的数据类型。
例如，您可以使用此选项确保数据类型满足
下游模块的要求，而不受数据类型覆盖设置的影响。

### **符号性** — 定点数据的符号性 `Signed`（默认）| `Unsigned`

指定您希望定点数据是有符号还是无符号。
有符号数据可以表示正值和负值，但无符号
数据仅表示正值。有关更多信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **字长** — 保存量化整数的字的位大小 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字的位大小。有关
更多信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **定标** — 定点数据的定标方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出
条件并最小化量化误差。有关更多信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **小数长度** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或
负整数。有关更多信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Binary point`。

### **斜率** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关更多信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Slope and bias`。

### **偏置** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关更多
信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Slope and bias`。

### 状态属性

### **状态名称** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

有关更多信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 依赖关系

当您为 **State name** 指定值并点击
**Apply** 时，将启用 **State name must resolve
to Simulink signal object** 参数。

#### 编程用法

|  |
| --- |
| **参数：**  `StateName` |
| **类型：**  字符向量 |
| **值：**  唯一名称 |
| **默认值：**  `''` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象的选项 `off`（默认）| `on`

指定是否要求状态名称解析为信号对象。如果选中，
当您指定的状态名称与信号对象的名称不匹配时，软件将在运行时生成错误。

选中此参数会禁用 **Code generation storage
class** 参数。

#### 依赖关系

当您为 **State name** 参数指定值，并将 **Signal resolution** 模型配置参数设置为
`None` 以外的值时启用。

#### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在触发子系统层次结构内使用时依赖于绝对时间。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 本机浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于尾数中没有前导零时可表示的最小浮点数的数。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min` 还是 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**限制**

- HDL 代码生成不支持状态端口。清除
  **Show state port** 选项。
- HDL 代码生成不支持外部初始条件。
  将 **Initial condition source** 设置为
  `Internal`。
- **External Reset** 必须设置为
  `none`、`rising`、
  `falling` 或 `level`。
- 不支持连续采样时间。请为模块使用离散采样时间。
- HDL 代码生成不支持输入使用浮点数据类型而
  **Gain value** 模块参数使用定点数据类型，或反之。

**注意**

为 Discrete Time Integrator 模块生成 HDL 代码时，
建议在 **Hardware
Implementation** 配置参数设置中将 **Device Vendor** 配置
参数设置为 `ASIC/FPGA`。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

执行信号的离散时间积分或累加

使用 Discrete-Time Integrator 模块代替 Integrator 模块来创建纯离散模型。使用 Discrete-Time Integrator 模块，您可以：

- 在模块对话框中定义初始条件，或将其作为模块的输入
- 定义输入增益（K）值
- 输出模块状态
- 定义积分的上限和下限
- 使用额外的复位输入复位状态

### 输出方程

在第一个时间步，模块状态 `n = 0`，初始输出 `y(0) = IC` 或初始状态 `x(0) = IC`，具体取决于 **Initial condition setting** 参数值。

对于给定的步 `n > 0` 及仿真时间 `t(n)`，Simulink® 按如下方式更新输出 `y(n)`：

- 前向欧拉法：

  ```
  y(n) = y(n-1) + K*[t(n) - t(n-1)]*u(n-1)
  ```
- 后向欧拉法：

  ```
  y(n) = y(n-1) + K*[t(n) - t(n-1)]*u(n)
  ```
- 梯形法：

  ```
  y(n) = y(n-1) + K*[t(n)-t(n-1)]*[u(n)+u(n-1)]/2
  ```

Simulink 根据模块采样时间（可以是显式的或触发的）自动选择这些输出方程的状态空间实现。当使用显式采样时间时，对于所有 `n > 0`，`t(n)-t(n-1)` 简化为采样时间 `T`。

### 积分和累加方法

此模块可以使用前向欧拉法、后向欧拉法或梯形法对信号进行积分或累加。假设 `u` 是输入，`y` 是输出，`x` 是状态。对于给定的步 `n`，Simulink 更新 `y(n)` 和 `x(n+1)`。在积分模式下，`T` 是模块采样时间（在触发采样时间的情况下为增量 `T`）。在累加模式下，`T = 1`。模块采样时间决定何时计算输出，但不决定输出值。`K` 是增益值。值根据上限或下限进行限幅。

**前向欧拉法**

前向欧拉法（默认），也称为前向矩形法或左手近似

软件将 `1/s` 近似为 `T/(z-1)`。模块在第 `n` 步的输出表达式为：

```
x(n+1) = x(n) + K*T*u(n)
y(n)   = x(n)
```

模块使用以下步骤计算输出：

```
Step 0:          y(0)   = IC (clip if necessary)
                 x(1)   = y(0) + K*T*u(0)

Step 1:          y(1)   = x(1)
                 x(2)   = x(1) + K*T*u(1)

Step n:          y(n)   = x(n)
                 x(n+1) = x(n) + K*T*u(n) (clip if necessary)
```

使用此方法时，输入端口 1 没有直接馈通。

**后向欧拉法**

后向欧拉法，也称为后向矩形法或右手近似

软件将 `1/s` 近似为 `T*z/(z-1)`。模块在第 `n` 步的输出表达式为

```
y(n) = y(n-1) + K*T*u(n).
```

令 `x(n) = y((n)-1)`。模块使用以下步骤计算输出。

- 如果 **Initial condition setting** 参数对于触发子系统和函数调用子系统设置为 `Output` 或 `Auto`：

  ```
  Step 0:          y(0) = IC (clipped if necessary)
                   x(1) = y(0)
  ```
- 如果 **Initial condition setting** 参数对于非触发子系统设置为 `Auto`：

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   x(1)   = y(0) = x(0) + K*T*u(0)

  Step 1:          y(1)   = x(1) + K*T*u(1)
                   x(2)   = y(1)

  Step n:          y(n)   = x(n) + K*T*u(n)
                   x(n+1) = y(n)
  ```

使用此方法时，输入端口 1 具有直接馈通。

**梯形法**

对于此方法，软件将 `1/s` 近似为 `T/2*(z+1)/(z-1)`。

当 `T` 固定时（等于采样周期），计算输出的表达式为：

```
x(n) = y(n-1) + K*T/2*u(n-1)
y(n) = x(n) + K*T/2*u(n)
```

- 如果 **Initial condition setting** 参数对于触发子系统和函数调用子系统设置为 `Output` 或 `Auto`：

  ```
  Step 0:          y(0)   = IC (clipped if necessary)
                   x(1)   = y(0) + K*T/2*u(0)
  ```
- 如果 **Initial condition setting** 参数对于非触发子系统设置为 `Auto`：

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   y(0)   = x(0) + K*T/2*u(0)
                   x(1)   = y(0) + K*T/2*u(0)

  Step 1:          y(1)   = x(1) + K*T/2*u(1)
                   x(2)   = y(1) + K*T/2*u(1)

  Step n:          y(n)   = x(n) + K*T/2*u(n)
                   x(n+1) = y(n) + K*T/2*u(n)
  ```

这里，`x(n+1)` 是下一个输出的最佳估计。它与状态不同，因为 `x(n)` 不等于 `y(n)`。

使用此方法时，输入端口 1 具有直接馈通。

**当 T 为变量时**

当 `T` 为变量时（例如，从触发时间获得），模块使用以下步骤计算输出。

- 如果 **Initial condition setting** 参数对于触发子系统和函数调用子系统设置为 `Output` 或 `Auto`：

  ```
  Step 0:          y(0)   = IC (clipped if necessary)
                   x(1)   = y(0)
  ```
- 如果 **Initial condition setting** 参数对于非触发子系统设置为 `Auto`：

  ```
  Step 0:          x(0)   = IC (clipped if necessary)
                   x(1)   = y(0) = x(0) + K*T/2*u(0)

  Step 1:          y(1)   = x(1) + K*T/2*(u(1) + u(0))
                   x(2)   = y(1)

  Step n:          y(n)   = x(n) + K*T/2*(u(n) + u(n-1))
                   x(n+1) = y(n)
  ```

### 定义初始条件

您可以将初始条件定义为模块对话框上的参数，或从外部信号输入：

- 要将初始条件定义为模块参数，请将 **Initial condition source** 参数设置为 `internal`，并在 **Initial condition** 文本框中输入值。
- 要从外部源提供初始条件，请将 **Initial condition source** 参数设置为 `external`。模块上会出现一个额外的输入端口。

### 何时使用状态端口

使用状态端口代替输出端口：

- 当模块的输出通过复位端口或初始条件端口反馈回模块时，会导致代数环。有关示例，请参阅 `sldemo_bounce_two_integrators` 模型。
- 当您想将状态从一个条件执行子系统传递到另一个条件执行子系统时，这可能会导致时序问题。有关示例，请参阅 Building a Clutch Lock-Up Model。

您可以通过状态端口而不是输出端口传递状态来解决这些问题。Simulink 生成状态的时间与输出略有不同，这可以保护您的模型免受这些问题的影响。要输出模块状态，请选中 **Show state port** 复选框。状态端口出现在模块顶部。

### 限制积分

要将输出保持在特定水平内，请选中 **Limit output** 复选框，并在相应的文本框中输入限值。这样做会使模块作为受限积分器运行。当输出达到限值时，积分作用关闭以防止积分饱和。在仿真期间，您可以更改限值，但不能更改输出是否受限。下表显示了模块如何确定输出。

| 积分 | 输出 |
| --- | --- |
| 小于 **Lower saturation limit** | 保持在 **Lower saturation limit** |
| 在 **Lower saturation limit** 和 **Upper saturation limit** 之间 | 积分值 |
| 大于 **Upper saturation limit** | 保持在 **Upper saturation limit** |

要生成指示积分何时达到限值的信号，请选中 **Show saturation port** 复选框。新的饱和端口出现在模块输出端口下方。

饱和信号具有以下三个值之一：

- 1 表示积分处于上限。
- 0 表示积分不受限制。
- -1 表示积分处于下限。

### 复位状态

模块根据外部信号将其状态复位到指定的初始条件。要使模块复位其状态，请选择 **External reset** 参数选项之一。会出现一个复位端口，指示复位触发类型。

复位端口具有直接馈通。如果模块输出直接或通过一系列具有直接馈通的模块反馈到此端口，则会产生代数环。要解决此环，请将模块状态端口的输出馈入复位端口。要访问模块状态，请选中 **Show state port** 复选框。

### 复位触发类型

**External reset** 参数允许您确定触发复位的复位信号属性。触发选项包括：

- `rising` – 当复位信号具有上升沿时复位状态。例如，此图显示了上升复位触发对后向欧拉积分的影响。
- `falling` — 当复位信号具有下降沿时复位状态。例如，此图显示了下降复位触发对后向欧拉积分的影响。
- `either` — 当复位信号上升或下降时复位状态。例如，下图显示了 either 复位触发对后向欧拉积分的影响。
- `level` — 当复位信号非零时，将输出复位并保持在初始条件。例如，此图显示了 level 复位触发对后向欧拉积分的影响。
- `sampled level` — 当复位信号非零时，将输出复位到初始条件。例如，此图显示了 sampled level 复位触发对后向欧拉积分的影响。

  `sampled level` 复位选项需要更少的计算，使其比 `level` 复位选项更高效。

  **注意**

  对于 Discrete-Time Integrator 模块，所有触发检测都基于具有正值的信号。例如，信号从 -1 变为 0 不被视为上升沿，但信号从 0 变为 1 被视为上升沿。

### 简化初始化模式下的行为

当您在配置参数对话框中将 **Underspecified initialization detection** 设置为 `Simplified` 时，将启用简化初始化模式。如果使用简化初始化模式，Discrete-Time Integrator 模块的行为与经典初始化模式不同。新的初始化行为更加稳健，并在以下情况下提供更一致的行为：

- 在代数环中
- 在使能和禁用时
- 在使用触发采样时间与显式采样时间比较结果时，其中模块以与显式采样时间相同的速率触发

简化初始化模式使从 Continuous-Time Integrator 模块到 Discrete-Time Integrator 模块的转换更加容易，因为初始条件对两个模块具有相同的含义。

有关经典和简化初始化模式的更多信息，请参阅 Underspecified initialization detection。

**Initial Condition Setting 设置为 Output 时的使能和禁用行为**

当您使用简化初始化模式并将 **Initial condition setting** 对于触发子系统和函数调用子系统设置为 `Output` 时，模块的使能和禁用行为简化如下。

在禁用时间 `td`：

```
 y(td) = y(td-1)
```

在使能时间 `te`：

- 如果父子系统控制端口的 **States when enabling** 设置为 `reset`：

  ```
  y(te) = IC.
  ```
- 如果父子系统控制端口的 **States when enabling** 设置为 `held`：

  ```
  y(te) = y(td).
  ```

  下图显示了此条件。

**迭代器子系统**

使用简化初始化模式时，不能将 Discrete-Time Integrator 模块放在迭代器子系统模块中。

在简化初始化模式下，迭代器子系统不维护经过时间。因此，如果需要经过时间的 Discrete-Time Integrator 模块被放置在迭代器子系统模块内，Simulink 会报告错误。

### 函数调用子系统内使能子系统中的行为

假设您有一个函数调用子系统，其中包含一个使能子系统，该子系统包含一个 Discrete-Time Integrator 模块。以下行为适用。

| 积分器方法 | 函数调用触发端口的采样时间类型 | 使能后函数调用子系统首次执行时的 `delta T` 值 | 行为原因 |
| --- | --- | --- | --- |
| 前向欧拉法 | 触发 | `t — tstart` | 当函数调用子系统首次执行时，积分器算法使用 `tstart` 作为先前的仿真时间。 |
| 后向欧拉法和梯形法 | 触发 | `t — tprevious` | 当函数调用子系统首次执行时，积分器算法使用 `tprevious` 作为先前的仿真时间。 |
| 前向欧拉法、后向欧拉法和梯形法 | 周期 | 函数调用生成器的采样时间 | 在周期模式下，Discrete-Time Integrator 模块使用函数调用生成器的采样时间作为 `delta T`。 |
