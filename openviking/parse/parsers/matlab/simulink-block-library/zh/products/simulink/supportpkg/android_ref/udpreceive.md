---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/android_ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 接收的 UDP 数据，数值向量

从远程主机接收的 UDP 数据，以数值向量形式返回。使用 **Data type** 参数设置此输出的数据类型。

如果在正常模式下于主机上仿真包含 UDP Receive 模块的模型，则当没有可用的 UDP 包时，**Data** 端口会在仿真的每个步长输出零。作为周期比运行在 Android® 设备上的实时应用程序更短的自由运行应用程序，输出端口 `Data` 可能会产生许多零。换言之，自由运行仿真在等待 Android 设备上较慢的实时应用程序发送数据时会输出零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Size** — 接收的 UDP 包的大小，非负标量

接收的 UDP 包的大小，以非负标量形式返回。当模块等待新数据到达时，此端口输出 `0`。当新数据到达时，此端口值变为接收到的 UDP 包的长度。

**数据类型：** `uint16`

## 参数

### **Local IP port** — 本地设备的 IP 端口号 `25000`（默认）| 1 到 65,535 的整数

指定本地设备的 IP 端口号。本地设备是运行该模型的 iOS 设备。

### **Data type** — 输出 UDP 包的数据类型 `uint8`（默认）| `uint16` | `unit32` | `int8` | `int16` | `int32` | `single` | `double`

设置输出中向量元素的数据类型。使此数据类型与用于创建 UDP 包的数据输入匹配。

### **Data size (N)** — 输出 UDP 包的大小 `255`（默认）| 正整数

指定每个 UDP 包中的数据元素数量。使其与用于创建 UDP 包的数据大小匹配。

### **Sample time** — 采样时间 `0.01`（默认）| 非负标量

指定该模块读取端口缓冲区的频率。输入大于零的值。

**注意**

较小的 **Sample time** 值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

通过 UDP 网络从远程主机接收数据

使用 UDP Receive  模块从远程主机接收用户数据报协议 (UDP) 数据。该模块从套接字缓冲区读取可用的 UDP 数据，并将该数据作为向量输出。
