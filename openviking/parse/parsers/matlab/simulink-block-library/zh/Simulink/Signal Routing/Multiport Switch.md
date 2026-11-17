---
type: simulink-block
title: 'Multiport Switch'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'multiportswitch'
documentation_source_path: 'slref/multiportswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiport Switch

## 端口

### 输入

### **Port\_1** — 控制信号 标量

控制信号可以是 Simulink® 支持的任何数据类型，包括定点类型和枚举类型。当控制输入不是整数值时，模块通过向零舍入将值截断为整数。

有关枚举类型控制信号的信息，请参阅 Guidelines on Setting Parameters for Enumerated Control Port。

有关模块如何处理超出范围条件的信息，请参阅 How the Block Handles an Out-of-Range Control Input。

#### 限制

- 如果控制信号是数值类型，则控制信号不能为复数。
- 如果控制信号是枚举信号，模块使用底层整数的值来选择数据端口。
- 如果底层整数不对应任何数据端口，则发生错误。
- 如果控制输入是超出整数数据类型范围的浮点值，Multiport Switch 模块会发出运行时错误。此范围包括 `Inf` 和 `NaN`。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

### **1** — 第一个数据输入 标量 | 向量 | 矩阵 | N 维数组

第一个数据输入，指定为标量、向量、矩阵或 N 维数组。所有输入数据信号可以是 Simulink 支持的任何数据类型。

- 如果所有数据输入均为标量，则输出为标量
- 如果至少有一个数据输入是向量，则模块输出为向量。在这种情况下，模块会将任何标量输入扩展为向量。
- 如果任意两个非标量信号具有不同的维数或不同的维度长度，请选中 **Allow different data input sizes** 复选框。有关详细信息，请参阅 Use Data Inputs That Have Different Dimensions
- 如果任何数据信号是枚举类型，则所有其他信号必须为相同的枚举类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **2** — 第二个数据输入 标量 | 向量 | 矩阵 | N 维数组

第二个数据输入，指定为标量、向量、矩阵或 N 维数组。所有输入数据信号可以是 Simulink 支持的任何数据类型。

- 如果所有数据输入均为标量，则输出为标量
- 如果至少有一个数据输入是向量，则模块输出为向量。在这种情况下，模块会将任何标量输入扩展为向量。
- 如果任意两个非标量信号具有不同的维数或不同的维度长度，请选中 **Allow different data input sizes** 复选框。有关详细信息，请参阅 Use Data Inputs That Have Different Dimensions
- 如果任何数据信号是枚举类型，则所有其他信号必须为相同的枚举类型。

#### 依赖关系

要启用此端口，请将 **Number of data ports** 设置为大于 1 的整数。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **N** — 第 N 个数据输入 标量 | 向量 | 矩阵 | N 维数组

第 N 个数据输入，指定为标量、向量、矩阵或 N 维数组。所有输入数据信号可以是 Simulink 支持的任何数据类型。

- 如果所有数据输入均为标量，则输出为标量
- 如果至少有一个数据输入是向量，则模块输出为向量。在这种情况下，模块会将任何标量输入扩展为向量。
- 如果任意两个非标量信号具有不同的维数或不同的维度长度，请选中 **Allow different data input sizes** 复选框。有关详细信息，请参阅 Use Data Inputs That Have Different Dimensions
- 如果任何数据信号是枚举类型，则所有其他信号必须为相同的枚举类型。

#### 依赖关系

要启用第 *N* 个输入端口，请将 **Number of data ports** 设置为大于或等于 *N* 的整数值。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `string` | `image`

### **\*** — 超出范围输入的数据端口 标量 | 向量 | 矩阵 | N 维数组

用于超出范围控制信号输入的数据输入端口，指定为标量、向量、矩阵或 N 维数组。所有输入数据信号可以是 Simulink 支持的任何数据类型。如果任何数据信号是枚举类型，则所有其他信号必须为相同的枚举类型。如果任意两个信号具有不同的维数或不同的维度长度，请选中 **Allow different data input sizes** 复选框。有关详细信息，请参阅 Use Data Inputs That Have Different Dimensions。

#### 依赖关系

要为超出范围的控制信号输入创建额外的数据端口，请将 **Data port for default case** 设置为 `Additional data port`。当您将 **Data port for default case** 设置为 `Last data port` 时，模块在控制信号值与任何数据端口索引都不匹配时使用最后一个数据端口进行输出。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 基于控制信号值选择的数据输入 标量 | 向量 | 矩阵 | N 维数组

模块根据控制信号值选择并输出其中一个数据输入。输出具有与对应数据输入相同的维度。输出数据类型是需要最大内存空间的输入端口的类型。当您选中 **Allow different data input sizes** 复选框时，模块的输出为可变大小信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `string` | `image`

## 参数

### 主要

### **Data port order** — 数据输入端口的排序类型 `One-based contiguous` | `Zero-based contiguous` | `Specify indices`

指定数据输入端口的排序类型。

- `Zero-based contiguous` — 模块使用从零开始的索引对连续数据端口进行排序。这是 Index Vector 模块的默认值。
- `One-based contiguous` — 模块使用从一开始的索引对连续数据端口进行排序。这是 Multiport Switch 模块的默认值
- `Specify indices` — 模块使用非连续索引对数据端口进行排序。

#### 提示

- 当控制端口为枚举类型时，请选择 `Specify indices`。
- 如果选择 `Zero-based contiguous` 或 `One-based contiguous`，请验证控制端口不是枚举类型。此配置已弃用并会产生错误。您可以对模型运行 Upgrade Advisor，将此配置的每个 Multiport Switch 模块替换为显式指定数据端口索引的模块。请参阅 Model Upgrades。
- 避免模块在仿真或代码生成中包含未使用的数据端口。当控制端口为定点或内置数据类型时，请验证所有数据端口索引均可由该类型表示。否则，将出现以下模块行为。

  | 如果模块具有未使用的数据端口且数据端口顺序为： | 模块将产生： |
  | --- | --- |
  | `Zero-based contiguous` 或 `One-based contiguous` | 警告 |
  | `Specify indices` | 错误 |

#### 依赖关系

选择 `Zero-based contiguous` 或 `One-based contiguous` 会启用 **Number of data ports** 参数。

选择 `Specify indices` 会启用 **Data port indices** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataPortOrder` |
| **类型：** 字符向量 |
| **值：** `'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **默认值：** `'One-based contiguous'` (Multiport Switch) | `'Zero-based contiguous'` (Index Vector) |

### **Number of data ports** — 数据输入端口数量 `1` | `3` | 1 到 65535 之间的整数

指定模块的数据输入端口数量。输入端口总数为您指定的数量，加上一个用于控制信号输入的端口，如果您将 **Data port for default case** 设置为 `Additional data port`，则再加一个。

#### 依赖关系

要启用此参数，请将 **Data port order** 设置为 `Zero-based contiguous` 或 `One-based contiguous`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** 1 到 65536 之间的整数 |
| **默认值：** `'3'` (Multiport Switch) | `'1'` (Index Vector) |

### **Data port indices** — 数据端口的索引数组 `{1,2,3}`（默认）| 索引数组

指定数据端口的索引数组。模块图标会更改以匹配您指定的数据端口索引。

#### 提示

- 要指定与枚举类型所有值对应的索引数组，请输入 `enumeration('name of the type')`。

  例如，如果 `MyColors` 是枚举类型的名称，则 `enumeration('MyColors')` 是有效条目。
- 要输入枚举类型的特定值，请使用 *`type_name.enumerated_name`* 格式。不要输入底层整数值。

  例如，`enumeration({MyColors.Red, MyColors.Green, MyColors.Blue})` 是有效条目。
- 要指示多个值映射到一个数据端口，请使用方括号。

  例如，以下条目均有效：

  - `enumeration({MyColors.Red, MyColors.Green, [MyColors.Blue, MyColors.Yellow]})`
  - `enumeration({[3,5],0,18})`
- 如果控制端口为定点或内置数据类型，则 **Data port indices** 的值必须可由该类型表示。否则，编译时会显示错误以提醒您存在未使用的数据端口。
- 如果控制端口为枚举数据类型，则 **Data port indices** 的值必须为该类型的枚举值。
- 如果 **Data port indices** 包含枚举类型的值，则控制端口必须为该数据类型。

#### 依赖关系

要启用此参数，请将 **Data port order** 设置为 `Specify indices`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataPortIndices` |
| **类型：** 字符向量 |
| **值：** 索引数组 |
| **默认值：** `'{1,2,3}'` |

### **Data port for default case** — 用于超出范围输入的端口 `Last data port`（默认）| `Additional data port`

指定是使用最后一个数据端口处理超出范围的输入，还是使用额外的端口。端口名称旁边的星号（\*）表示当控制端口值与任何数据端口索引都不匹配时模块使用的端口。

- `Last data port` — 当控制端口值与任何数据端口索引都不匹配时，模块使用最后一个数据端口进行输出。
- `Additional data port` — 当控制端口值与任何数据端口索引都不匹配时，模块使用额外的数据端口进行输出。

#### 提示

如果您将此参数设置为 `Additional data port` 且 **Number of data ports** 为 `3`，则模块上的输入端口数为 5。第一个输入是控制端口，接下来的三个输入是数据端口，第五个输入是用于超出范围输入的默认端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataPortForDefault` |
| **类型：** 字符向量 |
| **值：** `'Last data port' | 'Additional data port'` |
| **默认值：** `'Last data port'` |

### **Diagnostic for default case** — 控制端口值与数据端口索引不匹配时的诊断操作 `Error`（默认）| `Warning` | `None`

指定当控制端口值与任何数据端口索引都不匹配时要采取的诊断操作。

- `None` — 不产生任何响应。
- `Warning` — 显示警告并继续仿真。
- `Error` — 终止仿真并显示错误。在这种情况下，**Data port for default case** 仅用于代码生成，不用于仿真。

有关详细信息，请参阅 How the Block Handles an Out-of-Range Control Input。

#### 编程用法

|  |
| --- |
| **模块参数：** `DiagnosticForDefault` |
| **类型：** 字符向量 |
| **值：** `'None' | 'Warning' | 'Error'` |
| **默认值：** `'Error'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

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

### **Require all data port inputs to have the same data type** — 要求所有输入具有相同的数据类型 `off`（默认）| `on`

选中此复选框可要求所有数据输入端口具有相同的数据类型。清除此复选框时，模块允许数据端口输入具有不同的数据类型。

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
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

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
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first data input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Simulink.ImageType(480,640,3)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如
`Simulink.NumericType`。

当您选择继承选项时，模块的行为如下：

- `Inherit: Inherit via internal
  rule`—Simulink 选择一种数据类型以平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。如果您更改嵌入式目标设置，内部规则所选择的数据类型可能会改变。软件并不总是能够同时优化代码效率和数值精度。如果内部规则不满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 显式指定默认数据类型，例如
    `fixdt(1,32,16)`，然后使用定点工具为您的模型提议数据类型。有关更多信息，请参阅 `fxptdlg`（Fixed-Point Designer）。
  - 要指定您自己的继承规则，请使用
    `Inherit: Inherit via back
    propagation`，然后使用 Data Type
    Propagation 模块。有关如何使用此模块的示例，请参阅 Signal Attributes 库中的 Data Type Propagation Examples 模块。
- `Inherit: Inherit via back propagation` —
  使用驱动模块的数据类型。
- `Inherit: Same as first data input` — 使用
  第一个数据输入端口的数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **默认**：`'Inherit: Inherit via internal rule'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项以锁定此模块的输出数据类型设置，防止被定点工具和定点顾问更改。有关更多信息，请参阅 Use Lock Output Data Type Setting（Fixed-Point Designer）。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |

### **整数舍入模式** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数均向正无穷方向
    舍入。等效于
    MATLAB®
    `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示
    值。如果出现平局，则舍入到最接近的偶数
    整数。等效于 Fixed-Point Designer™
    `convergent` 函数。

`Floor`
:   将正数和负数均向负无穷方向
    舍入。等效于
    MATLAB
    `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示
    值。如果出现平局，则向正无穷方向
    舍入。等效于 Fixed-Point Designer
    `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示
    值。如果出现平局，则将正数向正无穷方向
    舍入，将负数向负无穷方向舍入。等效于
    Fixed-Point Designer
    `round` 函数。

`Simplest`
:   自动在向 floor 舍入和向零
    舍入之间进行选择，以生成尽可能高效的
    舍入代码。

`Zero`
:   将数字向零方向舍入。等效于
    MATLAB
    `fix` 函数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认**：`'Floor'` |

#### 另请参阅

有关更多信息，请参阅舍入模式（Fixed-Point Designer）。

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型能够表示的
  最小值或最大值。
- `off` — 溢出回绕到数据类型能够表示的
  相应值。

例如，有符号 8 位整数 `int8`
能够表示的最大值是 127。任何大于此最大值的模块运算结果都会导致
8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。
  类似地，模块输出饱和于最小值
  -128。
- 清除此参数时，软件将导致溢出的
  值解释为 `int8`，这可能会产生意外结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时是 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成代码中
  具有显式饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于
  避免过度指定模块如何处理超出范围的信号。有关更多
  信息，请参阅排查信号范围错误。
- 当您选中此参数时，饱和适用于模块上的每个内部
  运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种
  情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **允许不同的数据输入大小（导致可变大小输出信号）** — 允许不同大小的输入信号 `off`（默认）| `on`

选中此复选框以允许不同大小的输入信号。

- `On` — 允许不同大小的输入信号，并将
  输入信号大小传播到输出信号。在此模式下，模块
  产生可变大小输出信号。
- `Off` — 要求所有非标量数据输入信号
  具有相同的大小。

#### 程序化使用

|  |
| --- |
| **参数：** `AllowDiffInputSizes` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

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
  您可以使用这些参数来指定定点数据类型。
- `Expression` — 求值为数据类型的
  表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，
  您可以在其中输入表达式。

有关更多信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请点击 **显示数据类型
助手** 按钮。

### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据
  类型覆盖设置，即从正在使用该信号的模块、
  `Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型
  覆盖设置，并使用为该信号指定的定点数据类型。

有关更多信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Built
in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，在您应用数据类型覆盖时
提供了对模型中数据类型的更大控制。例如，您可以使用此选项来确保数据类型满足
下游模块的要求，而不管数据类型覆盖设置如何。

### **符号性** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示
正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为
  有符号。
- `Unsigned`，将定点数据指定为
  无符号。

有关更多信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed
point`。

### **定标** — 定点数据的定标方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出
条件并最小化量化误差。有关更多信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为
`Fixed point`。

### **字长** — 保存量化整数的字的位大小 `16`（默认）| 从 0 到 32 的整数

指定保存量化整数的字的位大小。有关
更多信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为
`Fixed point`。

### **小数长度** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或
负整数。有关更多信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **定标** 设置为
`Binary point`。

### **斜率** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关更多信息，请参阅
指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **定标** 设置为
`Slope and bias`。

### **偏置** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关更多
信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **定标** 设置为
`Slope and bias`。

## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **CodingStyle** | 指定生成 HDL 代码时使用 case 语句还是 if-else 语句。默认情况下，HDL Coder 生成 if-else 语句。另请参阅 CodingStyle（HDL Coder）。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline（HDL Coder）。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline（HDL Coder）。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline（HDL Coder）。 |

| 本机浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy（HDL Coder）。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**使用指定索引模式设置数据端口索引**

您可以使用指定索引模式为输入端口指定数据端口索引。要使用指定索引模式配置 Multiport Switch 模块，请将
**数据端口顺序** 模块参数设置为 `Specify
indices`。然后，在 **数据
端口索引** 模块参数中输入端口索引。对于面向 HDL 代码
生成的目标模型，您可以在指定索引模式下为控制输入使用以下输入数据类型：

- 定点和浮点类型
- 有符号和无符号整数类型
- 枚举类型
- 向量、矩阵和总线类型

**使用枚举类型作为端口索引**

您可以将 **数据端口顺序** 设置为 **指定
索引**，并为 **数据
端口索引** 输入枚举值。例如，您可以将 Enumerated
Constant 模块连接到 Multiport Switch 控制
端口，并使用枚举类型作为数据端口索引。

**限制**

您必须避免在控制端口使用 `NaN` 或超出范围的值。这可能导致验证模型中的仿真不匹配。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a：当输入具有浮点值时，Multiport Switch 模块出现运行时错误

当第一个端口中的控制信号具有超出整数数据类型范围的浮点值时，Multiport Switch 模块现在会发出运行时错误。此范围包括 `Inf` 和
`NaN`。

## 描述

根据控制信号选择输出信号

Multiport Switch 模块确定将模块的多个输入中的哪一个传递到输出。该模块根据第一个输入的值做出此决定。第一个输入是控制输入，其余输入是数据输入。控制输入的值决定哪个数据输入传递到输出。

Multiport Switch 和 Index Vector 模块是同一模块的替代配置。

- Multiport Switch — 根据控制信号选择输出信号。
- Index Vector — 根据第一个输入的值在不同输入之间切换输出。

下表总结了 Multiport Switch 如何解释控制输入并确定传递到输出的数据输入。

| 控制输入 | 截断 | 数据端口顺序的设置 | 仿真期间的模块行为 | |
| --- | --- | --- | --- | --- |
| 索引以选择数据输入 | 超出范围条件 |
| 整数值 | 无 | `Zero-based contiguous` | 从零开始的索引 | 控制输入小于 `0` 或大于数据输入数量减一。 |
| `One-based contiguous` | 从一开始的索引 | 控制输入小于 `1` 或大于数据输入数量。 |
| `Specify indices` | 你指定的索引 | 控制输入不对应任何指定的数据端口索引。 |
| 非整数值 | 模块通过向零舍入将值截断为整数。 | `Zero-based contiguous` | 从零开始的索引 | 截断后的控制输入小于 `0` 或大于数据输入数量减一。 |
| `One-based contiguous` | 从一开始的索引 | 截断后的控制输入小于 `1` 或大于数据输入数量。 |
| `Specify indices` | 你指定的索引 | 截断后的控制输入不对应任何指定的数据端口索引。 |

有关模块如何处理超出范围条件的信息，请参阅模块如何处理超出范围的控制输入。

### Multiport Switch 配置为 Index Vector 模块

Index Vector 是 Multiport Switch 模块的一种特殊配置，其中你指定一个数据输入，并且控制输入从零开始。模块输出是输入向量中索引与控制输入匹配的元素。例如，如果输入向量为 `[18 15 17 10]`，控制输入为 `3`，则索引 3（从零开始）匹配的元素是 10，该值成为输出值。

要将 Multiport Switch 模块配置为 Index Vector 模块，请将 **Number of data ports** 设置为 `1`，将 **Data port order** 设置为 `Zero-based contiguous`。

### 模块如何处理超出范围的控制输入

对于值小于 `intmax(‘int32’)` 的整数输入，当该值不匹配任何数据端口索引时，该输入超出范围。对于非整数值的控制输入，当*截断后的*值不匹配任何数据端口索引时，该输入超出范围。在这两种情况下，模块行为取决于你对 **Data port for default case** 和 **Diagnostic for default case** 的设置。

**注意**

如果控制输入大于 `intmax(‘int32’)`，模块会将输入值包装为整数。

**仿真行为**

以下行为仅适用于模型的仿真。

| 默认情况的数据端口 | 默认情况的诊断 | | |
| --- | --- | --- | --- |
| 无 | 警告 | 错误 |
| `Last data port` | 使用最后一个数据端口，不报告任何警告或错误。 | 使用最后一个数据端口并报告警告。 | 报告错误并停止仿真。 |
| `Additional data port` | 使用带有 `*` 标签的附加数据端口，不报告任何警告或错误。 | 使用带有 `*` 标签的附加数据端口并报告警告。 | 报告错误并停止仿真。 |

**代码生成行为**

以下行为适用于模型的代码生成。

| 默认情况的数据端口 | 默认情况的诊断 | | |
| --- | --- | --- | --- |
| 无 | 警告 | 错误 |
| `Last data port` | 使用最后一个数据端口。 | 使用最后一个数据端口。 | 使用最后一个数据端口。 |
| `Additional data port` | 使用带有 `*` 标签的附加数据端口。 | 使用带有 `*` 标签的附加数据端口。 | 使用带有 `*` 标签的附加数据端口。 |

### 使用具有不同维度的数据输入

如果两个信号具有不同的维度数量或不同的维度长度，你可以将这些信号用作 Multiport Switch 模块的数据输入。在模块对话框中，选择参数 **Allow different data input sizes**。在这种情况下，模块的输出是可变大小信号。如果你不选择此参数，模块将生成错误。

有关该参数的更多信息，请参阅 Allow different data input sizes (Results in variable-size output signal)。有关可变大小信号的更多信息，请参阅 Variable-Size Signal Basics。

### 确定模块行为的规则

你通过 **Number of data ports** 指定数据输入的数量。

- 如果将 **Number of data ports** 设置为 1，模块表现为*索引选择器*或*索引向量*，而不是多端口开关。有关更多详细信息，请参阅 Multiport Switch 配置为 Index Vector 模块。
- 如果将 **Number of data ports** 设置为大于 1 的整数，模块表现为多端口开关。模块输出是对应于控制输入值的数据输入。如果至少有一个数据输入是向量，则模块输出是向量。在这种情况下，模块会将任何标量输入扩展为向量。
- 如果所有数据输入都是标量，则输出是标量。

### 为枚举控制端口设置参数的指南

当 Multiport Switch 模块上的控制端口为枚举类型时，请遵循以下指南：

| 场景 | 操作 | 理由 |
| --- | --- | --- |
| 枚举类型包含表示无效、超出范围或未初始化值的值。 | - 将 **Data port order** 设置为 `Specify indices`。 - 将 **Data port indices** 设置为对最后一个数据端口使用此值。 - 将 **Data port for default case** 设置为 `Last data port`。 | 此模块配置处理枚举类型显式表示的无效值。 |
| 枚举类型仅包含有效的枚举值。但是，数据输入端口可能获取枚举类型的无效值。 | - 将 **Data port for default case** 设置为 `Additional data port`。 | 此模块配置处理枚举类型未显式表示的无效值。 |
| 枚举类型仅包含有效的枚举值。数据输入端口永远不会获取枚举类型的无效值。 | - 将 **Data port for default case** 设置为 `Last data port`。 - 将 **Diagnostic for default case** 设置为 `None`。 | 此模块配置避免不必要的诊断操作。 |
| 模块并非对枚举类型的每个值都有数据输入端口。 | - 将 **Data port for default case** 设置为 `Additional data port`。 | 此模块配置处理没有数据输入端口的枚举值以及无效值。 |
