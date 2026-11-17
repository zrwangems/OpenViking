---
type: simulink-block
title: 'Relational Operator'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'relationaloperator'
documentation_source_path: 'slref/relationaloperator.html'
language: zh-CN
chinese_source: worker-translation
---

# Relational Operator

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_2
  summary: 第二个输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵

第一个输入信号，指定为标量、向量或矩阵。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — 第二个输入信号 标量 | 向量 | 矩阵

第二个输入信号，指定为标量、向量或矩阵。

#### 依赖关系

要启用此端口，请将 **Relational operator** 设置为
`==`、`~=`、
`<`、
`<=`、
`>=` 或
`>`。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，由零和一组成，其维度与输入相同。您可以通过 **Output
data type** 参数控制输出数据类型。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Relational operator
  summary: 关系运算符 <=（默认）| ~= | == | < | >= | > | isInf | isNaN | isFinite
  group: 主要
  block_parameter: Operator
  type: 字符向量
  values: '''=='' | ''~='' | ''<'' | ''<='' | ''>='' | ''>'' | ''isInf'' | ''isNaN'' | ''isFinite'''
  default: '''<='''
- name: Enable zero-crossing detection
  summary: 启用过零检测 on（默认）| off
  group: 主要
  block_parameter: ZeroCross
  type: 字符向量、字符串
  values: '''on'' | ''off'''
  default: '''on'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的时间间隔 -1（默认）| 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Require all inputs to have the same data type
  summary: 要求所有输入具有相同的数据类型 off（默认）| on
  group: 数据类型
  block_parameter: InputSameDT
  type: 字符向量
  values: '''off'' | ''on'
  default: '''off'''
- name: Output data type
  summary: '输出数据类型 boolean（默认）| Inherit: Logical (see Configuration Parameters: Optimization) | Inherit: Inherit via back
    propagation | fixdt(1,16) | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Logical (see Configuration Parameters: Optimization)'' | ''boolean'' | ''fixdt(1,16)'' | ''<data type
    expression>'''
  default: '''boolean'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Simplest（默认）| Convergent | Floor | Nearest | Round | Ceiling | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: 字符向量
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Simplest'''
- name: Mode
  summary: 要指定的数据类别 Built in（默认）| Inherit | Fixed point | Expression
  group: 数据类型
- name: Data type override
  summary: 为此信号指定数据类型覆盖模式 Inherit | Off
  group: 数据类型
- name: Signedness
  summary: 定点数据的有符号性 Signed（默认）| Unsigned
  group: 数据类型
- name: Word length
  summary: 保存量化整数的字长位数 16（默认）| 0 到 32 的整数
  group: 数据类型
- name: Scaling
  summary: 定标方法 Integer（默认）
  group: 数据类型
```

### 主要

### **Relational operator** — 关系运算符 `<=`（默认）| `~=` | `==` | `<` | `>=` | `>` | `isInf` | `isNaN` | `isFinite`

指定用于比较两个输入或确定一个输入信号类型的操作。

- `==` — 如果第一个输入等于第二个输入，则为真
- `~=` — 如果第一个输入不等于第二个输入，则为真
- `<` — 如果第一个输入小于第二个输入，则为真
- `<=` — 如果第一个输入小于或等于第二个输入，则为真
- `>=` — 如果第一个输入大于或等于第二个输入，则为真
- `>` — 如果第一个输入大于第二个输入，则为真
- `isInf` — 如果输入为 `Inf`，则为真
- `isNaN` — 如果输入为 `NaN`，则为真
- `isFinite` — 如果输入为有限值，则为真

`==` 和 `~=` 在仿真和代码生成中支持复数。

#### 编程用法

|  |
| --- |
| **模块参数：** `Operator` |
| **类型：** 字符向量 |
| **值：** `'==' | '~=' | '<' | '<=' | '>=' | '>' | 'isInf' | 'isNaN' | 'isFinite'` |
| **默认值：** `'<='` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选择以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程用法

|  |
| --- |
| **参数：** `ZeroCross` |
| **类型：** 字符向量、字符串 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

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

### 数据类型

### **Require all inputs to have the same data type** — 要求所有输入具有相同的数据类型 `off`（默认）| `on`

要要求所有模块输入具有相同的数据类型，请选中此复选框。清除此复选框时，输入可以具有不同的数据类型。

#### 依赖关系

当您将 **Relational operator** 设置为 `isInf`、`isNaN` 或 `isFinite` 时，此复选框不可用，因为在这些模式下，模块只有一个输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputSameDT` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on` |
| **默认值：** `'off'` |

### **Output data type** — 输出数据类型 `boolean`（默认）| `Inherit: Logical (see Configuration Parameters: Optimization)` | `Inherit: Inherit via back propagation` | `fixdt(1,16)` | `<data type expression>`

指定输出数据类型。当您选择：

- `boolean` — 模块输出的数据类型为 `boolean`。
- `Inherit: Logical (see Configuration Parameters:
  Optimization)` — 模块使用 **Implement logic
  signals as Boolean data** 配置参数来指定输出数据类型（请参阅 Implement logic signals as Boolean data (vs. double)）。

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

### **Integer rounding mode** — 定点运算的舍入模式 `Simplest`（默认）| `Convergent` | `Floor` | `Nearest` | `Round` | `Ceiling` | `Zero`

指定定点运算的舍入模式。您可以选择：

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
:   在向 floor 舍入和向零舍入之间进行选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：** `'Simplest'` |

### **Mode** — 要指定的数据类别 `Built in`（默认）| `Inherit` | `Fixed point` | `Expression`

选择要指定的数据类别。

- `Built in` — 指定内置数据类型。选择 `Built in` 会启用 `boolean`。
- `Inherit` — 指定数据类型的继承规则。选择 `Inherit` 会启用 `Logical
  (see Configuration Parameters: Optimization)`。
- `Fixed point` — 指定定点数据类型。
- `Expression` — 指定求值为数据类型的表达式。

#### 依赖关系

要启用此参数，请单击 **Show data type
assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从使用该信号的模块、`Simulink.Signal` 对象或 Simulink® 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built
in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您可以在应用数据类型覆盖时对模型中的数据类型进行更好的控制。例如，您可以使用此选项来确保数据类型满足下游模块的要求，而不管数据类型覆盖设置如何。

### **Signedness** — 定点数据的有符号性 `Signed`（默认）| `Unsigned`

指定您希望定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定标方法 `Integer`（默认）

指定对定点数据进行定标的方法，以避免溢出情况并最小化量化误差。指定 `Integer` 与指定二进制小数点位置并将小数长度设置为 `0` 的结果相同。

#### 依赖关系

要启用此参数，请单击 **Show data type
assistant** 按钮并将 **Mode** 设置为 `Fixed point`。
## 所属库

Simulink / Commonly Used Blocks Simulink / Logic and Bit Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 本机浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 添加的延迟等于您为 **NFPCustomLatency** 设置指定的值。另请参阅 NFPCustomLatency (HDL Coder)。 |

**复数数据支持**

`~=` 和 `==` 运算符在仿真和代码生成中受支持。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入执行指定的关系运算

Relational Operator 模块对输入执行指定的关系运算。您为 **Relational operator** 参数选择的值决定模块接受一个还是两个输入信号。

### 双输入模式

默认情况下，Relational Operator 模块使用您指定的 **Relational operator** 参数比较两个输入。第一个输入对应于顶部输入端口，第二个输入对应于底部输入端口。（有关各种模块方向的端口顺序说明，请参阅 Identify Port Location on Rotated or Flipped Block。）

您可以在双输入模式下指定以下操作之一：

| 操作 | 描述 |
| --- | --- |
| `==` | 如果第一个输入等于第二个输入，则为真 |
| `~=` | 如果第一个输入不等于第二个输入，则为真 |
| `<` | 如果第一个输入小于第二个输入，则为真 |
| `<=` | 如果第一个输入小于或等于第二个输入，则为真 |
| `>=` | 如果第一个输入大于或等于第二个输入，则为真 |
| `>` | 如果第一个输入大于第二个输入，则为真 |

您可以将输入指定为标量、数组或标量与数组的组合。

| 对于... | 输出为... |
| --- | --- |
| 标量输入 | 标量 |
| 数组输入 | 具有相同维度的数组，其中每个元素是输入数组逐元素比较的结果 |
| 混合标量和数组输入 | 数组，其中每个元素是标量与对应数组元素比较的结果 |

如果关系运算可以在硬件板上高效且准确地表示，则使用此高效表示。否则，使用溢出饱和和指定的舍入模式将两个操作数转换为公共类型。

您可以使用 **Output data type** 参数指定输出数据类型。输出为真时等于 `1`，为假时等于 `0`。

**提示**

选择能够精确表示零的输出数据类型。满足此条件的数据类型包括有符号和无符号整数以及任何浮点数据类型。

### 单输入模式

当您为 **Relational operator** 选择以下操作之一时，模块切换到单输入模式。

| 操作 | 描述 |
| --- | --- |
| `isInf` | 如果输入为 `Inf`，则为真 |
| `isNaN` | 如果输入为 `NaN`，则为真 |
| `isFinite` | 如果输入为有限值，则为真 |

对于非浮点输入，模块产生以下输出。

| 数据类型 | 操作 | 模块输出 |
| --- | --- | --- |
| - 定点 - Boolean - 内置整数 | `isInf` | 假 |
| `isNaN` | 假 |
| `isFinite` | 真 |

### 数据类型传播规则

当您的模块具有一个或多个数据类型未指定的输入端口时，以下规则适用于数据类型传播。

| 当模块处于... | 并且... | 模块使用... |
| --- | --- | --- |
| 双输入模式 | 两个输入端口的数据类型均未指定 | `double` 作为两个输入的默认数据类型 |
| 一个输入端口的数据类型未指定 | 来自已指定输入端口的默认数据类型作为另一个端口的默认数据类型 |
| 单输入模式 | 输入端口的数据类型未指定 | `double` 作为输入的默认数据类型 |
