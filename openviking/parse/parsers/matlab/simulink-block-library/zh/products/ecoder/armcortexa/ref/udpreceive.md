---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'armcortexa/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Port\_1** — 接收到的 UDP 数据数值向量

从远程主机接收的 UDP 数据，以数值向量形式返回。使用 **消息的数据类型** 参数设置此输出的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **本地 IP 端口** — 远程主机上的 IP 端口 `25000`（默认） | `1 .. 65535`

指定要接收 UDP 数据包的硬件板上应用程序的本地 IP 端口号。端口号必须是 1 到 65,535 之间的整数。

**注意**

在 Linux® 上，要设置低于 1024 的本地 IP 端口号，请以 root 权限运行 MATLAB®。例如，在 Linux 命令行中，输入：

    sudo matlab

#### 编程用法

|  |
| --- |
| **模块参数：** `localPort` |

### **远程 IP 地址（'0.0.0.0' 表示接受所有）** — 要监听的远程 IP 地址 `'0.0.0.0'`（默认） | 有效 IP 地址

指定模块接受 UDP 数据包的来源 IP 地址。输入特定 IP 地址会阻止来自其他地址的 UDP 数据包。要接受来自所有 IP 地址的数据包，请使用默认值 `'0.0.0.0'`。

#### 编程用法

|  |
| --- |
| **模块参数：** `remoteURL` |

### **接收缓冲区大小 (bytes)** — 接收数据中数据字节的最大数量 `8192`（默认） | 正整数

指定用于存储接收到的 UDP 数据包的缓冲区大小。请将接收缓冲区大小指定得足够大，以避免缓冲区溢出导致的数据丢失。

#### 编程用法

|  |
| --- |
| **模块参数：** `recvBufferSize` |

### **消息最大长度** — 输出 UDP 数据的最大长度 `255`（默认） | 正整数

指定输出 UDP 数据的最大长度。此值必须大于或等于 UDP 数据包的数据大小。系统会截断超过此长度的任何数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `dims` |

### **消息的数据类型** — 输出数据的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择输出 UDP 数据的数据类型。此数据类型必须与远程主机发送的 UDP 消息的数据类型相同。

#### 编程用法

|  |
| --- |
| **模块参数：** `signalDataType` |

### **输出可变大小信号** — 启用或禁用可变输出信号大小 `off`（默认） | `on`

如果您的模型支持可变长度信号，请选择 **输出可变大小信号**。在此情况下：

- 输出向量长度会变化，具体取决于接收到的 UDP 数据中的数据量。
- 模块从单个未标记输出发出数据向量。

如果您的模型不支持可变长度信号，请清除 **输出可变大小信号**。在此情况下：

- 模块发出固定长度输出，其长度与 **消息最大长度** 相同。
- 如果 UDP 数据包包含的数据少于固定长度输出，则差异部分包含无效数据。
- 将启用 **长度的数据类型** 参数。

在两种情况下，模块都会截断超过 **消息最大长度** 的数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `isVarSize` |

### **阻塞时间 (seconds)** — 等待 UDP 数据包的时间 `inf`（默认） | 非负标量

指定每个采样中等待 UDP 数据包的持续时间，然后将控制权返回给调度器。

#### 编程用法

|  |
| --- |
| **模块参数：** `blockingTime` |

### **采样时间 (seconds)** — 采样时间 `1`（默认） | 正标量

指定调度器运行此模块的频率。将此参数设置为较大的值可降低丢弃 UDP 消息的可能性。

#### 编程用法

|  |
| --- |
| **模块参数：** `sampletime` |

## 所属库

Embedded Coder Support Package for ARM Cortex-A Processors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

接收 UDP 数据

UDP Receive 模块从远程主机接收用户数据报协议 (UDP) 数据。该模块从套接字缓冲区读取可用的 UDP 数据，并将数据以向量形式输出。
