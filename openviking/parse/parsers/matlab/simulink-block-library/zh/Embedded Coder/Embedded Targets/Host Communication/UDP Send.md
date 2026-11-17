---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'udpsend'
documentation_source_path: 'ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — UDP 数据包 标量（默认）| 向量

UDP 数据包，指定为数据向量，传输到 IP 网络端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Remote IP address ('255.255.255.255' for broadcast)** — 接受 UDP 数据包的 IP 地址 '255.255.255.255'（默认）| IP 地址 | 字符串

指定要发送 UDP 数据包的目标 IP 地址或主机名。如果指定主机名，请将其指定为字符串。要广播 UDP 数据包，请指定 `'255.255.255.255'`。

### **Remote IP port** — 远程 IP 端口号 25000（默认）| 范围 [1, 65535] 内的标量

指定要发送 UDP 数据包的目标 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB。例如，在 Linux 命令行中输入：

```
sudo matlab
```

### **Local IP port source** — 本地 IP 端口的来源 `Automatically determine`（默认）| `Specify via dialog`

指定模块是使用系统分配的本地端口号，还是使用通过 **Local IP port** 参数指定的端口号。要让系统分配端口号，请选择 `Automatically determine`。如果接收地址期望来自特定端口号的 UDP 数据包，请选择 `Specify via dialog` 并使用 **Local IP port** 参数指定端口号。

#### 参数依赖关系

要启用 **Local IP port** 参数，请选择 `Specify via dialog`。

### **Local IP port** — 本地 IP 端口号 -1（默认）| 范围 [1, 65535] 内的标量

指定模块发送 UDP 数据包的源 IP 端口号。当接收地址期望来自特定端口号的消息时，请使用此参数。

#### 参数依赖关系

要启用此参数，请将 **Local IP port source** 设置为 `Specify via dialog`。

### **Send buffer size (bytes)** — 发送 UDP 数据包的缓冲区大小 8192（默认）| 范围 [1, 67108864] 内的标量

指定发送 UDP 数据包的缓冲区大小（以字节为单位）。使缓冲区足够大，以避免缓冲区溢出导致的数据丢失。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

发送 UDP 数据包

UDP Send 模块使用用户数据报协议（UDP）通过网络发送数据包。UDP 是一种简单的基于消息的无连接协议，没有端到端连接。该协议从源到目的地单向发送数据包，不验证接收方是否就绪。该协议没有握手机制。数据包可能因多种原因被丢弃。UDP 中没有确认、重传或超时。然而，UDP 是一种非常简单的传输协议，适用于对时间敏感的应用，在这些应用中，丢弃数据包比等待因重传而延迟的数据包更可取。

UDP Send 模块将输入数据向量作为 UDP 数据包传输到远程 IP 网络端口。模块发送 UDP 数据包的目标远程 IP 端口号在生成的代码中可调。

某些 Simulink® 模块以及从包含这些模块的模型构建的 `.exe` 文件需要共享库，例如 Windows® 上的 `.dll` 文件。UDP Send 模块需要 `networkdevice.dll` 库文件。为满足此要求，请按照 `packNGo` 函数页面上的示例为您的模型打包代码文件。生成的压缩文件夹包含模型所需的 `.dll` 文件，包括 `networkdevice.dll`。要在 MATLAB® 环境之外运行此类 `.exe` 文件，请将所需的 `.dll` 文件放在与 `.exe` 文件相同的文件夹中，或将它们放在 Windows 系统路径上的文件夹中。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB (DSP System Toolbox)。
