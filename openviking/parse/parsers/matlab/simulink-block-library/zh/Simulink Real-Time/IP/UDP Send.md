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
chinese_source: official
---

# UDP Send

## 端口

### 输入

### **Data** — 待传输的数据 向量

包含通过 UDP 网络传输数据的 `uint8` 向量。要确定传输多少字节的数据，请使用 **Length** 输入端口。如果启用 **Enable Simulink messages** 参数，数据类型为 `UDP_Packet`。使用 `slrealtime.createUDPPacketBusObj` 函数创建 `Simulink.Bus` 类型的 `Ethernet_Packet`。该数据类型包含：

- `IP_Address`:数据类型：uint8，复杂度：实数，维度：[4 1]
- `IP_Port`:数据类型：uint16，复杂度：实数，维度：1
- `Length`:数据类型：uint16，复杂度：实数，维度：1
- `Data`:数据类型：uint8，复杂度：实数，维度：[75 1]

**数据类型:** `uint8` | `UDP_Packet`

### **Length** — 要传输的数据字节数 双精度

当禁用 **Enable Simulink messages** 参数时，此端口可用。Length 决定要传输的数据字节数。将 `Data` 向量的宽度指定为预期传输的最大字节数。

## 参数

### **Use host-target connection** — 在开发计算机和目标计算机之间使用以太网连接 `'off'` (默认) | `'on'`

#### 依赖关系

选择此参数时，将停用 **Local IP address** 参数，并禁止 UDP 使用端口范围 `1` 至 `1023` 以及 `5500` 至 `5560`。

#### 编程用法

|  |
| --- |
| **模块参数：**`useHostTargetConn` |

### **To IP address** — 目标设备的 IP 地址 `10.10.10.10` (默认) | `x.x.x.x`

指定目标设备的 IP 地址。要向本地子网中的所有设备广播，请发送至 `255.255.255.255`。

#### 编程用法

|  |
| --- |
| **模块参数：**`toAddress` |

### **To port** — 目标设备的 UDP 端口 `34` (默认) | `1–65535`

指定目标设备的 UDP 端口。对于 **To IP address**，此参数定义数据传输的目的地。

#### 编程用法

|  |
| --- |
| **模块参数：**`toPort` |

### **Sample time (-1 for inherited)** — 模块采样时间 `-1` (默认) | 数值

输入基本采样时间或基本采样时间的倍数。

#### 编程用法

|  |
| --- |
| **模块参数：**`sampleTime` |

### **Enable Simulink messages** — 数据作为消息 `off` (默认) | `on`

启用 Simulink 消息将指示模块将数据视为消息。启用后，长度端口将被移除。

#### 编程用法

|  |
| --- |
| **模块参数：**`MessageIn` |

### 高级参数

### **Local IP address** — 发送数据的源 IP 地址 无值 (默认) | `x.x.x.x`

当 **Local IP address** 设置为 **Use host-target connection** 时，该模块将使用开发计算机与目标计算机之间的连接。当指定 **To IP address** 作为多播地址时，将使用本地 IP 地址来确定发送多播数据报的出站接口。本地 IP 地址字段的默认值为无值。此处留空表示操作系统将为 UDP 传输选择本地 IP 地址。

#### 编程用法

|  |
| --- |
| **模块参数：**`ipAddress` |

### **Local port** — 源 UDP 端口用于传输数据 无值 (默认) | `0–65535` | `-1`

指定用于传输数据的本地 UDP 端口。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。

值 `0`、`−1` 或无值表示该模块通过任何可用端口传输数据。

#### 编程用法

|  |
| --- |
| **模块参数：**`localPort` |

## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

### R2021b: 已更改参数：本地 IP 地址和本地端口

UDP Send 模块的参数已更改。对于单播、广播和组播，参数 **Local IP address** 和 **Local port** 是可选的。

### R2021a: 新增多播支持

已添加 UDP Multicast Receive 模块，且 UDP Send 模块支持多播功能。这些模块为 UDP 通信协议提供多播消息支持。

## 描述

通过 UDP 网络向远程设备发送数据

UDP Send 模块通过 UDP 网络向远程设备发送数据。该模块可通过连接 MATLAB® 开发计算机与 Speedgoat® 目标计算机的通道发送数据，或通过专用以太网卡实现数据传输。若使用专用以太网卡，请使用 Speedgoat 配置工具来配置专用以太网板。该实用程序提供的设置之一是 **Default Gateway** 设置。使用 UDP Send 模块向 255.255.255.255 广播时，广播所用的 IP 接口基于此 **Default Gateway** 设置。

要向本地子网中的所有设备广播，请将 **To IP address** 设置为 `255.255.255.255`。否则，将 **To IP address** 设置为有效的 IP 地址。

对于单播、广播和组播，参数 **Local IP address** 和 **Local port** 是可选的。当模块在目标计算机上的实时应用程序中执行，或在开发计算机上的模型仿真中执行时，**Local IP address** 适用。如果您的模型在开发计算机的 Simulink® 中运行，则可使用此模块将数据传输至远程设备。在此情况下，Windows® 操作系统负责确定网络连接。
