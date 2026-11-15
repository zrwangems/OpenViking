---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'alterasoc/ref/udpsend.html'
language: zh-CN
chinese_source: official
---

# UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据信号 N×1 数组

要发送到远程 IP 地址和端口的报文的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。从 Simulink® 工具条中，在**仿真**选项卡上的**准备**库中，选择**属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **IP 地址** — IP 地址 `'255.255.255.255'` (默认) | 字符向量

指定模块向其发送报文的 IP 地址。要广播 UDP 报文，请保留默认值 `'255.255.255.255'`。

#### 编程用法

|  |
| --- |
| **模块参数：**`localURL` |

### **远程 IP 端口** — 远程 IP 端口 `25000` (默认) | 1–65535

指定模块发送报文的 IP 端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`remotePort` |

### **本地 IP 端口源** — 本地 IP 端口源 **自动分配** (默认) | **通过对话框指定**

要使系统自动分配端口号，请选择**自动分配**。要使用**本地 IP 端口**参数指定 IP 端口号，请选择**通过对话框指定**。

#### 编程用法

|  |
| --- |
| **模块参数：**`localPortSource` |

### **本地 IP 端口** — 本地 IP 端口 `-1` (默认) | `1 .. 65535`

指定模块发送报文的 IP 端口号。如果接收地址需要来自特定端口号的报文，请在此处输入该端口号。

#### 编程用法

|  |
| --- |
| **模块参数：**`localPort` |

## 所属库

Embedded Coder Support Package for Intel SoC Devices

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2014b 中推出**

## 描述

发送 UDP 报文

UDP Send 模块将输入向量作为用户数据报协议 (UDP) 报文通过 IP 网络端口传输。
