---
type: simulink-block
title: 'F2838x-M4 UDP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4udpsend'
documentation_source_path: 'ref/f2838xm4udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# F2838x-M4 UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据端口向量

该端口接受一个数组，并通过 IP 网络将其作为 UDP 数据包发送到接收 UDP 主机。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Length** — 可变长度标量

接收到的可变输入消息的长度

#### 依赖关系

要启用此端口，请选择 **启用可变长度** 参数。

**数据类型：** `uint32`

## 参数

### **远程 IP 地址（广播时为 255.255.255.255）** — 接收 UDP 主机的 IP 地址 `192.168.1.10`（默认）| `255.255.255.255`

指定模块向其发送 UDP 数据包的 IP 地址或主机名。要将数据包广播到所有接收主机，请指定 `255.255.255.255`。

### **远程 IP 端口** — 接收 UDP 主机上的 IP 端口 `25000`（默认）| 范围 `[1,65535]` 中的正整数

指定接收主机上要将数据包发送到的应用程序的端口号。将远程端口号与接收主机的本地端口号匹配。

### **本地 IP 端口（-1 表示自动分配端口）** — 发送 UDP 主机上的 IP 端口 `-1`（默认）|

指定要从其发送数据包的应用程序的端口号。

当指定默认值 `-1` 时，模块会从可用端口中随机选择一个端口来发送数据。如果接收主机期望来自特定端口号的 UDP 数据包，请指定该端口号。

### **启用可变长度** — 可变长度 `off`（默认）| `on`

当选择 **启用可变长度** 参数时，模块将配置一个输入端口，**Length**。

### **等待上一数据包传输完成** — 等待发送新数据包 off（默认）| on

- `on` — 当选择此参数时，发送操作以阻塞模式运行。在此模式下，如果模块仍在传输上一时间步接收到的数据包，则模块会保留当前时间步输入端口处的数据，并等待发送它。

  如果下一个发送操作计划开始时，目标硬件仍在等待所请求的数据发送，则会发生任务超限。要修复超限，请使用 **采样时间** 参数增大时间步。
- `off` — 当清除此参数时，发送操作以非阻塞模式运行。在此模式下，如果模块仍在传输上一时间步接收到的数据包，则当前时间步输入端口处的数据将被丢弃。

  在任一模式下，如果模块尚未在发送主机和接收主机之间建立连接，或者连接丢失，则输入端口处的数据将被丢弃。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 Instrument Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

将 UDP 数据包发送到 UDP 主机

UDP Send 模块将 UDP 数据包发送到 UDP 主机。使用该模块进行无状态且无连接的数据传输。

该模块从 **本地 IP 端口（-1 表示自动分配端口）** 参数指定的端口号发送数据包。接收主机的 IP 地址和端口号在 **远程 IP 地址（广播时为 255.255.255.255）** 和 **远程 IP 端口** 参数中指定。

您可以选择以阻塞或非阻塞模式发送 UDP 数据包。

**注意**

- 您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置软件以允许来自特定 IP 端口号的流量。
- 由于 F2838x（ARM Cortex-M4）上的 RAM 内存限制，此模块不支持将应用程序加载到 RAM。
- F2838x Arm Cortex-M4 内核（Connectivity Manager）的 CPU Timer 2 为 lwIP 协议栈提供时基。它被配置为每 1 ms 触发一次中断。如果模型中使用了 Ethernet 模块，则不应重新配置此定时器。如果通过 Hardware Interrupt 模块使能相应中断，它将每 1 ms 运行一次中断处理程序。
