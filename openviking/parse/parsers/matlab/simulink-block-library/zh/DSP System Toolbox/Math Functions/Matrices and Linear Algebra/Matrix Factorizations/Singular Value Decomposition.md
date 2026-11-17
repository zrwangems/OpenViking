---
type: simulink-block
title: 'Singular Value Decomposition'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'singularvaluedecomposition'
documentation_source_path: 'ref/singularvaluedecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Singular Value Decomposition

## 端口

### 输入

### **A** — 输入矩阵 matrix

将输入指定为 *M*×*N* 矩阵。输出 *U* 和 *V* 的维度取决于 *M* = *N*、*M* > *N*，还是 *M* < *N*。有关详细信息，请参阅输出端口 **U** 和 **V** 的说明。

长度为 *N* 的行输入被视为长度为 *N* 的列。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **U** — *U* 分量矩阵

奇异值分解的 *U* 分量，返回为以下之一：

- 当 *M* = *N* 时，*U* 是一个 *M*×*M* 酉矩阵。
- 当 *M* > *N* 时，*U* 是一个 *M*×*N* 矩阵，其列是酉矩阵的前 *N* 列。
- 当 *N* > *M* 时，*U* 是一个 *M*×*M* 酉矩阵。

如果奇异值分解计算未能收敛，端口 **U** 上的输出是大小正确的未定义矩阵。

#### 依赖关系

要启用此端口，请选中 **Show ports with U and V matrices** 复选框。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **S** — *S* 分量列向量

奇异值分解的 *S* 分量，返回为长度为 *P* 的列向量，其中包含正奇异值。

请注意，输出 *S* 的第一个（最大）元素等于矩阵 *A* 的 2-范数。

如果奇异值分解计算未能收敛，端口 **S** 上的输出是大小正确的未定义向量。

**数据类型：** `single` | `double`

### **V** — *V* 分量矩阵

奇异值分解的 *V* 分量，返回为以下之一：

- 当 *M* = *N* 时，*V* 是一个 *M*×*M* 酉矩阵。
- 当 *M* > *N* 时，*V* 是一个 *N*×*N* 酉矩阵。
- 当 *N* > *M* 时，*V* 是一个 *N*×*M* 矩阵，其列是酉矩阵的前 *M* 列。

如果奇异值分解计算未能收敛，端口 **V** 上的输出是大小正确的未定义矩阵。

#### 依赖关系

要启用此端口，请选中 **Show ports with U and V matrices** 复选框。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **E** — 错误端口标量

未能收敛，返回为以下之一：

- `0` — 奇异值分解计算收敛。
- `1` — 奇异值分解计算不收敛。

如果奇异值分解计算未能收敛，端口 **U**、**S** 和 **V** 上的输出是大小正确的未定义矩阵。

#### 依赖关系

要启用此端口，请选中 **Show error status port (E)** 复选框。

**数据类型：** `Boolean`

## 参数

### **Show ports with U and V matrices** — 显示具有 *U* 和 *V* 矩阵的端口 on (默认) | off

选中此复选框可启用 **U** 和 **V** 输出端口。

### **Show error status port (E)** — 显示错误状态端口 off (默认) | on

选中此复选框可启用输出端口 **E**，它报告未能收敛。有关详细信息，请参阅输出端口 **E** 的说明。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

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

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用奇异值分解对矩阵进行因式分解

Singular Value Decomposition 模块对 *M*×*N* 输入矩阵 *A* 进行因式分解，使得

A=U⋅diag(S)⋅V\*

其中

- *U* 是一个 *M*×*P* 矩阵
- *V* 是一个 *N*×*P* 矩阵
- *S* 是一个长度为 *P* 的向量
- *P* 定义为
  min(*M*,*N*)
