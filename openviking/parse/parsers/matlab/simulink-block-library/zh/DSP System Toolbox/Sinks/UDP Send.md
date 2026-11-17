---
type: simulink-block
title: 'UDP Send'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'udpsend'
documentation_source_path: 'ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口
```yaml
ports:
- name: Input
  summary: 输入数据向量 vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### 输入

### **Input** — 输入数据向量 vector

指定模块作为 UDP 数据包发送的输入数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Remote IP address ('255.255.255.255' for broadcast)
  summary: 从中接受 UDP 数据包的 IP 地址 '127.0.0.1'（默认）| IP 地址 | 字符串
  group: ''
- name: Remote IP port
  summary: 远程 IP 端口号 25000（默认）| 范围 [1, 65535] 内的标量
  group: ''
- name: Local IP port source
  summary: 本地 IP 端口的来源 Automatically determine（默认）| Specify via dialog
  group: ''
- name: Local IP port
  summary: 本地 IP 端口号 -1（默认）| 范围 [1, 65535] 内的标量
  group: ''
- name: Send buffer size (bytes)
  summary: 发送 UDP 数据包的缓冲区大小 8192（默认）| 范围 [1, 67108864] 内的标量
  group: ''
```

### **Remote IP address ('255.255.255.255' for broadcast)** — 从中接受 UDP 数据包的 IP 地址 `'127.0.0.1'`（默认）| IP 地址 | 字符串

指定要将 UDP 数据包发送到的 IP 地址或主机名。如果指定主机名，请将其指定为字符串。要广播 UDP 数据包，请指定
`'255.255.255.255'`。

### **Remote IP port** — 远程 IP 端口号 25000（默认）| 范围 [1, 65535] 内的标量

指定要将 UDP 数据包发送到的 IP 端口号。此参数在生成的代码中可调，
但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB。例如，在 Linux 命令行中，输入 `sudo matlab`。

### **Local IP port source** — 本地 IP 端口的来源 `Automatically determine`（默认）| `Specify via dialog`

指定模块使用的是系统分配的本地端口号，还是您通过 **Local IP port** 参数指定的本地端口号。要让系统
分配端口号，请选择 `Automatically determine`。如果
接收地址期望来自特定端口号的 UDP 数据包，请选择
`Specify via dialog` 并使用
**Local IP port** 参数指定端口号。

### **Local IP port** — 本地 IP 端口号 -1（默认）| 范围 [1, 65535] 内的标量

指定模块从中发送 UDP 数据包的 IP 端口号。当接收地址期望来自特定端口
号的消息时，请使用此参数。

#### 参数依赖关系

要启用此参数，请将 **Local IP port source** 设置为
`Specify via dialog`。

### **Send buffer size (bytes)** — 发送 UDP 数据包的缓冲区大小 8192（默认）| 范围 [1, 67108864] 内的标量

指定发送 UDP 数据包的缓冲区大小（以字节为单位）。使
缓冲区足够大，以避免缓冲区溢出导致的数据丢失。
## 所属库

DSP System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件
  （`.dll` 文件）。使用 `packNGo` 函数将此模块生成的代码
  及所有相关文件打包到一个压缩的 ZIP 文件中。使用
  此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发
  环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
- **Remote IP port** 参数在生成的代码中可调，
  但在仿真期间不可调。您可以通过多种方式控制生成的代码中的
  参数可调性。其中一种方式是将该参数配置为
  生成代码中全局结构体的可调字段。其他方式包括将内置存储类或自定义存储类
  应用于 `Simulink.Parameter`
  对象，并使用此对象设置模块参数的值。有关详细信息，请参阅
  在生成的代码中创建可调校准参数 (Simulink Coder)。

## 版本历史

**在 R2010a 中引入**

## 描述

发送 UDP 消息

UDP Send 模块使用用户数据报协议（UDP）通过网络发送数据包。UDP 是一种简单的基于消息的无连接协议，
不具有端到端连接。该协议从源到目的地单向发送数据包，
而不验证接收方是否已就绪。该协议没有
握手机制。数据包可能因多种原因被丢弃。UDP 中没有
确认、重传或超时。然而，UDP 是一种非常简单的
传输协议，适用于对时间敏感的应用，在这些应用中，丢弃数据包
比等待因重传而延迟的数据包更可取。

UDP Send 模块将输入数据向量作为 UDP 数据包发送到
远程 IP 网络端口。模块将 UDP 数据包发送到的远程 IP 端口号
在生成的代码中可调。

某些 Simulink® 模块以及从包含这些
模块的模型构建的 `.exe` 文件需要共享库，例如 Windows® 上的 `.dll` 文件。UDP Send 模块需要
`networkdevice.dll` 库文件。为满足此要求，请遵循
`packNGo` (Simulink Coder) 函数页面上的示例来打包您模型的代码
文件。生成的压缩文件夹包含模型所需的 `.dll`
文件，包括 `networkdevice.dll`。要在 MATLAB® 环境之外运行此类 `.exe` 文件，请将所需的 `.dll` 文件放在与 `.exe` 文件相同的
文件夹中，或将它们放在 Windows 系统路径上的文件夹中。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
