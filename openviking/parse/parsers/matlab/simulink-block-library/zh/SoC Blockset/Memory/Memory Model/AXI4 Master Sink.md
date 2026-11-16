---
type: simulink-block
title: 'AXI4 Master Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Memory Model'
documentation_page: 'axi4mastersink'
documentation_source_path: 'ref/axi4mastersink.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4 Master Sink

## 端口

### 输入

### **rdData** — 输入数据 标量 | 向量

来自数据源的输入数据。此值必须为标量或向量。

在读取数据之前，请设置所需的数据类型。要设置数据类型，请参阅 **Data type** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdCtrlIn** — 输入控制总线 bus

来自数据生产者的输入控制总线，指定为 bus。此控制总线包含以下控制信号：

- `rd_aready` — 指示数据源已接受读请求
- `rd_dvalid` — 指示为读请求返回的数据有效

**数据类型：** `ReadControlS2MBusObj`
### 输出

### **rdCtrlOut** — 输出控制总线 bus

发往数据源的输出控制总线，指示模块已准备好接受数据，以标量形式返回。此控制总线包含以下控制信号：

- `rd_addr` — 读事务的起始地址，在事务的第一个周期采样
- `rd_len` — 要读取的数据值数量，在事务的第一个周期采样
- `rd_avalid` — 指定读请求是否有效的控制信号
- `rd_dready` — 指示模块何时可以读取数据的控制信号

**数据类型：** `ReadControlM2SBusObj`

## 参数

### **Data type** — 输入数据类型 `uint8` (default) | `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

选择输入 AXI 数据的数据类型格式。

单击 按钮以显示 **Data Type Assistant**，它可帮助您为 **rdData** 输入端口设置数据类型。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Dimensions** — 输入数据维度 `1` (default) | positive integer | array

将输入数据的维度指定为正标量或数组。此值定义数据信号的大小。

**示例：** `1` 指定标量样本。

**示例：** `[10 1]` 指定十个标量的向量。

### **Enable sample packing (last signal dimension as channel)** — 在信号的最后一个维度上打包数据 `off` (default) | `on`

选择此参数可启用沿信号最后一个维度的数据打包。Memory Channel 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`，并且您选择此参数，则 memory channel 会生成 1024 个 128 bits 的读或写事务。对于此示例，如果您清除此样本打包参数，则 memory channel 会生成 4096 个 32 bits 的事务。

下图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据被打包时，三个 10-bit 字被串联，并扩展 2 bits 成为 32-bit 样本。当数据未被打包时，每个 10-bit 字被扩展为 16-bit 样本。

顶行显示打包数据按 10、10、10 和 2 的样本对齐，以构成 32 bits。底行显示未打包数据按 10 和 6 的样本对齐，以构成 16 bits。

下图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据被打包时，三个 8-bit 字被串联，并扩展 8 bits 成为 32-bit 样本。当数据未被打包时，每个 8-bit 字表示为 8-bit 样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐，以构成 32 bits。底行显示未打包数据按 8 bits 的样本对齐。

展平后的信号合并宽度不得超过 512 bits。

### **Number of transfers** — 要发送的读请求数量 `1` (default) | positive integer

指定模块要发送的读请求数量。

### **Initial address** — 起始地址 `0` (default) | nonnegative scalar integer

指定模块从中读取数据的地址。此值必须为非负整数。

### **Initial delay** — 初始延迟 `0` (default) | nonnegative scalar

指定初始时间，经过该时间后读取操作开始。

### **Sample time** — 采样时间间隔 1 (default) | positive scalar | vector

指定以 seconds 为单位的时间间隔，以定义模块更新的频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要为输出添加时间偏移，请将 **Sample time** 参数指定为 `1`-by-`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

### **Save data in workspace** — 保存到工作区 `off` (default) | `on`

选择此参数可将输入数据保存到 MATLAB® 工作区。

### **Variable name** — 工作区变量名称 `simOut` (default) | any MATLAB-supported variable name

指定输入数据保存到的工作区变量。此参数可以是任何 MATLAB 支持的变量名称。

#### 依赖关系

要启用此参数，请选择 **Save data in workspace** 参数。

## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

接收随机存取存储器数据

AXI4 Master Sink 模块从基于 AXI4 的数据接口模块接收随机存取存储器数据。您可以将此模块用作测试接收端模块，以仿真基于 AXI4 的数据应用。

该模块接受数据以及控制总线，并输出控制总线。
