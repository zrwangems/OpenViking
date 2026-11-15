---
type: simulink-block
title: 'COP'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Memory and File Operations'
documentation_page: 'cop'
documentation_source_path: 'ref/cop.html'
language: zh-CN
chinese_source: worker-translation
---

# COP

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认） | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不会更新。

### **src** — 源 scalar | vector | matrix

它给出存储在源处的值。此数据被复制到目标。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `single` | `String` | `Structure`

### **length** — 元素长度 scalar

它给出要复制的源元素数量。

**数据类型：** `int8` | `int16` | `int32`

### 输出

### **EnableOut** — 使能输出 off（默认） | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果到模块的 **EnableIn** 输入为 false，则模块实现的逻辑不执行，**EnableOut** 信号被设置为 false。

## 参数

### **源初始元素索引** — 源起始索引 1（默认） | scalar

仅当源为数组时，才会使用源起始索引。它指定要复制到目标中的第一个元素的索引。如果源不是数组，则 `Source Initial Element Index` 的值为 1。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCSRCArrayIndex` |
| **类型**: scalar |
| **值**: scalar |
| **默认值**: `1` |

**数据类型：** `int8` | `int16` | `int32` | `single`

### **目标数组名称** — 目标 A（默认） | boolean

从源复制的数据存储在目标中。目标以 `tags` 格式指定。在梯形图中，tags（变量）用于表示输入、输出和内部存储器，其属性包括 `Data Type`、`Initial Value` 和 `size`。要更改 `Destination Array Name` 的属性，请打开 Ladder Diagram Program 模块中的 **程序变量** 表。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'A'` |

### **目标初始元素索引** — 目标起始索引 scalar

仅当源为数组时，才会使用目标起始索引。它指定复制数据的目标起始索引。如果源数据和目标数据未存储在数组中，则 `Destination Initial Element Index` 的值为 1。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCDestArrayIndex` |
| **类型**: scalar |
| **值**: scalar |
| **默认值**: `0` |

**数据类型：** `int8` | `int16` | `int32` | `single`

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

复制文件

COP 模块实现 `COP` 指令。当梯级条件为 true 时，该模块用于复制源的数据并将其存储在目标处，同时保持源不变。
