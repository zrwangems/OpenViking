---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Network'
documentation_page: 'udpsendblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpsendblock.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **data** — 向 UDP 主机发送 UDP 数据包 向量

该端口接受一个数组，并通过 IP 网络端口将其作为 UDP 数据包发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### 输出

### **Status** — 确定请求的数据是否在给定时步发送 标量

在每个采样时间，当发送的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，端口输出 `0`。值 `0` 表示请求的数据在给定时步发送。否则，它输出一个非零值，表示没有新数据可用。

#### 依赖项

要启用此端口，请选择 **Output error status** 参数。

**数据类型：** `uint16`

## 参数

### **Remote IP address (255.255.255.255 for broadcast)** — 接收 UDP 主机的 IP 地址 `0.0.0.0`（默认）

指定模块将 UDP 数据包发送到的 IP 地址。此参数不接受主机名作为输入。要将数据包广播到所有接收主机，请指定 `255.255.255.255`。

### **Local IP Port** — 发送 UDP 主机上的 IP 端口 `25010`（默认） | `-1`

指定要从中发送数据包的应用程序的端口号。

值 `-1` 会将本地端口号设置为随机可用端口号，并使用该端口发送数据包。如果接收主机期望来自特定端口号的 UDP 数据包，请指定该端口号。

### **Remote IP Port** — 接收 UDP 主机上的 IP 端口 `25002`（默认） | `Any integer between 1 and 65535`

指定接收主机上要将数据包发送到的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

### **Wait until previous packet transmitted** — 等待上一步接收的数据包被发送 `off`（默认） | `on`

- `on` — 选择此参数时，发送操作以 **阻塞模式** 运行。如果上一步接收的数据包已发送，模块从输入端口接受数据。如果发送操作正在进行，模块会等待数据包发送完成，然后从输入端口接受数据。

  如果发送主机与接收主机之间的连接未建立，或者连接丢失，则输入端口处的数据会被丢弃。

  如果目标硬件在下一个发送操作计划开始时仍在等待请求的数据发送完成，则会发生任务超限。要修复超限：

  - 增加输入数据的采样时间。
  - 减少输入端口处的数据长度。
- `off` — 清除此参数时，发送操作以 **非阻塞模式** 运行。发送数据包时，如果上一步接收的数据包传输仍在进行，则给定时步输入端口处的数据会被丢弃。

  如果发送主机与接收主机之间的连接未建立，或者连接丢失，则输入端口处的数据会被丢弃。

### **Output error status** — 在数据传输期间显示错误状态的选项 `off`（默认） | `on`

选择此参数以显示数据传输期间的错误状态。

当您选择 Output error status 参数时，模块会配置一个输出端口。模块上的该端口标记为 Status，表示模块在输出端口输出读取操作的状态。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

向 UDP 主机发送 UDP 数据包

UDP Send 模块通过 IP 网络端口将输入向量作为 UDP 数据包发送到 UDP 主机。使用该模块进行无状态和无连接的数据传输。

该模块从 **Local IP Port (-1 for automatic port assignment)** 参数中指定的端口号发送数据包。

在 **Remote IP address (255.255.255.255 for broadcast)** 和 **Remote IP Port** 参数中指定接收主机的 IP 地址和端口号。

您可以选择以阻塞或非阻塞模式发送 UDP 数据包。

**注意**

确保在 STM32CubeMX 项目中配置以太网选项。有关更多信息，请参见在 STM32CubeMX 中为基于 STM32 处理器的板配置以太网选项。
