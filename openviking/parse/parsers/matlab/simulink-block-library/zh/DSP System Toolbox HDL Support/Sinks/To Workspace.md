---
type: simulink-block
title: 'To Workspace'
family: 'hdlcoder'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'toworkspace'
documentation_source_path: '../simulink/slref/toworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# To Workspace

## 端口

### 输入

### **Port\_1** — 要记录到工作区的数据 标量 | 向量 | 矩阵 | 数组 | 总线

接收要记录到工作区的数据的输入端口。To Workspace 模块支持记录任何内置数据类型或用户定义数据类型（如总线、枚举和定点数据）的实数和复数数据。

#### 提示

记录定点数据需要 Fixed-Point Designer™ 许可证。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **Variable name** — 保存数据的变量名称 `simout`（默认）| 字符串 | 字符向量

指定包含所记录数据的变量的名称。默认情况下，To Workspace 模块将记录的数据保存在名为 `simout` 的变量中。当模型包含多个 To Workspace 模块时，每个模块的 **Variable name** 参数值必须唯一。

有关 MATLAB® 变量命名的信息，请参阅变量名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VariableName` |
| **值：** | `"simout"`（默认）| 有效的 MATLAB 变量名 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"VariableName","myName")`

### **Limit data points to last** — 要记录的样本数 `inf`（默认）| 标量 | 向量

当您只想保存或分析仿真结束时的数据时，请将要记录的样本数指定为大于零的正整数。默认情况下，To Workspace 模块记录整个仿真的数据，**Limit data points to last** 参数的值为 `inf`。

将记录的数据限制为最后 *n* 个信号值会直接影响内存分配。当您指定此参数时，软件会根据指定的值预先分配内存，而不是根据仿真期间生成的时间步长。因此，在记录不确定数量的时间步长时，不建议使用 **Limit data points to last** 参数。

有关控制仿真期间记录哪些样本的详细信息，请参阅指定要记录的信号值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDataPoints` |
| **值：** | `"inf"`（默认）| 正整数 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"MaxDataPoints","20")`

### **Decimation** — 抽取因子 `1`（默认）| 正整数

指定抽取因子以降低所记录数据的有效采样率。对于抽取因子 *n*，To Workspace 模块记录每第 *n* 个样本值。例如，当您将 **Decimation** 值指定为 `2` 时，To Workspace 模块记录每隔一个数据点。

有关控制仿真期间记录哪些样本的详细信息，请参阅指定要记录的信号值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Decimation` |
| **值：** | `"1"`（默认）| 正整数 |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"Decimation","2")`

### **Save format** — 记录到工作区的数据格式 `Timeseries`（默认）| `Structure With Time` | `Structure` | `Array`

指定记录到工作区的数据的格式。要记录总线或总线数组输入的数据，请使用 `Timeseries` 格式。

| **Save Format** 值 | 工作区数据格式 | 仿真工作流支持 |
| --- | --- | --- |
| `Timeseries` | 非总线输入记录为 `timeseries` 对象。总线输入记录为 `timeseries` 对象的结构体。结构体中字段的层次结构和名称与定义总线的 `Simulink.Bus` 对象中指定的层次结构和名称匹配。总线数组输入记录为 `timeseries` 对象的结构体数组。 | 支持：- 普通模式仿真- 加速器模式仿真- 快速加速器模式仿真*（自 R2022a 起）*- 使用 XCP 通信的外部模式仿真，前提是 `StreamToWks` 设置为 `'on'` 且 `MATFileLogging` 设置为 `'off'`不支持：- 使用 TCP/IP 或串行通信的外部模式仿真- 软件在环（SIL）仿真- 处理器在环（PIL）仿真- Simulink Coder™ 目标的代码生成 |
| `Structure With Time` | 非总线输入记录为包含以下字段的结构体：- `time` — 记录输入值的仿真时间命中点的列向量。- `signals` — 包含样本值的结构体，包含以下字段：- `values` — 样本值的数组。- `dimensions` — 样本维度。- `label` — 模型中信号线的名称。- `blockName` — To Workspace 模块的名称。 | 始终支持：- 普通模式仿真。- 使用 XCP 通信的外部模式仿真，前提是 `StreamToWks` 设置为 `'on'` 且 `MATFileLogging` 设置为 `'off'`除 To Workspace 模块位于被引用模型中之外，支持：- 加速器模式仿真- 快速加速器模式仿真- 使用 TCP/IP 或串行通信的外部模式仿真如果为生成的代码启用了 **MAT-file logging (Simulink Coder)**，则支持（To Workspace 模块位于被引用模型中时除外）：- 软件在环（SIL）仿真- 处理器在环（PIL）仿真- Simulink Coder 目标的代码生成 |
| `Structure` | 非总线输入记录为与 `Structure With Time` 格式匹配的结构体，但结构体的 `time` 字段为空。 |
| `Array` | 非总线输入的样本值保存为 *N* 维数组，其中 *N* 比输入的维度大一。例如：- 标量信号数据记录为列向量。- 向量信号数据记录为矩阵。- 矩阵信号数据记录为三维数组。数组中值的结构取决于输入信号数据的维度：- 对于标量和向量信号，每个样本值是输出数组中的一行。数组的第一个维度与时间对齐，使得 `simout(1,:)` 返回第一个记录的信号值。- 对于矩阵信号，输出数组的第三个维度与时间对齐，使得 `simout(:,:,1)` 返回第一个记录的信号值。- 对于 *N* 维信号，最后一个维度与时间对齐，使得最后一个维度中的元素数等于从仿真中记录的样本数。输出数组仅包含信号值，不包含时间数据。 |

#### 提示

- 要以基于帧而非基于样本的方式记录数据：

  - 将 **Save format** 参数配置为使用 `Structure` 格式或 `Array` 格式记录数据。
  - 将 **Save 2-D signals as** 参数指定为 `2-D array (concatenate along first dimension)`
- 当您想要使用 From Workspace 模块加载所记录的数据时，请考虑使用 `Timeseries` 或 `Structure With Time` 格式。当您使用 `Array` 格式记录数据时，需要在加载数据之前将采样时间值合并到数组中。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaveFormat` |
| **值：** | `"Timeseries"`（默认）| `"Structure with Time"` | `"Structure"` | `"Array"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"SaveFormat","Structure")`

### **Save 2-D signals as** — 所记录数据中二维样本值的排列方式 `3-D array (concatenate along third dimension)`（默认）| `2-D array (concatenate along first dimension)`

指定将二维输入数据记录为三维数组还是二维数组。

记录为三维数组非常适合基于样本的输入数据。样本沿第三个维度串联，便于访问二维样本数据。

记录为二维数组非常适合基于帧的输入数据。样本沿第一个维度串联，这实际上从第一个维度中移除了帧缓冲。

| 输入数据维度 | Save 2-D Signal As... | 工作区数据维度 |
| --- | --- | --- |
| *M*×*N* | `2-D array (concatenate along first dimension)` | *K*×*N* 矩阵，其中 *K* 等于 *M* 乘以从仿真中记录的样本数。例如，记录 `2`×`4` 矩阵输入的十个样本会创建一个 `20`×`4` 矩阵。 |
| `3-D array (concatenate along first dimension)` | *M*×*N*×*K* 数组，其中 *K* 等于从仿真中记录的样本数。例如，记录 `2`×`4` 矩阵输入的十个样本会创建一个 `2`×`4`×`10` 数组。 |

#### 依赖关系

要启用此参数，请将 **Save format** 设置为 `Array` 或 `Structure`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Save2DSignal` |
| **值：** | `"3-D array (concatenate along third dimension)"`（默认）| `"2-D array (concatenate along first dimension)"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"Save2DSignal","2-D array (concatenate along first dimension)")`

### **Log fixed-point data as a fi object** — 所记录定点数据的数据类型 `on`（默认）| `off`

指定如何记录定点输入数据。

当 **Save format** 参数指定为 `Timeseries` 时，To Workspace 模块始终将定点输入数据记录为 `fi`（Fixed-Point Designer）对象。当 **Save format** 参数未指定为 `Timeseries` 时，要将定点数据记录为 `fi` 对象，请选择 **Log fixed-point data as a fi object** 参数并在普通或加速器模式下运行仿真。

当您清除 **Log fixed-point data as a fi object** 参数或在快速加速器模式下运行仿真时，定点输入数据记录为 `double`。

要将 `int64` 类型的输入数据记录为 `int64` 或将 `uint64` 类型记录为 `uint64`，请选择 **Log fixed-point data as a fi object** 参数。当您清除 **Log fixed-point data as a fi object** 参数时，`int64` 或 `uint64` 类型的输入数据记录为 `double`。

使用 To Workspace 模块记录定点数据需要 Fixed-Point Designer 许可证。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FixptAsFi` |
| **值：** | `"on"`（默认）| `"off"` |
| **数据类型：** | `character vector` | `string` |

**示例：** `set_param(gcb,"FixptAtFi","off")`

### **Sample time** — 采样间隔和可选时间偏移 -1（默认）| 标量

指定模块在仿真期间记录输入值的时间。默认情况下，采样时间继承（`-1`）。对于连续采样时间，将值指定为 `0`。要使用离散采样时间，请将 **Sample time** 参数指定为标量。有关详细信息，请参阅指定采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 标量 |
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

以下情况不支持代码生成：

- 字符串数据类型。
- 被引用模型内的模块。
- 使用 `Timeseries` 格式记录数据的模块。有关详细信息，请参阅 **Save format**。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

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

在普通和加速器模式仿真中，您可以使用 To Workspace 模块记录无界可变大小信号。不支持记录包含无界可变大小信号的非虚拟总线。

### R2023a：记录包含可变大小信号的非虚拟总线

在普通和加速器模式仿真中，To Workspace 模块支持记录：

- 直接或嵌套总线中包含可变大小信号的非虚拟总线
- 包含可变大小信号的嵌套非虚拟总线的总线

仅在普通模式仿真中，To Workspace 模块支持记录：

- 包含可变大小信号的非虚拟总线的总线数组

### R2022a：将数据记录到仿真数据检查器以及工作区

数据会自动记录到仿真数据检查器以及工作区。仿真数据检查器自动保留每次仿真的结果。由于使用 To Workspace 模块记录的数据会流式传输到仿真数据检查器，因此该数据也会被保留。

在以前的版本中，使用 To Workspace 模块记录的数据仅记录到工作区，并且每次仿真都会被覆盖，除非您更改记录变量名称或手动保存结果。

在大多数情况下，您无需对代码进行任何更改。记录大量数据或运行多次仿真可能会产生大量数据，从而占满磁盘空间。要了解如何控制仿真数据检查器中保留的数据量，请参阅限制记录数据的大小。

### R2022a：使用内置数据类型记录 `int64` 和 `uint64` 数据

使用内置数据类型记录 `int64` 和 `uint64` 数据。

在以前的版本中，当有 Fixed-Point Designer 许可证时，To Workspace 模块将 `int64` 和 `uint64` 数据记录为 `fi` 对象；当没有许可证时，记录为 `double`。

### R2022a：记录具有 `string` 和 `half` 数据类型的信号

To Workspace 模块支持记录具有 `string` 和 `half` 数据类型的信号。

### R2022a：记录总线数组

To Workspace 模块支持记录总线数组。

### R2022a: 在快速加速仿真中使用 `Timeseries` 格式记录数据

以前，只能使用普通模式仿真或加速器模式仿真来以 `Timeseries` 格式记录数据。

### R2022a: 在 for-each 子系统内的 To Workspace 模块中使用 `Timeseries` 格式记录数据

您可以使用 `Timeseries` 格式在 for-each 子系统内的 To Workspace 模块中记录数据。

## 描述

将 Simulink 模型中的数据记录到工作区

To Workspace 模块将其输入端口连接的数据记录到 Simulink® 模型的工作区。通常，记录的数据返回到基础工作区。当您在函数内以编程方式仿真模型时，记录的数据返回到该函数的工作区。在仿真期间，记录的数据流式传输到仿真数据检查器。当仿真暂停或停止时，记录的数据写入工作区。

您可以使用 To Workspace 模块记录信号、总线或总线数组的数据。To Workspace 模块支持记录标量和多维数据，包括可变大小信号的数据。

您可以配置存储 To Workspace 模块所记录数据的变量名称，并可以指定记录数据的格式。您还可以通过指定模块或模型参数来控制 To Workspace 模块记录哪些值。有关详细信息，请参阅指定要记录的信号值。

### 访问记录的数据

仿真结果如何返回到工作区取决于您如何仿真和配置模型。在以下任一情况下，仿真结果将返回到单个 `Simulink.SimulationOutput` 对象中：

- 您启用 **Single simulation output** 参数。

  默认情况下，当您创建新模型时，**Single simulation output** 参数处于启用状态。您可以使用配置参数对话框启用该参数。在 **Modeling** 选项卡的 **Settings** 下，点击 **Model Settings**。然后，在配置参数对话框中，选择 **Data Import/Export** 并选择 **Single simulation output**。
- 您使用 Multiple Simulations 窗格运行一组仿真。
- 您使用一个或多个 `Simulink.SimulationInput` 对象以编程方式仿真模型。

  当您使用 `sim`、`parsim` 和 `batchsim` 函数运行仿真时，可以使用 `SimulationInput` 对象配置仿真。
- 您使用将结果作为单个仿真输出返回的 `sim` 函数语法来仿真模型。

  有关详细信息，请参阅 `sim`。

当仿真结果以单个输出返回时，`SimulationOutput` 对象包含模型中每个 To Workspace 模块对应的变量。要访问 To Workspace 模块记录的数据：

- 使用点号加上通过模块的 **Variable name** 参数指定的变量名。默认情况下，模型配置为使用变量名 `out` 返回单个仿真输出，并且 To Workspace 模块将数据保存到名为 `simout` 的变量中。

  ```
  toWksData = out.simout;
  ```
- 使用 `get` 函数加上包含记录数据的变量名。

  ```
  toWksData = get(out,simout);
  ```

在模型中，To Workspace 模块指示如何访问工作区中的数据。默认情况下，该模块显示 `out.simout`。当您进行以下操作时，模块外观会更新：

- 为模块上的 **Variable name** 参数指定不同的值。
- 为单个仿真输出指定不同的变量名。
- 清除 **Single simulation output** 配置参数。
