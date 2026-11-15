---
type: simulink-block
title: 'XIO'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'xio'
documentation_source_path: 'ref/xio.html'
language: zh-CN
chinese_source: worker-translation
---

# XIO

## 端口

在 R2025b 中未记录。

## 参数

### **Operand Tag** — 要测试的位 A（默认） | boolean

指定要测试的数据位。数据位以 `tags` 的格式指定。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **程序变量** 表。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'A'` |

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

检查是否断开

`XIO` 是梯形图的基本构建块之一。XIO 模块实现 `XIO` 梯形逻辑指令。该模块检查操作数标签（数据位）是否处于 off 条件。如果该位为 clear，则梯级使能。如果该位为 set，则梯级禁用。
