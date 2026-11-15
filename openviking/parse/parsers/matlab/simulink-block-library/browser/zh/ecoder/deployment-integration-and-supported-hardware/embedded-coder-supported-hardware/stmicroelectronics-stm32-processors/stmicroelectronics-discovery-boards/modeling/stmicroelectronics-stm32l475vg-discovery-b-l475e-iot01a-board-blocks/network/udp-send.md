---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'udpsend'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 将 UDP 数据包发送到 UDP 主机向量

该端口接受一个数组，并通过 IP 网络端口将其作为 UDP 数据包发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Remote IP address (255.255.255.255 for broadcast)** — 接收 UDP 主机的 IP 地址 `192.168.1.2`（默认值）

指定模块将 UDP 数据包发送到的 IP 地址或主机名。要将数据包广播到所有接收主机，请指定 `255.255.255.255`。

### **Remote IP Port** — 接收 UDP 主机上的 IP 端口 `25002`（默认值） | `Any integer between 1 and 65535`

指定接收主机上要将数据包发送到的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

### **Local IP Port (-1 for automatic port assignment)** — 发送 UDP 主机上的 IP 端口 `-1`（默认值）

指定要从中发送数据包的应用程序的端口号。

默认值 `-1` 将本地端口号设置为一个可用的随机端口号，并使用该端口发送数据包。如果接收主机期望从特定端口号接收 UDP 数据包，请指定该端口号。

### **Wait until previous packet transmitted** — 等待直到上一个时间步中接收的数据包被发送 on（默认值） | off

- `on` — 选择此参数时，发送操作在**阻塞模式**下运行。如果上一个时间步中接收的数据包已发送，模块会从输入端口接受数据。如果发送操作正在进行，模块会等待数据包发送完成，然后从输入端口接受数据。

  如果发送主机与接收主机之间的连接未建立，或连接丢失，则输入端口处的数据将被丢弃。

  如果目标硬件在下一个发送操作计划开始时仍在等待所请求的数据发送完成，则会发生任务超限。要解决超限：

  - 增大输入数据的采样时间。
  - 减少输入端口处的数据长度。
- `off` — 清除此参数时，发送操作在**非阻塞模式**下运行。发送数据包时，如果上一个时间步中接收的数据包的传输仍在进行，则给定时间步中输入端口处的数据将被丢弃。

  如果发送主机与接收主机之间的连接未建立，或连接丢失，则输入端口处的数据将被丢弃。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将 UDP 数据包发送到 UDP 主机

UDP Send 模块将输入向量通过 IP 网络端口作为 UDP 数据包发送到 UDP 主机。使用该模块进行无状态、无连接的数据传输。

该模块从 **Local IP Port (-1 for automatic port assignment)** 参数中指定的端口号发送数据包。

在 **Remote IP address (255.255.255.255 for broadcast)** 和 **Remote IP Port** 参数中指定接收主机的 IP 地址和端口号。

您可以选择以阻塞或非阻塞模式发送 UDP 数据包。

**注意**

当模型中的 TCP/IP 或 UDP 模块启用 DHCP 时，代码会在无限循环中等待，直到为板卡分配 IP。因此，如果用户的模型中包含任何启用了 DHCP 的 UDP/TCP 模块，用户必须确保板卡已连接到路由器。
