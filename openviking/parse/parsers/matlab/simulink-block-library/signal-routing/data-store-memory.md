---
type: simulink-block
title: 'Data Store Memory'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'datastorememory'
---

# Data Store Memory

Define data store

## 中文

定义数据存储

### 所属库

Simulink / Signal Routing

### 描述

Data Store Memory 模块定义并初始化一个命名的共享数据存储，即一个内存区域，供指定相同数据存储名称的 Data Store Read 和 Data Store Write 模块使用。

定义数据存储的 Data Store Memory 模块的位置确定了哪些 Data Store Read 和 Data Store Write 模块可以访问该数据存储：

- 如果 Data Store Memory 模块在*顶层系统*中，则模型中任意位置的 Data Store Read 和 Data Store Write 模块都可以访问该数据存储。
- 如果 Data Store Memory 模块在*子系统*中，则位于同一子系统或模型层次结构中该子系统下面的任何子系统中的 Data Store Read 和 Data Store Write 模块都可以访问该数据存储。
- 在引用模型中定义的 Data Store Read  或 Data Store Write 模块可以访问存储在模型层次结构中更高级别的数据。

要允许 Data Store Read  或 Data Store Write 模块从引用模型内部访问存储在模型层次结构中更高级别上的数据，请执行以下操作：

- 在引用模型中放置 Data Store Memory 模块。
- 在 Data Store Memory 模块对话框中，选择**数据存储引用**。

不要在 For Each 子系统中包含 Data Store Memory 模块。

要从数据存储获取正确的结果，必须确保数据存储按照预期的顺序进行读取和写入。有关详细信息，请参阅：

- 对数据存储访问进行排序
- 数据存储诊断
- Log Data Stores

您可以使用 Data Store Memory 模块结合 `Simulink.Signal` 对象来定义数据存储，也可以不使用前者而只使用后者来定义数据存储。在*基础*工作区中定义的具有一个信号对象的数据存储是一个*全局*数据存储。每个模型都可以访问全局数据存储，包括所有引用的模型。有关详细信息，请参阅数据存储。

您可以选择 Data Store Read、Data Store Write 或 Data Store Memory 模块来突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择**相关模块** Related Blocks button。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

#### 字符串支持

仅当 Data Store Memory 模块配置为**初始值**参数采用默认值 (`0`) 时，该模块才接受和输出字符串数据类型。

### 参数

#### 常设

#### **数据存储名称** — 数据存储的名称 `A` (默认) | 字符向量 | 字符串

使用此模块指定您正在定义的数据存储的名称。具有相同名称的 Data Store Read 和 Data Store Write 模块可以读取和写入由此模块初始化的数据存储。此名称可以代表一个 Data Store Memory 模块或者一个定义为数据存储的信号对象。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataStoreName` |
| **类型**：字符向量 |
| **值**：`'A' | ...` |
| **默认值**：`'A'` |

#### **全部重命名** — 用于在整个模型中重命名数据存储的选项 按钮

重命名 Data Store Read 和 Data Store Write 模块使用的位于模型中任意位置的此数据存储。

##### 限制

在下列情况下，不能使用**全部重命名**来重命名数据存储：

- 在工作区中使用 `Simulink.Signal` 对象来管理为数据存储生成的代码
- 使用 `Simulink.Signal` 对象而不是 Data Store Memory 模块来定义数据存储

在这些情况下，您必须从模型资源管理器中重命名相应的 `Simulink.Signal` 对象。有关示例，请参阅重命名信号对象定义的数据存储。

#### **数据存储引用** — 访问在更高层级的模型中定义的内存 `off` (默认) | `on`

当您需要 Simulink® 的子集访问在模型层次结构中的更高级别定义的 Data Store Memory 模块的元素时，请选择此选项。这些模块包括 Data Store Read 模块、Data Store Write 模块、S-Function 模块、MATLAB Function 模块、MATLAB System 模块和 Chart (Stateflow) 模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataStoreReference` |
| **类型**：`character vector` |
| **值**：`'off'|'on'` |
| **默认值**：`'off'` |

##### 限制

当您选择**数据存储引用**参数时，以下信号属性不受支持：**数据类型**为**继承**、**维度**为 `-1`、**信号类型**为**自动**。您必须显式选择这些属性。

#### **对应的 Data Store Read/Write 模块** — 所连接的 Data Store Read/Write 模块的路径 模块路径

列出与当前模块具有相同数据存储名称且在当前系统中或者在模型层次结构中位于当前系统下面的任何子系统中的所有 Data Store Read 和 Data Store Write 模块。点击某模块路径将在模型中显示并突出显示该模块。

#### 信号属性

#### **初始值** — 数据存储的初始值 `0` (默认) | 标量 | 向量 | 矩阵 | N 维数组

指定数据存储的一个或多个初始值。**最小值**参数指定此参数的最小值，**最大值**参数指定最大值。

如果指定非标量值，并将**维度**设置为 `-1`（默认值），数据存储的维度将与数组的维度相同。您（通过使用 Data Store Write 模块）写入数据存储的数据必须具有这些维度。

如果将**维度**参数设置为 `-1` 以外的值，初始值维度必须与您指定的维度相匹配，除非初始值是标量或 MATLAB® 结构体。如果指定标量，则数据存储的每个元素都使用该标量作为初始值。使用这种方法可将同一初始值（您指定的标量）应用到每个元素，而无需手动将初始值的维度与数据存储的维度进行匹配。

要使用此模块初始化非虚拟总线信号，请将初始值指定为 MATLAB 结构体，并将模型配置参数Underspecified initialization detection设置为`简化`。有关使用结构体初始化非虚拟总线信号的详细信息，请参阅Specify Initial Conditions for Bus Elements。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialValue` |
| **类型**：字符向量 |
| **值**：标量 | 向量 | 矩阵 | N 维数组 |
| **默认值**：`'0'` |

#### **最小** — 范围检查的最小输出值 `[]` (默认) | 标量

指定模块应输出的最小值。默认值为 `[]`（未指定）。此数字必须为有限双精度实数标量值。

**注意**

如果您指定总线对象作为此模块的数据类型，请不要为模块上的总线数据设置最小值。Simulink 会忽略此设置。但请为指定作为数据类型的总线对象的总线元素设置最小值。有关总线元素的“最小值”属性的信息，请参阅 `Simulink.BusElement`。

Simulink 使用最小值执行下列操作：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

#### **最大** — 范围检查的最大输出值 `[]` (默认) | 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。此数字必须为有限双精度实数标量值。

**注意**

如果您指定总线对象作为此模块的数据类型，请不要为模块的总线数据设置最大值。Simulink 会忽略此设置。但请为指定作为数据类型的总线对象的总线元素设置最大值。有关总线元素的“最大值”属性的信息，请参阅 `Simulink.BusElement`。

Simulink 使用最大值执行下列操作：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

#### **数据类型** — 输出数据类型 **Inherit: auto** (默认) | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **字符串** | **Enum: <class name>** | **Simulink.ImageType(480,640,3)**

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则（例如，**Inherit: auto）**。
- 内置数据类型的名称（例如，`single`）。
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象。
- 计算结果为数据类型的表达式（例如，`fixdt(1,16,0)`）。不要在表达式中将总线对象指定为数据类型，请使用 `Bus: <object name>` 指定总线数据类型。
- 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数，并指定描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式，分别表示图像的行、列和通道。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Simulink.ImageType(480,640,3)'` |
| **默认值：**`'Inherit: auto'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **维度(-1 表示从初始值推断)** — 数据存储的维度 `-1` (默认) | 标量 | 向量 | 矩阵

数据存储的维度。为默认值 `-1` 时，您可以使用**初始值**参数来设置数据存储的维度。但是，在这种情况下，不能将标量扩展用于初始值。您必须通过使用具有所需维度的数组来指定初始值。

如果使用除 `-1` 以外的值，则指定的维度必须与**初始值**参数的维度相同，除非将初始值指定为标量（用于标量扩展）或 MATLAB 结构体。如果数据存储表示总线数组，并且初始值使用 MATLAB 结构体，则可以指定维度以使用此结构体初始化总线数组。

##### 编程用法

|  |
| --- |
| **模块参数**：`Dimensions` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'-1'` |

#### **将向量参数解释为一维向量** — 用于将向量解释为一维的选项 `on` (默认) | `off`

指定数据存储将向量初始值解释为一维。

默认情况下，MATLAB 将向量数据表示为具有两个维度的矩阵。例如，MATLAB 将向量 `[1 2 3]` 表示为一个 1×3 矩阵。

当选择此参数时，数据存储仅使用一维而不是二维来表示向量数据。例如，如果指定初始值 `[1 2 3]`，数据存储将存储包含三个元素的一维向量。

有关详细信息，请参阅 确定源模块的输出维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

#### **信号类型** — 数据存储值的复/实性 **自动** (默认) | **实数** | **复**

指定数据存储内的值的数值类型（实数或复数）。

##### 编程用法

|  |
| --- |
| **模块参数**：`SignalType` |
| **类型：**字符向量 |
| **值：**`'auto' | 'real' | 'complex'` |
| **默认值：**`'auto'` |

#### **跨模型实例共享** — 用于允许 Model 模块从同一个数据存储中读取数据的选项 `off` (默认) | `on`

在单一模型引用层次结构中，当使用多个 Model 模块来引用包含 Data Store Memory 模块的模型时，默认情况下，引用模型的每个实例（每个 Model 模块）都针对数据存储的一个单独副本进行读写。当您选择**跨模型实例共享**而不是与单独副本进行交互时，所有实例都针对同一数据存储进行读写。

将模型配置参数**代码接口打包**设置为**可重用函数**以从模型生成可重入代码 (Simulink Coder™) 时，选择了**跨模型实例共享**的数据存储在代码中将作为生成的入口函数可以直接访问的全局符号出现。例如，全局符号可以是一个全局变量，也可以是全局结构体变量中的一个字段。因此，您的代码对入口函数的每个调用（模型的每个实例）都会共享数据。

有关示例，请参阅在可重用算法的多个实例之间共享数据。有关详细信息，请参阅在引用模型实例之间共享数据。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShareAcrossModelInstances` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **数据存储名称必须解析为 Simulink 信号对象** — 用于将数据存储名称解析为 Simulink 信号对象的选项 `off` (默认) | `on`

指定 Simulink 软件在编译模型时需在模型和基础工作区中搜索具有相同名称的 `Simulink.Signal` 对象，如符号解析中所述。如果 Simulink 找不到此类对象，将停止编译并显示错误。否则，Simulink 会将该信号对象的属性与 Data Store Memory 模块的对应属性进行比较。如果模块与对象的属性不一致，Simulink 将中断模型编译并显示错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### 诊断

#### **检测写前读** — 模型在当前时间步中写入之前尝试读取数据时的操作 **警告** (默认) | **无** | **错误**

选择当模型试图从在当前时间步中未曾写入数据的数据存储中读取数据时要执行的诊断操作。另请参阅**模型配置参数** > **诊断** > **数据有效性** 窗格的 **Data Store Memory 模块**部分中的 Detect read before write 诊断。

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`ReadBeforeWriteMsg` |
| **类型：**字符向量 |
| **值：**`'none' | 'warning' | 'error'` |
| **默认值：**`'warning'` |

#### **检测读后写** — 模块在同一时间步中读取数据后尝试写入时的操作 **警告** (默认) | **无** | **错误**

选择当模型试图向曾在当前时间步中读取过数据的数据存储中写入数据时要执行的诊断操作。另请参阅**模型配置参数** > **诊断** > **数据有效性** 窗格的 **Data Store Memory 模块**部分中的 Detect write after read 诊断。

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`WriteAfterReadMsg` |
| **类型：**字符向量 |
| **值：**`'none' | 'warning' | 'error'` |
| **默认值：**`'warning'` |

#### **检测写后写** — 模型在同一时间步中写入两次时的操作 **警告** (默认) | **无** | **错误**

选择当模型试图在当前时间步中连续两次向数据存储中写入数据时要执行的诊断操作。另请参阅**模型配置参数** > **诊断** > **数据有效性** 窗格的 **Data Store Memory 模块**部分中的 Detect write after write 诊断。

- **无** - 不产生任何响应。
- **警告** - 显示警告并继续进行仿真。
- **错误** - 终止仿真并显示错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`WriteAfterWriteMsg` |
| **类型：**字符向量 |
| **值：**`'none' | 'warning' | 'error'` |
| **默认值：**`'warning'` |

#### 记录

#### **记录数据存储数据** — 用于记录数据存储数据的选项 `off` (默认) | `on`

选择此选项可在仿真过程中将此信号的值保存到 MATLAB 工作区。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataLogging` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **记录名称** — 与记录的信号数据相关联的名称 **使用数据存储名称** (默认) | **自定义**

使用这一对控件（包括一个列表框和一个编辑字段）指定与记录的信号数据相关联的名称。

默认情况下，Simulink 使用信号名称作为其记录名称。要指定自定义记录名称，请从列表框中选择**自定义**，然后在旁边的编辑字段中输入自定义名称。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataLoggingNameMode` |
| **类型：**字符向量 |
| **值：**`'SignalName'` | `'Custom'` |
| **默认值：**`'SignalName'` |

如果将 `DataLoggingNameMode` 设置为 `'Custom'`，则必须使用 `DataLoggingName` 参数指定与记录信号数据相关联的名称。

|  |
| --- |
| **模块参数：**`DataLoggingName` |
| **类型：**字符向量 |
| **值：**字符向量 |
| **默认值：**`''` |

#### **将数据点限制为最后** — 用于丢弃除最后 *N* 个数据点外的所有数据点的选项 `5000` | 非零整数

放弃除最后 `N` 个数据点之外的所有数据点，其中 `N` 是您在旁边的编辑字段中输入的数字。有关详细信息，请参阅Log Data Stores。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataLoggingLimitDataPoints` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

|  |
| --- |
| **模块参数**：`DataLoggingMaxPoints` |
| **类型：**字符向量 |
| **值：**非零整数 |
| **默认值：**`'5000'` |

#### **抽取** — 用于每隔 *N* 个数据点记录一次的选项 `2` (默认) | 整数

每 `N` 个数据点记录一次，其中 `N` 是您在相邻的编辑字段中输入的数字。例如，假设您的模型使用步长为 `0.1` 秒的定步长求解器。如果您选中此选项并接受默认抽取值 (`2`)，软件将在 `0.0`、`0.2`、`0.4` 秒等时间记录此信号的数据点。有关详细信息，请参阅Log Data Stores。

##### 编程用法

|  |
| --- |
| **模块参数**：`DataLoggingDecimateData` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

|  |
| --- |
| **模块参数**：`DataLoggingDecimation` |
| **类型：**字符向量 |
| **值：**非零整数 |
| **默认值：**`'2'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

要为使用 Data Store Memory 模块的模型生成 PLC 代码，请首先在基础工作区中定义 `Simulink.Signal`。然后在模块参数的**信号属性**选项卡中，将数据存储名称设置为解析为 `Simulink.Signal` 对象的名称。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024b: 在加速和快速加速模式仿真中记录数据存储

您可以在加速和快速加速模式仿真以及普通模式仿真中记录 Data Store Memory 模块变量。

#### R2023b: 访问在模型层次结构中较高级别定义的 Data Store Memory 模块元素

从 R2023b 开始，Data Store Read 模块、Data Store Write 模块、S-Function 模块、MATLAB Function 模块、MATLAB System 模块和 Chart 模块可以访问在模型层次结构中较高级别定义的 Data Store Memory 模块中的数据存储。

## Libraries

Simulink / Signal Routing

## Description

The Data Store Memory block defines and initializes a named shared data
store, which is a memory region usable by Data Store Read and Data
Store Write blocks that specify the same data store name.

The location of the Data Store Memory block that defines a data store
determines which Data Store Read and Data Store Write
blocks can access the data store:

- If the Data Store Memory block is in the *top-level
  system*, Data Store Read and Data Store
  Write blocks anywhere in the model can access the data store.
- If the Data Store Memory block is in a
  *subsystem*, Data Store Read and
  Data Store Write blocks in the same subsystem or in any
  subsystem below it in the model hierarchy can access the data store.
- A Data Store Read  or Data Store Write block
  defined inside a referenced model can access the data stored at a higher level
  in the model hierarchy.

To allow a Data Store Read  or Data Store Write block to
access the data stored at a higher level in the model hierarchy from inside a referenced model:

- Place a Data Store Memory block inside the referenced model.
- In the Data Store Memory block dialog box, select
  **Data store reference**.

Do not include a Data Store Memory block in a For Each
subsystem.

Obtaining correct results from data stores requires ensuring that data store reads and
writes occur in the expected order. For details, see:

- Order Data Store Access
- Data Store Diagnostics
- Log Data Stores

You can use `Simulink.Signal` objects in addition
to, or instead of, Data Store Memory blocks to define data stores. A data
store defined in the *base* workspace with a signal object is a
*global* data store. Global data stores are accessible to every
model, including all referenced models. See Data Stores for more
information.

You can select a Data Store Read, Data Store Write, or
Data Store Memory block to highlight blocks related to it. To show a
related block in an open diagram or new tab, pause on the ellipsis that appears after
selection. Then, select **Related Blocks**
Related Blocks button from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

### String Support

The Data Store Memory block can accept and output string data type only
if the block is configured for the default value of the **Initial
value** parameter (`0`).

## Parameters

### Main

### **Data store name** — Name for data store `A` (default) | character vector | string

Specify a name for the data store you are defining with this block.
Data Store Read and Data Store Write
blocks with the same name can read from, and write to, the data store
initialized by this block. The name can represent a Data Store
Memory block or a signal object defined to be a data
store.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreName` |
| **Type**: character vector |
| **Values**: `'A' | ...` |
| **Default**: `'A'` |

### **Rename All** — Option to rename data store throughout model button

Rename this data store everywhere the Data Store Read
and Data Store Write blocks use it in a model.

#### Limitations

You cannot use **Rename All** to rename a data
store if you:

- Use a `Simulink.Signal` object in a
  workspace to control the code generated for the data
  store
- Use a `Simulink.Signal` object instead
  of a Data Store Memory block to define
  the data store

You must instead rename the corresponding
`Simulink.Signal` object from Model Explorer. For
an example, see Rename Data Store Defined by Signal Object.

### **Data store reference** — To access the memory defined in higher-level model `off` (default) | `on`

Select this option when you need a subset of Simulink® to access the elements of a Data Store
Memory block defined at a higher level in the model
hierarchy. These blocks include the Data Store Read
block, Data Store Write block, S-Function block, MATLAB Function block,
MATLAB System block, and
Chart (Stateflow) block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreReference` |
| **Type**: `character vector` |
| **Values**: `'off'|'on'` |
| **Default**: `'off'` |

#### Limitations

When you select the **Data store reference**
parameter, these signal attributes are not supported:
`Inherit`  for **Data
type**, `-1` for
**Dimensions** and
`auto` for **Signal
type**.You must select these attributes
explicitly.

### **Corresponding Data Store Read/Write blocks** — Path to connected Data Store Read/Write blocks block path

List all the Data Store Read and Data Store
Write blocks that have the same data store name as the
current block, and that are in the current system or in any subsystem
below it in the model hierarchy. Clicking a block path displays and
highlights that block in your model.

### Signal Attributes

### **Initial value** — Initial value of data store `0` (default) | scalar | vector | matrix | N-D array

Specify the initial value or values of the data store. The
**Minimum** parameter specifies the minimum value
for this parameter, and the **Maximum** parameter
specifies the maximum value.

If you specify a nonscalar value and set
**Dimensions** to `-1` (the
default), the data store has the same dimensions as the array. Data that
you write to the data store (by using Data Store Write
blocks) must have these dimensions.

If you set the **Dimensions** parameter to a value
other than `-1`, the initial value dimensions must
match the dimensions that you specify, unless the initial value is a
scalar or a MATLAB® structure. If you specify a scalar, each element of the
data store uses the scalar as the initial value. Use this technique to
apply the same initial value (the scalar that you specify) to each
element without manually matching the dimensions of the initial value
with the dimensions of the data store.

To use this block to initialize a nonvirtual bus signal, specify the
initial value as a MATLAB structure and set the model configuration parameter Underspecified initialization detection to `Simplified`. For more information about
initializing nonvirtual bus signals using structures, see Specify Initial Conditions for Bus Elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialValue` |
| **Type**: character vector |
| **Values**: scalar | vector | matrix | N-D array |
| **Default**: `'0'` |

### **Minimum** — Minimum output value for range checking `[]` (default) | scalar

Specify the minimum value that the block should output. The default
value is `[]` (unspecified). This number must be a
finite real double scalar value.

**Note**

If you specify a bus object as the data type for this block, do
not set the minimum value for bus data on the block. Simulink
ignores this setting. Instead, set the minimum values for bus
elements of the bus object specified as the data type. For
information on the Minimum property of a bus element, see `Simulink.BusElement`.

Simulink uses the minimum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes such as SIL or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[ ]'` |

### **Maximum** — Maximum output value for range checking `[]` (default) | scalar

Specify the maximum value that the block should output. The default
value is `[]` (unspecified). This number must be a
finite real double scalar value.

**Note**

If you specify a bus object as the data type for this block, do
not set the maximum value for bus data on the block. Simulink
ignores this setting. Instead, set the maximum values for bus
elements of the bus object specified as the data type. For
information on the Maximum property of a bus element, see `Simulink.BusElement`.

Simulink uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes such as SIL or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'[ ]'` |

### **Data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Enum: <class name>` | `Simulink.ImageType(480,640,3)`

Specify the output data type. You can set it to:

- A rule that inherits a data type (for example,
  `Inherit: auto`).
- The name of a built-in data type (for example,
  `single`).
- The name of a data type object (for example, a
  `Simulink.NumericType` object).
- An expression that evaluates to a data type (for example,
  `fixdt(1,16,0)`). Do not specify a bus
  object as the data type in an expression; use `Bus:
  <object name>` to specify a bus data
  type.
- If you have Computer Vision Toolbox™, use the constructor for the `Simulink.ImageType` (Computer Vision Toolbox) object and specify the
  properties to describe the image. By default, the data type uses
  the `Simulink.ImageType(480,640,3)` expression
  that represents the rows, columns, and channels of the image
  respectively.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Simulink.ImageType(480,640,3)'` |
| **Default:** `'Inherit: auto'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Dimensions (-1 to infer from Initial value)** — Dimensions of data store `-1` (default) | scalar | vector | matrix

Dimensions of the data store. The default value,
`-1`, enables you to set the dimensions of the data
store by using the **Initial value** parameter.
However, in this case, you cannot use scalar expansion with the initial
value. You must specify the initial value by using an array that has the
dimensions that you want.

If you use a value other than `-1`, specify the same
dimensions as the dimensions of the **Initial value**
parameter, unless you specify the initial value as a scalar (for scalar
expansion) or a MATLAB structure. If the data store represents an array of buses,
and if you use a MATLAB structure for the initial value, you can specify
dimensions to initialize the array of buses with this structure.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Dimensions` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'-1'` |

### **Interpret vector parameters as 1-D** — Option to interpret vectors as 1-D `on` (default) | `off`

Specify that the data store interpret vector initial values as
one-dimensional.

By default, MATLAB represents vector data as matrices, which have two
dimensions. For example, MATLAB represents the vector `[1 2 3]` as a
1-by-3 matrix.

When you select this parameter, the data store represents vector data
by using only one dimension instead of two. For example, if you specify
an initial value of `[1 2 3]`, the data store stores a
one-dimensional vector with three elements.

For more information, see Determine the Output Dimensions of Source Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VectorParams1D` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'on'` |

### **Signal type** — Complexity of data store values `auto` (default) | `real` | `complex`

Specify the numeric type, real or complex, of the values in the data
store.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalType` |
| **Type:** character vector |
| **Values:** `'auto' | 'real' | 'complex'` |
| **Default:** `'auto'` |

### **Share across model instances** — Option to allow Model blocks to read from the same data store `off` (default) | `on`

In a single model reference hierarchy, when you use multiple
Model blocks to refer to a model that contains a
Data Store Memory block, by default, each instance of
the referenced model (each Model block) reads from and
writes to a separate copy of the data store. When you select
**Share across model instances**, instead of
interacting with a separate copy, all of the instances read from and
write to the same data store.

When you set the model configuration parameter **Code
interface packaging** to `Reusable
function` to generate reentrant code from a model
(Simulink
Coder™), a data store with **Share across model
instances** selected appears in the code as a global symbol
that the generated entry-point functions access directly. For example, a
global symbol is a global variable or a field of a global structure
variable. Therefore, each call that your code makes to the entry-point
functions (each instance of the model) shares the data.

For an example, see Share Data Among Multiple Instances of a Reusable Algorithm. For
more information, see Share Data Among Referenced Model Instances.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShareAcrossModelInstances` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Data store name must resolve to Simulink signal object** — Option to resolve data store name to Simulink signal object `off` (default) | `on`

Specify that Simulink software, when compiling the model, searches the model and
base workspace for a `Simulink.Signal` object
having the same name, as described in Symbol Resolution. If
Simulink does not find such an object, the compilation stops with
an error. Otherwise, Simulink compares the attributes of the signal object to the
corresponding attributes of the Data Store Memory block. If the block
and the object attributes are inconsistent, Simulink halts model compilation and displays an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### Diagnostics

### **Detect Read Before Write** — Action when model attempts to read data before writing in current time step `warning` (default) | `none` | `error`

Select the diagnostic action to take if the model attempts to read
data from a data store to which it has not written data in this time
step. See also the Detect read before write diagnostic in the **Data Store Memory
block** section of the **Model Configuration Parameters** >  **Diagnostics** > **Data Validity** pane.

- `None` — Produce no response.
- `Warning` — Display a warning and
  continue the simulation.
- `Error` — Terminate the simulation
  and display an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ReadBeforeWriteMsg` |
| **Type:** character vector |
| **Values:** `'none' | 'warning' | 'error'` |
| **Default:** `'warning'` |

### **Detect Write After Read** — Action when block attempts to write after reading in same time step `warning` (default) | `none` | `error`

Select the diagnostic action to take if the model attempts to write
data to the data store after previously reading data from it in the
current time step. See also the Detect write after read diagnostic in the **Data Store Memory block**
section of the **Model Configuration Parameters** >  **Diagnostics** > **Data Validity** pane.

- `None` — Produce no response.
- `Warning` — Display a warning and
  continue the simulation.
- `Error` — Terminate the simulation
  and display an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `WriteAfterReadMsg` |
| **Type:** character vector |
| **Values:** `'none' | 'warning' | 'error'` |
| **Default:** `'warning'` |

### **Detect Write After Write** — Action when model writes twice in same time step `warning` (default) | `none` | `error`

Select the diagnostic action to take if the model attempts to write
data to the data store twice in succession in the current time step. See
also the Detect write after write diagnostic in the **Data Store Memory
block** section of the **Model Configuration Parameters** >  **Diagnostics** > **Data Validity** pane.

- `None` — Produce no response.
- `Warning` — Display a warning and
  continue the simulation.
- `Error` — Terminate the simulation
  and display an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `WriteAfterWriteMsg` |
| **Type:** character vector |
| **Values:** `'none' | 'warning' | 'error'` |
| **Default:** `'warning'` |

### Logging

### **Log data store data** — Option to log data store data `off` (default) | `on`

Select this option to save the values of this signal to the
MATLAB workspace during simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataLogging` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Logging name** — Name associated with logged signal data `Use data store name` (default) | `Custom`

Use this pair of controls, consisting of a list box and an edit field,
to specify the name associated with logged signal data.

Simulink uses the signal name as its logging name by default. To
specify a custom logging name, select `Custom`
from the list box and enter the custom name in the adjacent edit
field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataLoggingNameMode` |
| **Type:** character vector |
| **Values:** `'SignalName'` | `'Custom'` |
| **Default:** `'SignalName'` |

If you set `DataLoggingNameMode` to
`'Custom'`, you must specify the name
associated with logged signal data using the
`DataLoggingName` parameter.

|  |
| --- |
| **Block Parameter:** `DataLoggingName` |
| **Type:** character vector |
| **Values:** character vector |
| **Default:** `''` |

### **Limit data points to last** — Option to discard all but last *N* data points `5000` | non-zero integer

Discard all but the last `N` data points, where
`N` is the number that you enter in the adjacent
edit field. For more information, see Log Data Stores.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataLoggingLimitDataPoints` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `DataLoggingMaxPoints` |
| **Type:** character vector |
| **Values:** nonzero integer |
| **Default:** `'5000'` |

### **Decimation** — Option to log every *N*th data point `2` (default) | integer

Log every `N`th data point, where
`N` is the number that you enter in the adjacent
edit field. For example, suppose that your model uses a fixed-step
solver with a step size of `0.1` s. If you select this
option and accept the default decimation value (`2`),
the software records data points for this signal at times
`0.0`, `0.2`,
`0.4`, and so on. For more information, see Log Data Stores.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataLoggingDecimateData` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `DataLoggingDecimation` |
| **Type:** character vector |
| **Values:** non-zero integer |
| **Default:** `'2'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

To generate PLC code for a model that uses a Data Store Memory
block, first define a `Simulink.Signal` in the base
workspace. Then in the **Signal Attributes** tab of the block
parameters, set the data store name to resolve to that of the `Simulink.Signal` object.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024b: Log data stores in accelerator and rapid accelerator mode simulations

You can log Data Store Memory block variables in accelerator and rapid accelerator
mode simulations as well as normal mode simulations.

### R2023b: Access Data Store Memory block elements defined at a higher level in the model hierarchy

Starting in R2023b, the Data Store Read block, Data Store
Write block, S-Function block, MATLAB
Function block, MATLAB System block, and
Chart block can access the data store in a Data Store
Memory block defined at a higher level in the model hierarchy.
