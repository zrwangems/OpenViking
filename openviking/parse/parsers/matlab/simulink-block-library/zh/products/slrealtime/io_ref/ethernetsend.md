---
type: simulink-block
title: 'Ethernet Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / Ethernet'
documentation_page: 'ethernetsend'
documentation_source_path: 'io_ref/ethernetsend.html'
language: zh-CN
chinese_source: official
---

# Ethernet Send

## 端口

### 输入

### **Data** — 以太网数据包的输入端口 构造以太网数据包的信号输入

将模型生成的以太网数据包信号连接至此输入端口。如果启用 **Enable Simulink messages** 参数，数据类型为 `Ethernet_Packet`。使用 `slrealtime.createEthernetPacketBusObj` 函数创建 `Simulink.Bus` 类型的 `Ethernet_Packet`。该数据类型包含：

- `Data`:数据类型：uint8，复杂度：实数，维度：[64 1]
- `Length`:数据类型：uint8，复杂度：实数，维度：1

**数据类型:** `uint8` | `Ethernet_Packet`

### **Length** — 要传输的数据字节数 双精度

当禁用 **Enable Simulink messages** 参数时，此端口可用。**Length** 决定要传输的数据字节数。将 `Data` 向量的宽度指定为预期传输的最大字节数。

**数据类型:** `double`

## 参数

### **Interface Name** — 目标计算机接口名称 `wm0` | `wm1` | 字符向量

**Interface Name** 是目标计算机以太网接口的名称。使用 Speedgoat 以太网配置工具来识别目标计算机上的以太网索引（接口）。

#### 编程用法

|  |
| --- |
| **模块参数：**`InterfaceName` |

### **Overwrite source MAC address** — 将源 MAC 地址替换为数据端口的 MAC 地址 `off` (默认) | `on`

若启用 (`on`)，该模块将发送包含目标计算机实际 MAC 地址的数据包，覆盖用户设置的 MAC 地址。若禁用 (`off`)，该模块将使用用户构造的数据包中指定的 MAC 地址发送数据包。

#### 编程用法

|  |
| --- |
| **模块参数：**`OverwriteSrcMACAddress` |

### **Enable Simulink messages** — 数据作为消息 `off` (默认) | `on`

启用 Simulink 消息将指示模块将数据视为消息。启用后，长度端口将被移除。

#### 编程用法

|  |
| --- |
| **模块参数：**`MessageIn` |

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

从目标计算机发送以太网数据包

Ethernet Send 模块可使您发送通过 Simulink® 模块或 MATLAB® Function 模块构造的以太网数据包，并将该信号连接至数据输入端口。此输入内容可完全自定义。该模块将数据包发送到您在 Speedgoat® 目标计算机上选择的以太网接口（设备）。
