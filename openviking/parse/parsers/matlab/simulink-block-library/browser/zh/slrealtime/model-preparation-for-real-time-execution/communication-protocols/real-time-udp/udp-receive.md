---
type: simulink-block
title: 'UDP Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / Real-Time UDP'
documentation_page: 'udpreceive'
documentation_source_path: 'io_ref/udpreceive.html'
language: zh-CN
chinese_source: official
---

# UDP Receive

## 端口

### 输出

### **Data** — 接收到的数据 向量

包含通过 UDP 网络接收的数据的 `uint8` 向量。若未收到新数据包，则保持数据值不变。要确定是否已接收到新数据包，请使用 **Length** 输出端口。如果启用 **Enable Simulink messages** 参数，数据类型为 `UDP_Packet`。该数据类型包含：

- `IP_Address`:数据类型：uint8，复杂度：实数，维度：[4 1]
- `IP_Port`:数据类型：uint16，复杂度：实数，维度：1
- `Length`:数据类型：uint16，复杂度：实数，维度：1
- `Data`:数据类型：uint8，复杂度：实数，维度：[75 1]

**数据类型:** `uint8` | `UDP_Packet`

### **Length** — 接收的字节数 双精度

当禁用 **Enable Simulink messages** 参数时，此端口可用。长度字段表示新接收数据包的字节数，否则为 `0`。若接收到的字节数超过通过宽度由 **Receive width** 定义的 **Data** 端口所能输出的字节数，则多余字节将被丢弃。

## 参数

### 通用参数

### **Use host-target connection** — 在开发计算机和目标计算机之间使用以太网连接 `'off'` (默认) | `'on'`

#### 依赖关系

选择此参数时，将停用 **Local IP address** 参数，并禁止 UDP 使用端口范围 `1` 至 `1023` 以及 `5500` 至 `5560`。

#### 编程用法

|  |
| --- |
| **模块参数：**`useHostTargetConn` |

### **Local IP address** — 接收数据的目标 IP 地址 **Use host-target connection** (默认)

当 **Local IP address** 设置为 **Use host-target connection** 时，该模块将使用开发计算机与目标计算机之间的连接。使用 `0.0.0.0` 绑定到 `INADDR_ANY`，这将使套接字能够接收广播数据报。

#### 编程用法

|  |
| --- |
| **模块参数：**`ipAddress` |

### **Local port** — 接收数据的目标 UDP 端口 `1–65535`

指定用于接收数据的 UDP 端口。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。

#### 编程用法

|  |
| --- |
| **模块参数：**`localPort` |

### **Receive width** — `Data` 输出向量的宽度 `1–65504`

确定 `Data` 输出向量的宽度。如果该值小于接收数据包中的字节数，则多余的字节将被丢弃。

#### 编程用法

|  |
| --- |
| **模块参数：**`rcvWidth` |

### **Receive from any source** — 使接收方接受来自任何 IP 地址的数据 `on` (默认) | `off`

当 **Receive from any source** 变为 `on` 时，该模块将接收来自任何可访问 IP 地址的数据。当设置为 `off` 时，该模块仅接收来自 **From IP address** 中指定地址的数据。

要使 **From IP address** 参数可见，请清除 **Receive from any source** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：**`rcvFmAny` |

### **From IP address** — 接收数据的来源 `x.x.x.x`

请输入有效的 IP 地址，格式为点分十进制字符向量，例如：`192.168.7.2`。您还可以使用一个返回有效 IP 地址作为字符向量的 MATLAB 表达式。

地址 `255.255.255.255` 是一个无效的 IP 地址。

要使此参数可见，请清除 **Receive from any source** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：**`fmAddress` |

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
| **模块参数：**`MessageOut` |

### **Maximum messages per timestep** — 消息限值 `1` (默认) | int

每时间步最大消息数值限制了允许在单个时间步中处理的消息数量。如果消息数量超过此限制，则会生成错误。

#### 编程用法

|  |
| --- |
| **模块参数：**`maxPacket` |

## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

通过 UDP 网络从远程设备接收数据

UDP Receive 模块通过 UDP 网络从远程设备接收数据。它可通过连接 MATLAB® 开发计算机与 Speedgoat® 目标计算机的通道接收数据，或通过专用以太网卡实现数据接收。若使用专用以太网卡，请使用 Speedgoat 配置工具来配置专用以太网板。

参数 **Local IP address** 在以下两种情况下生效：当模块在目标计算机上的实时应用程序中执行时，或在开发计算机上的模型仿真中执行时。如果您的模型在开发计算机的 Simulink® 中运行，则可使用此模块将数据接收至远程设备。在此情况下，Windows® 操作系统负责确定网络连接。
