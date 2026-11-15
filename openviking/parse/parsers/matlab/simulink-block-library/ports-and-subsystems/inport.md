---
type: simulink-block
title: 'Inport'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'inport'
---

# Inport

Create input port for subsystem or external input

## 中文

为子系统或外部输入创建输入端口

### 所属库

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sources

### 描述

Inport 模块将信号从系统外部链接到系统内。

软件根据以下规则分配 Inport 模块端口号：

- 根级系统或子系统中的 Inport 模块按顺序编号，从 1 开始。
- 如果添加 Inport 模块，标签将是下一个可用的编号。
- 如果您删除一个 Inport 模块，其他端口号会重新编号，以确保 Inport 模块的连续的且没有遗漏任何编号。
- 如果将 Inport 模块复制到系统中，其端口号不会重新编号，除非当前编号与系统中已存在的输入端口发生冲突。如果复制的 Inport 模块的端口号不符合顺序，则会对该模块重新进行编号。否则，当您仿真模型或更新模块图时，会出现一条错误消息。

#### 顶层系统中的 Inport 模块

您可以在顶层系统中使用 Inport 模块，以进行以下操作：

- 使用**输入**参数提供来自工作区的外部输入。如果不提供外部输入数据，则 Inport 模块的输出为接地值。有关详细信息，请参阅将数据加载到根级输入端口。

  - 要使用根级输入端口加载多个信号的数据，请考虑使用根输入端口映射器工具。请参阅使用根输入端口映射器工具映射数据。
  - 使用 `createInputDataset` 函数创建 `Simulink.SimulationData.Dataset` 对象，该对象包含与您指定的模型中每个根级 Inport 模块对应的元素。
- 通过 `linmod` 和 `trim` 分析函数提供模型扰动的方式。有关详细信息，请参阅线性化模型。

#### 子系统中的 Inport 模块

子系统中的 Inport 模块表示子系统的输入。到达 Subsystem 模块上的输入端口的信号从该子系统中的关联 Inport 模块流出。与 Subsystem 模块上的输入端口关联的 Inport 模块是其**端口号**参数与 Subsystem 模块上输入端口的相对位置匹配的模块。例如，**端口号**参数为 `1` 的 Inport 模块从连接到 Subsystem 模块上最顶层端口的模块获取其信号。

如果对 Inport 模块的**端口号**重新编号，则该模块将连接到其他输入端口。该模块继续从子系统外的同一模块接收其信号。

子系统内的 Inport 模块支持信号标签传播，但根级 Inport 模块不支持。有关详细信息，请参阅信号标签传播。

您可以直接编辑 Subsystem 模块上的端口标签。有关详细信息，请参阅 编辑子系统模块上的端口标签。

**提示**

对于包含总线的模型，如果总线信号中包含很多总线元素，则可以考虑使用 In Bus Element 和 Out Bus Element 模块。这些模块可以：

- 减少模块图中信号线的复杂度和杂乱无章。
- 使增量更改接口更容易。
- 允许访问更靠近使用点的总线元素，避免使用 Bus Selector 和 Goto 模块配置。

In Bus Element 模块属于 Inport 模块类型，Out Bus Element 模块属于 Outport 模块类型。

#### 创建重复 Inport 模块

您可以创建任意数量的 Inport 模块副本。副本是原型的图形表示，旨在通过去除不必要的线条来简化模块图。副本与原型具有相同的端口号、属性和输出。

要创建 Inport 模块的副本，请执行以下操作：

1. 在模块图中，选择要复制的未连接的 Inport 模块。
2. 按住 **Ctrl** 键并拖动模块。
3. 释放指针，然后从上下文菜单中选择**生成副本**。

您可以选择具有副本的 Inport 模块来突出显示副本模块。要在打开的图或新选项卡中显示相关模块，请使用光标在选择后出现的省略号上暂停。然后，从操作菜单中选择**相关模块** 。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

#### 将总线连接到根级 Inport 模块

如果您希望模型的根级 Inport 模块生成总线，请将**数据类型**参数设置为总线对象的名称（该总线对象定义 Inport 模块生成的总线）。有关详细信息，请参阅使用总线对象指定总线属性。

### 端口

#### 输出

#### **Port\_1** — 输入信号 标量 | 向量

通过输入端口流入系统的输入信号。

您可以在子系统中使用 Inport 模块，以结构体或任何其他格式提供定点数据。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

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

#### **图标显示** — 图标显示 **端口号** (默认) | **信号名称** | **端口号和信号名称**

指定在模块图标上显示的信息。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconDisplay` |
| **类型：**字符向量 |
| **值**：`'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **默认值**：`'Port number'` |

#### **通过延迟外部信号锁存输入** — 通过延迟锁存信号的选项 `off` (默认) | `on`

选择此项以指定模块输出是上一个时间步的输入信号值。

选择此选项将使软件能够解析属于某个循环的触发子系统之间的数据依赖关系。

Inport 模块通过显示 `<Lo>` 来指示已选择此选项。

##### 依赖关系

仅当模块表示触发子系统中的输入端口时，才会启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`LatchByDelayingOutsideSignal` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'off'` |

#### **针对函数调用子系统输出的反馈信号锁存输入** — 锁存信号以防止更改 `off` (默认) | `on`

选择此选项可指定模块锁存输入值，并防止它在函数调用子系统执行期间发生更改。对于分支出来调用多个函数调用子系统的单次函数调用，使用此选项会中断当信号从一个函数调用子系统反馈到另一个函数调用子系统时形成的循环。选择此选项可防止在包含此模块的子系统执行期间调用的函数调用子系统的反馈信号值发生任何更改。

Inport 模块通过显示 `<Li>` 来指示已选择此选项。

##### 依赖关系

仅当模块表示函数调用子系统中的输入端口时，才会启用此选项。

##### 编程用法

|  |
| --- |
| **模块参数**：`LatchInputForFeedbackSignals` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'off'` |

#### **连接输入** — 打开根输入端口映射器工具的选项 按钮

要将信号和总线数据导入、可视化并映射到根级 Inport 模块，请点击此按钮。根输入端口映射器工具将打开。

##### 依赖关系

仅当模块位于模型的根级时，此按钮才会出现。

#### 信号属性

#### **输出函数调用** — 产生函数调用事件的选项 `off` (默认) | `on`

指定输入信号产生函数调用事件信号。

如果当前模型在顶层模型中被引用时必须接受函数调用事件信号，请选择此选项。

##### 依赖关系

- 要启用此选项，该模块必须在异步函数调用中。
- 当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputFunctionCall` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

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

指定外部输入的输出数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

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

当您指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象作为数据类型时，会忽略 Inport 模块的一些参数。例如，忽略 Inport 模块的 **Min**、**Max** 和 **Unit** 参数。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象的对应属性。例如，假设一个模块将**单位**设置为 `ft/s`。当该模块的**数据类型**指定以 `m/s` 为单位的 `ValueType` 对象时，该模块会使用 `m/s` 而不是 `ft/s` 作为单位。

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

#### **以非虚拟总线输出** — 指定总线输出的虚拟性的选项 `off` (默认) | `on`

指定用于加载总线数据的顶层 Inport 模块的输出是虚拟的还是非虚拟的。

- 选择此参数可指定非虚拟总线输出。
- 清除此参数可指定虚拟总线输出。

##### 提示

- 非虚拟总线中的所有信号都必须具有相同的采样时间，即使关联的总线对象为某些元素指定了继承采样时间也是如此。任何可能导致包含不同采样率信号的非虚拟总线的操作都会生成错误。您不能为非虚拟总线加载多速率数据。有关如何将具有不同采样率的信号作为非虚拟总线传递给引用模型的详细信息，请参阅Modify Sample Times for Nonvirtual Buses。

  要为总线加载多速率数据，请清除**以非虚拟总线输出**参数，并将**采样时间**参数设置为继承 (`-1`)。
- 对于模型引用层次结构的顶层模型，代码生成将创建一个 C 结构体来表示非虚拟总线输出。
- 对于引用的模型，选择此选项将在生成的代码中创建一个 C 结构体。否则，代码生成过程将为总线的每个叶元素创建一个参量。

##### 依赖关系

要启用此参数，请进行如下设置：

- 该模块必须位于模型的顶层。
- **数据类型**模块参数必须解析为 `Simulink.Bus` 对象。例如，将**数据类型**设置为 `Simulink.Bus` 对象，或设置为将 `Simulink.Bus` 对象指定为其数据类型的 `Simulink.ValueType` 对象。

##### 编程用法

|  |
| --- |
| **模块参数**：`BusOutputAsStruct` |
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

#### **端口维度(-1 表示继承)** — 端口维度 `-1` (默认) | 整数 | [整数 整数]

指定输出信号的维度。

|  |  |
| --- | --- |
| `-1` | 端口可以为具有任何维度的信号加载数据。端口从连接的信号继承维度。 |
| `N` | 端口可以为大小是 `N` 的向量信号加载数据。 |
| `[R C]` | 端口可以为 `R` 行 `C` 列矩阵信号加载数据。 |

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`PortDimensions` |
| **类型**：字符向量 |
| **值**：`'-1'` | 整数 | [整数 整数] |
| **默认值**：`'-1'` |

#### **可变大小信号** — 允许或不允许可变大小信号的选项 **继承** (默认) | **否** | **是**

指定此端口允许的信号类型。要同时允许可变大小和固定大小的信号，请选择 **inherit**。要仅允许可变大小信号，请选择**是**。要仅允许固定大小的信号，请选择**否**。

当此端口的信号为可变大小的信号时，**端口维度**参数将指定信号的最大维度。

##### 依赖关系

当**数据类型**指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度模式。

##### 编程用法

|  |
| --- |
| **参数**：`VarSizeSig` |
| **类型：**字符向量 |
| **值：**`'Inherit'` | `'No'` | `'Yes'` |
| **默认值：**`'Inherit'` |

#### **信号类型** — 输出信号类型 **自动** (默认) | **实数** | **复**

指定信号输出的复/实性。要继承与其输入相连的信号的复/实性，请选择**自动**。否则，请选择实信号或复信号类型。

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

#### **数据插值** — 对输出数据进行线性插值的选项 `on` (默认) | `off`

从将数据从工作区加载到根级别 Inport 模块中时，指定模块在没有对应数据的时间步处是否对输出值进行线性内插和外插。

要从工作区加载离散数据，请执行以下操作：

1. 将**采样时间**设置为离散速率，例如 `2`。
2. 清除**数据插值**。

有关详细信息，请参阅Control How Models Load Input Data。

软件使用以下内插和外插：

- 对于第一个指定数据点与最后一个指定数据点之间的时间步 - 零阶保持。
- 对于第一个指定数据点之前和最后一个指定数据点之后的时间步 - 接地值。
- 对于第一个指定数据点之前的时间步的大小可变信号 - 如果是单精度或双精度数据类型，则记录 `NaN` 值，如果是其他数据类型，则记录接地值。对于最后一个指定数据点之后的时间步，软件使用接地值。

##### 编程用法

|  |
| --- |
| **模块参数**：`Interpolate` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

#### **事件** — 根据流入端口的数据流触发模型分区的选项 事件触发器对象的元胞数组

*自 R2022b 起*

**事件**参数存储与端口相关联的事件触发器。*事件触发器*根据模型中特定位置的运行时活动创建调度事件，以执行模型中的一个或多个分区。模型的调度指定因响应调度事件而执行的分区以及执行分区时的优先级。要为您的模型配置调度，请使用调度编辑器。

基于速率的模型中的根级输入端口支持三种类型的事件触发器，这些触发器会因响应与数据流入端口相关的*输入事件*创建调度事件。配置输入端口时，您可以为每个输入事件配置一个事件触发器。

| 输入事件 | 输入事件描述 | 事件触发器对象 |
| --- | --- | --- |
| 输入写入 | 在输入端口值每次更新时，都会发生一个*输入写入*事件。 | `simulink.event.InputWrite` |
| 输入写入超时 | 每次当输入端口值未在指定时间内更新时，都会发生一个*输入写入超时*事件。 | `simulink.event.InputWriteTimeout` |
| 输入写入丢失 | 每次当新输入端口值覆盖未处理的数据时，都会发生一次*输入写入丢失*事件。 | `simulink.event.InputWriteLost` |

##### 依赖关系

仅当模块表示基于速率的模型中的根级输入端口时，此参数才可见。

##### 编程用法

|  |
| --- |
| **模块参数**：`EventTriggers` |
| **值：**`1`×`1` 元胞数组 | `2`×`1` 元胞数组 | `3`×`1` 元胞数组 |
| **默认值：**`[]` |

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
| **BalanceDelays** | | **BalanceDelays** 设置 | 描述 | | --- | --- | | **on**（默认值） | 检测 DUT 中其他路径上引入的延迟，并在 Inport 模块路径上插入匹配的延迟。 | | **off** | 在 DUT 子系统的输入端口上禁用延迟平衡，以防止 HDL Coder 插入不必要的匹配延迟。例如，如果 DUT 子系统中的 Inport 模块位于具有稳定输入的路径上，即输入端口的输入信号是来自 DUT 之外的稳定输入信号，则可禁用该模块上的 **BalanceDelays**。 |  **注意**  此属性仅影响 DUT 级别的 Inport 模块。 |
| **BidirectionalPort** | | **BidirectionalPort** 设置 | 描述 | | --- | --- | | **on** | 将端口指定为双向。  需满足以下要求：  - 端口必须位于采用黑盒实现的 Subsystem 模块中。 - 同时，双向端口与对应的顶层 DUT 子系统端口之间不能有逻辑关系。  有关详细信息，请参阅 Specify Bidirectional Ports (HDL Coder)。 | | **off**（默认值） | 不将端口指定为双向。 | |

| 目标设定 | |
| --- | --- |
| **IOInterface** | DUT 端口的目标平台接口类型，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterface` 模块属性被忽略。  要指定有效的 `IOInterface` 设置，请使用 HDL 工作流顾问：  1. 在 HDL 工作流顾问中，在**设置目标** > **设置目标接口**步骤中，请在**目标平台接口表**中的**目标平台接口**列中，使用下拉列表设置目标平台接口类型。 2. 保存模型。  `IOInterface` 值保存为端口的 HDL 模块属性。  例如，要查看 `IOInterface` 值，如果 DUT 端口的完整路径是 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | DUT 端口的目标平台接口端口映射，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceMapping` 模块属性被忽略。  要指定有效的 `IOInterfaceMapping` 设置，请使用 HDL 工作流顾问：  1. 在 HDL 工作流顾问中，在**设置目标** > **设置目标接口**步骤中，请在**目标平台接口表**中的**目标平台接口**列中，使用下拉列表设置目标平台接口类型。 2. 在**位范围 / 地址 / FPGA 引脚**列中，如果要更改默认值，请输入目标平台接口映射。 3. 保存模型。  `IOInterfaceMapping` 值保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceMapping` 值，如果 DUT 端口的完整路径是 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | DUT 端口的目标平台接口端口映射选项，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceOptions` 模块属性被忽略。  要指定有效的 `IOInterfaceOptions` 设置，请使用 HDL 工作流顾问：  1. 在 HDL 工作流顾问的**设置目标** > **设置目标接口**步骤中，在**目标平台接口表**中的**目标平台接口**列中，将输入或输出端口映射到 AXI4 下级接口。 2. 在**接口选项**列中，如果要更改默认初始值，请点击**选项**按钮，并为 **RegisterInitialValue** 输入值。 3. 保存模型。  `IOInterfaceOptions` 值保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceOptions` 值，如果 DUT 端口的完整路径是 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

| 帧到采样的转换 | |
| --- | --- |
| **ConvertToSamples** | | **ConvertToSamples** 设置 | 描述 | | --- | --- | | **on** | 使用帧到采样的转换优化将传入的矩阵输入信号转换为采样。  要使用此属性，请启用模型配置参数**启用帧到采样的转换**。有关详细信息，请参阅Enable frame to sample conversion (HDL Coder)。 | | **off**（默认值） | 不将传入的矩阵输入信号转换为采样。 | |

**`Simulink.ValueType` 对象支持**

此模块支持 `Simulink.ValueType` 对象的生成代码。有关值类型的详细信息，请参阅Specify Common Set of Signal Properties as Value Type。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sources

## Description

Inport blocks link signals from outside a system into the system.

The software assigns Inport block port numbers according to these
rules:

- Inport blocks within a top-level system or subsystem are
  numbered sequentially, starting with 1.
- If you add an Inport block, the label is the next available
  number.
- If you delete an Inport block, other port numbers are
  renumbered to ensure that the Inport blocks are in sequence and
  that no numbers are omitted.
- If you copy an Inport block into a system, its port number is
  not renumbered unless its current number conflicts with an input port already in
  the system. If the port number for the copied Inport block is not
  in sequence, renumber the block. Otherwise, you get an error message when you
  simulate the model or update the block diagram.

### Inport Blocks in Top-Level Systems

You can use an Inport block in a top-level system to:

- Supply external inputs from a workspace using the **Input** parameter. If
  you do not provide external input data, the output from the
  Inport block is the ground value. For more information,
  see Load Data to Root-Level Input Ports.

  - To load data for several signals using root-level input ports,
    consider using the Root Inport Mapper tool. See Map Data Using Root Inport Mapper Tool.
  - Use the `createInputDataset` function to create a
    `Simulink.SimulationData.Dataset` object that
    contains an element for each root-level Inport
    block in the model you specify.
- Provide a means for perturbation of the model by the
  `linmod` and `trim` analysis
  functions. For more information, see Linearizing Models.

### Inport Blocks in Subsystems

Inport blocks in a subsystem represent inputs to the subsystem. A signal
arriving at an input port on a Subsystem block flows out of the
associated Inport block in that subsystem. The Inport
block associated with an input port on a Subsystem block is the block
whose **Port number** parameter matches the relative position of
the input port on the Subsystem block. For example, the
Inport block whose **Port number** parameter is
`1` gets its signal from the block connected to the topmost
port on the Subsystem block.

If you renumber the **Port number** of an Inport block, the
block becomes connected to a different input port. The block continues to receive
its signal from the same block outside the subsystem.

Inport blocks inside a subsystem support signal label propagation, but
root-level Inport blocks do not. For more information, see Signal Label Propagation.

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

The In Bus Element block is of block type Inport and the
Out Bus Element block is of block type
Outport.

### Create Duplicate Inport Blocks

You can create any number of duplicates of an Inport block. The duplicates
are graphical representations of the original intended to simplify block diagrams by
eliminating unnecessary lines. The duplicate has the same port number, properties,
and output as the original.

To create a duplicate of an Inport block:

1. In the block diagram, select the unconnected
   Inport block that you want to duplicate.
2. Press and hold the **Ctrl** key and drag
   the block.
3. Release the pointer, and then select
   **Duplicate** from the context menu.

You can select an Inport block that has duplicates to highlight the
duplicate blocks. To show a related block in an open diagram or new tab, pause your
cursor on the ellipsis that appears after selection. Then, select **Related
Blocks**
 from the action menu. When multiple blocks
correspond to the selected block, a list of related blocks opens. You can filter the
list of related blocks by entering a search term in the text box. After you select a
related block from the list, window focus goes to the open diagram or new tab that
shows the related block.

### Connect Buses to Root-Level Inport Blocks

If you want a root-level Inport block of a model to produce a bus, set the
**Data type** parameter to the name of a bus object that
defines the bus that the Inport block produces. For more information,
see Specify Bus Properties with Bus Objects.

## Ports

### Output

### **Port\_1** — Input signal scalar | vector

Input signal that flows into the system through the input port.

You can use an Inport block in a subsystem to supply fixed-point data in
a structure or in any other format.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

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

### **Icon display** — Icon display `Port number` (default) | `Signal name` | `Port number and signal name`

Specify the information displayed on the block icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **Default:** `'Port number'` |

### **Latch input by delaying outside signal** — Option to latch signal by delay `off` (default) | `on`

Select to specify that the block output is the value of the input
signal at the previous time step.

Selecting this option enables the software to resolve data
dependencies among triggered subsystems that are part of a loop.

The Inport block indicates that this option is selected
by displaying `<Lo>`.

#### Dependencies

This parameter is enabled only when the block represents an input
port in a triggered subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LatchByDelayingOutsideSignal` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Latch input for feedback signals of function-call subsystem outputs** — Latch signal from changing `off` (default) | `on`

Select to specify that the block latches the input value and prevents
it from changing during the execution of the function-call subsystem.
For a single function call that is branched to invoke multiple
function-call subsystems, this option breaks a loop formed when a signal
feeds back from one function-call subsystem into another. Selecting this
option prevents any change to the values of a feedback signal from a
function-call subsystem that is invoked during the execution of the
subsystem that contains this block.

The Inport block indicates that this option is selected
by displaying `<Li>`.

#### Dependencies

This option is enabled only when the block represents an input
port in a function-call subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LatchInputForFeedbackSignals` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Connect Inputs** — Option to open Root Inport Mapper tool button

To import, visualize, and map signal and bus data to root-level
Inport blocks, click this button. The Root Inport
Mapper tool opens.

#### Dependencies

This button appears only when the block is at the root level for
the model.

### Signal Attributes

### **Output function call** — Option to produce function-call event `off` (default) | `on`

Specify that the input signal produces a function-call event signal.

Select this option if a current model must accept a function-call event signal
when referenced in the top model.

#### Dependencies

- To enable this option, the block must be in an asynchronous function
  call.
- The software ignores the value of this parameter when **Data
  type** specifies a `Simulink.ValueType`
  object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputFunctionCall` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

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
inherited, specified directly, or expressed as a data type object, such
as `Simulink.NumericType`.

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
- Custom data type — Use a MATLAB® expression that specifies the type. For
  example, you can specify a `Simulink.NumericType` object whose
  `DataTypeMode` property is set to a
  value other than `'Fixed-point: unspecified
  scaling'`.

When you specify a `Simulink.ValueType` or
`Simulink.Bus` object as the data type, some parameters of the
Inport block are ignored. For example, the **Min**,
**Max**, and **Unit** parameters of the
Inport block are ignored. The software uses the corresponding properties of
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

### **Output as nonvirtual bus** — Option to specify virtuality of bus output `off` (default) | `on`

Specify whether the output for a top-level Inport block used to
load bus data is virtual or nonvirtual.

- Select this parameter to specify a nonvirtual bus output.
- Clear this parameter to specify a virtual bus output.

#### Tips

- All signals in a nonvirtual bus must have the same sample time, even if the
  associated bus object specifies inherited sample time for some elements. Any
  operation that would result in a nonvirtual bus containing signals with
  different sample rates generates an error. You cannot load multirate data for a
  nonvirtual bus. See Modify Sample Times for Nonvirtual Buses for details on how to pass signals with
  different sample rates into a referenced model as a nonvirtual bus.

  To load multirate data for a bus, clear the **Output as nonvirtual
  bus** parameter, and set the **Sample time**
  parameter to inherited (`-1`).
- For the top model in a model reference hierarchy, code generation creates a
  C structure to represent the nonvirtual bus output.
- For referenced models, select this option to create a C structure in
  generated code. Otherwise, code generation creates an argument for each leaf
  element of the bus.

#### Dependencies

To enable this parameter:

- The block must be at the top level of a model.
- The **Data type** block parameter must resolve to a
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

### **Port dimensions (-1 for inherited)** — Port dimensions `-1` (default) | integer | [integer integer]

Specify the dimensions of the output signal.

|  |  |
| --- | --- |
| `-1` | The port can load data for a signal with any dimensions. The port inherits dimensions from the connected signal. |
| `N` | The port can load data for a signal that is a vector of size `N`. |
| `[R C]` | The port can load data for a matrix signal having `R` rows and `C` columns. |

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
| **Values**: `'-1'` | integer | [integer integer] |
| **Default**: `'-1'` |

### **Variable-size signal** — Option to allow or disallow variable-size signals `Inherit` (default) | `No` | `Yes`

Specify the type of signals allowed for this port. To allow variable-size and
fixed-size signals, select `Inherit`. To allow only
variable-size signals, select `Yes`. To allow only fixed-size
signals, select `No`.

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
| **Parameter:** `VarSizeSig` |
| **Type:** character vector |
| **Value:** `'Inherit'` | `'No'` | `'Yes'` |
| **Default:** `'Inherit'` |

### **Signal type** — Output signal type `auto` (default) | `real` | `complex`

Specify the complexity of the signal output. To inherit the complexity from the
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

### **Interpolate data** — Option to linearly interpolate output data `on` (default) | `off`

When loading data from the workspace into a root-level Inport block,
specify whether the block linearly interpolates and extrapolates output
values at time steps for which no corresponding data exists.

To load discrete data from the workspace:

1. Set the **Sample time** to a discrete
   rate, such as `2`.
2. Clear **Interpolate data**.

For more information, see Control How Models Load Input Data.

The software uses the following interpolation and
extrapolation:

- For time steps between the first specified data point and the
  last specified data point — zero-order hold.
- For time steps before the first specified data point and after
  the last specified data point — ground value.
- For variable-size signals for time steps before the first
  specified data point — a `NaN` value is
  logged for single or double data types and ground for other data
  types. For time steps after the last specified data point, the
  software uses ground values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Interpolate` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Events** — Option to trigger model partition based on flow of data into port cell array of event trigger objects

*Since R2022b*

The **Events** parameter stores the event triggers
associated with the port. *Event triggers* create
schedule events to execute one or more partitions in the model based on
the runtime activity at a particular location in the model. The schedule
for the model specifies the partitions that execute in response to the
schedule event, as well as the priority of execution. To configure the
schedule for your model, use the Schedule Editor.

Root-level input ports in rate-based models support three types of
event triggers that create schedule events in response to
*input events* that relate to the flow of data
into the port. You can configure an input port with one event trigger
for each input event.

| Input Event | Input Event Description | Event Trigger Object |
| --- | --- | --- |
| Input write | An *input write* event occurs each time the input port value updates. | `simulink.event.InputWrite` |
| Input write timeout | An *input write timeout* event occurs each time the input port value does not update within a specified amount of time. | `simulink.event.InputWriteTimeout` |
| Input write lost | An *input write lost* event occurs each time a new input port value overwrites unprocessed data. | `simulink.event.InputWriteLost` |

#### Dependencies

This parameter is visible only when the block represents a
root-level input port in a rate-based model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EventTriggers` |
| **Values:** `1`-by-`1` cell array | `2`-by-`1` cell array | `3`-by-`1` cell array |
| **Default:** `[]` |

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
| **BalanceDelays** | | **BalanceDelays** Setting | Description | | --- | --- | | `on` (default) | Detects introduction of delays on other paths in the DUT and inserts matching delays on the Inport block path. | | `off` | Disable delay balancing on input ports in your DUT subsystem to prevent HDL Coder from inserting matching delays when they are unnecessary. For example, disable **BalanceDelays** on an Inport block in your DUT subsystem if it is on a path with a stable input, meaning the input signal to the input port is a stable input signal outside of the DUT. |  **Note**  This property affects only DUT-level Inport blocks. |
| **BidirectionalPort** | | **BidirectionalPort** Setting | Description | | --- | --- | | `on` | Specify the port as bidirectional.  The following requirements apply:  - The port must be in a Subsystem block   with black box implementation. - There must also be no   logic between the bidirectional port and the corresponding top-level   DUT subsystem port.  For more information, see Specify Bidirectional Ports (HDL Coder). | | `off` (default) | Do not specify the port as bidirectional. | |

| Target Specification | |
| --- | --- |
| **IOInterface** | Target platform interface type for DUT ports, specified as a character vector. The `IOInterface` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterface` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, in the **Set Target** > **Set Target Interface** step, in the **Target platform interface table**,    in the **Target Platform Interfaces** column, use    the drop-down list to set the target platform interface type. 2. Save the model.  The `IOInterface` value is saved as an HDL    block property of the port.  For example, to view the `IOInterface` value,    if the full path to your DUT port is `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | Target platform interface port mapping for DUT ports, specified as a character vector. The `IOInterfaceMapping` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterfaceMapping` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, in the **Set Target** > **Set Target Interface** step, in the **Target platform interface table**,    in the **Target Platform Interfaces** column, use    the drop-down list to set the target platform interface type. 2. In the **Bit Range / Address / FPGA Pin** column,    if you want to change the default value, enter a target platform interface    mapping. 3. Save the model.  The `IOInterfaceMapping` value is saved as    an HDL block property of the port.  For example, to view the `IOInterfaceMapping` value,    if the full path to your DUT port is `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | Target platform interface port mapping options for DUT ports, specified as a character vector. The `IOInterfaceOptions` block property is ignored for Inport and Outport blocks that are not DUT ports.  To specify valid `IOInterfaceOptions` settings, use the HDL Workflow Advisor:  1. In the HDL Workflow Advisor, on the **Set Target** > **Set Target Interface** step, in the **Target    platform interface table**, in the    **Target Platform Interfaces**    column, map the input or output ports to an AXI4    subordinate interface. 2. In the **Interface    Options** column, if you want to change    the default initial value, click the    **Options** button and enter a    value for    **RegisterInitialValue**. 3. Save the model.  The `IOInterfaceOptions`    value is saved as an HDL block property of the    port.  For example, to view the    `IOInterfaceOptions` value, if    the full path to your DUT port is    `hdlcoder_led_blinking/led_counter/LED`,    enter:  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

| Frame to Sample Conversion | |
| --- | --- |
| **ConvertToSamples** | | **ConvertToSamples** Setting | Description | | --- | --- | | `on` | Convert the incoming matrix input signal to samples by using the frame to sample conversion optimization.  To use this property, enable the model configuration parameter **Enable frame to sample conversion**. For more information, see Enable frame to sample conversion (HDL Coder). | | `off` (default) | Do not convert the incoming matrix input signal to samples. | |

**`Simulink.ValueType` Object Support**

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
