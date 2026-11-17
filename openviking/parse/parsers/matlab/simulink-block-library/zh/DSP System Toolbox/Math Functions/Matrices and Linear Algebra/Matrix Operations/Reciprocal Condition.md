---
type: simulink-block
title: 'Reciprocal Condition'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'reciprocalcondition'
documentation_source_path: 'ref/reciprocalcondition.html'
language: zh-CN
chinese_source: worker-translation
---

# Reciprocal Condition

## 端口

### 输入

### **Input** — 输入矩阵 方阵

将输入矩阵指定为方阵。

**数据类型：** `single` | `double`
### 输出

### **Output** — 倒数条件输出 标量

方阵输入
*A* 的条件数的倒数，以标量形式返回。

如果输入是良态的，输出接近 1.0。如果输入是
病态的，输出接近 0.0。

**数据类型：** `single` | `double`

## 参数

R2025b 中未记录。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算方阵在 1-范数下的倒数条件数

Reciprocal Condition 模块计算方阵输入矩阵 *A* 的条件数的
倒数。

以下是等效的 MATLAB® 代码。

```
y = rcond(A)
```

或

y=1κ=1‖A−1‖1‖A‖1,

其中 κ 是条件数（κ ≥ 1），*y* 是标量
输出（0 ≤ *y* < 1）。

矩阵 1-范数 ‖A‖1 是
*M*×*M* 矩阵 *A* 中的最大列和。

‖A‖1=1≤j≤Mmax∑i=1M|aij|

对于 3×3 矩阵：
