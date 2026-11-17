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
chinese_source: worker-translation
---

# F2837xD/F2838x/F2838x-M4 IPC Transmit

## 端口
```yaml
ports:
- name: Input
  summary: 要发送到另一个核的数据 uint16 | single | int8 | uint8 | int16 | int32 | uint32 | boolean
  direction: input
```

### 输入

### **Input** — 要发送到另一个核的数据 uint16 | single | int8 | uint8 | int16 | int32 | uint32 | boolean

该端口接收要以向量或标量形式传输到另一个核的数据。
## 参数
```yaml
parameters:
- name: Destination
  summary: 选择用于发送数据的目标 C28x (CPU1/CPU2)/CPU1（默认）| ARM Cortex-M4 (CM)/CPU2
  group: ''
- name: Channel
  summary: 选择用于传输数据的通道 0（默认）| 0–31
  group: ''
- name: Enable blocking
  summary: 指定核是否必须等待直到发送的数据被读取 off（默认）| on
  group: ''
```

### **Destination** — 选择用于发送数据的目标 `C28x (CPU1/CPU2)/CPU1`（默认）| `ARM Cortex-M4 (CM)/CPU2`

要发送数据的目标。目标选择取决于所选择的处理器。对于 F2838x(C28x) 处理器，目标是 C28x (CPU1/CPU2) 或 ARM Cortex-M4 (CM)。对于 F2838x-M4 ARM 核处理器，目标是 CPU1 或 CPU2。

IPC Transmit 模块掩码显示当前目标和所选通道。例如，如果模块显示 `C28x_Ch0`，则目标是 `C28x (CPU1/CPU2)`，通道是 `0`。类似地，如果 IPC Transmit 模块显示 `CM_Ch1`，则目标是 `ARM Cortex-M4 (CM)`，通道是 `1`。

**注意**

此参数仅适用于 F2838x(C28x) 和 F2838x-M4 ARM 核处理器。

### **Channel** — 选择用于传输数据的通道 `0`（默认）| `0–31`

要从中传输数据的通道。每个通道是共享内存中的独立内存位置。

**注意**

发送器和接收器各有 32 个通道用于发送和接收数据。对于数据发送和接收，发送器和接收器必须设置为相同的通道号。

### **Enable blocking** — 指定核是否必须等待直到发送的数据被读取 `off`（默认）| on

启用后，发送数据后，核会等待直到另一个核读取该数据。
## 所属库

C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

在为每个核使用单独模型时向任一核发送数据

IPC Transmit 模块将数据从一个核传输到另一个核。

**注意**

对于多核处理器，使用 IPC Receive 和 IPC Transmit 模块向任一核接收或发送数据。当您为每个核使用单独模型时，请使用这些模块进行扁平模型方法。

如果您使用多处理器建模方法，并通过 Task Manager 使用单个模型触发多个核，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在核之间发送和接收数据。

Core1 将数据传输到其分配的内存（Core1-to-Core2 Message RAM），并从 Core2 的分配内存（Core2-to-Core1 Message RAM）接收数据。类似地，Core2 将数据传输到其分配的内存（Core2-to-Core1 Message RAM），并从 Core1 的分配内存（Core1-to-Core2 Message RAM）接收数据。对于 F2838xD，Core1/Core2 可以是 CPU1、CPU2 或 ARM Cortex-M4 (CM)；对于 F2837xD，Core1/Core2 可以是 CPU1 或 CPU2。

如果 Core1 和 Core2 都是 C28x 核，则两个核之间的数据和通道结构分配在 Message RAM 中，数据数组分配在 Global Shared RAM 中。在 C28x 核中，默认情况下所有通道结构都在 Message RAM 中创建。

但是，如果其中一个核是 ARM Cortex M4（仅适用于 F2838x），则数据数组仅使用 Message RAM 分配，因为核之间没有可用的全局共享 RAM。为了容纳更多数据，仅在 Message RAM 中创建所需的通道结构。因此，如果一个核中 transmit 模块使用的通道号与另一个核中 receive 模块不匹配，则不会发生数据传输。

有关 IPC 模块内存分配方式的更多信息，请参阅 Memory Allocation for IPC Flat Models
