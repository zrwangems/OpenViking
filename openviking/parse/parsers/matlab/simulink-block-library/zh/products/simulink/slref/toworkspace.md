---
type: simulink-block
title: 'To Workspace'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sinks'
documentation_page: 'toworkspace'
documentation_source_path: 'slref/toworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# To Workspace

## 端口

### 输入

### **Port\_1** — 要记录到工作区的数据 scalar | vector | matrix | array | bus

接收要记录到工作区的数据的输入端口。To Workspace 模块支持记录任意内置数据类型或用户定义数据类型（例如 bus、枚举和定点数据）的实数和复数数据。

#### 提示

记录定点数据需要 Fixed-Point Designer™ 许可证。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**复数支持：** Yes

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **Property Inspector**。

### **变量名称** — 保存数据的变量名称 `simout`（默认） | string | character vector

为包含已记录数据的变量指定名称。默认情况下，To Workspace 模块将已记录数据保存在名为 `simout` 的变量中。当模型包含多个 To Workspace 模块时，每个模块的 **变量名称** 参数值必须唯一。

有关命名 MATLAB® 变量的信息，请参阅 Variable Names。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariableName` |
| **值：** | `"simout"`（默认） | 有效的 MATLAB 变量名称 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"VariableName","myName")`

### **将数据点限制为最后** — 要记录的样本数 `inf`（默认） | scalar | vector

当只想保存或分析仿真末尾的数据时，请将要记录的样本数指定为大于零的正整数。默认情况下，To Workspace 模块记录整个仿真的数据，**将数据点限制为最后** 参数的值为 `inf`。

将已记录数据限制为最后 *n* 个信号值会直接影响内存分配。指定此参数时，软件会根据指定的值预先分配内存，而不是根据仿真期间生成的时间步来分配。因此，当记录数量不确定的时间步时，不建议使用 **将数据点限制为最后** 参数。

有关控制仿真期间记录哪些样本的详细信息，请参阅 Specify Signal Values to Log。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDataPoints` |
| **值：** | `"inf"`（默认） | positive integer |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"MaxDataPoints","20")`

### **抽取** — 抽取因子 `1`（默认） | positive integer

指定抽取因子以降低已记录数据的有效采样率。对于抽取因子 *n*，To Workspace 模块记录每第 *n* 个样本值。例如，当将 **抽取** 值指定为 `2` 时，To Workspace 模块每隔一个数据点记录一次。

有关控制仿真期间记录哪些样本的详细信息，请参阅 Specify Signal Values to Log。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Decimation` |
| **值：** | `"1"`（默认） | positive integer |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"Decimation","2")`

### **保存格式** — 记录到工作区的数据格式 `Timeseries`（默认） | `Structure With Time` | `Structure` | `Array`

指定记录到工作区的数据格式。要记录 bus 或 bus 数组输入的数据，请使用 `Timeseries` 格式。

| **保存格式** 值 | 工作区数据格式 | 仿真工作流支持 |
| --- | --- | --- |
| `Timeseries` | 非 bus 输入记录为 `timeseries` 对象。  bus 输入记录为 `timeseries` 对象的结构体。该结构体中字段的层次结构和名称与定义该 bus 的 `Simulink.Bus` 对象中指定的层次结构和名称匹配。  bus 数组输入记录为 `timeseries` 对象的结构体数组。 | 支持：  - 普通模式仿真 - 加速器模式仿真 - 快速加速器模式仿真 *（自 R2022a 起）* - 使用 XCP 通信的外部模式仿真，前提是将 `StreamToWks` 设置为 `'on'` 且将 `MATFileLogging` 设置为 `'off'`    不支持：  - 使用 TCP/IP 或串行通信的外部模式仿真 - 软件在环 (SIL) 仿真 - 处理器在环 (PIL) 仿真 - 为 Simulink Coder™ 目标生成代码 |
| `Structure With Time` | 非 bus 输入记录为包含以下字段的结构体：  - `time` — 记录输入值时的仿真时间点的列向量。 - `signals` — 包含样本值的结构体，其中包含以下字段：  - `values` — 样本值数组。   - `dimensions` — 样本维度。   - `label` — 模型中信号线的名称。 - `blockName` — To Workspace 模块的名称。 | 始终支持：  - 普通模式仿真。 - 使用 XCP 通信的外部模式仿真，前提是将 `StreamToWks` 设置为 `'on'` 且将 `MATFileLogging` 设置为 `'off'`    支持，但 To Workspace 模块位于被引用模型中时除外：  - 加速器模式仿真 - 快速加速器模式仿真 - 使用 TCP/IP 或串行通信的外部模式仿真    如果为生成的代码启用了 **MAT-file logging (Simulink Coder)**，则支持，但 To Workspace 模块位于被引用模型中时除外：  - 软件在环 (SIL) 仿真 - 处理器在环 (PIL) 仿真 - 为 Simulink Coder 目标生成代码 |
| `Structure` | 非 bus 输入记录为与 `Structure With Time` 格式匹配的结构体，但该结构体的 `time` 字段为空。 |
| `Array` | 非 bus 输入的样本值保存为 *N* 维数组，其中 *N* 比输入的维度大一。例如：  - 标量信号数据记录为列向量。 - 向量信号数据记录为矩阵。 - 矩阵信号数据记录为 3-D 数组。    数组中值的结构取决于输入信号数据的维度：  - 对于标量和向量信号，每个样本值是输出数组中的一行。数组的第一维与时间对齐，因此 `simout(1,:)` 返回第一个记录的信号值。 - 对于矩阵信号，输出数组的第三维与时间对齐，因此 `simout(:,:,1)` 返回第一个记录的信号值。 - 对于 *N* 维信号，最后一维与时间对齐，因此最后一维中的元素数等于从仿真记录的样本数。    输出数组仅包含信号值，不包含时间数据。 |

#### 提示

- 要将数据记录为基于帧而不是基于样本：

  - 将 **保存格式** 参数配置为使用 `Structure` 格式或 `Array` 格式记录数据。
  - 将 **将 2-D 信号保存为** 参数指定为 `2-D array (concatenate along first dimension)`
- 当想要使用 From Workspace 模块加载已记录数据时，请考虑使用 `Timeseries` 或 `Structure With Time` 格式。使用 `Array` 格式记录数据时，需要在加载数据之前将采样时间值合并到数组中。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaveFormat` |
| **值：** | `"Timeseries"`（默认） | `"Structure with Time"` | `"Structure"` | `"Array"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"SaveFormat","Structure")`

### **将 2-D 信号保存为** — 已记录数据中 2-D 样本值的排列 `3-D array (concatenate along third dimension)`（默认） | `2-D array (concatenate along first dimension)`

指定是将 2-D 输入数据记录为 3-D 数组还是 2-D 数组。

记录为 3-D 数组非常适合基于样本的输入数据。样本沿第三维串联，从而可以轻松访问 2 维样本数据。

记录为 2-D 数组非常适合基于帧的输入数据。样本沿第一维串联，这实际上从第一维中移除了帧缓冲。

| 输入数据维度 | 将 2-D 信号保存为... | 工作区数据维度 |
| --- | --- | --- |
| *M*-by-*N* | `2-D array (concatenate along first dimension)` | *K*-by-*N* 矩阵，其中 *K* 等于 *M* 乘以从仿真记录的样本数。例如，记录 `2`-by-`4` 矩阵输入的十个样本会创建 `20`-by-`4` 矩阵。 |
| `3-D array (concatenate along first dimension)` | *M*-by-*N*-by-*K* 数组，其中 *K* 等于从仿真记录的样本数。例如，记录 `2`-by-`4` 矩阵输入的十个样本会创建 `2`-by-`4`-by-`10` 数组。 |

#### 依赖关系

要启用此参数，请将 **保存格式** 设置为 `Array` 或 `Structure`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Save2DSignal` |
| **值：** | `"3-D array (concatenate along third dimension)"`（默认） | `"2-D array (concatenate along first dimension)"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"Save2DSignal","2-D array (concatenate along first dimension)")`

### **将定点数据记录为 fi 对象** — 已记录定点数据的数据类型 `on`（默认） | `off`

指定如何记录定点输入数据。

当 **保存格式** 参数指定为 `Timeseries` 时，To Workspace 模块始终将定点输入数据记录为 `fi` (Fixed-Point Designer) 对象。当 **保存格式** 参数未指定为 `Timeseries` 时，要将定点数据记录为 `fi` 对象，请选择 **将定点数据记录为 fi 对象** 参数，并在普通或加速器模式下运行仿真。

当清除 **将定点数据记录为 fi 对象** 参数或在快速加速器模式下运行仿真时，定点输入数据记录为 `double`。

要将 `int64` 类型的输入数据记录为 `int64` 或将 `uint64` 类型的输入数据记录为 `uint64`，请选择 **将定点数据记录为 fi 对象** 参数。当清除 **将定点数据记录为 fi 对象** 参数时，`int64` 或 `uint64` 类型的输入数据记录为 `double`。

使用 To Workspace 模块记录定点数据需要 Fixed-Point Designer 许可证。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FixptAsFi` |
| **值：** | `"on"`（默认） | `"off"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"FixptAtFi","off")`

### **采样时间** — 采样间隔和可选时间偏移 -1（默认） | scalar

指定模块在仿真期间记录输入值的时间。默认情况下，采样时间是继承的 (`-1`)。对于连续采样时间，请将该值指定为 `0`。要使用离散采样时间，请将 **采样时间** 参数指定为标量。有关详细信息，请参阅 Specify Sample Time。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | scalar |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"SampleTime","0")`

## 所属库

Simulink / Sinks DSP System Toolbox / Sinks HDL Coder / Sinks

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

不建议用于生产代码。

要生成将 To Workspace 模块的输入记录到 MAT 文件的代码，请启用 **MAT-file logging** 参数。有关详细信息，请参阅 **MAT-file logging (Simulink Coder)**。

不支持为以下项生成代码：

- String 数据类型。
- 被引用模型内的模块。
- 使用 `Timeseries` 格式记录数据的模块。有关详细信息，请参阅 **保存格式**。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2025a：记录 `datetime` 数据

To Workspace 模块支持记录 `datetime` 数据。

### R2023b：记录无界可变大小信号

在普通和加速器模式仿真中，可以使用 To Workspace 模块记录无界可变大小信号。不支持记录包含无界可变大小信号的 nonvirtual bus。

### R2023a：记录包含可变大小信号的 nonvirtual bus

在普通和加速器模式仿真中，To Workspace 模块支持记录：

- 直接包含可变大小信号或在嵌套 bus 中包含可变大小信号的 nonvirtual bus
- 带有包含可变大小信号的嵌套 nonvirtual bus 的 bus

仅在普通模式仿真中，To Workspace 模块支持记录：

- 带有包含可变大小信号的 nonvirtual bus 的 bus 数组

### R2022a：将数据记录到仿真数据检查器以及工作区

数据会自动记录到仿真数据检查器以及工作区。仿真数据检查器会自动保留每次仿真的结果。由于使用 To Workspace 模块记录的数据会流式传输到仿真数据检查器，因此该数据也会被保留。

在以前的版本中，使用 To Workspace 模块记录的数据仅记录到工作区，并且每次仿真时都会被覆盖，除非您更改记录变量名称或手动保存结果。

在大多数情况下，您无需对代码进行任何更改。记录大量数据或运行多次仿真可能会产生大量数据，从而占满磁盘空间。要了解如何控制仿真数据检查器中保留的数据量，请参阅 Limit the Size of Logged Data。

### R2022a：使用内置数据类型记录 `int64` 和 `uint64` 数据

使用内置数据类型记录 `int64` 和 `uint64` 数据。

在以前的版本中，当有 Fixed-Point Designer 许可证时，To Workspace 模块将 `int64` 和 `uint64` 数据记录为 `fi` 对象；当没有许可证时，记录为 `double`。

### R2022a：记录具有 `string` 和 `half` 数据类型的信号

To Workspace 模块支持记录具有 `string` 和 `half` 数据类型的信号。

### R2022a：记录 bus 数组

To Workspace 模块支持记录 bus 数组。

### R2022a：在快速加速器仿真中使用 `Timeseries` 格式记录数据

以前，只能使用普通模式仿真或加速器模式仿真以 `Timeseries` 格式记录数据。

### R2022a：为 for-each 子系统内的 To Workspace 模块使用 `Timeseries` 格式记录数据

可以使用 `Timeseries` 格式在 for-each 子系统内的 To Workspace 模块中记录数据。

## 描述

从 Simulink 模型将数据记录到工作区

To Workspace 模块将连接到其输入端口的数据从 Simulink® 模型记录到工作区。通常，已记录数据会返回到基础工作区。当您在函数内以编程方式仿真模型时，已记录数据会返回到该函数的工作区。在仿真期间，已记录数据会流式传输到仿真数据检查器。当仿真暂停或停止时，已记录数据会写入工作区。

您可以使用 To Workspace 模块记录信号、bus 或 bus 数组的数据。To Workspace 模块支持记录标量和多维数据，包括可变大小信号的数据。

您可以配置存储 To Workspace 模块所记录数据的变量名称，并可以指定已记录数据的格式。您还可以通过指定模块或模型参数来控制 To Workspace 模块记录哪些值。有关详细信息，请参阅 Specify Signal Values to Log。

### 访问已记录数据

仿真结果返回到工作区的方式取决于您如何仿真和配置模型。在以下任一情况下，仿真结果会返回到单个 `Simulink.SimulationOutput` 对象中：

- 您启用 **单一仿真输出** 参数。

  默认情况下，创建新模型时会启用 **单一仿真输出** 参数。您可以使用配置参数对话框启用该参数。在 **建模** 选项卡上的 **设置** 下，点击 **模型设置**。然后，在配置参数对话框中，选择 **数据导入/导出** 并选择 **单一仿真输出**。
- 您使用多个仿真窗格运行一组仿真。
- 您使用一个或多个 `Simulink.SimulationInput` 对象以编程方式仿真模型。

  当您使用 `sim`、`parsim` 和 `batchsim` 函数运行仿真时，可以使用 `SimulationInput` 对象配置仿真。
- 您使用将结果作为单个仿真输出返回的 `sim` 函数语法来仿真模型。

  有关详细信息，请参阅 `sim`。

当仿真结果在单个输出中返回时，`SimulationOutput` 对象会为模型中的每个 To Workspace 模块包含一个变量。要访问 To Workspace 模块记录的数据：

- 使用点号加上使用模块的 **变量名称** 参数指定的变量名称。默认情况下，模型配置为使用变量名称 `out` 返回单个仿真输出，并且 To Workspace 模块将数据保存到名为 `simout` 的变量中。

  ```
  toWksData = out.simout;
  ```
- 将 `get` 函数与包含已记录数据的变量名称一起使用。

  ```
  toWksData = get(out,simout);
  ```

在模型中，To Workspace 模块指示如何在工作区中访问数据。默认情况下，模块显示 `out.simout`。当您执行以下操作时，模块外观会更新：

- 在模块上为 **变量名称** 参数指定不同的值。
- 为单个仿真输出指定不同的变量名称。
- 清除 **单一仿真输出** 配置参数。
