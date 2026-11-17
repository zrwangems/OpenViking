---
type: simulink-block
title: 'Real Burst Matrix Solve Using Q-less QR Decomposition with Forgetting Factor'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'realburstmatrixsolveusingqlessqrdecompositionwithforgettingfactor'
documentation_source_path: '../fixedpoint/ref/realburstmatrixsolveusingqlessqrdecompositionwithforgettingfactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Burst Matrix Solve Using Q-less QR Decomposition with Forgetting Factor

## 端口

### 输入

### **A(i,:)** — 实矩阵 *A* 的行 向量

实矩阵 *A* 的行，指定为向量。
*A* 是流式数据的无限高矩阵。如果
*B* 为 single 或 double，则 *A* 必须与 *B* 具有相同的数据
类型。如果 *A* 为定点数据类型，
则 *A* 必须为有符号类型，使用二进制小数点定标，并具有与 *B* 相同的
字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **B** — 实矩阵 *B* 的行 向量

实矩阵 *B* 的行，指定为向量。
*B* 是 *n* 乘 *p* 矩阵，其中 *n* ≥ 2。如果 *A* 为 single 或 double，则 *B*
必须与 *A* 具有相同的数据类型。如果 *B* 为
定点数据类型，则 *B* 必须为有符号类型，使用二进制小数点定标，
并具有与 *A* 相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validInA** — `A(i,:)` 输入是否有效 `Boolean` 标量

`A(i,:)` 输入是否有效，指定为布尔标量。
此控制信号指示来自 `A(i,:)` 输入
端口的数据何时有效。当此值为 `1`（`true`）且
`readyA` 值为 `1`（`true`）时，
模块捕获 `A(i,:)` 输入端口的值。当此
值为 `0`（`false`）时，模块忽略输入
样本。

发送 `true`
`validInA` 信号后，在
`readyA` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待直到 `readyA` 被设置为
`false`，然后再发送另一个 `true`
`validInA` 信号。

**数据类型：** `Boolean`

### **validInB** — `B` 输入是否有效 `Boolean` 标量

`B` 输入是否有效，指定为布尔标量。此
控制信号指示来自 `B` 输入端口的数据何时
有效。当此值为 `1`（`true`）且
`readyB` 值为 `1`（`true`）时，
模块捕获 `B` 输入端口的值。当此值为
`0`（`false`）时，模块忽略输入
样本。

发送 `true`
`validInB` 信号后，在
`readyB` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待直到 `readyB` 被设置为
`false`，然后再发送另一个 `true`
`validInB` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为布尔标量。当此值为
1（`true`）时，模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validIn` 处的值为 1（`true`）时，模块开始一个新的
子帧。

**数据类型：** `Boolean`
### 输出

### **X** — 矩阵 *X* 矩阵 | 向量

矩阵 *X*，以矩阵或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为布尔标量。此控制
信号指示输出端口 `X` 处的数据何时有效。当此
值为 1（`true`）时，模块已成功计算矩阵
*X*。当此值为 0（`false`）时，输出
数据无效。

**数据类型：** `Boolean`

### **readyA** — 模块是否已准备好接受输入 `A(i,:)` `Boolean` 标量

模块是否已准备好接受输入 `A(i,:)`，以布尔
标量形式返回。此控制信号指示模块何时准备好接受新输入数据。当
此值为 `1`（`true`）且
`validInA` 为 `1`（`true`）时，
模块在下一个时间步接受输入数据。当此值为
`0`（`false`）时，模块在
下一个时间步忽略输入数据。

发送 `true`
`validInA` 信号后，在
`readyA` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待直到 `readyA` 被设置为
`false`，然后再发送另一个 `true`
`validInA` 信号。

**数据类型：** `Boolean`

### **readyB** — 模块是否已准备好接受输入 `B` `Boolean` 标量

模块是否已准备好接受输入 `B`，以布尔
标量形式返回。此控制信号指示模块何时准备好接受新输入数据。当
此值为 `1`（`true`）且
`validInB` 为 `1`（`true`）时，
模块在下一个时间步接受输入数据。当此值为
`0`（`false`）时，模块在
下一个时间步忽略输入数据。

发送 `true`
`validInB` 信号后，在
`readyB` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待直到 `readyB` 被设置为
`false`，然后再发送另一个 `true`
`validInB` 信号。

**数据类型：** `Boolean`

## 参数

### **Number of columns in matrix A and rows in matrix B** — 矩阵 *A* 的列数和矩阵 *B* 的行数 `4`（默认值）| 正整数值标量

矩阵 *A* 的列数和矩阵 *B* 的行数，
指定为正整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`n` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`4` |

### **Number of columns in matrix B** — 矩阵 *B* 的列数 `1`（默认值）| 正整数值标量

矩阵 *B* 的列数，指定为正
整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`p` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`1` |

### **Forgetting factor** — 对矩阵的每一行进行分解后应用的遗忘因子 `0.99`（默认值）| 实正标量

对矩阵的每一行进行分解后应用的遗忘因子，指定为
实正标量。当 *A* 的每一行被无限期输入时，输出会随之更新。

#### 编程使用

|  |
| --- |
| **模块参数**：`forgetting_factor` |
| **类型**：character vector |
| **值**：real positive scalar |
| **默认值**：`0` |

### **Regularization parameter** — 正则化参数 0（默认值）| 实非负标量

正则化参数，指定为非负标量。较小的正
正则化参数值可以改善问题的条件数并减少
估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的减少通常
会带来更小的均方误差。

#### 编程使用

|  |
| --- |
| **模块参数**：`regularizationParameter` |
| **类型**：character vector |
| **值**：real nonnegative scalar |
| **默认值**：`0` |

### **Output datatype** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认值）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为
`fixdt(1,18,14)`、`double`、
`single`、`fixdt(1,16,0)`，或用户指定的
数据类型表达式。该类型可以直接指定，也可以表示为数据类型
对象，例如 `Simulink.NumericType`。

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

HDL Coder™ 提供影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

使用异步无 Q QR 分解计算具有无限行数的实值矩阵方程 A ' A X = B 中 X 的值

使用无 Q QR 分解与遗忘因子的实突发矩阵求解
Factor 模块使用异步无 Q QR 分解求解线性方程组 *A*'*A**X* =
*B*，其中 *A* 和
*B* 为实值矩阵。*A* 是表示流式数据的无限高
矩阵。

当 Regularization parameter 非零时，
使用无 Q QR 分解与遗忘因子的实突发矩阵求解 Factor
模块求解矩阵方程

[λInA]'⋅[λInA]X=(λ2In+A'A)X=B

其中 *λ* 是正则化参数，
*A* 是 *m* 乘 *n* 矩阵，且
*In* =
`eye(n)`。

此模块异步运行。前向和后向代入以及无 Q QR
分解使用最新的 *R* 和 *B*
矩阵独立运行。
