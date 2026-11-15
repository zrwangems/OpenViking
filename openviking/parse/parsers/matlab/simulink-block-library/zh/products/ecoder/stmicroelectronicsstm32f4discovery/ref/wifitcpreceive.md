---
type: simulink-block
title: 'WiFi TCP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'wifitcpreceive'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/wifitcpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi TCP Receive

## 端口

### 输出

### **Data** — 输出数据向量

在每个时间步，该端口输出一个大小由 **Data size (N)** 参数指定的数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 在给定时间步收到的请求数据 `scalar`

如果数据在给定时间步收到，该端口输出 `0`。在其他时间，该端口输出非零值，表示没有新数据可用。

#### 依赖关系

要启用此端口，请选择 **Output Status** 参数。

**数据类型：** `uint8`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认）| `Client`

将模块设置为 TCP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP port**。本地端口充当 TCP 服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须提供 **Remote IP address** 以及您要从其接收数据的 TCP 服务器上的 **Remote IP port**。在部署包含客户端 WiFi TCP Receive 模块的模型之前，请确保服务器已启动并正在运行。

### **Local IP port** — 接收主机上从其接收数据的 IP 端口 `25000`（默认）| `positive integer in the range [1 to 65,535]`

此本地端口号充当 TCP 服务器上的侦听端口。将本地端口号与发送主机的远程端口号匹配。

#### 依赖关系

要启用此参数，请将 **Connection mode** 参数设置为 `Server`。

### **Remote IP address** — 从其接收数据的服务器的远程 IP 地址 `192.168.1.2`（默认）| `any valid IP address`

指定从其接收数据的发送服务器的 IP 地址。

#### 依赖关系

要启用此参数，请将 **Connection mode** 参数设置为 `Server`。

### **Remote IP port** — 从其接收数据的服务器上的远程 IP 端口 `25000`（默认）| `positive integer in the range [1 to 65,535]`

指定从其接收数据的发送服务器的端口号。

#### 依赖关系

要启用此参数，请将 **Connection mode** 参数设置为 `Server`。

### **Data type** — 接收数据的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择模块接收的 TCP 数据中元素的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 接收数据中的数据字节数 `1`（默认）| 任意正整数

指定每个时间步要接收的数据字节数。

### **Sample time** — 模块从发送主机读取数据的时间间隔 `0.5`（默认）| 非负值

指定模块读取端口缓冲区的频率。输入大于 `0` 或 `-1` 的值（用于继承采样时间）。

此值默认为 `0.5` 秒的采样时间。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

### **Timeout in seconds** — 等待直到收到数据的时间 `0.001`（默认）| (0.0005s 到 30s)

指定模块在每个时间步中等待数据的最大时间量。如果发生超时，读取操作将中止。

**注意**

在外部模式下仿真模型时，请指定小于 `3` 秒的值。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

从互联网网络上的另一个 TCP/IP 主机接收 TCP/IP 数据包

WiFi TCP Receive 模块通过无线网络从远程主机或其他硬件接收数据。

在每个时间步，**Data** 端口输出一个大小由 **Data size (N)** 参数指定的数据向量。**Status** 端口输出 0 或非零值，指示是否收到新数据。**Status** 端口为 0 表示收到有效数据。

**注意**

您的防病毒软件或防火墙可能会阻止 TCP 流量。请配置软件以允许来自特定 IP 端口号的流量。
