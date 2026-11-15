---
type: simulink-block
title: 'Signal Specification'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'signalspecification'
---

# Signal Specification

Specify desired dimensions, sample time, data type, numeric type, and other attributes of signal

## 中文

指定信号所需的维度、采样时间、数据类型、数值类型和其他属性

### 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

### 描述

Signal Specification 模块允许您指定连接到其输入和输出端口上的信号的属性。如果指定的属性与其端口上连接的模块所指定的属性冲突，软件将在编译模型时显示错误消息。例如，在仿真开始时，如果不存在冲突，该软件将从已编译的模型中消除 Signal Specification 模块。换句话说，Signal Specification 模块是虚拟模块。它的存在只是为了指定信号的属性，在模型的仿真中不起任何作用。

您可以使用 Signal Specification 模块确保信号的实际属性满足所需的属性要求。例如，假设您和一位同事负责设计同一个模型的不同部分。您可以使用 Signal Specification 模块将您负责的那部分模型与您同事负责的那部分连接起来。如果您的同事更改了某个信号的属性而没有通知您，则输入对应 Signal Specification 模块的属性将不匹配。当您尝试对模型进行仿真时，您会看到错误消息。

您还可以使用 Signal Specification 模块确保信号属性在整个模型中的正确传播。但是，如果有些模块收到或输出的信号具有未指定的属性，模型将没有足够的信息进行正确的属性传播。在这些情况下，Signal Specification 模块可以提供软件需要的信息。使用 Signal Specification 模块，还可以在模块缺少信号属性时帮助您提高模型的编译速度。

Signal Specification 模块支持信号标签传播。有关详细信息，请参阅信号标签传播。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

要检查其属性的输入信号，指定为标量、向量、矩阵或 N 维数组。模块根据您在模块对话框中指定的属性检查输入信号的属性。如果属性不匹配，则模块会生成错误。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

当信号的所有属性与对话框中指定的属性都匹配时，输出信号就是输入信号。如果属性不匹配，则模块会生成错误。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### **最小** — 范围检查的最小值 `[]` (默认) | 标量

将模块输出的最小值指定为有限双精度实数标量值。

软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围）
- 定点数据类型的自动定标

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最小值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

#### **最大** — 范围检查的最大值 `[]` (默认) | 标量

将模块输出的最大值指定为有限双精度实数标量值。

软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围）
- 定点数据类型的自动定标

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最大值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

#### **数据类型** — 输出数据类型 **Inherit: auto** (默认) | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | ...

指定所需的输出数据类型。如果输入信号的数据类型与您指定的值不匹配，则模块会生成错误或警告。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

您可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink® 数据类型 - 例如，指定 **single** 或 **uint8**。请参阅 Simulink 支持的数据类型。
- 定点数据类型 - 使用 `fixdt` 函数。例如，指定 **fixdt(1,16,0)**。
- 枚举数据类型 - 使用以 `Enum:` 开头的类型名称。例如，指定 **Enum: myEnumType**。
- 总线数据类型 - 使用以 `Bus:` 开头的 `Simulink.Bus` 对象的名称。例如，指定 **Bus: myBusObject**。
- Simulink 图像数据类型 - 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数，并指定描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式，分别表示图像的行、列和通道。
- 值类型 - 使用以 `ValueType:` 开头的 `Simulink.ValueType` 对象的名称。例如，指定 **ValueType: windVelocity**。
- 自定义数据类型 - 使用指定类型的 MATLAB® 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `'Fixed-point: unspecified scaling'` 以外的值。

当您指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象作为数据类型时，会忽略 Signal Specification 模块的一些参数。例如，忽略 Signal Specification 模块的 **Min**、**Max** 和 **Unit** 参数。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象的对应属性。例如，假设一个模块将**单位**设置为 `ft/s`。当该模块的**数据类型**指定以 `m/s` 为单位的 `ValueType` 对象时，该模块会使用 `m/s` 而不是 `ft/s` 作为单位。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Bus: <object name>' | 'ValueType: <object name>' | <data type expression> | Simulink.ImageType(480,640,3)` |
| **默认值：**`'Inherit: auto'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的输出数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **需要非虚拟总线** — 仅接受非虚拟总线信号 `off` (默认) | `on`

如果您指定总线对象作为数据类型，请使用此参数指定是否只接受非虚拟总线信号。

- `off` - 指定信号必须来自*虚拟*总线。
- `on` - 指定信号必须来自*非虚拟*总线。

##### 依赖关系

要启用此参数，**数据类型**模块参数必须解析为 `Simulink.Bus` 对象。

##### 编程用法

|  |
| --- |
| **模块参数**：`BusOutputAsStruct` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **单位(例如，m、m/s^2、N\*m)** — 模块的输入信号的物理单位 `inherit` (默认) | `<Enter unit>`

指定模块的输入信号的物理单位。要指定单位，请在文本框中键入需要的值。随着您的键入，参数将显示可能匹配的单位。有关支持的单位列表，请使用 `showunitslist` 函数。

要约束单位制，请点击参数右侧的链接：

- 如果组件中存在 Unit System Configuration 模块，将打开其对话框。使用该对话框为组件指定允许和不允许使用的单位制。
- 如果组件中不存在 Unit System Configuration 模块，将显示模型的“配置参数”对话框。使用该对话框为模型指定允许和不允许使用的单位制。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的单位。

##### 编程用法

|  |
| --- |
| **模块参数**：`Unit` |
| **类型：**字符向量 |
| **值**：`'inherit'` | `'<Enter unit>'` |
| **默认值**：`'inherit'` |

要指定模块的输入信号的物理单位而不传播，请使用 `UnitNoProp`。

#### **维度(-1 表示继承)** — 输入和输出信号的维度 `-1` (默认) | `n` | `[m n]`

指定输入和输出信号的维度。

- `-1` - 指定信号继承维度。
- `n` - 指定宽度为 `n` 的向量。
- `[m n]` - 指定具有 `m` 行 `n` 列的矩阵。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`Dimensions` |
| **类型：**字符向量 |
| **值**：`'-1'` | `n` | `[m n]` |
| **默认值：**`'-1'` |

#### **可变大小信号** — 允许信号为可变大小、固定大小或两者皆可 **继承** (默认) | **否** | **是**

将信号指定为可变大小、固定大小或两者皆可。

- **inherit** - 允许可变大小和固定大小的信号。
- **否** - 不允许可变大小的信号。
- **是** - 仅允许可变大小的信号。

当信号为可变大小的信号时，**维度**参数指定信号的最大维度。

##### 依赖关系

- 当**数据类型**指定 `Simulink.Bus` 对象时，仿真只允许具有禁用的总线对象的可变大小信号。
- 当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度模式。

##### 编程用法

|  |
| --- |
| **模块参数**：`VarSizeSig` |
| **类型：**字符向量 |
| **值**：`'Inherit'` | `'No'` | `'Yes'` |
| **默认值：**`'Inherit'` |

#### **采样时间(-1 表示继承)** — 采样时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **参数：**`SampleTime` |
| **类型：**字符向量 |
| **值：**任何有效的采样时间 |
| **默认值：**`'-1'` |

#### **信号类型** — 信号的复/实性 **自动** (默认) | **实数** | **复**

指定输入和输出信号的复/实性。

- **自动** - 接受**实部**或**复**为数值类型。
- **实部** - 指定数值类型为实数。
- **复** - 指定数值类型为复数。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的复/实性。

##### 编程用法

|  |
| --- |
| **参数：**`SignalType` |
| **类型：**字符向量 |
| **值**：`'auto'` | `'real'` | `'complex'` |
| **默认值：**`'auto'` |

#### **模式** — 数据类型模式 **继承** (默认) | **内置** | **定点** | **枚举** | **总线对象** | **值类型** | **表达式**

选择要指定的数据类别。有关详细信息，请参阅使用数据类型助手指定数据类型。

**继承**
:   数据类型的继承规则。选择 `Inherit` 将启用 `auto`。

**内置**
:   内置的数据类型。选择 `Built in` 将启用一个可能值的列表：

    - `double`（默认值）
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

**定点**
:   定点数据类型。

**枚举**
:   枚举数据类型。选择 `Enumerated` 将在右侧启用另一个文本框，您可以在其中输入类名称。

**总线对象**
:   总线对象。选择**总线对象**将在右侧启用一个文本框，您可以在此处输入要用来定义总线结构的总线对象的名称。要创建或更改总线对象，点击文本框右侧的**编辑**。

**值类型**
:   值类型。选择**值类型**将在右侧启用一个文本框，您可在其中输入要用于定义信号属性的值类型的名称。要创建或更改值类型，请点击文本框右侧的**编辑**。

**表达式**
:   计算结果为数据类型的表达式。选择**表达式**将在右侧启用一个文本框，您可以在其中输入表达式。

    不要将总线对象指定为表达式。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮 。

#### **符号性** — 有符号或无符号 **有符号**

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，无符号数据只表示正值。

- **有符号**，将定点数据指定为有符号数据。
- **无符号**，将定点数据指定为无符号数据。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 **inherit** 时，Simulink 从信号的上下文（即：从 Simulink 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
- 当您选择 **off** 时，Simulink 忽略信号上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**内置**或**定点**。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **定标** — 定标定点数据的方法 **最佳精度** (默认) | **二进制小数点** | **斜率和偏置**

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **小数长度** — 指定定点数据类型的小数长度 `0` (默认) | 整数标量

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**二进制小数点**。

#### **斜率** — 指定定点数据类型的斜率。 `2^0` (默认) | 正实数值标量

指定定点数据类型的斜率。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**斜率和偏置**。

#### **偏置** — 指定定点数据类型的偏置。 `0` (默认) | 实数值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**斜率和偏置**。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有直通实现。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

**`Simulink.ValueType` 对象支持**

此模块支持 `Simulink.ValueType` 对象的生成代码。有关值类型的详细信息，请参阅Specify Common Set of Signal Properties as Value Type。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Signal Specification block allows you to specify the attributes of the
signal connected to its input and output ports. If the specified attributes conflict with the
attributes specified by the blocks connected to its ports, the software displays an error when
it compiles the model. For example, at the beginning of a simulation, if no conflict exists,
the software eliminates the Signal Specification block from the compiled model.
In other words, the Signal Specification block is a virtual block. It exists
only to specify the attributes of a signal and plays no role in the simulation of the
model.

You can use the Signal Specification block to ensure that the actual
attributes of a signal meet desired attributes. For example, suppose that you and a
colleague are working on different parts of the same model. You use Signal
Specification blocks to connect your part of the model with your
colleague's. If your colleague changes the attributes of a signal without informing you,
the attributes entering the corresponding Signal Specification block do
not match. When you try to simulate the model, you get an error.

You can also use the Signal Specification block to ensure correct propagation
of signal attributes throughout a model. However, if some blocks have unspecified attributes
for the signals they accept or output, the model does not have enough information to propagate
attributes correctly. In these cases, the Signal Specification block can
provide the information the software needs. Using the Signal Specification
block also helps speed up model compilation when blocks are missing signal attributes.

The Signal Specification block supports signal label propagation. For more
information, see Signal Label Propagation.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal whose attributes to check, specified as a scalar, vector, matrix, or N-D
array. The block checks the attributes of the input signal against the
desired attributes you specify in the block dialog box. If the
attributes do not match, the block generates an error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal is the input signal when all attributes of the signal match those
specified in the dialog box. If the attributes do not match, the block
generates an error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Minimum** — Minimum value for range checking `[]` (default) | scalar

Specify the minimum value for the block output as a finite real double scalar
value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the minimum values specified
by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[ ]'` |

### **Maximum** — Maximum value for range checking `[]` (default) | scalar

Specify the maximum value for the block output as a finite real double
scalar value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the maximum values specified
by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[ ]'` |

### **Data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

Specify the desired output data type. If the data type of the input signal
does not match the value you specify, the block generates an error or
warning.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

You can specify any of these options:

- Inherited data type
- Built-in Simulink® data type — For example, specify
  `single` or
  `uint8`. See Data Types Supported by Simulink.
- Fixed-point data type — Use the `fixdt`
  function. For example, specify
  `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded by
  `Enum:`. For example, specify
  `Enum: myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus`
  object preceded by `Bus:`. For example, specify
  `Bus: myBusObject`.
- Simulink image data type — If you have Computer Vision Toolbox™, use the constructor for the `Simulink.ImageType` (Computer Vision Toolbox) object and specify the
  properties to describe the image. By default, the data type uses
  the `Simulink.ImageType(480,640,3)` expression
  that represents the rows, columns, and channels of the image
  respectively.
- Value type — Use the name of the `Simulink.ValueType` object preceded by
  `ValueType:`. For example, specify
  `ValueType: windVelocity`.
- Custom data type — Use a MATLAB® expression that specifies the type. For example,
  you can specify a `Simulink.NumericType` object whose
  `DataTypeMode` property is set to a value
  other than `'Fixed-point: unspecified
  scaling'`.

When you specify a `Simulink.ValueType` or
`Simulink.Bus` object as the data type, some parameters of the
Signal Specification block are ignored. For example, the **Min**,
**Max**, and **Unit** parameters of the
Signal Specification block are ignored. The software uses the corresponding properties of
the `Simulink.ValueType` object or the `Simulink.BusElement` objects
in the `Simulink.Bus` object instead. For example, suppose a block sets
**Unit** to `ft/s`. When the **Data type** of
the block specifies a `ValueType` object that has `m/s` as its
unit, the block uses `m/s` instead of `ft/s`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Value:** `'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Bus: <object name>' | 'ValueType: <object name>' | <data type expression> | Simulink.ImageType(480,640,3)` |
| **Default:** `'Inherit: auto'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the output data
type you specify on the block. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Require nonvirtual bus** — Accept only nonvirtual bus signals `off` (default) | `on`

If you specify a bus object as the data type, use this parameter to
specify whether to accept only nonvirtual bus signals.

- `off` — Specifies that a signal must come from a
  *virtual* bus.
- `on` — Specifies that a signal must come from a
  *nonvirtual* bus.

#### Dependencies

To enable this parameter, the **Data type** block parameter must
resolve to a `Simulink.Bus` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BusOutputAsStruct` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Unit (e.g., m, m/s^2, N\*m)** — Physical unit of the input signal to the block `inherit` (default) | `<Enter unit>`

Specify the physical unit of the input signal to the block. To specify a unit, begin
typing in the text box. As you type, the parameter displays potential matching units.
For a list of supported units, use the `showunitslist` function.

To constrain the unit system, click the link to the right of the parameter:

- If a Unit System Configuration block
  exists in the component, its dialog box opens. Use that dialog box to specify
  allowed and disallowed unit systems for the component.
- If a Unit System Configuration block
  does not exist in the component, the model Configuration Parameters dialog box
  displays. Use that dialog box to specify allowed and disallowed unit systems for
  the model.

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` or `Simulink.Bus` object. The
software uses the units specified by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus` object
instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Unit` |
| **Type:** character vector |
| **Values:** `'inherit'` | `'<Enter unit>'` |
| **Default:** `'inherit'` |

To specify the physical unit of the input signal to the block
without propagation, use `UnitNoProp`.

### **Dimensions (-1 for inherited)** — Dimensions of input and output signals `-1` (default) | `n` | `[m n]`

Specify the dimensions of the input and output signals.

- `-1` — Specifies that signals inherit
  dimensions.
- `n` — Specifies a vector of width
  `n`.
- `[m n]` — Specifies a matrix with
  `m` rows and `n`
  columns.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` object. The
software uses the dimensions specified by the `Simulink.ValueType`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Dimensions` |
| **Type:** character vector |
| **Values:** `'-1'` | `n` | `[m n]` |
| **Default:** `'-1'` |

### **Variable-size signal** — Allow signal to be variable-size, fixed-size, or both `Inherit` (default) | `No` | `Yes`

Specify the signal to be of variable-size, fixed size, or both.

- `Inherit` — Allows variable-size and
  fixed-size signals.
- `No` — Does not allow variable-size
  signals.
- `Yes` — Allows only variable-size
  signals.

When the signal is a variable-size signal, the **Dimensions**
parameter specifies the maximum dimensions of the signal.

#### Dependencies

- When **Data type** specifies a
  `Simulink.Bus` object, the simulation allows variable-size
  signals only with a disabled bus object.
- The software ignores the value of this parameter when **Data
  type** specifies a `Simulink.ValueType` object. The
  software uses the dimensions mode specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VarSizeSig` |
| **Type:** character vector |
| **Values:** `'Inherit'` | `'No'` | `'Yes'` |
| **Default:** `'Inherit'` |

### **Sample time (-1 for inherited)** — Time interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set
this parameter to `-1`. See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** Any valid sample time |
| **Default:** `'-1'` |

### **Signal type** — Complexity of signal `auto` (default) | `real` | `complex`

Specify the complexity of the input and output signals.

- `auto` — Accepts either
  `real` or
  `complex` as the numeric type.
- `real` — Specifies the numeric type as a
  real number.
- `complex` — Specifies the numeric type as
  a complex number.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the complexity specified by
the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SignalType` |
| **Type:** character vector |
| **Values:** `'auto'` | `'real'` | `'complex'` |
| **Default:** `'auto'` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Enumerated` | `Bus object` | `Value type` | `Expression`

Select the category of data to specify. For more information, see Specify Data Types Using Data Type Assistant.

`Inherit`
:   Inheritance rules for data types. Selecting `Inherit` enables
    `auto`.

`Built in`
:   Built-in data types. Selecting `Built in` enables a list of
    possible values:

    - `double` (default)
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
:   Fixed-point data types.

`Enumerated`
:   Enumerated data types. Selecting `Enumerated` enables a text
    box to the right, where you can enter a class name.

`Bus object`
:   Bus object. Selecting `Bus object` enables a text box
    to the right, where you enter the name of a bus object that you want to use to
    define the structure of the bus. To create or change a bus object, click
    **Edit** to the right of the text box.

`Value type`
:   Value type. Selecting `Value type` enables a text box
    to the right, where you enter the name of a value type that you want to use to
    define the properties of the signal. To create or change a value type, click
    **Edit** to the right of the text box.

`Expression`
:   Expressions that evaluate to data types. Selecting
    `Expression` enables a text box to the right, where you
    can enter the expression.

    Do not specify a bus object as the expression.

#### Dependencies

To enable this parameter, click the **Show data type assistant**
button .

### **Signedness** — Signed or unsigned `Signed`

Specify whether the fixed-point data is signed or unsigned. Signed data
can represent positive and negative values, but unsigned data represents
positive values only.

- `Signed`, specifies the fixed-point data
  as signed.
- `Unsigned`, specifies the fixed-point
  data as unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has a pass-through implementation.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**`Simulink.ValueType` Object Support**

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
