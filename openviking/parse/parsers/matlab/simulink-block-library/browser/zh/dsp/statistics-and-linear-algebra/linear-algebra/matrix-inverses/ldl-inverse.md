---
type: simulink-block
title: 'LDL Inverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Matrix Inverses'
documentation_page: 'ldlinverse'
documentation_source_path: 'ref/ldlinverse.html'
language: zh-CN
chinese_source: worker-translation
---

# LDL Inverse

## 端口

### 输入

### **Input** — 输入矩阵，方阵

指定输入为 Hermitian 正定方阵 *S*。当输入不是正定矩阵时，模块将按照 **Non-positive definite input** 参数指定的行为做出反应。有关更多详细信息，请参见 **Non-positive definite input** 参数的描述。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Output** — 矩阵逆，方阵

Hermitian 正定输入矩阵 *S* 的逆，以方阵形式返回。以下是 LDL 分解的方程。

S−1=(LDL\*)−1

*L* 是单位对角线元素的下三角方阵，*D* 是对角矩阵，*L*\* 是 *L* 的 Hermitian（复共轭）转置。仅使用输入矩阵的对角线和下三角部分，并且忽略对角线元素的任何虚部。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **Non-positive definite input** — 非正定输入 `Warning`（默认） | `Ignore` | `Error`

将针对非正定矩阵输入的响应指定为 `Ignore`、`Warning` 或 `Error`。

该算法要求输入为 Hermitian 正定矩阵。当输入不是正定矩阵时，模块将按照 **Non-positive definite input** 参数指定的行为做出反应。以下选项可用：

- `Ignore` — 继续计算，并且不发出警报。输出不是有效的逆。
- `Warning` — 在 MATLAB® 命令窗口中显示警告消息，并继续仿真。输出不是有效的逆。
- `Error` — 显示错误对话框并终止仿真。

**注意**

**Non-positive definite input** 参数是一个诊断参数。与 Configuration Parameters 对话框上的所有诊断参数一样，在 Simulink® Coder™ 代码生成软件为此模块生成的代码中，它设置为 `Ignore`。

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

在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 LDL 分解计算 Hermitian 正定矩阵的逆

LDL Inverse 模块通过执行 LDL 分解来计算 Hermitian 正定输入矩阵 *S* 的逆。

S−1=(LDL\*)−1

*L* 是单位对角线元素的下三角方阵，*D* 是对角矩阵，*L*\* 是 *L* 的 Hermitian（复共轭）转置。仅使用输入矩阵的对角线和下三角部分，并且忽略对角线元素的任何虚部。

LDL 分解所需的计算量是高斯消元（LU 分解）的一半，并且始终稳定。它比 Cholesky 分解更高效，因为它避免计算对角线元素的平方根。
