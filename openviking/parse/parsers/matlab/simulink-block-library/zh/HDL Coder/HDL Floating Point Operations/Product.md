---
type: simulink-block
title: 'Matrix Multiply'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'MAT'
documentation_page: 'product'
documentation_source_path: '../simulink/slref/product.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Multiply

## 端口

### 输入

### **Port\_1** — 要相乘或相除的第一个输入 标量 | 向量 | 矩阵 | N 维数组

要相乘或相除的第一个输入，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — 要相乘或相除的第 N 个输入 标量 | 向量 | 矩阵 | N 维数组

要相乘或相除的第 N 个输入，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **X** — 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组

要与其他输入相乘的输入信号。

#### 依赖关系

要启用一个或多个 **X** 端口，请为 **Number of inputs** 参数指定一个或多个 `*` 字符，并将 **Multiplication** 参数设置为 `Element-wise(.*)`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **÷** — 要相除或求逆的输入信号 标量 | 向量 | 矩阵 | N 维数组

用于相除或求逆运算的输入信号。

#### 依赖关系

要启用一个或多个 **÷** 端口，请为 **Number of inputs** 参数指定一个或多个 `/` 字符，并将 **Multiplication** 参数设置为 `Element-wise(.*)`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **\*** — 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组

要与其他输入相乘的输入信号。

#### 依赖关系

要启用一个或多个 **\*** 端口，请为 **Number of inputs** 参数指定一个或多个 `*` 字符，并将 **Multiplication** 参数设置为 `Matrix(*)`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Inv** — 要相除或求逆的输入信号 标量 | 向量 | 矩阵 | N 维数组

用于相除或求逆运算的输入信号。

#### 依赖关系

要启用一个或多个 **Inv** 端口，请为 **Number of inputs** 参数指定一个或多个 `/` 字符，并将 **Multiplication** 参数设置为 `Matrix(*)`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 通过对输入进行相乘、相除或求逆计算得到的输出 标量 | 向量 | 矩阵 | N 维数组

通过对输入进行相乘、相除或求逆计算得到的输出。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Number of inputs** — 控制输入数量和运算类型 `2`（默认）| 标量 | 每个输入端口对应 `*` 或 `/`

控制模块的两个属性：

- 模块上的输入端口数量
- 每个输入是相乘还是相除到输出中

当您指定：

- **`1` 或 `*` 或 `/`**

  模块有一个输入端口。在逐元素模式下，模块按照 Product of Elements 模块所述处理输入。在矩阵模式下，如果参数值为 `1` 或 `*`，模块输出输入值。如果值为 `/`，则输入必须是方阵（包括作为退化情况的标量），模块输出矩阵的逆。有关详细信息，请参阅逐元素模式和矩阵模式。
- **大于 1 的整数值**

  模块具有由该整数值给出的输入数量。这些输入按照 **Multiplication** 参数的指定，在逐元素模式或矩阵模式下相乘。有关详细信息，请参阅逐元素模式和矩阵模式。
- **由两个或更多 `*` 和 `/` 字符组成的未加引号字符串**

  模块具有由字符向量长度给出的输入数量。每个对应 `*` 字符的输入相乘到输出中。每个对应 `/` 字符的输入相除到输出中。这些运算按照 **Multiplication** 参数的指定，在逐元素模式或矩阵模式下进行。有关详细信息，请参阅逐元素模式和矩阵模式。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** `'2' | '**' | '*/' | '*/*' | ...` |
| **默认值：** `'2'` |

### **Multiplication** — 逐元素 (.\*) 或矩阵 (\*) 乘法 `Element-wise(.*)`（默认）| `Matrix(*)`

指定模块执行 `Element-wise(.*)` 还是 `Matrix(*)` 乘法。

#### 编程用法

|  |
| --- |
| **模块参数：** `Multiplication` |
| **类型：** 字符向量 |
| **值：** `'Element-wise(.*)' | 'Matrix(*)'` |
| **默认值：** `'Element-wise(.*)'` |

### **Apply over** — 如何沿指定维度应用函数 `All dimensions`（默认）| `Specified dimension`

指定如何沿指定维度应用函数。

- `All dimensions` — 对所有维度的所有输入值应用函数。
- `Specified dimension` — 对指定维度的所有输入值应用函数。

例如，在此模型中，**Multiplication** 设置为 `Element-wise(.*)`，**Apply over** 设置为 `All dimensions`。模块返回所有维度中所有值的乘积。

以 Constant 模块值 [1 2 3;7 6 4] 作为 Product 模块输入的 2 维矩阵，该模块配置为所有维度

#### 依赖关系

要启用此参数，请将 **Number of inputs** 设置为 `*`，并将 **Multiplication** 设置为 `Element-wise (.*)`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CollapseMode` |
| **类型：** 字符向量 |
| **值：** `'All dimensions' | 'Specified dimension'` |
| **默认值：** `'All dimensions'` |

### **Dimension** — 沿其进行相乘的维度 `1`（默认）| 正整数

指定沿其进行相乘的维度，为正整数。例如，对于 2 维矩阵，`1` 对每列应用函数，`2` 对每行应用函数。

例如，在此模型中，**Multiplication** 设置为 `Element-wise(.*)`，**Apply over** 设置为 `Specified dimension`，**Dimension** 设置为 `2`。模块返回每一行中所有值的乘积。

以 Constant 模块值 [1 2 3;7 6 4] 作为 Product 模块输入的 2 维矩阵，该模块配置为维度 2

#### 依赖关系

要启用此参数：

- 将 **Number of inputs** 设置为 `*`
- 将 **Multiplication** 设置为 `Element-wise (.*)`
- 将 **Apply over** 设置为 `Specified dimension`

#### 编程用法

|  |
| --- |
| **模块参数：** `CollapseDim` |
| **类型：** 字符向量 |
| **值：** `'1' | '2' | ...` |
| **默认值：** `'1'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

### **Require all inputs to have the same data type** — 要求所有输入具有相同的数据类型 `off`（默认）| `on`

指定输入信号是否必须全部具有相同的数据类型。如果启用此参数，则当输入信号类型不同时，仿真期间将发生错误。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputSameDT` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。有关详细信息，请参阅控制信号的数据类型。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule` — Simulink® 选择一种数据类型，以在数值精度、性能和生成的代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。如果您更改嵌入式目标设置，内部规则所选择的数据类型可能会改变。例如，如果模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 `ASIC/FPGA` 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果将 `Unspecified (assume 32-bit Generic)`（即通用 32 位微处理器）指定为目标硬件，则输出数据类型为 `int32`。如果目标微处理器提供的字长都无法容纳输出范围，Simulink 软件将在诊断查看器中显示错误。
- `Inherit: Keep MSB`– Simulink 选择一种数据类型，该类型保持运算的完整范围，然后将输出的精度降低到适合嵌入式目标硬件的大小。

  **提示**

  要生成更高效的代码，请清除 **Saturate on integer overflow** 参数。

  此规则从不产生溢出。
- `Inherit: Match scaling`– Simulink 选择一种数据类型，其定标与输入类型的定标匹配。如果该类型的完整范围不适合嵌入式目标硬件，则范围会减小，从而产生适合嵌入式目标硬件的类型。此规则可能产生溢出。此规则不支持复数信号之间的乘法。

  `Inherit: Keep MSB` 和 `Inherit: Match scaling` 规则不支持复数信号或具有非零偏置的信号之间的乘法。这些规则仅支持两个输入之间的乘法和除法（`'**'`、`'*/'`、`'/*'`）、两个输入的矩阵乘法，以及向量两个元素的折叠乘积。

  软件并不总是能够同时优化代码效率和数值精度。如果内部规则不能满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用 `Inherit: Same as input` 的简单选择。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型提议数据类型。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用 `Inherit: Inherit via back propagation`，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例，请参阅 Signal Attributes 库中的 Data Type Propagation Examples 模块。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。
- `Inherit: Same as first input` — 使用第一个输入信号的数据类型。

#### 依赖关系

当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'Inherit: Inherit via internal rule` | `'Inherit: Keep MSB'`| `'Inherit: Match scaling'`| `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'`|`'int64'`|`'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**： `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。您可以选择：

`Ceiling`
:   将正数和负数向正无穷方向舍入。等效于 MATLAB
    `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入
    到最接近的偶数整数。等效于 Fixed-Point Designer™
    `convergent` 函数。

`Floor`
:   将正数和负数向负无穷方向舍入。等效于 MATLAB
    `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向
    正无穷方向舍入。等效于 Fixed-Point Designer
    `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将
    正数向正无穷方向舍入，将负数向
    负无穷方向舍入。等效于 Fixed-Point Designer
    `round` 函数。

`Simplest`
:   在向 floor 舍入和向零舍入之间进行选择，以生成
    尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB
    `fix` 函数。

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制
模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型所能表示的
  最小值或最大值。
- `off` — 溢出回绕到数据类型所能表示的
  相应值。

例如，有符号 8 位整数 `int8`
能表示的最大值是 127。任何大于此最大值的模块运算结果都会导致
8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值
  -128。
- 清除此参数时，软件将导致溢出的值解释为
  `int8`，这可能会产生非预期的结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时是 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中
  获得显式饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。
  清除此参数还有助于避免过度指定模块如何处理
  超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部
  运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。
  在这种情况下，代码生成器不会生成饱和
  代码。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### **Mode** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。
  选择 `Inherit` 会启用右侧的第二个菜单/文本框，
  您可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择
  `Built in` 会启用右侧的第二个菜单/文本框，
  您可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择
  `Fixed point` 会启用附加参数，
  您可以使用这些参数来指定定点数据类型。
- `Expression` — 求值为数据
  类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，
  您可以在其中输入表达式。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请点击 **Show data type
assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据
  类型覆盖设置，即从正在使用该信号的模块、
  `Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型
  覆盖设置，并使用为该信号指定的定点数据类型。

有关更多信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built
in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您在选择应用数据类型覆盖时
能够更好地控制模型中的数据类型。
例如，无论数据类型覆盖设置如何，您都可以使用此选项来确保数据类型满足
下游模块的要求。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示
正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为
  有符号。
- `Unsigned`，将定点数据指定为
  无符号。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed
point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关
更多信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或
负整数。有关更多信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Binary point`。

### **Scaling** — 定点数据的缩放方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的缩放方法，以避免溢出
条件并最小化量化误差。有关更多信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Slope** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关更多信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Slope and bias`。

### **Bias** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关更多
信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Slope and bias`。

## 所属库

Simulink / Commonly Used Blocks Simulink / Math Operations Simulink / Matrix Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

如果您拥有 Embedded Coder® 许可证，则可以生成 Halide 代码。有关更多信息，请参阅 Speed Up Generated Code Execution with Halide Code (Embedded Coder)。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Linear(default)` | 默认的 `Linear` 实现为 N 个输入生成 N 个操作（乘法器）的链。在生成的代码中生成乘积运算符 `*`。 |
| `ShiftAdd` | 通过使用多个移位和加法操作对定点类型执行乘积运算。该模块具有流水线实现，会在生成的代码中引入额外延迟。`ShiftAdd` 架构可映射到 ASIC 应用中的高效电路。该架构适用于没有 DSP 单元的目标 FPGA 板上的应用。不同字长的 `MAX` 延迟使用以下公式计算：`ceil(log2(min(in1WL,in2WL)))`。`in1WL` 是第一个输入字长，`in2WL` 是第二个输入字长。例如，如果两个输入的字长均为四，则 `MAX` 延迟为二。使用定点数据类型时，输入的字长必须小于 63。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。要使用此属性，请将 HDL 架构设置为 `Linear`。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。指定是将设计中的模块映射为定点类型和浮点类型的 `MAX`、`Min`、`Custom` 还是 `ZERO` 延迟。默认值为 `MAX`。另请参阅 LatencyStrategy (HDL Coder)。您可以通过将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 来控制迭代算法的流水线级数。有关更多信息，请参阅 Divide (HDL Coder)。 |
| **CustomLatency** | 要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅 LatencyStrategy (HDL Coder)。 |
| **IterationsPerPipeline** | 当您将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线级的迭代次数。要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。有关更多信息，请参阅 Divide (HDL Coder)。 |
| **DotProductStrategy** | 如果在矩阵乘法模式下使用该模块，则可以指定 **DotProductStrategy**。此设置决定您是要使用加法器和乘法器树来实现矩阵乘法，还是使用 Multiply-Accumulate 模块实现。默认值为 `Fully Parallel`。有关更多信息，请参阅 DotProductStrategy (HDL Coder)。当您使用 `Native Floating Point` 模式时，**DotProductStrategy** 必须设置为 `Fully Parallel`。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定您是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于可表示的最小浮点数的数，该最小浮点数在尾数中没有前导零。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min`、`Zero` 还是 `Custom`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会添加等于您为 **NFPCustomLatency** 设置指定的值的延迟。另请参阅 NFPCustomLatency (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**延迟详细信息**

该模块具有多周期实现，会在生成的代码中引入额外延迟。要查看添加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**原生浮点延迟**

| 运算符 | 浮点类型 | 延迟策略 | 延迟（周期） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| Product | Double | Min | 6 | 是 |
| Max | 9 |
| Single | Min | 6 |
| Max | 8 |
| Half | Min | 4 |
| Max | 7 |
| Divide | Double | Min | 31 | 是 |
| Max | 61 |
| Single | Min | 17 |
| Max | 32 |
| Half | Min | 10 |
| Max | 19 |
| Reciprocal | Double | Min | 6 | 是 |
| Max | 9 |
| Single | Min | 6 |
| Max | 8 |
| Half | Min | 4 |
| Max | 7 |

**复数数据支持**

默认（线性）实现支持复数数据。

不支持复数除法。有关 Product 模块在除法模式或倒数模式下的模块实现，请参阅 Divide 模块参考页上的 HDL Code Generation。

**复数乘法器**

HDL Coder 提供了一个用于复数乘法器的 Simulink 模型模板，专为 HDL 代码生成而设计。有关更多信息，请参阅 Complex Multiplier (HDL Coder)。

**优化**

您可以使用这些 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等效的资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 在其中将向量数据路径转换为标量数据路径（或转换为若干较小尺寸的向量数据路径）。 |

当使用 `ShiftAdd` 架构时，您可以对 Product、Divide 和 Reciprocal 模块应用共享或流式处理优化。

| 模块（输入） | 资源共享 | 流式处理 |
| --- | --- | --- |
| Product(\*) | 是 | 是 |
| Divide(/\* or \*/) | 是 | 是 |
| Reciprocal (/) | 是 | 否 |

当您对这些模块使用共享优化时，请确保将该模块包含在原子子系统内，并将 **Default parameter behavior** 配置参数设置为 `Inlined`。

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它在保持功能行为的同时移动设计中的现有延迟以减少关键路径。对于 Divide 和 Reciprocal 模块，HDL Coder 将流水线寄存器分布在模块周围，而不是模块内部。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**I/O 优化**

| 优化 | 描述 |
| --- | --- |
| Frame to Sample Conversion (HDL Coder) | 要优化设计所需的 I/O，请使用帧到样本转换。此优化将基于帧的向量或矩阵输入转换为较小尺寸的样本或像素，以便进行 HDL 代码生成，从而面向基于流的硬件，并减少处理大型输入和输出信号所需的 FPGA I/O。 |

**HDL 建模指南**

有关使用该模块的最佳实践，请参阅：

- 矩阵和向量的设计考虑 (HDL Coder)
- 面向 FPGA 目标的高效乘法和除法运算建模 (HDL Coder)
- 定点数据类型的舍入和饱和设置使用指南 (HDL Coder)

**限制**

- HDL 代码生成不支持该模块具有两个以上的输入。
- **Number of inputs** 模块参数为 `/*` 的 Product 模块执行除法，其中第二个输入除以第一个输入。此模式具有适用于 Divide 模块的相同限制。请参阅 HDL Code Generation。

### 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a：Product 和 Matrix Multiply 模块具有新的参数名称

对于 Product 和 Matrix Multiply 模块，**Multiply over** 参数已重命名为 **Apply over**。

## 描述

对标量和非标量进行乘法与除法，或对矩阵进行乘法与求逆

Product 模块输出两个输入相乘的结果：两个标量、一个标量和一个非标量，或两个具有相同维度的非标量。指定此行为的默认参数值为：

- **Multiplication：** `Element-wise(.*)`
- **Number of inputs：** `2`

此表显示了使用默认模块参数值时，Product 模块对不同维度输入相乘的输出。

| 输入和行为 | 示例 |
| --- | --- |
| **标量 X 标量** 输出两个输入的乘积。 |  |
| **标量 X 非标量** 输出一个与输入非标量具有相同维度的非标量。输出非标量的每个元素是输入标量与输入非标量对应元素的乘积。 |  |
| **非标量 X 非标量** 输出一个与输入具有相同维度的非标量。输出的每个元素是输入对应元素的乘积。 |  |

Divide 和 Product of Elements 模块是 Product 模块的变体。

- 有关 Divide 模块的信息，请参阅 Divide。
- 有关 Product of Elements 模块的信息，请参阅 Product of Elements。

Product 模块（或适当配置的 Divide 模块或 Product of Elements 模块）可以：

- 对任意数量的标量、向量或矩阵输入进行数值乘法和除法
- 对任意数量的矩阵输入执行矩阵乘法和除法

Product 模块执行标量乘法或矩阵乘法，具体取决于 **Multiplication** 参数的值。该模块接受一个或多个输入，具体取决于 **Number of inputs** 参数。**Number of inputs** 参数还指定要对每个输入执行的操作。

Product 模块可以输入标量、向量和矩阵的任意组合，只要要执行的操作具有数学上定义的结果。该模块对输入执行指定的操作，然后输出结果。

Product 模块有两种模式：*逐元素模式*，它逐个元素处理非标量输入；以及*矩阵模式*，它将非标量输入作为矩阵处理。

### 逐元素模式

当您将 **Multiplication** 设置为 `Element-wise(.*)` 时，Product 模块处于*逐元素模式*，在该模式下它对任何非标量输入的各个数值元素进行操作。MATLAB® 等效项是 `.*` 运算符。在逐元素模式下，Product 模块可以执行各种乘法、除法和算术求逆操作。

**Number of inputs** 参数的值控制存在多少个输入以及每个输入是相乘还是相除以形成输出。当 Product 模块处于逐元素模式且只有一个输入时，它在功能上等效于 Product of Elements 模块。当该模块有多个输入时，任何非标量输入必须具有相同的维度，并且该模块输出具有这些维度的非标量。为了计算输出，该模块首先将任何标量输入扩展为与这些非标量输入具有相同维度的非标量。

此表显示了使用 **Number of inputs** 参数的指定值时，Product 模块对不同维度输入相乘的输出。

| 参数值 | 示例 |
| --- | --- |
| **Number of inputs：** `2` |  |
| **Number of inputs：** `*/` |  |
| **Number of inputs：** `/**/` |  |
| **Number of inputs：**`**` |  |
| **Number of inputs：** `*/*` |  |

### 矩阵模式

当 **Multiplication** 参数的值为 `Matrix(*)` 时，Product 模块处于*矩阵模式*，在该模式下它将非标量输入作为矩阵处理。MATLAB 等效项是 `*` 运算符。在矩阵模式下，Product 模块可以对单个方阵求逆，或对任意数量的矩阵进行乘法和除法，只要这些矩阵的维度使结果在数学上有定义。

**Number of inputs** 参数的值控制存在多少个输入以及每个输入矩阵是相乘还是相除以形成输出。**Number of inputs** 的语法与逐元素模式下相同。两种模式之间的区别在于所发生的乘法和除法类型。

### 模块输入与模式之间的交互

Product 模块输入与其 **Multiplication** 模式之间的交互为：

- **`1` 或 `*` 或 `/`**

  该模块有一个输入端口。在逐元素模式下，该模块按 Product of Elements 模块所述处理输入。在矩阵模式下，如果参数值为 `1` 或 `*`，则该模块输出输入值。如果值为 `/`，则输入必须是方阵（包括作为退化情况的标量），并且该模块输出矩阵的逆。有关更多信息，请参阅逐元素模式和矩阵模式。
- **大于 1 的整数值**

  该模块具有由该整数值给出的输入数量。这些输入在逐元素模式或矩阵模式下相乘，具体由 **Multiplication** 参数指定。有关更多信息，请参阅逐元素模式和矩阵模式。
- **由两个或更多 `*` 和 `/` 字符组成的未加引号字符串**

  该模块具有由字符向量长度给出的输入数量。每个对应于 `*` 字符的输入被乘入输出。每个对应于 `/` 字符的输入被除入输出。这些操作在逐元素模式或矩阵模式下发生，具体由 **Multiplication** 参数指定。有关更多信息，请参阅逐元素模式和矩阵模式。

### 仿真与代码生成之间的预期差异

对于复数浮点输入的逐元素运算，仿真和代码生成结果在接近溢出的情况下可能会有所不同。尽管在配置参数对话框的**代码生成** > **接口**窗格中选择了**复数**，并且未选择**非有限数**，代码生成器不会为中间溢出生成特殊情形代码。此方法提高了不包含极值的一般情况下嵌入式运算的效率。如果输入可能包含极值，您必须显式管理这些情况。

当这些值在数学上无意义时，生成的代码可能不会产生与仿真相同的 `NaN` 和 `inf` 值模式。例如，如果仿真输出包含 `NaN`，生成的代码输出也包含 `NaN`，但不一定在同一位置。
