---
type: simulink-block
title: 'LIN Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / LIN'
documentation_page: 'linpack'
documentation_source_path: 'io_ref/linpack.html'
language: zh-CN
chinese_source: official
---

# LIN Pack

## 端口

### 输入

### **in** — 将数据输入到包中 数据

接收用于 LIN 封装的数据。输入端口数量根据所选帧进行分配。端口名称被分配给每个端口。
### 输出

### **lin\_data** — 输出 LIN 数据 LIN 数据

发送打包的 LIN 数据。

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

通过 LIN 描述文件中的配置将信号打包到数据帧中

LIN Pack 模块通过使用 LIN 描述文件 (LDF) 中的配置，将信号打包到数据帧中。本地互连网络 (LIN) 总线可使用打包数据。LIN Pack 模块支持 LDF 2.2 及更早版本。
