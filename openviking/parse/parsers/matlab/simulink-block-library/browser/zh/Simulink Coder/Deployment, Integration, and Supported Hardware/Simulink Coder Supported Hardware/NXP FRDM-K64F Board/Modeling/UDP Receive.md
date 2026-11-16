---
type: simulink-block
title: 'UDP Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'freescalefrdmk64fboard/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 从发送 UDP 主机接收到的 UDP 消息输出向量

在每个采样时间，该端口将接收到的消息的数据字节输出为大小由 **Data size (N)** 参数指定的数据向量。有关详细信息，请参阅接收 UDP 消息。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Size** — 接收到的 UDP 消息中的数据字节数（标量）

在每个采样时间，该端口输出接收到的消息中的数据字节数。有关详细信息，请参阅接收 UDP 消息。

**数据类型：** `uint16`

## 参数

### **Local IP Port** — 接收 UDP 主机上的 IP 端口 `25000`（默认值） | `Any integer between 1 and 65535`

指定要接收消息的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

### **Data type** — UDP 消息中数据字节的数据类型 `uint8`（默认值） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择模块从发送主机接收数据字节时使用的数据类型。

### **Data size (N)** — 每条 UDP 消息中的数据字节数 `1`（默认值）

指定您希望在每条消息中接收的数据字节数。

### **Wait until data received** — 等待直到请求的数据可用 off（默认值） | on

- `on` — 选择此参数时，读取操作在**阻塞模式**下运行。在等待请求的数据可用期间，读取操作会被阻塞。如果数据可用，`Data` 端口输出数据。如果数据不可用，`Data` 端口等待数据。当模块等待新数据到达时，`Size` 端口输出 `0`。当新数据到达时，`Size` 端口处的值变为非零值。

  如果当下一次读取操作计划开始时，目标硬件仍在等待数据可用，则会发生任务超限。

  要解决超限：

  - 使用 **Sample time** 参数增加时间步长。
  - 使用 **Data size (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读取操作在**非阻塞模式**下运行。读取数据时，如果数据不可用，`Data` 端口包含其在上一个时间步中收到的消息。`Size` 端口输出 `0`。在此模式下，模块不等待请求的数据可用。

### **Sample time** — 此模块读取来自发送 UDP 主机的消息的频率 `0.1`（默认值）

将此参数指定为`-1`时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

### 接收 UDP 消息

此示例描述当接收到的消息长度小于、大于或等于请求的数据长度时，输出端口处的值。本节说明当 **Data type** 设置为 `uint8` 且 **Data size (N)** 设置为 `4` 时，输出端口处的值。

- **接收到的 UDP 消息长度 = Data size (N)**：`Data` 端口将消息输出为大小由 **Data size (N)** 参数指定的数据向量。

  `Size` 端口输出接收到的数据字节数。

  假设指定的 **Data size (N)** 参数为 4，并且接收到的消息长度也为 4。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量，其中填充了该消息的数据字节。

  `Size` 端口处的值为 `4`。
- **接收到的 UDP 消息长度 < Data size (N)**：`Data` 端口将消息输出为大小由 **Data size (N)** 参数指定的数据向量。向量中的所有空余位置都填充随机值。

  `Size` 端口输出接收到的数据字节数（不包括随机值）。

  假设指定的 **Data size (N)** 参数为 4，并且接收到的数据长度为 3 字节。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量。向量中的前三个数据字节是来自接收消息的字节。剩余空间填充一个随机值。

  `Size` 端口处的值为 `3`。
- **接收到的 UDP 消息长度 > Data size (N)**：`Data` 端口输出大小由 **Data size (N)** 参数指定的数据向量。该向量仅包含消息中的前 *N* 个数据字节。其余数据字节被丢弃。

  `Size` 端口输出接收到的数据字节数（包括输出的数据字节和被丢弃的数据字节）。

  假设指定的 **Data size (N)** 参数为 4，并且接收到的数据长度为 5 字节。在这种情况下，`Data` 端口输出大小为 4 的数据向量。该向量仅包含来自接收消息的前四个数据字节。其余数据字节被丢弃。`Size` 端口处的值为 `4+1=5`。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

从 UDP 主机接收 UDP 消息

UDP Receive 模块从 UDP 主机接收 UDP 消息。

在每次采样时，模块将 UDP 消息的数据字节输出为大小由 **Data size (N)** 参数指定的数据向量。

该模块在 **Local IP Port** 参数指定的端口号上接收消息。将 **Local IP Port** 参数指定的端口号与发送主机的远程端口号匹配。

您可以选择以阻塞模式或非阻塞模式接收 UDP 消息。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，请检查是否是防病毒或防火墙软件阻止了 UDP 流量。如果是，请尝试配置该软件以允许特定 IP 端口号的流量。
