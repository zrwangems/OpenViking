---
type: simulink-block
title: 'Real Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: "Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Linear System Solvers / Solve A'AX = B with Infinitely Tall A Matrix"
documentation_page: 'realpartialsystolicmatrixsolveusingqlessqrdecompositionwithforgettingfactor'
documentation_source_path: 'ref/realpartialsystolicmatrixsolveusingqlessqrdecompositionwithforgettingfactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor

## 端口

### 输入

### **A(i,:)** — 实矩阵 *A* 的行 向量

实矩阵 *A* 的行，指定为向量。
*A* 是具有无限行数的流式数据矩阵。如果
*B* 是 single 或 double，则 *A* 必须与 *B* 具有相同的数据类型。如果 *A* 是定点数据类型，
则 *A* 必须是有符号的、使用二进制小数点定标，并且与 *B* 具有相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **B** — 矩阵 *B* 矩阵

实矩阵 *B*，指定为矩阵。*B* 是
*n*×*p* 矩阵，其中 *n* ≥ 2。如果 *A* 是 single 或 double，则 *B*
必须与 *A* 具有相同的数据类型。如果 *B* 是
定点数据类型，则 *B* 必须是有符号的、使用二进制小数点定标，
并且与 *A* 具有相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validInA** — A 输入是否有效 `Boolean` 标量

`A(i, ;)` 输入是否有效，指定为 Boolean
标量。此控制信号指示来自
`A(i,:)` 输入端口的数据何时有效。当此值为
`1`（`true`）且 `readyA`
值为 `1`（`true`）时，模块在 `A(i,:)` 输入端口捕获值。当此值为 `0`
（`false`）时，模块忽略输入样本。

发送 `true`
`validInA` 信号后，在 `readyA` 被设置为
`false` 之前可能会有一些延迟。为确保处理所有数据，
必须先等待 `readyA` 被设置为
`false`，然后再发送另一个 `true`
`validInA` 信号。

**数据类型：** `Boolean`

### **validInB** — B 输入是否有效 `Boolean` 标量

`B` 输入是否有效，指定为 Boolean 标量。此
控制信号指示来自 `B` 输入端口的数据何时
有效。当此值为 `1`（`true`）且
`readyB` 值为 `1`（`true`）时，
模块在 `B` 输入端口捕获值。当此
值为 `0`（`false`）时，模块忽略输入
样本。

发送 `true`
`validInB` 信号后，在 `readyB` 被设置为
`false` 之前可能会有一些延迟。为确保处理所有数据，
必须先等待 `readyB` 被设置为
`false`，然后再发送另一个 `true`
`validInB` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1（`true`）时，模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validInA` 和 `validInB` 值均为 1
（`true`）时，模块开始一个新的子帧。

**数据类型：** `Boolean`
### 输出

### **X** — 矩阵 *X* 向量 | 矩阵

矩阵 *X*，以向量或矩阵形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制
信号指示输出端口 `X` 处的数据何时有效。
当此值为 `1`（`true`）时，模块已成功计算 *X* 的一行。当此值为
`0`（`false`）时，输出数据
无效。

**数据类型：** `Boolean`

### **readyA** — 模块是否已准备好接收输入 A `Boolean` 标量

模块是否已准备好接收输入 A，以 Boolean 标量形式返回。此控制
信号指示模块何时准备好接收新输入数据。当此值为 1
（`true`）且 `validInA` 值为 1
（`true`）时，模块在下一时间步接受输入数据。当
此值为 0（`false`）时，模块在下一时间步忽略输入数据。

发送 `true`
`validInA` 信号后，在 `readyA` 被设置为
`false` 之前可能会有一些延迟。为确保处理所有数据，
必须先等待 `readyA` 被设置为
`false`，然后再发送另一个 `true`
`validInA` 信号。

**数据类型：** `Boolean`

### **readyB** — 模块是否已准备好接收输入 B `Boolean` 标量

模块是否已准备好接收输入 B，以 Boolean 标量形式返回。此控制
信号指示模块何时准备好接收新输入数据。当此值为 1
（`true`）且 `validInB` 值为 1
（`true`）时，模块在下一时间步接受输入数据。当
此值为 0（`false`）时，模块在下一时间步忽略输入数据。

发送 `true`
`validInB` 信号后，在 `readyB` 被设置为
`false` 之前可能会有一些延迟。为确保处理所有数据，
必须先等待 `readyB` 被设置为
`false`，然后再发送另一个 `true`
`validInB` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 的列数和矩阵 B 的行数** — 矩阵 *A* 的列数和矩阵 *B* 的行数 `4`（默认） | 正整数值标量

矩阵 *A* 的列数和矩阵
*B* 的行数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 B 的列数** — 矩阵 *B* 的列数 `1`（默认） | 正整数值标量

矩阵 *B* 的列数，指定为正
整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `p` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `1` |

### **遗忘因子** — 在矩阵每一行被分解后应用的遗忘因子 0.99（默认） | 实正标量

在矩阵每一行被分解后应用的遗忘因子，指定为
实正标量。随着 *A* 的每一行被无限期输入，输出会更新。

#### 程序化使用

|  |
| --- |
| **模块参数：** `forgettingFactor` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `0.99` |

### **正则化参数** — 正则化参数 0（默认） | 实非负标量

正则化参数，指定为非负标量。正则化参数的较小正值
可以改善问题的条件数并降低估计的方差。虽然有偏，但与最小二乘估计相比，
估计方差的降低通常会带来更小的均方误差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** 实非负标量 |
| **默认值：** `0` |

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认） | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为
`fixdt(1,18,14)`、`double`、
`single`、`fixdt(1,16,0)`，或用户指定的
数据类型表达式。该类型可以直接指定，或表示为数据类型
对象，例如 `Simulink.NumericType`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputType` |
| **类型：** character vector |
| **值：** `'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值：** `'fixdt(1,18,14)'` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以改进资源利用率

此模块依赖一个 partial-systolic QR 分解模块。从 23a 开始，当您
更新图时，构成 QR 分解模块中 partial-systolic 流水线的循环会展开。这种更新的内部架构会在仿真和生成的代码中移除无用操作，
因此需要更少的硬件资源。此模块在仿真时相对于先前版本中这些模块的库版本具有时钟和位真保真度。

### R2022a：支持 Tikhonov 正则化参数

Real Partial-Systolic Matrix Solve Using Q-less QR Decomposition with
Forgetting Factor 模块现在支持 Tikhonov 正则化参数。

## 描述

使用 Q-less QR 分解计算具有无限行数的实值矩阵的方程 *A*'*A**X* = *B* 中 *X* 的值

Real Partial-Systolic Matrix Solve Using Q-less QR Decomposition with
Forgetting Factor 模块使用 Q-less QR 分解求解线性方程组 *A*'*A**X* =
*B*，其中 *A* 和
*B* 是实值矩阵。*A* 是表示流式数据的无限高矩阵。

当正则化参数非零时，Real Partial-Systolic Matrix
Solve Using Q-less QR Decomposition with Forgetting Factor 在将 *A* 的行分解之前，将第一个
上三角因子 *R* 初始化为 *λ**In*，其中
*λ* 是正则化参数，且
*In* =
`eye(n)`。
