---
type: simulink-block
title: 'F2838x-M4 UDP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4udpreceive'
documentation_source_path: 'ref/f2838xm4udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# F2838x-M4 UDP Receive

## 端口

### 输出

### **Data** — 从发送 UDP 主机接收的 UDP 数据包向量

在每个采样时间，该端口输出接收到的数据包内容，作为大小由 **Data size (N)** 参数指定的数据向量。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 确定在给定时步是否接收到请求的数据（标量）

当接收到的数据元素数量小于或等于块中指定的 **Data size (N)** 时，该端口输出 `0`（成功）。否则，它输出一个非零值，表示没有新数据可用。

**数据类型：** `uint8`

### **Length** — 可变长度标量

接收到的可变输出消息的长度

#### 依赖项

要启用此端口，请选择 **Enable variable length** 参数。

**数据类型：** `uint32`

## 参数

### **Local IP Port** — 接收 UDP 主机上的 IP 端口 `25000`（默认）| 范围 `[1,65535]` 内的正整数

指定要从中接收数据包的应用的端口号。将本地端口号与发送主机的远程端口号匹配。

### **Remote IP address (0.0.0.0 for accepting all)** — 块从中接收 UDP 数据包的 IP 地址 `192.1.168.10`（默认）| `0.0.0.0`

指定块从中接收数据包的远程主机的 IP 地址。要从所有发送主机接收数据包，请指定 `0.0.0.0`。

### **Data type** — UDP 数据包中元素的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择块接收的 UDP 数据包中元素的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 每个 UDP 数据包中的数据元素数量 `1`（默认）

指定您希望在每个数据包中接收的元素数量。

为避免数据丢失，在将数据发送到目标中的 UDP Receive 时，请确保考虑以下条件。

**注意**

- UDP 模块可以处理最大数据包大小（数据报大小）`1472` 字节。确保发送到目标的数据包大小小于或等于 `1472` 字节。
- 确保发送到目标的数据大小小于或等于数据包大小（数据报大小）。

### **Enable variable length** — 可变长度 `off`（默认）| `on`

当选择 **Enable variable length** 参数时，该模块配置一个输出端口 **Length**。

### **Maximum data size (N)** — 数据的最大长度 `1`（默认）| 正整数

指定要接收的数据的最大长度。

#### 依赖项

要启用此参数，请选择 **Enable variable length** 参数。

### **Wait until data received** — 等待直到请求的数据可用 on（默认）| off

- `on` — 当选择此参数时，读取操作在阻塞模式下运行。当块正在等待请求的数据时，读取操作会被阻塞。如果数据可用，则该块输出数据。如果数据不可用，则该块等待数据。

  如果下一次读取操作开始时目标硬件仍在等待数据，则会发生任务超限。

  要修复超限，请使用 **Sample time** 参数增大时间步长。
- `off` — 当清除此参数时，读取操作在非阻塞模式下运行。读取数据时，如果数据不可用，则该块保留上一步接收到的数据包。在此模式下，该块不会等待请求的数据可用。

### **Sample time** — 此块从发送 UDP 主机读取数据包的频率 `0.1`（默认）

指定该模块应多久读取一次端口缓冲区。输入大于 `0` 的值或 `-1`（用于继承采样时间）。

此值默认为采样时间 `0.1` 秒。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 Instrument Control Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从 UDP 主机接收 UDP 数据包

UDP Receive 模块从 UDP 主机接收 UDP 数据包。该模块用于无状态和无连接的数据交换。

在每个采样中，该模块将 UDP 数据包的内容输出为由 **Data size (N)** 参数指定大小的数据向量。

该模块在 **Local IP Port** 参数指定的端口号上，从 **Remote IP address (0.0.0.0 for accepting all)** 参数指定的 IP 地址接收数据包。

您可以选择以阻塞或非阻塞模式接收 UDP 数据包。

**注意**

- 您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置软件以允许来自特定 IP 端口号的流量。
- 由于 F2838x(ARM Cortex-M4) 上的 RAM 内存限制，此模块不支持将应用程序加载到 RAM。
- F2838x Arm Cortex-M 内核（Connectivity Manager）的 CPU Timer 2 为 lwIP 协议栈提供时基。它被配置为每 1 ms 触发一次中断。如果模型中使用了以太网模块，则不应重新配置此计时器。如果通过 Hardware Interrupt 模块使能相应中断，则它将每 1 ms 运行一次中断处理程序。
