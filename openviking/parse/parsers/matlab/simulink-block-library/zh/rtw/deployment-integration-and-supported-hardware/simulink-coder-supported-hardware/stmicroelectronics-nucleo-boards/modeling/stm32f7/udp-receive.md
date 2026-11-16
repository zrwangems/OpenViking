---
type: simulink-block
title: 'UDP Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'udpreceive'
documentation_source_path: 'nucleo/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 输出从发送 UDP 主机接收的 UDP 数据包向量

在每个采样时刻，该端口将接收到的数据包内容输出为数据向量，其大小由 **Data size (N)** 参数指定。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 确定在给定时间步是否接收到请求的数据（标量）

在每个采样时刻，当接收到的数据长度大于或等于 **Data size (N)** 参数指定的长度时，该端口输出 `0`。值 `0` 表示在给定时间步接收到请求的数据。否则，它输出一个非零值，表示没有新数据可用。

**数据类型：** `uint16`

## 参数

### **Local IP Port** — 接收 UDP 主机上的 IP 端口 `25000`（默认）| `1 到 65535 之间的任意整数`

指定您希望从中接收数据包的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

### **Remote IP address (0.0.0.0 for accepting all)** — 模块从中接收 UDP 数据包的 IP 地址 `192.168.1.15`（默认）

指定模块从中接收数据包的远程主机的 IP 地址。要从所有发送主机接收数据包，请指定 `0.0.0.0`。

### **Data type** — UDP 数据包中元素的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择模块从发送主机接收元素时采用的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 每个 UDP 数据包中的数据元素数量 `1`（默认）| `标量`

指定您希望在每个数据包中接收的元素数量。数据大小必须是标量值。

### **Wait until data received** — 等待直到请求的数据可用 `off`（默认）| `on`

- `on` — 选择此参数时，读取操作在 **阻塞模式** 下运行。在等待请求的数据可用期间，读取操作被阻塞。如果数据可用，`Data` 端口输出数据。如果数据不可用，`Data` 端口等待数据。

  如果目标硬件在下一个读取操作计划开始时仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 通过使用 **Sample time** 参数增加时间步长。
  - 通过使用 **Data size (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读取操作在 **非阻塞模式** 下运行。读取数据时，如果数据不可用，`Data` 端口包含上一个时间步接收到的数据包。在此模式下，模块不等待请求的数据可用。

### **Output error status** — 在数据传输期间显示错误状态的选项 `on`（默认）| `off`

选择此选项以在数据传输期间显示错误状态。

选择 Output error status 参数时，模块会配置一个输出端口。模块上的该端口标记为 Status，表示模块在该输出端口输出读取操作的状态。

### **Sample time** — 此模块从发送 UDP 主机读取数据包的频率 `-1`（默认）

当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 接收 UDP 数据包

此示例描述当接收到的数据包长度小于、大于或等于请求的数据长度时，输出端口的值。

- **接收的 UDP 数据包长度 = Data size (N)**：`Data` 端口将数据包输出为数据向量，其大小由 **Data size (N)** 参数指定。

  `Status` 端口输出 `0`，表示接收到请求的数据。

  假设指定的 **Data size (N)** 参数为 4，且接收到的数据包长度也为 4。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量，其中填充了该数据包的元素。

  `Status` 端口处的值为 `0`。
- **接收的 UDP 数据包长度 < Data size (N)**：`Data` 端口将数据包输出为数据向量，其大小由 **Data size (N)** 参数指定。向量中的所有空余位置都用随机值填充。

  `Status` 端口输出一个非零值，表示未接收到新数据。

  假设指定的 **Data size (N)** 参数为 4，且接收到的数据长度为 3 bytes。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量。向量中的前三个元素是来自所接收数据包的元素。剩余位置用随机值填充。

  `Status` 端口输出一个非零值。
- **接收的 UDP 数据包长度 > Data size (N)**：`Data` 端口输出数据向量，其大小由 **Data size (N)** 参数指定。该向量仅包含数据包中的前 *N* 个元素。其余元素被丢弃。

  `Status` 端口输出 `0`，表示接收到请求的数据。

  假设指定的 **Data size (N)** 参数为 4，且接收到的数据长度为 5 bytes。在这种情况下，`Data` 端口输出大小为 4 的数据向量。该向量仅包含所接收数据包中的前四个元素。其余元素被丢弃。`Status` 端口处的值为 `0`。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

从 UDP 主机接收 UDP 数据包

UDP Receive 模块从 UDP 主机接收 UDP 数据包。使用该模块进行无状态和无连接的数据传输。

在每个采样时刻，该模块将 UDP 数据包的内容输出为 **(Nx1)** 数组。

该模块在 **Local IP Port** 参数指定的端口号上，从 **Remote IP address (0.0.0.0 for accepting all)** 参数指定的 IP 地址接收数据包。要从所有发送主机接收数据包，请将远程 IP 地址指定为 `0.0.0.0`。将 **Local IP Port** 参数中指定的端口号与发送主机的远程端口号匹配。

您可以选择以阻塞或非阻塞模式接收 UDP 数据包。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，请检查是否是防病毒或防火墙软件阻止了 UDP 流量。如果是，请尝试配置该软件，以允许特定 IP 端口号的流量。
