---
type: simulink-block
title: 'Outport'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'outport'
---

# Outport

Create output port for subsystem or external output

## 中文

为子系统或外部输出创建输出端口

### 所属库

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sinks

### 描述

Outport 模块将信号从系统内链接到系统外部的目标。它们可以连接从子系统流动到模型其他部分的信号。它们还可以在模型层次结构的顶层提供外部输出。

Outport 模块端口号根据以下规则进行分配：

- 根级系统或子系统中的 Outport 模块按顺序编号，从 1 开始。
- 如果添加一个 Outport 模块，Simulink 将为其分配下一个可用的编号。
- 如果您删除一个 Outport 模块，其他端口号会自动重新编号，以确保 Outport 模块的连续的且没有遗漏任何编号。

#### 子系统中的 Outport 模块

子系统中的 Outport 模块表示来自子系统的输出。到达子系统中某个 Outport 模块的信号将从 Subsystem 模块上的关联输出端口流出。与输出端口关联的 Outport 模块是指**端口号**参数与该输出端口在 Subsystem 模块上的相对位置匹配的模块。例如，**端口号**参数为 `1` 的 Outport 模块将其信号发送给与 Subsystem 模块上最上面的输出端口连接的模块。

如果您对 Outport 模块的**端口号**重新进行编号，模块将连接到一个不同的输出端口。模块会继续将信号发送给子系统外部的同一个模块。

您可以直接编辑 Subsystem 模块上的端口标签。有关详细信息，请参阅 编辑子系统模块上的端口标签。

**提示**

对于包含总线的模型，如果总线信号中包含很多总线元素，则可以考虑使用 In Bus Element 和 Out Bus Element 模块。这些模块可以：

- 减少模块图中信号线的复杂度和杂乱无章。
- 使增量更改接口更容易。
- 允许访问更靠近使用点的总线元素，避免使用 Bus Selector 和 Goto 模块配置。

In Bus Element 模块属于 Inport 模块类型，Out Bus Element 模块属于 Outport 模块类型。

#### 模型层次结构中的顶层 Outport 模块

模型层次结构顶层的 Outport 模块有两种用途。它们可以为 MATLAB® 基础工作区提供外部输出，为 `linmod` 和 `trim` 分析函数提供一种从系统中获取输出的方法。

要为工作区提供外部输出，请使用**配置参数** > **数据导入/导出**窗格（请参阅将输出数据导出到 MATLAB 工作区）或 `sim` 命令。例如，如果系统有多个 Outport 模块，且保存格式为数组，则以下命令

```
[t,x,y] = sim(...);
```

将 `y` 写入为矩阵，每一列均包含一个不同 Outport 模块的数据。列顺序与 Outport 模块的端口号顺序匹配。

如果您在第二个 (state) 参量之后指定多个变量名称，系统会将来自每个 Outport 模块的数据写入不同的变量。例如，如果系统有两个 Outport 模块，要将 Outport 模块 1 的数据保存到 `speed`，将 Outport 模块 2 的数据保存到 `dist`，请指定以下命令：

```
[t,x,speed,dist] = sim(...);
```

#### 将总线连接到根级 Outport

只有当虚拟总线中的所有元素均具有相同的数据类型时，模型中的根级 Outport 模块才会接受虚拟总线。Outport 模块自动将总线统一为与总线具有相同元素数的向量并提供该向量作为输出。

如果希望模型的根级 Outport 模块接受包含混合类型的总线，请将 Outport 模块**数据类型**设置为 `Bus: <object name>`。如果总线为虚拟信号，则被转换为非虚拟信号，如Virtual and Nonvirtual Bus Conversions中所述。

#### 将根级 Outport 模块与 `Simulink.Signal` 对象关联

要将根级 Outport 模块与 `Simulink.Signal` 对象关联，请使用模型数据编辑器。请参阅用于信号。

### 端口

#### 输入

#### **Port\_1** — 输出端口信号 标量 | 向量

通过输出端口流向外部子系统或模型的输入信号。

当 Outport 模块不是根级输出端口时，可以接受定点和枚举数据类型。模块输出的复/实性和数据类型与其输入相同。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`

### 参数

#### 常设

#### **端口号** — 端口在父模块上的位置 `1` (默认) | 实整数

指定与模块对应的端口在父级 Subsystem 或 Model 模块上的显示顺序。

- 如果新添加的模块创建了一个新端口，则其端口号是下一个可用编号。
- 删除与某端口相关联的所有模块后，该端口也会被删除。其他端口会重新编号，使之依序排列且不跳过任何数字。
- 如果指定的端口号超过端口数量，则会为该编号和中间跳过的每个序号创建端口。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Port` |
| **值:** | `"1"` (默认) | real integer in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

#### **信号名称** — 信号名称 `' '` (默认) | 字符向量

指定生成的代码中的相应信号数据的名称。使用此参数可以指定当您将存储类应用到根级 Outport 模块时信号数据的名称。

##### 依赖关系

要启用此参数，该模块必须位于模型的顶层。

##### 编程用法

|  |
| --- |
| **模块参数**：`SignalName` |
| **类型：**字符向量 |
| **值：**字符向量 |
| **默认值：**`' '` |

#### **图标显示** — 图标显示 **端口号** (默认) | **信号名称** | **端口号和信号名称**

指定在模块图标上显示的信息。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconDisplay` |
| **类型：**字符向量 |
| **值**：`'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **默认值**：`'Port number'` |

#### **指定未连接源时的输出** — 指定未连接的输出值 `off` (默认) | `on`

指定未连接信源时的常量输出值。

##### 依赖关系

适用于 Variant Subsystem 模块内未连接的 Outport 模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputWhenUnconnected` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'off'` |

#### **常量值** — 模块未连接时的输出值 `0` (默认) | 标量 | 向量

指定未连接信源时的常量输出值。

##### 依赖关系

适用于未连接的 Outport 模块的 Variant Subsystem 模块（**指定未连接源时的输出**处于选中状态）。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputWhenUnconnectedValue` |
| **类型：**字符向量 |
| **值：**`scalar` | `vector` |
| **默认值：**`'0'` |

#### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，选中此复选框将输出长度为 `N` 的向量。

##### 依赖关系

适用于未连接的 Outport 模块上的 Variant Subsystem 模块（当您选择了**指定未连接源时的输出**参数时）。

##### 编程用法

|  |
| --- |
| **模块参数**：`VectorParamsAs1DForOutWhenUnconnected` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

#### **确保输出端口为虚拟端口** — 确保输出端口为虚拟 `off` (默认) | `on`

清除此参数可允许 Simulink® 在输出端口上使用信号缓冲区。此缓冲区等效于 Signal Conversion 模块，但不显示在画布上，可确保 Outport 模块信号的初始化保持一致。

如果选择此参数，Simulink 会尝试删除信号缓冲区。

- 如果不需要信号缓冲区，Simulink 将删除缓冲区。
- 如果为确保数据一致性和正常执行而需要信号缓冲区，Simulink 会显示错误，指示可能无法删除缓冲区。

允许通过 Assignment 模块部分写入。

有关此参数的详细信息，包括具有条件写入和部分写入的示例，请参阅Ensure Output Port Is Virtual。

**注意**

如果该模块位于模型的根级，并且由 Initialize Function 模块、Reset Function 模块、Reinitialize Function 模块或 Terminate Function 模块内的另一个 Outport 模块驱动，则该模块始终为虚拟模块。

##### 依赖关系

此参数适用于以下模块：

- 条件子系统
- Assignment
- Merge
- 具有根 Outport 模块的模型

##### 编程用法

|  |
| --- |
| **模块参数**：`EnsureOutportIsVirtual` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'off'` |

#### **禁用时的输出** — 禁用时的输出 **保持** (默认) | **重置**

指定子系统被禁用的情况下，模块输出会出现什么情况。选择**保持**表示当子系统被禁用时，输出保持不变。选择**重置**表示当子系统被禁用时，输出将重置为**初始输出**指定的值。

##### 依赖关系

当 Outport 模块位于具有有效启用和禁用语义的条件子系统中时可用。例如，该参数适用于 Enabled Subsystem 模块内的 Outport 模块，不适用于 Triggered Subsystem 模块内的 Outport 模块。

如果 Outport 模块位于 Function-Call Subsystem 模块内，则仅当 Function-Call Subsystem 模块连接到 Stateflow® 图中的某个状态时，此参数才有意义。有关详细信息，请参阅Bind a Function-Call Subsystem to a State (Stateflow)。

将条件子系统的输出连接到 Merge 模块时，请将此参数设置为**保持**。将其设置为**重置**会返回错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputWhenDisabled` |
| **类型：**字符向量 |
| **值**：`'held' | 'reset'` |
| **默认值：**`'held'` |

#### **初始输出** — 条件执行子系统的初始输出 `[]` (默认) | 标量 | 结构体

对于条件执行子系统，请在子系统执行之前且此选项处于禁用状态时指定模块输出。要从输入信号继承初始输出值，请应用以下两种默认设置：

- 将**初始输出**参数设置为 `[]`。
- 将**禁用时的输出**参数设置为**保持**。

Simulink 尝试从输入信号继承输出值。然而，如果输入信号不是初始输出值的有效源，则初始输出值 `[]` 被视为 `double(0)`。有关详细信息，请参阅条件子系统初始输出值。

有关指定初始条件结构体的信息，请参阅Specify Initial Conditions for Bus Elements。

##### 提示

如果条件子系统驱动的是 Merge 模块，则无需为 Outport 模块指定初始条件 (IC)。有关详细信息，请参阅 Underspecified initialization detection。

##### 依赖关系

当 Outport 模块位于条件子系统内部时可用。

##### 限制

- 此模块不允许初始输出为 `inf` 或 `NaN`。
- 当输入是虚拟总线时，**初始输出**值 `[]` 被视为 `double(0)`。
- 当输入包含非虚拟总线时，**初始输出**不支持非零标量值。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型：**字符向量 |
| **值：**`'[]'` | 标量 | 结构体 |
| **默认值：**`'[]'` |

#### 信号属性

#### **最小** — 最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

此数字必须为有限双精度实数标量值。

软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最小值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

#### **最大** — 最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

此数字必须为有限双精度实数标量值。

软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最大值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[ ]'`| 标量 |
| **默认值**：`'[ ]'` |

#### **数据类型** — 输出数据类型 **Inherit: auto** (默认) | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | ...

指定外部输入的输出数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType` 对象。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

您可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink 数据类型 - 例如，指定 **single** 或 **uint8**。请参阅 Simulink 支持的数据类型。
- 定点数据类型 - 使用 `fixdt` 函数。例如，指定 **fixdt(1,16,0)**。
- 枚举数据类型 - 使用以 `Enum:` 开头的类型名称。例如，指定 **Enum: myEnumType**。
- 总线数据类型 - 使用以 `Bus:` 开头的 `Simulink.Bus` 对象的名称。例如，指定 **Bus: myBusObject**。
- Simulink 图像数据类型 - 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数，并指定描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式，分别表示图像的行、列和通道。
- 值类型 - 使用以 `ValueType:` 开头的 `Simulink.ValueType` 对象的名称。例如，指定 **ValueType: windVelocity**。
- 自定义数据类型 - 使用指定类型的 MATLAB 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `'Fixed-point: unspecified scaling'` 以外的值。

当您指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象作为数据类型时，会忽略 Outport 模块的一些参数。例如，忽略 Outport 模块的 **Min**、**Max** 和 **Unit** 参数。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象的对应属性。例如，假设一个模块将**单位**设置为 `ft/s`。当该模块的**数据类型**指定以 `m/s` 为单位的 `ValueType` 对象时，该模块会使用 `m/s` 而不是 `ft/s` 作为单位。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` | `Simulink.ImageType(480,640,3)` |
| **默认值**：`'Inherit: auto'` |

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

#### **在父模型中以非虚拟总线输出** — 在父模型中以非虚拟总线输出 `off` (默认) | `on`

指定输出总线在父模型中作为非虚拟总线。如果您希望父模型中出现的总线为非虚拟总线，请选择此参数。输入到该端口的总线可以是虚拟或非虚拟总线，无论**在父模型中以非虚拟总线输出**的设置如何。

如果您希望父模型中出现的总线为虚拟总线，则请清除此参数。

##### 提示

- 在非虚拟总线中，所有信号必须具有相同的采样时间，即使关联总线对象的元素指定继承采样时间也是如此。任何操作如果可能会生成违反此要求的非虚拟总线，都会生成错误。有关详细信息，请参阅Modify Sample Times for Nonvirtual Buses。

  要对虚拟总线使用多速率信号，请将根级 Outport 模块的**采样时间**参数设置为继承 (`-1`)。
- 对于模型引用层次结构的顶层模型，代码生成将创建 C 结构体，以表示此模块输出的总线。
- 对于引用的模型，选择此选项将创建 C 结构体。否则，代码生成过程将为总线的每个叶元素创建一个参量。

##### 依赖关系

要启用此参数，**数据类型**必须解析为 `Simulink.Bus` 对象。例如，将**数据类型**设置为 `Simulink.Bus` 对象，或设置为将 `Simulink.Bus` 对象指定为其数据类型的 `Simulink.ValueType` 对象。

##### 编程用法

|  |
| --- |
| **模块参数**： `BusOutputAsStruct` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

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

#### **端口维度(-1 表示继承)** — 端口维度 `-1` (默认) | 整数 | [整数, 整数]

指定信号要连接到此 Outport 模块所必须具有的维度。

|  |  |
| --- | --- |
| `-1` | 任意维度的信号都可以连接到此端口。 |
| `N` | 连接到此端口的信号必须是大小为 `N` 的向量。 |
| `[R C]` | 连接到此端口的信号必须是具有 `R` 行和 `C` 列的矩阵。 |

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度。

##### 编程用法

|  |
| --- |
| **模块参数**： `PortDimensions` |
| **类型**：字符向量 |
| **值**：`'-1'` | 整数 | [整数, 整数] |
| **默认值**：`'-1'` |

#### **可变大小信号** — 允许可变大小信号 **继承** (默认) | **否** | **是**

指定此端口的输出端允许的信号类型。要同时允许可变大小和固定大小的信号，请选择 **inherit**。要仅允许可变大小信号，请选择**是**。要仅允许固定大小的信号，请选择**否**。

当此端口的信号为可变大小的信号时，**端口维度**参数将指定信号的最大维度。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度模式。

##### 编程用法

|  |
| --- |
| **参数：** `VarSizeSig` |
| **类型：**字符向量 |
| **值：**`'Inherit'` | `'No'` | `'Yes'` |
| **默认值：**`'Inherit'` |

#### **信号类型** — 输出信号类型 **自动** (默认) | **实数** | **复**

指定信号输出的数值类型。要选择连接到其输入的信号的数值类型，请选择**自动**。否则，请选择实信号或复信号类型。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的复/实性。

##### 编程用法

|  |
| --- |
| **模块参数**：`SignalType` |
| **类型：**字符向量 |
| **值**：`'auto'` | `'real'` | `'complex'` |
| **默认值：**`'auto'` |

#### 执行

#### **采样时间(-1 表示继承)** — 指定采样时间的选项 `-1` (默认) | 标量

指定采样时间命中点之间的离散间隔，或指定另一个采样时间类型，如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅采样时间的类型。

默认情况下，模块根据模型中的模块上下文继承其采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'-1'` |

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

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **BalanceDelays** | | **BalanceDelays** 设置 | 描述 | | --- | --- | | **on**（默认值） | 检测 DUT 中其他路径上引入的延迟，并在 Outport 模块路径上插入匹配的延迟。 | | **off** | 在 DUT 子系统的输出端口上禁用延迟平衡，以防止 HDL Coder 插入不必要的匹配延迟。例如，当将手动添加的输出端口视为测试点时，可禁用 DUT 子系统中 Outport 模块上的 **BalanceDelays**。 |  **注意**  此属性仅影响 DUT 级别的  Outport 模块。 |
| **BidirectionalPort** | | **BidirectionalPort** 设置 | 描述 | | --- | --- | | **on** | 将端口指定为双向。  需满足以下要求：  - 端口必须位于采用黑盒实现的 Subsystem 模块中。 - 同时，双向端口与对应的顶层 DUT 子系统端口之间不能有逻辑关系。  有关详细信息，请参阅 Specify Bidirectional Ports (HDL Coder)。 | | **off**（默认值） | 不将端口指定为双向。 | |

| 目标设定 | |
| --- | --- |
| **IOInterface** | DUT 端口的目标平台接口类型，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterface` 模块属性被忽略。  要指定有效的 `IOInterface` 设置，请使用 HDL 工作流顾问：  1. 在 HDL 工作流顾问中，在**设置目标** > **设置目标接口**步骤中，请在**目标平台接口表**中的**目标平台接口**列中，使用下拉列表设置目标平台接口类型。 2. 保存模型。  `IOInterface` 值保存为端口的 HDL 模块属性。  例如，要查看 `IOInterface` 值，如果 DUT 端口的完整路径是 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | DUT 端口的目标平台接口端口映射，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceMapping` 模块属性被忽略。  要指定有效的 `IOInterfaceMapping` 设置，请使用 HDL 工作流顾问：  1. 在 HDL 工作流顾问中，在**设置目标** > **设置目标接口**步骤中，请在**目标平台接口表**中的**目标平台接口**列中，使用下拉列表设置目标平台接口类型。 2. 在**位范围 / 地址 / FPGA 引脚**列中，如果要更改默认值，请输入目标平台接口映射。 3. 保存模型。  `IOInterfaceMapping` 值保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceMapping` 值，如果 DUT 端口的完整路径是 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | DUT 端口的目标平台接口端口映射选项，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceOptions` 模块属性被忽略。  要指定有效的 `IOInterfaceOptions` 设置，请使用 HDL 工作流顾问：  1. 在 HDL 工作流顾问的**设置目标** > **设置目标接口**步骤中，在**目标平台接口表**中的**目标平台接口**列中，将输入或输出端口映射到 AXI4 下级接口。 2. 在**接口选项**列中，如果要更改默认初始值，请点击**选项**按钮，并为 **RegisterInitialValue** 输入值。 3. 保存模型。  `IOInterfaceOptions` 值保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceOptions` 值，如果 DUT 端口的完整路径是 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

**`Simulink.ValueType` 对象支持**

此模块支持 `Simulink.ValueType` 对象的生成代码。有关值类型的详细信息，请参阅Specify Common Set of Signal Properties as Value Type。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2025a: 记录 `datetime` 数据

Outport 模块支持记录 `datetime` 数据。

#### R2024a: **初始输出值的源**参数已删除

从 R2024a 开始，对于条件执行子系统，初始输出值继承自子系统的输入信号。软件将**初始输出**参数设置为 `[]`，并将**禁用时的输出**参数设置为**保持**。

#### R2023b: 记录无界可变大小信号

在普通和加速模式仿真中，Outport 模块支持记录无界可变大小信号。不支持记录包含无界可变大小信号的非虚拟总线。

## Libraries

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sinks

## Description

Outport blocks link signals from a system to a destination outside of
the system. They can connect signals flowing from a subsystem to other parts of the
model. They can also supply external outputs at the top level of a model
hierarchy.

Outport block port numbers are assigned according to these rules:

- Outport blocks within a root-level system or subsystem are
  numbered sequentially, starting with 1.
- If you add an Outport block, it is assigned the next available
  number.
- If you delete an Outport block, other port numbers are
  automatically renumbered to ensure that the Outport blocks are in
  sequence and that no numbers are omitted.

### Outport Blocks in a Subsystem

Outport blocks in a subsystem represent outputs from the subsystem. A signal
arriving at an Outport block in a subsystem flows out of the
associated output port on that Subsystem block. The Outport block
associated with an output port is the block whose **Port
number** parameter matches the relative position of the output port on
the Subsystem block. For example, the Outport block whose **Port number** parameter is `1` sends its
signal to the block connected to the topmost output port on the
Subsystem block.

If you renumber the **Port number** of an
Outport block, the block becomes connected to a different output
port. The block continues to send the signal to the same block outside the
subsystem.

You can directly edit port labels on a Subsystem block. For more
information, see Edit Port Labels on Subsystem Blocks.

**Tip**

For models that include buses composed of many bus elements, consider using In Bus
Element and Out Bus Element blocks. These
blocks:

- Reduce signal line complexity and clutter in a block diagram.
- Make it easier to change the interface incrementally.
- Allow access to a bus element closer to the point of usage, avoiding
  the use of a Bus Selector and Goto block
  configuration.

The In Bus Element block is of block type Inport
and the Out Bus Element block is of block type
Outport.

### Top-Level Outport Block in a Model Hierarchy

Outport blocks at the top level of a model hierarchy have two uses. They can
supply external outputs to the base MATLAB® workspace, and they provide a means for the `linmod`
and `trim` analysis functions to obtain output from the
system.

To supply external outputs to the workspace, use the **Configuration Parameters** > **Data Import/Export** pane (see Exporting Output Data to
the MATLAB Workspace) or the `sim` command. For example, if a system has more than one
Outport block and the save format is array, this command

```
[t,x,y] = sim(...);
```

writes `y` as a matrix, with each column containing data for a
different Outport block. The column order matches the order of the
port numbers for the Outport blocks.

If you specify more than one variable name after the second (state) argument, data
from each Outport block is written to a different variable. For
example, if the system has two Outport blocks, to save data from
Outport block 1 to `speed` and the data from
Outport block 2 to `dist`, specify this
command:

```
[t,x,speed,dist] = sim(...);
```

### Connecting Buses to Root-Level Outports

A root-level Outport block in a model can accept a virtual bus only if all
elements of the bus have the same data type. The Outport block
automatically unifies the bus to a vector having the same number of elements as the
bus, and provides that vector as output.

If you want a root-level Outport block of a model to accept a bus that
contains mixed types, set the Outport block **Data
type** to `Bus: <object name>`. If the bus is
virtual, it is converted to nonvirtual, as described in Virtual and Nonvirtual Bus Conversions.

### Associate Root-Level Outport Block with `Simulink.Signal` Object

To associate a root-level Outport block with a
`Simulink.Signal` object, use the Model Data Editor. See For Signals.

## Ports

### Input

### **Port\_1** — Outport signal scalar | vector

Input signal that flows through the outport to an external subsystem or model.

An Outport block can accept fixed-point and enumerated data types when
the block is not a root-level output port. The complexity and data type
of the block output are the same as its input.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`

## Parameters

### Main

### **Port number** — Position of port on parent block `1` (default) | real integer

Specify the order in which the port that corresponds to the block appears on the parent
Subsystem or Model block.

- If you add a block that creates another port, the port number is the next available
  number.
- Deleting all blocks associated with a port deletes the port. Other ports are
  renumbered so that they are sequential and do not skip any numbers.
- Specifying a port number that exceeds the number of ports creates a port for that
  number and for any skipped sequential numbers.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **Values:** | `"1"` (default) | real integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

### **Signal name** — Signal name `' '` (default) | character vector

Specify the name of the corresponding signal data in the generated
code. Use this parameter to specify a name for the signal data when you
apply a storage class to a root-level Outport
block.

#### Dependencies

To enable this parameter, the block must be at the top level of a
model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalName` |
| **Type:** character vector |
| **Values:** character vector |
| **Default:** `' '` |

### **Icon display** — Icon display `Port number` (default) | `Signal name` | `Port number and signal name`

Specify the information displayed on the block icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **Default:** `'Port number'` |

### **Specify output when source is unconnected** — Specify unconnected output value `off` (default) | `on`

Specify a constant output value for when source is not
connected.

#### Dependencies

Available for unconnected Outport blocks inside a Variant
Subsystem block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWhenUnconnected` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Constant value** — Output value when the block is not connected `0` (default) | scalar | vector

Specify a constant output value for when source is not
connected.

#### Dependencies

Available in a Variant Subsystem block for an unconnected
Outport block with **Specify output when
source is unconnected** selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWhenUnconnectedValue` |
| **Type:** character vector |
| **Values:** `scalar` | `vector` |
| **Default:** `'0'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to create a vector of length `N` at the output if
the **Constant value** parameter evaluates
to an `N`-element row or column vector.

#### Dependencies

Available in a Variant Subsystem block on an unconnected
Outport block when you select the
**Specify output when source is unconnected**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParamsAs1DForOutWhenUnconnected` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Ensure outport is virtual** — Ensure that outport is virtual `off` (default) | `on`

Clear this parameter to allow Simulink® to use a signal buffer on output port. This buffer, which
is the equivalent of a Signal Conversion block
but is not displayed on the canvas, ensures consistent initialization of
the Outport block signal.

If you select this parameter, Simulink tries to remove the signal buffer.

- If the signal buffer is not needed, Simulink removes the buffer.
- If the signal buffer is needed for data consistency and
  proper execution, Simulink displays an error indicating the buffer could
  not be removed.

Allow partial writes through Assignment
blocks.

For more information regarding this parameter, including examples with conditional
writes and partial writes, see Ensure Output Port Is Virtual.

**Note**

The block is always virtual if it is at the root-level of a model
and is driven by another Outport block inside an
Initialize Function
block, a Reset Function
block, a Reinitialize Function block or a Terminate Function
block.

#### Dependencies

This parameter applies to these blocks and this configuration parameter setting:

- Conditional subsystem
- Assignment
- Merge
- Model with root Outport block
- The **Underspecified
  initialization detection** configuration
  parameter must be set to
  `Simplified`. This block
  parameter is not available when the
  `Classic` option of the configuration
  parameter is selected. For more information about how to
  switch from classic to simplified initialization mode, see
  Convert from Classic to Simplified Initialization Mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EnsureOutportIsVirtual` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Output when disabled** — Output when disabled `held` (default) | `reset`

Specify what happens to the block output when the subsystem is
disabled. Select `held` to indicate that the
output is held when the subsystem is disabled. Select
`reset` to indicate that the output is
reset to the value given by **Initial output** when the
subsystem is disabled.

#### Dependencies

Available when an Outport block is inside a conditional subsystem with
valid enabling and disabling semantics. For example, the parameter
is available for an Outport block inside an
Enabled Subsystem block and not for an
Outport block inside a Triggered
Subsystem block.

If an Outport block is inside a Function-Call Subsystem
block, this parameter is only meaningful if the Function-Call
Subsystem block is connected to a state in a Stateflow® chart. For more information, see Bind a Function-Call Subsystem to a State (Stateflow).

When connecting the output of a conditional subsystem to a Merge block, set
this parameter to `held`. Setting it to
`reset` returns an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWhenDisabled` |
| **Type:** character vector |
| **Values:** `'held' | 'reset'` |
| **Default:** `'held'` |

### **Initial output** — Initial output for conditionally executed subsystems `[]` (default) | scalar | structure

For conditionally executed subsystems, specify the block output before the subsystem
executes and while it is disabled. To inherit the initial output value
from the input signal, apply both of these default settings:

- Set **Initial output** parameter to
  `[]`.
- Set **Output when
  disabled** parameter to
  `held`.

Simulink attempts to inherit the output value from the input
signal. However, if the input signal is not a valid source for the
initial output value, the initial output value `[]` is
treated as `double(0)`. For more information, see Conditional Subsystem Initial Output Values.

For information about specifying an initial condition structure, see
Specify Initial Conditions for Bus Elements.

#### Tips

If the conditional subsystem is driving a Merge
block, you do not need to specify an Initial Condition (IC) for the
Outport block. For more information, see Underspecified initialization detection.

#### Dependencies

Available when an Outport block is inside a conditional
subsystem.

#### Limitations

- This block does not allow an initial output of
  `inf` or
  `NaN`.
- When the input is a virtual bus, an **Initial
  output** value `[]` is
  treated as `double(0)`.
- When the input contains a nonvirtual bus,
  **Initial output** does not support
  nonzero scalar values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector |
| **Values:** `'[]'` | scalar | structure |
| **Default:** `'[]'` |

### Signal Attributes

### **Minimum** — Minimum output value `[]` (default) | scalar

Lower value of the output range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` or `Simulink.Bus` object. The
software uses the minimum values specified by the `Simulink.ValueType` object
or the `Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Maximum** — Maximum output value `[]` (default) | scalar

Upper value of the output range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

The software ignores the value of this parameter when **Data type**
specifies a `Simulink.ValueType` or `Simulink.Bus` object. The
software uses the maximum values specified by the `Simulink.ValueType` object
or the `Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

Specify the output data type of the external input. The type can be
inherited, specified directly, or expressed as a data type object such
as a `Simulink.NumericType` object.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

You can specify any of these options:

- Inherited data type
- Built-in Simulink data type — For example, specify
  `single` or
  `uint8`. See Data Types Supported by Simulink.
- Fixed-point data type — Use the `fixdt`
  function. For example, specify
  `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded
  by `Enum:`. For example, specify
  `Enum: myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus` object preceded by
  `Bus:`. For example, specify
  `Bus: myBusObject`.
- Simulink image data type — If you have Computer Vision Toolbox™, use the constructor for the `Simulink.ImageType` (Computer Vision Toolbox) object and specify the
  properties to describe the image. By default, the data type
  uses the `Simulink.ImageType(480,640,3)`
  expression that represents the rows, columns, and channels
  of the image respectively.
- Value type — Use the name of the `Simulink.ValueType` object preceded by
  `ValueType:`. For example, specify
  `ValueType:
  windVelocity`.
- Custom data type — Use a MATLAB expression that specifies the type. For
  example, you can specify a `Simulink.NumericType` object whose
  `DataTypeMode` property is set to a
  value other than `'Fixed-point: unspecified
  scaling'`.

When you specify a `Simulink.ValueType` or
`Simulink.Bus` object as the data type, some parameters of the
Outport block are ignored. For example, the **Min**,
**Max**, and **Unit** parameters of the
Outport block are ignored. The software uses the corresponding properties of
the `Simulink.ValueType` object or the `Simulink.BusElement` objects
in the `Simulink.Bus` object instead. For example, suppose a block sets
**Unit** to `ft/s`. When the **Data type** of
the block specifies a `ValueType` object that has `m/s` as its
unit, the block uses `m/s` instead of `ft/s`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` | `Simulink.ImageType(480,640,3)` |
| **Default**: `'Inherit: auto'` |

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

### **Output as nonvirtual bus in parent model** — Output as nonvirtual bus in parent model `off` (default) | `on`

Specify the outport bus to be nonvirtual in the parent model. Select this
parameter if you want the bus emerging in the parent model to be nonvirtual. The bus
that is input to the port can be virtual or nonvirtual, regardless of the setting of
**Output as nonvirtual bus in parent model**.

Clear this parameter if you want the bus emerging in the parent model to be
virtual.

#### Tips

- In a nonvirtual bus, all signals must have the same sample time, even if the
  elements of the associated bus object specify inherited sample times. Any
  operation that would result in a nonvirtual bus that violates this requirement
  generates an error. For details, see Modify Sample Times for Nonvirtual Buses.

  To use a multirate signal for a virtual bus, in the root-level
  Outport block, set the **Sample time**
  parameter to inherited (`-1`).
- For the top model in a model reference hierarchy, code generation creates a
  C structure to represent the bus output of this block.
- For referenced models, select this option to create a C structure.
  Otherwise, code generation creates an argument for each leaf element of the
  bus.

#### Dependencies

To enable this parameter, **Data type** must resolve to a
`Simulink.Bus` object. For example, set **Data
type** to a `Simulink.Bus` object or a
`Simulink.ValueType` object that specifies a
`Simulink.Bus` object as its data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BusOutputAsStruct` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

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

### **Port dimensions (-1 for inherited)** — Port dimensions `-1` (default) | integer | [integer, integer]

Specify the dimensions that a signal must have to be connected to this Outport
block.

|  |  |
| --- | --- |
| `-1` | A signal of any dimensions can be connected to this port. |
| `N` | The signal connected to this port must be a vector of size `N`. |
| `[R C]` | The signal connected to this port must be a matrix having `R` rows and `C` columns. |

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` object. The
software uses the dimensions specified by the `Simulink.ValueType`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PortDimensions` |
| **Type**: character vector |
| **Values**: `'-1'` | integer | [integer, integer] |
| **Default**: `'-1'` |

### **Variable-size signal** — Allow variable-size signals `Inherit` (default) | `No` | `Yes`

Specify the type of signals allowed at the output of this port. To allow
variable-size and fixed-size signals, select `Inherit`. To
allow only variable-size signals, select `Yes`. To allow only
fixed-size signals, select `No`.

When the signal at this port is a variable-size signal, the **Port
dimensions** parameter specifies the maximum dimensions of the
signal.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` object. The
software uses the dimensions mode specified by the
`Simulink.ValueType` object instead.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `VarSizeSig` |
| **Type:** character vector |
| **Value:** `'Inherit'` | `'No'` | `'Yes'` |
| **Default:** `'Inherit'` |

### **Signal type** — Output signal type `auto` (default) | `real` | `complex`

Specify the numeric type of the signal output. To choose the numeric type of the
signal that is connected to its input, select `auto`.
Otherwise, choose a real or complex signal type.

#### Dependencies

The software ignores the value of this parameter when **Data
type** specifies a `Simulink.ValueType` or
`Simulink.Bus` object. The software uses the complexity specified
by the `Simulink.ValueType` object or the
`Simulink.BusElement` objects in the `Simulink.Bus`
object instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalType` |
| **Type:** character vector |
| **Values:** `'auto'` | `'real'` | `'complex'` |
| **Default:** `'auto'` |

### Execution

### **Sample time (-1 for inherited)** — Option to specify sample time `-1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`-1`). For more options, see Types of Sample Time.

By default, the block inherits its sample time based upon the context of the block
within the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'-1'` |

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

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **BalanceDelays** | | **BalanceDelays** Setting | Description | | --- | --- | | `on` (default) | Detects introduction of delays on other paths in the DUT and inserts matching delays on the Outport block path. | | `off` | Disable delay balancing on output ports in your DUT subsystem to prevent HDL Coder from inserting matching delays when they are unnecessary. For example, disable **BalanceDelays** on an Outport block in your DUT subsystem when treating a manually added output port as a test point. |  **Note**  This property affects only DUT-level  Outport blocks. |
| **BidirectionalPort** | | **BidirectionalPort** Setting | Description | | --- | --- | | `on` | Specify the port as bidirectional.  The following requirements apply:  - The port must be in a Subsystem block   with black box implementation. - There must also be no   logic between the bidirectional port and the corresponding top-level   DUT subsystem port.  For more information, see Specify Bidirectional Ports (HDL Coder). | | `off` (default) | Do not specify the port as bidirectional. | |

| Target Specification | |
| --- | --- |
| **IOInterface** | Target platform interface type for DUT ports, specified as a character vector. The `IOInterface` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterface` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, in the **Set Target** > **Set Target Interface** step, in the **Target platform interface table**,    in the **Target Platform Interfaces** column, use    the drop-down list to set the target platform interface type. 2. Save the model.  The `IOInterface` value is saved as an HDL    block property of the port.  For example, to view the `IOInterface` value,    if the full path to your DUT port is `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | Target platform interface port mapping for DUT ports, specified as a character vector. The `IOInterfaceMapping` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterfaceMapping` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, in the **Set Target** > **Set Target Interface** step, in the **Target platform interface table**,    in the **Target Platform Interfaces** column, use    the drop-down list to set the target platform interface type. 2. In the **Bit Range / Address / FPGA Pin** column,    if you want to change the default value, enter a target platform interface    mapping. 3. Save the model.  The `IOInterfaceMapping` value is saved as    an HDL block property of the port.  For example, to view the `IOInterfaceMapping` value,    if the full path to your DUT port is `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | Target platform interface port mapping options for DUT ports, specified as a character vector. The `IOInterfaceOptions` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterfaceOptions` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, on the **Set Target** > **Set Target Interface** step, in the **Target    platform interface table**, in the    **Target Platform Interfaces**    column, map the input or output ports to an AXI4    subordinate interface. 2. In the **Interface    Options** column, if you want to change    the default initial value, click the    **Options** button and enter a    value for    **RegisterInitialValue**. 3. Save the model.  The `IOInterfaceOptions`    value is saved as an HDL block property of the    port.  For example, to view the    `IOInterfaceOptions` value, if    the full path to your DUT port is    `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

**`Simulink.ValueType` Object Support**

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2025a: Log `datetime` data

The Outport block supports logging `datetime` data.

### R2024a: **Source of initial output value** parameter has been removed

Starting in R2024a, for conditionally executed subsystems, the initial output value is
inherited from the input signal of the subsystem. The software sets the
**Initial output** parameter to `[]` and
**Output when disabled** parameter to
`held`.

### R2023b: Log unbounded variable-size signals

In normal and accelerator mode simulations, the Outport block supports
logging unbounded variable-size signals. Logging is not supported for nonvirtual
buses that contain unbounded variable-size signals.
