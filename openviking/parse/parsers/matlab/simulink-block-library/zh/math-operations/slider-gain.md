---
type: simulink-block
title: 'Slider Gain'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'slidergain'
language: zh-CN
chinese_source: official
---

# Slider Gain

使用滑块更改标量增益

## 所属库

Simulink / Math Operations

## 描述

Slider Gain 模块执行标量增益，您可以在仿真过程中修改标量增益。使用滑块参数即可修改该增益。

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

Slider Gain 模块接受实数或复数值标量、向量或矩阵输入。该模块支持定点数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输入乘以增益 标量 | 向量 | 矩阵

Slider Gain 模块的输出是输入乘以常量增益值的结果。当该模块的输入为实数且增益为复数时，输出为复数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **滑块增益** — 增益值 `0` (默认) | 实数值

选择应用于输入的增益值。

#### 编程用法

|  |
| --- |
| **模块参数**：`gain` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'1'` |

### **低** — 滑块范围的下限 `0` (默认) | 实数值

指定滑块范围的下限。

#### 编程用法

|  |
| --- |
| **模块参数**：`low` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'0'` |

### **高** — 滑块范围的上限 `2` (默认) | 实数值

指定滑块范围的上限。

#### 编程用法

|  |
| --- |
| **模块参数**：`high` |
| **类型**：字符向量 |
| **值**：实数标量 |
| **默认值**：`'2'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史记录

**在 R2006a 之前推出**
