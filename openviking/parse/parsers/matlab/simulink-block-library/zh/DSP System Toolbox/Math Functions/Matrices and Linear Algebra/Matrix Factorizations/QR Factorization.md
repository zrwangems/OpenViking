---
type: simulink-block
title: 'QR Factorization'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'qrfactorization'
documentation_source_path: 'ref/qrfactorization.html'
language: zh-CN
chinese_source: worker-translation
---

# QR Factorization

## 端口

### 输入

### **A** — 输入向量 | 矩阵

将输入指定为大小为 *M*×*N* 的向量或矩阵。

该模块将长度为 *M* 的无方向向量输入视为 *M*×1 矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **Q** — QR 分解的正交归一分量 *Q* 向量 | 矩阵

QR 分解的正交归一分量 *Q*，
以向量或矩阵形式返回。*Q* 的大小
取决于 **Output size**
参数的设置：

*Q* 的大小取决于
**Output size** 参数的设置：

- 当您为输出大小选择 `Economy` 时，*Q* 是
  *M*×`min`(*M*,*N*)
  酉矩阵。

  ```
  [Q R E] = qr(A,0)   % Equivalent MATLAB code
  ```
- 当您为输出大小选择 `Full` 时，
  *Q* 是
  *M*×*M* 酉
  矩阵。

  ```
  [Q R E] = qr(A)      % Equivalent MATLAB code
  ```

**数据类型：** `single` | `double`
**复数支持：** Yes

### **R** — QR 分解的上三角分量 *R* 向量 | 矩阵

QR 分解的上三角分量 *R*，
以向量或矩阵形式返回。

*R* 的大小取决于
**Output size** 参数的设置：

- 当您为输出大小选择 `Economy` 时，
  *R* 是
  `min`(*M*,*N*)×*N*
  上三角矩阵。

  ```
  [Q R E] = qr(A,0)   % Equivalent MATLAB code
  ```
- 当您为输出大小选择 `Full` 时，
  *R* 是
  *M*×*N*
  上三角矩阵。

  ```
  [Q R E] = qr(A)      % Equivalent MATLAB code
  ```

**数据类型：** `single` | `double`
**复数支持：** Yes

### **E** — 列置换向量 向量

长度为 *N* 的列置换向量 *E*，其中 *N* 是输入矩阵的列数。

该模块选择列置换向量，以确保矩阵 *R* 的对角元素按幅值递减顺序排列。

|ri+1,j+1|<|ri,j|        i=j

有关该模块如何使用此向量的更多详细信息，请参阅算法。

**数据类型：** `single` | `double`

## 参数

### **Output size** — 输出大小 `Economy` (default) | `Full`

指定输出矩阵 *Q* 和
*R* 的大小：

- `Economy` — 当您选择此
  输出大小时，该模块输出一个
  *M*×min(*M*,*N*)
  酉矩阵 *Q* 和一个
  min(*M*,*N*)×*N*
  上三角矩阵 *R*。
- `Full` — 当您选择此
  输出大小时，该模块输出一个
  *M*×*M* 酉矩阵
  *Q* 和一个
  *M*×*N* 上三角
  矩阵 *R*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用
  MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项
  需要额外的启动时间，但可提供更快的后续
  仿真。

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

将任意矩阵分解为酉矩阵和上三角分量

QR Factorization 模块使用一系列 Householder
变换将输入矩阵 *A* 三角化。

QR 分解是求解线性方程组的重要工具，因为它具有
良好的误差传播特性以及酉矩阵的可逆性：

*Q*
 –1 = *Q*
`'`

其中 *Q*`'` 是 *Q* 的复共轭转置。

与 LU 和 Cholesky 分解不同，矩阵 *A* 对于 QR 分解不需要
是方阵。然而，QR 分解所需的运算次数是 LU Factorization（高斯消元）的两倍。

有关该模块如何执行 QR 分解的更多详细信息，请参阅算法。
