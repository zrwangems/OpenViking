---
type: simulink-block
title: 'To File'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'tofile'
---

# To File

Write data to file

## 中文

将数据写入到文件

### 所属库

Simulink / Sinks HDL Coder / Sinks

### 描述

To File 模块将输入信号数据写入 MAT 文件。此模块以增量方式写入到输出文件中，在仿真期间的内存开销极少。如果仿真开始时已经存在输出文件，模块将覆盖该文件。暂停仿真或仿真完成时，文件会自动关闭。如果仿真异常终止，To File 模块将保存它在异常终止时间点之前记录的数据。

To File 模块图标会显示输出文件的名称。

#### 控制保存的数据量

如果使用**配置参数** > **数据导入/导出** > **记录间隔**参数指定数据记录间隔，则 To File 模块仅记录时间间隔内的数据。例如，如果时间间隔为空 (`[]`)，模块则不会记录任何数据。此模块将记录的数据存储在与模块关联的文件中，而不是存储在您为**单一仿真输出**参数指定的变量中。

对于变步长求解器，要控制 To File 模块可用的数据量，请使用**配置参数** > **数据导入/导出** > **附加参数** > **输出选项**参数。例如，要在多次仿真的相同时间点写入数据，请选择 `Produce specified output only` 选项。

模块参数还控制保存的数据量。请参阅抽取和采样时间。

#### 暂停仿真

暂停仿真后，不要更改 To File 模块记录的任何文件。例如，不要使用 MATLAB® `save` 命令保存此类文件。更改文件可能会导致恢复仿真时出现错误。如果要在暂停后更改文件，请复制文件并使用文件副本。

如果通过仿真步进器暂停，To File 模块将捕获暂停时间点之前的仿真数据。当您步退时，To File 数据文件将不再包含上次输出在减少时间之后的任何仿真数据。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | 数组

要存储在文件中的信号。每个采样都包含时间戳和相关数据值。数据可以是数组格式或 MATLAB `timeseries` 格式。To File 模块接受 Simulink® 软件支持的任何数据类型的实信号或复信号数据，但字长超过 32 位的定点数据除外。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **文件名** — 路径或文件名 `untitled.mat` (默认) | MAT 文件路径或名称

指定用来存储输出的 MAT 文件的路径名或文件名。在 UNIX® 系统中，路径名称可以用波浪号字符 (~) 开头（该符号表示主文件夹）。如果指定的文件名没有路径信息，Simulink 软件会将文件存储在 MATLAB 工作文件夹中。（要确定工作文件夹，请在 MATLAB 命令行输入 `pwd`。）如果文件存在，Simulink 软件将覆盖它。

##### 编程用法

|  |
| --- |
| **模块参数：**`FileName` |
| **类型：**字符向量 |
| **值：**MAT 文件路径或名称 |
| **默认值：**`'untitled.mat'` |

#### **变量名称** — 矩阵名称 `ans` (默认) | 字符向量

指定文件中包含的矩阵的名称。

##### 编程用法

|  |
| --- |
| **模块参数：**`MatrixName` |
| **类型：**字符向量 |
| **值：**字符向量 |
| **默认值：**`'ans'` |

#### **保存格式** — 数据格式 **时间序列** (默认) | **数组**

指定 To File 模块写入数据所使用的数据格式。

**数组**格式仅用于向量、双精度、非复信号。

对于**时间序列**格式，To File 模块：

- 将数据写入到 MATLAB `timeseries` 对象中。
- 支持写入多维、实数或复数输出值。
- 支持写入任何内置数据类型的输出值，包括 `Boolean`、枚举 (`enum`) 和字长最多 32 位的定点数据。
- 对于虚拟和非虚拟总线输入信号，创建与总线架构匹配的 MATLAB 结构体。结构体的每个叶是一个 MATLAB `timeseries` 对象。

对于**数组**格式，To File 模块：

- 将数据写入到包含两行或多行的矩阵中。矩阵形式如下：

  [t1t2…tfinalu11u12…u1final…un1un2…unfinal]

  Simulink 软件在矩阵中为每个数据采样写入一列。列中的第一个元素包含时间戳。列的其余部分包含对应输出值的数据。
- 支持写入一维、双精度和非复数数据。

From File 模块可使用 To File 模块以任何格式（`Timeseries` 或 `Array`）写入的数据，无需对数据进行任何修改，也没有其他特殊配置。

From Workspace 模块可读取 `Array` 格式的数据，以及 To File 模块写入的数据的转置数据。要提供所需的格式，请使用 MATLAB 命令从 MAT 文件中加载并转置数据。

下表显示了不同**保存格式**值对仿真模式的支持情况。

| 仿真模式 | **时间序列** | **数组** |
| --- | --- | --- |
| 普通 | 支持 | 支持 |
| 加速 | 支持 | 支持 |
| 快速加速 | 支持 | 支持 |
| 软件在环 (SIL) | 不支持 | 如果启用 MAT 文件记录，则支持 |
| 处理器在环 (PIL) | 不支持 | 如果 MAT 文件记录可用并已启用，则支持 |
| 外部 | 不支持 | 如果启用 MAT 文件记录，则支持 |
| RSim 目标 | 支持 | 如果启用 MAT 文件记录，则支持 |

##### 编程用法

|  |
| --- |
| **模块参数：**`SaveFormat` |
| **类型：**字符向量 |
| **值**：`'Timeseries' | 'Array'` |
| **默认值：**`'Timeseries'` |

#### **抽取** — 确定数据写入时间的抽取因子 1 (默认) | 标量 | 向量

指定抽取因子 *n*，它在模块每执行 *n* 次时写入数据。默认值使此模块在每个时间步写入数据。

##### 编程用法

|  |
| --- |
| **模块参数**：`Decimation` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'1'` |

#### **采样时间** — 采样周期和偏移量 -1 (默认) | 标量 | 向量

指定采集数据点的采样周期和偏移量。使用时间步间隔不是常量的变步长求解器时，此参数很有用。默认值使此模块继承驱动模块的采样时间。请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 最高支持 32 位定点数据类型。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含动态分配和释放内存、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

RSim 目标的代码生成提供与 Simulink 相同的支持；所有其他代码生成目标仅支持具有时间格式的数组中的一维双精度实信号。

要为 To File 模块生成代码，请在**代码生成** > **接口**窗格中选择配置参数 MAT 文件记录 (Simulink Coder)。

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

支持多达 32 位的定点数据类型。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Description

The To File block writes input signal data into a MAT file.
The block writes to the output file incrementally, with minimal memory overhead during
simulation. If the output file exists when the simulation starts, the block overwrites
the file. The file automatically closes when you pause the simulation or the simulation
completes. If simulation terminates abnormally, the To File block saves
the data it has logged up until the point of the abnormal termination.

The To File block icon shows the name of the output file.

### Control Amount of Data Saved

If you specify data logging intervals with the **Configuration Parameters** >  **Data Import/Export** >  **Logging intervals** parameter, the To File block logs only data inside of
the intervals. For example, the block logs no data if the intervals are empty
(`[]`). The block stores the logged data in the file associated
with the block instead of in the variable that you specify for the **Single
simulation output** parameter.

For variable-step solvers, to control the amount of data available to the
To File block, use the **Configuration Parameters** >  **Data Import/Export** >  **Additional parameters** >  **Output options** parameter. For example, to write data at identical time points over
multiple simulations, select the `Produce specified output only`
option.

Block parameters also control the amount of data saved. See Decimation and Sample time.

### Pause Simulation

After pausing a simulation, do not alter any file that a To File
block logs into. For example, do not save such a file with the MATLAB®
`save` command. Altering the file can cause an error when you
resume the simulation. If you want to alter the file after pausing, copy the file
and work with the copy of the file.

If you pause using the Simulation Stepper, the To File block
captures the simulation data up to the point of the pause. When you step back, the
To File data file no longer contains any simulation data past the
new reduced time of the last output.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | array

Signal to store in file. Each sample consists of a timestamp and an
associated data value. The data can be in array format or MATLAB
`timeseries` format. The To File block
accepts real or complex signal data of any data type that Simulink® software supports, except fixed-point data with a word
length greater than 32 bits.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **File name** — Path or file name `untitled.mat` (default) | MAT file path or name

Specify the path or file name of the MAT file in which to store the
output. On UNIX® systems, the path name can start with a tilde (~) character
signifying your home folder. If you specify a file name without path
information, Simulink software stores the file in the MATLAB working folder. (To determine the working folder, at the
MATLAB command line, enter `pwd`.) If the file
exists, Simulink software overwrites it.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `FileName` |
| **Type:** character vector |
| **Values:** MAT file path or name |
| **Default:**  `'untitled.mat'` |

### **Variable name** — Matrix name `ans` (default) | character vector

Specify the name of the matrix contained in the file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `MatrixName` |
| **Type:** character vector |
| **Values:** character vector |
| **Default:**  `'ans'` |

### **Save format** — Data format `Timeseries` (default) | `Array`

Specify the data format that the To File block uses for
writing data.

Use the `Array` format only for vector, double,
noncomplex signals.

For the `Timeseries` format, the To
File block:

- Writes data in a MATLAB
  `timeseries` object.
- Supports writing multidimensional, real, or complex output
  values.
- Supports writing output values that have any built-in data type,
  including `Boolean`, enumerated
  (`enum`), and fixed-point data with a word
  length of up to 32 bits.
- For virtual and nonvirtual bus input signals, creates a
  MATLAB structure that matches the bus hierarchy. Each leaf of
  the structure is a MATLAB
  `timeseries` object.

For the `Array` format, the To
File block:

- Writes data into a matrix containing two or more rows. The matrix
  has the following form:

  [t1t2…tfinalu11u12…u1final…un1un2…unfinal]

  Simulink software writes one column to the matrix for each data
  sample. The first element of the column contains the timestamp. The
  remainder of the column contains data for the corresponding output
  values.
- Supports writing data that is one-dimensional, double, and
  noncomplex.

The From File block can use data
written by a To File block in any format
(`Timeseries` or `Array`) without any
modifications to the data or other special provisions.

The From Workspace block can
read data that is in the `Array` format and is the
transposition of the data written by the To File block. To
provide the required format, use MATLAB commands to load and transpose the data from the MAT
file.

The following table shows how simulation mode support depends on the
**Save format** value.

| Simulation Mode | `Timeseries` | `Array` |
| --- | --- | --- |
| Normal | Supported | Supported |
| Accelerator | Supported | Supported |
| Rapid Accelerator | Supported | Supported |
| Software-in-the-loop (SIL) | Not supported | Supported if MAT file logging is enabled |
| Processor-in-the-loop (PIL) | Not supported | Supported if MAT file logging is available and enabled |
| External | Not supported | Supported if MAT file logging is enabled |
| RSim target | Supported | Supported if MAT file logging is enabled |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `SaveFormat` |
| **Type:** character vector |
| **Values:** `'Timeseries' | 'Array'` |
| **Default:**  `'Timeseries'` |

### **Decimation** — Decimation factor that determines when data writes 1 (default) | scalar | vector

Specify the decimation factor, *n*, that writes data at
every *n*th time that the block executes. The default value
has this block writing data at every time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decimation` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1'` |

### **Sample time** — Sample period and offset -1 (default) | scalar | vector

Specifies the sample period and offset at which to collect data points.
This parameter is useful when you are using a variable-step solver where the
interval between time steps is not constant. The default value causes the
block to inherit the sample time from the driving block. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Supports up to 32-bit fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

Code generation for RSim target provides identical support as Simulink; all other code generation targets support only double,
one-dimensional, real signals in array with time format.

To generate code for a To File block, on
the **Code Generation** > **Interface** pane, select the configuration parameter MAT-file logging (Simulink Coder).

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

Supports up to 32-bit fixed-point data types.

## Version History

**Introduced before R2006a**
