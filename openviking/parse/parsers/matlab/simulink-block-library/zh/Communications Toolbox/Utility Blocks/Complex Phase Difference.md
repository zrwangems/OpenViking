---
type: simulink-block
title: 'Complex Phase Difference'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'complexphasedifference'
documentation_source_path: 'ref/complexphasedifference.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Phase Difference

## 端口

### 输入

### **In1** — 第一输入信号 标量 | 列向量 | 矩阵

第一输入信号，指定为标量、列向量或矩阵。
如果两个输入信号均为非标量，则它们必须具有相同的维度。

**注意**

该模块处理复数信号。输入端口处的实数值会类型转换为具有 `+j0` 复数分量的复数值。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **In2** — 第二输入信号 标量 | 列向量 | 矩阵

第二输入信号，指定为标量、列向量或矩阵。
如果两个输入信号均为非标量，则它们必须具有相同的维度。
**In2** 的数据类型必须与 **In1** 相同。

**注意**

该模块处理复数信号。输入端口处的实数值会类型转换为具有 `+j0` 复数分量的复数值。

**数据类型：** `double` | `single`
### 输出

### **Out1** — 相移差 标量 | 列向量 | 矩阵

以 radians 表示的相移差，返回为标量、列向量或矩阵。如果任一输入信号为非标量，则输出信号维度与那个非标量输入信号的维度匹配。
输出是第二输入信号与第一输入信号之间的相位差。输出信号的元素介于 -π 和 π 之间，并且与输入信号具有相同的数据类型。

## 参数

R2025b 中未记录。

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

两个复数信号之间的相位差

Complex Phase Difference 模块计算第二输入信号与第一输入信号之间以 radians 表示的相位差。输出的元素介于 -π 和 π 之间。该模块独立处理每一对对应元素。
