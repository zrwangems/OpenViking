---
type: simulink-block
title: 'TCP Client'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / TCP'
documentation_page: 'tcpclient'
documentation_source_path: 'io_ref/tcpclient.html'
language: zh-CN
chinese_source: official
---

# TCP Client

## 端口

### 输入

### **Enable** — 将模块连接至远程以太网设备 整数

如果 `Enable` 大于零，则该模块连接到以太网设备。否则，该模块将无法连接到以太网设备。
### 输出

### **Status** — 设备返回未连接或已连接的状态 `0` | `1`

状态值为以下之一：

- `0` - 未连接
- `1` - 互联

作为最佳做法，应将 TCP 配置模块的 `Status` 输出端口连接至关联的 TCP Send 和 TCP Receive 模块的 `Enable` 输入端口。

## 参数

### **Use host-target connection** — 在开发计算机和目标计算机之间使用以太网连接 `'off'` (默认) | `'on'`

#### 依赖关系

选择此参数时，将停用 **Client IP address** 参数，并禁止 TCP 使用端口范围 `1` 至 `1023` 以及 `5500` 至 `5560`。

#### 编程用法

|  |
| --- |
| **模块参数：**`useHostTargetConn` |

### **Remote server IP address** — 服务器设备的 IP 地址 `x.x.x.x`

输入您要连接客户端的服务器的 IP 地址。

#### 编程用法

|  |
| --- |
| **模块参数：**`remoteAddress` |

### **Remote server port** — 服务器设备的端口号 `1–65535`

输入您要连接客户端的服务器的端口号。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。

#### 编程用法

|  |
| --- |
| **模块参数：**`remotePort` |

### **Use Nagle's algorithm** — 启用 Nagle 算法以合并数据包 `on` (默认) | `off`

启用纳格尔算法以提升 TCP/IP 网络的效率。纳格尔算法减少了通过网络发送的数据包数量。这种效率提升的代价是，纳格尔算法会在数据包通过网络发送前引入延迟。您可以通过禁用此模块的 Nagle 算法来降低网络延迟。

#### 编程用法

|  |
| --- |
| **模块参数：**`useNaglesAlgorithm` |

### 高级参数

### **Client IP address** — 正在配置的客户端设备的 IP 地址 无值 (默认) | `x.x.x.x`

若使用专用以太网卡，此值必须与网络接口的 IP Config 模块中的 **Local IP Address** 参数相匹配。客户端 IP 地址字段的默认值为空值。此处留空表示操作系统将为 TCP 传输选择客户端 IP 地址。

#### 编程用法

|  |
| --- |
| **模块参数：**`clientAddress` |

### **Client local port** — 正在配置的客户端设备的 IP 端口 无值 (默认) | `0–65535`

**Client IP address** 与 **Client local port** 的组合必须是唯一的。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。值 '-1'、'0' 或 '空' 表示该模块使用任何可用端口传输数据。

#### 编程用法

|  |
| --- |
| **模块参数：**`clientPort` |

## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

### R2025a: 新增参数以启用或禁用 Nagle 算法

通过禁用 TCP Client 模块和 TCP Server 模块的 Nagle 算法，可降低网络延迟（同时降低网络效率）。有关更多信息，请参阅 **Use Nagle's algorithm** 模块参数。

### R2021b: 已更改参数：客户端 IP 地址和客户端端口

TCP Client 模块的参数已更改。参数 **Client IP address** 和 **Client port** 是可选的。

## 描述

配置 TCP 客户端

TCP Client 模块用于配置 TCP 客户端。

参数 **Client IP address** 和 **Client port** 是可选的。当模块在实时应用程序中于 Speedgoat® 目标计算机上执行，或在模型仿真中于 MATLAB® 开发计算机上运行时，**Client IP address** 适用。如果您的模型在开发计算机的 Simulink® 中运行，则可使用此模块将数据传输至远程设备。在此情况下，Windows® 操作系统负责确定网络连接。

若实时应用中的 TCP 客户端无法立即建立连接，则该连接将异步建立，并在下一个时间步中生效。
