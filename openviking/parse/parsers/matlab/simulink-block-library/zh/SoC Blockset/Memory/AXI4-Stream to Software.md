---
type: simulink-block
title: 'AXI4-Stream to Software'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'axi4streamtosoftware'
documentation_source_path: 'ref/axi4streamtosoftware.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Stream to Software

## 端口
```yaml
ports:
- name: wrData
  summary: 写入器数据总线信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: wrCtrlIn
  summary: 写入器输入控制信号总线
  direction: input
  data_types: StreamM2SBusObj
- name: done
  summary: 读取完成通知消息 标量
  direction: input
  data_types: Boolean
- name: event
  summary: 任务读取事件信号 标量
  direction: output
  data_types: rteEvent
- name: msg
  summary: 输出到软件的数据信号 标量 | 向量 | 矩阵
  direction: output
  data_types: SoCData
- name: wrCtrlOut
  summary: 写入器到数据生产者的控制信号总线
  direction: output
  data_types: StreamS2MBusObj
```

### 输入

### **wrData** — 写入器数据总线信号 标量 | 向量 | 矩阵

此信号包含要写入存储器的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **wrCtrlIn** — 写入器输入控制信号总线

此端口表示从数据生产者到处理器的协议。AXI4-Stream to Software 模块在使用 **wrData** 时检查此信号。控制总线上的信号类型为 `StreamM2SBusObj`。要创建此控制总线，请使用 SoC Bus Creator 模块。有关总线类型的更多信息，请参阅 External Memory Channel Protocols。

**数据类型：** `StreamM2SBusObj`

### **done** — 读取完成通知消息 标量

此消息端口接收来自所连接的 Stream Read 模块的通知。该通知表示读取事务已完成。有关消息的更多信息，请参阅 Messages。

**数据类型：** `Boolean`
### 输出

### **event** — 任务读取事件信号 标量

此端口发送任务事件信号，触发 Task Manager 模块执行关联的事件驱动读取。

**数据类型：** `rteEvent`

### **msg** — 输出到软件的数据信号 标量 | 向量 | 矩阵

此信号包含从存储器读取的数据，作为消息发送到所连接的 Stream Read 模块。有关消息的更多信息，请参阅 Messages。

**数据类型：** `SoCData`

### **wrCtrlOut** — 写入器到数据生产者的控制信号总线

此总线表示从存储器通道到数据生产者的协议总线。总线上的信号类型为 `StreamS2MBusObj`。要从总线中分离信号，请使用 SoC Bus Selector 模块。

**数据类型：** `StreamS2MBusObj`
## 参数
```yaml
parameters:
- name: Memory simulation
  summary: 设置仿真时序精度 Burst accurate（默认）| Protocol accurate | Behavioral
  group: ''
- name: Memory selection
  summary: 在存储器区域之间选择 PS memory（默认）| PL memory
  group: 主要
- name: Region size (bytes)
  summary: 已分配存储器区域的大小，以字节为单位 只读：计算得出
  group: 主要
- name: Number of buffers
  summary: 区域中的缓冲区数量 8（默认）| 整数
  group: 主要
- name: Burst length
  summary: 内存事务的突发长度 256（默认）| 标量
  group: 主要
- name: FIFO depth (number of bursts)
  summary: 数据 FIFO 深度 8（默认）| 标量
  group: 主要
- name: FIFO almost-full depth (number of bursts)
  summary: 断言反压时的 FIFO 深度 6（默认）| 标量
  group: 主要
- name: Clock frequency (MHz)
  summary: 管理器数据路径的互连频率 100（默认）
  group: 主要
- name: Data width (bits)
  summary: 管理器数据路径的数据宽度 64（默认）| 标量
  group: 主要
- name: Dimensions
  summary: 输入数据信号的维度 1（默认）| 标量 | 数组
  group: 信号属性
- name: Data type
  summary: 写入方数据的数据类型 uint32（默认）| double | single | int8 | int16 | int32 | int64 | uint8 | uint16 | uint64 | Boolean | fixed
    point
  group: 信号属性
- name: Sample time
  summary: 采样时间间隔 1（默认）| 正标量 | 向量
  group: 信号属性
- name: Enable sample packing (last signal dimension as channel)
  summary: 在信号的最后一个维度上打包数据 off（默认）| on
  group: 信号属性
- name: Dimensions
  summary: 软件数据的维度 标量
  group: 信号属性
- name: Data type
  summary: '软件数据的数据类型 Inherit: Same as input（默认）| uint16 | uint32 | uint64 | fixdt(0,128,0)'
  group: 信号属性
- name: View performance plots
  summary: 显示性能指标 按钮
  group: Performance
- name: View performance plots
  summary: 显示性能指标 按钮
  group: Performance
```

### **Memory simulation** — 设置仿真时序精度 `Burst accurate`（默认）| `Protocol accurate` | `Behavioral`

Memory simulation 提供三个级别的时序分辨率。选择以下选项之一：

- **Burst accurate** — 仿真存储器争用和高分辨率时序。
- **Protocol accurate** — 仿真 AXI4 协议握手时序和低分辨率时序。
- **Behavioral** — 仅仿真数据事务，不仿真时序。

  当此参数设置为 **Behavioral** 模式时，`TLAST` 信号的值将被忽略。

### 主要

### **Memory selection** — 在存储器区域之间选择 `PS memory`（默认）| `PL memory`

在处理子系统（PS）或可编程逻辑（PL）存储器之间选择。

- 如果所选开发板仅支持 PL 存储器，则默认值为 `PL memory`。
- 如果所选开发板仅支持 PS 存储器或仅支持 PL 存储器，则此参数为只读。
- 如果所选开发板不是受支持的 SoC 开发板，则此参数不可见。

### **Region size (bytes)** — 已分配存储器区域的大小，以字节为单位 只读：计算得出

此参数为只读。

区域大小以字节为单位。此值计算为缓冲区数量乘以缓冲区大小。缓冲区大小定义为数据大小乘以软件帧大小。通过在 **Signal Attributes** 选项卡上设置 **Data type** 和 **Dimensions** 参数来定义此值。

**示例：** 软件帧大小为 1024 uint32 定义了 4096 字节的缓冲区。如果缓冲区数量设置为 2，则区域大小为 8192 字节。

### **Number of buffers** — 区域中的缓冲区数量 `8`（默认）| 整数

定义内存中的缓冲区数量。

内存访问采用环形缓冲区模式。只要有可用的缓冲区，写入方就可以持续写入。当一个缓冲区完成后，它就可供读取方使用。写入方和读取方以循环模式遍历缓冲区。只要写入方和读取方保持相似的速率，缓冲就能防止阻塞。

读取方和写入方之间的速率差异会减慢较快设备的速度。例如，慢速读取方会导致写入方耗尽缓冲区并阻塞写入方，从而有效地将写入方减慢到读取方的速率。同样，慢速写入方会导致读取方耗尽缓冲区并阻塞读取方，从而有效地将读取方减慢到写入方的速率。

**Number of buffers** 参数必须是 3 到 64 之间的整数。

### **Burst length** — 内存事务的突发长度 `256`（默认）| 标量

内存总线上此连接的突发长度，以标量数据为单位。标量单位是打包数据类型。为写入方和读取方对通道的访问指定突发大小。

通道数据始终使用突发事务传输到内存模型。对于 AXI4 配置，算法逻辑负责通过协议信号定义突发。

**Burst length** 参数决定到内存的突发大小，**wrData** 信号定义接口上每次传输的大小。

### **FIFO depth (number of bursts)** — 数据 FIFO 深度 `8`（默认）| 标量

指定数据 FIFO 的深度，以突发为单位。当写入方没有可写入的缓冲区时，FIFO 可以吸收数据，直到缓冲区变为可用。此值是 FIFO 在丢弃数据之前可以缓冲的最大突发数。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### **FIFO almost-full depth (number of bursts)** — 断言反压时的 FIFO 深度 `6`（默认）| 标量

指定一个数值，用于断言从通道到数据源的反压信号。为避免丢弃数据，请设置一个高水位标记，使数据生产者有足够的时间对反压做出反应。此数值必须小于 FIFO 深度。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### **Clock frequency (MHz)** — 管理器数据路径的互连频率 `100`（默认）

以 MHz 为单位指定管理器数据路径的频率。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### **Data width (bits)** — 管理器数据路径的数据宽度 `64`（默认）| 标量

以位为单位指定到互连控制器的管理器数据路径的数据宽度。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### 信号属性

#### 流数据信号

### **Dimensions** — 输入数据信号的维度 1（默认）| 标量 | 数组

**wrData** 可以是多维数组。将数组的维度指定为整数。

**示例：** 1 — 一个标量样本。

**示例：** [10 1] — 十个标量的向量。

**示例：** [1080 1920 3] — 一个 1080p 帧。该帧包括 1080 行，每行 1920 个像素，每个像素由三个值表示（红色、绿色和蓝色）。

### **Data type** — 写入方数据的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint64` | `Boolean` | `fixed point`

指定 **wrData** 端口的数据类型。如需帮助，请点击 **...** 按钮并选择 **Data Type Assistant**。

### **Sample time** — 采样时间间隔 1（默认）| 正标量 | 向量

指定一个以秒为单位的时间间隔，以定义模块更新的频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要向输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

### **Enable sample packing (last signal dimension as channel)** — 在信号的最后一个维度上打包数据 `off`（默认）| `on`

选择此参数可启用跨信号最后一个维度的数据打包。AXI4-Stream to Software 模块沿信号的最后一个维度打包数据。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`。如果选择此采样打包参数，则内存通道会生成 1024 个 128 位的读或写事务。如果清除此采样打包参数，则内存通道会生成 4096 个每个 32 位的事务。

此图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据被打包时，三个 10 位字被串联起来，并扩展 2 位成为一个 32 位字。当数据未被打包时，每个 10 位字被扩展为一个 16 位字。

顶行显示打包数据按 10、10、10 和 2 的样本对齐以构成 32 位。底行显示未打包数据按 10 和 6 的样本对齐以构成 16 位。

此图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据被打包时，三个 8 位字被串联起来，并扩展 8 位成为一个 32 位字。当数据未被打包时，每个 8 位字表示为 8 位样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐以构成 32 位。底行显示未打包数据按 8 位样本对齐。

展平信号的组合宽度不得超过 512 位。

#### 软件数据信号

### **Dimensions** — 软件数据的维度 标量

将软件数据（读取器）的维度指定为整数。

默认值为 `1024`。

### **Data type** — 软件数据的数据类型 `Inherit: Same as input`（默认）| `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`

指定软件数据（读取器）的数据类型。如需帮助，请点击 **...** 按钮并选择 **Data Type Assistant**。默认情况下，此值设置为从源信号继承数据类型。

### Performance

#### Local master

### **View performance plots** — 显示性能指标 按钮

点击该按钮会在新窗口中打开本地主设备的性能图。有关性能图的详细信息，请参阅 Memory Channel Latency Plots。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

#### Memory Controller

### **View performance plots** — 显示性能指标 按钮

点击该按钮会打开 **Performance Plots for Memory Controller** 窗口。然后您可以选择绘制带宽、突发或延迟。有关性能图的详细信息，请参阅 Memory Controller Latency Plots。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。
## 所属库

SoC Blockset / Memory

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

### R2023b：支持多个 AXI 流

使用多个 AXI4-Stream to Software、Software to AXI4-Stream 或 Memory Channel 模块，对具有多个流入和流出软件的流的设计进行建模、仿真和部署。在之前的版本中，SoC Blockset™ 仅支持用于建模的多个流。此版本增加了生成二进制文件和软件并将其部署到 SoC 设备上的功能。

## 描述

将 AXI4 数据从 FPGA 流式传输到软件

AXI4-Stream to Software 模块通过外部存储器对硬件逻辑和软件任务之间的连接进行建模。写入器使用 MathWorks® 简化的 AXI 流协议将数据放入通道，读取器（处理器）从 DMA 驱动程序接口获取数据。该模块对该连接的 datapath 和软件栈进行建模，包括 FIFO、DMA 引擎、互连和外部存储器、中断、DMA 驱动程序的 kernel buffer 管理，以及到软件任务的数据传输。

此模块等效于一个 Memory Channel 模块，其 **Channel type** 参数设置为 `AXI4-Stream to Software via DMA`，并连接到一个 Memory Controller 模块。

由于存储器控制器是该设计所隐含的——您可以实例化多个存储器模块，这些模块通过一个存储器控制器连接到同一个存储器单元。有效的模块包括：

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

连接到 Memory Controller 模块的 Memory Channel 模块，由 AXI4-Stream to Software 模块替代

有关 MathWorks 简化 AXI 流协议的更多信息，请参阅 AXI4-Stream Interface。
