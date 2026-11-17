---
type: simulink-block
title: 'Logical Operator'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'logicaloperator'
documentation_source_path: '../simulink/slref/logicaloperator.html'
language: zh-CN
chinese_source: worker-translation
---

# Logical Operator

## 端口

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵

第一个输入信号，指定为标量、向量或矩阵。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — 第二个输入信号 标量 | 向量 | 矩阵

第二个输入信号，指定为标量、向量或矩阵。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — 第 N 个输入信号 标量 | 向量 | 矩阵

第 N 个输入信号，指定为标量、向量或矩阵。

#### 依赖关系

要启用额外的输入端口，请使用 **Number of input ports** 参数。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，由 0 和 1 组成，其维度与输入相同。您可以通过 **Require all inputs and output to have the same data type** 和 **Output data type** 参数控制输出数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Operator** — 逻辑运算符 `AND`（默认） | `OR` | `NAND` | `NOR` | `XOR` | `NXOR` | `NOT`

选择要应用于模块输入的逻辑运算符。

- `AND` — 如果所有输入均为 TRUE，则为 TRUE
- `OR` — 如果至少一个输入为 TRUE，则为 TRUE
- `NAND` — 如果至少一个输入为 FALSE，则为 TRUE
- `NOR` — 当没有输入为 TRUE 时，则为 TRUE
- `XOR` — 如果为 TRUE 的输入数量为奇数，则为 TRUE
- `NXOR` — 如果为 TRUE 的输入数量为偶数，则为 TRUE
- `NOT` — 如果输入为 FALSE，则为 TRUE

#### 编程用法

|  |
| --- |
| **模块参数：** `Operator` |
| **类型：** 字符向量 |
| **值：** `'AND' | 'OR' | 'NAND' | 'NOR' | 'XOR' | 'NXOR' | 'NOT'` |
| **默认值：** `'AND'` |

### **Number of input ports** — 输入数量 `2`（默认） | 正整数

将模块输入数量指定为正整数。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** 正整数 |
| **默认值：** `'2'` |

#### 依赖关系

当您将 **Operator** 设置为 `NOT` 时，此参数不可用。

### **Icon shape** — 图标形状 `rectangular`（默认） | `distinctive`

指定模块图标的形状。

- `rectangular` — 生成矩形模块，显示所选运算符的名称。
- `distinctive` — 使用 IEEE 标准规定的所选运算符图形符号。

#### 编程用法

|  |
| --- |
| **模块参数：** `IconShape` |
| **类型：** 字符向量 |
| **值：** `'rectangular' | 'distinctive'` |
| **默认值：** `'rectangular'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量或向量 |

### 数据类型

### **Require all inputs and output to have the same data type** — 要求所有端口具有相同的数据类型 `off`（默认） | `on`

要要求所有模块输入和输出具有相同的数据类型，请选中此复选框。清除此复选框时，输入和输出可以具有不同的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `AllPortsSameDT` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on` |
| **默认值：** `'off'` |

### **Output data type** — 输出数据类型 `boolean`（默认） | `Inherit: Logical (see Configuration Parameters: Optimization)` | `Inherit: Inherit via back propagation` | `fixdt(1,16)` | `<data type expression>`

指定输出数据类型。当您选择：

- `boolean` — 模块输出的数据类型为 `boolean`。
- `Inherit: Logical (see Configuration Parameters: Optimization)` — 模块使用 **Implement logic signals as Boolean data** 配置参数来指定输出数据类型（请参阅 Implement logic signals as Boolean data (vs. double)）。

  **注意**

  此选项支持在 `boolean` 选项可用之前创建的模型。对于新模型，请使用其他选项之一，最好是 `boolean`。
- `Inherit: Inherit via back propagation` — 模块继承数据类型。当您选择此选项时，输出数据类型和定标与下一个下游模块匹配。
- `fixdt(1,16)` — 模块输出具有指定的定点数据类型 `fixdt(1,16)`。

  **提示**

  **Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。
- `<data type expression>` — 模块输出具有您指定为数据类型表达式的数据类型，例如 `Simulink.NumericType`。

  **提示**

  要输入内置数据类型（`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`），请将表达式用单引号括起来。例如，输入 `'double'` 而不是 `double`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Logical (see Configuration Parameters: Optimization)'` | `'boolean'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **默认值：** `'boolean'` |

### **Mode** — 要指定的数据类别 `Built in`（默认） | `Inherit` | `Fixed point` | `Expression`

选择要指定的数据类别。

- `Built in` — 指定内置数据类型。选择 `Built in` 会启用 `boolean`。
- `Inherit` — 指定数据类型的继承规则。选择 `Inherit` 会启用 `Logical (see Configuration Parameters: Optimization)`。
- `Fixed point` — 指定定点数据类型。
- `Expression` — 指定可求值为数据类型的表达式。

#### 依赖关系

要启用此参数，请单击 **Show data type assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从正在使用该信号的模块、`Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为该信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您可以在应用数据类型覆盖时对模型中的数据类型进行更精细的控制。例如，无论数据类型覆盖设置如何，您都可以使用此选项来确保数据类型满足下游模块的要求。

### **Signedness** — 定点数据的有符号性 `Signed`（默认） | `Unsigned`

指定您希望定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认） | 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定标方法 `Integer`（默认）

指定对定点数据进行定标的方法，以避免溢出情况并最小化量化误差。指定 `Integer` 与指定二进制小数点位置并将小数长度设置为 `0` 的结果相同。

#### 依赖关系

要启用此参数，请单击 **Show data type assistant** 按钮，并将 **Mode** 设置为 `Fixed point`。

## 所属库

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / Logic and Bit Operations

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

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

对输入执行指定的逻辑运算

Logical Operator 模块对其输入执行指定的逻辑运算。如果输入值非零，则为 true（`1`）；如果输入值为零，则为 false（`0`）。

您可以通过 **Operator** 参数列表选择连接输入的布尔运算。如果您选择 `rectangular` 作为 **Icon shape** 属性，所选运算符的名称将显示在模块图标上。如果您选择 `distinctive` 作为 **Icon shape** 属性，所选运算符的名称不会显示在模块图标上。下表显示了支持的操作：

| 操作 | 描述 |
| --- | --- |
| AND | 如果所有输入均为 TRUE，则为 TRUE |
| OR | 如果至少一个输入为 TRUE，则为 TRUE |
| NAND | 如果至少一个输入为 FALSE，则为 TRUE |
| NOR | 当没有输入为 TRUE 时，则为 TRUE |
| XOR | 如果为 TRUE 的输入数量为奇数，则为 TRUE |
| NXOR | 如果为 TRUE 的输入数量为偶数，则为 TRUE |
| NOT | 如果输入为 FALSE，则为 TRUE |

如果您选择 `distinctive` 作为 **Icon shape**，模块外观将指示其功能。Simulink® 软件会为所选运算符显示符合 IEEE® Standard Graphic Symbols for Logic Functions 的独特形状。

要指定输入端口数量，请使用 **Number of input ports** 参数。输出类型使用 **Output data type** 参数指定。如果为 TRUE，则输出值为 `1`；如果为 FALSE，则输出值为 `0`。

**注意**

输出数据类型应能精确表示零。满足此条件的数据类型包括有符号和无符号整数，以及任何浮点数据类型。

输出的大小取决于输入向量大小和所选运算符：

- 如果模块有多个输入，任何非标量输入必须具有相同的维度。例如，如果任一输入是 2×2 数组，则所有其他非标量输入也必须是 2×2 数组。

  标量输入会扩展为与非标量输入具有相同的维度。

  如果模块有多个输入，则输出具有与输入相同的维度（在标量扩展之后），并且每个输出元素是将指定的逻辑运算应用于对应输入元素的结果。例如，如果指定的运算是 AND，且输入是 2×2 数组，则输出是一个 2×2 数组，其左上角元素是将 AND 应用于输入左上角元素的结果，依此类推。
- 对于单个向量输入，模块对该向量的所有元素应用该运算（NOT 运算符除外）。输出始终为标量。
- NOT 运算符仅接受一个输入，该输入可以是标量或向量。如果输入是向量，则输出是相同大小的向量，其中包含输入向量元素的逻辑补码。

当配置为多输入 XOR 门时，此模块按照 IEEE Standard for Logic Elements 的要求执行模二加法运算。
