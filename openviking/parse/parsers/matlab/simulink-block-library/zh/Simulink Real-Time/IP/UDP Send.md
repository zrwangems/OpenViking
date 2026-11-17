---
type: simulink-block
title: 'UDP Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'udpsend'
documentation_source_path: 'io_ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口
```yaml
ports:
- name: Data
  summary: 要传输的数据向量
  direction: input
  data_types: uint8 | UDP_Packet
- name: Length
  summary: 要传输的数据字节数 double
  direction: input
```

### 输入

### **Data** — 要传输的数据向量

包含要通过 UDP 网络传输的数据的 `uint8` 向量。要确定要传输多少字节的数据，请使用 **Length** 输入端口。如果启用 **Enable Simulink messages** 参数，则数据类型为 `UDP_Packet`。使用 `slrealtime.createUDPPacketBusObj` 函数创建 `Simulink.Bus` 类型 `Ethernet_Packet`。此数据类型由以下部分组成：

- `IP_Address`：DataType: uint8, Complexity: real, Dimensions: [4 1]
- `IP_Port`：DataType: uint16, Complexity: real, Dimensions: 1
- `Length`：DataType: uint16, Complexity: real, Dimensions: 1
- `Data`：DataType: uint8, Complexity: real, Dimensions: [75 1]

**数据类型：** `uint8` | `UDP_Packet`

### **Length** — 要传输的数据字节数 double

当您禁用 **Enable Simulink messages** 参数时，此端口可用。Length 决定要传输的数据字节数。将 `Data` 向量的宽度指定为您预期传输的最大字节数。
## 参数
```yaml
parameters:
- name: Use host-target connection
  summary: 使用开发计算机与目标计算机之间的以太网连接 'off'（默认）| 'on'
  group: ''
  block_parameter: useHostTargetConn
- name: To IP address
  summary: 目标设备的 IP 地址 10.10.10.10（默认）| x.x.x.x
  group: ''
  block_parameter: toAddress
- name: To port
  summary: 目标设备的 UDP 端口 34（默认）| 1–65535
  group: ''
  block_parameter: toPort
- name: Sample time (-1 for inherited)
  summary: 模块的采样时间 -1（默认）| 数值
  group: ''
  block_parameter: sampleTime
- name: Enable Simulink messages
  summary: 将数据作为消息处理 off（默认）| on
  group: ''
  block_parameter: MessageIn
- name: Local IP address
  summary: 用于发送数据的源 IP 地址 无值（默认）| x.x.x.x
  group: 高级参数
  block_parameter: ipAddress
- name: Local port
  summary: 用于传输数据的源 UDP 端口 无值（默认）| 0–65535 | -1
  group: 高级参数
  block_parameter: localPort
```

### **Use host-target connection** — 使用开发计算机与目标计算机之间的以太网连接 `'off'`（默认）| `'on'`

#### 依赖关系

当您选择此参数时，它会停用 **Local IP address** 参数，并将端口 `1` 到 `1023` 以及 `5500` 到 `5560` 排除在 UDP 使用之外。

#### 编程使用

|  |
| --- |
| **模块参数**：`useHostTargetConn` |

### **To IP address** — 目标设备的 IP 地址 `10.10.10.10`（默认）| `x.x.x.x`

指定目标设备的 IP 地址。要广播到本地子网上的所有设备，请发送到 `255.255.255.255`。

#### 编程使用

|  |
| --- |
| **模块参数**：`toAddress` |

### **To port** — 目标设备的 UDP 端口 `34`（默认）| `1–65535`

指定目标设备的 UDP 端口。与 **To IP address** 一起，此参数定义数据传输的目标。

#### 编程使用

|  |
| --- |
| **模块参数**：`toPort` |

### **Sample time (-1 for inherited)** — 模块的采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。

#### 编程使用

|  |
| --- |
| **模块参数**：`sampleTime` |

### **Enable Simulink messages** — 将数据作为消息处理 `off`（默认）| `on`

Enable Simulink messages 指示模块将数据作为消息处理。启用后，Length 端口将被移除。

#### 编程使用

|  |
| --- |
| **模块参数**：`MessageIn` |

### 高级参数

### **Local IP address** — 用于发送数据的源 IP 地址 无值（默认）| `x.x.x.x`

当 **Local IP address** 设置为 **Use host-target connection** 时，模块使用开发计算机与目标计算机之间的连接。当 **To IP address** 指定为多播地址时，本地 IP 地址用于确定发送多播数据报的出站接口。Local IP address 字段的默认值为无值。此空字段表示操作系统为 UDP 传输选择本地 IP 地址。

#### 编程使用

|  |
| --- |
| **模块参数**：`ipAddress` |

### **Local port** — 用于传输数据的源 UDP 端口 无值（默认）| `0–65535` | `-1`

指定用于传输数据的本地 UDP 端口。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。

值 `0`、`−1` 或无值表示模块使用任何可用端口传输数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`localPort` |
## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2021b：更改了参数 Local IP Address 和 Local Port

UDP Send 模块的参数已更改。对于单播、广播和多播，参数 **Local IP address** 和 **Local port** 是可选的。

### R2021a：添加了多播支持

添加了 UDP Multicast Receive 模块，并且 UDP Send 模块具有多播支持。这些模块为 UDP 通信协议提供多播消息支持。

## 描述

通过 UDP 网络向远程设备发送数据

UDP Send 模块通过 UDP 网络向远程设备发送数据。该模块可以通过使用 MATLAB® 开发计算机与 Speedgoat® 目标计算机之间的连接来发送数据，也可以通过使用专用以太网卡来发送数据。如果使用专用以太网卡，请使用 Speedgoat 配置实用程序配置专用以太网板。该实用程序提供的设置之一是 **Default Gateway** 设置。当使用 UDP Send 模块广播到 255.255.255.255 时，用于广播的 IP 接口基于此 **Default Gateway** 设置。

要广播到本地子网上的所有设备，请将 **To IP address** 设置为 `255.255.255.255`。否则，请将 **To IP address** 设置为有效的 IP 地址。

对于单播、广播和多播，参数 **Local IP address** 和 **Local port** 是可选的。**Local IP address** 适用于该模块在目标计算机上的实时应用程序中执行或在开发计算机上的模型仿真中执行的情况。如果您的模型在开发计算机上的 Simulink® 中运行，您可以使用此模块向远程设备发送数据。在这种情况下，Windows® 操作系统将确定网络连接。
