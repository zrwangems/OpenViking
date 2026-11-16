---
type: simulink-block
title: 'TCP Server'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'tcpserver'
documentation_source_path: 'io_ref/tcpserver.html'
language: zh-CN
chinese_source: official
---

# TCP Server

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

### **Use host-target connection** — 在开发计算机与目标计算机之间使用以太网连接 `'off'` (默认) | `'on'`

#### 依赖关系

当您选择此参数时，它将停用 **Server IP address** 参数，并禁止 TCP 使用端口 `1` 至 `1023` 以及 `5500` 至 `5560`。

#### 编程用法

|  |
| --- |
| **模块参数：**`useHostTargetConn` |

### **Server IP address** — 正在配置的服务器设备的 IP 地址 `x.x.x.x`

若使用专用以太网卡，此值必须与目标计算机上为该以太网卡配置的 IP 地址相匹配。

#### 编程用法

|  |
| --- |
| **模块参数：**`serverAddress` |

### **Server port** — 正在配置的服务器设备的 IP 端口 `1–65535`

**Server IP address** 与 **Server port** 的组合必须是唯一的。

端口 `1` 至 `1023` 以及 `5500` 至 `5560` 专用于 Simulink Real-Time 通信。

#### 编程用法

|  |
| --- |
| **模块参数：**`serverPort` |

### **Use Nagle's algorithm** — 启用 Nagle 算法以合并数据包 `on` (默认) | `off`

启用纳格尔算法以提升 TCP/IP 网络的效率。纳格尔算法减少了通过网络发送的数据包数量。这种效率提升的代价是，纳格尔算法会在数据包通过网络发送前引入延迟。您可以通过禁用此模块的 Nagle 算法来降低网络延迟。

#### 编程用法

|  |
| --- |
| **模块参数：**`useNaglesAlgorithm` |

## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2020b 中推出**

### R2025a: 新增参数以启用或禁用 Nagle 算法

通过禁用 TCP Client 模块和 TCP Server 模块的 Nagle 算法，可降低网络延迟（同时降低网络效率）。有关更多信息，请参阅 **Use Nagle's algorithm** 模块参数。

## 描述

配置 TCP 服务器

TCP Server 模块用于配置 TCP 服务器。
