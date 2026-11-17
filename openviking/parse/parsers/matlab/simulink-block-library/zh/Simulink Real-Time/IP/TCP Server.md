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
chinese_source: worker-translation
---

# TCP Server

## 端口
```yaml
ports:
- name: Enable
  summary: 将模块连接到远程以太网设备 整数
  direction: input
- name: Status
  summary: 设备返回未连接或已连接的状态 0 | 1
  direction: output
```

### 输入

### **Enable** — 将模块连接到远程以太网设备 整数

如果 `Enable` 大于零，模块将连接到以太网设备。否则，模块不会连接到以太网设备。

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
  summary: 使用开发计算机与目标计算机之间的以太网连接 'off'（默认）| 'on'
  group: ''
  block_parameter: useHostTargetConn
- name: Server IP address
  summary: 正在配置的服务器设备的 IP 地址 x.x.x.x
  group: ''
  block_parameter: serverAddress
- name: Server port
  summary: 正在配置的服务器设备的 IP 端口 1–65535
  group: ''
  block_parameter: serverPort
- name: Use Nagle's algorithm
  summary: 启用 Nagle 算法以合并数据包 on（默认）| off
  group: ''
  block_parameter: useNaglesAlgorithm
```

### **Use host-target connection** — 使用开发计算机与目标计算机之间的以太网连接 `'off'`（默认）| `'on'`

#### 依赖关系

当您选择此参数时，它会停用 **Server IP address** 参数，并将端口 `1` 到 `1023` 以及 `5500` 到 `5560` 排除在 TCP 使用之外。

#### 编程使用

|  |
| --- |
| **模块参数：** `useHostTargetConn` |

### **Server IP address** — 正在配置的服务器设备的 IP 地址 `x.x.x.x`

如果您使用的是专用以太网卡，此值必须与目标计算机上以太网卡配置的 IP 地址匹配。

#### 编程使用

|  |
| --- |
| **模块参数：** `serverAddress` |

### **Server port** — 正在配置的服务器设备的 IP 端口 `1–65535`

**Server IP address** 和 **Server port** 的组合必须唯一。

端口 `1` 到 `1023` 以及 `5500` 到 `5560` 保留用于 Simulink Real-Time 通信。

#### 编程使用

|  |
| --- |
| **模块参数：** `serverPort` |

### **Use Nagle's algorithm** — 启用 Nagle 算法以合并数据包 `on`（默认）| `off`

启用 Nagle 算法以提高 TCP/IP 网络的效率。Nagle 算法减少了通过网络发送的数据包数量。这种效率提升的代价是 Nagle 算法会在数据包通过网络发送之前引入延迟。您可以通过为此模块禁用 Nagle 算法来减少网络延迟。

#### 编程使用

|  |
| --- |
| **模块参数：** `useNaglesAlgorithm` |
## 所属库

Simulink Real-Time / IP

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a：添加了启用或禁用 Nagle 算法的参数

您可以通过为 TCP Client 模块和 TCP Server 模块禁用 Nagle 算法来减少网络延迟（并降低网络效率）。有关详细信息，请参阅 **Use Nagle's algorithm** 模块参数。

## 描述

配置 TCP 服务器

TCP Server 模块配置一个 TCP 服务器。
