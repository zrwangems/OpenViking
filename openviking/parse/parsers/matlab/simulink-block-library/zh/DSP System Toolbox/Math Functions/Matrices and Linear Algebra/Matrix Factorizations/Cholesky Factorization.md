---
type: simulink-block
title: 'Cholesky Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'choleskyfactorization'
documentation_source_path: 'ref/choleskyfactorization.html'
language: zh-CN
chinese_source: worker-translation
---

# Cholesky Factorization

## 端口

### 输入

### **S** — 输入矩阵 方阵

将输入矩阵指定为方阵。仅当输入具有以下特性时，模块输出才有效：

- Hermitian — 该模块不检查输入是否为 Hermitian。该模块仅使用输入的对角线和上三角来计算输出。
- 实值对角元素 — 该模块忽略输入对角元素的任何虚部。
- 正定 — 当输入不是正定时，该模块会向您发出通知，具体如 **Non-positive definite input** 参数说明中所述。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **LL'** — 下三角和上三角因子 方阵

该模块输出一个方阵，其下三角元素来自 *L*，上三角元素来自 *L*'。输出形式与 MATLAB® `chol` 函数的输出形式不同。为了将 Cholesky Factorization 模块的输出转换为 MATLAB 形式，请使用以下方程：

```
R = triu(LL');
```

为了仅提取 *L* 矩阵，请将 Cholesky Factorization 模块的输出 *LL'* 传递给 Extract Triangular Matrix 模块。将 Extract Triangular Matrix 的 **Extract** 参数设置为 `Lower` 可提取 *L* 矩阵。将 **Extract** 参数设置为 `Upper` 可提取 *L*' 矩阵。

在此图中，`LL'` 是 Cholesky Factorization 模块的输出。由于舍入误差，这些方程产生的结果与 MATLAB 结果并不完全相同。

**由 L 和 L \* 组成的模块输出**

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **Non-positive definite input** — 非正定输入 `Warning`（默认） | `Ignore` | `Error`

将针对非正定矩阵输入的响应指定为以下之一：

- `Ignore` — 继续计算并且 *不* 发出警报。输出 *不是* 有效的因子分解。部分因子分解将出现在输出的左上角。
- `Warning` — 在 MATLAB 命令窗口中显示警告消息，并继续仿真。输出 *不是* 有效的因子分解。部分因子分解将出现在输出的左上角。
- `Error` — 显示错误对话框并终止仿真。

为了生成有效输出，模块算法要求输入为正定。有关详细信息，请参阅 **S** 端口说明。

**注意**

**Non-positive definite input** 参数是诊断参数。与“配置参数”对话框上的所有诊断参数一样，在 Simulink® Coder™ 代码生成软件为此模块生成的代码中，它设置为 `Ignore`。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Factorizations

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

将方阵 Hermitian 正定矩阵分解为三角分量

Cholesky Factorization 模块将方阵 Hermitian 正定输入矩阵 *S* 唯一分解为

S=LL'

其中 *L* 是具有正对角元素的下三角方阵，*L*' 是 *L* 的 Hermitian（复共轭）转置。

请注意，*L* 和 *L*' 在输出矩阵中共享同一对角线。Cholesky 分解所需计算量是高斯消去法（LU 分解）的一半，并且始终稳定。
