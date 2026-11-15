---
type: simulink-block
title: 'Ethernet Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / Ethernet'
documentation_page: 'ethernetreceive'
documentation_source_path: 'io_ref/ethernetreceive.html'
language: zh-CN
chinese_source: official
---

# Ethernet Receive

## 端口

### 输出

### **Data** — 以太网数据包 Simulink 消息

将此端口的以太网数据包信号连接至模型。如果启用 **Enable Simulink messages** 参数，数据类型为 `Ethernet_Packet`。该数据类型包含：

- `Data`:数据类型：uint8，复杂度：实数，维度：[64 1]
- `Length`:数据类型：uint8，复杂度：实数，维度：1

**数据类型:** `uint8` | `Ethernet_Packet`

### **Length** — 接收的字节数 双精度

当禁用 **Enable Simulink messages** 参数时，此端口可用。长度字段表示接收到的新的数据包中的字节数，否则为 `0`。

**数据类型:** `double`

## 参数

### **Interface Name** — 目标计算机以太网接口名称 `wm0` | `wm1` | 字符向量

**Interface Name** 是目标计算机以太网接口的名称。使用 Speedgoat 以太网配置工具来识别目标计算机上的以太网索引（接口）。

#### 编程用法

|  |
| --- |
| **模块参数：**`InterfaceName` |

### **Data Width** — 数据端口宽度（单位：字节） 64 (默认) | 整数

**Data Width** 是数据端口的宽度（以字节为单位）。长度小于该宽度的以太网数据包将用零填充。

#### 编程用法

|  |
| --- |
| **模块参数：**`DataWidth` |

### **Enable Simulink messages** — 数据作为消息 `off` (默认) | `on`

启用 Simulink 消息将指示模块将数据视为消息。启用后，长度端口将被移除。

#### 编程用法

|  |
| --- |
| **模块参数：**`MessageOut` |

### **Maximum messages in a time step** — 每时间步限制数据包数量 1 (默认) | 整数

**Maximum messages in a time step** 选取每个时间步长内该模块输出的最大数据包数量。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaxMessagesPerStep` |

### **Capture filter** — 过滤接收到的数据包 字符向量

捕获过滤器用于选择要接收的数据包。如果未提供过滤器，则接收所有数据包。有关捕获过滤器语法的信息，请参阅 QNX Neutrino 文档中 `tcpdump` 页面的**表达式**部分。此示例过滤器捕获发往目标端口 9001 的数据包。

```
dst port 9001
```

#### 编程用法

|  |
| --- |
| **模块参数：**`FilterString` |

### **Sample Time** — 模块采样时间 -1 (默认) | 数值

输入基本采样时间或其倍数。`-1` 表示采样时间继承自父级。

#### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |

## 所属库

Simulink Real-Time / IP / Ethernet

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2022a 中推出**

## 描述

接收来自目标计算机 Simulink Real-Time 的以太网数据包

Ethernet Receive 模块使您能够在目标计算机 Simulink® Real-Time™ 上接收以太网数据包。该模块接收来自目标计算机上您所选以太网接口（设备）的数据包。
