---
type: simulink-block
title: 'C28x SCI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xscitransmit'
documentation_source_path: 'ref/c28xscitransmit.html'
language: zh-CN
chinese_source: official
---

# C28x SCI Transmit

## 端口

### 输入

### **Data** — 写入串行总线的数据 标量 | 向量

输入数据写入串行通信总线。

如果 SCI Transmit 的输入端口是可变数据大小，并且可变数据的长度为 `0`，则该模块将只传输头部和终止符。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single`
### 输出

### **Status** — 在给定时间步传输的数据 标量

如果在给定的时间步长传输了数据，则端口输出 `0`。否则，它将输出值 `1`，表示传输 FIFO 已满，数据传输不成功。

#### 依赖关系

要启用此端口，请选择**输出状态**参数。

**数据类型:** `uint8` | `uint16`

## 参数

### **SCI 模块** — SCI 通信模块 **A** (默认) | **B** | **C** | **D**

用于通信的 SCI 模块。

### **附加包头** — 表示数据开始 `'S'` (默认) | 字符串 | char | 0 到 255 之间的数字

位于已发送数据包开头的数据，不属于正在传输的数据，它指示数据的开始。附加包头必须使用 ASCII 字符表示。使用字符串或数字 (0–255)。您必须为该参数输入的字符串添加单引号，但引号不会被发送，也不会计入总字节数。要指定空值（无包头），只需输入两个单引号。

头部的数据类型与模块中提到的数据类型无关。

**注意**

将附加包头或终止符与主机 SCI Receive 模块中指定的包头或终止符进行匹配。

### **附加包终止符** — 表示数据结尾 `'E'` (默认) | 字符串 | char | 0 到 255 之间的数字

位于已发送数据包末尾的数据，不属于正在传输的数据，表示数据结束。附加包终止符必须使用 ASCII 字符表示。使用字符串或数字 (0–255)。必须用单引号将在此字段中输入的字符串括起来，但引号不会被发送，也不会计入总字节数。要指定空值（不带包终止符），只需输入两个单引号。

终止符的数据类型与模块中提到的数据类型无关。

### **帧大小** — 指定要接收的数据长度 `600` (默认) | 任何正整数

指定要传输的数据字节数。当发送速率大于接收速率时，可以使用此参数。

帧大小的计算依据如下：接收速率/发送速率。例如，如果信号以 `50` 微秒传输，帧大小为 `600`，则可以在 `0.03` 秒内接收数据。

当帧大小超过 `1` 时，会在帧的开头和结尾添加额外的包头和终止符。例如，`<Header>DATA(1:frame size)<Terminator>`

其中，`DATA(1:frame size)` 表示要传输的长度为帧大小的信号。

### **等到传输以前的数据** — 等待上一时间步接收到的数据发送完毕。 `on` (默认) | `off`

- `on` - 选择此参数时，传输操作将以阻塞模式运行。在这种模式下，如果发送 FIFO 已满，则会等待先前的数据发送完毕，并检查 FIFO 中是否有空间来发送当前数据。

  如果在下一次发送操作计划开始时，目标硬件仍在等待发送请求的数据，则会发生任务溢出。要解决超时问题，请使用**采样时间**参数增加时间步长。
- `off` - 清除此参数后，传输操作将以非阻塞模式运行。在这种模式下，如果模块仍在传输上一个时间步接收到的数据，则当前时间步输入端口的数据将被丢弃。

  无论哪种模式，如果模块尚未建立发送主机和接收主机之间的连接，或者连接丢失，则输入端口的数据将被丢弃。

### **输出状态** — 数据传输期间显示传输状态的选项 `off` (默认) | `on`

选择此选项可在数据传输期间显示传输状态。

选择“输出状态”参数时，该模块会配置一个输出端口。该模块上的端口标记为状态，表示该模块在输出端口输出发送操作的状态。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

通过串行通信接口 (SCI) 将目标数据传输到主机

SCI Transmit 模块使用指定的 SCI 硬件模块传输标量或向量数据。采样率和数据类型继承自输入端口。

每个模块的模型只能包含一个 SCI Transmit 模块。C28x 处理器有四个 SCI 模块 - A、B、C 和 D。可用的 SCI 模块数量取决于所选处理器。您可以通过导航到 **硬件实现** > **Target hardware resources** 来配置 SCI 模块。请确认这些设置符合您的应用程序要求。请确认这些设置符合您的应用程序要求。

**注意**

- 此模块不支持定点输入，但您可以使用 Data Type Conversion 模块将定点格式转换为原生数据类型。在 Data Type Conversion 模块中，将**输入和输出具有相等的**参数设置为**存储的整数(SI)**。
- 使用类似的 SCI 模块模块进行串行外部模式连接会导致冲突检查错误。

该模块可以以阻塞模式或非阻塞模式输出数据。在阻塞模式下，如果传输 FIFO 已满，则模型模块执行并等待。在非阻塞模式下，模型会持续运行。要将模块设置为阻塞模式，请选择 **Wait until previous data transmitted** 选项。

**注意**

在非阻塞模式下，尝试发送大于 FIFO 长度的数据时，可能会遇到数据丢失的情况。
