---
type: simulink-block
title: 'Divide by Constant and Round'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Arithmetic Operations'
documentation_page: 'dividebyconstantandround'
documentation_source_path: 'ref/dividebyconstantandround.html'
language: zh-CN
chinese_source: official
---

# Divide by Constant and Round

## 端口

### 输入

### **X** — 被除数 标量 | 向量 | 矩阵 | N 维数组

被除数，指定为标量、向量、矩阵或 N 维数组。

Divide by Constant and Round 不支持字长大于 65,535 的数据类型。定点数据类型不支持斜率偏置表示。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持:** 是
### 输出

### **Y** — 除法和舍入运算的结果 标量 | 向量 | 矩阵 | N 维数组

除法和舍入运算的结果，以标量、向量、矩阵或 N 维数组形式返回。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **分母** — 除数 10 (默认) | 标量

除数，指定为正实数值有限标量。

#### 编程用法

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型：**字符向量 |
| **值：**计算结果为正实数值有限定点或数值的 MATLAB® 表达式 |
| **数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认值：**`'10'` |

### **舍入方法** — 要使用的舍入方法 **向下** (默认) | **向上** | **最邻近值** | **零** | **收敛**

要使用的舍入方法，指定为以下值之一：

- **向下** - 朝负无穷方向舍入到最接近的整数。
- **向上** - 向正无穷方向舍入到最接近的整数。
- **最邻近值** - 舍入到最接近的整数。结值向正无穷方向舍入到最接近的整数。
- **零** - 向零方向舍入到最接近的整数。
- **收敛** - 舍入到最接近的整数。结值舍入到最接近的偶数。

#### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：** `'Floor'` | `'Ceiling'` | `'Nearest'` | `'Zero'` | `'Convergent'` |
| **默认值：**`'Floor'` |

## 所属库

Fixed-Point Designer

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

定点数据类型不支持斜率偏置表示。

## 版本历史

**在 R2021a 中推出**

## 描述

将输入除以常量并舍入到整数

Divide by Constant and Round 模块输出输入除以某个常量的结果，并使用指定的舍入方法将结果舍入为整数。

Divide by Constant and Round 模块使用的算法在功能上类似于 Granlund-Montgomery-Warren 方法。除法运算是通过与倒数相乘计算的，这通常有助于在嵌入式系统上实现更好的性能。
