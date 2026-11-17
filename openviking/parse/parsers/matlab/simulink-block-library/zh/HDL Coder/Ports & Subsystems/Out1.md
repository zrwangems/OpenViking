---
type: simulink-block
title: 'Outport'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'outport'
documentation_source_path: '../simulink/slref/outport.html'
language: zh-CN
chinese_source: worker-translation
---

# Outport

## 端口
```yaml
ports:
- name: Port_1
  summary: Outport 信号 标量 | 向量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus | image | datetime
```

### 输入

### **Port\_1** — Outport 信号 标量 | 向量

通过 outport 流向外部子系统或模型的输入信号。

当 Outport 模块不是根级输出端口时，它可以接受定点数和枚举数据类型。模块输出的复杂度和数据类型与其输入相同。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
## 参数
```yaml
parameters:
- name: Port number
  summary: 端口在父模块上的位置 1（默认）| 实数整数
  group: 主要
  block_parameter: Port
  values: '"1"（默认）| 带引号的实数整数'
- name: Signal name
  summary: 信号名称 ' '（默认）| 字符向量
  group: 主要
  block_parameter: SignalName
  type: 字符向量
  values: 字符向量
  default: ''' '''
- name: Icon display
  summary: 图标显示 Port number（默认）| Signal name | Port number and signal name
  group: 主要
  block_parameter: IconDisplay
  type: 字符向量
  values: '''Signal name'' | ''Port number'' | ''Port number and signal name'''
  default: '''Port number'''
- name: Specify output when source is unconnected
  summary: 指定未连接时的输出值 off（默认）| on
  group: 主要
  block_parameter: OutputWhenUnconnected
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Constant value
  summary: 模块未连接时的输出值 0（默认）| 标量 | 向量
  group: 主要
  block_parameter: OutputWhenUnconnectedValue
  type: 字符向量
  values: scalar | vector
  default: '''0'''
- name: Interpret vector parameters as 1-D
  summary: 将向量视为一维 on（默认）| off
  group: 主要
  block_parameter: VectorParamsAs1DForOutWhenUnconnected
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Ensure outport is virtual
  summary: 确保 outport 为虚拟 off（默认）| on
  group: 主要
  block_parameter: EnsureOutportIsVirtual
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Output when disabled
  summary: 禁用时的输出 held（默认）| reset
  group: 主要
  block_parameter: OutputWhenDisabled
  type: 字符向量
  values: '''held'' | ''reset'''
  default: '''held'''
- name: Initial output
  summary: 条件执行子系统的初始输出 []（默认）| 标量 | 结构体
  group: 主要
  block_parameter: InitialOutput
  type: 字符向量
  values: '''[]'' | 标量 | 结构体'
  default: '''[]'''
- name: Minimum
  summary: 最小输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMin
  type: 字符向量
  values: '''[ ]''| 标量'
  default: '''[ ]'''
- name: Maximum
  summary: 最大输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMax
  type: 字符向量
  values: '''[ ]''| 标量'
  default: '''[ ]'''
- name: Data type
  summary: '输出数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | ...'
  group: 信号属性
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32''
    | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''string''
    | ''Enum: <class name>'' | ''Bus: <object name>'' | ''ValueType: <object name>'' | ''<data type expression>'' | Simulink.ImageType(480,640,3)'
  default: '''Inherit: auto'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型的选项 off（默认）| on
  group: 信号属性
  block_parameter: LockScale
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output as nonvirtual bus in parent model
  summary: 在父模型中作为非虚拟总线输出 off（默认）| on
  group: 信号属性
  block_parameter: BusOutputAsStruct
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Unit (e.g., m, m/s^2, N\*m)
  summary: 模块输入信号的物理单位 inherit（默认）| <Enter unit>
  group: 信号属性
  block_parameter: Unit
  type: character vector
  values: '''inherit'' | ''<Enter unit>'''
  default: '''inherit'''
- name: Port dimensions (-1 for inherited)
  summary: 端口维度 -1（默认）| 整数 | [整数, 整数]
  group: 信号属性
  block_parameter: PortDimensions
  type: character vector
  values: '''-1'' | integer | [integer, integer]'
  default: '''-1'''
- name: Variable-size signal
  summary: 允许可变大小信号 Inherit（默认）| No | Yes
  group: 信号属性
  block_parameter: VarSizeSig
  type: character vector
  values: '''Inherit'' | ''No'' | ''Yes'''
  default: '''Inherit'''
- name: Signal type
  summary: 输出信号类型 auto（默认）| real | complex
  group: 信号属性
  block_parameter: SignalType
  type: character vector
  values: '''auto'' | ''real'' | ''complex'''
  default: '''auto'''
- name: Sample time (-1 for inherited)
  summary: 指定采样时间的选项 -1（默认）| 标量
  group: Execution
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''-1'''
```

### 主要

### **Port number** — 端口在父模块上的位置 `1`（默认）| 实数整数

指定与该模块对应的端口在父 Subsystem 或 Model 模块上出现的顺序。

- 如果添加一个创建另一个端口的模块，端口编号为下一个可用编号。
- 删除与某个端口关联的所有模块会删除该端口。其他端口会重新编号，使其连续且不跳过任何编号。
- 指定一个超过端口数量的端口编号会为该编号以及任何被跳过的连续编号创建端口。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **值**：| `"1"`（默认）| 带引号的实数整数 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

### **Signal name** — 信号名称 `' '`（默认）| 字符向量

指定生成代码中对应信号数据的名称。当您对根级 Outport 模块应用存储类时，使用此参数为信号数据指定名称。

#### 依赖关系

要启用此参数，模块必须位于模型的顶层。

#### 编程使用

|  |
| --- |
| **模块参数**：`SignalName` |
| **类型**：字符向量 |
| **值**：字符向量 |
| **默认值**：`' '` |

### **Icon display** — 图标显示 `Port number`（默认）| `Signal name` | `Port number and signal name`

指定模块图标上显示的信息。

#### 编程使用

|  |
| --- |
| **模块参数**：`IconDisplay` |
| **类型**：字符向量 |
| **值**：`'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **默认值**：`'Port number'` |

### **Specify output when source is unconnected** — 指定未连接时的输出值 `off`（默认）| `on`

指定当源未连接时的常量输出值。

#### 依赖关系

适用于 Variant Subsystem 模块内未连接的 Outport 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputWhenUnconnected` |
| **类型**：字符向量 |
| **值**：`'on' | 'off'` |
| **默认值**：`'off'` |

### **Constant value** — 模块未连接时的输出值 `0`（默认）| 标量 | 向量

指定当源未连接时的常量输出值。

#### 依赖关系

在 Variant Subsystem 模块中，对于选中了 **Specify output when source is unconnected** 的未连接 Outport 模块可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputWhenUnconnectedValue` |
| **类型**：字符向量 |
| **值**：`scalar` | `vector` |
| **默认值**：`'0'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Constant value** 参数求值为 `N` 元素的行向量或列向量，则选中此复选框以在输出端创建长度为 `N` 的向量。

#### 依赖关系

在 Variant Subsystem 模块中，当您选择 **Specify output when source is unconnected** 参数时，对未连接的 Outport 模块可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`VectorParamsAs1DForOutWhenUnconnected` |
| **类型**：字符向量 |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

### **Ensure outport is virtual** — 确保 outport 为虚拟 `off`（默认）| `on`

清除此参数以允许 Simulink® 在输出端口上使用信号缓冲区。此缓冲区相当于 Signal Conversion 模块，但不在画布上显示，它确保 Outport 模块信号的一致初始化。

如果选中此参数，Simulink 会尝试移除信号缓冲区。

- 如果不需要信号缓冲区，Simulink 会移除该缓冲区。
- 如果为了数据一致性和正确执行而需要信号缓冲区，Simulink 会显示错误，指示无法移除该缓冲区。

允许通过 Assignment 模块进行部分写入。

有关此参数的更多信息，包括条件写入和部分写入的示例，请参阅 Ensure Output Port Is Virtual。

**Note**

如果模块位于模型的根级，并且由 Initialize Function 模块、Reset Function 模块、Reinitialize Function 模块或 Terminate Function 模块内的另一个 Outport 模块驱动，则该模块始终为虚拟。

#### 依赖关系

此参数适用于以下模块和此配置参数设置：

- Conditional subsystem
- Assignment
- Merge
- 具有根 Outport 模块的模型
- **Underspecified initialization detection** 配置参数必须设置为 `Simplified`。当选择该配置参数的 `Classic` 选项时，此模块参数不可用。有关如何从经典初始化模式切换到简化初始化模式的更多信息，请参阅 Convert from Classic to Simplified Initialization Mode。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnsureOutportIsVirtual` |
| **类型**：字符向量 |
| **值**：`'on' | 'off'` |
| **默认值**：`'off'` |

### **Output when disabled** — 禁用时的输出 `held`（默认）| `reset`

指定当子系统禁用时模块输出的行为。选择 `held` 表示当子系统禁用时输出保持不变。选择 `reset` 表示当子系统禁用时输出重置为 **Initial output** 给定的值。

#### 依赖关系

当 Outport 模块位于具有有效启用和禁用语义的条件子系统内时可用。例如，该参数对于 Enabled Subsystem 模块内的 Outport 模块可用，而对于 Triggered Subsystem 模块内的 Outport 模块不可用。

如果 Outport 模块位于 Function-Call Subsystem 模块内，则仅当 Function-Call Subsystem 模块连接到 Stateflow® 图中的状态时，此参数才有意义。有关更多信息，请参阅 Bind a Function-Call Subsystem to a State (Stateflow)。

当将条件子系统的输出连接到 Merge 模块时，请将此参数设置为 `held`。将其设置为 `reset` 会返回错误。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputWhenDisabled` |
| **类型**：字符向量 |
| **值**：`'held' | 'reset'` |
| **默认值**：`'held'` |

### **Initial output** — 条件执行子系统的初始输出 `[]`（默认）| 标量 | 结构体

对于条件执行的子系统，指定子系统执行之前以及禁用期间的模块输出。要从输入信号继承初始输出值，请应用以下两个默认设置：

- 将 **Initial output** 参数设置为 `[]`。
- 将 **Output when disabled** 参数设置为 `held`。

Simulink 尝试从输入信号继承输出值。但是，如果输入信号不是初始输出值的有效来源，则初始输出值 `[]` 将被视为 `double(0)`。有关更多信息，请参阅 Conditional Subsystem Initial Output Values。

有关指定初始条件结构体的信息，请参阅 Specify Initial Conditions for Bus Elements。

#### 提示

如果条件子系统驱动 Merge 模块，则无需为 Outport 模块指定 Initial Condition (IC)。有关更多信息，请参阅 Underspecified initialization detection。

#### 依赖关系

当 Outport 模块位于条件子系统内时可用。

#### 限制

- 此模块不允许初始输出为 `inf` 或 `NaN`。
- 当输入为虚拟总线时，**Initial output** 值 `[]` 被视为 `double(0)`。
- 当输入包含非虚拟总线时，**Initial output** 不支持非零标量值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 | 结构体 |
| **默认值**：`'[]'` |

### 信号属性

### **Minimum** — 最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

此数字必须为有限实数双精度标量值。

软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最小值。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

### **Maximum** — 最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

此数字必须为有限实数双精度标量值。

软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最大值。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

### **Data type** — 输出数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

指定外部输入的输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType` 对象）。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

您可以指定以下任一选项：

- 继承数据类型
- 内置 Simulink 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Data Types Supported by Simulink。
- 定点数据类型 — 使用 `fixdt` 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用类型名称并在前面加上 `Enum:`。例如，指定 `Enum: myEnumType`。
- 总线数据类型 — 使用 `Simulink.Bus` 对象的名称并在前面加上 `Bus:`。例如，指定 `Bus: myBusObject`。
- Simulink 图像数据类型 — 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数并指定描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式，分别表示图像的行、列和通道。
- 值类型 — 使用 `Simulink.ValueType` 对象的名称并在前面加上 `ValueType:`。例如，指定 `ValueType: windVelocity`。
- 自定义数据类型 — 使用指定类型的 MATLAB 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `'Fixed-point: unspecified scaling'` 以外的值。

当您指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象作为数据类型时，Outport 模块的某些参数将被忽略。例如，Outport 模块的 **Min**、**Max** 和 **Unit** 参数将被忽略。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象的相应属性。例如，假设某个模块将 **Unit** 设置为 `ft/s`。当该模块的 **Data type** 指定一个单位为 `m/s` 的 `ValueType` 对象时，该模块使用 `m/s` 而不是 `ft/s`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` | `Simulink.ImageType(480,640,3)` |
| **默认值**：`'Inherit: auto'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型的选项 `off`（默认）| `on`

选中此参数以防止定点工具覆盖您在模块上指定的输出数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output as nonvirtual bus in parent model** — 在父模型中作为非虚拟总线输出 `off`（默认）| `on`

指定 outport 总线在父模型中为非虚拟。如果您希望父模型中出现的总线为非虚拟，请选中此参数。无论 **Output as nonvirtual bus in parent model** 的设置如何，输入到该端口的总线可以是虚拟的或非虚拟的。

如果您希望父模型中出现的总线为虚拟，请清除此参数。

#### 提示

- 在非虚拟总线中，所有信号必须具有相同的采样时间，即使关联总线对象的元素指定了继承采样时间。任何会导致非虚拟总线违反此要求的操作都会产生错误。有关详细信息，请参阅 Modify Sample Times for Nonvirtual Buses。

  要将多速率信号用于虚拟总线，请在根级 Outport 模块中将 **Sample time** 参数设置为继承（`-1`）。
- 对于模型引用层次结构中的顶层模型，代码生成会创建一个 C 结构体来表示此模块的总线输出。
- 对于被引用的模型，选中此选项以创建 C 结构体。否则，代码生成会为总线的每个叶元素创建一个参数。

#### 依赖关系

要启用此参数，**Data type** 必须解析为 `Simulink.Bus` 对象。例如，将 **Data type** 设置为 `Simulink.Bus` 对象或将其数据类型指定为 `Simulink.Bus` 对象的 `Simulink.ValueType` 对象。

#### 编程使用

|  |
| --- |
| **模块参数**：`BusOutputAsStruct` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Unit (e.g., m, m/s^2, N\*m)** — 模块输入信号的物理单位 `inherit`（默认）| `<Enter unit>`

指定模块输入信号的物理单位。要指定单位，请在文本框中开始输入。输入时，该参数会显示可能匹配的单位。有关支持的单位列表，请使用 `showunitslist` 函数。

要约束单位系统，请单击该参数右侧的链接：

- 如果组件中存在 Unit System Configuration 模块，则会打开其对话框。使用该对话框指定组件允许和不允许的单位系统。
- 如果组件中不存在 Unit System Configuration 模块，则会显示模型配置参数对话框。使用该对话框指定模型允许和不允许的单位系统。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象所指定的单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`Unit` |
| **类型**：character vector |
| **值**：`'inherit'` | `'<Enter unit>'` |
| **默认值**：`'inherit'` |

要在不传播的情况下指定模块输入信号的物理单位，请使用 `UnitNoProp`。

### **Port dimensions (-1 for inherited)** — 端口维度 `-1`（默认）| 整数 | [整数, 整数]

指定信号必须具有的维度才能连接到此 Outport 模块。

|  |  |
| --- | --- |
| `-1` | 任意维度的信号都可以连接到此端口。 |
| `N` | 连接到此端口的信号必须是大小为 `N` 的向量。 |
| `[R C]` | 连接到此端口的信号必须是具有 `R` 行和 `C` 列的矩阵。 |

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象所指定的维度。

#### 编程使用

|  |
| --- |
| **模块参数**：`PortDimensions` |
| **类型**：character vector |
| **值**：`'-1'` | integer | [integer, integer] |
| **默认值**：`'-1'` |

### **Variable-size signal** — 允许可变大小信号 `Inherit`（默认）| `No` | `Yes`

指定此端口输出允许的信号类型。要允许可变大小和固定大小信号，请选择 `Inherit`。要仅允许可变大小信号，请选择 `Yes`。要仅允许固定大小信号，请选择 `No`。

当此端口上的信号为可变大小信号时，**Port dimensions** 参数指定信号的最大维度。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象所指定的维度模式。

#### 编程使用

|  |
| --- |
| **Parameter:**  `VarSizeSig` |
| **类型**：character vector |
| **Value:** `'Inherit'` | `'No'` | `'Yes'` |
| **默认值**：`'Inherit'` |

### **Signal type** — 输出信号类型 `auto`（默认）| `real` | `complex`

指定信号输出的数值类型。要选择连接到其输入的信号的数值类型，请选择 `auto`。否则，请选择实数或复数信号类型。

#### 依赖关系

当 **Data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象所指定的复数性。

#### 编程使用

|  |
| --- |
| **模块参数**：`SignalType` |
| **类型**：character vector |
| **值**：`'auto'` | `'real'` | `'complex'` |
| **默认值**：`'auto'` |

### Execution

### **Sample time (-1 for inherited)** — 指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'-1'` |
## 所属库

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sinks

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

此模块具有一个默认 HDL 架构。

**HDL Block Properties**

| General | |
| --- | --- |
| **BalanceDelays** | | **BalanceDelays** 设置 | 说明 | | --- | --- | | `on`（默认） | 检测 DUT 中其他路径上延迟的引入，并在 Outport 模块路径上插入匹配的延迟。 | | `off` | 禁用 DUT 子系统中输出端口上的延迟平衡，以防止 HDL Coder 在不必要时插入匹配的延迟。例如，当将手动添加的输出端口视为测试点时，在 DUT 子系统中的 Outport 模块上禁用 **BalanceDelays**。 |  **注意**  此属性仅影响 DUT 级 Outport 模块。 |
| **BidirectionalPort** | | **BidirectionalPort** 设置 | 说明 | | --- | --- | | `on` | 将端口指定为双向。 以下要求适用：  - 端口必须位于具有黑盒实现的 Subsystem 模块中。 - 双向端口与对应的顶层 DUT 子系统端口之间不得存在任何逻辑。  有关详细信息，请参阅 Specify Bidirectional Ports (HDL Coder)。 | | `off`（默认） | 不将端口指定为双向。 | |

| Target Specification | |
| --- | --- |
| **IOInterface** | DUT 端口的目标平台接口类型，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterface` 模块属性将被忽略。  要指定有效的 `IOInterface` 设置，请使用 HDL Workflow Advisor：  1. 在 HDL Workflow Advisor 中，在 **Set Target** > **Set Target Interface** 步骤中，在 **Target platform interface table** 中的 **Target Platform Interfaces** 列中，使用下拉列表设置目标平台接口类型。 2. 保存模型。  `IOInterface` 值将保存为端口的 HDL 模块属性。  例如，要查看 `IOInterface` 值，如果 DUT 端口的完整路径为 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | DUT 端口的目标平台接口端口映射，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceMapping` 模块属性将被忽略。  要指定有效的 `IOInterfaceMapping` 设置，请使用 HDL Workflow Advisor：  1. 在 HDL Workflow Advisor 中，在 **Set Target** > **Set Target Interface** 步骤中，在 **Target platform interface table** 中的 **Target Platform Interfaces** 列中，使用下拉列表设置目标平台接口类型。 2. 在 **Bit Range / Address / FPGA Pin** 列中，如果要更改默认值，请输入目标平台接口映射。 3. 保存模型。  `IOInterfaceMapping` 值将保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceMapping` 值，如果 DUT 端口的完整路径为 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | DUT 端口的目标平台接口端口映射选项，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceOptions` 模块属性将被忽略。  要指定有效的 `IOInterfaceOptions` 设置，请使用 HDL Workflow Advisor：  1. 在 HDL Workflow Advisor 中，在 **Set Target** > **Set Target Interface** 步骤中，在 **Target platform interface table** 中的 **Target Platform Interfaces** 列中，将输入或输出端口映射到 AXI4 从属接口。 2. 在 **Interface Options** 列中，如果要更改默认初始值，请点击 **Options** 按钮，并为 **RegisterInitialValue** 输入一个值。 3. 保存模型。  `IOInterfaceOptions` 值将保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceOptions` 值，如果 DUT 端口的完整路径为 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

**`Simulink.ValueType` Object Support**

此模块支持为 `Simulink.ValueType` 对象生成代码。有关
值类型的详细信息，请参阅 Specify Common Set of Signal Properties as Value Type。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2025a: Log `datetime` data

Outport 模块支持记录 `datetime` 数据。

### R2024a：**初始输出值的来源**参数已被移除

从 R2024a 开始，对于条件执行子系统，初始输出值
继承自子系统的输入信号。软件将
**初始输出**参数设置为 `[]`，并将
**禁用时的输出**参数设置为
`held`.

### R2023b: Log unbounded variable-size signals

在普通和加速模式下仿真时，Outport 模块支持
记录无界可变大小信号。不支持记录非虚拟
包含无界可变大小信号的总线。

## 描述

为子系统或外部输出创建输出端口

Outport 模块将信号从系统链接到系统外部的目的地。
系统。它们可以将从子系统流出的信号连接到模型的
其他部分。它们还可以在模型的顶层提供外部输出
hierarchy.

Outport 模块端口号按以下规则分配：

- 根级系统或子系统中的 Outport 模块按
  numbered sequentially, starting with 1.
- 如果添加 Outport 模块，则为其分配下一个可用的
  number.
- 如果删除 Outport 模块，其他端口号会
  自动重新编号，以确保 Outport 模块按
  序列，且不省略任何编号。

### Outport Blocks in a Subsystem

子系统中的 Outport 模块表示子系统的输出。信号
到达子系统中的 Outport 模块后，会从
该 Subsystem 模块上关联的输出端口流出。Outport 模块
与输出端口关联的依据是，该模块的 **Port
number** 参数与该输出端口在
Subsystem 模块上的相对位置相匹配。例如，**Port number** 参数为 `1` 的 Outport 模块会将其
信号发送到与最上方输出端口连接的模块，该端口位于
Subsystem block.

如果重新编号某个
Outport 模块的 **Port number**，该模块将连接到不同的输出
端口。该模块继续将信号发送到外部同一模块
subsystem.

你可以直接在 Subsystem 模块上编辑端口标签。有关更多
信息，请参阅 Edit Port Labels on Subsystem Blocks。

**Tip**

对于包含由许多总线元素组成的总线的模型，请考虑使用 In Bus
Element 和 Out Bus Element 模块。这些
blocks:

- 减少模块图中的信号线复杂度和杂乱。
- Make it easier to change the interface incrementally.
- Allow access to a bus element closer to the point of usage, avoiding
  使用 Bus Selector 和 Goto 模块
  configuration.

In Bus Element 模块的模块类型为 Inport
而 Out Bus Element 模块的模块类型为
Outport.

### 模型层次结构中的顶层 Outport 模块

模型层次结构顶层的 Outport 模块有两个用途。它们可以
向基础 MATLAB® 工作区提供外部输出，并且它们为 `linmod`
和 `trim` 分析函数提供了一种从
system.

要向工作区提供外部输出，请使用 **Configuration Parameters** > **Data Import/Export** 窗格（请参阅 Exporting Output Data to
the MATLAB Workspace）或 `sim` 命令。例如，如果一个系统有多个
Outport 模块且保存格式为数组，则此命令

```
[t,x,y] = sim(...);
```

将 `y` 写为矩阵，其中每一列包含
不同 Outport 模块的数据。列顺序与
Outport 模块的端口编号顺序一致。

如果在第二个（状态）参数之后指定多个变量名，则数据
来自每个 Outport 模块的数据都会写入不同的变量。例如，
如果系统有两个 Outport 模块，要将来自
Outport 模块 1 的数据保存到 `speed`，并将来自
Outport 模块 2 的数据保存到 `dist`，请指定此
command:

```
[t,x,speed,dist] = sim(...);
```

### Connecting Buses to Root-Level Outports

模型中的根级 Outport 模块只有在总线的所有
元素都具有相同数据类型时才能接受虚拟总线。Outport 模块
automatically unifies the bus to a vector having the same number of elements as the
总线，并将该向量作为输出提供。

如果你希望模型的根级 Outport 模块接受包含
混合类型的总线，请将 Outport 模块的 **Data
type** 设置为 `Bus: <object name>`。如果该总线是
virtual, it is converted to nonvirtual, as described in Virtual and Nonvirtual Bus Conversions.

### 将根级 Outport 模块与 `Simulink.Signal` 对象关联

要将根级 Outport 模块与
`Simulink.Signal` 对象关联，请使用模型数据编辑器。请参阅 For Signals。
