---
type: simulink-block
title: 'Complex Phase Shift'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'complexphaseshift'
documentation_source_path: 'ref/complexphaseshift.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Phase Shift

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量 | 矩阵

输入信号，指定为标量、列向量或矩阵。

**注意**

此模块处理并输出复信号。输入端口处的实数值会被类型转换为带有 `+j0` 复数分量的复数值。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **Ph** — 相移 标量 | 列向量 | 矩阵

相移，以弧度为单位，指定为标量、列向量或矩阵。如果相移是非标量，则其维度必须与端口 **In** 处的信号相同。

**数据类型：** `double`
### 输出

### **Out1** — 相移后信号 标量 | 列向量 | 矩阵

相移后信号，返回为复数值标量、列向量或矩阵。此输出的维度和数据类型与输入信号相同。

## 参数

在 R2025b 中未记录。

## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对复信号应用复相移

Complex Phase Shift 模块对复信号应用复相移。此模块独立处理每一对对应元素。
