---
type: simulink-block
title: 'Signal Specification'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'signalspecification'
documentation_source_path: 'slref/signalspecification.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Specification

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

要检查其属性的输入信号，指定为标量、向量、矩阵或 N 维数组。该模块将输入信号的属性与您在模块对话框中指定的所需属性进行对比检查。如果属性不匹配，模块将生成错误。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

当信号的所有属性与对话框中指定的属性匹配时，输出信号即为输入信号。如果属性不匹配，模块将生成错误。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Minimum
  summary: 范围检查的最小值 []（默认）| 标量
  group: ''
  block_parameter: OutMin
  type: 字符向量
  values: 标量
  default: '''[ ]'''
- name: Maximum
  summary: 范围检查的最大值 []（默认）| 标量
  group: ''
  block_parameter: OutMax
  type: 字符向量
  values: 标量
  default: '''[ ]'''
- name: Data type
  summary: '输出数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | ...'
  group: ''
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32''
    | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''string'' | ''Enum:
    <class name>'' | ''Bus: <object name>'' | ''ValueType: <object name>'' | <data type expression> | Simulink.ImageType(480,640,3)'
  default: '''Inherit: auto'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型的选项 off（默认）| on
  group: ''
  block_parameter: LockScale
  values: '''off'' | ''on'''
  default: '''off'''
- name: Require nonvirtual bus
  summary: 仅接受非虚拟总线信号 off（默认）| on
  group: ''
  block_parameter: BusOutputAsStruct
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Unit (e.g., m, m/s^2, N\*m)
  summary: 模块输入信号的物理单位 inherit（默认）| <Enter unit>
  group: ''
  block_parameter: Unit
  type: 字符向量
  values: '''inherit'' | ''<Enter unit>'''
  default: '''inherit'''
- name: Dimensions (-1 for inherited)
  summary: 输入和输出信号的维度 -1（默认）| n | [m n]
  group: ''
  block_parameter: Dimensions
  type: 字符向量
  values: '''-1'' | n | [m n]'
  default: '''-1'''
- name: Variable-size signal
  summary: 允许信号为可变大小、固定大小或两者兼有 Inherit（默认）| No | Yes
  group: ''
  block_parameter: VarSizeSig
  type: 字符向量
  values: '''Inherit'' | ''No'' | ''Yes'''
  default: '''Inherit'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的时间间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 任何有效的采样时间
  default: '''-1'''
- name: Signal type
  summary: 信号的复/实性 auto（默认）| real | complex
  group: ''
  block_parameter: SignalType
  type: 字符向量
  values: '''auto'' | ''real'' | ''complex'''
  default: '''auto'''
- name: Mode
  summary: 数据类型模式 Inherit（默认）| Built in | Fixed point | Enumerated | Bus object | Value type | Expression
  group: ''
- name: Signedness
  summary: 有符号或无符号 Signed
  group: ''
- name: Data type override
  summary: 为此信号指定数据类型覆盖模式 Inherit | Off
  group: ''
- name: Word length
  summary: 保存量化整数的字长位数 16（默认）| 0 到 32 的整数
  group: ''
- name: Scaling
  summary: 定点数据的定标方法 Best precision（默认）| Binary point | Slope and bias
  group: ''
- name: Fraction length
  summary: 指定定点数据类型的小数长度 0（默认）| 标量整数
  group: ''
- name: Slope
  summary: 指定定点数据类型的斜率 2^0（默认）| 正实值标量
  group: ''
- name: Bias
  summary: 指定定点数据类型的偏置 0（默认）| 实值标量
  group: ''
```

### **Minimum** — 范围检查的最小值 `[]`（默认）| 标量

将模块输出的最小值指定为有限实数双精度标量值。

软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象所指定的最小值。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

### **Maximum** — 范围检查的最大值 `[]`（默认）| 标量

将模块输出的最大值指定为有限实数双精度标量值。

软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象所指定的最大值。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

### **Data type** — 输出数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

指定所需的输出数据类型。如果输入信号的数据类型与您指定的值不匹配，模块将生成错误或警告。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

您可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink® 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Data Types Supported by Simulink。
- 定点数据类型 — 使用 `fixdt` 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用类型名称并在前面加上 `Enum:`。例如，指定 `Enum: myEnumType`。
- 总线数据类型 — 使用 `Simulink.Bus` 对象的名称并在前面加上 `Bus:`。例如，指定 `Bus: myBusObject`。
- Simulink 图像数据类型 — 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数，并指定用于描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式，分别表示图像的行、列和通道。
- 值类型 — 使用 `Simulink.ValueType` 对象的名称并在前面加上 `ValueType:`。例如，指定 `ValueType: windVelocity`。
- 自定义数据类型 — 使用指定类型的 MATLAB® 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `'Fixed-point: unspecified scaling'` 以外的值。

当您将 `Simulink.ValueType` 或 `Simulink.Bus` 对象指定为数据类型时，Signal Specification 模块的某些参数将被忽略。例如，Signal Specification 模块的 **Min**、**Max** 和 **Unit** 参数将被忽略。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象的相应属性。例如，假设某个模块将 **Unit** 设置为 `ft/s`。当该模块的 **Data type** 指定了一个单位为 `m/s` 的 `ValueType` 对象时，该模块将使用 `m/s` 而不是 `ft/s`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Bus: <object name>' | 'ValueType: <object name>' | <data type expression> | Simulink.ImageType(480,640,3)` |
| **默认值：** `'Inherit: auto'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型的选项 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块上指定的输出数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Require nonvirtual bus** — 仅接受非虚拟总线信号 `off`（默认）| `on`

如果您将总线对象指定为数据类型，请使用此参数指定是否仅接受非虚拟总线信号。

- `off` — 指定信号必须来自*虚拟*总线。
- `on` — 指定信号必须来自*非虚拟*总线。

#### 依赖关系

要启用此参数，**Data type** 模块参数必须解析为 `Simulink.Bus` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：** `BusOutputAsStruct` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Unit (e.g., m, m/s^2, N\*m)** — 模块输入信号的物理单位 `inherit`（默认）| `<Enter unit>`

指定模块输入信号的物理单位。要指定单位，请在文本框中开始键入。键入时，该参数会显示可能匹配的单位。有关支持的单位列表，请使用 `showunitslist` 函数。

要约束单位制，请点击参数右侧的链接：

- 如果组件中存在 Unit System Configuration 模块，将打开其对话框。使用该对话框指定组件允许和不允许的单位制。
- 如果组件中不存在 Unit System Configuration 模块，将显示模型 Configuration Parameters 对话框。使用该对话框指定模型允许和不允许的单位制。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象所指定的单位。

#### 编程用法

|  |
| --- |
| **模块参数：** `Unit` |
| **类型：** 字符向量 |
| **值：** `'inherit'` | `'<Enter unit>'` |
| **默认值：** `'inherit'` |

要在不传播的情况下指定模块输入信号的物理单位，请使用 `UnitNoProp`。

### **Dimensions (-1 for inherited)** — 输入和输出信号的维度 `-1`（默认）| `n` | `[m n]`

指定输入和输出信号的维度。

- `-1` — 指定信号继承维度。
- `n` — 指定宽度为 `n` 的向量。
- `[m n]` — 指定具有 `m` 行和 `n` 列的矩阵。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象所指定的维度。

#### 编程用法

|  |
| --- |
| **模块参数：** `Dimensions` |
| **类型：** 字符向量 |
| **值：** `'-1'` | `n` | `[m n]` |
| **默认值：** `'-1'` |

### **Variable-size signal** — 允许信号为可变大小、固定大小或两者兼有 `Inherit`（默认）| `No` | `Yes`

指定信号为可变大小、固定大小或两者兼有。

- `Inherit` — 允许可变大小和固定大小信号。
- `No` — 不允许可变大小信号。
- `Yes` — 仅允许可变大小信号。

当信号为可变大小信号时，**Dimensions** 参数指定信号的最大维度。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，仿真仅允许使用已禁用总线对象的可变大小信号。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象所指定的维度模式。

#### 编程用法

|  |
| --- |
| **模块参数：** `VarSizeSig` |
| **类型：** 字符向量 |
| **值：** `'Inherit'` | `'No'` | `'Yes'` |
| **默认值：** `'Inherit'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程用法

|  |
| --- |
| **参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 任何有效的采样时间 |
| **默认值：** `'-1'` |

### **Signal type** — 信号的复/实性 `auto`（默认）| `real` | `complex`

指定输入和输出信号的复/实性。

- `auto` — 接受 `real` 或 `complex` 作为数值类型。
- `real` — 将数值类型指定为实数。
- `complex` — 将数值类型指定为复数。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象所指定的复/实性。

#### 编程用法

|  |
| --- |
| **参数：** `SignalType` |
| **类型：** 字符向量 |
| **值：** `'auto'` | `'real'` | `'complex'` |
| **默认值：** `'auto'` |

### **Mode** — 数据类型模式 `Inherit`（默认）| `Built in` | `Fixed point` | `Enumerated` | `Bus object` | `Value type` | `Expression`

选择要指定的数据类别。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

`Inherit`
:   数据类型的继承规则。选择 `Inherit` 会启用 `auto`。

`Built in`
:   内置数据类型。选择 `Built in` 会启用可能值的列表：

    - `double`（默认）
    - `single`
    - `int8`
    - `uint8`
    - `int16`
    - `uint16`
    - `int32`
    - `uint32`
    - `int64`
    - `uint64`
    - `boolean`

`Fixed point`
:   定点数据类型。

`Enumerated`
:   枚举数据类型。选择 `Enumerated` 会启用右侧的文本框，您可以在其中输入类名。

`Bus object`
:   总线对象。选择 `Bus object` 会启用右侧的文本框，您可以在其中输入要用于定义总线结构的总线对象名称。要创建或更改总线对象，请点击文本框右侧的 **Edit**。

`Value type`
:   值类型。选择 `Value type` 会启用右侧的文本框，您可以在其中输入要用于定义信号属性的值类型名称。要创建或更改值类型，请点击文本框右侧的 **Edit**。

`Expression`
:   求值为数据类型的表达式。选择 `Expression` 会启用右侧的文本框，您可以在其中输入表达式。

    不要将总线对象指定为表达式。

#### 依赖关系

要启用此参数，请点击 **Show data type assistant** 按钮 。

### **Signedness** — 有符号或无符号 `Signed`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，而无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink 从其上下文中继承数据类型覆盖设置，即从使用该信号的 Simulink 中的模块、`Simulink.Signal` 对象或 Stateflow® 图中继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置，并使用为该信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，使您可以在应用数据类型覆盖时对模型中的数据类型进行更精细的控制。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定点数据的定标方法 `Best precision`（默认）| `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0`（默认）| 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Binary point`。

### **Slope** — 指定定点数据类型的斜率 `2^0`（默认）| 正实值标量

指定定点数据类型的斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

### **Bias** — 指定定点数据类型的偏置 `0`（默认）| 实值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。
## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有直通实现。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**`Simulink.ValueType` 对象支持**

此模块支持 `Simulink.ValueType` 对象的代码生成。有关值类型的更多信息，请参阅 Specify Common Set of Signal Properties as Value Type。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

指定信号的期望维度、采样时间、数据类型、数值类型和其他属性

Signal Specification 模块允许您指定连接到其输入和输出端口的信号的属性。如果指定的属性与连接到其端口的模块指定的属性冲突，软件在编译模型时会显示错误。例如，在仿真开始时，如果不存在冲突，软件会从编译模型中消除 Signal Specification 模块。换句话说，Signal Specification 模块是一个虚拟模块。它仅用于指定信号的属性，在模型的仿真中不起任何作用。

您可以使用 Signal Specification 模块来确保信号的实际属性满足期望属性。例如，假设您和同事正在处理同一模型的不同部分。您使用 Signal Specification 模块将您的模型部分与同事的模型部分连接起来。如果您的同事在未通知您的情况下更改了信号的属性，则进入相应 Signal Specification 模块的属性将不匹配。当您尝试仿真模型时，会收到错误。

您还可以使用 Signal Specification 模块来确保信号属性在整个模型中正确传播。但是，如果某些模块对其接受或输出的信号具有未指定的属性，则模型没有足够的信息来正确传播属性。在这些情况下，Signal Specification 模块可以提供软件所需的信息。当模块缺少信号属性时，使用 Signal Specification 模块还有助于加快模型编译速度。

Signal Specification 模块支持信号标签传播。有关更多信息，请参阅 Signal Label Propagation。
