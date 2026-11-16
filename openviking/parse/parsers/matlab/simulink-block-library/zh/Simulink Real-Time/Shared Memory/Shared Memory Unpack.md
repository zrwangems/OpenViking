---
type: simulink-block
title: 'Shared Memory Unpack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Shared Memory'
documentation_page: 'sharedmemoryunpack'
documentation_source_path: 'io_ref/sharedmemoryunpack.html'
language: zh-CN
chinese_source: official
---

# Shared Memory Unpack

## 端口

R2025b 官方文档未提供。

## 参数

### **Partition struct** — 结构体名称 `[]` (默认)

输入预定义共享内存分区结构体的名称。该模块将双字数组向量解包到此结构体中。

#### 编程用法

|  |
| --- |
| **模块参数：**`partition` |

## 所属库

Simulink Real-Time / Shared Memory

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 中推出**

## 描述

共享内存解包

Shared Memory Unpack 模块将来自 Shared Memory Pack 模块的无结构双字数组向量解包至指定的分区结构体中。

在开始配置此模块之前，请确保您已根据共享内存制造商的要求预先定义了共享内存分区结构体。

此模块忽略分区结构体中的 **Address** 字段。
