---
type: simulink-block
title: 'Gain'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'gain'
documentation_source_path: 'slref/gain.html'
language: zh-CN
chinese_source: worker-translation
---

# Gain

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

Gain 模块接受实数或复数值的标量、向量或矩阵输入。Gain 模块支持定点数据类型。如果 Gain 模块的输入为实数且增益为复数，则输出为复数。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输入乘以增益 标量 | 向量 | 矩阵

Gain 模块输出输入乘以常量增益值的结果。当 Gain 模块的输入为实数且增益为复数时，输出为复数。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主要

### **Gain** — 用于乘以输入的值 `1`（默认）| 实数或复数值的标量、向量或矩阵

指定用于乘以输入的值。增益可以是实数或复数值的标量、向量或矩阵。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Gain` |
| **值：** | `'1'`（默认）| 带引号的实数或复数值的标量、向量或矩阵 |

### **Multiplication** — 指定乘法模式 `Element-wise(K.*u)`（默认）| `Matrix(K*u)` | `Matrix(u*K)` | `Matrix(K*u) (u vector)`

指定以下乘法模式之一：

- `Element-wise(K.*u)` — 输入的每个元素乘以增益的每个元素。如有必要，模块会执行扩展，使输入和增益具有相同的维度。
- `Matrix(K*u)` — 输入和增益进行矩阵乘法，输入作为第二个操作数。
- `Matrix(u*K)` — 输入和增益进行矩阵乘法，输入作为第一个操作数。
- `Matrix(K*u) (u vector)` — 输入和增益进行矩阵乘法，输入作为第二个操作数。此模式与 `Matrix(K*u)` 相同，只是维度的确定方式不同。

  假设 `K` 是一个 `m×n` 矩阵。`Matrix(K*u)(u vector)` 将输入设置为长度为 `n` 的向量，将输出设置为长度为 `m` 的向量。相比之下，`Matrix(K*u)` 使用传播来确定输入和输出的维度。对于 `m×n` 的增益矩阵，输入可以传播为 `n×q` 矩阵，输出则变为 `m×q` 矩阵。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Multiplication` |
| **值：** | `'Element-wise(K.*u)'`（默认）| `'Matrix(K*u)'` | `'Matrix(u*K)'` | `'Matrix(K*u) (u vector)'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行以下操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化（Embedded Coder）。

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

软件使用最大值执行以下操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围并启用仿真范围检查）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化（Embedded Coder）。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

当您选择继承选项时，模块会表现出以下行为：

- `Inherit: Inherit via internal rule` — 软件选择一种数据类型，在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成的代码大小。如果更改嵌入式目标设置，内部规则选择的数据类型可能会改变。例如，如果模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 `ASIC/FPGA` 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果将 `Unspecified (assume 32-bit Generic)`（即通用 32 位微处理器）指定为目标硬件，则输出数据类型为 `int32`。如果目标微处理器提供的字长都无法容纳输出范围，软件将在诊断查看器中显示错误。
- `Inherit: Keep MSB` — 软件选择一种数据类型，保持操作的完整范围，然后将输出的精度降低到适合嵌入式目标硬件的大小。

  **提示**

  要生成更高效的代码，请清除**Saturate on integer overflow**。

  此规则永远不会产生溢出。
- `Inherit: Match scaling` — 软件选择一种数据类型，其定标与输入类型的定标匹配。如果该类型的完整范围不适合嵌入式目标硬件，则范围会缩小，从而产生适合嵌入式目标硬件的类型。此规则可能会产生溢出。

  软件并不总是能够同时优化代码效率和数值精度。如果这些内部规则不能满足您对数值精度或性能的特定需求，请使用以下选项之一：

  - 显式指定输出数据类型。
  - 使用 `Inherit: Same as input` 的简单选择。
  - 显式指定默认数据类型（如 `fixdt(1,32,16)`），然后使用 Fixed-Point Tool 为您的模型提议数据类型。有关详细信息，请参阅 `fxptdlg`（Fixed-Point Designer）。
  - 要指定自己的继承规则，请使用 `Inherit: Inherit via back propagation` 并使用 Data Type Propagation 模块。有关如何使用此模块的示例，请参阅 Signal Attributes 库中的 Data Type Propagation Examples 模块。
- `Inherit: Inherit via back propagation` — 使用驱动模块的数据类型。
- `Inherit: Same as input` — 使用输入信号的数据类型。

#### 依赖关系

当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 **Inherit floating-point output type smaller than single precision** 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅使用锁定输出数据类型设置（Fixed-Point Designer）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选择此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误。
- 选中此参数时，饱和适用于模块上的每个内部操作，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **Mode** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。选择 `Inherit` 会在右侧启用第二个菜单/文本框，您可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择 `Built in` 会在右侧启用第二个菜单/文本框，您可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择 `Fixed point` 会启用可用于指定定点数据类型的附加参数。
- `Expression` — 求值为数据类型的表达式。选择 `Expression` 会在右侧启用第二个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请单击“显示数据类型助手”按钮 。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从使用该信号的 Simulink 中的模块、`Simulink.Signal` 对象或 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，在您应用数据类型覆盖时可以更好地控制模型中的数据类型。例如，无论数据类型覆盖设置如何，您都可以使用此选项确保数据类型满足下游模块的要求。

### **Signedness** — 指定有符号或无符号 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字的位大小 `16`（默认）| 从 0 到 32 的整数

指定保存量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Scaling** — 定点数据的定标方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出条件并最小化量化误差。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`。

### **Slope** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Slope and bias`。

### **Bias** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Slope and bias`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为
`Binary point`。

### 参数属性

### **Parameter minimum** — 指定增益的最小值 `[]`（默认）| 标量

指定增益的最小值。默认值为 `[]`
（未指定）。该软件使用此值来执行：

- 参数范围检查（请参阅为模块参数指定最小值和最大值）
- 定点数据类型的自动定标

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParamMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Parameter maximum** — 指定增益的最大值 `[]`（默认）| 标量

指定增益的最大值。默认值为 `[]`
（未指定）。该软件使用此值来执行：

- 参数范围检查（请参阅为模块参数指定最小值和最大值）
- 定点数据类型的自动定标

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParamMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Parameter data type** — 指定 Gain 参数的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Inherit from 'Gain'` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **Gain**
参数的数据类型。

将 **Parameter data type** 设置为
`Inherit: Inherit via internal rule` 可让
Gain 模块基于内部启发式方法选择数据类型，该方法会查看当前增益值并提供
全精度数据类型来表示当前增益值。当您更新
模型时，该软件会推导出一个数据类型，以高精度拟合增益值
`3` 且无范围损失。例如，使用此启发式方法，如果指定的增益值为
`3`，Gain 模块会推导出
所选数据类型为 `sfix32_En29`。因此，此
推导出的数据类型无法容纳大于 `4` 的值。
在仿真期间，如果您将增益值调整为 `6`，
所选数据类型中会发生溢出，行为将
不符合预期。

在使用此 **Parameter data
type** 设置调整参数时，请指定 **Parameter
Minimum** 和 **Parameter Maximum**
参数。这些设置会告知软件您在仿真期间所需的值范围，并允许软件提供具有足够范围的全
精度数据类型，以便在指定范围内安全地调整
增益值。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParamDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Same as input'` | `'Inherit: Inherit from 'Gain''` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**可调参数**

您可以在用于 HDL 代码生成的 Gain 模块中使用可调参数。有关详细信息，请参阅为可调参数生成 DUT 端口 (HDL Coder)。

**HDL 架构**

| `ConstMultiplierOptimization` | 描述 |
| --- | --- |
| `none`（*默认*） | 默认情况下，HDL Coder 不执行 CSD 或 FCSD 优化。为 Gain 模块生成的代码保留乘法器运算。 |
| `csd` | 当您指定此选项时，生成的代码使用规范有符号数字 (CSD) 技术减少模型使用的面积，同时保持或提高时钟速度。CSD 将乘法器运算替换为加法和减法运算。CSD 通过以最少非零位数表示二进制数，最小化常数乘法所需的加法运算次数。 |
| `fcsd` | 此选项使用因式分解 CSD (FCSD) 技术，该技术将乘法器运算替换为对操作数某些因子的移位和加/减法运算。这些因子通常是素数，但也可以是接近 2 的幂的数，这有利于面积缩减。使用 FCSD 可以实现更大的面积缩减，但代价是降低时钟速度。 |
| `auto` | 当您指定此选项时，编码器会在 CSD 或 FCSD 优化之间进行选择。编码器根据所需的加法器数量，选择产生最具面积效率实现的优化。当您指定 `auto` 时，编码器不使用乘法器，除非条件使得 CSD 或 FCSD 优化不可能（例如，如果设计使用浮点运算）。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstMultiplierOptimization** | 规范有符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**注意**

对于 **Gain** 参数的某些值，本机浮点会以不同方式实现算法，而不是使用乘法器。例如，如果您将 **Gain** 参数设置为 `1`，生成的模型使用一根线将输入传递到输出。如果您将 **Gain** 参数设置为 `-1`，生成的模型会显示一个 Unary Minus 模块，用于反转输入信号的极性。此实现减少了目标平台上的延迟和资源使用。

| 本机浮点 | |
| --- | --- |
| **HandleDenormals** | 指定您是否希望 HDL Coder 插入额外逻辑来处理设计中的非规格化数。非规格化数是幅值小于可表示的最小浮点数的数，该浮点数在尾数中没有前导零。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 添加的延迟等于您为 **NFPCustomLatency** 设置指定的值。另请参阅 NFPCustomLatency (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用量。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入乘以常数

Gain 模块将输入乘以常数值或增益。输入
和增益可以分别是标量、向量或矩阵。

您在 **Gain** 参数中指定增益的值。**Multiplication** 参数允许您指定逐元素或
矩阵乘法。对于矩阵乘法，此参数还允许您指示
被乘数的顺序。

增益在离线状态下使用舍入到最近和饱和从 double 转换为模块掩码中指定的数据类型。然后输入和增益相乘，并
使用指定的舍入和溢出模式将结果转换为输出数据类型。
