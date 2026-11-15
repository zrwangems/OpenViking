---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'udpreceive'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 将从发送 UDP 主机接收到的 UDP 数据包输出为向量

在每个采样时间，该端口将接收到的数据包内容输出为数据向量，其大小由 **Data size (N)** 参数指定。有关详细信息，请参阅接收 UDP 数据包。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 确定在给定时步是否接收到请求的数据（标量）

在每个采样时间，当接收到的数据长度大于或等于 **Data size (N)** 参数指定的长度时，该端口输出 `0`。值 `0` 表示在给定时步接收到了请求的数据。否则，它输出非零值，表示没有新数据可用。

有关详细信息，请参阅接收 UDP 数据包。

**数据类型：** `uint16`

## 参数

### **Local IP Port** — 接收 UDP 主机上的 IP 端口 `25000`（默认）| `Any integer between 1 and 65535`

指定要从中接收数据包的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

### **Remote IP address (0.0.0.0 for accepting all)** — 该模块从中接收 UDP 数据包的 IP 地址 `0.0.0.0`（默认）

指定该模块从中接收数据包的远程主机的 IP 地址。要从所有发送主机接收数据包，请指定 `0.0.0.0`。

### **Data type** — UDP 数据包中元素的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择该模块从发送主机接收元素时所用的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 每个 UDP 数据包中的数据元素数 `1`（默认）

指定每个数据包中要接收的元素数。

### **Wait until data received** — 等待直到请求的数据可用 on（默认）| off

- `on` — 选择此参数时，读取操作在 **阻塞模式** 中运行。读取操作在等待请求的数据可用时被阻塞。如果数据可用，`Data` 端口输出数据。如果数据不可用，`Data` 端口等待数据。

  如果当下一次读取操作计划开始而目标硬件仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 使用 **Sample time** 参数增大时间步长。
  - 使用 **Data size (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读取操作在 **非阻塞模式** 中运行。读取数据时，如果数据不可用，`Data` 端口包含上一时间步接收到的数据包。在此模式下，该模块不会等待请求的数据可用。

### **Sample time** — 此模块从发送 UDP 主机读取数据包的频率 `-1`（默认）

当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定为该模块最佳的采样时间。

### 接收 UDP 数据包

此示例描述了当接收到的数据包长度小于、大于或等于请求的数据长度时，输出端口的值。

- **接收到的 UDP 数据包长度 = Data size (N)**：`Data` 端口将该数据包输出为数据向量，其大小由 **Data size (N)** 参数指定。

  `Status` 端口输出 `0`，表示接收到了请求的数据。

  假设指定的 **Data size (N)** 参数为 4，且接收到的数据包长度也为 4。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量，其中填充了该数据包的元素。

  `Status` 端口处的值为 `0`。
- **接收到的 UDP 数据包长度 < Data size (N)**：`Data` 端口将该数据包输出为数据向量，其大小由 **Data size (N)** 参数指定。向量中的所有空位都用随机值填充。

  `Status` 端口输出非零值，表示没有接收到新数据。

  假设指定的 **Data size (N)** 参数为 4，且接收到的数据长度为 3 字节。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量。向量中的前三个元素是来自接收数据包的元素。剩余空间用随机值填充。

  `Status` 端口输出非零值。
- **接收到的 UDP 数据包长度 > Data size (N)**：`Data` 端口输出数据向量，其大小由 **Data size (N)** 参数指定。该向量仅包含数据包中的前 *N* 个元素。其余元素被丢弃。

  `Status` 端口输出 `0`，表示接收到了请求的数据。

  假设指定的 **Data size (N)** 参数为 4，且接收到的数据长度为 5 字节。在这种情况下，`Data` 端口输出大小为 4 的数据向量。该向量仅包含接收数据包中的前四个元素。其余元素被丢弃。`Status` 端口处的值为 `0`。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

从 UDP 主机接收 UDP 数据包

UDP Receive 模块从 UDP 主机接收 UDP 数据包。使用该模块进行无状态和无连接的数据传输。

在每个采样时，该模块将 UDP 数据包的内容输出为数据向量，其大小由 **Data size (N)** 参数指定。

该模块从 **Remote IP address (0.0.0.0 for accepting all)** 参数指定的 IP 地址，在 **Local IP Port** 参数指定的端口号上接收数据包。要从所有发送主机接收数据包，请将远程 IP 地址指定为 `0.0.0.0`。将 **Local IP Port** 参数中指定的端口号与发送主机的远程端口号匹配。

您可以选择在阻塞或非阻塞模式下接收 UDP 数据包。

**注意**

- 当模型中的 TCP/IP 或 UDP 模块启用 DHCP 时，代码会在无限循环中等待，直到为板卡分配 IP。因此，如果用户的模型中任何 UDP/TCP 模块启用了 DHCP，用户必须确保板卡连接到路由器
- 如果您在使用 UDP 与计算机通信时遇到问题，请检查防病毒或防火墙软件是否阻止了 UDP 流量。如果是，请尝试配置该软件以允许特定 IP 端口号的流量。
