---
type: simulink-block
title: 'TCP Receive'
family: 'slrealtime'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'tcpreceive'
documentation_source_path: '../slrealtime/io_ref/tcpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Receive

## 端口
```yaml
ports:
- name: Enable
  summary: 允许数据接收 integer
  direction: input
- name: Data
  summary: 从远程客户端接收的数据 vector
  direction: output
  data_types: uint8
- name: Length
  summary: 数据向量的实际大小 double
  direction: output
```

### 输入

### **Enable** — 允许数据接收 integer

当 `Enable` > `0` 时，该模块尝试接收发送到远程设备的数据。

作为最佳实践，将 TCP configure 模块的 `Status` 输出连接到关联的 TCP Send 和 TCP Receive 模块的 `Enable` 输入。
### 输出

### **Data** — 从远程客户端接收的数据 vector

参数 **Receive width** 决定数据向量的最大大小。

**数据类型：** `uint8`

### **Length** — 数据向量的实际大小 double

要测试数据项数量是否超过数据输出端口的宽度，请使用此值。
## 参数
```yaml
parameters:
- name: Receive using
  summary: 'IP 地址和端口对列表 Read-only: x.x.x.x:y'
  group: ''
  block_parameter: socketAddPort
- name: Receive width
  summary: 数据向量的最大预期长度 1–65504
  group: ''
  block_parameter: rcvWidth
- name: Sample time
  summary: 模块的采样时间 -1 (default) | numeric
  group: ''
  block_parameter: sampleTime
```

### **Receive using** — IP 地址和端口对列表 Read-only: `x.x.x.x:y`

此参数为只读。

该模块从模型中的 TCP 配置模块接收 IP 地址和端口对列表。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。

#### 编程使用

|  |
| --- |
| **模块参数**：`socketAddPort` |

### **Receive width** — 数据向量的最大预期长度 `1–65504`

该模块期望从客户端设备接收的 `uint8` 值的最大数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`rcvWidth` |

### **Sample time** — 模块的采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程使用

|  |
| --- |
| **模块参数**：`sampleTime` |
## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

通过 TCP 网络从远程设备接收数据

TCP Receive 模块接收从远程客户端设备发送到 Speedgoat® 目标计算机上服务器应用程序的数据。
