---
type: simulink-block
title: 'Variable Write'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Input/Output'
documentation_page: 'variablewrite'
documentation_source_path: 'ref/variablewrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Write

## 端口

R2025b 中未记录。

## 参数

### **Data Tag** — 要写入的数据 A (default) | boolean

指定要写入的数据位，格式为 `tags`。在 Ladder Diagrams 中，tags（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Data Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **Program Variables** 表。

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

Variable Write

该模块用作输出变量赋值。
