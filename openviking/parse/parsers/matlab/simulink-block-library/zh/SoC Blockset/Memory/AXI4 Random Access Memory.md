---
type: simulink-block
title: 'AXI4 Random Access Memory'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'axi4randomaccessmemory'
documentation_source_path: 'ref/axi4randomaccessmemory.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4 Random Access Memory

## 端口
```yaml
ports:
- name: wrData
  summary: 写入方数据总线信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: rdCtrlIn
  summary: 读取方输入控制信号总线
  direction: input
  data_types: ReadControlM2SBusObj
- name: wrCtrlIn
  summary: 写入方输入控制信号总线
  direction: input
  data_types: WriteControlM2SBusObj
- name: rdData
  summary: 输出到数据消费者的数据信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: rdCtrlOut
  summary: 从存储器通道到数据消费者的读取方控制信号 总线
  direction: output
  data_types: ReadControlS2MBusObj
- name: wrCtrlOut
  summary: 从存储器通道到数据生产者的写入方控制信号 总线
  direction: output
  data_types: WriteControlS2MBusObj
```

### 输入

### **wrData** — 写入方数据总线信号 标量 | 向量 | 矩阵

此信号包含要写入存储器的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **rdCtrlIn** — 读取方输入控制信号总线

此端口接受来自数据消费者模块的控制总线，表示消费者模块已准备好接受读取数据。此输入是来自读取方的读取请求。要创建控制总线，请使用 SoC Bus Creator 模块。

**数据类型：** `ReadControlM2SBusObj`

### **wrCtrlIn** — 写入方输入控制信号总线

此端口接受来自数据生产者模块的控制总线，表示生产者模块已准备好发送数据。此输入是来自写入方的写入请求。要创建控制总线，请使用 SoC Bus Creator 模块。

**数据类型：** `WriteControlM2SBusObj`
### 输出

### **rdData** — 输出到数据消费者的数据信号 标量 | 向量 | 矩阵

此信号包含从存储器读取的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **rdCtrlOut** — 从存储器通道到数据消费者的读取方控制信号 总线

此总线表示从存储器通道到数据消费者的协议总线。要从总线中分离信号，请使用 SoC Bus Selector 模块。

**数据类型：** `ReadControlS2MBusObj`

### **wrCtrlOut** — 从存储器通道到数据生产者的写入方控制信号 总线

此总线表示从存储器通道到数据生产者的协议总线。要从总线中分离信号，请使用 SoC Bus Selector 模块。

**数据类型：** `WriteControlS2MBusObj`
## 参数
```yaml
parameters:
- name: Memory simulation
  summary: 设置仿真时序精度 Burst accurate（默认）| Protocol accurate
  group: ''
- name: Memory selection
  summary: 在存储器区域之间选择 PS memory（默认）| PL memory
  group: 主要
- name: Region size (bytes)
  summary: 缓冲区大小，以字节为单位 4096（默认）| 标量
  group: 主要
- name: Initialize memory content
  summary: 为仿真初始化存储器 off（默认）| on
  group: 主要
- name: Initial value
  summary: 初始存储器值 0（默认）| 标量 | 向量
  group: 主要
- name: Log memory content
  summary: 记录存储器内容 off（默认）| on
  group: 主要
- name: Log variable name
  summary: 内存日志字符串的变量名称 | 字符向量
  group: 主要
- name: Dimensions
  summary: 输入数据信号的维度 标量 | 数组
  group: 信号属性
- name: Data type
  summary: 写入器数据的数据类型 uint32（默认）| double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | boolean | 定点
  group: 信号属性
- name: Sample time
  summary: 采样时间间隔 1（默认）| 正标量 | 向量
  group: 信号属性
- name: Enable sample packing (last signal dimension as channel)
  summary: 在信号的最后一个维度上打包数据 off（默认）| on
  group: 信号属性
- name: Output data signal matches input
  summary: 读取器和写入器使用相同的值 on（默认）| off
  group: 信号属性
- name: Dimensions
  summary: 输出数据信号的维度 标量 | 数组
  group: 信号属性
- name: Data type
  summary: 读取器数据的数据类型 uint32 (默认) | double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | boolean | fixed
    point
  group: 信号属性
- name: Sample time
  summary: 采样时间间隔 1 (默认) | 正标量 | 向量
  group: 信号属性
- name: Enable sample packing (last signal dimension as channel)
  summary: 在信号的最后一个维度上打包数据 off (默认) | on
  group: 信号属性
- name: View performance plots
  summary: 显示性能指标 按钮
  group: 性能
```

### **Memory simulation** — 设置仿真时序精度 `Burst accurate`（默认）| `Protocol accurate`

存储器仿真提供两个级别的时序分辨率。选择以下选项之一：

- **Burst accurate** — 仿真存储器争用和高分辨率时序。
- **Protocol accurate** — 仿真 AXI4 协议握手时序和低分辨率时序。

### 主要

### **Memory selection** — 在存储器区域之间选择 `PS memory`（默认）| `PL memory`

在处理子系统（PS）或可编程逻辑（PL）存储器之间选择。

- 如果所选板卡仅支持 PL 存储器，则默认值为 `PL memory`。
- 如果所选板卡仅支持 PS 存储器或仅支持 PL 存储器，则此参数为只读。
- 如果所选板卡不是受支持的 SoC 板卡，则此参数不可见。

### **Region size (bytes)** — 缓冲区大小，以字节为单位 4096（默认）| 标量

指定存储器缓冲区的大小，以字节为单位。

### **Initialize memory content** — 为仿真初始化存储器 `off`（默认）| `on`

选择此参数以启用仿真前存储器初始化。

### **Initial value** — 初始存储器值 0（默认）| 标量 | 向量

为存储器仿真指定初始值，可以是以下之一：

- 0–255 之间的整数标量值 — 模块将此值复制并加载到所有存储器位置。
- `uint8` 向量 — 模块将向量的每个元素写入一个存储器位置。

  - 如果向量小于存储器区域，则用零填充向量以匹配存储器区域的大小。
  - 如果向量大于存储器区域，则截断向量以匹配存储器区域的大小。

**示例：** `0` — 将所有存储器位置初始化为零。

**示例：** `1:10` — 将前十个存储器位置初始化为值 1–10，其他位置初始化为零。

#### 依赖关系

要启用此参数，请选择 **Initialize memory**。

### **Log memory content** — 记录存储器内容 `off`（默认）| `on`

选择此参数以启用仿真后存储器记录。

### **Log variable name** — 内存日志字符串的变量名称 | 字符向量

用于保存内存内容数据的变量名称，指定为字符串或字符向量。

**示例：** `'mem_content'`

#### 依赖关系

要启用此参数，请选择 **Log memory ending value**。

### 信号属性

#### 写数据信号

### **Dimensions** — 输入数据信号的维度 标量 | 数组

**wrData** 可以是多维数组。将数组的维度指定为整数。

**示例：** 1 — 标量样本。

**示例：** [10 1] — 十个标量的向量。

**示例：** [1080 1920 3] — 1080p 帧。该帧包含 1080 行，每行 1920 个像素，每个像素由三个值表示（分别对应红色、绿色和蓝色）。

### **Data type** — 写入器数据的数据类型 uint32（默认）| double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | boolean | 定点

指定 **wrData** 端口的数据类型。如需帮助，请点击 **...** 按钮并选择 **Data Type Assistant**。

### **Sample time** — 采样时间间隔 1（默认）| 正标量 | 向量

以秒为单位指定时间间隔，以定义模块的更新频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要为输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素为采样周期，第二个元素为偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

### **Enable sample packing (last signal dimension as channel)** — 在信号的最后一个维度上打包数据 `off`（默认）| `on`

选择此参数可启用跨信号最后一个维度的数据打包。AXI4-Random Access Memory 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`。如果选择此样本打包参数，则内存通道生成 1024 个 128 位的读或写事务。如果清除此样本打包参数，则内存通道生成 4096 个 32 位的事务。

下图展示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据被打包时，三个 10 位字被拼接并扩展 2 位，组成一个 32 位字。当数据未被打包时，每个 10 位字被扩展为一个 16 位字。

顶行显示打包数据按 10、10、10 和 2 的样本对齐，组成 32 位。底行显示未打包数据按 10 和 6 的样本对齐，组成 16 位。

下图展示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据被打包时，三个 8 位字被拼接并扩展 8 位，组成一个 32 位字。当数据未被打包时，每个 8 位字表示为 8 位样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐，组成 32 位。底行显示未打包数据按 8 位样本对齐。

展平信号的组合宽度不得超过 512 位。

#### 读数据信号

### **Output data signal matches input** — 读取器和写入器使用相同的值 on（默认）| off

选中此框可为此通道的读取器和写入器使用相同的维度和数据类型。清除此框可为读取器和写入器接口自定义不同的维度和数据类型。

### **Dimensions** — 输出数据信号的维度 标量 | 数组

**rdData** 可以是多维数组。将数组的维度指定为整数。

**示例：** 1 — 标量样本。

**示例：** [10 1] — 十个标量的向量。

**示例：** [1080 1920 3] — 1080p 帧。该帧包含 1080 行，每行 1920 个像素，每个像素由三个值表示（分别对应红色、绿色和蓝色）。

### **Data type** — 读取器数据的数据类型 uint32 (默认) | double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | boolean | fixed point

指定 **rdData** 端口的数据类型。如需帮助，请点击 **...** 按钮并选择 **Data Type Assistant**。

#### 依赖关系

要启用此参数，请清除 **Output data signal matches input** 复选框。

### **Sample time** — 采样时间间隔 1 (默认) | 正标量 | 向量

以秒为单位指定时间间隔，以定义模块的更新频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要为输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink 中采样时间的详细信息，请参阅 Specify Sample Time。

#### 依赖关系

要启用此参数，请清除 **Output data signal matches input** 复选框。

### **Enable sample packing (last signal dimension as channel)** — 在信号的最后一个维度上打包数据 `off` (默认) | `on`

选择此参数可启用跨信号最后一个维度的数据打包。AXI4 Random Access Memory 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`。如果选择此样本打包参数，则内存通道会生成 1024 个 128 位的读或写事务。如果清除此样本打包参数，则内存通道会生成 4096 个 32 位的事务。

下图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据被打包时，三个 10 位字被串联并通过 2 位扩展为 32 位字。当数据未被打包时，每个 10 位字被扩展为 16 位字。

顶行显示打包数据按 10、10、10 和 2 的样本对齐以构成 32 位。底行显示未打包数据按 10 和 6 的样本对齐以构成 16 位。

下图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据被打包时，三个 8 位字被串联并通过 8 位扩展为 32 位字。当数据未被打包时，每个 8 位字表示为 8 位样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐以构成 32 位。底行显示未打包数据按 8 位样本对齐。

展平信号的组合宽度不得超过 512 位。

#### 依赖关系

要启用此参数，请清除 **Output data signal matches input** 复选框。

### 性能

### **View performance plots** — 显示性能指标 按钮

点击该按钮将打开 **Performance Plots for Memory Controller** 窗口。然后您可以选择绘制带宽、突发或延迟图。有关性能图的详细信息，请参阅 Memory Controller Latency Plots。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。
## 所属库

SoC Blockset / Memory

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

### R2023a：新增对内存初始化和日志记录的支持

您现在可以在仿真前加载初始值，或在仿真后记录内存内容。

- 要初始化内存，请打开模块封装并在主选项卡中选择 **Initialize memory**。然后，在 **Initial value** 框中指定初始值。
- 要在仿真后记录内存内容，请打开模块封装并在主选项卡中选择 **Log memory ending value**。然后，在 **Initial value** 框中指定初始值。

### R2023a: **Buffer size** 和 **Region size** 参数已合并

在之前的版本中，您可以在 **Buffer size** 框中指定内存区域的大小，该值会反映为只读的 **Region size** 参数。在 R2023a 中，请在 **Region size (bytes)** 参数中指定该大小。

## 描述

对外部内存的随机访问进行建模

AXI4 Random Access Memory 模块使用 MathWorks® 简化 AXI4 manager 协议，对外部内存连接两个硬件算法之间的通信进行建模。写入端和读取端都是 manager，通过该模块向内存发送读请求和写请求。外部内存是非托管的（无逻辑缓冲区，无循环缓冲区）。为确保数据完整性，读取端和写入端会协调访问时序。

该模块等效于将 Memory Channel 模块的 **Channel type** 参数设置为 `AXI4 Random Access` 并连接到 Memory Controller 模块。

由于内存控制器是该设计的隐式组成部分，您可以实例化多个内存模块，通过内存控制器连接到同一内存单元。有效的模块包括：

- AXI4 Random Access
  Memory
- AXI4-Stream to
  Software
- Software to
  AXI4-Stream
- AXI4 Video Frame
  Buffer
- Memory Traffic
  Generator

一个模型中 manager 接口的最大数量为 16。

Memory Channel 模块连接到 Memory Controller 模块，已由 AXI4 Random Access Memory 模块替代

有关详细信息，请参阅 Simplified AXI4 Master Interface。
