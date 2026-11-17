---
type: simulink-block
title: 'Byte Reversal/Change Endianess'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Shared Memory'
documentation_page: 'bytereversalchangeendianess'
documentation_source_path: 'io_ref/bytereversalchangeendianess.html'
language: zh-CN
chinese_source: official
---

# Byte Reversal/Change Endianess

## 端口

R2025b 官方文档未提供。

## 参数

### 用于更改字节序的模块参数

### **Number of input ports** — 端口数量 `1` (默认)

输入端口数量会根据此参数自动调整，且输出端口数量等于输入端口数量。

#### 编程用法

|  |
| --- |
| **模块参数：**`numInp` |

### **Machine word length** — 转换的单词长度 `Byte` (默认) | `Word` | `Double Word`

从列表中选择要将数据转换的目标计算机字长度。

#### 编程用法

|  |
| --- |
| **模块参数：** /> |

### Byte Reversal 模块参数

### **Number of inputs** — 端口数量 `1` (默认)

输入端口数量会根据此参数自动调整，且输出端口数量等于输入端口数量。

#### 编程用法

|  |
| --- |
| **模块参数：**`numInp` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 中推出**

## 描述

将小端数据转换为大端格式以供大端处理器使用

Byte Reversal/Change Endianess 模块实现了 Simulink® Real-Time™ 系统与采用*大端序*处理器运行的系统之间的通信。与 Intel® 80x86 系列兼容的处理器采用*小端*字节序。对于这种情况，请在 Pack 模块之前插入一个 Byte Reversal/Change Endianess 模块，并在 Unpack 模块之后再插入一个。以下是 Change Endianess 模块。
