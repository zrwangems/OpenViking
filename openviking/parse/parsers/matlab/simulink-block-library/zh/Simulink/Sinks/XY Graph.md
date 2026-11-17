---
type: simulink-block
title: 'Record, XY Graph'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2023b
official_category: 'Sinks'
documentation_page: 'record'
documentation_source_path: 'slref/record.html'
language: zh-CN
chinese_source: worker-translation
---

# Record, XY Graph

## 端口
```yaml
ports:
- name: Port_1
  summary: 要记录的信号 标量 | 向量 | 矩阵 | 数组 | 总线
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 要记录的信号 标量 | 向量 | 矩阵 | 数组 | 总线

要记录的信号。您可以通过将信号线拖到模块边缘或使用 **Ports** 参数来向 Record 模块添加端口。

Record 模块支持记录可变大小信号，但不支持可视化可变大小信号。

XY Graph 模块是 Record 模块的一种替代配置，可在 XY 图上可视化连接到两个输入端口的数据。第一个输入端口提供 XY 图的 *x* 数据，第二个输入端口提供 *y* 数据。

#### 提示

- 要记录基于帧的数据，请为接收基于帧信号的每个端口指定 **Input Processing** 参数。
- 当您将非标量信号连接到 XY Graph 模块的输入端口时，必须手动配置非标量信号的哪些通道或元素为 XY 图提供 *x* 和 *y* 数据。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Number of input ports
  summary: 输入端口数量 1（默认）| [1,100] 范围内的整数
  group: 主要
  block_parameter: '''NumPorts'''
  type: integer | character vector
  values: '[1,100] 范围内的整数'
  default: '1'
- name: Port
  summary: 要为其指定输入处理模式的端口 1（默认）| 整数
  group: 主要
  block_parameter: '''FrameSettings'''
  type: 逻辑数组
  values: 1×n 行向量，其中 n 等于端口数量
  default: '0'
- name: Input Processing
  summary: 所选端口的输入处理模式 Elements as channels (sample-based)（默认）| Columns as channels (frame-based)
  group: 主要
  block_parameter: '''FrameSettings'''
  type: 逻辑数组
  values: 1×n 行向量，其中 n 等于端口数量
  default: '0'
- name: Record to Workspace
  summary: 工作区记录选项 off（默认）| on
  group: 记录
  block_parameter: '''RecordToWorkspace'''
  type: character vector | boolean | numeric
  values: '''on'' | ''off'' | true 或 1 | false 或 0'
  default: '''off'''
- name: Workspace Variable Name
  summary: 包含所记录模块数据的工作区变量名称 recordout（默认）| 字符向量 | 字符串
  group: 记录
  block_parameter: '''VariableName'''
  type: character vector | string
  default: '''recordout'''
- name: Record to File
  summary: 记录到文件选项 off（默认）| on
  group: 记录
  block_parameter: '''RecordToFile'''
  type: character vector | boolean | numeric
  values: '''on'' | ''off'' | true 或 1 | false 或 0'
  default: '''off'''
- name: File Name
  summary: 包含所记录数据的文件名 recording.mldatx（默认）| 字符向量 | 字符串
  group: 记录
  block_parameter: '''FileName'''
  type: character vector | string
  default: '''recording.mldatx'''
- name: File Type
  summary: 所记录数据的文件类型 *.mldatx（默认）| *.mat | *.xslx
  group: 记录
  block_parameter: '''FileName'''
  type: character vector | string
  default: '''recording.mldatx'''
- name: File Location
  summary: 包含所记录数据的文件路径 工作目录（默认）| 字符向量 | 字符串
  group: 记录
  block_parameter: '''FileName'''
  type: character vector | string
  default: '''recording.mldatx'''
- name: Time
  summary: 将时间数据导出到 Excel 文件的选项 Shared Time Columns（默认）| Individual Time Columns
  group: 记录
- name: Attributes
  summary: 要导出到 Excel 文件的信号属性 Data Type | Units | Port Index | Block Path | Interpolation
  group: 记录
```

要修改 Record 模块参数，请使用属性检查器。

### 主要

### **Number of input ports** — 输入端口数量 `1`（默认）| [`1,100`] 范围内的整数

输入端口数量，指定为 `1` 到 `100`（含）之间的整数。

XY Graph 模块是 Record 模块的一种替代配置，可在 XY 图上可视化连接到两个输入端口的数据。第一个输入端口提供 XY 图的 *x* 数据，第二个输入端口提供 *y* 数据。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `'NumPorts'` |
| **类型：** `integer` | `character vector` |
| **值：** [`1`,`100`] 范围内的整数 |
| **默认值：** `1` |

### **Port** — 要为其指定输入处理模式的端口 `1`（默认）| 整数

将 **Port** 和 **Input Processing** 参数结合使用，可为端口指定输入处理模式。输入处理模式决定 Record 模块如何解释矩阵数据：

- 基于采样 — 矩阵中的每个元素是单独的通道。
- 基于帧 — 矩阵中的每一列是单独的通道。

要使用基于帧的输入处理，信号必须具有离散采样率，且采样值必须是非标量且具有固定维度。

默认情况下，每个端口将输入信号作为基于采样处理。

要更改端口的输入处理模式：

1. 使用 **Port** 参数选择端口号。
2. 使用 **Input Processing** 参数选择输入处理模式。

#### 编程方式使用

通过将 `FrameSettings` 参数指定为与模块端口数量相同元素数的行向量，以编程方式为每个端口指定输入处理模式。元素索引对应模块上的端口号。指定 `1` 表示该端口使用基于帧的输入处理，指定 `0` 表示使用基于采样的处理。

|  |
| --- |
| **模块参数：** `'FrameSettings'` |
| **类型：** 逻辑数组 |
| **值：** `1`×`n` 行向量，其中 `n` 等于端口数量 |
| **默认值：** `0` |

### **Input Processing** — 所选端口的输入处理模式 `Elements as channels (sample-based)`（默认）| `Columns as channels (frame-based)`

将 **Port** 和 **Input Processing** 参数结合使用，可为端口指定输入处理模式。输入处理模式决定 Record 模块如何解释矩阵数据：

- 基于采样 — 矩阵中的每个元素是单独的通道。
- 基于帧 — 矩阵中的每一列是单独的通道。

要使用基于帧的输入处理，信号必须具有离散采样率，且采样值必须是非标量且具有固定维度。

默认情况下，每个端口将输入信号作为基于采样处理。

要更改端口的输入处理模式：

1. 使用 **Port** 参数选择端口号。
2. 使用 **Input Processing** 参数选择输入处理模式。

#### 编程方式使用

通过将 `FrameSettings` 参数指定为与模块端口数量相同元素数的行向量，以编程方式为每个端口指定输入处理模式。元素索引对应模块上的端口号。指定 `1` 表示该端口使用基于帧的输入处理，指定 `0` 表示使用基于采样的处理。

|  |
| --- |
| **模块参数：** `'FrameSettings'` |
| **类型：** 逻辑数组 |
| **值：** `1`×`n` 行向量，其中 `n` 等于端口数量 |
| **默认值：** `0` |

### 记录

### **Record to Workspace** — 工作区记录选项 `off`（默认）| `on`

工作区记录选项。默认情况下，Record 模块仅将数据记录到仿真数据检查器。选择 **Record to Workspace** 可将连接到 Record 模块的信号数据以 `Simulink.SimulationData.Dataset` 对象记录到 MATLAB® 工作区。

使用 **Workspace Variable Name** 参数指定包含所记录 Record 模块数据的 `Dataset` 对象的名称。

#### 提示

- 当您将数据记录到工作区时，访问数据的方式取决于您的模型配置。默认情况下，模型将所有记录的数据以单个输出变量 `Simulink.SimulationOutput` 对象的形式提供。您可以使用 `get` 函数或使用点号加 Record 模块工作区变量名来访问 Record 模块数据。当 **Single simulation output** 选项禁用时，记录数据会出现在工作区中的单独变量中，您可以直接访问 Record 模块数据。
- 使用 **Logging intervals** 配置参数指定的记录区间适用于使用 Record 模块记录到工作区的数据。
- 您可以使用单个 Record 模块将数据记录到仿真数据检查器、工作区和文件。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `'RecordToWorkspace'` |
| **类型：** character vector | boolean | numeric |
| **值：** `'on'` | `'off'` | `true` 或 `1` | `false` 或 `0` |
| **默认值：** `'off'` |

### **Workspace Variable Name** — 包含所记录模块数据的工作区变量名称 `recordout`（默认）| 字符向量 | 字符串

包含所记录模块数据的工作区变量名称。

#### 依赖关系

要启用此参数，请选择 **Record to Workspace** 参数。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `'VariableName'` |
| **类型：** character vector | string |
| **默认值：** `'recordout'` |

### **Record to File** — 记录到文件选项 `off`（默认）| `on`

记录到文件选项。默认情况下，Record 模块仅将数据记录到仿真数据检查器。选择 **Record to File** 可将连接到 Record 模块的信号数据记录到文件。

#### 提示

- 使用 **File Name** 参数指定文件名。
- 使用 **File Type** 参数指定是将数据记录到 MLDATX 文件、MAT 文件还是 Excel 文件。
- 使用 **File Location** 参数指定文件路径。
- 使用 **Logging intervals** 配置参数指定的记录区间不适用于使用 Record 模块记录到文件的数据。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `'RecordToFile'` |
| **类型：** character vector | boolean | numeric |
| **值：** `'on'` | `'off'` | `true` 或 `1` | `false` 或 `0` |
| **默认值：** `'off'` |

### **File Name** — 包含所记录数据的文件名 `recording.mldatx`（默认）| 字符向量 | 字符串

包含所记录数据的文件名。名称不需要包含文件扩展名。如果您在名称中包含了文件扩展名，请确保该名称使用指定 **File Type** 的有效扩展名。

#### 提示

- 如果您在两次运行之间不更改记录文件的名称或位置，Record 模块将覆盖文件中的先前数据。
- 当您想将文件保存到工作目录以外的位置时，请使用 **File Location** 参数指定要保存文件的目录路径。

#### 依赖关系

要启用此参数，请选择 **Record to File** 参数。

#### 编程方式使用

使用 `FileName` 参数指定 **File Name**、**File Type** 和 **File Location** 参数。在传递给 `set_param` 的名称中包含所需文件类型的扩展名。当您想将文件保存到当前工作目录以外的位置时，请指定包含文件名和扩展名的路径。

|  |
| --- |
| **模块参数：** `'FileName'` |
| **类型：** character vector | string |
| **默认值：** `'recording.mldatx'` |

### **File Type** — 所记录数据的文件类型 `*.mldatx`（默认）| `*.mat` | `*.xslx`

使用 **File Type** 参数指定是将数据记录到 MLDATX 文件、MAT 文件还是 Excel 文件。

#### 提示

- 当您将数据记录到 Excel 文件时，数据格式如 Microsoft Excel Import, Export, and Logging Format 中所述。
- 当您将数据记录到 Excel 文件时，您可以使用 **Time** 参数指定是否共享时间列，并使用 **Attributes** 参数指定要记录的信号属性。

#### 依赖关系

要启用此参数，请选择 **Record to File**。

#### 编程方式使用

使用 `FileName` 参数指定 **File Name**、**File Type** 和 **File Location** 参数。在传递给 `set_param` 的名称中包含所需文件类型的扩展名。当您想将文件保存到当前工作目录以外的位置时，请指定包含文件名和扩展名的路径。

|  |
| --- |
| **模块参数：** `'FileName'` |
| **类型：** character vector | string |
| **默认值：** `'recording.mldatx'` |

### **File Location** — 包含所记录数据的文件路径 工作目录（默认）| 字符向量 | 字符串

当您想将包含所记录数据的文件保存到工作目录以外的位置时，请使用 **File Location** 参数指定要保存文件的位置。确保您对指定的目录具有写入权限。

#### 依赖关系

要启用此参数，请选择 **Record to File**。

#### 编程方式使用

使用 `FileName` 参数指定 **File Name**、**File Type** 和 **File Location** 参数。在传递给 `set_param` 的名称中包含所需文件类型的扩展名。当您想将文件保存到当前工作目录以外的位置时，请指定包含文件名和扩展名的路径。

|  |
| --- |
| **模块参数：** `'FileName'` |
| **类型：** character vector | string |
| **默认值：** `'recording.mldatx'` |

### **Time** — 将时间数据导出到 Excel 文件的选项 `Shared Time Columns`（默认）| `Individual Time Columns`

当您将 Record 模块数据记录到 Excel 文件时，使用 **Time** 参数指定如何记录信号时间数据。

- `Shared Time Columns` — 当多个信号的时间数据相同时，这些信号在记录文件中共享单个时间列。如果 Record 模块记录具有唯一时间数据的信号，记录文件仍可能包含多个时间列。
- `Individual Time Columns` — 每个记录的信号在记录文件中始终有自己的时间列。

#### 依赖关系

要启用此参数，请选择 **Record to File** 并将 **File Type** 指定为 `*.xlsx`。

### **Attributes** — 要导出到 Excel 文件的信号属性 `Data Type` | `Units` | `Port Index` | `Block Path` | `Interpolation`

当您将数据记录到 Excel 文件时，选择一个或多个信号属性选项以包含在记录文件中。所选信号属性按照 Microsoft Excel Import, Export, and Logging Format 中描述的格式出现在第一个数据点上方的信号列中。

#### 依赖关系

要启用此参数，请选择 **Record to File** 并将 **File Type** 指定为 `*.xlsx`。
## 所属库

Simulink / Sinks

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

此模块在代码生成时被忽略。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

当您将此模块与生成 HDL 代码的子系统一起使用时，可以使用此模块记录仿真数据。该模块不能包含在硬件实现中。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

此模块在代码生成时被忽略。

## 版本历史

**在 R2021a 中引入**

### R2023b：记录无界可变大小信号

在普通和加速模式仿真中，Record 模块支持记录无界可变大小信号，但不支持可视化无界可变大小信号。对于包含无界可变大小信号的非虚拟总线，不支持记录。

### R2023a：记录包含可变大小信号的非虚拟总线

在普通和加速模式仿真中，Record 模块支持记录：

- 直接或嵌套总线中包含可变大小信号的非虚拟总线
- 包含可变大小信号的嵌套非虚拟总线的总线

仅在普通模式仿真中，Record 模块支持记录：

- 包含可变大小信号的非虚拟总线的总线数组

Record 模块不支持可视化可变大小信号。

### R2022b：缩放单个信号

您可以在 Record 模块中为单个信号设置显示比例和偏移量。

- 时间图和迷你图 — 缩放和偏移 *y* 值的显示。
- XY 图 — 独立缩放和偏移 *x* 值和 *y* 值的显示。
- 地图 — 独立缩放和偏移经度和纬度。

光标继续显示未缩放的值。

### R2021b：XY Graph 模块替换为 Record 模块的替代配置

XY Graph 模块替换为预配置为在 XY 图上显示两个输入信号的 Record 模块。使用更新后的 XY Graph 模块，您可以：

- 在仿真期间在 XY 图上查看数据。
- 将 XY 图数据记录到工作区、文件或工作区和文件。
- 缩放、平移、适应视图以及调整 XY 图的轴范围，而无需重新仿真。
- 通过使用光标和添加趋势线来分析 XY 迹线。
- 添加额外的端口和子图，以在 XY 图旁边以多种可视化类型（包括时间图、地图或其他 XY 图）可视化额外的仿真数据。
- 在 XY 图上可视化多个迹线。

仿真时，先前版本的 XY Graph 模块会打开一个新窗口，在仿真期间显示所连接的信号数据。要查看更新后的 XY Graph 模块上的数据，请双击模型中的模块。要在新窗口中查看 XY 图，请右键单击模块并选择 **Open in New Window**。

现有模型中的 XY Graph 模块会自动替换为新的 XY Graph 模块。XY Graph 查看器也会替换为新的 XY Graph 模块。Goto 和 From 模块将信号连接到替换 XY Graph 查看器的 XY Graph 模块。

连接到 XY Graph 模块的信号始终流式传输到仿真数据检查器。

### R2021a：**Logging intervals** 配置参数适用于使用 Record 模块记录到工作区的数据

**Logging intervals** 配置参数适用于使用 Record 模块记录到工作区的数据。

**Logging intervals** 参数不影响使用 Record 模块记录到文件的数据，也不影响信号在 Record 模块中的显示方式。你还可以在 Simulation Data Inspector 中访问连接到 Record 模块的信号的完整信号数据。

## 描述

将数据记录到工作区、文件或两者

你可以使用 Record 模块或 XY Graph 模块将数据记录到工作区、文件或同时记录到工作区和文件。当你将数据记录到文件时，可以选择记录到 MAT 文件、MLDATX 文件或 Excel® 文件。连接到 Record 模块的信号始终记录到 Simulation Data Inspector。如果你决定在仿真后需要保存数据，可以将数据从 Record 模块导出到工作区或任何受支持的文件类型。

你还可以使用 Record 模块可视化已连接的信号。要查看连接到 Record 模块的信号的数据，请双击该模块。在 Record 模块中查看数据时，你可以访问仿真控制项，例如 **Run** 按钮。

默认情况下，Record 模块会在 sparklines 图上显示所有已连接的信号。每个已连接的信号都会添加一个 sparkline。当 sparklines 填满可见空间后，滚动条允许你继续绘制信号。

打开一个模型以查看由 Record 模块记录的数据，且模块参数在 Property Inspector 中可见。

### 构建可视化

Record 模块支持 Simulation Data Inspector 中可用的大多数可视化。当另一种可视化更适合你的数据时，你可以使用 **Layouts** 选项和绘图类型选择器（默认标记为 **Sparklines**）修改绘图布局和绘图类型。使用 **Layouts** 列表选择子图布局。要更改子图的绘图类型，请选择该子图，然后从绘图类型选择器中选择所需的绘图类型。

有关详细信息，请参阅 Log Data to the Workspace and a File Using the Record Block。有关展示如何使用每种可视化类型的示例，请参阅：

- 迷你图 — 使用迷你图一起查看多个信号
- XY — 在 XY 图上可视化仿真数据并使用 XY 图分析数据
- 地图 — 查看和回放地图数据
- 时间图与文本编辑器 — 使用仿真数据检查器创建图

Record 模块不支持 Simulation Data Inspector 中可用的数组可视化。Record 模块支持记录多维信号数据，包括可变大小信号，但不支持可视化多维数据。要使用 Record 模块可视化多维信号的数据，请将具有多维样本值的信号转换为一组信号，称为 *channels*，其中每个信号都具有标量样本值。有关详细信息，请参阅 Analyze Multidimensional Signal Data。
