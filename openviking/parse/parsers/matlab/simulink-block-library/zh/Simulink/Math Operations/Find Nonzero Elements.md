---
type: simulink-block
title: 'Find Nonzero Elements'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'findnonzeroelements'
documentation_source_path: 'slref/findnonzeroelements.html'
language: zh-CN
chinese_source: worker-translation
---

# Find Nonzero Elements

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 非零元素的索引 可变大小信号
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_2
  summary: 非零元素的值 可变大小信号
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

模块从中查找所有非零元素的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 非零元素的索引 可变大小信号

Find Nonzero Elements 模块将非零元素的索引输出为可变大小信号。您可以使用 **Output data type** 模块参数控制输出的数据类型。

#### 依赖关系

默认情况下，模块从第一个输出端口输出线性索引。当您将 **Index output format** 更改为 `Subscripts` 时，模块改为以子脚本形式提供二维或更高维信号的元素索引。在此模式下，您必须指定 **Number of input dimensions**，模块会为每个维度创建一个单独的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — 非零元素的值 可变大小信号

Find 模块可以选择性地将所有非零元素的值输出为可变大小信号。

#### 依赖关系

要启用此端口，请选择 **Show output port for nonzero input values**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Index output format
  summary: 非零元素索引的格式 Linear indices（默认）| Subscripts
  group: 主要
  block_parameter: IndexOutputFormat
  type: 字符向量
  values: '''Linear indices'' | ''Subscripts'''
  default: '''Linear indices'''
- name: Number of input dimensions
  summary: 输入信号的维度数 1（默认）| 标量
  group: 主要
  block_parameter: NumberOfInputDimensions
  type: 字符向量
  values: 标量
  default: '''1'''
- name: Index mode
  summary: 指定从零开始或从一开始的索引 Zero-based（默认）| One-based
  group: 主要
  block_parameter: IndexMode
  type: 字符向量
  values: '''Zero-based'' | ''One-based'''
  default: '''Zero-based'''
- name: Show output port for nonzero input values
  summary: 启用非零值的输出端口 off（默认）| on
  group: 主要
  block_parameter: ShowOutputPortForNonzeroInputValues
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Output data type
  summary: '输出数据类型 Inherit: Inherit via internal rule（默认）| int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64
    | fixdt(1,16) | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''
    | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Mode
  summary: 选择数据类型模式 Inherit（默认）| Built in | Fixed Point
  group: 数据类型
- name: Data type override
  summary: 为此信号指定数据类型覆盖模式 Inherit | Off
  group: 数据类型
- name: Signedness
  summary: 指定有符号或无符号 Signed（默认）| Unsigned
  group: 数据类型
- name: Word length
  summary: 保存量化整数的字长位数 16（默认）| 0 到 32 的整数
  group: 数据类型
- name: Scaling
  summary: 缩放定点数据的方法 Integer（默认）
  group: 数据类型
```

### 主要

### **Index output format** — 非零元素索引的格式 `Linear indices`（默认）| `Subscripts`

选择非零输入值索引的输出格式。

- 选择 `Linear indices` 以向量形式提供任意维度信号的元素索引。对于一维（向量）信号，索引对应于非零值在向量中的位置。对于多于一维的信号，子脚本到索引的转换沿第一个维度进行。您无需知道输入信号的信号维度。
- 选择 `Subscripts` 以子脚本形式提供二维或更高维信号的元素索引。由于模块为每个维度显示一个输出端口，此选项要求您指定 **Number of input dimensions**。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexOutputFormat` |
| **类型：** 字符向量 |
| **值：** `'Linear indices'` | `'Subscripts'` |
| **默认值：** `'Linear indices'` |

### **Number of input dimensions** — 输入信号的维度数 `1`（默认）| 标量

将输入信号的维度数指定为 1 到 32 之间的正整数值。

#### 依赖关系

要启用此参数，请将 **Index output format** 设置为 `Subscripts`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfInputDimensions` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'1'` |

### **Index mode** — 指定从零开始或从一开始的索引 `Zero-based`（默认）| `One-based`

将索引模式指定为 `Zero-based` 或 `One-based`。

- 对于 `Zero-based` 索引，索引 `0` 指定输入向量的第一个元素。索引 `1` 指定第二个元素，依此类推。
- 对于 `One-based` 索引，索引 `1` 指定输入向量的第一个元素。索引 `2` 指定第二个元素，依此类推。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexMode` |
| **类型：** 字符向量 |
| **值：** `'Zero-based'` | `'One-based'` |
| **默认值：** `'Zero-based'` |

### **Show output port for nonzero input values** — 启用非零值的输出端口 `off`（默认）| `on`

显示或隐藏非零输入值的输出端口。

- 当您清除此复选框（`off`）时，模块隐藏非零输入值的输出端口。
- 当您选中此复选框（`on`）时，模块显示非零输入值的输出端口。附加输出端口提供非零输入元素的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputPortForNonzeroInputValues` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

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

### 数据类型

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

指定输出数据类型。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **默认值：** `'Inherit: Inherit via internal rule'` |

### **Mode** — 选择数据类型模式 `Inherit`（默认）| `Built in` | `Fixed Point`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。选择 `Inherit` 会启用右侧的第二个菜单/文本框，您可以在其中选择继承模式。
- `Built in` — 内置数据类型。选择 `Built in` 会启用右侧的第二个菜单/文本框，您可以在其中选择内置数据类型。
- `Fixed point` — 定点数据类型。选择 `Fixed point` 会启用附加参数，您可以使用这些参数指定定点数据类型。
- `Expression` — 求值为数据类型的表达式。选择 `Expression` 会启用右侧的第二个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请单击 **Show data type assistant** 按钮。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从使用该信号的模块、`Simulink.Signal` 对象或 Simulink® 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您可以在应用数据类型覆盖时对模型中的数据类型进行更好的控制。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

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

### **Scaling** — 缩放定点数据的方法 `Integer`（默认）

指定缩放定点数据的方法，以避免溢出情况并最小化量化误差。选择 `Integer` 会为定点数据指定二进制小数点位置，并将小数长度设置为 `0`。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。
## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2010a 中引入**

## 描述

查找数组中的非零元素

Find Nonzero Elements 模块定位输入信号的所有非零元素，并返回这些元素的线性索引。如果输入是多维信号，Find Nonzero Elements 模块还可以返回非零输入元素的子脚本。在这两种情况下，您都可以显示一个包含非零输入值的输出端口。

Find Nonzero Elements 模块输出可变大小信号。任何可变大小信号的采样时间都必须是离散的。如果您的模型尚未使用固定步长求解器，您可能需要在 Configuration Parameters 对话框中选择固定步长求解器。有关详细信息，请参阅 Compare Solvers 和 Choose a Solver。
