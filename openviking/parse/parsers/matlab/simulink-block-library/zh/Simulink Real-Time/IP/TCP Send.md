---
type: simulink-block
title: 'TCP Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'tcpsend'
documentation_source_path: 'io_ref/tcpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Send

## 端口

### 输入

### **Enable** — 允许数据传输 integer

当 `Enable` > `0` 时，该模块尝试向远程设备发送数据。

作为最佳实践，将 TCP configure 模块的 `Status` 输出连接到关联的 TCP Send 和 TCP Receive 模块的 `Enable` 输入。

### **Data** — 要通过 TCP 网络传输的数据 vector

要传输到客户端设备的 `Length` 向量。

**数据类型：** `uint8`

### **Length** — 数据向量长度 double

要传输到客户端设备的 `uint8` 值的数量。
### 输出

### **Status** — 已发送字节数 double

返回传输到客户端设备的 `uint8` 值的数量。

## 参数

### **Send using** — IP 地址和端口对列表 只读：`x.x.x.x:y`

此参数为只读。

该模块从模型中的 TCP 配置模块接收 IP 地址和端口对列表。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。

#### 程序化使用

|  |
| --- |
| **模块参数：** `socketAddPort` |

### **Sample time** — 模块采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampleTime` |

## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

通过 TCP 网络向远程设备发送数据

TCP Send 模块将数据从 Speedgoat® 目标计算机上的服务器应用程序发送到远程客户端设备。
