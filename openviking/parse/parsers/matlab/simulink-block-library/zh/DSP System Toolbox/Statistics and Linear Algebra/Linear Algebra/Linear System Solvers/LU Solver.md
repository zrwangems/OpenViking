---
type: simulink-block
title: 'LU Solver'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Linear System Solvers'
documentation_page: 'lusolver'
documentation_source_path: 'ref/lusolver.html'
language: zh-CN
chinese_source: worker-translation
---

# LU Solver

## 端口

### 输入

### **A** — 输入 *A* 矩阵 *M*×*M* 矩阵

通过此端口指定输入 *M*×*M* 方阵 *A*。输入 *A* 和 *B* 必须具有相同的行数。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **B** — *B* 矩阵 *M*×*N* 矩阵 | *M*×1 向量

将 *AX* = *B* 方程中的 *B* 矩阵指定为 *M*×*N* 矩阵或 *M*×1 向量。

当您指定 *M*×1 向量时，模块将端口 **B** 处的长度 *M* 无向向量输入视为 *M*×1 矩阵。输入 *A* 和 *B* 必须具有相同的行数。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **X** — 方程组的解 *M*×*N* 矩阵 | *M*×1 矩阵

模块将输出返回为 *M*×*N* 矩阵或 *M*×1 矩阵。*X* 矩阵的大小与 *B* 矩阵的大小相同。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

未在 R2025b 中记录。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

当 A 为方阵时，求解 AX = B

LU Solver 模块通过应用 LU 分解来求解线性系统 *A**X* = *B*，其中：

- *A* 是通过 **A** 端口输入的 *M*×*M* 方阵。
- *B* 是通过 **B** 端口输入的 *M*×*N* 矩阵。
- *X* 是 *M*×*N* 输出矩阵，并且是方程组的唯一解。
