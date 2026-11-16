---
type: simulink-block
title: 'ONS'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Bit Operations'
documentation_page: 'ons'
documentation_source_path: 'ref/ons.html'
language: zh-CN
chinese_source: worker-translation
---

# ONS

## 端口

### 输入

### **EnableIn** — 使能输入 off (default) | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，且输出不会更新。
### 输出

### **EN** — 使能输出 off (default) | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不会执行，且 **EnableOut** 信号设置为 false。

## 参数

### **存储位** — 内部存储位 SB (default) | boolean

内部存储位，用于保留上次执行指令时的 `rung-condition-in`。以 `tags` 格式指定。在 Ladder Diagrams 中，tags（变量）用于表示输入、输出和内部存储器，其属性包括 `Data Type`、`Initial Value` 和 `size`。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块内的 **程序变量** 表。

#### 编程用法

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'SB'` |

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

单触发

ONS 模块实现 `ONS` 指令。每当 `rung-condition-in` 从 false 转换为 true 时，该模块使梯级的其余部分为 true。
