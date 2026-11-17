---
type: simulink-block
title: 'Cholesky Solver'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'choleskysolver'
documentation_source_path: 'ref/choleskysolver.html'
language: zh-CN
chinese_source: worker-translation
---

# Cholesky Solver

## 端口

### 输入

### **S** — 输入 *S* 矩阵 *M*-by-*M* 矩阵

通过此端口指定输入 *M*-by-*M* 方阵 *S*。该矩阵必须为 Hermitian 正定。该模块仅使用矩阵的对角线及上三角部分，并忽略对角元素中的任何虚部。输入 *S* 和 *B* 必须具有相同的行数。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **B** — *B* 矩阵 *M*-by-*N* 矩阵 | *M*-by-1 向量

在 *SX* = *B* 方程中将 *B* 矩阵指定为 *M*-by-*N* 矩阵或 *M*-by-1 向量。

当指定 *M*-by-1 向量时，该模块将端口 **B** 处的长度为 *M* 的未定向向量输入视为 *M*-by-1 矩阵。输入 *S* 和 *B* 必须具有相同的行数。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **X** — 方程组的解 *M*-by-*N* 矩阵 | *M*-by-1 矩阵

该模块将输出返回为 *M*-by-*N* 矩阵或 *M*-by-1 矩阵。矩阵 *X* 的大小与矩阵 *B* 的大小相同。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **Non-positive definite input** — 对非正定矩阵输入的响应 `Ignore` (默认) | `Warning` | `Error`

输入矩阵 *S* 必须为 Hermitian 正定。

当输入不是正定矩阵时，该模块会根据你在 **Non-positive definite input** 参数中指定的行为作出反应。

- `Ignore` — 继续计算，不发出任何提示。输出不是有效解。
- `Warning` — 继续计算，并在 MATLAB® 命令窗口中显示警告消息。输出不是有效解。
- `Error` — 显示错误对话框并终止仿真。

**注意**

**Non-positive definite input** 参数是诊断参数。与配置参数对话框中的所有诊断参数一样，在 Simulink® Coder™ 代码生成软件为此模块生成的代码中，该参数被设置为 `Ignore`。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

当 S 为方阵 Hermitian 正定矩阵时，求解 SX = B 得到 X

Cholesky Solver 模块通过将 Cholesky 分解应用于输入矩阵来求解线性方程组 *SX* = *B*，其中：

- *S* 是通过 **S** 端口输入的 *M*-by-*M* 方阵。该矩阵必须为 Hermitian 正定。
- *B* 是通过 **B** 端口输入的 *M*-by-*N* 矩阵。
- *X* 是 *M*-by-*N* 输出矩阵，并且是这些方程的唯一解。
