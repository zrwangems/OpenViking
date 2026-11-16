---
type: simulink-block
title: 'AXI4 Video Frame Buffer'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Memory Model'
documentation_page: 'axi4videoframebuffer'
documentation_source_path: 'ref/axi4videoframebuffer.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4 Video Frame Buffer

## 端口

### 输入

### **wrData** — 写入器数据总线信号 scalar | vector | matrix

该信号包含要写入存储器的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **wrCtrlIn** — 写入器输入控制信号总线

此端口表示从数据生产者到存储器通道的协议。
AXI4 Video Frame Buffer 模块在使用 **wrData** 时检查此信号。要创建此控制总线，请使用 SoC Bus Creator 模块。有关总线类型的详细信息，请参阅 External Memory Channel Protocols。

**数据类型：** `pixelcontrol`

### **rdCtrlIn** — 读取器输入控制信号总线

此端口接受来自数据使用者模块的总线，指示该使用者模块已准备好接受读取数据。**rdCtrlIn** 端口是从数据使用者到存储器的背压信号。要创建此控制总线，请使用 SoC Bus Creator 模块。

**数据类型：** `StreamVideoFSyncS2MBusObj`

### 输出

### **rdData** — 输出到数据使用者的数据信号 scalar | vector | matrix

该信号包含从存储器读取的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `SoCData`

### **rdCtrlOut** — 从存储器通道到数据使用者的读取器控制信号总线

此总线表示从存储器通道到数据使用者的协议总线。要将信号从总线中分离出来，请使用 SoC Bus Selector 模块。

**数据类型：** `pixelcontrol`

### **wrCtrlOut** — 从存储器通道到数据生产者的写入器控制信号总线

此总线表示从存储器通道到数据生产者的协议总线。要将信号从总线中分离出来，请使用 SoC Bus Selector 模块。

**数据类型：** `StreamVideoS2MBusObj`

## 参数

### **Memory simulation** — 设置仿真时序精度 `Burst accurate`（默认） | `Protocol accurate` | `Behavioral`

Memory simulation 提供三个级别的时序分辨率。请选择以下选项之一：

- **Burst accurate** — 仿真存储器争用和高分辨率时序。
- **Protocol accurate** — 仿真 AXI4 协议握手序列和低分辨率时序。
- **Behavioral** — 仅仿真数据事务，不仿真时序。

### 主要

### **Memory selection** — 在存储器区域之间选择 `PS memory`（默认） | `PL memory`

在处理子系统 (PS) 存储器或编程逻辑 (PL) 存储器之间选择。

- 如果所选开发板仅支持 PL 存储器，则默认值为 `PL memory`。
- 如果所选开发板仅支持 PS 存储器或仅支持 PL 存储器，则此参数为只读。
- 如果所选开发板不是受支持的 SoC 开发板，则此参数不可见。

### **Region size (bytes)** — 已分配存储器区域的大小，以 bytes 为单位 只读：计算所得

此参数为只读。

区域的大小，以 bytes 为单位。此值计算为帧数乘以帧大小再乘以数据大小。可通过在 **主要** 选项卡上设置 **Frame size** 和 **Number of Frames** 参数，以及在 **信号属性** 选项卡上设置 **Data type** 和 **Dimensions** 参数来定义此值。

**示例：** 软件帧大小为 1024 uint32 时，定义 4096 bytes 的缓冲区。如果缓冲区数设置为 2，则区域大小为 8192 bytes。

### **Frame size** — 帧维度 `1080p HDTV (1920x1080p)`（默认）

在组合框中选择或输入帧大小。

从列表中选择帧格式，或将帧维度输入为 2 元素向量，例如 `[1920 1080]`。

- `480p SDTV (720x480p)`
- `576p SDTV (720x576p)`
- `720p HDTV (1280x720p)`
- `1080p HDTV (1920x1080p)`
- `160x120p`
- `320x240p`
- `640x480p`
- `800x600p`
- `1024x768p`
- `1280x768p`
- `1280x1024p`
- `1360x768p`
- `1400x1050p`
- `1600x1200p`
- `1680x1050p`
- `1920x1200p`

### **Number of Frames** — 区域中的缓冲区数量 3（默认） | integer

定义存储器中的视频帧数。

存储器访问采用环形缓冲区模式。只要缓冲区可用，写入器就可以连续写入。当缓冲区完成时，它可供读取器使用。写入器和读取器以循环模式遍历这些缓冲区。只要写入器和读取器保持相近的速率，缓冲就可以防止阻塞。

读取器与写入器之间的速率差异会使较快的设备变慢。例如，较慢的读取器会导致写入器耗尽缓冲区并阻塞写入器，从而有效地将写入器减慢到读取器的速率。同样，较慢的写入器会导致读取器耗尽缓冲区并阻塞读取器，从而有效地将读取器减慢到写入器的速率。

**Number of Frames** 参数必须是 3 到 64 之间的整数。

### **Burst length** — 存储器事务的突发长度 256（默认） | scalar

此连接在存储器总线上的突发长度，以标量数据为单位。标量单位是打包数据类型。为写入器和读取器对该通道的访问指定突发大小。

通道数据始终使用突发事务传输到存储器模型。对于 AXI4 配置，算法逻辑负责通过协议信号定义突发。

**Burst length** 参数确定到存储器的突发大小，而 **rdData** 信号定义接口上每次传输的大小。

### **FIFO depth (number of bursts)** — 数据 FIFO 的深度 `8`（默认） | scalar

指定数据 FIFO 的深度，以突发为单位。当写入器没有可写入的缓冲区时，FIFO 可以吸收数据，直到有缓冲区可用。此值是 FIFO 在丢弃数据之前可以缓冲的最大突发数。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### **FIFO almost-full depth (number of bursts)** — 断言背压时的 FIFO 深度 `6`（默认） | scalar

指定一个数值，用于断言从通道到数据源的背压信号。为避免丢弃数据，请设置一个高水位标记，使数据生产者有足够时间对背压做出反应。此数值必须小于 FIFO 深度。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### **Clock frequency (MHz)** — 管理器数据路径的互连频率 `100`（默认）

指定管理器数据路径的频率，以 MHz 为单位。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### **Data width (bits)** — 管理器数据路径的数据宽度 `64`（默认） | scalar

指定管理器数据路径到互连控制器的数据宽度，以 bits 为单位。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

### 信号属性

#### 数据信号

### **Dimensions** — 视频数据的维度 `[1 3]`（默认） | scalar | vector

将视频数据的维度指定为整体标量或向量。

**示例：** `[1 3]` — 一个像素由三个值表示（分别对应红色、绿色和蓝色）。

**示例：** `[1080 1920 3]` — 一个 1080p 帧。该帧包含 1080 行，每行 1920 个像素，每个像素由三个值表示（分别对应红色、绿色和蓝色）。

### **Data type** — 视频像素的数据类型 uint8（默认） | uint16 | uint32 | uint64 | `fixdt(1,16,0)`

指定视频像素的数据类型。如需帮助，请点击 **...** 按钮并选择 **Data Type Assistant**。默认情况下，此值设置为从源信号继承数据类型。

### **Sample time** — 采样的时间间隔 1（默认） | positive scalar | vector

指定时间间隔，以 seconds 为单位，以定义模块的更新频率。

如果不希望输出具有时间偏移，请将 **Sample time** 参数指定为标量。要向输出添加时间偏移，请将 **Sample time** 参数指定为 `1`×`2` 向量，其中第一个元素是采样周期，第二个元素是偏移量。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

### **Enable sample packing (last signal dimension as channel)** — 在信号的最后一个维度上打包数据 `on`（默认） | `off`

选择此参数可启用跨信号最后一个维度的数据打包。例如，如果通道数据类型为 `uint32`，维度为 `[1024 4]`。如果选择此样本打包参数，则存储器通道会生成 1024 个 128 bits 的读取或写入事务。如果清除此样本打包参数，则存储器通道会生成 4096 个每个 32 bits 的事务。

下图显示了数据类型为 `fixdt10[4x3]` 的信号的数据对齐方式。当数据被打包时，三个 10-bit 字被串联并扩展 2 bits，形成 32-bit 字。当数据未被打包时，每个 10-bit 字被扩展为 16-bit 字。

顶行显示打包数据按 10、10、10 和 2 的样本对齐以构成 32 bits。底行显示未打包数据按 10 和 6 的样本对齐以构成 16 bits。

下图显示了数据类型为 `uint8[8x3]` 的信号的数据对齐方式。当数据被打包时，三个 8-bit 字被串联并扩展 8 bits，形成 32-bit 字。当数据未被打包时，每个 8-bit 字表示为一个 8-bit 样本。

顶行显示打包数据按 8、8、8 和 8 的样本对齐以构成 32 bits。底行显示未打包数据按 8 bits 的样本对齐。

展平信号的总宽度不得超过 512 bits。

### **Inherit sample time offset** — 使读取器从写入器继承采样时间 `on`（默认） | `off`

选中此框可使读取器从写入器继承采样时间偏移。清除此框可使用与写入器不同的采样时间偏移。有关采样时间偏移的详细信息，请参阅 Sample Time Offset。

### **Use pixel clock sample times** — 使用像素时钟采样时间 off（默认） | on

选中此框可使用像素时钟采样时间。要使用像素时钟采样时间，必须使用标量像素维度。像素时钟采样时间仅在流式传输像素时相关。如果读取器和写入器都在流式传输帧，则选中此框时会出错。

### 性能

#### 本地管理器

### **View performance plots** — 显示性能指标按钮

点击该按钮将在新窗口中打开本地管理器的性能图。有关性能图的详细信息，请参阅 Memory Channel Latency Plots。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

#### Memory Controller

### **View performance plots** — 显示性能指标按钮

点击该按钮将打开 **Performance Plots for Memory Controller** 窗口。然后可以选择绘制带宽、突发或延迟。有关性能图的详细信息，请参阅 Memory Controller Latency Plots。

#### 依赖关系

要启用此参数，请在 **Memory simulation** 下选择 **Burst accurate**。

## 所属库

SoC Blockset / Memory

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

通过外部存储器对两个硬件算法之间的连接进行建模

AXI Video Frame Buffer 模块使用完整视频帧缓冲区，对外部存储器连接两个硬件算法之间的连接进行建模。该协议是带背压的 MathWorks® 流式像素协议。此外，读取器可以通过断言 FSYNC 协议信号来确保帧缓冲区与下游视频时序同步。数据路径包括 Video-DMA (VDMA) 引擎，并且外部存储器缓冲区作为完整视频帧的循环缓冲区进行管理。

此模块等效于一个 **Channel type** 参数设置为 `AXI4 Video Frame Buffer` 的 Memory Channel 模块，该模块连接到 Memory Controller 模块。

由于内存控制器对于设计是隐式的，因此可以实例化多个存储器模块，它们通过一个内存控制器连接到同一存储器单元。有效的模块包括：

- AXI4 Random Access Memory
- AXI4-Stream to Software
- Software to AXI4-Stream
- AXI4 Video Frame Buffer
- Memory Traffic Generator

一个模型中的管理器接口最大数量为 16。

Memory Channel 模块连接到 Memory Controller 模块，由 AXI4 Video Frame Buffer 模块替代

有关详细信息，请参阅 AXI4-Stream Video Interface。
