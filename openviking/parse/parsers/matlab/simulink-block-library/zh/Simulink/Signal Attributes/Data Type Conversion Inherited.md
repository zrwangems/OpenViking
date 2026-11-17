---
type: simulink-block
title: 'Data Type Conversion Inherited'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypeconversioninherited'
documentation_source_path: 'slref/datatypeconversioninherited.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Type Conversion Inherited

## 端口

### 输入

### **Port\_1** — 参考信号 标量 | 向量 | 矩阵 | N 维数组

参考信号，定义用于转换输入信号 **u** 的数据类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — 要转换的输入信号 标量 | 向量 | 矩阵 | N 维数组

要转换为参考数据类型的输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **y** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出为输入信号 **u** 转换为参考数据类型后的结果。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **Input and Output to have equal** — 定点数据类型转换的约束 `Real World Value`（默认） | `Stored Integer`

在定点数据表示的上下文中，指定输入和输出中哪种类型必须相等。

- `Real World Value` — 指定使输入的 `Real World Value` 等于输出的 `Real World Value` 的目标。
- `Stored Integer` — 指定使输入的 `Stored Integer` 值等于输出的 `Stored Integer` 值的目标。

#### 编程使用

|  |
| --- |
| **模块参数**：`ConvertRealWorld` |
| **类型**：character vector |
| **值**：`'Real World Value' | 'Stored Integer'` |
| **默认值**：`'Real World Value'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。
有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Saturate to max or min when overflows occur** — 溢出操作方法 `off`（默认） | `on`

选中此复选框时，溢出饱和到数据类型可表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和适用于模块上的每次内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用继承的数据类型和定标从一种数据类型转换为另一种数据类型

Data Type Conversion Inherited 模块将一个输入转换为另一个输入的数据类型和定标。第一个输入用作参考信号。第二个输入 **u** 通过继承数据类型和定标信息转换为参考类型。（有关各种模块方向的端口顺序说明，请参阅 Identify Port Location on Rotated or Flipped Block。）

继承数据类型和定标具有以下优势：

- 使重用现有模型更加容易。
- 允许您以更少的精力创建新的定点模型，因为您可以避免指定相关参数的细节。
