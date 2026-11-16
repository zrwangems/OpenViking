---
type: simulink-block
title: 'Matrix Exponential'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'matrixexponential'
documentation_source_path: 'ref/matrixexponential.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix Exponential

## 端口

### 输入

### **Input 1** — 数据输入矩阵

将输入数据指定为方阵。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Output 1** — 矩阵指数输出矩阵

输入方阵的矩阵指数输出。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

未在 R2025b 中记录。

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

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算矩阵指数

Matrix Exponential 模块使用带 Pade 逼近的缩放与平方算法计算方阵的矩阵指数。
