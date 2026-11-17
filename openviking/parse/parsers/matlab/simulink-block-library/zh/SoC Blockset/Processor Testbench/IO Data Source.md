---
type: simulink-block
title: 'IO Data Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Testbench'
documentation_page: 'iodatasource'
documentation_source_path: 'ref/iodatasource.html'
language: zh-CN
chinese_source: worker-translation
---

# IO Data Source

## 端口
```yaml
ports:
- name: data
  summary: 输入数据 数值向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: length
  summary: 输入数据长度 非负标量
  direction: input
  data_types: uint32
- name: valid
  summary: 有效数据信号 Boolean 标量
  direction: input
  data_types: Boolean
- name: done
  summary: 内存中缓冲区已释放的通知 False（默认）| True
  direction: input
  data_types: Boolean
- name: event
  summary: 任务事件信号 标量
  direction: output
  data_types: rteEvent
- name: msg
  summary: SoC 消息数据 数值向量
  direction: output
  data_types: SoCData
```

### 输入

### **data** — 输入数据 数值向量

输入数据，指定为数值向量。该模块将此数据转换为由 **Device type** 参数指定的特定设备类型的总线信号。将此输入数据的数据类型与您在 **Data type** 参数中选择的数据类型匹配。输出总线信号由数据值、数据长度和数据的有效状态组成。

#### 依赖关系

要启用此端口，请将 **Input** 参数设置为 `From input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **length** — 输入数据长度 非负标量

输入数据长度，指定为非负标量。

#### 依赖关系

要启用此端口，请将 **Input source** 参数设置为 `From input port`。

**数据类型：** `uint32`

### **valid** — 有效数据信号 `Boolean` 标量

当 **valid** 为 `1` 时，该模块从 **data** 和 **length** 端口捕获输入数据。当 **valid** 为 `0` 时，该模块将输入数据视为无效，不捕获该数据。

#### 依赖关系

要启用此端口，请将 **Input source** 参数设置为 `From input port`。

**数据类型：** `Boolean`

### **done** — 内存中缓冲区已释放的通知 `False`（默认）| `True`

此消息端口从连接的 Memory Channel 或 IO Data Sink 模块接收通知，表明读事务已完成，并且内存中的缓冲区可用于写入。

#### 依赖关系

要启用此端口，请将 **Device type** 参数设置为 `Stream`。

**数据类型：** `Boolean`
### 输出

### **event** — 任务事件信号 标量

此端口发送任务事件信号，触发 Task Manager 模块执行关联的事件驱动任务。

#### 依赖关系

要启用此端口，请将 **Show port** 参数设置为 `Event` 或 `Data and event`。

**数据类型：** `rteEvent`

### **msg** — SoC 消息数据 数值向量

此端口将数据向量作为消息发送到处理器 I/O 模块的 **msg** 输入端口，这些模块包括 Register Read、Stream Read、UDP Read 和 TCP Read 模块。

#### 依赖关系

要启用此端口，请将 **Show port** 参数设置为 `Data` 或 `Data and Event`。

**数据类型：** `SoCData`
## 参数
```yaml
parameters:
- name: Input
  summary: 输入数据源 From file（默认）| From dialog | From input port | From timeseries object
  group: ''
- name: Value
  summary: 源数据的值 uint32(1:1024)（默认）| 用于生成输入数据的函数
  group: ''
- name: Data type
  summary: 输入数据的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | boolean | fixed
    point
  group: ''
- name: Device type
  summary: 输入数据源的设备类型 UDP（默认）| TCP | Register | Stream
  group: ''
- name: Sample time
  summary: 采样时间间隔 -1（默认）| 非负标量
  group: ''
- name: Dimensions
  summary: 每帧采样数 1024（默认）| 非负标量
  group: ''
- name: Dataset name
  summary: 录制文件的名称 无默认值 | 文件路径
  group: ''
- name: Source name
  summary: 数据集名称 无默认值
  group: ''
- name: Number of buffers
  summary: 数据缓冲区数量 1024（默认）| 非负标量
  group: ''
- name: Show port
  summary: 启用输出端口 Data（默认）| Event | Data and event
  group: ''
- name: Object name
  summary: timeseries 对象的名称 []（默认）| timeseries 对象
  group: ''
```

### **Input** — 输入数据源 `From file`（默认）| `From dialog` | `From input port` | `From timeseries object`

通过选择以下值之一来设置模块的输入数据源。

- `From file` — 从记录的数据文件中读取数据，时间间隔与在硬件板上记录时的时间间隔相同。
- `From dialog` — 通过使用函数输入一维数据数组。为 **Value** 参数指定此函数。
- `From input port` — 使用模块上的输入端口输入数据和信号。
- `From timeseries object` — 使用您在 MATLAB® 中创建的 timeseries 对象输入数据和时间值。有关详细信息，请参阅 Time Series Objects and Collections。

### **Value** — 源数据的值 `uint32(1:1024)`（默认）| 用于生成输入数据的函数

指定一个 MATLAB 函数，该函数创建一个数值数据的行向量。此行向量被捕获为模块的输入数据。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From dialog`。

### **Data type** — 输入数据的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `boolean` | `fixed point`

选择 **data** 端口要接收的输入数据的数据类型。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From file`。

### **Device type** — 输入数据源的设备类型 `UDP`（默认）| `TCP` | `Register` | `Stream`

选择设备类型以启用相应的输出数据端口。

- `UDP` — 启用 **msg** 输出端口，将 UDP 数据作为消息输出。
- `TCP` — 启用 **msg** 输出端口，将 TCP 数据作为消息输出。
- `Register` — 启用 **msg** 输出端口，将 Register 数据作为消息输出。
- `Stream` — 启用 **msg** 输出端口，将 Stream 数据作为消息输出。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From input port` 或 `From dialog`。

### **Sample time** — 采样时间间隔 `-1`（默认）| 非负标量

指定模块输出数据的离散时间间隔，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From dialog`。

### **Dimensions** — 每帧采样数 `1024`（默认）| 非负标量

指定输入数据的大小。模块在仿真中读取和回放期间每帧读取此数量的采样。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From file`。

### **Dataset name** — 录制文件的名称 无默认值 | 文件路径

指定主机 PC 上录制数据文件的完整路径，或浏览并选择主机 PC 上的文件。此模块仅支持使用 SoC Blockset™ 数据录制 API 创建的 TGZ 文件。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From file`。

### **Source name** — 数据集名称 无默认值

指定您想要用作输入源的数据集源名称，该输入源在 **Dataset name** 参数指定的录制数据中可用。您可以在 **Source name** 框中键入名称，或点击 **Select** 从录制数据文件中可用的源列表中选择名称。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From file`。

### **Number of buffers** — 数据缓冲区数量 `1024`（默认）| 非负标量

指定要存储在输入数据队列中的数据元素数量。

#### 依赖关系

要启用此参数，请将 **Device type** 参数设置为 `Stream`。

### **Show port** — 启用输出端口 `Data`（默认）| `Event` | `Data and event`

选择以下值之一以启用相应的输出端口。

- `Data` — 仅启用 **msg** 输出端口。
- `Event` — 仅启用 **event** 输出端口。
- `Data and event` — 启用 **msg** 和 **event** 输出端口。

### **Object name** — timeseries 对象的名称 `[]`（默认）| timeseries 对象

指定一个 `timeseries` 对象。此 `timeseries` 对象为模块提供输入数据。有关时间序列对象的更多信息，请参阅 Time Series Objects and Collections。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From timeseries object`。
## 所属库

SoC Blockset / I/O Data Source and Sink

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 不为该模块生成代码。在生成的代码中，设备 I/O 直接连接到 TCP Read、UDP Read、Stream Read 或 Register Read 模块。

## 版本历史

**在 R2019a 中引入**

## 描述

回放记录的数据

IO Data Source 模块使您能够导入记录的硬件 IO 数据，并在您的 Simulink® 模型中回放。该模块将输入数据转换为消息信号，您可以根据所选择的设备类型，将其作为输入提供给 TCP Read、UDP Read、Stream Read 或 Register Read 模块。在您的 Simulink 模型中回放硬件 IO 数据有助于您开发出比在仿真期间使用随机生成数据所开发的模型具有更高精度的模型。

当您开发在部署期间使用真实硬件 IO 数据的模型时，您可以选择在仿真中使用随机生成的合成数据作为硬件 IO 数据。因为物理硬件数据会考虑各种效应，如数据丢失、时间延迟等。如果您在此类模型的仿真中使用合成数据作为硬件 IO 数据，则在将其部署到硬件板中时会导致意外结果。为了评估和验证此类模型，建议在仿真期间使用真实硬件 IO 数据。有关如何记录硬件 IO 数据并将其保存到您的主机计算机的更多信息，请参阅 `DataRecorder` 对象。

**注意**

如果您的模型中有一个 IO Data Source 模块，其 **Input** 设置为 `From file`，并与 `Timer-driven` Task Manager 模块关联，并且您计划使用固定步长求解器，则输入的步长值应小于 Task Manager 模块中 **Period** 参数设置的值。例如，假设 Task Manager 模块中指定的 **Period** 值为 `0.1`，则选择小于 `0.1` 的固定步长。
