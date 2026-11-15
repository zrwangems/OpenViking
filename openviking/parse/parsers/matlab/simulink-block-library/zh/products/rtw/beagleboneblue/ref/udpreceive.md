---
type: simulink-block
title: 'UDP Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'udpreceive'
documentation_source_path: 'beagleboneblue/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 数据 [Nx1] 数组的输出端口

该输出端口将 UDP 包数据作为指定数据类型的一维向量发出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Size** — UDP 缓冲区中数据的大小 标量

该输出端口发出 UDP 缓冲区中数据的大小。

**数据类型：** `uint16`

## 参数

### **Local IP port** — 发送 UDP 主机使用的本地 IP 端口号 25000 (默认) | 标量

本地设备上的 IP 端口号，范围为 1 到 65535。该值默认为 `25000`。
本地设备是运行该模型的开发板。

### **Data type** — 消息输出中向量元素的数据类型 uint8 (默认) | 标量

这是消息输出中向量元素的数据类型。将该数据类型与用于创建 UDP 包的数据输入相匹配。

### **Data size (N)** — 每个 UDP 包中的数据元素数量 255 (默认) | 标量

设置每个 UDP 包中的数据元素数量。将数据大小与用于创建 UDP 包的数据大小相匹配。

### **Sample time** — 模块读取端口缓冲区的时间频率 0.1 (默认) | 标量

指定此模块读取端口缓冲区的频率。输入大于零的值。

较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

在 R2025b 中未记录。

## 描述

从互联网上的另一台 UDP 主机接收 UDP 包

从本地网络接收 UDP 包。模块输出 **data** 将 UDP 包数据作为指定数据类型的一维向量发出。模块输出 **size** 发出 UDP 缓冲区中数据的大小。

模块输出 `Data` 的数据类型取决于 **Data type** 参数。模块输出 `Size` 的数据类型为 `uint16`。

当 UDP Receive 等待新数据到达时，**size** 发出一串零。当新数据到达时，**size** 变为非零值。

如果您在主机计算机上仿真包含 UDP Receive 模块的模型（例如，Simulation > Normal），并从开发板向该模型发送 UDP 包，则 **data** 输出会发出数量不成比例的大量零。这是因为 Simulink® 软件将该模型作为自由运行应用程序进行仿真，其周期比开发板上运行的实时应用程序更短。换句话说，自由运行仿真输出零，是因为它在等待开发板上“较慢”的实时应用程序发送数据。如果两个应用程序都在开发板上运行，则不会发生这种不匹配。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，请检查是否有防病毒或防火墙软件可能正在阻止 UDP 流量。如果是这样，请尝试配置该软件以允许特定 IP 端口号的 UDP 流量。
