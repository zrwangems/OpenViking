---
type: simulink-block
title: 'To File'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'tofile'
documentation_source_path: '../simulink/slref/tofile.html'
language: zh-CN
chinese_source: worker-translation
---

# To File

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | 数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | 数组

要存储在文件中的信号。每个样本由一个时间戳和一个关联的数据值组成。数据可以是数组格式或 MATLAB `timeseries` 格式。To File 模块接受 Simulink® 软件支持的任何数据类型的实数或复数信号数据，但字长大于 32 位的定点数据除外。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: File name
  summary: 路径或文件名 untitled.mat（默认）| MAT 文件路径或名称
  group: ''
  block_parameter: FileName
  type: character vector
  values: MAT file path or name
  default: '''untitled.mat'''
- name: Variable name
  summary: 矩阵名称 ans（默认）| 字符向量
  group: ''
  block_parameter: MatrixName
  type: character vector
  values: character vector
  default: '''ans'''
- name: Save format
  summary: 数据格式 Timeseries（默认）| Array
  group: ''
  block_parameter: SaveFormat
  type: character vector
  values: '''Timeseries'' | ''Array'''
  default: '''Timeseries'''
- name: Decimation
  summary: 决定何时写入数据的抽取因子 1（默认）| 标量 | 向量
  group: ''
  block_parameter: Decimation
  type: character vector
  values: scalar | vector
  default: '''1'''
- name: Sample time
  summary: 采样周期和偏移量 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar | vector
  default: '''-1'''
```

### **File name** — 路径或文件名 `untitled.mat`（默认）| MAT 文件路径或名称

指定用于存储输出的 MAT 文件的路径或文件名。在 UNIX® 系统上，路径名可以以波浪号（~）字符开头，表示您的主文件夹。如果指定的文件名不包含路径信息，Simulink 软件会将文件存储在 MATLAB 工作文件夹中。（要确定工作文件夹，请在 MATLAB 命令行中输入 `pwd`。）如果文件已存在，Simulink 软件将覆盖它。

#### 编程使用

|  |
| --- |
| **模块参数**：`FileName` |
| **类型**：character vector |
| **值**：MAT file path or name |
| **默认值**：`'untitled.mat'` |

### **Variable name** — 矩阵名称 `ans`（默认）| 字符向量

指定文件中包含的矩阵的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`MatrixName` |
| **类型**：character vector |
| **值**：character vector |
| **默认值**：`'ans'` |

### **Save format** — 数据格式 `Timeseries`（默认）| `Array`

指定 To File 模块用于写入数据的数据格式。

仅对向量、双精度、非复数信号使用 `Array` 格式。

对于 `Timeseries` 格式，To File 模块：

- 将数据写入 MATLAB `timeseries` 对象。
- 支持写入多维、实数或复数输出值。
- 支持写入具有任何内置数据类型的输出值，包括 `Boolean`、枚举（`enum`）以及字长最多为 32 位的定点数据。
- 对于虚拟和非虚拟总线输入信号，创建与总线层次结构匹配的 MATLAB 结构体。结构体的每个叶节点都是一个 MATLAB `timeseries` 对象。

对于 `Array` 格式，To File 模块：

- 将数据写入包含两行或更多行的矩阵。该矩阵具有以下形式：

  [t1t2…tfinalu11u12…u1final…un1un2…unfinal]

  Simulink 软件为每个数据样本向矩阵写入一列。列的第一个元素包含时间戳。列的其余部分包含对应输出值的数据。
- 支持写入一维、双精度和非复数数据。

From File 模块可以使用 To File 模块以任何格式（`Timeseries` 或 `Array`）写入的数据，而无需对数据进行任何修改或其他特殊处理。

From Workspace 模块可以读取 `Array` 格式的数据，该数据是 To File 模块写入数据的转置。要提供所需的格式，请使用 MATLAB 命令从 MAT 文件中加载并转置数据。

下表显示了仿真模式支持如何取决于 **Save format** 值。

| 仿真模式 | `Timeseries` | `Array` |
| --- | --- | --- |
| Normal | 支持 | 支持 |
| Accelerator | 支持 | 支持 |
| Rapid Accelerator | 支持 | 支持 |
| Software-in-the-loop (SIL) | 不支持 | 如果启用了 MAT 文件记录则支持 |
| Processor-in-the-loop (PIL) | 不支持 | 如果 MAT 文件记录可用且已启用则支持 |
| External | 不支持 | 如果启用了 MAT 文件记录则支持 |
| RSim target | 支持 | 如果启用了 MAT 文件记录则支持 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaveFormat` |
| **类型**：character vector |
| **值**：`'Timeseries' | 'Array'` |
| **默认值**：`'Timeseries'` |

### **Decimation** — 决定何时写入数据的抽取因子 1（默认）| 标量 | 向量

指定抽取因子 *n*，即模块每执行 *n* 次写入一次数据。默认值使该模块在每个时间步写入数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`Decimation` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'1'` |

### **Sample time** — 采样周期和偏移量 -1（默认）| 标量 | 向量

指定采集数据点的采样周期和偏移量。当您使用时间步之间的间隔不固定的变步长求解器时，此参数非常有用。默认值使模块从驱动模块继承采样时间。请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'-1'` |
## 所属库

Simulink / Sinks HDL Coder / Sinks

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 支持最多 32 位定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。涉及嵌入式系统中常见的资源限制以及速度和内存限制。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化很大的执行时间。虽然该代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐渐演变为适合生产代码。因此，适合生产代码的模块仍然适合。

RSim 目标的代码生成提供与 Simulink 相同的支持；所有其他代码生成目标仅支持数组时间格式的双精度、一维、实数信号。

要为 To File 模块生成代码，请在 **Code Generation** > **Interface** 窗格中，选择配置参数 MAT-file logging (Simulink Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

支持最多 32 位定点数据类型。

## 版本历史

**在 R2006a 之前推出**

## 描述

将数据写入文件

To File 模块将输入信号数据写入 MAT 文件。该模块以增量方式写入输出文件，在仿真期间内存开销最小。如果仿真开始时输出文件已存在，该模块将覆盖该文件。当您暂停仿真或仿真完成时，文件会自动关闭。如果仿真异常终止，To File 模块会保存直到异常终止点之前已记录的数据。

To File 模块图标显示输出文件的名称。

### 控制保存的数据量

如果您使用 **Configuration Parameters** > **Data Import/Export** > **Logging intervals** 参数指定数据记录间隔，则 To File 模块仅记录这些间隔内的数据。例如，如果间隔为空（`[]`），则该模块不记录任何数据。该模块将记录的数据存储在与其关联的文件中，而不是存储在您为 **Single simulation output** 参数指定的变量中。

对于变步长求解器，要控制 To File 模块可用的数据量，请使用 **Configuration Parameters** > **Data Import/Export** > **Additional parameters** > **Output options** 参数。例如，要在多次仿真中在相同的时间点写入数据，请选择 `Produce specified output only` 选项。

模块参数也控制保存的数据量。请参阅 Decimation 和 Sample time。

### 暂停仿真

暂停仿真后，请勿更改 To File 模块记录到的任何文件。例如，不要使用 MATLAB® 的 `save` 命令保存此类文件。更改文件可能会导致恢复仿真时出错。如果您想在暂停后更改文件，请复制该文件并使用该文件的副本进行操作。

如果您使用 Simulation Stepper 暂停，To File 模块会捕获直到暂停点之前的仿真数据。当您后退时，To File 数据文件将不再包含超过新的缩减后的最后输出时间的任何仿真数据。
