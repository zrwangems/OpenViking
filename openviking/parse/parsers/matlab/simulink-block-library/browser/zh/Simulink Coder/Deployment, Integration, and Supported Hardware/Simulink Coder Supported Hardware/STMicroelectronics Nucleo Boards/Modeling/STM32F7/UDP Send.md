---
type: simulink-block
title: 'UDP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'udpsend'
documentation_source_path: 'nucleo/ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 将 UDP 数据包发送到 UDP 主机（向量）

该端口接受一个数组，并通过 IP 网络端口将其作为 UDP 数据包发送到接收主机。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### 输出

### **Status** — 确定请求的数据是否在给定时间步发送（标量）

在每个采样时间，当发送的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，该端口输出 `0`。值 `0` 表示请求的数据在给定时间步发送。否则，它输出一个非零值，表示没有新数据可用。

**数据类型：** `uint16`

## 参数

### **Remote IP address (255.255.255.255 for broadcast)** — 接收 UDP 主机的 IP 地址 `192.168.1.2`（默认值）

指定模块将 UDP 数据包发送到的 IP 地址。此参数不接受主机名作为输入。要将数据包广播到所有接收主机，请指定 `255.255.255.255`。

### **Remote IP Port** — 接收 UDP 主机上的 IP 端口 `25002`（默认值）| `Any integer between 1 and 65535`

指定接收主机上要向其发送数据包的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

### **Local IP Port (-1 for automatic port assignment)** — 发送 UDP 主机上的 IP 端口 `-1`（默认值）

指定要从中发送数据包的应用程序的端口号。

默认值 `-1` 将本地端口号设置为随机可用端口号，并使用该端口发送数据包。如果接收主机期望来自特定端口号的 UDP 数据包，请指定该端口号。

### **Wait until previous packet transmitted** — 等待前一个时间步接收到的数据包发送完成 `off`（默认值）| `on`

- `on` — 选择此参数时，发送操作以 **阻塞模式** 运行。如果前一个时间步接收到的数据包已发送，模块从输入端口接受数据。如果发送操作正在进行，模块等待数据包发送完成，然后从输入端口接受数据。

  如果发送主机与接收主机之间的连接未建立，或连接丢失，输入端口的数据将被丢弃。

  如果计划开始下一次发送操作时，目标硬件仍在等待请求的数据发送完成，则会发生任务溢出。要修复溢出：

  - 增加输入数据的采样时间。
  - 减少输入端口的数据长度。
- `off` — 清除此参数时，发送操作以 **非阻塞模式** 运行。发送数据包时，如果前一个时间步接收到的数据包传输仍在进行中，则给定时间步输入端口的数据将被丢弃。

  如果发送主机与接收主机之间的连接未建立，或连接丢失，输入端口的数据将被丢弃。

### **Output error status** — 在数据传输期间显示错误状态的选项 `off`（默认值）| `on`

选择此选项可在数据传输期间显示错误状态。

选择 Output error status 参数时，模块会配置一个输出端口。模块上的该端口标记为 Status，表示模块在输出端口输出读取操作的状态。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将 UDP 数据包发送到 UDP 主机

UDP Send 模块将输入向量作为 UDP 数据包通过 IP 网络端口发送到 UDP 主机。使用该模块进行无状态且无连接的数据传输。

该模块从 **Local IP Port (-1 for automatic port assignment)** 参数中指定的端口号发送数据包。

在 **Remote IP address (255.255.255.255 for broadcast)** 和 **Remote IP Port** 参数中指定接收主机的 IP 地址和端口号。

您可以选择以阻塞或非阻塞模式发送 UDP 数据包。
