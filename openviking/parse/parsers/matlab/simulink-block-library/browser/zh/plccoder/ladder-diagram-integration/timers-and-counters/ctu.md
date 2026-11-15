---
type: simulink-block
title: 'CTU'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'ctu'
documentation_source_path: 'ref/ctu.html'
language: zh-CN
chinese_source: worker-translation
---

# CTU

## 端口

### 输入

### **EnableIn** — 使能输入 off (default) | on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，**EnableIn** 为 false，则模块不会执行，输出也不会更新。
### 输出

### **CU** — 递增计数使能输出 off (default) | on

递增计数使能输出包含该指令上次执行时的梯级输入条件。默认情况下，**CU** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不会执行，并且 **CU** 信号会设置为 false。

## 参数

### **计数器标签** — 计数器结构 C (default) | character vector

以 `tags` 格式指定计数器参数。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag` 的属性，请打开 Ladder Diagram Program 模块中的 **程序变量** 表。计数器标签的 `Data Type` 为 `Bus:COUNTER` 类型，其初始值指定为包含以下字段的结构体：

| 字段 | 描述 | 默认值 |
| --- | --- | --- |
| `PRE` | 预设值指定在指令指示完成之前累计值必须达到的值 | 0 |
| `ACC` | 累计值指定指令已计数的转换次数。 | 0 |
| `CU` | 递增计数使能包含该指令上次执行时的 `rung-condition-in`。 | 1 |
| `CD` | 递减计数使能。 | 1 |
| `DN` | 完成位在被置位时表示计数操作已完成 | 0 |
| `OV` | 溢出位在被置位时表示计数器递增超过了上限 2,147,483,647 | 0 |
| `UN` | 下溢位在被置位时表示计数器递减超过了下限 -2,147,483,648。 | 0 |

#### 编程用法

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'T'` |

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

递增计数

CTU 模块实现 `CTU` 梯形图逻辑指令。当梯级条件为 true 时，模块向上计数。
