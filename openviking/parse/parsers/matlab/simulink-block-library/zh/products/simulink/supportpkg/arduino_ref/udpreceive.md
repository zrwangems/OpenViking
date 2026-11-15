---
type: simulink-block
title: 'UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'udpreceive'
documentation_source_path: 'supportpkg/arduino_ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 接收到的 UDP 数据数值向量

从远程主机接收的 UDP 数据，以数值向量形式返回。使用 **数据类型** 参数设置此输出的数据类型。

如果在主机计算机上以正常模式仿真包含 UDP Receive 模块的模型，则当没有可用的 UDP 数据包时，**Data** 端口会在仿真的每一步输出零。作为自由运行应用程序，其周期短于 Android® 设备上运行的实时应用程序，输出端口 `Data` 可能会产生许多零。换句话说，自由运行仿真在等待 Android 设备上较慢的实时应用程序发送数据时会输出零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **本地 IP 端口** — 本地设备的 IP 端口号 `56789` (默认) | 从 1 到 65,535 的整数

指定用于接收 UDP 数据包的 IP 端口号。本地设备是运行该模型的 iOS 设备。

### **采样时间** — 采样时间 `1` (默认) | 非负标量

指定此模块读取 UDP 消息的频率，单位为 seconds。输入大于零的值。此值默认为采样时间 1 second。

较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2013b 中引入**

## 描述

通过 UDP 网络从远程主机接收数据

使用 UDP Receive 模块从远程主机接收用户数据报协议 (UDP) 数据。该模块从套接字缓冲区读取可用的 UDP 数据，并将数据作为向量输出。
