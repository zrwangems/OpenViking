---
type: simulink-block
title: 'Implies'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'implies'
documentation_source_path: 'ref/implies.html'
language: zh-CN
chinese_source: official
---

# Implies

## 端口

### 输入

### **Values** — 输入信号 标量 | 元胞数组

Implies 模块接受 Simulink 软件支持的所有数值数据类型的信号。有关 Simulink 软件支持的数据类型的讨论，请参阅Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Design Verifier / Verification Utilities

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2009a 中推出**

## 描述

指定生成特定响应的条件

您可以使用 Implies 模块指定生成给定响应的条件；例如，当您踩下汽车的制动踏板时，巡航控制机构会被禁用。如果输入 A 为 true，并且输入 B 为 false，则输出为 false；对于所有其他输入对组，输出均为 true。

您可以在任何模型中使用 Implies 模块，而不仅仅是在运行 Simulink® Design Verifier™ 软件时使用该模块。
