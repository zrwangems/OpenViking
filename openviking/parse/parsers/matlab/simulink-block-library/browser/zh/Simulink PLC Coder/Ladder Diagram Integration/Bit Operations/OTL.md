---
type: simulink-block
title: 'OTL'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'otl'
documentation_source_path: 'ref/otl.html'
language: zh-CN
chinese_source: worker-translation
---

# OTL

## 端口

R2025b 中未记录。

## 参数

### **Operand Tag** — 要测试的位 A（默认）| boolean

指定要修改的数据位。数据位以 `tags` 的格式指定。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并具有 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **Program Variables** 表。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCOperandTag` |
| **类型**：character vector |
| **值**：character vector |
| **默认值**：`'A'` |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019a 中引入**

## 描述

输出锁存

`OTL` 是梯形图的基本构建模块之一。OTL 模块实现 `OTL` 梯形逻辑指令。当梯级条件为 true 时，该模块将操作数标签（数据位）设置为 true。该数据位保持 true，直到被清除，通常由 OTU 模块清除。当梯级条件变为 false 时，该模块不会更改数据位的状态。
