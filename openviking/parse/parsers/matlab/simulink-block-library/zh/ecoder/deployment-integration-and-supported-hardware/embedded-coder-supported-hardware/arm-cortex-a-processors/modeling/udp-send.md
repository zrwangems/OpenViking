---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'armcortexa/ref/udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据信号（numeric vector）

输入数据信号，指定为 numeric vector。该模块将此数据作为 UDP 数据发送到远程 IP 端口上的远程 IP 地址。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **远程 IP 地址（广播时为 '255.255.255.255'）** — 远程主机的 IP 地址 `'255.255.255.255'`（默认）| 有效 IP 地址

指定要将 UDP 数据发送到的远程主机的 IP 地址。要广播 UDP 消息，请保留默认值 `'255.255.255.255'`。

#### 编程使用

|  |
| --- |
| **模块参数：** `remoteURL` |

### **远程 IP 端口** — 远程主机的 IP 端口 `25000`（默认）| 1 到 65,535 的整数

指定要将 UDP 数据发送到的远程主机的端口号。端口号必须是 1 到 65,535 的整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `remotePort` |

### **本地 IP 端口源** — 选择本地 IP 端口源 `Assign automatically`（默认）| `Specify via dialog`

要使系统自动分配发送数据所用的本地 IP 端口号，请选择 `Assign automatically`。要使用 **本地 IP 端口** 参数指定本地 IP 端口号，请选择 `Specify via dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `localPortSource` |

### **本地 IP 端口** — 本地主机上的 IP 端口 `-1`（默认）| 1 到 65,535 的整数

指定要从中发送数据的硬件板上应用程序的本地 IP 端口号。端口号必须是 1 到 65,535 的整数。默认值 `-1` 会将任意随机可用端口分配为本地 IP 端口。

如果接收主机接受来自特定端口号的 UDP 数据，请将此参数设置为该端口号。

要启用此参数，请将 **本地 IP 端口源** 设置为 `Specify via dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `localPort` |

## 所属库

ARM Cortex-A 处理器的 Embedded Coder 支持包

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2014b 中引入**

## 描述

发送 UDP 数据

UDP Send 模块将用户数据报协议 (UDP) 数据传输到远程主机。
