---
type: simulink-block
title: 'Width'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'width'
documentation_source_path: 'slref/width.html'
language: zh-CN
chinese_source: official
---

# Width

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输入信号的宽度 标量

输出是输入信号的宽度，指定为标量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输出数据类型模式** — 输出数据类型模式 **选择固有数据类型** (默认) | **通过反向传播继承** | **所有端口都具有相同数据类型**

指定输出数据类型与输入相同，或通过反向传播继承数据类型。您也可以选择从**输出数据类型**参数的下拉列表中指定内置数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputDataTypeScalingMode` |
| **类型：**字符向量 |
| **值：**`'Choose intrinsic data type' | 'Inherit via back propagation' | 'All ports same datatype'` |
| **默认值：**`'Choose intrinsic data type'` |

### **输出数据类型** — 输出数据类型 **double** (默认) | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32**

当您为**输出数据类型模式**选择**选择固有数据类型**时，此参数可见。从下拉列表中选择一种内置数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`DataType` |
| **类型：**字符向量 |
| **值：**`'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32'` |
| **默认值：**`'double'` |

### **始终使用常量采样时间** — 始终使用常量采样时间 off (默认) | on

要始终使用常量采样时间，请选择此参数。要继承采样时间，请清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**：`AlwaysUseConstantSampleTime` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2024a: Width 模块支持符号维度

Width 模块具有以下更改：

- 支持符号维度。
- 新参数**始终使用常量采样时间**。

## 描述

输出输入向量的宽度

Width 模块生成其输入向量的宽度作为输出。

可使用总线数组作为 Width 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅使用总线数组组合非虚拟总线。
