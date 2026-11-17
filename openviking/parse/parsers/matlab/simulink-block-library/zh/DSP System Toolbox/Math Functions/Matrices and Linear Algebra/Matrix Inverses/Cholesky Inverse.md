---
type: simulink-block
title: 'Cholesky Inverse'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Inverses'
documentation_page: 'choleskyinverse'
documentation_source_path: 'ref/choleskyinverse.html'
language: zh-CN
chinese_source: worker-translation
---

# Cholesky Inverse

## 端口

### 输入

### **Input** — 输入矩阵 方阵

将输入指定为 Hermitian 正定方阵 *S*。当输入不是正定时，模块的行为由 **非正定输入** 参数指定。有关详细信息，请参阅 **非正定输入** 参数的描述。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Output** — 矩阵逆 方阵

Hermitian 正定输入矩阵 *S* 的逆，以方阵形式返回。这是 Cholesky 分解的方程。

S−1=(LL∗)−1

*L* 是对角线元素为正的下三角方阵，*L*\* 是 *L* 的 Hermitian（复共轭）转置。模块仅使用输入矩阵的对角线和上三角部分，并忽略对角线元素的任何虚部。Cholesky 分解所需的计算量是高斯消元（LU 分解）的一半，并且始终稳定。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **非正定输入** — 非正定输入 `Warning`（默认） | `Ignore` | `Error`

将针对非正定矩阵输入的响应指定为 `Ignore`、`Warning` 或 `Error`。

算法要求输入为 Hermitian 正定。当输入不是正定时，模块的行为由 **非正定输入** 参数指定。将此参数设置为：

- `Ignore` — 模块继续计算且不发出警报。输出不是有效逆矩阵。
- `Warning` — 模块在 MATLAB® 命令窗口中显示警告消息并继续仿真。输出不是有效逆矩阵。
- `Error` — 模块显示错误对话框并终止仿真。

**注意**

**非正定输入** 参数是诊断参数。与“配置参数”对话框中的所有诊断参数一样，在 Simulink® Coder™ 代码生成软件为此模块生成的代码中，它被设置为 `Ignore`。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Inverses

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

使用 Cholesky 分解计算 Hermitian 正定矩阵的逆

Cholesky Inverse 模块通过执行 Cholesky 分解来计算 Hermitian 正定输入矩阵 *S* 的逆。

S−1=(LL∗)−1

*L* 是对角线元素为正的下三角方阵，*L*\* 是 *L* 的 Hermitian（复共轭）转置。模块仅使用输入矩阵的对角线和上三角部分，并忽略对角线元素的任何虚部。Cholesky 分解所需的计算量是高斯消元（LU 分解）的一半，并且始终稳定。
