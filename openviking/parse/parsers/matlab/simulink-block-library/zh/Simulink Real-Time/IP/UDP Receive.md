---
type: simulink-block
title: 'UDP Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'udpreceive'
documentation_source_path: 'io_ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 接收到的数据向量

包含通过 UDP 网络接收到的数据的 `uint8` 向量。如果未接收到新数据包，则保持数据值不变。要确定是否接收到新数据包，请使用 **Length** 输出端口。如果启用 **Enable Simulink messages** 参数，则数据类型为 `UDP_Packet`。该数据类型包含：

- `IP_Address`：DataType: uint8，Complexity:
  real，Dimensions: [4 1]
- `IP_Port`：DataType: uint16，Complexity:
  real，Dimensions: 1
- `Length`：DataType: uint16，Complexity: real，
  Dimensions: 1
- `Data`：DataType: uint8，Complexity: real，
  Dimensions: [75 1]

**数据类型：** `uint8` | `UDP_Packet`

### **Length** — 接收到的字节数 double

当禁用 **Enable Simulink
messages** 参数时，此端口可用。Length 是接收到的新数据包中的字节数，否则为 `0`。如果接收到的字节数超过通过 **Data**
端口以 **Receive width** 定义的宽度输出的字节数，则多余的字节将被丢弃。

## 参数

### 常规参数

### **Use host-target connection** — 使用开发计算机和目标计算机之间的以太网连接 `'off'`（默认）| `'on'`

#### 依赖关系

当您选择此参数时，它会停用 **Local
IP address** 参数，并将端口
`1` 到 `1023` 以及
`5500` 到 `5560` 从 UDP 使用中排除。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `useHostTargetConn` |

### **Local IP address** — 用于接收数据的目标 IP 地址 `Use host-target connection`（默认）

当 **Local IP address** 设置为 `Use
host-target connection` 时，模块使用开发计算机和目标计算机之间的连接。
使用 `0.0.0.0` 绑定到 `INADDR_ANY`，
这使套接字能够接收广播数据报。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `ipAddress` |

### **Local port** — 用于接收数据的目标 UDP 端口 `1–65535`

指定用于接收数据的 UDP 端口。

端口 `1` 到 `1023` 以及
`5500` 到 `5560` 保留用于 Simulink Real-Time
通信。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `localPort` |

### **Receive width** — `Data` 输出向量的宽度 `1–65504`

确定 `Data` 输出向量的宽度。如果此值小于接收数据包中的字节数，则多余的字节将被丢弃。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `rcvWidth` |

### **Receive from any source** — 使接收方接受来自任何 IP 地址的数据 `on`（默认）| `off`

当 **Receive from any source** 为
`on` 时，模块接收来自任何可访问 IP 地址的数据。当其为 `off` 时，模块仅接收来自您在 **From IP address** 中指定的地址的数据。

要使 **From IP address** 参数可见，请清除 **Receive from any source** 复选框。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `rcvFmAny` |

### **From IP address** — 接收数据的来源 `x.x.x.x`

以点分十进制字符向量形式输入有效的 IP 地址，例如 `192.168.7.2`。您也可以使用返回有效 IP 地址字符向量的 MATLAB 表达式。

地址 `255.255.255.255` 是无效的 IP 地址。

要使此参数可见，请清除 **Receive from any source** 复选框。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `fmAddress` |

### **Sample time (-1 for inherited)** — 模块的采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `sampleTime` |

### **Enable Simulink messages** — 将数据作为消息处理 `off`（默认）| `on`

Enable Simulink messages 指示模块将数据作为消息处理。启用后，Length 端口将被移除。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `MessageOut` |

### **每个时间步的最大消息数** — 限制消息数 `1`（默认）| int

每个时间步的最大消息数数值限制在一个时间步内允许的消息数量。如果消息数量超过此限制，则会生成错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `maxPacket` |

## 所属库

Simulink Real-Time / IP

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

通过 UDP 网络从远程设备接收数据

UDP Receive 模块通过 UDP 网络从远程设备接收数据。它可以通过使用 MATLAB® 开发计算机与 Speedgoat® 目标计算机之间的连接来接收数据，也可以通过使用专用以太网卡来接收数据。如果使用专用以太网卡，请使用 Speedgoat 配置实用程序来配置专用以太网板。

参数 **Local IP address** 适用于模块在目标计算机上的实时应用程序中执行或在开发计算机上的模型仿真中执行的情况。如果您的模型在开发计算机上的 Simulink® 中运行，您可以使用此模块接收来自远程设备的数据。在这种情况下，Windows® 操作系统决定网络连接。
