---
type: simulink-block
title: 'Product of Elements'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'productofelements'
documentation_source_path: '../simulink/slref/productofelements.html'
language: zh-CN
chinese_source: worker-translation
---

# Product of Elements

## 端口
```yaml
ports:
- name: Port_1
  summary: 要相乘或相除的第一个输入 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_N
  summary: 要相乘或相除的第 N 个输入 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: X
  summary: 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: ÷
  summary: 要相除或求逆的输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 通过对输入进行相乘、相除或求逆计算得到的输出 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

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

要启用一个或多个 **X** 端口，请为 **Number of inputs** 参数指定一个或多个 `*` 字符。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **÷** — 要相除或求逆的输入信号 标量 | 向量 | 矩阵 | N 维数组

用于相除或求逆运算的输入信号。

#### 依赖关系

要启用一个或多个 **÷** 端口，请为 **Number of inputs** 参数指定一个或多个 `/` 字符。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 通过对输入进行相乘、相除或求逆计算得到的输出 标量 | 向量 | 矩阵 | N 维数组

通过对输入进行相乘、相除或求逆计算得到的输出。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 控制输入数量和运算类型 *（默认）| 正整数标量 | 每个输入端口的 * 或 /
  group: 主要
  block_parameter: Inputs
  type: 字符向量
  values: '''2'' | ''*'' | '''' | ''*/'' | ''*/*'' | ...'
  default: '''*'''
- name: Multiplication
  summary: 逐元素 (.\*) 或矩阵 (\*) 乘法 Element-wise(.*)（默认）| Matrix(*)
  group: 主要
  block_parameter: Multiplication
  type: 字符向量
  values: '''Element-wise(.*)'' | ''Matrix(*)'''
  default: '''Element-wise(.*)'''
- name: Apply over
  summary: 如何沿指定维度应用函数 All dimensions（默认）| Specified dimension
  group: 主要
  block_parameter: CollapseMode
  type: 字符向量
  values: '''All dimensions'' | ''Specified dimension'''
  default: '''All dimensions'''
- name: Dimension
  summary: 要沿其相乘的维度 1（默认）| 正整数
  group: 主要
  block_parameter: CollapseDim
  type: 字符向量
  values: '''1'' | ''2'' | ...'
  default: '''1'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Require all inputs to have the same data type
  summary: 要求所有输入具有相同的数据类型 off（默认）| on
  group: 信号属性
  block_parameter: InputSameDT
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output minimum
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: Output data type
  summary: '指定输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Inherit via back propagation | Inherit: Same as first
    input | double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0)
    | fixdt(1,16,2^0,0) | <data type expression>'
  group: 信号属性
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule | ''Inherit: Same as first input'' | ''Inherit: Inherit via back propagation''
    | ''double'' | ''single'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64''
    | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖 Output data type 的选项 off（默认）| on
  group: 信号属性
  block_parameter: LockScale
  values: '''off''（默认）| ''on'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 信号属性
  block_parameter: RndMeth
  type: 字符向量
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 信号属性
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
- name: Mode
  summary: 选择数据类型模式 Inherit（默认）| Built in | Fixed Point
  group: 信号属性
- name: Data type override
  summary: 为此信号指定数据类型覆盖模式 Inherit | Off
  group: 信号属性
- name: Signedness
  summary: 指定有符号或无符号 Signed（默认）| Unsigned
  group: 信号属性
- name: Word length
  summary: 保存量化整数的字长位数 16（默认）| 0 到 32 的整数
  group: 信号属性
- name: Fraction length
  summary: 为定点数据类型指定小数长度 0（默认）| 标量整数
  group: 信号属性
- name: Scaling
  summary: 定点数据的缩放方法 Best precision（默认）| Binary point | Slope and bias
  group: 信号属性
- name: Slope
  summary: 为定点数据类型指定斜率 2^0（默认）| 正实值标量
  group: 信号属性
- name: Bias
  summary: 为定点数据类型指定偏置 0（默认）| 实值标量
  group: 信号属性
```

### 主要

### **Number of inputs** — 控制输入数量和运算类型 `*`（默认）| 正整数标量 | 每个输入端口的 `*` 或 `/`

控制模块的两个属性：

- 模块上的输入端口数量
- 每个输入是相乘还是相除到输出中

当您指定：

- **`1` 或 `*` 或 `/`**

  模块有一个输入端口。在逐元素模式下，模块按 Product of Elements 模块所述处理输入。在矩阵模式下，如果参数值为 `1` 或 `*`，模块输出输入值。如果值为 `/`，输入必须是方阵（包括作为退化情况的标量），模块输出矩阵的逆。有关详细信息，请参阅逐元素模式和矩阵模式。
- **大于 1 的整数值**

  模块具有由该整数值给出的输入数量。输入按 **Multiplication** 参数指定的方式在逐元素模式或矩阵模式下相乘。有关详细信息，请参阅逐元素模式和矩阵模式。
- **由两个或更多 `*` 和 `/` 字符组成的未加引号字符串**

  模块具有由字符向量长度给出的输入数量。每个对应 `*` 字符的输入相乘到输出中。每个对应 `/` 字符的输入相除到输出中。运算按 **Multiplication** 参数指定的方式在逐元素模式或矩阵模式下进行。有关详细信息，请参阅逐元素模式和矩阵模式。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** `'2' | '*' | '**' | '*/' | '*/*' | ...` |
| **默认值：** `'*'` |

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

  例如，在此模型中，**Multiplication** 设置为 `Element-wise(.*)`，**Apply over** 设置为 `All dimensions`。模块返回所有维度中所有值的乘积。

  2D 矩阵，Constant 模块值为 [1 2 3;7 6 4]，作为配置为所有维度的 Product 模块的输入

  当您选择 `All dimensions` 并选择配置参数 **Use algorithms optimized for row-major array layout** 时，Simulink® 为仿真启用行主序算法。要生成行主序代码，请将配置参数 **Array layout** (Simulink Coder) 设置为 `Row-major`，并选择 **Use algorithms optimized for row-major array layout**。列主序和行主序算法仅在乘法顺序上有所不同。在某些情况下，由于对同一数据集的操作函数顺序，您可能会在列主序和行主序算法的输出中遇到轻微的数值差异。
- `Specified dimensions` — 对指定维度的所有输入值应用函数。

#### 依赖关系

要启用此参数，请将 **Number of inputs** 设置为 `*`，并将 **Multiplication** 设置为 `Element-wise (.*)`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CollapseMode` |
| **类型：** 字符向量 |
| **值：** `'All dimensions' | 'Specified dimension'` |
| **默认值：** `'All dimensions'` |

### **Dimension** — 要沿其相乘的维度 `1`（默认）| 正整数

指定要沿其相乘的维度，为正整数。例如，对于 2 维矩阵，`1` 将函数应用于每一列，`2` 将函数应用于每一行。

例如，在此模型中，**Multiplication** 设置为 `Element-wise(.*)`，**Apply over** 设置为 `Specified dimension`，**Dimension** 设置为 `2`。模块返回每一行中所有值的乘积。

2D 矩阵，Constant 模块值为 [1 2 3;7 6 4]，作为配置为维度 2 的 Product 模块的输入

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

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

### **Require all inputs to have the same data type** — 要求所有输入具有相同的数据类型 `off`（默认）| `on`

指定输入信号是否必须全部具有相同的数据类型。如果启用此参数，则当输入信号类型不同时，仿真期间会发生错误。

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

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

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

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。有关详细信息，请参阅 Control Data Types of Signals。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule` — Simulink 选择一种数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。如果您更改嵌入式目标设置，内部规则选择的数据类型可能会改变。例如，如果模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 `ASIC/FPGA` 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定 `Unspecified (assume 32-bit Generic)`，即通用 32 位微处理器，作为目标硬件，则输出数据类型为 `int32`。如果目标微处理器提供的字长都无法容纳输出范围，Simulink 软件会在诊断查看器中显示错误。

  软件并不总是能够同时优化代码效率和数值精度。如果内部规则不满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用 `Inherit: Same as input` 的简单选择。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型提议数据类型。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用 `Inherit: Inherit via back propagation`，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例可在 Signal Attributes 库的 Data Type Propagation Examples 模块中找到。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。
- `Inherit: Same as first input` — 使用第一个输入信号的数据类型。

#### 依赖关系

当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**： `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。您可以选择：

`Ceiling`
:   将正数和负数向正无穷方向舍入。等效于 MATLAB® 的 `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ 的 `convergent` 函数。

`Floor`
:   将正数和负数向负无穷方向舍入。等效于 MATLAB 的 `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer 的 `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer 的 `round` 函数。

`Simplest`
:   在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：** `'Floor'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型能够表示的最小值或最大值。
- `off` — 溢出回绕到数据类型能够表示的相应值。

例如，有符号 8 位整数 `int8` 能够表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和在 127。类似地，模块输出饱和在最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式添加饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### **Mode** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。选择 `Inherit` 会启用右侧的第二个菜单/文本框，您可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择 `Built in` 会启用右侧的第二个菜单/文本框，您可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择 `Fixed point` 会启用附加参数，您可以使用这些参数指定定点数据类型。
- `Expression` — 求值为数据类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请点击 **Show data type assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从正在使用该信号的模块、`Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图中继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为该信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您能够在应用数据类型覆盖时对模型中的数据类型进行更精细的控制。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 为定点数据类型指定小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Binary point`。

### **Scaling** — 定点数据的缩放方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的缩放方法，以避免溢出条件并最小化量化误差。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Slope** — 为定点数据类型指定斜率 `2^0`（默认）| 正实值标量

为定点数据类型指定斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

### **Bias** — 为定点数据类型指定偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。
## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

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

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

HDL Coder 支持 `Tree` 架构，用于具有单个多元素向量输入的 Product 或 Product of Elements 模块。

| 架构 | 描述 |
| --- | --- |
| `Linear`（默认） | 生成用于计算乘积之和的线性加法器链。 |
| `Tree` | 生成用于计算乘积之和的树形加法器结构。 |

**HDL 模块属性**

如果在矩阵乘法模式下使用该模块，可以指定 **DotProductStrategy**。此设置决定您是要使用加法器和乘法器树来实现矩阵乘法，还是使用 Multiply-Accumulate 模块实现。默认值为 `Fully Parallel`。

**注意**

当您使用 `Native Floating Point` 模式时，**DotProductStrategy** 必须设置为 `Fully Parallel`。

有关详细信息，请参阅 DotProductStrategy (HDL Coder)。

另请参阅 Design Considerations for Matrices and Vectors (HDL Coder)。

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | 指定您是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于尾数中没有前导零时可表示的最小浮点数的数。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是将设计中的模块映射为 `inherit`、`Max`、`Min`、`Zero` 还是 `Custom` 以用于浮点运算符。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 添加的延迟等于您为 **NFPCustomLatency** 设置指定的值。另请参阅 NFPCustomLatency (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 器件上的 DSP 使用量。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**复数数据支持**

默认（线性）实现支持复数数据。

不支持复数除法。有关 Product 模块在除法模式或倒数模式下的模块实现，请参阅 Divide 模块参考页面上的 HDL Code Generation。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

复制或反转一个标量输入，或将一个非标量输入折叠

Product of Elements 模块输入一个标量、向量或矩阵。您可以使用该模块来：

- 原样复制一个标量输入
- 反转一个标量输入（用 1 除以它）
- 通过将所有元素相乘或对元素连续取倒数，将向量或矩阵折叠为标量
- 使用以下选项之一将矩阵折叠为向量：

  - 将每一行或每一列的元素相乘
  - 对每一行或每一列的元素连续取倒数

Product of Elements 模块在功能上是一个具有两个预设参数值的 Product 模块：

- **Multiplication**：`Element-wise(.*)`
- **Number of inputs**：`*`

为其中任一参数设置非默认值，都可以使 Product of Elements 模块在功能上等同于 Product 模块或 Divide 模块。
