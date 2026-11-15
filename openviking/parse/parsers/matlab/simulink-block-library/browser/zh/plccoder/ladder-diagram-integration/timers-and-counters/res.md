---
type: simulink-block
title: 'RES'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Timers and Counters'
documentation_page: 'res'
documentation_source_path: 'ref/res.html'
language: zh-CN
chinese_source: worker-translation
---

# RES

## 端口

### 输入

### **EnableIn** — 启用输入 off（默认） | on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不会执行，并且输出不会更新。
### 输出

### **EN** — 启用输出 off（默认） | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不会执行，并且 **EnableOut** 信号会设置为 false。

## 参数

### **要复位的操作数标签** — 要复位的结构 A（默认） | character vector

指定要复位的 `tag`。在梯形图中，tag（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Operand Tag To Reset` 的属性，请在 Ladder Diagram Program 模块中打开 **程序变量** 表。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCTagToReset` |
| **类型**：character vector |
| **值**：character vector |
| **默认**：`'A'` |

### **标签结构** — 结构类型 'TIMER or COUNTER'（默认） | 'CONTROL'

指定要复位的结构类型。

| 类型 | 描述 |
| --- | --- |
| `TIMER or COUNTER` | 清除结构的 `ACC` 字段。 |
| `CONTROL` | 清除结构的 `POS` 字段。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCTagDataType` |
| **类型**：character vector |
| **值**：'TIMER or COUNTER'|'CONTROL' |
| **默认**：'TIMER or COUNTER' |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

复位

`RES` 模块实现 `RES` 梯形图逻辑指令。当梯级条件为 true 时，模块会复位 `TIMER`、`COUNTER` 或 `CONTROL` 结构的值。
