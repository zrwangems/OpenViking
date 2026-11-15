---
type: simulink-block
title: 'TCP Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / TCP'
documentation_page: 'tcpsend'
documentation_source_path: 'io_ref/tcpsend.html'
language: zh-CN
chinese_source: official
---

# TCP Send

## 端口

### 输入

### **Enable** — 允许数据传输 整数

当 `Enable` > `0` 时，该模块尝试向远程设备传输数据。

作为最佳做法，应将 TCP 配置模块的 `Status` 输出端口连接至关联的 TCP Send 和 TCP Receive 模块的 `Enable` 输入端口。

### **Data** — 通过 TCP 网络传输的数据 向量

向客户端设备传输的 `Length` 向量。

**数据类型:** `uint8`

### **Length** — 数据向量的长度 双精度

需要传输至客户端设备的 `uint8` 值的数量。
### 输出

### **Status** — 发送的字节数 双精度

返回传输到客户端设备的 `uint8` 值的数量。

## 参数

### **Send using** — IP 地址与端口对列表 只读: `x.x.x.x:y`

此 参数 为只读。

该模块从模型中的 TCP 配置模块接收 IP 地址与端口对的列表。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。

#### 编程用法

|  |
| --- |
| **模块参数：**`socketAddPort` |

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

通过 TCP 网络向远程设备发送数据

TCP Send 模块将数据从 Speedgoat® 目标计算机上的服务器应用程序发送至远程客户端设备。
