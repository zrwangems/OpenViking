---
type: simulink-block
title: 'TCP Client'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'tcpclient'
documentation_source_path: 'io_ref/tcpclient.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP Client

## 端口
```yaml
ports:
- name: Enable
  summary: 将模块连接到远程以太网设备 integer
  direction: input
- name: Status
  summary: 设备返回未连接或已连接的状态 0 | 1
  direction: output
```

### 输入

### **Enable** — 将模块连接到远程以太网设备 integer

如果 `Enable` 大于零，则模块连接到以太网设备。否则，模块不连接到以太网设备。
### 输出

### **Status** — 设备返回未连接或已连接的状态 `0` | `1`

状态值为以下之一：

- `0` — 未连接
- `1` — 已连接

作为最佳实践，将 TCP 配置模块的 `Status` 输出连接到关联的 TCP Send 和 TCP Receive 模块的 `Enable` 输入。
## 参数
```yaml
parameters:
- name: Use host-target connection
  summary: 使用开发计算机和目标计算机之间的以太网连接 'off'（默认）| 'on'
  group: ''
  block_parameter: useHostTargetConn
- name: Remote server IP address
  summary: 服务器设备的 IP 地址 x.x.x.x
  group: ''
  block_parameter: remoteAddress
- name: Remote server port
  summary: 服务器设备的端口号 1–65535
  group: ''
  block_parameter: remotePort
- name: Use Nagle's algorithm
  summary: 启用 Nagle 算法以合并数据包 on（默认）| off
  group: ''
  block_parameter: useNaglesAlgorithm
- name: Client IP address
  summary: 正在配置的客户端设备的 IP 地址 无值（默认）| x.x.x.x
  group: 高级参数
  block_parameter: clientAddress
- name: Client local port
  summary: 正在配置的客户端设备的 IP 端口 无值（默认）| 0–65535
  group: 高级参数
  block_parameter: clientPort
```

### **Use host-target connection** — 使用开发计算机和目标计算机之间的以太网连接 `'off'`（默认）| `'on'`

#### 依赖关系

当您选择此参数时，它会停用 **Client IP address** 参数，并将端口 `1` 到 `1023` 以及 `5500` 到 `5560` 从 TCP 使用中排除。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useHostTargetConn` |

### **Remote server IP address** — 服务器设备的 IP 地址 `x.x.x.x`

输入您要将客户端连接到的服务器的 IP 地址。

#### 程序化使用

|  |
| --- |
| **模块参数：** `remoteAddress` |

### **Remote server port** — 服务器设备的端口号 `1–65535`

输入您要将客户端连接到的服务器的端口号。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。

#### 程序化使用

|  |
| --- |
| **模块参数：** `remotePort` |

### **Use Nagle's algorithm** — 启用 Nagle 算法以合并数据包 `on`（默认）| `off`

启用 Nagle 算法以提高 TCP/IP 网络的效率。Nagle 算法减少了通过网络发送的数据包数量。这种效率提升的代价是 Nagle 算法在数据包通过网络发送之前引入了延迟。您可以通过为此模块禁用 Nagle 算法来减少网络延迟。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useNaglesAlgorithm` |

### 高级参数

### **Client IP address** — 正在配置的客户端设备的 IP 地址 无值（默认）| `x.x.x.x`

如果您使用的是专用以太网卡，此值必须与网络接口的 IP Config 模块中的 **Local IP Address** 参数匹配。Client IP address 字段的默认值为无值。此空字段意味着操作系统为 TCP 传输选择 Client IP address。

#### 程序化使用

|  |
| --- |
| **模块参数：** `clientAddress` |

### **Client local port** — 正在配置的客户端设备的 IP 端口 无值（默认）| `0–65535`

**Client IP address** 和 **Client local port** 的组合必须是唯一的。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。值 '-1'、'0' 或 'empty' 表示模块使用任何可用端口传输数据。

#### 程序化使用

|  |
| --- |
| **模块参数：** `clientPort` |
## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a：添加了启用或禁用 Nagle 算法的参数

您可以通过为 TCP Client 模块和 TCP Server 模块禁用 Nagle 算法来减少网络延迟（并降低网络效率）。有关详细信息，请参阅 **Use Nagle's algorithm** 模块参数。

### R2021b：更改了参数 Client IP Address 和 Client Port

TCP Client 模块的参数已更改。**Client IP address** 和 **Client port** 参数为可选参数。

## 描述

配置 TCP 客户端

TCP Client 模块用于配置一个 TCP 客户端。

参数 **Client IP address** 和 **Client port** 是可选的。**Client IP address** 适用于模块在 Speedgoat® 目标计算机上的实时应用程序中执行，或在 MATLAB® 开发计算机上的模型仿真中执行的情况。如果您的模型在开发计算机上的 Simulink® 中运行，您可以使用此模块向远程设备传输数据。在这种情况下，由 Windows® 操作系统决定网络连接。

如果实时应用程序中的 TCP Client 无法立即建立连接，则连接将异步建立，并在下一个时间步可用。
