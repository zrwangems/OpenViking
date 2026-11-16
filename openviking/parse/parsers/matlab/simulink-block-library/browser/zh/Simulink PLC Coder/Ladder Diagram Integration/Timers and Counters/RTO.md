---
type: simulink-block
title: 'RTO'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'rto'
documentation_source_path: 'ref/rto.html'
language: zh-CN
chinese_source: worker-translation
---

# RTO

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，**EnableIn** 为 false，模块不执行，并且输出不会更新。
### 输出

### **EN** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果该模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不会执行，并且 **EnableOut** 信号设置为 false。

## 参数

### **定时器标签** — 定时器结构 T（默认）| character vector

以 `tags` 的格式指定定时器参数。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **程序变量** 表。定时器标签的 `Data Type` 为 `Bus:TIMER` 类型，其初始值指定为包含以下字段的结构体：

| 字段 | 描述 | 默认值 |
| --- | --- | --- |
| `PRE` | 预设值指定在指令指示其完成之前，累加值必须达到的值（1 millisecond units） | 0 |
| `ACC` | 累加值指定自 `RTO` 指令启用以来已经过的 milliseconds 数量。 | 0 |
| `EN` | 使能位包含该指令上次执行时的梯级条件输入。 | 0 |
| `TT` | 定时位在被置位时表示定时操作正在进行中。 | 0 |
| `DN` | 完成位在被置位时表示定时操作已完成（或已暂停）。 | 0 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认**: `'T'` |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

保持型定时器接通

RTO 模块实现 `RTO` 梯形图逻辑指令。当梯级条件为 true 时，该模块会累加时间，直到：

- 定时器被禁用
- 定时器完成
