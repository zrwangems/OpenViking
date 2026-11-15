---
type: simulink-block
title: 'TCP Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / TCP'
documentation_page: 'tcpreceive'
documentation_source_path: 'io_ref/tcpreceive.html'
language: zh-CN
chinese_source: official
---

# TCP Receive

## 端口

### 输入

### **Enable** — 允许数据接收 整数

当 `Enable` > `0` 时，该模块尝试接收发往远程设备的数据。

作为最佳做法，应将 TCP 配置模块的 `Status` 输出端口连接至关联的 TCP Send 和 TCP Receive 模块的 `Enable` 输入端口。
### 输出

### **Data** — 从远程客户端接收到的数据 向量

参数 **Receive width** 决定数据向量的最大尺寸。

**数据类型:** `uint8`

### **Length** — 数据向量的实际大小 双精度

要测试数据项的数量是否超过数据输出端口的宽度，请使用此值。

## 参数

### **Receive using** — IP 地址与端口对列表 只读: `x.x.x.x:y`

此 参数 为只读。

该模块从模型中的 TCP 配置模块接收 IP 地址与端口对的列表。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。

#### 编程用法

|  |
| --- |
| **模块参数：**`socketAddPort` |

### **Receive width** — 数据向量的最大预期长度 `1–65504`

该模块预期从客户端设备接收的 `uint8` 值的最大数量。

#### 编程用法

|  |
| --- |
| **模块参数：**`rcvWidth` |

### **Sample time** — 模块采样时间 `-1` (默认) | 数值

输入基本采样时间或其倍数。`-1` 表示采样时间被继承。

#### 编程用法

|  |
| --- |
| **模块参数：**`sampleTime` |

## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

通过 TCP 网络从远程设备接收数据

TCP Receive 模块接收来自远程客户端设备的数据，并将数据发送至目标计算机 Speedgoat® 上的服务器应用程序。
