---
type: simulink-block
title: 'UDP Multicast Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'udpmulticastreceive'
documentation_source_path: 'io_ref/udpmulticastreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Multicast Receive

## 端口
```yaml
ports:
- name: Data
  summary: 接收到的数据向量
  direction: output
  data_types: uint8
- name: Length
  summary: 接收到的字节数 double
  direction: output
```

### 输出

### **Data** — 接收到的数据向量

包含通过 UDP 网络接收到的数据的 `uint8` 向量。如果未接收到新数据包，则保持数据值不变。要确定是否已接收到新数据包，请使用 **Length** 输出端口。

**数据类型：** `uint8`

### **Length** — 接收到的字节数 double

新接收到的数据包中的字节数，否则为 `0`。如果接收到的字节数超过通过接收端口输出的字节数（宽度由 **Receive width** 定义），则多余的字节将被丢弃。
## 参数
```yaml
parameters:
- name: Bind address
  summary: 用于接收多播数据的绑定 IP 地址 0.0.0.0（默认值）
  group: 常规参数
  block_parameter: bindAddress
- name: Local port
  summary: 用于接收数据的目标 UDP 端口 1–65535
  group: 常规参数
  block_parameter: localPort
- name: Receive width
  summary: Data 输出向量的宽度 16（默认值） | 1–65504
  group: 常规参数
  block_parameter: rcvWidth
- name: Group address
  summary: 要加入的多播组 {}（默认值） | {'x.x.x.x'} | 点分十进制字符向量
  group: 常规参数
  block_parameter: multicastAddress
- name: Group interface
  summary: 用于接收数据的本地 IP 接口 {}（默认值） | {'x.x.x.x'} | 点分十进制字符向量
  group: 常规参数
  block_parameter: multicastInterface
- name: Sample time (-1 for inherited)
  summary: 模块的采样时间 -1（默认）| 数值
  group: 常规参数
  block_parameter: sampleTime
```

### 常规参数

### **Bind address** — 用于接收多播数据的绑定 IP 地址 `0.0.0.0`（默认值）

**Bind address** 可以是 `0.0.0.0` 或一个多播地址。当 **Bind address** 设置为 `0.0.0.0` 时，模块绑定到 `INADDR_ANY`，这使套接字能够在所有接口上接收数据报。此设置会启用模块掩码上的 **Group address** 字段。当 **Bind address** 设置为多播 IP 地址时，模块掩码上的 **Group address** 字段将被隐藏。

如果 **Bind address** 设置为 `0.0.0.0`，并且模块配置在发送单播消息的组接口上，则该模块也可以接收单播消息。之所以会发生这种单播消息接收，是因为地址 `0.0.0.0` 允许监听目标计算机所有接口上的任何消息。要避免这种单播消息接收操作，请使用多播地址作为绑定地址。使用该设置后，模块仅接收多播消息，不接收单播消息。

#### 程序化使用

|  |
| --- |
| **模块参数：** `bindAddress` |

### **Local port** — 用于接收数据的目标 UDP 端口 `1–65535`

指定用于接收数据的 UDP 端口。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。

#### 程序化使用

|  |
| --- |
| **模块参数：** `localPort` |

### **Receive width** — `Data` 输出向量的宽度 `16`（默认值） | `1–65504`

确定 `Data` 输出向量的宽度。如果此值小于接收到的数据包中的字节数，则多余的字节将被丢弃。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rcvWidth` |

### **Group address** — 要加入的多播组 `{}`（默认值） | `{'x.x.x.x'}` | 点分十进制字符向量

当绑定地址为多播地址时，此字段将被隐藏。以点分十进制字符向量的形式输入有效的 IP 地址，例如 `{'224.0.0.0'}`。可以指定一个或多个组地址。

如果组 IP 地址不是 `224.0.0.0` 到 `239.255.255.255` 范围内的有效多播地址，UDP Multicast Receive 模块将在模型更新时发出错误。

**示例：** `{'224.100.1.1'}`

**示例：** `{'224.100.1.1', '224.100.1.2'}`

#### 程序化使用

|  |
| --- |
| **模块参数：** `multicastAddress` |

### **Group interface** — 用于接收数据的本地 IP 接口 `{}`（默认值） | `{'x.x.x.x'}` | 点分十进制字符向量

**Group interface** IP 地址指定应通过哪些接口接收传入的多播消息。当绑定地址为 `0.0.0.0` 时，**Group address** 字段中指定的多播组通过指定的组接口接收消息。当绑定地址为多播地址时，该地址通过指定的组接口接收消息。以点分十进制字符向量的形式输入有效的接口 IP 地址，例如 `{'192.168.7.5'}`。您也可以使用返回有效 IP 地址字符向量的 MATLAB 表达式。可以指定一个或多个组接口。

**示例：** `{'192.168.7.5'}`

**示例：** `{'192.168.7.5', '192.168.7.10'}`

#### 程序化使用

|  |
| --- |
| **模块参数：** `multicastInterface` |

### **Sample time (-1 for inherited)** — 模块的采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。

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

**在 R2021a 中引入**

## 描述

通过 UDP 网络从远程设备接收数据

UDP Multicast Receive 模块通过 UDP 网络从远程设备接收组播数据。它可以通过使用 MATLAB® 开发计算机与 Speedgoat® 目标计算机之间的连接来接收数据，也可以通过使用专用以太网卡来接收数据。如果使用专用以太网卡，请使用 Speedgoat 配置实用程序配置专用以太网板。

UDP Multicast Receive 模块在目标计算机上运行的实时应用程序中运行。该模块不会在开发计算机上的模型仿真中运行。

最多可加入 20 个组播组。此数量由模块掩码上的组地址和组接口字段的乘积决定。
