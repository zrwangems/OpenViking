---
type: simulink-block
title: 'CPT'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'cpt'
documentation_source_path: 'ref/cpt.html'
language: zh-CN
chinese_source: worker-translation
---

# CPT

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认） | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，**EnableIn** 为 false，则模块不执行，且输出不会更新。

### 输出

### **EnableOut** — 使能输出 off（默认） | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不会执行，并且 **EnableOut** 信号设置为 false。

### **dest** — 输出信号 标量

计算表达式后得到的结果放置在目标位置。

**数据类型：** `int8` | `int16` | `int32` | `single`

## 参数

### **要计算的表达式** — 要计算的表达式 'Expr'（默认） | 字符向量

指定要计算的表达式。表达式由 `tags` 和/或立即值组成，并由运算符分隔。在梯形图中，`tags`（变量）用于表示输入、输出和内部存储器，其属性包括 `Data Type`、`Initial Value` 和 `size`。要更改 `Expression to Evaluate` 的属性，请在 Ladder Diagram Program block 中打开 **程序变量** 表。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCOperandTag` |
| **类型**：字符向量 |
| **值**：字符向量 |
| **默认值**：`'Expr'` |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

计算表达式

CPT 模块实现 `CPT` 梯形图逻辑指令。当梯级条件为 true 时，模块计算表达式 **Expr**，并将结果输出到目标（`dest`）。
