---
type: simulink-block
title: 'Divide by Constant and Round'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: ''
documentation_page: 'dividebyconstantandround'
documentation_source_path: 'ref/dividebyconstantandround.html'
language: zh-CN
chinese_source: worker-translation
---

# Divide by Constant and Round

## 端口
```yaml
ports:
- name: X
  summary: 被除数 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Y
  summary: 除法与舍入运算的结果 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **X** — 被除数 标量 | 向量 | 矩阵 | N 维数组

被除数，指定为标量、向量、矩阵或 N 维数组。

Divide by Constant and Round 不支持字长大于 65,535 的数据类型。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Y** — 除法与舍入运算的结果 标量 | 向量 | 矩阵 | N 维数组

除法与舍入运算的结果，以标量、向量、矩阵或 N 维数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Denominator
  summary: 除数 10 （默认） | 标量
  group: ''
  block_parameter: Denominator
  type: 字符向量
  values: 求值为正的、实值、有限定点或数值的 MATLAB® 表达式
- name: Rounding Method
  summary: 要使用的舍入方法 Floor （默认） | Ceiling | Nearest | Zero | Convergent
  group: ''
  block_parameter: RndMeth
  type: 字符向量
  values: '''Floor'' | ''Ceiling'' | ''Nearest'' | ''Zero'' | ''Convergent'''
```

### **Denominator** — 除数 10 （默认） | 标量

除数，指定为正的、实值、有限标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Denominator` |
| **类型：** 字符向量 |
| **值：** 求值为正的、实值、有限定点或数值的 MATLAB® 表达式 |
| **数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认：** `'10'` |

### **Rounding Method** — 要使用的舍入方法 `Floor` （默认） | `Ceiling` | `Nearest` | `Zero` | `Convergent`

要使用的舍入方法，指定为以下值之一：

- `Floor` — 向负无穷方向舍入到最接近的整数。
- `Ceiling` — 向正无穷方向舍入到最接近的整数。
- `Nearest` — 舍入到最接近的整数。遇到平局时向正无穷方向舍入到最接近的整数。
- `Zero` — 向零方向舍入到最接近的整数。
- `Convergent` — 舍入到最接近的整数。遇到平局时舍入到最接近的偶数整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Floor'` | `'Ceiling'` | `'Nearest'` | `'Zero'` | `'Convergent'` |
| **默认：** `'Floor'` |
## 所属库

Fixed-Point Designer

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

## 版本历史

**在 R2021a 中引入**

## 描述

将输入除以常量并舍入为整数

Divide by Constant and Round 模块输出将输入除以常量后的结果，并使用指定的舍入方法将结果舍入为整数。

Divide by Constant and Round 模块使用的算法在功能上类似于 Granlund-Montgomery-Warren 方法。除法运算通过乘以倒数来计算，这通常可在嵌入式系统上获得更好的性能。
