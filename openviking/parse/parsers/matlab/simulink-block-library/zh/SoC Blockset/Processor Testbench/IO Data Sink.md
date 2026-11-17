---
type: simulink-block
title: 'IO Data Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Testbench'
documentation_page: 'iodatasink'
documentation_source_path: 'ref/iodatasink.html'
language: zh-CN
chinese_source: worker-translation
---

# IO Data Sink

## 端口
```yaml
ports:
- name: msg
  summary: SoC 消息数据数值向量
  direction: input
  data_types: SoCData
- name: data
  summary: 输出数据数值向量
  direction: output
  data_types: uint32 | double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | Boolean | fixedpoint
- name: length
  summary: 输出数据长度 非负标量
  direction: output
  data_types: double
- name: valid
  summary: 有效数据指示 Boolean 标量
  direction: output
  data_types: Boolean
- name: done
  summary: 数据流完成 Boolean 标量
  direction: output
  data_types: Boolean
- name: event
  summary: 任务事件信号 标量
  direction: output
  data_types: rteEvent
```

### 输入

### **msg** — SoC 消息数据数值向量

此端口接收来自处理器 I/O 模块的 **msg** 端口的数据向量，包括 Stream Write、TCP Write、UDP Write 或 Register Write 模块。

**数据类型：** `SoCData`
### 输出

### **data** — 输出数据数值向量

输出数据，以数值向量形式返回。该模块将接收到的输入消息转换为数据信号。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `To output port`。

**数据类型：** `uint32` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `Boolean` | `fixedpoint`

### **length** — 输出数据长度 非负标量

输出数据的长度，以非负标量形式返回。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `To output port`。

**数据类型：** `double`

### **valid** — 有效数据指示 `Boolean` 标量

控制信号，指示输出数据是否有效。当此值为 `1`（true）时，输出 **data** 端口上的值有效。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `To output port`。

**数据类型：** `Boolean`

### **done** — 数据流完成 `Boolean` 标量

当 **done** 为 `1` 时，该模块没有更多流输出数据可在 **data** 端口中返回。当 **done** 为 `0` 时，该模块还有更多流数据可在 **data** 端口中返回。

#### 依赖关系

要启用此端口，请将 **Device type** 参数设置为 `Stream`。

**数据类型：** `Boolean`

### **event** — 任务事件信号 标量

此端口发送任务事件信号，触发 Task Manager 模块执行关联的事件驱动任务。

#### 依赖关系

要启用此端口，请将 **Show port** 参数设置为 `Data and Event`。

**数据类型：** `rteEvent`
## 参数
```yaml
parameters:
- name: Output
  summary: 模块输出数据的接收端 To file（默认）| To output port | To terminator
  group: ''
- name: Device type
  summary: 设备类型选择 UDP（默认）| TCP | Register | Stream
  group: ''
- name: Show port
  summary: 启用输出端口 Data（默认）| Data and Event
  group: ''
- name: Number of buffers
  summary: 数据缓冲区数量 8（默认）| 非负标量
  group: ''
- name: Sample time
  summary: 采样时间间隔 -1（默认）| 非负数值标量
  group: ''
- name: Dataset name
  summary: 数据文件的名称 无默认值 | 文件路径
  group: ''
- name: Source name
  summary: 数据集名称 无默认值
  group: ''
- name: Data type
  summary: 输出数据的数据类型 uint32（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | boolean | fixedpoint
  group: ''
```

### **Output** — 模块输出数据的接收端 `To file`（默认）| `To output port` | `To terminator`

通过选择以下值之一来设置模块输出数据的接收端。

- `To file` — 将输出数据保存到文件。
- `To output port` — 通过模块上的输出端口输出数据和信号。
- `To terminator` — 终止接收到的输入信号。

### **Device type** — 设备类型选择 `UDP`（默认）| `TCP` | `Register` | `Stream`

选择设备类型以启用相应的输入数据端口。

- `UDP` — 启用 **msg** 输入端口，以消息形式从 UDP Write 模块的 **msg** 端口接收 UDP 数据。
- `TCP` — 启用 **msg** 输入端口，以消息形式从 TCP Write 模块的 **msg** 端口接收 TCP 数据。
- `Register` — 启用 **msg** 输入端口，以消息形式从 Register Write 模块的 **msg** 端口接收 Register 数据。
- `Stream` — 启用 **msg** 输入端口，以消息形式从 Stream Write 模块的 **msg** 端口接收 Stream 数据。

### **Show port** — 启用输出端口 `Data`（默认）| `Data and Event`

选择以下值之一以启用朝向写入源的相应输出端口。

- `Data` — 仅启用 **msg** 输入端口。
- `Data and event` — 启用 **msg** 输入端口和 **event** 输出端口。

### **Number of buffers** — 数据缓冲区数量 `8`（默认）| 非负标量

指定要存储在数据队列中的数据元素数量。此参数必须与 Memory Channel 模块中指定的 **Number of buffers** 参数匹配。

#### 依赖关系

要启用此参数，请将 **Device type** 参数设置为 `Stream`。

### **Sample time** — 采样时间间隔 `-1`（默认）| 非负数值标量

指定模块输出数据的离散时间间隔，以秒为单位。默认值 `-1` 从用于仿真模型的求解器继承采样时间。

### **Dataset name** — 数据文件的名称 无默认值 | 文件路径

指定主机 PC 上要保存文件的完整路径。此模块将输出数据保存为 TGZ 文件。您可以使用 IO Data Source 模块将此文件导入模型。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为 `To file`。

### **Source name** — 数据集名称 无默认值

为输出数据源指定一个名称，用于将数据保存在数据集文件中。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为 `To file`。

### **Data type** — 输出数据的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `boolean` | `fixedpoint`

选择输出数据的数据类型。此值必须与输入数据的数据类型匹配。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为 `To file` 或 `To output port`。
## 所属库

SoC Blockset / I/O Data Source and Sink

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 不为该模块生成代码。在生成的代码中，设备 I/O 直接连接到 TCP Write、UDP Write 或 Register Write 模块。

## 版本历史

**在 R2019a 中引入**

## 描述

记录、输出或终止输入消息

IO Data Sink 模块记录、输出或终止接收到的输入消息信号。此模块的输入连接到 TCP Write、UDP Write 或 Register Write 模块的输出。此模块使您能够将接收到的输入数据保存到文件中，您可以使用模型中的 IO Data Source 模块回放该文件。您还可以终止信号，或通过输出端口输出信号，该信号可作为 IO Data Source 模块的输入。
