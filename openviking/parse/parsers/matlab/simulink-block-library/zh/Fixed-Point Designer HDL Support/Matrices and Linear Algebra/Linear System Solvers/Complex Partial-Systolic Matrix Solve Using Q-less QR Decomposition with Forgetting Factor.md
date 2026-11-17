---
type: simulink-block
title: 'Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'complexpartialsystolicmatrixsolveusingqlessqrdecompositionwithforgettingfactor'
documentation_source_path: '../fixedpoint/ref/complexpartialsystolicmatrixsolveusingqlessqrdecompositionwithforgettingfactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行 向量

矩阵 *A* 的行，指定为向量。*A* 是流式数据的无限高矩阵。如果 *B* 为 single 或 double，则 *A* 必须与 *B* 具有相同的数据类型。如果 *A* 为定点数据类型，则 *A* 必须为有符号类型，使用二进制小数点缩放，并具有与 *B* 相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **B** — 矩阵 *B* 矩阵 | 向量

矩阵 *B*，指定为向量或矩阵。*B* 是一个 *n*×*p* 矩阵，其中 *n* ≥ 2。如果 *A* 为 single 或 double，则 *B* 必须与 *A* 具有相同的数据类型。如果 *B* 为定点数据类型，则 *B* 必须为有符号类型，使用二进制小数点缩放，并具有与 *A* 相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validInA** — A 输入是否有效 `Boolean` 标量

`A(i, :)` 输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 输入端口的信号何时有效。当此值为 `1`（`true`）且 `readyA` 值为 `1`（`true`）时，模块捕获 `A(i,:)` 输入端口的值。当此值为 `0`（`false`）时，模块忽略输入样本。

发送 `true` 的 `validInA` 信号后，在 `readyA` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等到 `readyA` 被设置为 `false` 后再发送另一个 `true` 的 `validInA` 信号。

**数据类型：** `Boolean`

### **validInB** — 输入 B 是否有效 `Boolean` 标量

输入 `B` 是否有效，指定为 Boolean 标量。此控制信号指示来自 `B` 输入端口的信号何时有效。当此值为 `1`（`true`）且 `readyB` 值为 `1`（`true`）时，模块捕获 `B` 输入端口的值。当此值为 `0`（`false`）时，模块忽略输入样本。

发送 `true` 的 `validInB` 信号后，在 `readyB` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等到 `readyB` 被设置为 `false` 后再发送另一个 `true` 的 `validInB` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1（`true`）时，模块停止当前计算并清除所有内部状态。当此值为 0（`false`）且 `validInA` 和 `validInB` 值为 1（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **X** — 矩阵 *X* 矩阵 | 向量

矩阵 *X*，以矩阵或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制信号指示输出端口 `X` 处的数据何时有效。当此值为 `1`（`true`）时，模块已成功计算出一行 *X*。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **readyA** — 模块是否已准备好接收输入 A `Boolean` 标量

模块是否已准备好接收输入 A，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 1（`true`）且 `validInA` 值为 1（`true`）时，模块在下一个时间步接受输入数据。当此值为 0（`false`）时，模块在下一个时间步忽略输入数据。

发送 `true` 的 `validInA` 信号后，在 `readyA` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等到 `readyA` 被设置为 `false` 后再发送另一个 `true` 的 `validInA` 信号。

**数据类型：** `Boolean`

### **readyB** — 模块是否已准备好接收输入 B `Boolean` 标量

模块是否已准备好接收输入 B，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 1（`true`）且 `validInB` 值为 1（`true`）时，模块在下一个时间步接受输入数据。当此值为 0（`false`）时，模块在下一个时间步忽略输入数据。

发送 `true` 的 `validInB` 信号后，在 `readyB` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等到 `readyB` 被设置为 `false` 后再发送另一个 `true` 的 `validInB` 信号。

**数据类型：** `Boolean`

## 参数

### **Number of columns in matrix A and rows in matrix B** — 矩阵 *A* 的列数和矩阵 *B* 的行数 `4`（默认）| 正整数值标量

矩阵 *A* 的列数和矩阵 *B* 的行数，指定为正整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`n` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`4` |

### **Number of columns in matrix B** — 矩阵 *B* 的列数 `1`（默认）| 正整数值标量

矩阵 *B* 的列数，指定为正整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`p` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`1` |

### **Forgetting factor** — 对矩阵的每一行进行分解后应用的遗忘因子 0.99（默认）| 实正标量

对矩阵的每一行进行分解后应用的遗忘因子，指定为实正标量。当 *A* 的每一行被无限期输入时，输出会被更新。

#### 编程使用

|  |
| --- |
| **模块参数**：`forgettingFactor` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`0.99` |

### **Regularization parameter** — 正则化参数 0（默认）| 实非负标量

正则化参数，指定为非负标量。较小的正正则化参数值可以改善问题的条件数并减小估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的减小通常会带来更小的均方误差。

#### 编程使用

|  |
| --- |
| **模块参数**：`regularizationParameter` |
| **类型**：character vector |
| **值**：real nonnegative scalar |
| **默认值**：`0` |

### **Output datatype** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为 `fixdt(1,18,14)`、`double`、`single`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputType` |
| **类型**：character vector |
| **值**：`'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值**：`'fixdt(1,18,14)'` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以改进资源利用率

此模块依赖于部分脉动 QR 分解模块。自 23a 起，当您更新图时，QR 分解模块中构成部分脉动流水线的循环会被展开。此更新的内部架构消除了仿真和生成代码中的死操作，从而需要更少的硬件资源。此模块在时钟和位真保真度方面与之前版本中这些模块的库版本仿真一致。

### R2022a：支持 Tikhonov 正则化参数

Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor 模块现在支持 Tikhonov 正则化参数。

### R2021a：减少 HDL 资源利用率

此模块现在具有改进的算法，可在硬件受限的目标平台上减少资源利用率。

## 描述

使用无 Q QR 分解计算具有无限行数的复值矩阵方程 A' A X = B 中 X 的值

Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor 模块使用无 Q QR 分解求解线性方程组 *A*'*A**X* = *B*，其中 *A* 和 *B* 为复值矩阵。*A* 是表示流式数据的无限高矩阵。

当正则化参数非零时，Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor 在分解 *A* 的行之前，将第一个上三角因子 *R* 初始化为 *λ**In*，其中 *λ* 是正则化参数，*In* = `eye(n)`。
