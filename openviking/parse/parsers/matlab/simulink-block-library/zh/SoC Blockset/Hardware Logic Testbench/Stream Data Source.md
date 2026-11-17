---
type: simulink-block
title: 'Stream Data Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'streamdatasource'
documentation_source_path: 'ref/streamdatasource.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Data Source

## 端口
```yaml
ports:
- name: wrCtrlIn
  summary: 输入控制总线 bus
  direction: input
  data_types: StreamS2MBusObj
- name: wrData
  summary: 输出流数据 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: wrCtrlOut
  summary: 输出控制总线 bus
  direction: output
  data_types: StreamM2SBusObj
```

### 输入

### **wrCtrlIn** — 输入控制总线 bus

来自数据消费者的控制总线，用于指示数据消费者已准备好接受流数据。该控制总线包含一个 ready 信号。

**数据类型：** `StreamS2MBusObj`
### 输出

### **wrData** — 输出流数据 标量 | 向量

输出到数据消费者的流数据。该值以标量或向量形式返回。

您可以更改输出流数据的数据类型。有关详细信息，请参阅 **Data type** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlOut** — 输出控制总线 bus

输出到数据消费者的控制总线，以 bus 形式返回。该控制总线包含以下控制信号：

- `valid` — 指示 **wrData** 输出端口上的输出数据有效
- `tlast` — 指示数据事务结束

**数据类型：** `StreamM2SBusObj`
## 参数
```yaml
parameters:
- name: Data type
  summary: 输出数据类型 uint8（默认）| double | single | int8 | int16 | int32 | int64 | uint16 | uint32 | uint64 | fixdt(1,16,0)
  group: ''
- name: Dimensions
  summary: 输出数据维度 10（默认）| 正整数 | 数组
  group: ''
- name: Burst length
  summary: 单次 burst 的长度 20（默认）| 正整数
  group: ''
- name: Total bursts
  summary: burst 总数 4（默认）| 正整数
  group: ''
- name: Data generation
  summary: 输出生成类型 counter（默认）| random | ones | workspace
  group: ''
- name: Counter init value
  summary: 计数器初始值 0（默认）| 标量
  group: ''
- name: Variable name
  summary: 工作区变量名称 simOut（默认）| 任何 MATLAB 支持的变量名
  group: ''
- name: Sample time
  summary: 采样时间间隔 1（默认）| 正标量 | 向量
  group: ''
- name: 传输延迟（以采样数为单位）
  summary: 突发之间的延迟 0（默认）| 非负整数
  group: ''
```

### **Data type** — 输出数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixdt(1,16,0)`

选择输出流数据的数据类型格式。

单击 按钮以显示 **Data Type Assistant**，它可帮助您为 **wrData** 输出端口设置数据类型。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Dimensions** — 输出数据维度 `10`（默认）| 正整数 | 数组

将输出流数据的维度指定为正标量或数组。

**示例：** `1` 指定标量样本。

**示例：** `[10 1]` 指定包含十个标量的向量。

### **Burst length** — 单次 burst 的长度 `20`（默认）| 正整数

单次 burst 的长度，指定为正整数。

### **Total bursts** — burst 总数 `4`（默认）| 正整数

该模块生成的 burst 总数，指定为正整数。

### **Data generation** — 输出生成类型 `counter`（默认）| `random` | `ones` | `workspace`

将输出的生成类型指定为以下值之一：

- `counter` — 基于所选数据类型从计数器生成数据。
- `random` — 生成随机数据。
- `ones` — 基于所选数据类型生成所有位均为 1 的数据。
- `workspace` — 从 MATLAB® 工作区生成数据。

### **Counter init value** — 计数器初始值 `0`（默认）| 标量

指定计数器开始的值。计数器值的有效范围取决于为 **Data type** 参数选择的值。如果该值超出有效范围，则会舍入到最近的有效值。

例如，如果 **Data type** 为 `uint8`，而该值为 `6.787`，则该值会舍入为 `7`。

#### 依赖关系

要启用此参数，请将 **Data generation** 参数设置为 `counter`。

### **Variable name** — 工作区变量名称 `simOut`（默认）| 任何 MATLAB 支持的变量名

指定从中生成输出流数据的变量名称。此参数可以是任何 MATLAB 支持的变量名。

**注意**

工作区变量必须是数值数组。

#### 依赖关系

要启用此参数，请将 **Data generation** 参数设置为 `workspace`。

### **Sample time** — 采样时间间隔 1（默认）| 正标量 | 向量

指定以秒为单位的时间间隔，以定义模块更新的频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要向输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

### **传输延迟（以采样数为单位）** — 突发之间的延迟 `0`（默认）| 非负整数

下一次突发发生之后的时间。此值必须为非负整数。
## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

生成连续流数据

Stream Data Source 模块向基于高级可扩展接口 AXI4 的流数据接口模块生成流数据。您可以将此模块用作测试源模块，用于仿真基于 AXI4 的流数据应用。

该模块接受控制总线，并输出流数据以及控制总线。
