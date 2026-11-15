---
type: simulink-block
title: 'Permute Matrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Matrix Operations'
documentation_page: 'permutematrix'
documentation_source_path: 'slref/permutematrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Permute Matrix

## 端口

### 输入

### **A** — 输入矩阵 标量 | 向量 | 矩阵

输入矩阵，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **P** — 索引矩阵 标量 | 向量

索引矩阵，指定为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated`
### 输出

### **Port\_1** — 输出信号 向量 | 矩阵

输出信号，指定为向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **Permute** — 置换方法 `Columns` （默认） | `Rows`

通过置换输入的行或列来构造输出矩阵的方法。

当 **Permute** 参数设置为：

- `Rows` –– 该模块使用 `A` 的行创建具有相同列维度的矩阵。输入 `P` 是长度为 *L* 的向量，其元素确定 `A` 的每一行必须放置在 *L*×*N* 输出矩阵中的位置。

  ```
  y = [A(P(1),:) ; A(P(2),:) ; A(P(3),:) ; ... ; A(P(end),:)] % Equivalent MATLAB code
  ```

  对于行置换，该模块将端口 `A` 处的长度为 *M* 的未定向向量输入视为 *M*×1 矩阵。
- `Columns` –– 该模块使用 `A` 的列创建具有相同行维度的矩阵。输入 `P` 是长度为 *L* 的向量，其元素确定 `A` 的每一列必须放置在 *M*×*L* 输出矩阵中的位置。

  ```
  % Equivalent MATLAB code y = [A(:,P(1)) A(:,P(2)) A(:,P(3)) ... A(:,P(end))]
  ```

  对于列置换，该模块将端口 `A` 处的长度为 *N* 的未定向向量输入视为 1×*N* 矩阵。

#### 编程用法

|  |
| --- |
| **模块参数**：`mode` |
| **类型**：character vector, string |
| **值**：`' Columns'` | `'Rows'` |
| **默认值**：`' Columns'` |

### **Index mode** — 索引模式 `One-based` （默认） | `Zero-based`

当设置为 `One-based` 时，置换向量 `P` 中的值 `1` 指输入矩阵 `A` 的第一行或第一列。当设置为 `Zero-based` 时，`P` 中的值 `0` 指 `A` 的第一行或第一列。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroOneIdxMode` |
| **类型**：character vector, string |
| **值**：`' Zero-based'` | `'One-based'` |
| **默认值**：`'One-based'` |

### **Invalid permutation index** — 对无效索引值的响应 `Clip index` （默认） | `Clip and warn` | `Generate error`

对无效索引值的响应。当输入 `P` 中的索引值引用矩阵 `A` 中不存在的行或列时，该模块按此参数中的指定进行响应。以下选项可用：

- `Clip index` –– 将索引裁剪到最近的有效值（行置换为 1 或 M，列置换为 1 或 N），并且*不*发出警报。示例：对于 3×7 输入矩阵，列索引 9 被裁剪为 7，行索引 -2 被裁剪为 1。
- `Clip and warn` –– 在 MATLAB® 命令行窗口中显示警告消息，并按前一项所述裁剪索引。
- `Generate error` –– 显示错误对话框并终止仿真。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数**：`errmode` |
| **类型**：character vector, string |
| **值**： `'Clip index'` | `'Clip and warn'` | `'Generate error'` |
| **默认值**： `'Clip index'` |

### **Error when length of P is not equal to Permute dimension size** — P 长度的错误消息 `off` （默认） | `on`

当置换向量 `P` 的长度不等于输入矩阵 `A` 的行数或列数时，用于显示错误对话框并终止仿真的选项。

您可以通过将此参数设置为 `on` 来选择打开错误对话框并终止仿真。

#### 编程用法

|  |
| --- |
| **模块参数**：`checkDims` |
| **类型**：character vector, string |
| **值**： `'off'` | `'on'` |
| **默认值**： `'off'` |

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2023b: Permute Matrix 模块行主序支持更新

Permute Matrix 模块现在支持行主序算法以及针对行主序数组布局的代码生成。

### R2021b: 创建 Permute Matrix 模块已移至 Simulink Matrix Operations 库

Permute Matrix 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 库移至 **Simulink** > **Matrix Operations** 库。所有现有模型继续正常工作。

## 描述

重新排列矩阵的行或列

Permute Matrix 模块按照索引输入 `P` 的指定，重新排列 *M*×*N* 输入矩阵 `A` 的行或列。
