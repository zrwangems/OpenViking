---
type: simulink-block
title: 'Divide'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'divide'
documentation_source_path: 'slref/divide.html'
language: zh-CN
chinese_source: worker-translation
---

# Divide

## 端口
```yaml
ports:
- name: X
  summary: 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: ÷
  summary: 要相除或求逆的输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 要相乘或相除的第一个输入 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_N
  summary: 要相乘或相除的第 N 个输入 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: \*
  summary: 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Inv
  summary: 要相除或求逆的输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 通过对输入进行乘法、除法或求逆运算计算得到的输出 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

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

### **Port\_1** — 要相乘或相除的第一个输入 标量 | 向量 | 矩阵 | N 维数组

要相乘或相除的第一个输入，以标量、向量、矩阵或 N 维数组形式提供。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — 要相乘或相除的第 N 个输入 标量 | 向量 | 矩阵 | N 维数组

要相乘或相除的第 N 个输入，以标量、向量、矩阵或 N 维数组形式提供。

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

### **Port\_1** — 通过对输入进行乘法、除法或求逆运算计算得到的输出 标量 | 向量 | 矩阵 | N 维数组

通过对输入进行乘法、除法或求逆运算计算得到的输出。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 控制输入数量和运算类型 */（默认）| 正整数标量 | 每个输入端口对应 * 或 /
  group: 主要
  block_parameter: Inputs
  type: 字符向量
  values: '''2'' | ''*'' | '''' | ''*/'' | ''*/*'' | ...'
  default: '''*/'''
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
  summary: 沿其进行乘法的维度 1（默认）| 正整数
  group: 主要
  block_parameter: CollapseDim
  type: 字符向量
  values: '''1'' | ''2'' | ...'
  default: '''1'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的时间间隔 -1（默认）| 标量 | 向量
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
  type: character vector
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
  summary: 指定定点数据类型的小数长度 0（默认）| 标量整数
  group: 信号属性
- name: Scaling
  summary: 定点数据的定标方法 Best precision（默认）| Binary point | Slope and bias
  group: 信号属性
- name: Slope
  summary: 指定定点数据类型的斜率 2^0（默认）| 正实值标量
  group: 信号属性
- name: Bias
  summary: 指定定点数据类型的偏置 0（默认）| 实值标量
  group: 信号属性
```

### 主要

### **Number of inputs** — 控制输入数量和运算类型 `*/`（默认）| 正整数标量 | 每个输入端口对应 `*` 或 `/`

控制模块的两个属性：

- 模块上的输入端口数量
- 每个输入是乘入还是除入输出

当您指定：

- **`1` 或 `*` 或 `/`**

  模块有一个输入端口。在逐元素模式下，模块按照 Product of Elements 模块所述处理输入。在矩阵模式下，如果参数值为 `1` 或 `*`，模块输出输入值。如果值为 `/`，则输入必须是方阵（包括标量作为退化情况），模块输出矩阵的逆。有关详细信息，请参阅逐元素模式和矩阵模式。
- **大于 1 的整数值**

  模块具有由该整数值给定的输入数量。这些输入按照 **Multiplication** 参数指定的方式在逐元素模式或矩阵模式下相乘。有关详细信息，请参阅逐元素模式和矩阵模式。
- **由两个或更多 `*` 和 `/` 字符组成的未加引号字符串**

  模块具有由字符向量长度给定的输入数量。每个对应 `*` 字符的输入被乘入输出。每个对应 `/` 字符的输入被除入输出。这些运算按照 **Multiplication** 参数指定的方式在逐元素模式或矩阵模式下进行。有关详细信息，请参阅逐元素模式和矩阵模式。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** `'2' | '*' | '**' | '*/' | '*/*' | ...` |
| **默认值：** `'*/'` |

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

以 Constant 模块值 [1 2 3;7 6 4] 作为 Product 模块输入的 2D 矩阵，该模块配置为所有维度

#### 依赖关系

要启用此参数，请将 **Number of inputs** 设置为 `*`，并将 **Multiplication** 设置为 `Element-wise (.*)`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CollapseMode` |
| **类型：** 字符向量 |
| **值：** `'All dimensions' | 'Specified dimension'` |
| **默认值：** `'All dimensions'` |

### **Dimension** — 沿其进行乘法的维度 `1`（默认）| 正整数

指定沿其进行乘法的维度，以正整数表示。例如，对于 2 维矩阵，`1` 对每列应用函数，`2` 对每行应用函数。

例如，在此模型中，**Multiplication** 设置为 `Element-wise(.*)`，**Apply over** 设置为 `Specified dimension`，**Dimension** 设置为 `2`。模块返回每行中所有值的乘积。

以 Constant 模块值 [1 2 3;7 6 4] 作为 Product 模块输入的 2D 矩阵，该模块配置为维度 2

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

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

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
- 优化您从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。有关详细信息，请参阅控制信号的数据类型。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal rule` — Simulink® 选择一种数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。如果您更改嵌入式目标设置，内部规则选择的数据类型可能会改变。例如，如果模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 `ASIC/FPGA` 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定 `Unspecified (assume 32-bit Generic)`，即通用 32 位微处理器，作为目标硬件，则输出数据类型为 `int32`。如果目标微处理器提供的字长都无法容纳输出范围，Simulink 软件会在诊断查看器中显示错误。

  软件并不总是能够同时优化代码效率和数值精度。如果内部规则不能满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用 `Inherit: Same as input` 的简单选择。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型建议数据类型。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
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
| **值**： `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
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
:   将正数和负数向正无穷方向舍入。等效于 MATLAB®
    `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，
    则舍入到最接近的偶数整数。等效于
    Fixed-Point Designer™
    `convergent` 函数。

`Floor`
:   将正数和负数向负无穷方向舍入。等效于 MATLAB
    `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，
    则向正无穷方向舍入。等效于
    Fixed-Point Designer
    `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，
    则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效
    于 Fixed-Point Designer
    `round` 函数。

`Simplest`
:   在向 floor 舍入和向
    zero 舍入之间进行选择，以生成尽可能高效的舍入代码。此舍入模式受 **Hardware
    Implementation** 窗格上以下配置参数的影响。

    - 如果 **Signed integer division rounds
      to** 参数设置为
      `Zero` 或
      `Undefined`，
      则 `Simplest` 解析为
      zero。
    - 如果 **Signed integer division rounds
      to** 参数设置为
      `Floor`，
      则 `Simplest` 解析为
      `floor`。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB
    `fix` 函数。

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，
请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型能够表示的最小值或最大值。
- `off` — 溢出回绕到数据类型能够表示的适当值。

例如，有符号 8 位整数 `int8` 能够表示的最大值是 127。任何大于此最大值的模块运算结果都会导致
8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值
  -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中提供显式饱和保护时，
  请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于
  避免过度指定模块如何处理超出范围的信号。有关
  详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部
  运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种
  情况下，代码生成器不会生成饱和代码。

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

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请点击 **Show data type
assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据
  类型覆盖设置，即从正在使用该信号的 Simulink 中的模块、
  `Simulink.Signal` 对象或 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型
  覆盖设置，并使用为该信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built
in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您能够在应用数据类型覆盖时
对模型中的数据类型进行更好的控制。
例如，您可以使用此选项确保数据类型满足
下游模块的要求，而不管数据类型覆盖设置如何。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示
正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为
  有符号。
- `Unsigned`，将定点数据指定为
  无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed
point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关
详细信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或
负整数。有关详细信息，请参阅 指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Binary point`。

### **Scaling** — 定点数据的定标方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出
条件并最小化量化误差。有关详细信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Slope** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关详细信息，请参阅
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

**仿真与代码生成之间的预期差异**

以下条件可能导致仿真与生成代码之间产生不同结果：

- Divide 模块输入包含
  `NaN` 或 `inf` 值
- Divide 模块在执行期间生成 `NaN` 或
  `inf`

此差异是由于非有限 `NaN` 或
`inf` 值造成的。在这种情况下，请检查您的模型
配置并消除产生 `NaN`
或 `inf` 的条件。

**代码优化**

Simulink
Coder™ 构建过程为矩阵求逆和
除法运算提供高效的代码。下表描述了各项优势以及每项优势何时
可用。

| 优势 | 小矩阵（2×2 到 5×5） | 中等矩阵（6×6 到 20×20） | 大矩阵（大于 20×20） |
| --- | --- | --- | --- |
| 与 R2011a 及更早版本相比，代码执行时间更快 | 是 | 否 | 是 |
| 与 R2011a 及更早版本相比，减少 ROM 和 RAM 使用量 | 是，对于实数值 | 是，对于实数值 | 是，对于实数值 |
| 变量重用 | 是 | 是 | 是 |
| 死代码消除 | 是 | 是 | 是 |
| 常量折叠 | 是 | 是 | 是 |
| 表达式折叠 | 是 | 是 | 是 |
| 与 MATLAB Coder 结果一致 | 是 | 是 | 是 |

对于具有三个或更多不同维度输入的模块，代码
可能包含额外的缓冲区来存储中间
结果的临时变量。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

要执行 HDL 优化的除法运算，请将 Product 模块连接到 Divide 模块，并将 Divide 模块的 **Number of Inputs 参数**设置为 `/`。

**HDL 架构**

Divide 模块与 **Number of Inputs** 设置为 `*/` 的 Product 模块相同。

| 架构 | 描述 |
| --- | --- |
| `ShiftAdd`（默认） | 使用非恢复除法算法执行除法运算，该算法执行多次移位和加法运算来计算商。当 **Architecture** 设置为 `ShiftAdd` 时，模块使用流水线架构将计算分解为多个阶段。这种流水线设计在 HDL 实现中引入延迟。您可以使用 **LatencyStrategy** HDL 模块属性指定延迟。默认情况下，**LatencyStrategy** 设置为 `Max`。要实现无延迟的模块，请将 **LatencyStrategy** 设置为 `Zero`。 |

**倒数模式**

当 **Number of Inputs** 设置为 `/` 时，Divide 模块处于倒数模式。

| 架构 | 描述 |
| --- | --- |
| `ShiftAdd`（默认） | 使用非恢复除法算法执行倒数运算，该算法执行多次移位和加法运算来计算倒数。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。指定是否将设计中的模块映射为定点类型和浮点类型的 `MAX`、`Min`、`Custom` 或 `ZERO` 延迟。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。您可以通过将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 来控制迭代算法的流水线阶段。有关更多信息，请参阅 Divide (HDL Coder)。 |
| **CustomLatency** | 要启用此属性，请将 HDL 架构设置为 `ShiftAdd`。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定 `ZERO` 到 `MAX` 之间的自定义延迟值。另请参阅 LatencyStrategy (HDL Coder)。 |
| **IterationsPerPipeline** | 当您将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线阶段的迭代次数。有关更多信息，请参阅 Divide (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入额外逻辑来处理设计中的非规格化数。非规格化数是幅值小于最小浮点数的数，该最小浮点数可以在尾数中没有前导零的情况下表示。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用量。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |
| **DivisionAlgorithm** | 指定使用 Radix-2 还是 Radix-4 算法来执行浮点除法。Radix-2 模式在延迟和频率之间提供权衡。Radix-4 模式在延迟和资源使用之间提供权衡。有关更多信息，请参阅 DivisionAlgorithm (HDL Coder)。 |

**延迟详细信息**

此模块具有多周期实现，会在生成代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**原生浮点延迟**

| 运算符 | 浮点类型 | 延迟策略 | 延迟（周期数） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
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

**定点延迟**

| 运算符 | 额外延迟周期数 | 延迟策略支持 | 自定义延迟支持 |
| --- | --- | --- | --- |
| Divide | 取决于输入和输出的字长和小数长度。有关更多信息，请参阅 `HDLMathLib` Divide (HDL Coder)。 | 是 | 是 |
| Reciprocal | 取决于输入和输出的字长和小数长度。有关更多信息，请参阅 `HDLMathLib` Reciprocal (HDL Coder)。 | 是 | 是 |

**模块参数配置**

HDL 代码生成支持 `ShiftAdd` 中 `divide (*/)` 和 `reciprocal (/)` 运算的不同输出数据类型。您可以对这些模块使用以下输出数据类型：

- `Inherit: Inherit via internal rule`
- `Inherit: Keep MSB​`
- `Inherit: Match scaling​`
- `Inherit: Inherit via back propagation`​
- `Inherit: Same as first input​`
- `Integer types (uint8,int8,uint16,int16,uint32,int32,uint64,int64)​`
- `Fixed point types​`
- `Floating-point types`

您可以对这些模块使用以下整数舍入模式：

| 模块 | 整数舍入模式 |
| --- | --- |
| Divide | - `Zero` - `Simplest` - `Ceiling` *（自 R2025a 起）* - `Convergent` *（自 R2025a 起）* - `Floor` *（自 R2025a 起）* - `Nearest` *（自 R2025a 起）* - `Round` *（自 R2025a 起）* |
| Reciprocal | - `Zero` - `Ceiling` *（自 R2025a 起）* - `Convergent` *（自 R2025a 起）* - `Floor` *（自 R2025a 起）* - `Nearest` *（自 R2025a 起）* - `Round` *（自 R2025a 起）* - `Simplest` *（自 R2025a 起）* |

**注意**

当您将生成的 HDL 代码部署到目标硬件时，请确保将配置参数对话框的 **Hardware Implementation** 窗格中的 **signed integer division rounds to** 参数设置为 `Zero` 或 `Floor`。

**复数数据支持**

此模块不支持复数信号除法的代码生成。

**优化**

您可以使用以下 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 识别多个功能等效的资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 将向量数据路径转换为标量数据路径（或转换为多个较小尺寸的向量数据路径）。 |

您可以使用 `ShiftAdd` 架构对 Divide 和 Reciprocal 模块应用共享或流式处理优化。

| 模块（输入） | 资源共享 | 流式处理 |
| --- | --- | --- |
| Divide(/\* 或 \*/) | 是 | 是 |
| Reciprocal (/) | 是 | 否 |

当您对这些模块使用共享优化时，请确保将模块包含在原子子系统中，并将 **Default parameter behavior** 配置参数设置为 `Inlined`。

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。对于 Divide 和 Reciprocal 模块，HDL Coder 将流水线寄存器分布在模块周围而不是模块内部。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**I/O 优化**

| 优化 | 描述 |
| --- | --- |
| Frame to Sample Conversion (HDL Coder) | 要优化设计所需的 I/O，请使用帧到样本转换。此优化将基于帧的向量或矩阵输入转换为较小尺寸的样本或像素，用于 HDL 代码生成，以面向基于流的硬件并减少处理大型输入和输出信号所需的 FPGA I/O。 |

**HDL 建模指南**

有关使用该模块的最佳实践，请参阅：

- 矩阵和向量的设计考虑 (HDL Coder)
- 面向 FPGA 目标的高效乘法和除法运算建模 (HDL Coder)
- 定点数据类型的舍入和饱和设置使用指南 (HDL Coder)

**限制**

当您在倒数模式下使用 Divide 模块时，以下限制适用：

- 当您使用定点类型时，输入和输出必须是标量。要使用向量输入，请使用浮点类型输入和输出。
- 您必须在模块上选择 **Saturate on integer overflow** 选项。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a：Divide 和 Reciprocal 模块使用 ShiftAdd 作为默认架构

Divide 和 Reciprocal 模块的 **Architecture** HDL 模块属性现在默认为 `ShiftAdd`。使用 `ShiftAdd` 设置生成的代码比其他现有架构更适合硬件。

以下架构设置已从 Divide 和 Reciprocal 模块的 **Architecture** HDL 模块属性中移除：

| 模块 | 架构设置 |
| --- | --- |
| Divide | `Linear` |
| Reciprocal | `Linear` `ReciprocalRsqrtBasedNewtonSingleRate` |

线性架构使用除法运算符 (/) 来实现模块，不支持流水线。这导致长组合路径和较低性能。移位加法架构使用流水线架构将计算分解为多个阶段。这种流水线设计在 HDL 实现中引入延迟。要实现无延迟的模块，请将 **LatencyStrategy** 设置为 `Zero`。

## 描述

将一个输入除以另一个输入

Divide 模块输出其第一个输入除以第二个输入的结果。输入可以是标量、一个标量和一个非标量，或两个具有相同维度的非标量。当所有端口具有相同的 single 或 double 数据类型时，此模块仅支持除法端口上的复数输入值。

Divide 模块在功能上是一个 Product 模块，具有两个预设的模块参数值：

- **Multiplication —** `Element-wise(.*)`
- **Number of Inputs —** `*/`

为这两个参数中的任一个设置非默认值可以将 Divide 模块变为在功能上等同于 Product 模块或 Product of Elements 模块。
