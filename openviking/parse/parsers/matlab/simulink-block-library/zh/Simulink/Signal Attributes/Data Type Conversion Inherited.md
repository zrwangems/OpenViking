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
chinese_source: official
---

# Data Type Conversion Inherited

## 端口

### 输入

### **Port\_1** — 参考信号 标量 | 向量 | 矩阵 | N 维数组

参考信号，定义用于转换输入信号 **u** 的数据类型。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — 要转换的输入信号 标量 | 向量 | 矩阵 | N 维数组

要转换为参考数据类型的输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **y** — 输出信号 标量 | 向量 | 矩阵 | N 维数组

输出是输入信号 **u**，转换为参考数据类型。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **输入和输出具有相等的** — 转换定点数据类型的约束 **真实值** (默认) | **存储的整数**

在定点数据表示的上下文中，指定哪种类型的输入和输出必须相等。

- **真实值** - 指定希望输入的**真实值**等于输出的**真实值**。
- **存储的整数** - 指定希望输入的**存储的整数**值等于输出的**存储的整数**值。

#### 编程用法

|  |
| --- |
| **模块参数**：`ConvertRealWorld` |
| **类型：**字符向量 |
| **值**：`'Real World Value' | 'Stored Integer'` |
| **默认值：**`'Real World Value'` |

### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

### **发生溢出时饱和处理为最大值或最小值** — 溢出操作的方法 `off` (默认) | `on`

当您选中此复选框时，溢出将饱和处理为数据类型可表示的最大值或最小值。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用继承的数据类型和定标将一种数据类型转换为另一种

Data Type Conversion Inherited 模块将一个输入转换为另一个输入的数据类型和定标。第一个输入用作参考信号。第二个输入 **u** 通过继承数据类型和定标信息转换为参考类型。（有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。）

继承数据类型和定标具有以下优势：

- 可以更方便地重用现有模型。
- 您可以更轻松地创建新定点模型，因为无需执行关联参数指定等细节工作。
