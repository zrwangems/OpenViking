---
type: simulink-block
title: 'Least Squares Polynomial Fit'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Polynomial Functions'
documentation_page: 'leastsquarespolynomialfit'
documentation_source_path: 'ref/leastsquarespolynomialfit.html'
language: zh-CN
chinese_source: worker-translation
---

# Least Squares Polynomial Fit

## 端口

### 输入

### **输入** — 输入数据向量 | 矩阵

指定输入数据为大小为 *M*×*N* 的向量或矩阵。该模块将长度为 *M* 的无方向向量输入视为 *M*×1 矩阵。

**数据类型：** `single` | `double`

### 输出

### **输出** — 多项式系数列向量 | 矩阵

在最小二乘意义下最佳拟合输入数据的多项式的系数，以列向量或大小为 (*n*+1)×*N* 的矩阵形式返回，其中 *n* 是您在 **多项式阶数** 参数中指定的值。

(*n*+1)×*N* 输出矩阵 *c* 的每一列表示一组 *n*+1 个系数，用于描述输入对应列的最佳拟合多项式。每一列中的系数按指数降序排列，*c*1、*c*2、...、*c*n+1。

有关此模块如何计算多项式系数的详细信息，请参阅算法。

**数据类型：** `single` | `double`

## 参数

### **控制点 (X)** — 控制点 `(0:31)/31`（默认）| 向量

指定每个输入列中的数据所对应的自变量的值。对于 *M*×*N* 输入，此参数必须是长度为 *M* 的向量。

**可调：** 是

### **多项式阶数 (N)** — 多项式阶数 `3`（默认）| 正整数

指定模块用于构造最佳拟合的多项式阶数 *n*。系数数量为 *n*+1。

## 所属库

DSP System Toolbox / Math Functions / Polynomial Functions

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算在最小二乘意义下最佳拟合输入数据的多项式系数

Least Squares Polynomial Fit 模块计算在最小二乘意义下最佳拟合输入数据的 *n* 阶多项式的系数，其中 *n* 是您在 **多项式阶数** 参数中指定的值。该模块为 *M*×*N* 输入 *u* 的每一列计算一组不同的 *n*+1 个系数。
