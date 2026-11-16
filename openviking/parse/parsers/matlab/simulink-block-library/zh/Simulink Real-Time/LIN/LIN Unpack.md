---
type: simulink-block
title: 'LIN Unpack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'LIN'
documentation_page: 'linunpack'
documentation_source_path: 'io_ref/linunpack.html'
language: zh-CN
chinese_source: official
---

# LIN Unpack

## 端口

### 输入

### **message\_updated** — 表示消息更新 0（逻辑假） | 1（逻辑真）

当 `message_updated` 值为 1（逻辑真）时，表示 LIN 总线有消息传入。该模块输出解包后的信号。当 `message_updated` 值为 0（逻辑假）时，LIN 总线上没有消息更新，该模块将输出 LDF 文件中定义的每个信号的默认值。

### **Lin\_data\_8\_bytes** — 输入 LIN 数据进行解包 LIN 数据

接收 LIN 数据以进行解包。
### 输出

### **out** — 输出数据 数据

发送未压缩的数据。输出端口数量根据所选帧中的信号数量进行分配。当选中一个帧时，端口名称会被分配给每个端口。

## 参数

### **LDF File Name** — LDF 文件的路径 空 (默认) | 字符向量 | 字符串标量

提供 LDF 文件的路径。若未设置此参数，则无法使用该模块。

#### 编程用法

|  |
| --- |
| **模块参数：**`LDFFileName` |

### **Select Frame** — LIN 帧 `None` (默认) | 字符向量 | 字符串标量

从 LDF 中可用的选项中选择 LIN 帧。若未选择 LDF，该模块将使用 `None`。

#### 编程用法

|  |
| --- |
| **模块参数：**`selectedFrameName` |

### **Frame ID** — LIN 帧 ID `1` (默认) | uint8

从 LDF 中可用的选项中选择 LIN 帧 ID。若未选择 LDF，该模块将使用 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：**`frameId` |

## 所属库

Simulink Real-Time / LIN

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2021b 中推出**

## 描述

通过 LIN 描述文件中的配置，从数据帧中解包信号

LIN Unpack 模块通过使用 LIN 描述文件 (LDF) 中的配置解包数据帧，并输出信号数据。您可以在模型中将未解包的本地互连网络 (LIN) 总线数据用作信号数据。LIN Unpack 模块支持 LDF 2.2 及更早版本。
