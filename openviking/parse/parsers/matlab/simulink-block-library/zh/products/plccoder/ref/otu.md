---
type: simulink-block
title: 'OTU'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'otu'
documentation_source_path: 'ref/otu.html'
language: zh-CN
chinese_source: worker-translation
---

# OTU

## 端口

在 R2025b 中未记录。

## 参数

### **操作数标签** — 要测试的位 A（默认） | boolean

指定要修改的数据位。数据位以 `tags` 的格式指定。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并带有 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块内的 **程序变量**表。

#### 编程用法

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

输出解锁

`OTU` 是梯形图的构建块之一。OTU 模块实现 `OTU` 梯形图逻辑指令。当梯级条件为 true 时，模块将操作数标签（数据位）清除为 false。当梯级条件变为 false 时，模块不会更改数据位的状态。它通常用在 OTL 模块之后，以解锁状态并禁用梯级。
