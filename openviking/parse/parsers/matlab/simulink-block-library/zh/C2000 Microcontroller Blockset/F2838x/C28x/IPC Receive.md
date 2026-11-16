---
type: simulink-block
title: 'F2837xD/F2838x/F2838x-M4 IPC Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2837xD'
documentation_page: 'f2837xdf2838xf2838xm4ipcreceive'
documentation_source_path: 'ref/f2837xdf2838xf2838xm4ipcreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# F2837xD/F2838x/F2838x-M4 IPC Receive

## 端口

### 输出

### **Out** — IPC 接收向量 | 标量

从另一个 Core 读取的数据。

### **Status** — IPC 接收状态 0 | 1 | 2 | 3 | 4 | 6

状态端口输出以下值之一：

- 0 — 无错误
- 1 — 数据不可用
- 2 — 数据类型不匹配
- 4 — 数据长度不匹配
- 6 — 数据类型和数据长度不匹配

**注意**

当没有数据传输时，IPC Receive 模块接收 uint16 数据类型的 0，并显示数据类型不匹配状态

## 参数

### **Source** — 选择用于接收数据的源 `C28x (CPU1/CPU2)/CPU1`（默认） | `ARM Cortex-M4 (CM)/CPU2`

选择要从中接收数据的源。源选择基于您选择的处理器。对于 F2838x(C28x) 处理器，源是 C28x (CPU1/CPU2) 或 ARM Cortex-M4 (CM)。对于 F2838x-M4 ARM 核处理器，源是 CPU1 或 CPU2。

IPC Receive 模块掩码显示当前源和所选通道。例如，如果模块显示 `C28x_Ch0`，则源为 `C28x (CPU1/CPU2)`，通道为 `0`。类似地，如果 IPC Receive 模块显示 `CM_Ch1`，则源为 `ARM Cortex-M4 (CM)`，通道为 `1`。

**注意**

此参数仅适用于 F2838x(C28x) 和 F2838x-M4 ARM 核处理器。

### **Channel** — 选择用于接收数据的通道 `0`（默认） | 0–31

要从中接收数据的通道。每个通道是共享内存中的单独内存位置。

**注意**

发送器和接收器各有 32 个通道用于发送和接收数据。对于数据发送和接收，发送器和接收器必须设置为相同的通道号。

### **Data type** — 要接收的数据类型 `uint16`（默认） | single | int8 | uint8 | int16 | int32 | uint32 | boolean

模块接收的数据类型。

向量数据存储在 global shared RAM 中，数据的地址存储在 MSGRAM 中。

### **Data length** — 要接收的数据大小 `1`（默认） | 正整数

每个采样时间接收的数据单元数。如果数据长度为 1，模块将每个传入数据解释为标量值；如果数据长度大于 1，模块将每个传入数据解释为长度等于 **Data length** 的向量。标量和向量数据的最大大小为 32 bits。

### **Enable blocking** — 指定 Core 是否必须等待读取数据 `off`（默认） | on

启用后，Core 会等待，直到另一个 Core 的数据可用。

### **Sample time** — 模块读取数据的时间间隔 `0.001`（默认） | `–1` | 正标量

数据采样之间的时间，以 seconds 为单位。当将此参数设置为 `-1` 时，Simulink® 根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

为每个核使用单独的模型时，从任一核接收数据

IPC Receive 模块接收并输出从一个 Core 发送到另一个 Core 的数据。

**注意**

对于多核处理器，使用 IPC Receive 和 IPC Transmit 模块向任一核接收或发送数据。当您为每个核使用单独的模型时，将这些模块用于 flat model 方法。

如果您使用多处理器建模方法，使用 Task Manager 通过单个模型触发多个核，则使用 Interprocess Data Read 和 Interprocess Data Write 模块在核之间发送和接收数据。

Core1 将数据发送到其分配的内存（Core1-to-Core2 Message RAM），并从 Core2 的分配内存（Core2-to-Core1 Message RAM）接收数据。类似地，Core2 将数据发送到其分配的内存（Core2-to-Core1 Message RAM），并从 Core1 的分配内存（Core1-to-Core2 Message RAM）接收数据。对于 F2838xD，Core1/Core2 可以是 CPU1、CPU2 或 ARM Cortex-M4 (CM)；对于 F2837xD，Core1/Core2 可以是 CPU1 或 CPU2。

如果 Core1 和 Core2 均为 C28x 核，则两个核之间的数据和通道结构分配在 Message RAM 中，数据数组分配在 Global Shared RAM 中。在 C28x 核中，默认情况下所有通道结构都在 Message RAM 中创建。

但是，如果其中一个核是 ARM Cortex M4（仅适用于 F2838x），则数据数组仅使用 Message RAM 分配，因为核之间没有 global shared RAM 可用。为了容纳更多数据，仅在 Message RAM 中创建所需的通道结构。因此，如果一个核中发送模块使用的通道号与另一个核中的接收模块不匹配，则不会发生数据传输。

硬件中断模块可以与 IPC Receive 模块一起使用，以基于硬件中断接收数据。

- **C28x processor** - 通道 0、1、2 和 3 分别配置为硬件中断 IPC0、IPC1、IPC2 和 IPC3。
- **F2838x-M4 processor** - 通道 0、1、2、3、4、5、6 和 7 分别配置为硬件中断 IPC0、IPC1、IPC2、IPC3、IPC4、IPC5、IPC6 和 IPC7。

可以使用以下参数在硬件中断模块中设置这些硬件中断：**CPU interrupt number** `1` 以及 **PIE interrupt numbers** `13`、`14`、`15` 和 `16`（分别对应）。

### IPC Flat Models 的内存分配

**Channel assignment**、**Memory usage in CM message RAM** 和 **Memory usage in C28x message RAM** 提供了有关在 IPC 模块中如何为 flat models 分配内存的详细说明。

- **Channel assignment** - C28x-CM IPC（Inter-Processor Communication）中的通道分配是实现 CPU1、CPU2 和 Communication Manager (CM) 之间无缝通信的关键方面。在内部，为每个 CPU 维护通道数组，以便与 CM 交换数据。此过程涉及对数组排序，以基于预定顺序分配通道，从而最大化 message RAM 的利用率以实现高效通信。

  IPC 模块对数组排序，并基于排序后的顺序分配通道，这可能导致模块上的通道选择与生成代码中的通道选择不匹配。此逻辑有助于我们最大化 message RAM 的充分利用，以与 CPUx 和 CM 通信。

  例如，基于模型上的通道选择：

  - **CM-CPU1 channel selection** - 如果 CM-CPU1 数组排序为 `[0_Rx, 0_Tx, 1_Tx, 2_Rx, 4_Rx]`，则生成代码中的对应条目将为 `[0_Rx, 0_Tx, 1_Tx, 2_Rx, 3_Rx]`。
  - **CM-CPU2 channel selection** - 如果 CM-CPU2 数组排序看起来像 `[0_Rx, 0_Tx, 2_Rx, 3_Tx, 5_Tx, 6_Tx]`，则生成代码中的对应条目将为 `[0_Rx, 0_Tx, 1_Rx, 2_Tx, 3_Tx, 4_Tx]`。
- **Memory usage in CM message RAM** - 当模型中配置了 IPC Transmit 或 Receive 模块时，CM message RAM 会创建以下带有 IPC 结构和缓冲区的变量。例如，当 **Buffer size = 2** 时：

  1. **MW\_IPCCMtoCPUxBuffers** - 元素数量 = (通道数 \* Buffer size) - 大小 = 8 bytes，用于将 datatype、data length 和 data 存储为结构体
  2. **MW\_Cpu1PutWriteIndexes** - 元素数量 = 通道数 - 大小 = 2 bytes
  3. **MW\_Cpu1GetReadIndexes** - 元素数量 = 通道数 - 大小 = 2 bytes
  4. **MW\_CPU1WRITEFLAGBUFF1** - 元素数量 = 通道数 - 大小 = 2 bytes
  5. **MW\_CPU1WRITEFLAGBUFF2** - 元素数量 = 通道数 - 大小 = 2 bytes
  6. **MW\_CPU1READFLAGBUFF1** - 元素数量 = 通道数 - 大小 = 2 bytes
  7. **MW\_CPU1READFLAGBUFF2** - 元素数量 = 通道数 - 大小 = 2 bytes

     基于通道选择和数据长度的缓冲区分配

     - mwCpu1Channel<channelNumber>Buff1
     - mwCpu1Channel<channelNumber>Buff2 - 元素数量 = 数据长度
       (datalength) - 大小 4 bytes
- **Memory usage in C28x message RAM** - 当模型中配置了 IPC Transmit 或 Receive 模块时，C28x message RAM 会创建以下带有 IPC 结构和缓冲区的变量。例如，当 **Buffer size = 2** 时：

  1. **MW\_IPCCPUtoCMBuffers** - 元素数量 = (通道数 \* Buffer size) - 大小 = 8 bytes，用于将 datatype、data length 和 data 存储为结构体。
  2. **MW\_CmPutWriteIndexes** - 元素数量 = 通道数 - 大小 = 2 bytes
  3. **MW\_CmGetReadIndexes** - 元素数量 = 通道数 - 大小 = 2 bytes
  4. **MW\_CMWRITEFLAGBUFF1** - 元素数量 = 通道数 - 大小 = 2 bytes
  5. **MW\_CMWRITEFLAGBUFF2** - 元素数量 = 通道数 - 大小 = 2 bytes
  6. **MW\_CMREADFLAGBUFF1** - 元素数量 = 通道数 - 大小 = 2 bytes
  7. MW\_CMREADFLAGBUFF2 - 元素数量 = 通道数 - 大小 = 2 bytes

     基于通道选择和数据长度的缓冲区分配。

     - mwCmChannel<channelNumber>Buff1
     - mwCmChannel<channelNumber>Buff2 - 元素数量 = 数据长度
       (datalength) - 大小 4 bytes
