---
type: simulink-block
title: 'SVD Solver'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'svdsolver'
documentation_source_path: 'ref/svdsolver.html'
language: zh-CN
chinese_source: worker-translation
---

# SVD Solver

## 端口

### 输入

### **A** — 输入 *A* 矩阵 *M*×*N* 矩阵

通过此端口将输入矩阵 *A* 指定为 *M*×*N* 矩阵。输入 *A* 和 *B* 必须具有相同的行数。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **B** — *B* 矩阵 *M*×*L* 矩阵 | *M*×1 向量

在 *AX* = *B* 方程中将矩阵 *B* 指定为 *M*×*L* 矩阵或 *M*×1 向量。

当您指定 *M*×1 向量时，该模块将端口 **B** 处长度为 *M* 的无方向向量输入视为 *M*×1 矩阵。输入 *A* 和 *B* 必须具有相同的行数。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **X** — 方程组的解 *N*×*L* 矩阵

**X** 端口处的输出是 *N*×*L* 矩阵 *X*。该模块计算 *X*，以最小化 *B* − *A**X*（残差）元素的平方和。

当 *B* 是向量时，此解最小化残差的向量 2-范数。当 *B* 是矩阵时，此解最小化残差的矩阵 Frobenius 范数。在这种情况下，*X* 的列是 *L* 个对应系统 *A**Xk* = *Bk* 的解，其中 *Bk* 是 *B* 的第 *k* 列，*Xk* 是 *X* 的第 *k* 列。

*X* 被称为 *A**X* = *B* 的最小范数残差解。对于超定和恰定线性系统，最小范数残差解是唯一的，但对于欠定线性系统，该解不是唯一的。因此，当您将 SVD Solver 模块应用于欠定系统时，该模块计算 *X* 以最小化 *X* 中非零项的数目。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **E** — 显示错误状态报告逻辑标量

如果奇异值分解计算收敛，该模块返回逻辑标量值 `0`；如果奇异值分解计算不收敛，则返回逻辑标量值 `1`。

**数据类型：** `Boolean`

## 参数

### **Show error status port (E)** — 选择以报告未能收敛 `off`（默认） | `on`

选择此项以启用 **E** 输出端口，该端口将未能收敛报告为以下之一：

- `0` — 奇异值分解计算收敛。
- `1` — 奇异值分解计算不收敛。

如果奇异值分解计算未能收敛，端口 **X** 的输出为预期大小的未定义矩阵。

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用奇异值分解求解 AX = B

SVD Solver 模块求解线性系统 *A**X* = *B*。该线性系统可以是超定、欠定或恰定。该模块通过对 **A** 端口的输入矩阵应用奇异值分解 (SVD) 分解来求解该系统。
