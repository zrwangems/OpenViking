---
type: simulink-block
title: 'Record'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'record'
documentation_source_path: 'slref/record.html'
language: zh-CN
chinese_source: worker-translation
---

# Record

## 端口

### 输入

### **Port\_1** — 要记录的信号 scalar | vector | matrix | array | bus

要记录的信号。您可以通过将连线拖到模块边缘或使用 **端口** 参数来向 Record 模块添加端口。

Record 模块支持记录可变大小信号，但不支持可视化可变大小信号。

XY Graph 模块是 Record 模块的替代配置，用于在 XY 图上可视化连接到两个输入端口的数据。第一个输入端口提供 XY 图的 *x* 数据，第二个输入端口提供 *y* 数据。

#### 提示

- 要记录基于帧的数据，请为接收基于帧信号的每个端口指定 **输入处理** 参数。
- 当您将非标量信号连接到 XY Graph 模块的输入端口时，必须手动配置非标量信号的哪些通道或元素为 XY 图提供 *x* 和 *y* 数据。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **输入端口数** — 输入端口数 `1`（默认）| [`1,100`] 范围内的整数

输入端口数，指定为介于 `1` 和 `100` 之间（含两端）的整数。

XY Graph 模块是 Record 模块的替代配置，用于在 XY 图上可视化连接到两个输入端口的数据。在 XY Graph 模块中，第一个输入端口提供 *x* 数据，第二个输入端口提供 *y* 数据。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumPorts` |
| **值：** | `1`（默认）| [`1`, `100`] 范围内的整数 |
| **数据类型：** | `integer` |

**示例：** `set_param("myModel/Record","NumPorts",2)`

### **抽取** — 抽取因子 `1`（默认）| 正整数

*自 R2025a 起*

指定抽取因子以降低记录数据的有效采样率。对于抽取因子 *n*，Record 模块记录每第 *n* 个采样值。例如，当您将 **抽取** 值指定为 `2` 时，Record 模块每隔一个数据点记录一次。

有关控制仿真期间记录哪些采样值的详细信息，请参阅 Specify Signal Values to Log。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Decimation` |
| **值：** | `"1"`（默认）| 带引号的正整数 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","Decimation","2")`

### **将数据点限制为最后** — 要记录的采样数 `inf`（默认）| 标量 | 向量

*自 R2025a 起*

当您只想保存或分析仿真末尾的数据时，请将要记录的采样数指定为大于零的正整数。默认情况下，Record 模块记录整个仿真的数据，并且 **将数据点限制为最后** 参数的值为 `inf`。

将记录数据限制为最后 *n* 个信号值会直接影响内存分配。当您指定此参数时，软件会根据指定的值预先分配内存，而不是根据仿真期间生成的时间步。因此，当记录不确定数量的时间步时，不建议使用 **将数据点限制为最后** 参数。

有关控制仿真期间记录哪些采样值的详细信息，请参阅 Specify Signal Values to Log。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDataPoints` |
| **值：** | `"inf"`（默认）| 带引号的正整数 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","MaxDataPoints","20")`

### **选择端口** — 要为其指定输入处理模式的端口 `1`（默认）| 整数

结合使用 **选择端口** 和 **输入处理** 参数来指定端口的输入处理模式。输入处理模式确定 Record 模块如何解释矩阵数据：

- Sample-based — 矩阵中的每个元素是单独的通道。
- Frame-based — 矩阵中的每一列是单独的通道。

要使用基于帧的输入处理，信号必须具有离散采样率，并且采样值必须是非标量且具有固定维度。

默认情况下，每个端口将输入信号作为 sample-based 处理。

要更改端口的输入处理模式：

1. 使用 **选择端口** 参数选择端口号。
2. 使用 **输入处理** 参数选择输入处理模式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

通过将 `FrameSettings` 参数指定为具有与模块端口数量相同元素数的行向量，以编程方式为每个端口指定输入处理模式。元素索引对应于模块上的端口号。指定 `1` 以对端口使用基于帧的输入处理，指定 `0` 以使用基于采样的处理。

|  |  |
| --- | --- |
| **参数：** | `FrameSettings` |
| **值：** | `false`（默认）| `1`-by-`n` 逻辑值行向量，其中 `n` 等于端口数 |
| **数据类型：** | `logical array` |

**示例：** `set_param("myModel/Record","FrameSettings",[true,false,true])`

### **输入处理** — 所选端口的输入处理模式 `Elements as channels (sample-based)`（默认）| `Columns as channels (frame-based)`

结合使用 **选择端口** 和 **输入处理** 参数来指定端口的输入处理模式。输入处理模式确定 Record 模块如何解释矩阵数据：

- Sample-based — 矩阵中的每个元素是单独的通道。
- Frame-based — 矩阵中的每一列是单独的通道。

要使用基于帧的输入处理，信号必须具有离散采样率，并且采样值必须是非标量且具有固定维度。

默认情况下，每个端口将输入信号作为 sample-based 处理。

要更改端口的输入处理模式：

1. 使用 **选择端口** 参数选择端口号。
2. 使用 **输入处理** 参数选择输入处理模式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

通过将 `FrameSettings` 参数指定为具有与模块端口数量相同元素数的行向量，以编程方式为每个端口指定输入处理模式。元素索引对应于模块上的端口号。指定 `1` 以对端口使用基于帧的输入处理，指定 `0` 以使用基于采样的处理。

|  |  |
| --- | --- |
| **参数：** | `FrameSettings` |
| **值：** | `false`（默认）| `1`-by-`n` 逻辑值行向量，其中 `n` 等于端口数 |
| **数据类型：** | `logical array` |

**示例：** `set_param("myModel/Record","FrameSettings"[true,false,true])`

### 记录

### **记录到工作区** — 工作区记录选项 `off`（默认）| `on`

工作区记录选项。默认情况下，Record 模块仅将数据记录到仿真数据检查器。选择 **记录到工作区** 可将连接到 Record 模块的信号数据记录到 MATLAB® 工作区中的 `Simulink.SimulationData.Dataset` 对象。

使用 **工作区变量名称** 参数指定包含记录的 Record 模块数据的 `Dataset` 对象名称。

#### 提示

- 当您将数据记录到工作区时，访问数据的方式取决于您的模型配置。默认情况下，模型将所有记录的数据作为 `Simulink.SimulationOutput` 对象提供在单个输出变量中。您可以使用 `get` 函数或通过 Record 模块工作区变量名的点表示法访问 Record 模块数据。当 **单一仿真输出** 选项禁用时，记录数据会显示在工作区的单独变量中，您可以直接访问 Record 模块数据。
- 使用 **记录间隔** 配置参数指定的记录间隔适用于使用 Record 模块记录到工作区的数据。
- 使用单个 Record 模块将数据记录到仿真数据检查器、工作区和文件。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RecordToWorkspace` |
| **值：** | `"off"`（默认）| "on" | `false` 或 `0` | `true` 或 `1` |

**示例：** `set_param("myModel/Record","RecordToWorkspace","on")`

### **工作区变量名称** — 包含记录的模块数据的工作区变量名称 `recordout`（默认）| 字符向量 | 字符串

包含记录的模块数据的工作区变量名称。

#### 依赖关系

要启用此参数，请选择 **记录到工作区** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariableName` |
| **值：** | `"recordout"`（默认）| 有效的 MATLAB 变量名称 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","VariableName","RecordedData")`

### **记录到文件** — 记录到文件选项 `off`（默认）| `on`

记录到文件选项。默认情况下，Record 模块仅将数据记录到仿真数据检查器。选择 **记录到文件** 可将连接到 Record 模块的信号数据记录到文件。

#### 提示

- 使用 **文件名** 参数指定文件的名称。
- 使用 **文件类型** 参数指定是将数据记录到 MLDATX 文件、MAT 文件、Excel 文件还是 Parquet 文件 *(自 R2025a 起)*。
- 使用 **文件位置** 参数指定文件的路径。
- 使用 **记录间隔** 配置参数指定的记录间隔不适用于使用 Record 模块记录到文件的数据。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RecordToFile` |
| **值：** | `"off"`（默认）| "on" | `false` 或 `0` | `true` 或 `1` |

**示例：** `set_param("myModel/Record","RecordToFile","on")`

### **文件名** — 包含记录数据的文件名称 `recording.mldatx`（默认）| 字符向量 | 字符串

包含记录数据的文件名称。名称无需包含文件扩展名。如果您在名称中包含文件扩展名，请确保该名称对指定的 **文件类型** 使用有效的扩展名。

#### 提示

- 如果从一次运行到下一次运行，您不更改记录到的文件的名称或位置，Record 模块将覆盖文件中的先前数据。
- 当您要将文件保存到工作目录以外的位置时，请使用 **文件位置** 参数指定要保存文件的目录路径。

#### 依赖关系

要启用此参数，请选择 **记录到文件** 参数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

指定 **文件名**、**文件类型** 和 **文件位置** 参数。在传递给 `set_param` 的名称中包含所需文件类型的扩展名。当您要将文件保存到当前工作目录以外的位置时，请指定包含文件名和扩展名的路径。

|  |  |
| --- | --- |
| **参数：** | `FileName` |
| **值：** | `"recording.mldatx"`（默认）| 有效文件名 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","FileName","myRecording.mldatx")`

### **文件类型** — 记录数据的文件类型 `*.mldatx`（默认）| `*.mat` | `*.xslx` | `*.parquet`

使用 **文件类型** 参数指定要将数据记录到 MLDATX、MAT、Excel 还是 Parquet 文件 *(自 R2025a 起)*。

#### 提示

- 当您将数据记录到 Excel 文件时，数据将按 Microsoft Excel Import, Export, and Logging Format 中所述进行格式化。
- 当您将数据记录到 Excel 文件时，可以使用 **时间** 参数指定是否共享时间列，并使用 **属性** 参数指定要记录的信号属性。

#### 依赖关系

要启用此参数，请选择 **记录到文件**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

使用 `FileName` 参数指定 **文件名**、**文件类型** 和 **文件位置** 参数。在传递给 `set_param` 的名称中包含所需文件类型的扩展名。当您要将文件保存到当前工作目录以外的位置时，请指定包含文件名和扩展名的路径。

|  |  |
| --- | --- |
| **参数：** | `FileName` |
| **值：** | `"recording.mldatx"`（默认）| 有效文件名 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","FileName","myRecording.parquet")`

### **文件位置** — 包含记录数据的文件路径 工作目录（默认）| 字符向量 | 字符串

当您要将文件保存到工作目录以外的位置时，使用 **文件位置** 参数指定要保存包含记录数据的文件的位置。确保您在指定的目录中具有写入权限。

#### 依赖关系

要启用此参数，请选择 **记录到文件**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

使用 `FileName` 参数指定 **文件名**、**文件类型** 和 **文件位置** 参数。在传递给 `set_param` 的名称中包含所需文件类型的扩展名。当您要将文件保存到当前工作目录以外的位置时，请指定包含文件名和扩展名的路径。

|  |  |
| --- | --- |
| **参数：** | `FileName` |
| **值：** | `"recording.mldatx"`（默认）| 有效文件名 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","FileName","myRecording.mldatx")`

### **时间** — 将时间数据导出到 Excel 或 Parquet 文件的选项 `Shared Time Columns`（默认）| `Individual Time Columns`

指定当您将 Record 模块数据记录到 Excel 文件或 Parquet 文件时如何记录信号时间数据 *(自 R2025a 起)*。

- `Shared Time Columns` — 当多个信号的时间数据相同时，这些信号在记录文件中共享单个时间列。如果 Record 模块记录具有唯一时间数据的信号的数据，则记录文件仍可包含多个时间列。
- `Individual Time Columns` — 每个记录的信号在记录文件中始终拥有自己的时间列。

#### 依赖关系

要启用此参数，请选择 **记录到文件**，并将 **文件类型** 指定为 `*.xlsx` 或 `*.parquet` *(自 R2025a 起)*。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

以编程方式设置 **时间** 参数仅支持 Parquet 文件。

|  |  |
| --- | --- |
| **参数：** | `SharedTimeColumn` |
| **值：** | `"on"`（默认）| `"off"` |

**示例：** `set_param("myModel/Record","SharedTimeColumn",
"off")`

### **信号属性** — 要导出到 Excel 文件的信号属性 `Data Type` | `Units` | `Port Index` | `Block Path` | `Interpolation`

选择一个或多个信号属性选项，以便在将数据记录到 Excel 文件时包含在日志文件中。选定的信号属性按照 Microsoft Excel 导入、导出和日志记录格式中描述的格式，显示在第一个数据点上方的信号列中。

#### 依赖项

要启用此参数，请选择 **记录到文件**，并将 **文件类型** 指定为 `*.xlsx`。

### **压缩类型** — 压缩选项 `Fastest (snappy)`（默认） | `Balanced for Size and Speed (gzip)` | `Compact (brotli)` | `None (uncompressed)`

*自 R2025a 起*

将压缩指定为以下选项之一：

- `Fastest (snappy)` — 保存速度与未压缩文件相似，文件大小更小
- `Balanced for Size and Speed (gzip)` — 在文件大小和保存速度之间取得平衡
- `Compact (brotli)` — 文件大小最小，保存速度最慢
- `None (uncompressed)` — 文件大小最大，保存速度最快

#### 依赖项

要启用此参数，请选择 **记录到文件**，并将 **文件类型** 指定为 `*.parquet`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParquetCompression` |
| **值：** | `"fastest"`（默认） | `"balanced"` | `"compact"` | `"none"` |

**示例：** `set_param("myModel/Record","ParquetCompression","balanced")`

### **生成 Sidecar** — 生成 JSON sidecar 的选项 `on`（默认） | `off`

*自 R2025a 起*

选择此参数以生成包含所有记录元数据的 JSON sidecar。

#### 依赖项

要启用此参数，请选择 **记录到文件**，并将 **文件类型** 指定为 `*.parquet`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParquetMetaData` |
| **值：** | `"on"`（默认） | `"off"` |

**示例：** `set_param("myModel/Record","ParquetMetaData","off")`

### **行组策略** — Parquet 文件中对行进行分组的选项 `Row Group Height`（默认） | `Row Group Size (MB)`

*自 R2025a 起*

指定 Parquet 文件中的行组。

- `Row Group Height` — 指定每个组的行数。
- `Row Group Size (MB)` — 以兆字节为单位指定行组的大小。

#### 依赖项

要启用此参数，请选择 **记录到文件**，并将 **文件类型** 指定为 `*.parquet`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParquetRowGroupPolicy` |
| **值：** | `"height"`（默认） | `"sizeinmb"` |

**示例：** `set_param("myModel/Record","ParquetRowGroupPolicy","sizeinmb")`

### **行组策略值** — 行组的高度或大小 `auto`（默认，当 `Row Group Policy` 为 `Row Group Height`） | `512`（默认，当 `Row Group Policy` 为 `Row Group Size (MB)` | 行数 | 行组大小

*自 R2025a 起*

要指定每个行组中的行数，请将 **行组策略** 参数设置为 `Row Group Height`。然后，使用 **行组策略值** 参数定义每个组中的行数，选择 `1` 到 `67,108,864` 之间的值。默认情况下，该值为 `auto`，这会创建不超过 512 MB 的最大可能行组。

要指定每个行组的大小，请将 **行组策略** 参数设置为 `Row Group Size (MB)`。然后，使用 **行组策略值** 参数以兆字节为单位设置行组的数据大小，最大为 1GB。

#### 依赖项

要启用此参数，请选择 **记录到文件**，并将 **文件类型** 指定为 `*.parquet`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParquetRowGroupHeight` |
| **值：** | `"auto"`（默认） | 带引号的整数，范围 [`1`, `67108864`] |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","ParquetRowGroupPolicy","height","ParquetRowGroupHeight","5000")`

|  |  |
| --- | --- |
| **参数：** | `ParquetRowGroupSize` |
| **值：** | `"512"`（默认） | 带引号的正数，范围 (`0`, `1000`] |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param("myModel/Record","ParquetRowGroupPolicy","sizeinmb","ParquetRowGroupsize","450")`

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

此模块在代码生成时会被忽略。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

此模块在代码生成时会被忽略。

## 版本历史

**在 R2021a 中引入**

### R2025a：记录 `datetime` 数据

Record 模块支持记录 `datetime` 数据。

### R2025a：XY 可视化中不再支持实时流式传输

为避免可扩展性问题，数据不再流式传输到 Simulation Data Inspector、Record 模块或 XY Graph 模块中的 XY 可视化。

### R2025a：限制 Record 模块记录的数据

通过指定要记录的信号值，限制 Record 模块记录的数据大小。可以使用以下两个参数指定要记录的信号值：

- **抽取** — 记录每第 *n* 个信号值。
- **将数据点限制为最后** — 仅记录最后 *n* 个信号值。

### R2025a：使用 Record 模块将数据导出到 Parquet 文件

使用 Record 模块将来自标量和多维信号的数据，以及来自总线或总线数组的数据，导出到 Parquet 文件。Record 模块记录并可导出任何内置数据类型的实数和复数数据，以及枚举、字符串和定点数据。有关更多信息，请参阅使用 Record 模块将数据导出到 Parquet 文件。

### R2023b：记录无界可变大小信号

在 normal 和 accelerator 模式仿真中，Record 模块支持记录无界可变大小信号，但不支持可视化无界可变大小信号。对于包含无界可变大小信号的 nonvirtual 总线，不支持记录。

### R2023a：记录包含可变大小信号的非虚拟总线

在 normal 和 accelerator 模式仿真中，Record 模块支持记录：

- 直接包含可变大小信号或在嵌套总线中包含可变大小信号的非虚拟总线
- 具有包含可变大小信号的嵌套非虚拟总线的总线

仅在 normal 模式仿真中，Record 模块支持记录：

- 具有包含可变大小信号的非虚拟总线的总线数组

Record 模块不支持可视化可变大小信号。

### R2022b：缩放单个信号

可以为 Record 模块中的单个信号设置显示比例和偏移量。

- 时间图和迷你图 — 缩放和偏移 *y* 值的显示。
- XY 图 — 独立缩放和偏移 *x* 值和 *y* 值的显示。
- 地图 — 独立缩放和偏移经度和纬度。

光标继续显示未缩放的值。

### R2021b：XY Graph 模块替换为 Record 模块的替代配置

XY Graph 模块替换为预配置为在 XY 图上显示两个输入信号的 Record 模块。使用更新后的 XY Graph 模块，可以：

- 在仿真期间查看 XY 图上的数据。
- 将 XY 图数据记录到工作区、文件，或工作区和文件。
- 无需再次仿真即可缩放、平移、适应视图以及调整 XY 图的坐标轴范围。
- 通过使用光标和添加趋势线来分析 XY 迹线。
- 添加其他端口和子图，以在若干可视化类型（包括时间图、地图或其他 XY 图）中随 XY 图一起可视化其他仿真数据。
- 在 XY 图上可视化多条迹线。

仿真时，之前版本的 XY Graph 模块会打开一个新窗口，以在仿真期间显示连接的信号数据。要查看更新后的 XY Graph 模块上的数据，请在模型中双击该模块。要在新窗口中查看 XY 图，请右键单击该模块，然后选择 **在新窗口中打开**。

现有模型中的 XY Graph 模块会自动替换为新的 XY Graph 模块。XY Graph 查看器也会替换为新的 XY Graph 模块。Goto 和 From 模块将信号连接到替换 XY Graph 查看器的 XY Graph 模块。

连接到 XY Graph 模块的信号始终流式传输到 Simulation Data Inspector。

### R2021a：**日志记录间隔**配置参数适用于使用 Record 模块记录到工作区的数据

**日志记录间隔**配置参数适用于使用 Record 模块记录到工作区的数据。

**日志记录间隔**参数不会影响使用 Record 模块记录到文件的数据，也不会影响信号在 Record 模块中的显示方式。还可以在 Simulation Data Inspector 中访问连接到 Record 模块的信号的完整信号数据。

## 描述

查看数据并将数据记录到工作区、文件或两者

使用 Record 模块或 XY Graph 模块将数据记录到工作区、文件，或同时记录到工作区和文件。将数据记录到文件时，可以选择记录到 MAT 文件、MLDATX 文件、Excel® 文件或 Parquet 文件 *(自 R2025a 起)*。连接到 Record 模块的信号始终记录到 Simulation Data Inspector。如果确定需要在仿真后保存数据，可以将数据从 Record 模块导出到工作区或除 Parquet 文件之外的任何受支持文件类型。

还可以使用 Record 模块可视化连接的信号。要查看连接到 Record 模块的信号的数据，请双击该模块。在 Record 模块中查看数据时，可以访问仿真控件，例如 **运行** 按钮。

默认情况下，Record 模块在迷你图上显示所有连接的信号。为每个连接的信号添加一个迷你图。当迷你图填满可见空间后，滚动条允许继续绘制信号。

打开以查看由 Record 模块记录的数据的模型，其模块参数在属性检查器中可见

### 构建可视化

Record 模块支持 Simulation Data Inspector 中可用的大多数可视化。当其他可视化更适合你的数据时，可以使用 **布局** 选项和绘图类型选择器（默认标记为 **迷你图**）修改绘图布局和绘图类型。使用 **布局** 列表选择子图布局。要更改子图的绘图类型，请选择该子图，然后从绘图类型选择器中选择所需的绘图类型。

有关更多信息，请参阅使用 Record 模块将数据记录到工作区和文件。有关展示如何使用每种可视化类型的示例，请参阅：

- 迷你图 — 使用迷你图一起查看多个信号
- XY — 在 XY 图上可视化仿真数据并使用 XY 图分析数据
- 地图 — 查看和回放地图数据
- 时间图和文本编辑器 — 使用 Simulation Data Inspector 创建绘图
