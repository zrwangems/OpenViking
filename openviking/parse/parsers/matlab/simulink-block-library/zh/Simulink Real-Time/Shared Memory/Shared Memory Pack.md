---
type: simulink-block
title: 'Shared Memory Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Shared Memory'
documentation_page: 'sharedmemorypack'
documentation_source_path: 'io_ref/sharedmemorypack.html'
language: zh-CN
chinese_source: worker-translation
---

# Shared Memory Pack

## 端口

R2025b 中未记录。

## 参数

### **Partition struct** — 结构体名称 `[]`（默认）

输入预定义共享内存分区结构体的名称。

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

共享内存打包

Shared Memory Pack 模块将指定的分区结构体打包为无结构的双字数组向量。它将一个或多个不同数据类型的 Simulink® 信号转换为该向量。通常，pack 模块的输入是 write 模块的输出。Simulink 接口不感知结构体；请将每个结构体段的输出作为 Shared Memory Pack 模块的输入传入。

内存分区由 Simulink 信号组构成，这些信号被组合成 32 位字的块（数据包）。在开始配置此模块之前，请确保已按照共享内存制造商的要求预定义了共享内存分区结构体。

此模块忽略分区结构体的 **Address** 字段。
