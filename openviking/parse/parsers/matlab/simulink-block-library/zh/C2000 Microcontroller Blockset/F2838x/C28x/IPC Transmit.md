---
type: simulink-block
title: 'F2837xD/F2838x/F2838x-M4 IPC Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2837xD'
documentation_page: 'f2837xdf2838xf2838xm4ipctransmit'
documentation_source_path: 'ref/f2837xdf2838xf2838xm4ipctransmit.html'
language: zh-CN
chinese_source: official
---

# F2837xD/F2838x/F2838x-M4 IPC Transmit

## 端口

### 输入

### **Input** — 要发送到另一个核心的数据 uint16 | 单精度 | int8 | uint8 | int16 | int32 | uint32 | 布尔

该端口接受以向量或标量形式传输到其他核心的数据。

## 参数

### **目标** — 已选择数据发送目的地 `C28x (CPU1/CPU2)/CPU1` (默认) | `ARM Cortex-M4 (CM)/CPU2`

您要将数据发送到的目标位置。目标位置的选择取决于您选择的处理器。对于 F2838x(C28x) 处理器，目标可以是 C28x (CPU1/CPU2) 或 ARM Cortex-M4 (CM)。对于 F2838x-M4 ARM 内核处理器，目标是 CPU1 或 CPU2。

IPC Transmit 模块掩码显示当前目的地和所选信道。例如，如果模块显示 `C28x_Ch0`，则目的地为 `C28x (CPU1/CPU2)`，通道为 `0`。同样，如果 IPC Transmit 模块显示 `CM_Ch1`，则目的地为 `ARM Cortex-M4 (CM)`，通道为 `1`。

**注意**

此参数仅适用于 F2838x(C28x) 和 F2838x-M4 ARM 内核处理器。

### **通道** — 选择用于传输数据的信道 `0` (默认) | `0–31`

您要从中传输数据的通道。每个通道都是共享内存中的一个独立内存位置。

**注意**

发射器和接收器各有 32 个通道用于发送和接收数据。数据传输和接收时，发射器和接收器必须设置为相同的频道号。

### **启用阻塞** — 指定 Core 是否必须等待直到读取已发送的数据。 `off` (默认) | on

启用后，核心在发送数据后会等待另一个核心读取数据。

## 所属库

C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2018a 中推出**

## 描述

使用为每个内核单独建模的方式，将数据传输到任一内核。

IPC Transmit 模块将数据从一个核心传输到另一个核心。

**注意**

对于多核处理器，使用 IPC 接收和 IPC 发送模块来接收或发送数据到任一核心。这些模块适用于扁平模型方法，其中每个核心都使用单独的模型。

如果您使用多处理器建模方法，并且使用任务管理器通过单个模型触发多个核心，请使用 Interprocess Data Read 和 Interprocess Data Write模块在核心之间发送和接收数据。

Core1 将数据传输到其分配的内存（Core1 到 Core2 消息 RAM），并从 Core2 的分配内存（Core2 到 Core1 消息 RAM）接收数据。同样，Core2 将数据传输到其分配的内存（Core2 到 Core1 消息 RAM），并从 Core1 的分配内存（Core1 到 Core2 消息 RAM）接收数据。对于 F2838xD，Core1/Core2 可以是 CPU1、CPU2 或 ARM Cortex-M4 (CM)；对于 F2837xD，Core1/Core2 可以是 CPU1 或 CPU2。

如果 Core1 和 Core2 都是 C28x 内核，则两个内核之间的数据和通道结构分配在消息 RAM 中，数据数组分配在全局共享 RAM 中。在 C28x 内核中，默认情况下所有通道结构都在消息 RAM 中创建。

但是，如果其中一个核心是 ARM Cortex M4（仅适用于 F2838x），则数据数组仅使用消息 RAM 进行分配，因为核心之间没有全局共享 RAM。为了容纳更多数据，消息 RAM 中仅创建所需的通道结构。因此，如果一个内核中用于发送块的通道号与另一个内核中用于接收模块的通道号不匹配，则数据传输将不会发生。

有关 IPC 模块内存分配方式的更多信息，请参阅 Memory Allocation for IPC Flat Models
