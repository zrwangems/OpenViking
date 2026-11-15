---
type: simulink-block
title: 'OTE'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'ote'
documentation_source_path: 'ref/ote.html'
language: zh-CN
chinese_source: worker-translation
---

# OTE

## 端口

R2025b 中未记录。

## 参数

### **Operand Tag** — 要测试的位 A（默认）| boolean

指定要修改的数据位。数据位以 `tags` 格式指定。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并带有 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **Program Variables** 表。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'A'` |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

输出激励

`OTE` 是梯形图的构建块之一。OTE 模块实现 `OTE` 梯形图逻辑指令。该模块检查 `rung-condition-in` 的状态，并置位或清零操作数标签（数据位）。如果梯级条件为 true，则该模块将数据位设置为 true。
