---
type: simulink-block
title: 'TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'tcpipreceive'
documentation_source_path: 'supportpkg/parrot_ref/tcpipreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Receive

## 端口

### 输出

### **Data** — 输出数据 [Nx1] 数组

在每个时间步，端口将数据输出为大小在 **Data size (N)** 参数中指定的向量。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 接收数据的状态 `1` | `0`

在每个时间步，当接收的数据长度大于或等于 **Data size (N)** 参数中指定的长度时，端口输出 `1`。否则，它输出 `0`，表示未接收到新数据。

**数据类型：** `uint16`

## 参数

#### 主选项卡

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认）| `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP port**。本地端口用作 TCP/IP 服务器的侦听端口。

当您将此参数设置为 `Client` 时，必须提供要从其接收数据的 TCP/IP 服务器的 **Remote IP port**。

### **Local IP port** — 从其接收数据的接收主机的 IP 端口 `25000`（默认）| [1, 65535]

此本地端口号用作接收主机的侦听端口。将本地端口号与发送主机的远程端口号匹配。

### **Remote IP address** — 从其接收数据的服务器的远程 IP 地址 `192.168.3.2`（默认）

从其接收数据的服务器的 IP 地址。**Remote IP address** 设置为 192.168.3.2；请勿更改此 IP 地址。

#### 依赖项

此参数仅在将 **Connection mode** 参数设置为 `Client` 时显示。

### **Remote IP port** — 从其接收数据的服务器的远程 IP 端口 `25000`（默认）| [1, 65535]

指定从其接收数据的服务器的端口号。

**注意**

请勿将端口 `24099` 和 `26061` 用于与 Parrot minidrone 的 TCP/IP 通信，因为这些端口是保留端口。

#### 依赖项

此参数仅在将 **Connection mode** 参数设置为 `Client` 时显示。

### **Data type** — 接收数据的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定模块从发送主机接收的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 接收数据中的字节数 `1`（默认）| 任意正整数

每个时间步要接收的字节数。

### **Sample time** — 模块从发送主机读取数据的时间间隔 `0.005`（默认）| 任意非负值，且为 0.005（5 ms）的倍数 | -1

输入接收数据的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Manually specify local IP port** — 手动指定本地 IP 端口号 off（默认）| logical

允许手动指定接收数据的本地 IP 端口。此参数仅在将 **Connection mode** 设置为 `Client` 时显示。

### **Local IP port** — 接收数据的本地端口 25000（默认）| 标量

输入客户端接收数据的本地端口。此参数仅在将 **Connection mode** 设置为 `Client` 并选中 **Manually specify local IP port** 复选框时显示。

### 接收 TCP 数据

本节说明非阻塞模式下输出端口的值，其中以下模块参数设置为：

| 模块参数 | 值 |
| --- | --- |
| **Data type** | `uint8` |
| **Data size (N)** | `4` |

输出端口的值取决于接收的数据长度是小于、大于还是等于请求的数据长度。

- 接收的数据长度 = Data size (N)：**Data** 端口将数据输出为大小在 **Data size (N)** 参数中指定的向量。**Status** 端口输出 `1`，表示已接收到请求的数据。

  假设接收的数据长度为 4。在这种情况下，**Data** 端口输出大小为 4 的数据向量，其中填充接收的数据字节。**Status** 端口输出 `1`。
- 接收的数据长度 < Data size (N)：在非阻塞模式下，模块不会等待请求的数据可用。**Data** 端口将数据输出为大小在 **Data size (N)** 参数中指定的向量，其中填充零。**Status** 端口输出 `0`，表示未接收到新数据。
- 接收的数据长度 > Data size (N)：**Data** 端口输出大小在 **Data size (N)** 参数中指定的数据向量。该向量仅包含数据中的前 *N* 个字节。其余字节将在下一个时间步与数据字节一起输出。**Status** 端口输出 `1`，表示已接收到请求的数据。

  假设接收的数据长度为 5 字节。在这种情况下，**Data** 端口输出大小为 4 的数据向量。该向量仅包含接收数据中的前 4 个字节。第五个字节将在下一个时间步与数据字节一起输出。**Status** 端口输出 `1`。

| 数据长度 | 读取操作模式 | | 输出端口 | |
| --- | --- | --- | --- | --- |
| Data | Status |
| 接收的数据长度 = Data size (N) | 非阻塞 | |  | `1` |
| 接收的数据长度 < Data size (N) | 非阻塞 | |  | `0` |
| 接收的数据长度 > Data size (N) | 非阻塞 | |  | `1` |

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

通过 TCP/IP 网络从远程主机接收数据

TCP/IP Receive 模块通过 Bluetooth® 网络从远程主机接收数据。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP port**。**Local IP port** 用作 TCP/IP 服务器的侦听端口。当您将 **Connection mode** 设置为 `Client` 时，必须提供要从其接收数据的服务器的 **Remote IP port**。

该模块有两个输出端口：**Data** 和 **Status**。在每个采样时间，**Data** 端口将数据输出为大小在 **Data size (N)** 参数中指定的向量。**Status** 端口包含 0 或 1，以指示是否接收到指定时间步的新数据。**Status** 端口值为 1 表示来自 **Data** 端口的数据有效。

Parrot® minidrone 是 little-endian 设备。TCP/IP Receive 模块期望接收的 TCP/IP 数据的字节序为 big-endian，并将其转换为 little-endian。

**注意**

在某些情况下，防病毒或防火墙软件可能会阻止 TCP 流量。如果是这样，请配置防病毒或防火墙软件以允许特定 IP 端口号的流量。
