---
type: simulink-block
title: 'Puncture'
family: 'sequence-operations'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'puncture'
documentation_source_path: 'ref/puncture.html'
language: zh-CN
chinese_source: worker-translation
---

# Puncture

## 端口

### 输入

### **In** — 输入信号列向量

输入信号，指定为列向量。输入长度必须是 **Puncture vector** 参数长度的整数倍。

**数据类型：** `double` | `single`
**复数支持：** Yes
### 输出

### **Out** — 输出信号列向量

输出信号，以列向量形式返回。输出向量的长度是 **Puncture vector** 参数中 1 的个数的整数倍。输出信号仅包含输入信号中与 **Puncture vector** 中 1 的元素位置的整数倍对齐的那些元素。

## 参数

### **Puncture vector** — 打孔模式 `[1 1 0 1 0 1]'`（默认）| 二进制值列向量

打孔模式，指定为二进制值列向量。输入信号长度必须是 **Puncture vector** 参数长度的整数倍。该模块根据需要重复打孔模式，以包含所有输入元素。

- **Puncture vector** 中 0 的元素位置指示从输入信号中移除哪些元素以构造输出信号。
- **Puncture vector** 中 1 的元素位置指示保留输入信号中的哪些元素以构造输出信号。

## 所属库

Communications Toolbox / Sequence Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

输出对应于二进制打孔向量中 1 的元素

Puncture 模块通过移除输入向量的选定元素并保留其他元素来创建输出向量。该模块使用二进制 **Puncture vector** 参数确定要移除和保留哪些元素。该模块根据需要重复打孔模式，以包含所有输入元素。保留的元素在输出向量中出现的顺序与它们在输入向量中出现的顺序相同。
