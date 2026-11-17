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
chinese_source: worker-translation
---

# LIN Unpack

## 端口

### 输入

### **message\_updated** — 指示报文更新 0（逻辑 false）| 1（逻辑 true）

当 `message_updated` 值为 1（逻辑 true）时，表示有来自 LIN 总线的报文传入。此模块输出解包后的信号。当 `message_updated` 值为 0（逻辑 false）时，LIN 总线上没有报文更新，此模块为 LDF 文件中定义的每个信号输出默认值。

### **Lin\_data\_8\_bytes** — 用于解包的输入 LIN 数据 LIN 数据

接收要解包的 LIN 数据。
### 输出

### **out** — 输出数据 数据

发送解包后的数据。输出端口数量根据所选帧中的信号数量进行分配。选择帧后，端口名称将分配给每个端口。

## 参数

### **LDF File Name** — LDF 的文件路径 空（默认）| 字符向量 | 字符串标量

提供 LDF 的文件路径。如果未设置此参数，则无法使用该模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LDFFileName` |

### **Select Frame** — LIN 帧 `None`（默认）| 字符向量 | 字符串标量

从 LDF 中可用的选项中选择 LIN 帧。如果未选择 LDF，该模块使用 `None`。

#### 编程使用

|  |
| --- |
| **模块参数**：`selectedFrameName` |

### **Frame ID** — LIN 帧 ID `1`（默认）| uint8

从 LDF 中可用的选项中选择 LIN 帧 ID。如果未选择 LDF，该模块使用 `1`。

#### 编程使用

|  |
| --- |
| **模块参数**：`frameId` |

## 所属库

Simulink Real-Time / LIN

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

通过使用 LIN 描述文件中的配置从数据帧中解包信号

LIN Unpack 模块通过使用 LIN 描述文件（LDF）中的配置对数据帧进行解包，并输出信号数据。您可以将解包后的本地互连网络（LIN）总线数据用作模型中的信号数据。LIN Unpack 模块支持 LDF 版本 2.2 及更早版本。
