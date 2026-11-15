---
type: simulink-block
title: 'Permute Matrix'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'permutematrix'
---

# Permute Matrix

Reorder matrix rows or columns

## 中文

重排矩阵的行或列

### 库
Simulink / Matrix Operations

### 描述
Permute Matrix 模块根据索引输入 `P` 的指定，重排 *M*×*N* 输入矩阵 `A` 的行或列。

### 端口
#### 输入
#### **A** — 输入矩阵 标量 | 向量 | 矩阵
输入矩阵，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

#### **P** — 索引矩阵 标量 | 向量
索引矩阵，指定为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
#### 输出
#### **Port\_1** — 输出信号 向量 | 矩阵
输出信号，指定为向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 参数
#### **Permute** — 排列方法 `Columns`（默认） | `Rows`
通过排列输入的行或列来构造输出矩阵的方法。

当 **Permute** 参数设置为：

- `Rows` –– 该模块使用 `A` 的行创建一个具有相同列维度的矩阵。输入 `P` 是长度为 *L* 的向量，其元素确定 `A` 中的每一行必须放置在 *L*×*N* 输出矩阵中的位置。

  ```
  y = [A(P(1),:) ; A(P(2),:) ; A(P(3),:) ; ... ; A(P(end),:)] % Equivalent MATLAB code
  ```

  对于行排列，该模块将端口 `A` 处长度为 *M* 的未定向向量输入视为 M×1 矩阵。
- `Columns` –– 该模块使用 `A` 的列创建一个具有相同行维度的矩阵。输入 `P` 是长度为 *L* 的向量，其元素确定 `A` 中的每一列必须放置在 *M*×*L* 输出矩阵中的位置。

  ```
  % Equivalent MATLAB code y = [A(:,P(1)) A(:,P(2)) A(:,P(3)) ... A(:,P(end))]
  ```

  对于列排列，该模块将端口 `A` 处长度为 *N* 的未定向向量输入视为 1×*N* 矩阵。

#### 编程用法

|  |
| --- |
| **模块参数**：`mode` |
| **类型**：character vector, string |
| **值**：`' Columns'` | `'Rows'` |
| **默认值**：`' Columns'` |

#### **Index mode** — 索引模式 `One-based`（默认） | `Zero-based`
当设置为 `One-based` 时，排列向量 `P` 中的值 `1` 指输入矩阵 `A` 的第一行或第一列。当设置为 `Zero-based` 时，`P` 中的值 `0` 指 `A` 的第一行或第一列。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroOneIdxMode` |
| **类型**：character vector, string |
| **值**：`' Zero-based'` | `'One-based'` |
| **默认值**：`'One-based'` |

#### **Invalid permutation index** — 对无效索引值的响应 `Clip index`（默认） | `Clip and warn` | `Generate error`
对无效索引值的响应。当输入 `P` 中的索引值引用矩阵 `A` 的不存在行或列时，该模块按此参数中的指定进行反应。以下选项可用：

- `Clip index` –– 将索引裁剪到最接近的有效值（行排列时为 1 或 M，列排列时为 1 或 N），并且*不*发出警报。示例：对于 3×7 输入矩阵，列索引 9 被裁剪为 7，行索引 -2 被裁剪为 1。
- `Clip and warn` –– 在 MATLAB® 命令窗口中显示警告消息，并按前一项所述裁剪索引。
- `Generate error` –– 显示错误对话框并终止仿真。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数**：`errmode` |
| **类型**：character vector, string |
| **值**：`'Clip index'` | `'Clip and warn'` | `'Generate error'` |
| **默认值**：`'Clip index'` |

#### **Error when length of P is not equal to Permute dimension size** — P 长度的错误消息 `off`（默认） | `on`
当排列向量 `P` 的长度不等于输入矩阵 `A` 的行数或列数时，显示错误对话框并终止仿真的选项。

您可以通过将此参数设置为 `on`，选择打开错误对话框并终止仿真。

#### 编程用法

|  |
| --- |
| **模块参数**：`checkDims` |
| **类型**：character vector, string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。
在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

#### R2023b：Permute Matrix 模块行主序支持更新
Permute Matrix 模块现在支持行主序算法以及针对行主序数组布局的代码生成。

#### R2021b：创建 Permute Matrix 模块已移至 Simulink Matrix Operations 库
Permute Matrix 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 库移至 **Simulink** > **Matrix Operations** 库。所有现有模型仍可正常工作。

## Libraries

Simulink / Matrix Operations

## Description

The Permute Matrix block reorders the rows or columns of an
*M*-by-*N* input matrix `A` as
specified by indexing input `P`.

## Ports

### Input

### **A** — Input matrix scalar | vector | matrix

Input matrix, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **P** — Index matrix scalar | vector

Index matrix, specified as a scalar or vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
### Output

### **Port\_1** — Output signal vector | matrix

Output signal, specified as a vector or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Permute** — Permute method `Columns` (default) | `Rows`

Method of constructing the output matrix by permuting rows or columns of
the input.

When the **Permute** parameter is set to:

- `Rows` –– The block uses the rows of
  `A` to create a matrix that has the same
  column dimension. Input `P` is a
  length-*L* vector whose elements determine
  where each row from `A` must be placed in the
  *L*-by-*N* output
  matrix.

  ```
  y = [A(P(1),:) ; A(P(2),:) ; A(P(3),:) ; ... ; A(P(end),:)] % Equivalent MATLAB code
  ```

  For row permutation, the block treats the
  length-*M* unoriented vector input at the
  port `A` as an M-by-1 matrix.
- `Columns` –– The block uses the
  columns of `A` to create a matrix that has the
  same row dimension. Input `P` is a
  length-*L* vector whose elements determine
  where each column from `A` must be placed in
  the *M*-by-*L* output
  matrix.

  ```
  % Equivalent MATLAB code y = [A(:,P(1)) A(:,P(2)) A(:,P(3)) ... A(:,P(end))]
  ```

  For column permutation, the block treats the
  length-*N* unoriented vector input at port
  `A` as a 1-by-*N*
  matrix.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mode` |
| **Type**: character vector, string |
| **Values**:`' Columns'` | `'Rows'` |
| **Default**: `' Columns'` |

### **Index mode** — Index mode `One-based` (default) | `Zero-based`

When set to `One-based`, a value of
`1` in the permutation vector `P`
refers to the first row or column of the input matrix `A`.
When set to `Zero-based`, a value of
`0` in `P` refers to the first row or
column of `A`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroOneIdxMode` |
| **Type**: character vector, string |
| **Values**:`' Zero-based'` | `'One-based'` |
| **Default**: `'One-based'` |

### **Invalid permutation index** — Response to an invalid index value `Clip index` (default) | `Clip and warn` | `Generate error`

Response to an invalid index value. When an index value in input
`P` references a nonexistent row or column of matrix
`A`, the block reacts as specified in this parameter.
These options are available:

- `Clip index` –– Clip the index to the
  nearest valid value (1 or M for row permutation and 1 or N for
  column permutation) and *do not* issue an alert.
  Example: For a 3-by-7 input matrix, a column index of 9 is clipped
  to 7 and a row index of -2 is clipped to 1.
- `Clip and warn` –– Display a warning
  message in the MATLAB® Command Window and clip the index as described in the
  preceding bullet.
- `Generate error` –– Display an error
  dialog box and terminate the simulation.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `errmode` |
| **Type**: character vector, string |
| **Values**: `'Clip index'` | `'Clip and warn'` | `'Generate error'` |
| **Default**: `'Clip index'` |

### **Error when length of P is not equal to Permute dimension size** — Error message for P length `off` (default) | `on`

Option to display an error dialog box and terminate the simulation when
the length of the permutation vector `P` is not equal to
the number of rows or columns of the input matrix
`A`.

You can choose to open an error dialog box and terminate the simulation by
setting this parameter to `on`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `checkDims` |
| **Type**: character vector, string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
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

### R2023b: Permute Matrix Block Row-Major Support Update

The Permute Matrix block now supports row-major algorithms and code
generation for row-major array layout.

### R2021b: Create Permute Matrix Block Moved to Simulink Matrix Operations Library

The Permute Matrix block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** library to the **Simulink** > **Matrix Operations**library. All existing models continue to work.
