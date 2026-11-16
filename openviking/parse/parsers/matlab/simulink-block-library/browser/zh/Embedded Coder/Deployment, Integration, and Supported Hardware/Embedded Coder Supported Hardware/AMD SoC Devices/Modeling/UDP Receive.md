---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'xilinxzynq7000ec/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Message** — 接收到的消息 N×1 数组

UDP Receive 模块将接收到的 UDP 数据包输出为 N×1 数据向量。**Data type for Message** 和 **Maximum length for Message** 参数分别设置向量的数据类型和长度 N。

当 **Output variable-size signal** 启用时，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Length** — Message 向量的长度（正标量）

此端口输出端口 `Message` 上消息向量信号的长度。

当 **Output variable-size signal** 启用时，此端口隐藏。

**数据类型：** `single`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **Local IP port** — 本地 IP 端口 `25000`（默认） | `1 .. 65535`

输入硬件板上接收 UDP 数据包的 IP 端口号。

**注意**

在 Linux® 上，要设置低于 1024 的 IP 端口号，请以 root 权限运行 MATLAB®。例如，在 Linux 命令行中，输入：

    sudo matlab

#### 编程使用

|  |
| --- |
| **模块参数：** `localURL` |

### **Remote IP address** — 远程 IP 地址 `'0.0.0.0'`（默认） | 字符向量

输入从中接受数据包的 IP 地址。输入特定 IP 地址会阻止来自其他地址的 UDP 数据包。要接受来自任何 IP 地址的数据包，请输入 `'0.0.0.0'`。

#### 编程使用

|  |
| --- |
| **模块参数：** `remoteURL` |

### **Receive buffer size (bytes)** — 接收缓冲区大小 `8192`（默认） | 正整数标量

使接收缓冲区足够大，以避免缓冲区溢出导致的数据丢失。

#### 编程使用

|  |
| --- |
| **模块参数：** `recvBufferSize` |

### **Maximum length for Message** — Message 的最大长度 `255`（默认） | 正整数

输入数据输出向量的最大长度（以向量元素为单位）。将此参数设置为大于或等于 UDP 数据包数据大小的值。系统会截断超过此长度的数据。

如果禁用 **Output variable-size signal**，模块输出与 **Maximum length for Message** 长度相同的固定长度输出。

#### 编程使用

|  |
| --- |
| **模块参数：** `dims` |

### **Data type for Message** — Message 的数据类型 `uint8`（默认） | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

设置 Message 输出中向量元素的数据类型。使该数据类型与用于创建 UDP 数据包的数据输入匹配。

#### 编程使用

|  |
| --- |
| **模块参数：** `signalDatatype` |

### **Output variable-size signal** — 输出可变大小信号 `on`（默认） | `off`

要支持模型中长度可变的信号，请选中此参数。要支持固定长度信号，请清除此参数。清除此参数时，模块：

- 从 **Message** 输出发出由 **Maximum length for Message** 设置的固定长度数据向量。
- 从 **Length** 输出发出有效数据的长度。
- 如果 UDP 数据包包含的数据少于固定长度输出，则差值部分包含无效数据。

在这两种情况下，模块都会截断超过 **Maximum length for Message** 的数据。

#### 编程使用

|  |
| --- |
| **模块参数：** `isVarSize` |

### **Blocking time (seconds)** — 等待 UDP 数据包的时间 `inf`（默认） | 正标量

对于每个采样，等待此长度时间以接收 UDP 数据包，然后将控制权返回给调度器。此值默认为 `inf`，表示无限期等待。

#### 编程使用

|  |
| --- |
| **模块参数：** `blockingTime` |

### **Sample time (seconds)** — 采样时间 `0.01`（默认） | 正标量

指定调度器运行此模块的频率。输入大于零的值。在实时操作中，将此选项设置为较大值可降低 UDP 消息丢失的可能性。

#### 编程使用

|  |
| --- |
| **模块参数：** `sampletime` |

## 所属库

Embedded Coder Support Package for AMD SoC Devices

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

接收 UDP 数据

UDP Receive 模块从 IP 网络端口接收用户数据报协议 (UDP) 数据包，并将其保存到其缓冲区。在每个采样中，模块将单个 UDP 数据包的内容输出为数据向量。
