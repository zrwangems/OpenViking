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
chinese_source: worker-translation
---

# Shared Memory Unpack

## 端口

R2025b 中未记录。

## 参数

### **Partition struct** — 结构体名称 `[]`（默认值）

输入预定义共享内存分区结构体的名称。该模块将双字数组向量解包到该结构体中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `partition` |

## 所属库

Simulink Real-Time / Shared Memory

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

## 描述

共享内存解包

Shared Memory Unpack 模块将非结构化双字数组向量（来自 Shared Memory Pack 模块）解包到指定的分区结构体中。

在开始配置此模块之前，请确保您已按照共享内存制造商的要求拥有预定义的共享内存分区结构体。

此模块忽略分区结构体的 **Address** 字段。
