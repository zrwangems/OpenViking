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
chinese_source: worker-translation
---

# Byte Reversal/Change Endianess

## 端口

R2025b 中未记录。

## 参数

### Change Endianess 的模块参数

### **Number of input ports** — 端口数量 `1`（默认）

输入端口数量随此参数调整，输出数量等于输入数量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `numInp` |

### **Machine word length** — 转换的字长 `Byte`（默认） | `Word` | `Double Word`

从列表中选择要将数据转换为的机器字长。

#### 程序化使用

|  |
| --- |
| **模块参数：** /> |

### Byte Reversal 模块参数

### **Number of inputs** — 端口数量 `1`（默认）

输入端口数量随此参数调整，输出数量等于输入数量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `numInp` |

## 所属库

Simulink Real-Time / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

## 描述

为大端处理器反转小端数据

Byte Reversal/Change Endianess 模块提供 Simulink®
Real-Time™ 系统与运行 *big-endian* 处理器的系统之间的通信。与 Intel® 80x86 系列兼容的处理器是 *little-endian*。对于这种情况，在 Pack 模块之前插入一个 Byte Reversal/Change Endianess 模块，并在 Unpack 模块之后紧接着插入另一个。以下是 Change Endianess 模块。
