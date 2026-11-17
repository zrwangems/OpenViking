---
type: simulink-block
title: 'QR Solver'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'qrsolver'
documentation_source_path: 'ref/qrsolver.html'
language: zh-CN
chinese_source: worker-translation
---

# QR Solver

## 端口

### 输入

### **A** — 系统矩阵 向量 | 矩阵

将系统矩阵 A 指定为向量或大小为 *M*×*N* 的矩阵。该模块将长度为 *M* 的无向向量输入视为 *M*×1 矩阵。

系统通过在 `A` 端口对 *M*×*N* 矩阵 A 应用 QR 分解来求解。

**数据类型：** `single` | `double`
**复数支持：** 是

### **B** — 系统方程右侧矩阵 向量 | 矩阵

将系统方程 A*X*=B 的右侧矩阵 B 指定为 *M*×*L* 矩阵。

当 B 为向量时，解 *X* 使残差的向量 2-范数最小化（B−A*X* 为残差）。当 B 为矩阵时，解 *X* 使残差的矩阵 Frobenius 范数最小化。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **X** — 最小范数残差解 向量 | 矩阵

A*X*=B 的最小范数残差解，以 *N*×*L* 矩阵 *X* 返回。该模块确定 *X* 以使 B−A*X* 各元素的平方和最小化。最小范数残差解对于超定和恰定线性系统是唯一的，但对于欠定线性系统不唯一。因此，当 QR Solver 应用于欠定系统时，输出 *X* 的选择使得 *X* 中非零元素的个数最小化。

当 B 为向量时，该解使残差的向量 2-范数最小化（B−A*X* 为残差）。当 B 为矩阵时，该解使残差的矩阵 Frobenius 范数最小化。在这种情况下，*X* 的各列是 *L* 个对应系统 A*X*k=Bk 的解，其中 Bk 是 B 的第 *k* 列，*X*k 是 *X* 的第 *k* 列。

有关该模块如何计算 *X* 的更多信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

求 A X =B 的最小范数残差解

QR Solver 模块求解线性系统 A*X*=B，该系统可以是超定的、欠定的或恰定的。该模块对矩阵 A 应用 QR 分解以求得 A*X*=B 的最小范数残差解。有关更多详细信息，请参阅算法。
