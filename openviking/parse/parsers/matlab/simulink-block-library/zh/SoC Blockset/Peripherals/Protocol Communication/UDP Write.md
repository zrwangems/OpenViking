---
type: simulink-block
title: 'UDP Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpwrite'
documentation_source_path: 'ref/udpwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Write

## 端口

### 输入

### **data** — 输入信号，数值向量

输入数据，指定为数值向量。该模块将此数据作为 UDP 包发送到远程主机。要设置发送此 UDP 数据时所需的字节序，请设置 **字节序** 参数。该模块将此输入数据转换为指定的字节序类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **msg** — 发送到远程主机的 UDP 包，数值向量

此消息端口将 UDP 包作为消息发送到连接的 IO Data Sink 模块。有关消息的详细信息，请参阅消息。

**注意**

此输出仅在仿真期间使用，在代码生成和外部模式仿真中不起作用。

**数据类型：** `SoCData`

## 参数

### **远程 IP 地址（255.255.255.255 表示广播）** — 数据发送到的远程主机的 IP 地址 `127.0.0.1`（默认值） | 点分四组表达式

指定要将 UDP 包发送到的远程主机的 IP 地址。

### **远程端口** — 数据发送到的远程主机的 IP 端口 `25000`（默认值） | 1 到 65,535 的整数

指定要将 UDP 包发送到的主机的端口号。

### **本地端口** — 目标上发送数据的应用程序的 IP 端口号 `-1`（默认值） | 1 到 65,535 的整数

指定目标上要从中发送 UDP 包的应用程序的端口号。默认值 `-1` 将本地端口号设置为随机可用端口号，并使用该端口发送 UDP 包。

### **字节序** — 字节序 `LittleEndian`（默认值） | `BigEndian`

UDP 包的字节序，指定为下列值之一：

- `LittleEndian` — 将 UDP 包的字节序设置为小端。
- `BigEndian` — 将 UDP 包的字节序设置为大端。

## 所属库

SoC Blockset / Processor I/O SoC Blockset / Host I/O

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要自动为您的设计生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅使用 SoC Builder 生成 SoC 设计。

Embedded Coder 为此模块生成事件驱动代码。此图显示了所生成代码实现的通用表示。

**注意**

与仿真中任务的时序相比，生成代码的时序测量值在任务实例执行期间可能有所不同。您可以将模型配置为在任务信号中使用数据缓存，以提高仿真与生成代码之间的一致性。有关详细信息，请参阅任务子系统信号的值与缓存。

## 版本历史

**在 R2019a 中引入**

## 描述

向远程主机发送 UDP 包

UDP Write 模块将 UDP（用户数据报协议）包从目标上的应用程序发送到远程主机。远程主机是您要将 UDP 包发送到的计算机或硬件。
