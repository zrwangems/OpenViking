---
type: simulink-block
title: 'Interlacer'
family: 'sequence-operations'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'interlacer'
documentation_source_path: 'ref/interlacer.html'
language: zh-CN
chinese_source: worker-translation
---

# Interlacer

## 端口

### 输入

### **O** — 奇数编号元素向量

奇数编号元素，指定为向量。输入 `O` 和 `E` 的复/实性必须匹配。

**数据类型:** `double` | `single`
**复数支持:** Yes

### **E** — 偶数编号元素向量

偶数编号元素，指定为向量。输入 `O` 和 `E` 的复/实性必须匹配。

**数据类型:** `double` | `single`
**复数支持:** Yes
### 输出

### **Out** — 输出信号列向量

输出信号，返回为偶数长度列向量。输出向量中的奇数编号元素包含来自输入 `O` 的元素，输出向量中的偶数编号元素包含来自输入 `E` 的元素。输出向量具有与输入相同的数据类型和采样时间。

## 参数

在 R2025b 中未记录。

## 所属库

Communications Toolbox / Sequence Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

交替从两个输入向量中选择元素以生成输出向量

Interlacer 模块接受两个具有相同大小、复/实性和采样时间的向量。它通过交替取第一个输入（标记为 `O`，表示奇数）和第二个输入（标记为 `E`，表示偶数）中的元素来生成一个输出向量。
