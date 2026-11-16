---
type: simulink-block
title: 'UDP Receive'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'udpreceive'
documentation_source_path: 'nvidia/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 从发送 UDP 主机接收的 UDP 数据包 `vector`（默认）

在每个采样时间，该端口将接收到的数据包内容输出为数据向量，其大小由 **数据大小 (N)** 参数指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Size** — 确定在给定时步是否接收到请求的数据 `scalar`（默认）

如果在给定时步接收到数据，该端口输出 0。否则，它会输出一个非零值，表示没有新数据可用。

**数据类型：** `uint8`

## 参数

### **本地 IP 端口** — 用于接收数据的 NVIDIA® Jetson™ 板上的 IP 端口 `25000` | `[1,65535]` 范围内的正整数

指定您希望从其接收数据包的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

### **数据类型** — UDP 数据包中元素的数据类型 `uint8`（默认） | `boolean` | `uint16` | `uint32` | `int8` | `int16` | `int32` | `single` | `double`

选择该模块接收的 UDP 数据包中元素的数据类型。每个元素的大小取决于其数据类型。

### **数据大小** — 每个 UDP 数据包中的数据元素数 `255`（默认）

指定您希望在每个数据包中接收的元素数量。

### **采样时间 (seconds)** — 模块接收数据的时间频率 `0.1`（默认） | `scalar`

指定该模块读取端口缓冲区的频率。输入大于 `0` 的值或 `-1`（用于继承采样时间）。

当您将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

此值默认为 `0.1` seconds 的采样时间。
较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

NVIDIA Jetson 和 NVIDIA DRIVE / Network

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

从 UDP 主机接收 UDP 数据包

UDP Receive 模块从 UDP 主机接收 UDP 数据包。使用该模块进行无状态、无连接的数据交换。

在每个采样中，该模块将 UDP 数据包的内容输出为数据向量，其大小由 **数据大小 (N)** 参数指定。

模块输出 `Data` 的数据类型取决于 **数据类型** 参数。模块输出 `Size` 的数据类型为 `uint16`。

**注意**

您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置该软件以允许来自特定 IP 端口号的流量。
