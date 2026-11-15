---
type: simulink-block
title: 'Extract Diagonal'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'extractdiagonal'
---

# Extract Diagonal

Extract main diagonal of input matrix

## 中文

提取输入矩阵的主对角线

### 库

Simulink / Matrix Operations

### 描述

Extract Diagonal 模块用 *M*×*N* 输入矩阵 `A` 主对角线上的元素填充未定向输出向量。

等效的 MATLAB® 代码如下：

    D = diag(A)

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要从中提取对角线的输入矩阵，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes
#### 输出

#### **Port\_1** — 输出信号 向量

由每个对角线元素组成的输出向量。

输出的数据类型和复/实性与输入相同。输出向量的长度为 `min(M,N)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖 `memcpy` 或
`memset` 函数（`string.h`）。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

#### R2021b: Extract Diagonal 模块已移至 Simulink Matrix Operations 库

Extract Diagonal 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 库移至 **Simulink** > **Matrix Operations** 库。所有现有模型继续正常工作。

## Libraries

Simulink / Matrix Operations

## Description

The Extract Diagonal block populates the unoriented output vector with
the elements on the main diagonal of the *M*-by-*N*
input matrix `A`.

Equivalent MATLAB® code is given by:

```
D = diag(A)
```

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input matrix to extract the diagonal from, specified as a scalar,
vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal vector

Output vector of each diagonal element.

The output is the same data type and complexity as the input. The
output vector has length `min(M,N)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Extract Diagonal Block Moved to Simulink Matrix Operations Library

The Extract Diagonal block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** library to the **Simulink** > **Matrix Operations**library. All existing models continue to work.
