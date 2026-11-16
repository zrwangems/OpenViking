---
type: simulink-block
title: 'TON'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'ton'
documentation_source_path: 'ref/ton.html'
language: zh-CN
chinese_source: worker-translation
---

# TON

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，**EnableIn** 为 false，模块不执行，输出不会更新。
### 输出

### **EN** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果到模块的 **EnableIn** 输入为 false，模块实现的逻辑不执行，**EnableOut** 信号设置为 false。

## 参数

### **Timer Tag** — 定时器结构 T（默认）| character vector

以 `tags` 的格式指定定时器参数。在 Ladder Diagrams 中，tags（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **Program Variables** 表。定时器 tag 的 `Data Type` 为 `Bus:TIMER` 类型，其初始值指定为包含以下字段的结构体：

| 字段 | 描述 | 默认值 |
| --- | --- | --- |
| `PRE` | 预设值指定累积值必须达到的值（1 millisecond units），之后指令才指示其已完成 | 0 |
| `ACC` | 累积值指定自 `TON` 指令启用以来已经过的 milliseconds 数量。 | 0 |
| `EN` | 使能位包含该指令上次执行时的 rung-condition-in。 | 0 |
| `TT` | 定时位被置位时表示定时操作正在进行。 | 0 |
| `DN` | 完成位被置位时表示定时操作已完成（或暂停）。 | 0 |

#### 编程用法

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'T'` |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

接通延时定时器

TON 模块实现 `TON` 梯形图逻辑指令。当梯级条件为 true 时，模块累积时间，直到：

- 定时器被禁用
- 定时器完成
