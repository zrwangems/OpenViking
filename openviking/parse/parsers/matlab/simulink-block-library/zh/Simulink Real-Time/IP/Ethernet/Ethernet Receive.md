---
type: simulink-block
title: 'Ethernet Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP / Ethernet'
documentation_page: 'ethernetreceive'
documentation_source_path: 'io_ref/ethernetreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Ethernet Receive

## 端口

### 输出

### **Data** — Ethernet packet Simulink message

将此端口输出的以太网数据包信号连接到模型。如果启用 **Enable Simulink messages** 参数，则数据类型为 `Ethernet_Packet`。该数据类型由以下部分组成：

- `Data`：DataType: uint8，Complexity: real，Dimensions: [64 1]
- `Length`：DataType: uint8，Complexity: real，Dimensions: 1

**Data Types:** `uint8` | `Ethernet_Packet`

### **Length** — Number of bytes received double

当禁用 **Enable Simulink messages** 参数时，此端口可用。Length 是接收到的新数据包中的字节数，否则为 `0`。

**Data Types:** `double`

## 参数

### **Interface Name** — Target computer Ethernet interface name `wm0` | `wm1` | character vector

**Interface Name** 是目标计算机以太网接口的名称。使用 Speedgoat Ethernet Configuration Tool 来识别目标计算机上的以太网索引（接口）。

#### 编程使用

|  |
| --- |
| **模块参数**：`InterfaceName` |

### **Data Width** — 数据端口宽度，以字节为单位 64（默认）| 整数

**Data Width** 是 Data 端口的宽度，以字节为单位。短于此宽度的以太网数据包将用零填充。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataWidth` |

### **Enable Simulink messages** — 以消息形式传输数据 `off`（默认）| `on`

Enable Simulink messages 指示模块将数据视为消息。启用后，Length 端口将被移除。

#### 编程使用

|  |
| --- |
| **模块参数**：`MessageOut` |

### **Maximum messages in a time step** — Limit packets per time step 1 (default) | integer

**Maximum messages in a time step** 选择模块在每个时间步输出的最大数据包数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaxMessagesPerStep` |

### **Capture filter** — Filter on received packets character vector

Capture filter 选择要接收哪些数据包。如果未提供过滤器，则接收所有数据包。有关捕获过滤器语法的信息，请参阅 QNX Neutrino 文档中 `tcpdump` 页面的 **Expressions** 部分。以下示例过滤器捕获发往目标端口 9001 的数据包。

```
dst port 9001
```

#### 编程使用

|  |
| --- |
| **模块参数**：`FilterString` |

### **Sample Time** — 模块的采样时间 -1（默认）| 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |

## 所属库

Simulink Real-Time / IP / Ethernet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

Receive Ethernet packets from Simulink Real-Time target computer

Ethernet Receive 模块使您能够在 Simulink® Real-Time™ 目标计算机上接收以太网数据包。该模块从您在目标计算机上选择的以太网接口（设备）接收数据包。
