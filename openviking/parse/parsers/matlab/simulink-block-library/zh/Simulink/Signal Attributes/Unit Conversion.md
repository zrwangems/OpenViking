---
type: simulink-block
title: 'Unit Conversion'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'unitconversion'
documentation_source_path: 'slref/unitconversion.html'
language: zh-CN
chinese_source: official
---

# Unit Conversion

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

转换单位后的输出信号的维度与输入信号相同。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输出数据类型** — 输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承**

指定输出数据类型。

- **继承: Inherit via internal rule** - Simulink® 在考虑嵌入式目标硬件的属性的同时，会选择中间和输出数据类型来平衡数值准确性、性能和生成的代码大小。如果更改了嵌入式目标的设置，则依内部规则选择的数据类型可能会发生变化。
- **继承: Inherit via back propagation** - 通过反向传播继承输出数据类型。内部规则确定中间数据类型，并且 Simulink 将最终结果转换为输出数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputType` |
| **类型：**字符向量 |
| **值：**`'Inherit via internal rule' | 'Inherit via back propagation'` |
| **默认值：**`'Inherit via internal rule'` |

## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016a 中推出**

## 描述

转换单位

Unit Conversion 模块将输入信号的单位转换为输出信号的单位。如果单位之间成倍数关系或存在一个偏移量，或是互为倒数，则模块可以执行转换，例如：

- *y* = *a*\**U*
- *y* = *a*\**U*+*b*，其中 *a* 是尺度，*b* 是偏移量
- *y* = *a*/*U*

此模块支持普通、快速和快速加速模式以及快速重启。
