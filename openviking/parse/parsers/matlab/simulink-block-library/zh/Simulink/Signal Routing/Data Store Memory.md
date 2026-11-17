---
type: simulink-block
title: 'Data Store Memory'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'SUP'
documentation_page: 'datastorememory'
documentation_source_path: 'slref/datastorememory.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Store Memory

## 端口

R2025b 中未记录。

## 参数

### 主要

### **Data store name** — 数据存储的名称 `A`（默认）| 字符向量 | 字符串

为使用此模块定义的数据存储指定名称。
具有相同名称的 Data Store Read 和 Data Store Write
模块可以读取和写入由此模块初始化的数据存储。该名称可以表示 Data Store
Memory 模块或定义为数据
存储的信号对象。

#### 程序化使用

|  |
| --- |
| **模块参数**：`DataStoreName` |
| **类型**：字符向量 |
| **值**：`'A' | ...` |
| **默认值**：`'A'` |

### **Rename All** — 在模型中重命名数据存储的选项 按钮

在模型中 Data Store Read
和 Data Store Write 模块使用此数据存储的所有位置重命名该数据存储。

#### 限制

在以下情况下，您不能使用 **Rename All** 重命名数据
存储：

- 在工作区中使用 `Simulink.Signal` 对象来控制为数据
  存储生成的代码
- 使用 `Simulink.Signal` 对象代替
  Data Store Memory 模块来定义
  数据存储

您必须改为从模型资源管理器中重命名相应的
`Simulink.Signal` 对象。有关示例，请参阅 Rename Data Store Defined by Signal Object。

### **Data store reference** — 用于访问更高层级模型中定义的内存 `off`（默认）| `on`

当您需要 Simulink® 的一部分访问在模型
层级中更高层定义的 Data Store
Memory 模块的元素时，选择此选项。这些模块包括 Data Store Read
模块、Data Store Write 模块、S-Function 模块、MATLAB Function 模块、
MATLAB System 模块和
Chart (Stateflow) 模块。

#### 程序化使用

|  |
| --- |
| **模块参数**：`DataStoreReference` |
| **类型**：`character vector` |
| **值**：`'off'|'on'` |
| **默认值**：`'off'` |

#### 限制

当您选择 **Data store reference**
参数时，不支持以下信号属性：
**Data type** 的 `Inherit`、**Dimensions** 的 `-1` 以及
**Signal type** 的 `auto`。您必须显式选择这些属性。

### **Corresponding Data Store Read/Write blocks** — 连接的 Data Store Read/Write 模块的路径 模块路径

列出所有与当前模块具有相同数据存储名称的 Data Store Read 和 Data Store
Write 模块，这些模块位于当前系统中或模型层级中其下方的任何子系统中。点击模块路径将在模型中显示并
高亮该模块。

### 信号属性

### **Initial value** — 数据存储的初始值 `0`（默认）| 标量 | 向量 | 矩阵 | N 维数组

指定数据存储的初始值。
**Minimum** 参数指定此参数的最小值，
**Maximum** 参数指定最大值。

如果指定非标量值并将
**Dimensions** 设置为 `-1`（默认值），则数据存储具有与该数组相同的维度。您写入数据存储的数据（通过使用 Data Store Write
模块）必须具有这些维度。

如果将 **Dimensions** 参数设置为 `-1` 以外的值，则初始值维度必须
与您指定的维度匹配，除非初始值是标量或 MATLAB® 结构体。如果指定标量，则数据
存储的每个元素使用该标量作为初始值。使用此方法可以将相同的初始值（您指定的标量）应用于每个
元素，而无需手动将初始值的维度与数据存储的维度匹配。

要使用此模块初始化非虚拟总线信号，请将初始值指定为 MATLAB 结构体，并将模型配置参数 Underspecified initialization detection 设置为 `Simplified`。有关使用结构体
初始化非虚拟总线信号的更多信息，请参阅 Specify Initial Conditions for Bus Elements。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InitialValue` |
| **类型**：字符向量 |
| **值**：标量 | 向量 | 矩阵 | N 维数组 |
| **默认值**：`'0'` |

### **Minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

指定模块应输出的最小值。默认
值为 `[]`（未指定）。此数字必须是
有限实数双精度标量值。

**注意**

如果为此模块的数据类型指定总线对象，请
不要在模块上设置总线数据的最小值。Simulink
会忽略此设置。而应设置指定为数据类型的总线对象的
总线元素的最小值。有关总线元素的 Minimum 属性的
信息，请参阅 `Simulink.BusElement`。

Simulink 使用最小值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。
  此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的
  结果。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

### **Maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

指定模块应输出的最大值。默认
值为 `[]`（未指定）。此数字必须是
有限实数双精度标量值。

**注意**

如果为此模块的数据类型指定总线对象，请
不要在模块上设置总线数据的最大值。Simulink
会忽略此设置。而应设置指定为数据类型的总线对象的
总线元素的最大值。有关总线元素的 Maximum 属性的
信息，请参阅 `Simulink.BusElement`。

Simulink 使用最大值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。
  此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的
  结果。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'[ ]'` |

### **Data type** — 输出数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Enum: <class name>` | `Simulink.ImageType(480,640,3)`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则（例如
  `Inherit: auto`）。
- 内置数据类型的名称（例如
  `single`）。
- 数据类型对象的名称（例如
  `Simulink.NumericType` 对象）。
- 计算结果为数据类型的表达式（例如
  `fixdt(1,16,0)`）。不要在表达式中将总线
  对象指定为数据类型；请使用 `Bus:
  <object name>` 来指定总线数据
  类型。
- 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数并指定
  描述图像的属性。默认情况下，数据类型使用
  `Simulink.ImageType(480,640,3)` 表达式，
  该表达式分别表示图像的行、列和通道。

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: auto' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'string' | 'Enum: <class name>' | 'Simulink.ImageType(480,640,3)'` |
| **默认值：** `'Inherit: auto'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的
**Output** 数据类型。有关更多
信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Dimensions (-1 to infer from Initial value)** — 数据存储的维度 `-1`（默认）| 标量 | 向量 | 矩阵

数据存储的维度。默认值
`-1` 使您能够通过 **Initial value** 参数设置数据
存储的维度。
但是，在这种情况下，您不能对初始
值使用标量扩展。您必须使用具有所需
维度的数组来指定初始值。

如果使用 `-1` 以外的值，请指定与 **Initial value**
参数的维度相同的维度，除非您将初始值指定为标量（用于标量
扩展）或 MATLAB 结构体。如果数据存储表示总线数组，
并且您使用 MATLAB 结构体作为初始值，则可以指定
维度以使用此结构体初始化总线数组。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Dimensions` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'-1'` |

### **Interpret vector parameters as 1-D** — 将向量解释为一维的选项 `on`（默认）| `off`

指定数据存储将向量初始值解释为
一维。

默认情况下，MATLAB 将向量数据表示为矩阵，矩阵具有两个
维度。例如，MATLAB 将向量 `[1 2 3]` 表示为
1×3 矩阵。

当您选择此参数时，数据存储仅使用一个维度而不是两个维度来表示向量数据。例如，如果您指定
初始值 `[1 2 3]`，则数据存储存储一个包含三个元素的
一维向量。

有关更多信息，请参阅 Determine the Output Dimensions of Source Blocks。

#### 程序化使用

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

### **Signal type** — 数据存储值的复杂度 `auto`（默认）| `real` | `complex`

指定数据存储中值的数值类型，实数或复数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SignalType` |
| **类型：** 字符向量 |
| **值：** `'auto' | 'real' | 'complex'` |
| **默认值：** `'auto'` |

### **Share across model instances** — 允许 Model 模块从同一数据存储读取的选项 `off`（默认）| `on`

在单个模型引用层级中，当您使用多个
Model 模块引用包含
Data Store Memory 模块的模型时，默认情况下，被引用模型的每个实例（每个 Model 模块）读取和
写入数据存储的单独副本。当您选择
**Share across model instances** 时，所有实例不是与单独的副本
交互，而是读取和写入同一数据存储。

当您将模型配置参数 **Code
interface packaging** 设置为 `Reusable
function` 以从模型生成可重入代码
(Simulink
Coder™) 时，选择了 **Share across model
instances** 的数据存储在代码中显示为全局符号，
生成的入口点函数直接访问该符号。例如，
全局符号是全局变量或全局结构体
变量的字段。因此，您的代码对入口点
函数进行的每次调用（模型的每个实例）都共享该数据。

有关示例，请参阅 Share Data Among Multiple Instances of a Reusable Algorithm。有关
更多信息，请参阅 Share Data Among Referenced Model Instances。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShareAcrossModelInstances` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Data store name must resolve to Simulink signal object** — 将数据存储名称解析为 Simulink 信号对象的选项 `off`（默认）| `on`

指定 Simulink 软件在编译模型时，在模型和
基础工作区中搜索具有相同名称的 `Simulink.Signal` 对象，如 Symbol Resolution 中所述。如果
Simulink 未找到此类对象，则编译停止并
报错。否则，Simulink 将信号对象的属性与
Data Store Memory 模块的相应属性进行比较。如果模块
和对象属性不一致，Simulink 会停止模型编译并显示错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateMustResolveToSignalObject` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### 诊断

### **Detect Read Before Write** — 模型在当前时间步中尝试在写入之前读取数据时的操作 `warning`（默认）| `none` | `error`

选择当模型尝试从数据存储读取数据但在此时间
步中尚未向其写入数据时要采取的诊断操作。另请参阅 **Model Configuration Parameters** > **Diagnostics** > **Data Validity** 窗格中 **Data Store Memory
block** 部分的 Detect read before write 诊断。

- `None` — 不产生响应。
- `Warning` — 显示警告并
  继续仿真。
- `Error` — 终止仿真
  并显示错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ReadBeforeWriteMsg` |
| **类型：** 字符向量 |
| **值：** `'none' | 'warning' | 'error'` |
| **默认值：** `'warning'` |

### **Detect Write After Read** — 模块在同一时间步中读取后尝试写入时的操作 `warning`（默认）| `none` | `error`

选择当模型在当前时间步中先前从数据存储读取数据后尝试向其写入
数据时要采取的诊断操作。另请参阅 **Model Configuration Parameters** > **Diagnostics** > **Data Validity** 窗格中 **Data Store Memory block**
部分的 Detect write after read 诊断。

- `None` — 不产生响应。
- `Warning` — 显示警告并
  继续仿真。
- `Error` — 终止仿真
  并显示错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `WriteAfterReadMsg` |
| **类型：** 字符向量 |
| **值：** `'none' | 'warning' | 'error'` |
| **默认值：** `'warning'` |

### **Detect Write After Write** — 模型在同一时间步中写入两次时的操作 `warning`（默认）| `none` | `error`

选择当模型在当前时间步中连续两次尝试向数据存储写入
数据时要采取的诊断操作。另请
参阅 **Model Configuration Parameters** > **Diagnostics** > **Data Validity** 窗格中 **Data Store Memory
block** 部分的 Detect write after write 诊断。

- `None` — 不产生响应。
- `Warning` — 显示警告并
  继续仿真。
- `Error` — 终止仿真
  并显示错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `WriteAfterWriteMsg` |
| **类型：** 字符向量 |
| **值：** `'none' | 'warning' | 'error'` |
| **默认值：** `'warning'` |

### 记录

### **Log data store data** — 记录数据存储数据的选项 `off`（默认）| `on`

选择此选项可在仿真期间将此信号的值保存到
MATLAB 工作区。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataLogging` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **日志名称** — 与记录的信号数据关联的名称 `Use data store name`（默认）| `Custom`

使用这对控件（由一个列表框和一个编辑字段组成）来指定与记录的信号数据关联的名称。

默认情况下，Simulink 使用信号名称作为其日志名称。要指定自定义日志名称，请从列表框中选择 `Custom`，然后在相邻的编辑字段中输入自定义名称。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataLoggingNameMode` |
| **类型：** 字符向量 |
| **值：** `'SignalName'` | `'Custom'` |
| **默认值：** `'SignalName'` |

如果将 `DataLoggingNameMode` 设置为 `'Custom'`，则必须使用 `DataLoggingName` 参数指定与记录的信号数据关联的名称。

|  |
| --- |
| **模块参数：** `DataLoggingName` |
| **类型：** 字符向量 |
| **值：** 字符向量 |
| **默认值：** `''` |

### **将数据点限制为最后** — 丢弃除最后 *N* 个数据点之外的所有数据点的选项 `5000` | 非零整数

丢弃除最后 `N` 个数据点之外的所有数据点，其中 `N` 是您在相邻编辑字段中输入的数字。有关详细信息，请参阅记录数据存储。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataLoggingLimitDataPoints` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

|  |
| --- |
| **模块参数：** `DataLoggingMaxPoints` |
| **类型：** 字符向量 |
| **值：** 非零整数 |
| **默认值：** `'5000'` |

### **抽取** — 记录每第 *N* 个数据点的选项 `2`（默认）| 整数

记录每第 `N` 个数据点，其中 `N` 是您在相邻编辑字段中输入的数字。例如，假设您的模型使用步长为 `0.1` 秒的固定步长求解器。如果您选择此选项并接受默认抽取值（`2`），软件将在 `0.0`、`0.2`、`0.4` 等时刻记录此信号的数据点。有关详细信息，请参阅记录数据存储。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataLoggingDecimateData` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

|  |
| --- |
| **模块参数：** `DataLoggingDecimation` |
| **类型：** 字符向量 |
| **值：** 非零整数 |
| **默认值：** `'2'` |

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

要为使用 Data Store Memory 模块的模型生成 PLC 代码，请首先在基础工作区中定义一个 `Simulink.Signal`。然后在模块参数的 **Signal Attributes** 选项卡中，将数据存储名称设置为解析为该 `Simulink.Signal` 对象的名称。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024b：在加速和快速加速模式仿真中记录数据存储

您可以在加速和快速加速模式仿真以及普通模式仿真中记录 Data Store Memory 模块变量。

### R2023b：访问在模型层次结构中更高层定义的 Data Store Memory 模块元素

从 R2023b 开始，Data Store Read 模块、Data Store Write 模块、S-Function 模块、MATLAB Function 模块、MATLAB System 模块和 Chart 模块可以访问在模型层次结构中更高层定义的 Data Store Memory 模块中的数据存储。

## 描述

定义数据存储

Data Store Memory 模块定义并初始化一个命名共享数据存储，这是一个可供指定相同数据存储名称的 Data Store Read 和 Data Store Write 模块使用的内存区域。

定义数据存储的 Data Store Memory 模块的位置决定了哪些 Data Store Read 和 Data Store Write 模块可以访问该数据存储：

- 如果 Data Store Memory 模块位于*顶层系统*中，则模型中任意位置的 Data Store Read 和 Data Store Write 模块都可以访问该数据存储。
- 如果 Data Store Memory 模块位于*子系统*中，则同一子系统中或模型层次结构中其下方任意子系统中的 Data Store Read 和 Data Store Write 模块都可以访问该数据存储。
- 在引用模型内部定义的 Data Store Read 或 Data Store Write 模块可以访问模型层次结构中更高层的数据存储。

要允许引用模型内部的 Data Store Read 或 Data Store Write 模块访问模型层次结构中更高层的数据存储：

- 在引用模型内部放置一个 Data Store Memory 模块。
- 在 Data Store Memory 模块对话框中，选择 **Data store reference**。

不要在 For Each 子系统中包含 Data Store Memory 模块。

从数据存储获得正确结果需要确保数据存储的读取和写入按预期顺序发生。有关详细信息，请参阅：

- 数据存储访问排序
- 数据存储诊断
- 记录数据存储

除了使用 Data Store Memory 模块之外，您还可以使用 `Simulink.Signal` 对象来定义数据存储，或者使用 `Simulink.Signal` 对象替代 Data Store Memory 模块。在*基础*工作区中使用信号对象定义的数据存储是*全局*数据存储。全局数据存储可供每个模型访问，包括所有引用模型。有关详细信息，请参阅数据存储。

您可以选择 Data Store Read、Data Store Write 或 Data Store Memory 模块来高亮显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请将鼠标悬停在选择后出现的省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块与所选模块对应时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开图或新选项卡。

### 字符串支持

Data Store Memory 模块仅在模块配置为 **Initial value** 参数的默认值（`0`）时，才能接受和输出字符串数据类型。
