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
chinese_source: worker-translation
---

# Unit Conversion

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

具有转换后单位的输出信号，其维度与输入信号相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation`

指定输出数据类型。

- `Inherit: Inherit via internal rule` —
  Simulink® 选择中间数据类型和输出数据类型，以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。如果更改嵌入式目标设置，内部规则所选择的数据类型可能会发生变化。
- `Inherit: Inherit via back propagation` —
  输出数据类型通过反向传播继承。内部规则确定中间数据类型，Simulink 将最终结果转换为输出数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputType` |
| **类型：** 字符向量 |
| **值：** `'Inherit via internal rule' | 'Inherit via back propagation'` |
| **默认值：** `'Inherit via internal rule'` |

## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016a 中引入**

## 描述

转换单位

Unit Conversion 模块将输入信号的单位转换为输出信号。如果单位之间通过比例因子或偏移量相关联，或者互为倒数单位，该模块可以执行转换，例如：

- *y* = *a*\**U*
- *y* =
  *a*\**U*+*b*，其中
  *a* 是比例，*b* 是
  偏移量
- *y* = *a*/*U*

该模块支持普通、加速和快速加速模式以及快速重启。
