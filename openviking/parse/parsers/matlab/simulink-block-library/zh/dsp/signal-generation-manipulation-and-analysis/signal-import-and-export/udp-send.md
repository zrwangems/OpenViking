---
type: simulink-block
title: 'UDP Send'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Import and Export'
documentation_page: 'udpsend'
documentation_source_path: 'ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Input** — 输入数据向量 vector

指定模块作为 UDP 数据包发送的输入数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**复数支持：** Yes

## 参数

### **远程 IP 地址（广播时为 '255.255.255.255'）** — 从中接受 UDP 数据包的 IP 地址 `'127.0.0.1'`（默认） | IP 地址 | string

指定向其发送 UDP 数据包的 IP 地址或主机名。如果指定主机名，请将其指定为字符串。要广播 UDP 数据包，请指定 `'255.255.255.255'`。

### **远程 IP 端口** — 远程 IP 端口号 25000（默认） | 范围 [1, 65535] 中的标量

指定向其发送 UDP 数据包的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB。例如，在 Linux 命令行中，输入 `sudo matlab`。

### **本地 IP 端口源** — 本地 IP 端口的来源 `Automatically determine`（默认） | `Specify via dialog`

指定模块使用系统分配的本地端口号，还是使用您通过 **本地 IP 端口** 参数指定的本地端口号。要让系统分配端口号，请选择 `Automatically determine`。如果接收地址期望从特定端口号接收 UDP 数据包，请选择 `Specify via dialog`，并使用 **本地 IP 端口** 参数指定端口号。

### **本地 IP 端口** — 本地 IP 端口号 -1（默认） | 范围 [1, 65535] 中的标量

指定模块从其发送 UDP 数据包的 IP 端口号。当接收地址期望来自特定端口号的消息时，使用此参数。

#### 参数依赖关系

要启用此参数，请将 **本地 IP 端口源** 设置为 `Specify via dialog`。

### **发送缓冲区大小 (bytes)** — 发送 UDP 数据包的缓冲区大小 8192（默认） | 范围 [1, 67108864] 中的标量

指定发送 UDP 数据包的缓冲区大小，以 bytes 为单位。使缓冲区足够大以避免缓冲区溢出导致的数据丢失。

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

- 从此模块生成的可执行文件依赖于 MATLAB 随附的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将从此模块生成的代码以及所有相关文件打包到一个压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发环境中重定位、解包并重新构建项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
- **远程 IP 端口** 参数在生成的代码中可调，但在仿真期间不可调。您可以通过多种方式控制生成的代码中的参数可调性。其中一种方式是将该参数配置为生成的代码中全局结构的可调字段。其他方式包括：将内置存储类或自定义存储类应用于 `Simulink.Parameter` 对象，并使用该对象设置模块参数的值。有关详细信息，请参阅 Create Tunable Calibration Parameter in the Generated Code (Simulink Coder)。

## 版本历史

**在 R2010a 中引入**

## 描述

发送 UDP 消息

UDP Send 模块使用用户数据报协议 (UDP) 通过网络发送数据包。UDP 是一种简单的基于消息的无连接协议，没有端到端连接。该协议将数据包从源单向发送到目标，而不验证接收方是否就绪。该协议没有握手机制。数据包可能因多种原因丢失。UDP 中没有确认、重传或超时。但是，UDP 是一种非常简单的传输协议，适用于对时间敏感的应用程序，在这些应用程序中，丢弃数据包比等待因重传而延迟的数据包更可取。

UDP Send 模块将输入数据向量作为 UDP 数据包发送到远程 IP 网络端口。模块向其发送 UDP 数据包的远程 IP 端口号在生成的代码中可调。

某些 Simulink® 模块以及从包含这些模块的模型构建的 `.exe` 文件需要共享库，例如 Windows® 上的 `.dll` 文件。UDP Send 模块需要 `networkdevice.dll` 库文件。为满足此要求，请按照 `packNGo` (Simulink Coder) 函数页面上的示例操作，为您的模型打包代码文件。生成的压缩文件夹包含模型所需的 `.dll` 文件，包括 `networkdevice.dll`。要在 MATLAB® 环境之外运行此类 `.exe` 文件，请将所需的 `.dll` 文件放在与 `.exe` 文件相同的文件夹中，或将它们放在 Windows 系统路径上的文件夹中。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
