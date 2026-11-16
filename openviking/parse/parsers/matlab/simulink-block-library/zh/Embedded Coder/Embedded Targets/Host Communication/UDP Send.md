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
chinese_source: official
---

# UDP Send

## 端口

### 输入

### **Port\_1** — UDP 数据包 标量 (默认) | 向量

UDP 数据包，指定为数据向量，传输到 IP 网络端口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **远程 IP 地址 ('255.255.255.255' 表示广播)** — 接受 UDP 数据包的 IP 地址 “255.255.255.255” (默认) | IP 地址 | 字符串

指定要发送 UDP 数据包的 IP 地址或主机名。如果指定主机名，请将其指定为字符串。要广播 UDP 数据包，请指定 `'255.255.255.255'`。

### **远程 IP 端口** — 远程 IP 端口号 25000 (默认) | 标量范围为 [1, 65535]

指定要发送 UDP 数据包的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为 1024 以下，请使用 root 特权运行 MATLAB。例如，在 Linux 命令行中输入：

```
sudo matlab
```

### **本地 IP 端口源** — 本地 IP 端口源 `Automatically determine` (默认) | `Specify via dialog`

指定模块是否使用系统分配的本地端口号或您使用**本地 IP 端口**参数指定的本地端口号。要让系统分配端口号，请选择**自动确定**。如果接收地址期望来自特定端口号的 UDP 数据包，请选择**通过对话框指定**并使用**本地 IP 端口**参数指定端口号。

#### 参数依赖关系

要启用**本地 IP 端口**参数，请选择**通过对话框指定**。

### **本地 IP 端口** — 本地 IP 端口号 -1 (默认) | 标量范围为 [1, 65535]

指定模块发送 UDP 数据包的 IP 端口号。当接收地址期望来自特定端口号的消息时使用此参数。

#### 参数依赖关系

要启用此参数，请将**本地 IP 端口源**设置为**通过对话框指定**。

### **发送缓冲区大小 (字节)** — 发送 UDP 数据包的缓冲区大小 8192 (默认) | 范围内的标量 [1, 67108864]

指定发送 UDP 数据包的缓冲区大小（以字节为单位）。使缓冲区足够大，以避免因缓冲区溢出而导致数据丢失。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2011a 中推出**

## 描述

发送 UDP 数据包

UDP Send 模块使用用户数据报协议 (UDP) 通过网络发送数据包。UDP 是一种简单的基于消息的无连接协议，没有端到端连接。该协议从源到目标单向发送数据包，而不验证接收方是否准备就绪。该协议没有握手机制。数据包可能会因多种原因而被丢弃。UDP 中没有确认、重传或超时。然而，UDP 是一种非常简单的传输协议，适用于时间敏感的应用程序，在这些应用程序中，丢弃数据包比等待因重传而延迟的数据包更可取。

UDP Send 模块将输入数据向量作为 UDP 数据包传输到远程 IP 网络端口。该模块发送 UDP 数据包的远程 IP 端口号在生成的代码中是可调的。

一些从包含这些模块的模型构建的 Simulink® 模块和 `.exe` 文件需要共享库，例如 Windows® 上的 `.dll` 文件。UDP Send 模块需要 `networkdevice.dll` 库文件。为了满足此要求，请按照 `packNGo` 函数页面上的示例来打包模型的代码文件。生成的压缩文件夹包含模型所需的 `.dll` 文件，包括 `networkdevice.dll`。要在 MATLAB® 环境之外运行此类 `.exe` 文件，请将所需的 `.dll` 文件放在与 `.exe` 文件相同的文件夹中，或将它们放在 Windows 系统路径上的文件夹中。欲了解更多详情，请参阅How To Run a Generated Executable Outside MATLAB (DSP System Toolbox)。
