---
type: simulink-block
title: 'FLL'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Memory and File Operations'
documentation_page: 'fll'
documentation_source_path: 'ref/fll.html'
language: zh-CN
chinese_source: worker-translation
---

# FLL

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出不会更新。

### **src** — 源 scalar | vector | matrix

它给出存储在源处的值。此数据被复制到目标。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `single` | `String` | `Structure`

### **length** — 元素长度 scalar

要填充的目标元素数量。

**数据类型:** `int8` | `int16` | `int32`

### 输出

### **EnableOut** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不执行，且 **EnableOut** 信号设置为 false。

## 参数

### **Destination Array Name** — 目标 A（默认）| boolean

从源复制来的数据被填充到目标。目标以 `tags` 格式指定。在 Ladder Diagrams 中，tags（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Destination Array Name` 的属性，请打开 Ladder Diagram Program 模块中的 **Program Variables** 表。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'A'` |

### **Destination Initial Element Index** — 目标起始索引 scalar

目标起始索引仅在源为数组时使用。它指定数据复制到目标处的起始索引。如果源数据和目标数据未存储在数组中，则 `Destination Initial Element Index` 的值为 1。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCDestArrayIndex` |
| **类型**: scalar |
| **值**: scalar |
| **默认值**: `0` |

**数据类型:** `int8` | `int16` | `int32` | `single`

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

文件填充

FLL 模块实现 `FLL` 指令。当梯级条件为 true 时，该模块使用提供的源值填充一块内存。Source 保持不变。
