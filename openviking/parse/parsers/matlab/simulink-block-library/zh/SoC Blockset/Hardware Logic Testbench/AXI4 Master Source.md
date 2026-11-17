---
type: simulink-block
title: 'AXI4 Master Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'axi4mastersource'
documentation_source_path: 'ref/axi4mastersource.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4 Master Source

## 端口
```yaml
ports:
- name: wrCtrlIn
  summary: 输入控制总线 bus
  direction: input
  data_types: WriteControlS2MBusObj
- name: wrData
  summary: 输出 AXI 数据 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: wrCtrlOut
  summary: 输出控制总线 bus
  direction: output
  data_types: WriteControlM2SBusObj
```

### 输入

### **wrCtrlIn** — 输入控制总线 bus

来自数据使用方的控制总线，用于指示数据使用方已准备好接受数据，指定为标量。该控制总线包含以下控制信号：

- `wr_ready` — 指示模块可以向数据使用方发送数据
- `wr_complete` — 指示写事务已在数据使用方处完成
- `wr_bvalid` — 指示数据使用方已接受该事务

**数据类型：** `WriteControlS2MBusObj`
### 输出

### **wrData** — 输出 AXI 数据 标量 | 向量

向数据使用方输出 AXI 数据。该值以标量或向量形式返回。

您可以更改输出数据的数据类型。有关详细信息，请参阅 **Data type** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlOut** — 输出控制总线 bus

发送至数据使用方的控制总线，以总线形式返回。该控制总线包含以下控制信号：

- `wr_addr` — 指定模块写入的起始地址
- `wr_len` — 指定写事务中数据元素的数量
- `wr_valid` — 指示在 **wrData** 输出端口采样的数据有效

**数据类型：** `WriteControlM2SBusObj`
## 参数
```yaml
parameters:
- name: Data type
  summary: 输出数据类型 uint8（默认）| double | single | int8 | int16 | int32 | int64 | uint16 | uint32 | uint64 | fixed point
  group: ''
- name: Dimensions
  summary: 输出数据维度 1 | 正标量 | 数组
  group: ''
- name: Enable sample packing (last signal dimension as channel)
  summary: 沿信号最后一个维度打包数据 off（默认）| on
  group: ''
- name: Number of transfers
  summary: 要发送的写请求数量 1（默认）| 正整数
  group: ''
- name: Initial address
  summary: 起始地址 0（默认）| 非负整数
  group: ''
- name: Initial delay
  summary: 初始延迟 0（默认）| 非负标量
  group: ''
- name: Data generation
  summary: 输出生成类型 counter（默认）| random | ones | workspace
  group: ''
- name: Counter init value
  summary: 计数器初始值 0（默认）| 标量
  group: ''
- name: Variable name
  summary: 工作区变量名称 simOut（默认）| 任何 MATLAB 支持的变量名称
  group: ''
- name: Sample time
  summary: 采样时间间隔 1（默认）| 正标量 | 向量
  group: ''
```

### **Data type** — 输出数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

选择输出 AXI 数据的数据类型格式。

点击  按钮以显示 **Data Type Assistant**，它可帮助您为 **wrData** 输出端口设置数据类型。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Dimensions** — 输出数据维度 `1` | 正标量 | 数组

将输出数据的维度指定为正标量或数组。该值定义数据信号的大小。

**示例：** `1` 指定一个标量样本。

**示例：** `[10 1]` 指定一个包含十个标量的向量。

### **Enable sample packing (last signal dimension as channel)** — 沿信号最后一个维度打包数据 `off`（默认）| `on`

选择此参数以启用沿信号最后一个维度的数据打包。Memory Channel 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`，并且您选择此参数，则内存通道会生成 1024 个 128 位的读或写事务。对于此示例，如果您清除此样本打包参数，则内存通道会生成 4096 个事务，每个事务为 32 位。

下图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据被打包时，三个 10 位字被串联并通过 2 位扩展为 32 位样本。当数据未被打包时，每个 10 位字被扩展为 16 位样本。

顶行显示打包数据按 10、10、10 和 2 的样本对齐以构成 32 位。底行显示未打包数据按 10 和 6 的样本对齐以构成 16 位。

下图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据被打包时，三个 8 位字被串联并通过 8 位扩展为 32 位样本。当数据未被打包时，每个 8 位字表示为 8 位样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐以构成 32 位。底行显示未打包数据按 8 位样本对齐。

展平信号的总宽度不得超过 512 位。

### **Number of transfers** — 要发送的写请求数量 `1`（默认）| 正整数

指定模块要发送的写请求数量。

### **Initial address** — 起始地址 `0`（默认）| 非负整数

指定模块写入数据的地址。该值必须为非负整数。

### **Initial delay** — 初始延迟 `0`（默认）| 非负标量

指定写入操作开始后的初始时间。此值必须为非负标量。

### **Data generation** — 输出生成类型 `counter`（默认）| `random` | `ones` | `workspace`

将输出的生成类型指定为以下值之一：

- `counter` — 基于所选数据类型从计数器生成数据。
- `random` — 生成随机数据。
- `ones` — 基于所选数据类型生成所有位均为 1 的数据。
- `workspace` — 从 MATLAB® 工作区生成数据。

### **Counter init value** — 计数器初始值 `0`（默认）| 标量

指定计数器开始的值。计数器值的有效范围取决于 **Data type** 参数所选的值。如果此值超出有效范围，则将其舍入到最近的有效值。

例如，如果 **Data type** 为 `uint8`，且此值为 `6.787`，则此值舍入为 `7`。

#### 依赖关系

要启用此参数，请将 **Data generation** 参数设置为 `counter`。

### **Variable name** — 工作区变量名称 `simOut`（默认）| 任何 MATLAB 支持的变量名称

指定从中生成输出数据的工作区变量。此参数可以是任何 MATLAB 支持的变量名称。

**注意**

工作区变量必须为数值数组。

#### 依赖关系

要启用此参数，请将 **Data generation** 参数设置为 `workspace`。

### **Sample time** — 采样时间间隔 1（默认）| 正标量 | 向量

以秒为单位指定时间间隔，以定义模块的更新频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要为输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素为采样周期，第二个元素为偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。
## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

生成随机存取存储器数据

AXI4 Master Source 模块向基于 AXI4 的数据接口模块生成随机存取存储器数据。您可以将此模块用作测试源模块，以仿真基于 AXI4 的数据应用。

该模块接受控制总线，并输出数据以及控制总线。
