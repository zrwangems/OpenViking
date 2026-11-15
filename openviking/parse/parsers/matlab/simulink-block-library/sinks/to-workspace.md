---
type: simulink-block
title: 'To Workspace'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'toworkspace'
---

# To Workspace

Log data to workspace from Simulink model

## 中文

将数据从 Simulink 模型记录到工作区

### 所属库

Simulink / Sinks DSP System Toolbox / Sinks HDL Coder / Sinks

### 描述

To Workspace 模块将连接到其输入端口的数据从 Simulink® 模型记录到工作区。通常，记录的数据在基础工作区中返回。当您以编程方式在函数中仿真模型时，记录的数据将返回到函数的工作区中。在仿真期间，记录的数据会流式传输到仿真数据检查器。当仿真暂停或停止时，记录的数据会写入工作区。

您可以使用 To Workspace 模块记录信号、总线或总线数组的数据。To Workspace 模块支持记录标量和多维数据，包括可变大小信号的数据。

您可以配置存储 To Workspace 模块所记录数据的变量的名称，还可以指定所记录数据的格式。您还可以通过指定模块或模型参数来控制 To Workspace 模块记录的值。有关详细信息，请参阅Specify Signal Values to Log。

#### 访问记录的数据

仿真结果如何返回到工作区取决于您如何仿真和配置模型。在以下任何情况下，仿真结果都以单个 `Simulink.SimulationOutput` 对象形式返回：

- 启用**单一仿真输出**参数。

  默认情况下，创建新模型时，**单一仿真输出**参数处于启用状态。您可以使用“配置参数”对话框来启用该参数。在**建模**选项卡上的**设置**下，点击**模型设置**。然后，在“配置参数”对话框中，选择**数据导入/导出**，并选择**单一仿真输出**。
- 您可以使用多个仿真窗格运行一组仿真。
- 您可以使用一个或多个 `Simulink.SimulationInput` 对象以编程方式对模型进行仿真。

  使用 `sim`、`parsim` 和 `batchsim` 函数运行仿真时，您可以使用 `SimulationInput` 对象配置仿真。
- 使用 `sim` 函数语法仿真模型，该语法将结果以单个仿真输出形式返回。

  有关详细信息，请参阅 `sim`。

当仿真结果在单个输出中返回时，对于模型中的每个 To Workspace 模块，`SimulationOutput` 对象都包含一个对应的变量。要访问 To Workspace 模块记录的数据，请执行以下操作：

- 使用一个圆点，后跟使用模块的**变量名称**参数指定的变量名称。默认情况下，模型配置为使用变量名称 `out` 返回单个仿真输出，To Workspace 模块会将数据保存到名为 `simout` 的变量中。

  ```
  toWksData = out.simout;
  ```
- 使用 `get` 函数和包含所记录数据的变量的名称。

  ```
  toWksData = get(out,simout);
  ```

在模型中，To Workspace 模块指示如何访问工作区中的数据。默认情况下，该模块显示 `out.simout`。当您执行以下操作时，模块外观会更新：

- 为模块中的**变量名称**参数指定不同的值。
- 为单个仿真输出指定不同的变量名称。
- 清除**单一仿真输出**配置参数。

### 端口

#### 输入

#### **Port\_1** — 要记录到工作区的数据 标量 | 向量 | 矩阵 | 数组 | 总线

接收数据以记录到工作区的输入端口。To Workspace 模块支持记录任何内置数据类型或用户定义数据类型的实数和复数数据，如总线、枚举和定点数据。

##### 提示

记录定点数据需要 Fixed-Point Designer™ 许可证。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**复数支持:** 是

### 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

#### **变量名称** — 用于保存数据的变量的名称 `simout` (默认) | 字符串 | 字符向量

为包含所记录数据的变量指定名称。默认情况下，To Workspace 模块将记录的数据保存在名为 `simout` 的变量中。当一个模型包含多个 To Workspace 模块时，每个模块的**变量名称**参数值必须是唯一的。

有关命名 MATLAB® 变量的信息，请参阅变量名称。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VariableName` |
| **值:** | `"simout"` (默认) | valid MATLAB variable name |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"VariableName","myName")`

#### **将数据点限制为最后** — 要记录的采样数 `inf` (默认) | 标量 | 向量

如果只想保存或分析仿真结束时的数据，请将要记录的采样数指定为大于零的正整数。默认情况下，To Workspace 模块记录整个仿真的数据，并且**将数据点限制为最后**参数的值为 `inf`。

将记录的数据限制为最后 *n* 个信号值会直接影响内存分配。指定此参数时，软件会根据指定的值（而不是根据在仿真期间生成的时间步）预分配内存。因此，当记录不确定数量的时间步时，不推荐使用**将数据点限制为最后**参数。

有关控制在仿真期间记录哪些采样的详细信息，请参阅Specify Signal Values to Log。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `MaxDataPoints` |
| **值:** | `"inf"` (默认) | positive integer |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"MaxDataPoints","20")`

#### **抽取** — 抽取因子 `1` (默认) | 正整数

指定抽取因子以降低记录数据的有效采样率。对于抽取因子 *n*，To Workspace 模块记录每第 *n* 个采样值。例如，当**抽取**值指定为 `2` 时，To Workspace 模块每隔一个数据点记录一个采样。

有关控制在仿真期间记录哪些采样的详细信息，请参阅Specify Signal Values to Log。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Decimation` |
| **值:** | `"1"` (默认) | positive integer |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"Decimation","2")`

#### **保存格式** — 记录到工作区的数据的格式 **时间序列** (默认) | **带时间的结构体** | **结构体** | **数组**

指定记录到工作区的数据的格式。要记录总线或总线数组输入的数据，请使用**时间序列**格式。

| **保存格式**值 | 工作区数据格式 | 仿真工作流支持 |
| --- | --- | --- |
| **时间序列** | 非总线输入记录为 `timeseries` 对象。  总线输入记录为由 `timeseries` 对象组成的结构体。结构体中字段的层次结构和名称与在定义总线的 `Simulink.Bus` 对象中指定的层次结构和名称匹配。  总线数组输入记录为由 `timeseries` 对象组成的结构体数组。 | 支持：  - 普通模式仿真 - 加速模式仿真 - 快速加速模式仿真 *(自 R2022a 起)* - 使用 XCP 通信的外部模式仿真（如果 `StreamToWks` 设置为 `'on'` 并且 `MATFileLogging` 设置为 `'off'`）    不支持：  - 使用 TCP/IP 或串行通信的外部模式仿真 - 软件在环 (SIL) 仿真 - 处理器在环 (PIL) 仿真 - Simulink Coder™ 目标的代码生成 |
| **带时间的结构体** | 非总线输入记录为包含以下字段的结构体：  - `time` - 由记录输入值的仿真时间点组成的列向量。 - `signals` - 具有采样值的结构体，包含以下字段：  - `values` - 由采样值组成的数组。   - `dimensions` - 采样维度。   - `label` - 模型中信号线的名称。 - `blockName` - To Workspace 模块的名称。 | 始终支持：  - 普通模式仿真。 - 使用 XCP 通信的外部模式仿真（如果 `StreamToWks` 设置为 `'on'` 并且 `MATFileLogging` 设置为 `'off'`）    支持，除非 To Workspace 模块位于引用模型中：  - 加速模式仿真 - 快速加速模式仿真 - 使用 TCP/IP 或串行通信的外部模式仿真    如果为生成的代码启用 **MAT 文件记录 (Simulink Coder)**，则支持，除非 To Workspace 模块位于引用模型中：  - 软件在环 (SIL) 仿真 - 处理器在环 (PIL) 仿真 - Simulink Coder 目标的代码生成 |
| **结构体** | 非总线输入记录为与**带时间的结构体**格式匹配的结构体，但该结构体的 `time` 字段为空。 |
| **数组** | 非总线输入的采样值保存为 *N* 维数组，其中 *N* 比输入维数大一。例如：  - 标量信号数据记录为列向量。 - 向量信号数据记录为矩阵。 - 矩阵信号数据记录为三维数组。    数组中值的结构取决于输入信号数据的维数：  - 对于标量和向量信号，每个采样值在输出数组中都有一个对应的行。数组的第一个维度与时间对齐，使得 `simout(1,:)` 返回记录的第一个信号值。 - 对于矩阵信号，输出数组的第三个维度与时间对齐，使得 `simout(:,:,1)` 返回记录的第一个信号值。 - 对于 *N* 维信号，最后一个维度与时间对齐，使得最后一个维度中的元素数等于从仿真记录的采样数。    输出数组只包含信号值，不包含时间数据。 |

##### 提示

- 要将数据记录为基于帧而不是基于采样，请执行以下操作：

  - 配置**保存格式**参数，以使用**结构体**或**数组**格式记录数据。
  - 将**将二维信号另存为**参数指定为**二维数组(沿第一个维度串联)**
- 当您要使用 From Workspace 模块加载记录的数据时，请考虑使用**时间序列**或**带时间的结构体**格式。当使用**数组**格式记录数据时，您需要在加载数据之前将采样时间值合并到数组中。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaveFormat` |
| **值:** | `"Timeseries"` (默认) | `"Structure with Time"` | `"Structure"` | `"Array"` |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"SaveFormat","Structure")`

#### **将二维信号另存为** — 所记录数据中二维采样值的排列 **三维数组(沿第三个维度串联)** (默认) | **二维数组(沿第一个维度串联)**

指定将二维输入数据记录为三维数组还是二维数组。

记录为三维数组非常适合基于采样的输入数据。采样在第三个维度上串联，这样可以轻松访问二维采样数据。

记录为二维数组非常适合基于帧的输入数据。采样在第一个维度上串联，这实际上从第一个维度删除了帧缓冲。

| 输入数据维度 | 将二维信号另存为... | 工作区数据维度 |
| --- | --- | --- |
| *M*×*N* | **二维数组(沿第一个维度串联)** | *K*×*N* 矩阵，其中 *K* 等于 *M* 乘以从仿真记录的采样数。  例如，记录 `2`×`4` 矩阵输入的十个采样会创建一个 `20`×`4` 矩阵。 |
| **三维数组(沿第一个维度串联)** | *M*×*N*×*K* 数组，其中 *K* 等于从仿真记录的采样数。  例如，记录 `2`×`4` 矩阵输入的十个采样会创建一个 `2`×`4`×`10` 数组。 |

##### 依赖关系

要启用此参数，请将**保存格式**设置为**数组**或**结构体**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Save2DSignal` |
| **值:** | `"3-D array (concatenate along third dimension)"` (默认) | `"2-D array (concatenate along first dimension)"` |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"Save2DSignal","2-D array (concatenate along first dimension)")`

#### **将定点数据记录为 fi 对象** — 记录的定点数据的数据类型 `on` (默认) | `off`

指定如何记录定点输入数据。

当**保存格式**参数指定为**时间序列**时，To Workspace 模块始终将定点输入数据记录为 `fi` (Fixed-Point Designer) 对象。要在**保存格式**参数未指定为**时间序列**时将定点数据记录为 `fi` 对象，请选择**将定点数据记录为 fi 对象**参数，并在普通或加速模式下运行仿真。

当您清除**将定点数据记录为 fi 对象**参数或在快速加速模式下运行仿真时，定点输入数据将记录为 `double`。

要将 `int64` 类型的输入数据记录为 `int64` 或将 `uint64` 类型的输入数据记录为 `uint64`，请选择**将定点数据记录为 fi 对象**参数。当您清除**将定点数据记录为 fi 对象**参数时，类型为 `int64` 或 `uint64` 的输入数据将记录为 `double`。

使用 To Workspace 模块记录定点数据需要 Fixed-Point Designer 许可证。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FixptAsFi` |
| **值:** | `"on"` (默认) | `"off"` |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"FixptAtFi","off")`

#### **采样时间** — 采样间隔和可选时间偏移量 -1 (默认) | 标量

指定模块在仿真期间记录输入值的时间。默认情况下，采样时间为继承 (`-1`)。对于连续采样时间，将值指定为 `0`。要使用离散采样时间，请将**采样时间**参数指定为标量。有关详细信息，请参阅指定采样时间。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar |
| **数据类型:** | `character vector` | `string` |

**示例:** `set_param(gcb,"SampleTime","0")`

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

不建议用于生产代码。

要生成将 To Workspace 模块的输入记录到 MAT 文件的代码，请启用 **MAT 文件记录**参数。有关详细信息，请参阅 **MAT 文件记录 (Simulink Coder)**。

下列情况不支持代码生成：

- 字符串数据类型。
- 引用模型中的模块。
- 使用**时间序列**格式记录数据的模块。有关详细信息，请参阅**保存格式**。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2025a: 记录 `datetime` 数据

To Workspace 模块支持记录 `datetime` 数据。

#### R2023b: 记录无界可变大小信号

在普通模式和加速模式仿真中，您可以使用 To Workspace 模块记录无界大小可变信号。不支持记录包含无界可变大小信号的非虚拟总线。

#### R2023a: 记录包含可变大小信号的非虚拟总线

在普通模式和加速模式仿真中，To Workspace 模块支持记录：

- 直接包含或在嵌套总线中包含可变大小信号的非虚拟总线
- 包含可变大小信号的嵌套非虚拟总线的总线

仅在普通模式仿真中，To Workspace 模块支持记录：

- 具有包含可变大小信号的非虚拟总线的总线数组

#### R2022a: 将数据记录到仿真数据检查器和工作区

数据会自动记录到仿真数据检查器和工作区中。仿真数据检查器会自动保留每个仿真的结果。由于使用 To Workspace 模块记录的数据会流式传输到仿真数据检查器，这些数据也会保留。

在以前的版本中，使用 To Workspace 模块记录的数据仅记录到工作区，并且每次仿真时都会被覆盖，除非您更改了记录变量名称或手动保存了结果。

在大多数情况下，您不需要对代码进行任何更改。记录大量数据或运行许多仿真会产生大量数据，导致磁盘空间被填满。要了解如何控制仿真数据检查器中保留的数据量，请参阅限制记录数据的大小。

#### R2022a: 使用内置数据类型记录 `int64` 和 `uint64` 数据

使用内置数据类型记录 `int64` 和 `uint64` 数据。

在以前的版本中，如果有 Fixed-Point Designer 许可证，则 To Workspace 模块会将 `int64` 和 `uint64` 数据记录为 `fi` 对象，如果没有许可证，则记录为 `double`。

#### R2022a: 使用 `string` 和 `half` 数据类型记录信号

To Workspace 模块支持 `string` 和 `half` 数据类型的记录信号。

#### R2022a: 记录总线数组

To Workspace 模块支持记录总线数组。

#### R2022a: 在快速加速仿真中使用 `Timeseries` 格式记录数据

以前，只有普通模式仿真或加速模式仿真可用于记录 `Timeseries` 格式的数据。

#### R2022a: 对 for-each 子系统内的 To Workspace 模块使用 `Timeseries` 格式记录数据

您可以使用 `Timeseries` 格式在 for-each 子系统内的 To Workspace 模块中记录数据。

## Libraries

Simulink / Sinks DSP System Toolbox / Sinks HDL Coder / Sinks

## Description

The To Workspace block logs the data connected to its input port to a
workspace from a Simulink® model. Typically, logged data is returned in the base workspace. When you
simulate a model programmatically inside a function, logged data is returned in the
workspace for the function. During simulation, logged data streams to the Simulation
Data Inspector. Logged data is written to the workspace when the simulation pauses or
stops.

You can use the To Workspace block to log data for a signal, a bus, or
an array of buses. The To Workspace block supports logging scalar and
multidimensional data, including data for variable-size signals.

You can configure the name of the variable that stores the data the To
Workspace block logs, and you can specify the format for the logged data.
You can also control which values the To Workspace block logs by
specifying block or model parameters. For more information, see Specify Signal Values to Log.

### Access Logged Data

How simulation results are returned to the workspace depends on how you simulate
and configure the model. Simulation results are returned in a single `Simulink.SimulationOutput` object in
any of these situations:

- You enable the **Single simulation
  output** parameter.

  By default, the **Single simulation output**
  parameter is enabled when you create a new model. You can enable the
  parameter using the Configuration Parameters dialog box. On the
  **Modeling** tab, under
  **Settings**, click **Model
  Settings**. Then, in the Configuration Parameters dialog
  box, select **Data Import/Export** and select
  **Single simulation output**.
- You run a set of simulations using the Multiple Simulations pane.
- You simulate the model programmatically using one or more `Simulink.SimulationInput`
  objects.

  You can configure simulations using `SimulationInput`
  objects when you run simulations using the `sim`, `parsim`, and `batchsim` functions.
- You simulate the model using a `sim` function
  syntax that returns results as a single simulation output.

  For more information, see `sim`.

When simulation results are returned in a single output, the
`SimulationOutput` object contains a variable for each To
Workspace block in the model. To access the data logged by a To
Workspace block:

- Use a dot with the variable name specified using the
  **Variable name** parameter of the block. By
  default, models are configured to return a single simulation output
  using the variable name `out`, and the To
  Workspace block saves data to a variable named
  `simout`.

  ```
  toWksData = out.simout;
  ```
- Use the `get` function with the
  name of the variable that contains the logged data.

  ```
  toWksData = get(out,simout);
  ```

In the model, the To Workspace block indicates how to access the
data in the workspace. By default, the block shows `out.simout`.
The block appearance updates when you:

- Specify a different value for the **Variable name**
  parameter on the block.
- Specify a different variable name for the single simulation
  output.
- Clear the **Single simulation output** configuration
  parameter.

## Ports

### Input

### **Port\_1** — Data to log to workspace scalar | vector | matrix | array | bus

Input port that receives data to log to workspace. The To
Workspace block supports logging real and complex data of
any built-in data type or user-defined data types such as buses,
enumerations, and fixed-point data.

#### Tips

Logging fixed-point data requires a license for Fixed-Point Designer™.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image` | `datetime`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Variable name** — Name of variable for saved data `simout` (default) | string | character vector

Specify a name for the variable that contains the logged data. By default,
the To Workspace block saves logged data in a variable called
`simout`. When a model contains multiple To
Workspace blocks, the **Variable name**
parameter value for each block must be unique.

For information about naming MATLAB® variables, see Variable Names.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VariableName` |
| **Values:** | `"simout"` (default) | valid MATLAB variable name |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"VariableName","myName")`

### **Limit data points to last** — Number of samples to log `inf` (default) | scalar | vector

When you want to save or analyze only the data from the end of a
simulation, specify the number of samples you want to log as a positive
whole number greater than zero. By default, the To Workspace
block logs data for the entire simulation, and the value for the
**Limit data points to last** parameter is
`inf`.

Limiting logged data to the last *n* signal values
directly impacts memory allocation. When you specify this parameter, the
software allocates memory upfront based on the specified value, not on the
time steps generated during the simulation. For this reason, the
**Limit data points to last** parameter is not
recommended when logging an indeterminate number of time steps.

For more information about controlling which samples are logged during
simulation, see Specify Signal Values to Log.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxDataPoints` |
| **Values:** | `"inf"` (default) | positive integer |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"MaxDataPoints","20")`

### **Decimation** — Decimation factor `1` (default) | positive integer

Specify a decimation factor to reduce the effective sample rate for the
logged data. For a decimation factor, *n*, the To
Workspace block logs every
*n*th sample value. For
example, when you specify the **Decimation** value as
`2`, the To Workspace block logs every
other data point.

For more information about controlling which samples are logged during
simulation, see Specify Signal Values to Log.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Decimation` |
| **Values:** | `"1"` (default) | positive integer |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"Decimation","2")`

### **Save format** — Format for data logged to workspace `Timeseries` (default) | `Structure With Time` | `Structure` | `Array`

Specify the format for the data logged to the workspace. To log data for a
bus or array of buses input, use `Timeseries`
format.

| **Save Format** Value | Workspace Data Format | Simulation Workflow Support |
| --- | --- | --- |
| `Timeseries` | Nonbus input logged as a `timeseries` object.  Bus input logged as a structure of `timeseries` objects. The hierarchy and names for fields in the structure matches the hierarchy and names specified in the `Simulink.Bus` object that defines the bus.  Array of buses input logged as an array of structures of `timeseries` objects. | Supported:  - Normal mode simulation - Accelerator mode simulation - Rapid   accelerator mode simulation *(since R2022a)* - External mode simulation that uses XCP   communication provided   `StreamToWks` is set to   `'on'` and   `MATFileLogging` is set to   `'off'`    Not supported:  - External mode simulation that uses TCP/IP or   serial communication - Software-in-the-loop (SIL) simulation - Processor-in-the-loop (PIL)   simulation - Code generation for Simulink   Coder™ targets |
| `Structure With Time` | Nonbus input logged as a structure that contains these fields:  - `time` — Column vector of   simulation time hits for which input value was   logged. - `signals` — Structure with   sample values that contains the fields:  - `values` — Array of sample     values.   - `dimensions` — Sample     dimensions.   - `label` — Name of signal     line in model. - `blockName` — Name of the   To Workspace block. | Always supported:  - Normal mode simulation. - External mode simulation that uses XCP   communication provided   `StreamToWks` is set to   `'on'` and   `MATFileLogging` is set to   `'off'`    Supported except when the To Workspace block is in a referenced model:  - Accelerator mode simulation - Rapid accelerator mode simulation - External mode simulation that uses TCP/IP or   serial communication    Supported if **MAT-file logging (Simulink Coder)** is enabled for generated code, except when the To Workspace block is in a referenced model:  - Software-in-the-loop (SIL) simulation - Processor-in-the-loop (PIL)   simulation - Code generation for Simulink   Coder targets |
| `Structure` | Nonbus input logged as a structure that matches the `Structure With Time` format, but the `time` field of the structure is empty. |
| `Array` | Sample values for nonbus input saved as *N*-dimensional array, where *N* is one greater than the dimensions of the input. For example:  - Scalar signal data is logged as a column   vector. - Vector signal data is logged as a   matrix. - Matrix signal data is logged as a 3-D   array.    The structure of the values in the array depends on the dimensions of the input signal data:  - For scalar and vector signals, each sample   value is a row in the output array. The first   dimension of the array aligns with time such that   `simout(1,:)` returns the first   logged signal value. - For matrix signals, the third dimension of   the output array aligns with time such that   `simout(:,:,1)` returns the first   logged signal value. - For *N*-dimensional   signals, the last dimension aligns with time, such   that the number of elements in the last dimension   is equal to the number of samples logged from   simulation.    The output array contains only signal values and does not contain time data. |

#### Tips

- To log data as frame-based instead of sample-based:

  - Configure the **Save format**
    parameter to log data using the
    `Structure` format or the
    `Array` format.
  - Specify the **Save 2-D signals
    as** parameter as `2-D array
    (concatenate along first
    dimension)`
- When you want to load the logged data using a From
  Workspace block, consider using the
  `Timeseries` or
  `Structure With Time` formats. When
  you log data using the `Array` format,
  you need to incorporate the sample time values into the array
  before loading the data.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaveFormat` |
| **Values:** | `"Timeseries"` (default) | `"Structure with Time"` | `"Structure"` | `"Array"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"SaveFormat","Structure")`

### **Save 2-D signals as** — Arrangement of 2-D sample values in logged data `3-D array (concatenate along third dimension)` (default) | `2-D array (concatenate along first dimension)`

Specify whether to log 2-D input data as a 3-D array or a 2-D
array.

Logging as a 3-D array is well suited for sample-based input data. Samples
are concatenated along the third dimension, allowing easy access of
2-dimensional sample data.

Logging as a 2-D array is well suited for frame-based input data. Samples
are concatenated along the first dimension, which in effect removes the
frame buffering from the first dimension.

| Input Data Dimensions | Save 2-D Signal As... | Workspace Data Dimensions |
| --- | --- | --- |
| *M*-by-*N* | `2-D array (concatenate along first dimension)` | *K*-by-*N* matrix, where *K* is equal to *M* times the number of samples logged from simulation.  For example, logging ten samples of a `2`-by-`4` matrix input creates a `20`-by-`4` matrix. |
| `3-D array (concatenate along first dimension)` | *M*-by-*N*-by-*K* array, where *K* is equal to the number of samples logged from simulation.  For example, logging ten samples of a `2`-by-`4` matrix input creates a `2`-by-`4`-by-`10` array. |

#### Dependencies

To enable this parameter, set the **Save format** to
`Array` or
`Structure`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Save2DSignal` |
| **Values:** | `"3-D array (concatenate along third dimension)"` (default) | `"2-D array (concatenate along first dimension)"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"Save2DSignal","2-D array
(concatenate along first dimension)")`

### **Log fixed-point data as a fi object** — Data type for logged fixed-point data `on` (default) | `off`

Specify how to log fixed-point input data.

The To Workspace block always logs fixed-point input data
as a `fi` (Fixed-Point Designer) object when the
**Save format** parameter is specified as
`Timeseries`. To log fixed-point data as a
`fi` object when the **Save format**
parameter is not specified as `Timeseries`, select
the **Log fixed-point data as a fi object** parameter and
run the simulation in normal or accelerator mode.

When you clear the **Log fixed-point data as a fi
object** parameter or run the simulation in rapid accelerator
mode, fixed-point input data is logged as `double`.

To log input data of type `int64` as
`int64` or type `uint64` as
`uint64`, select the **Log fixed-point data as
a fi object** parameter. When you clear the **Log
fixed-point data as a fi object** parameter, input data of type
`int64` or `uint64` is logged as
`double`.

Using the To Workspace block to log fixed-point data
requires a license for Fixed-Point Designer.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FixptAsFi` |
| **Values:** | `"on"` (default) | `"off"` |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"FixptAtFi","off")`

### **Sample time** — Sampling interval and optional time offset -1 (default) | scalar

Specify when the block logs the input value during simulation. By default,
the sample time is inherited (`-1`). For continuous sample
time, specify the value as `0`. To use a discrete sample
time, specify the **Sample time** parameter as a scalar.
For more information, see Specify Sample Time.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar |
| **Data Types:** | `character vector` | `string` |

**Example:** `set_param(gcb,"SampleTime","0")`

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

Not recommended for production code.

To generate code that logs the input to the To Workspace block to a
MAT file, enable the **MAT-file logging** parameter. For more
information, see **MAT-file logging (Simulink Coder)**.

Code generation is not supported for:

- String data types.
- Blocks inside referenced models.
- Blocks that log data using the `Timeseries`
  format. For more information, see **Save
  format**.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2025a: Log `datetime` data

The To Workspace block supports logging `datetime` data.

### R2023b: Log unbounded variable-size signals

In normal and accelerator mode simulations, you can log an unbounded variable-size
signal using the To Workspace block. Logging is not supported for
nonvirtual buses that contain unbounded variable-size signals.

### R2023a: Log nonvirtual buses that contain variable-size signals

In normal and accelerator mode simulation, the To Workspace block
supports logging:

- Nonvirtual buses that contain variable-size signals directly or in nested
  buses
- Buses with nested nonvirtual buses that contain variable-size
  signals

In normal mode simulations only, the To Workspace block supports
logging:

- Arrays of buses with nonvirtual buses that contain variable-size
  signals

### R2022a: Log data to the Simulation Data Inspector as well as the workspace

Data is automatically logged to the Simulation Data Inspector as well as the
workspace. The Simulation Data Inspector automatically retains results from each
simulation. Because data logged using the To Workspace block streams
to the Simulation Data Inspector, this data is also retained.

In previous releases, data logged using the To Workspace block
only logged to the workspace and was overwritten for each simulation unless you
changed the logging variable names or manually saved the results.

In most cases, you do not need to make any changes to your code. Logging large
amounts of data or running many simulations can produce large amounts of data that
fill up disk space. To learn how to control the amount of data retained in the
Simulation Data Inspector, see Limit the Size of Logged Data.

### R2022a: Log `int64` and `uint64` data using built-in data types

Log `int64` and `uint64` data using the built-in
data types.

In previous releases, the To Workspace block logged
`int64` and `uint64` data as a
`fi` object when a license for Fixed-Point Designer was available and as `double` when the license was
not available.

### R2022a: Log signals with `string` and `half` data types

The To Workspace block supports logging signals with
`string` and `half` data types.

### R2022a: Log arrays of buses

The To Workspace block supports logging an array of buses.

### R2022a: Log data using the `Timeseries` format in rapid accelerator simulations

Previously, only normal mode simulation or accelerator mode simulation could be
used to log data in `Timeseries` format.

### R2022a: Log data using the `Timeseries` format for To Workspace blocks inside for-each subsystems

You can use the `Timeseries` format to log data in a To
Workspace block inside for-each subsystems.
