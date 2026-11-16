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

### **A(i,:)** — 矩阵 *A* 的行，向量

矩阵 *A* 的行，指定为向量。*A* 是流式数据的无限高矩阵。如果 *B* 是 single 或 double，则 *A* 必须与 *B* 具有相同的数据类型。如果 *A* 是定点数据类型，则 *A* 必须为有符号，使用二进制点缩放，并且与 *B* 具有相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **B** — 矩阵 *B*，矩阵 | 向量

矩阵 *B*，指定为向量或矩阵。*B* 是 *n*×*p* 矩阵，其中 *n* ≥ 2。如果 *A* 是 single 或 double，则 *B* 必须与 *A* 具有相同的数据类型。如果 *B* 是定点数据类型，则 *B* 必须为有符号，使用二进制点缩放，并且与 *A* 具有相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validInA** — A 输入是否有效 `Boolean` 标量

`A(i, ;)` 输入是否有效，指定为 `Boolean` 标量。此控制信号指示来自 `A(i,:)` 输入端口的数据何时有效。当此值为 `1` (`true`) 且 `readyA` 值为 `1` (`true`) 时，模块在 `A(i,:)` 输入端口捕获值。当此值为 `0` (`false`) 时，模块忽略输入样本。

在发送 `true` `validInA` 信号后，在 `readyA` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `readyA` 设置为 `false`，然后再发送另一个 `true` `validInA` 信号。

**数据类型：** `Boolean`

### **validInB** — 输入 B 是否有效 `Boolean` 标量

输入 `B` 是否有效，指定为 `Boolean` 标量。此控制信号指示来自 `B` 输入端口的数据何时有效。当此值为 `1` (`true`) 且 `readyB` 值为 `1` (`true`) 时，模块在 `B` 输入端口捕获值。当此值为 `0` (`false`) 时，模块忽略输入样本。

在发送 `true` `validInB` 信号后，在 `readyB` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `readyB` 设置为 `false`，然后再发送另一个 `true` `validInB` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 `Boolean` 标量。当此值为 1 (`true`) 时，模块停止当前计算并清除所有内部状态。当此值为 0 (`false`) 且 `validInA` 和 `validInB` 值为 1 (`true`) 时，模块开始新的子帧。

**数据类型：** `Boolean`

### 输出

### **X** — 矩阵 *X*，矩阵 | 向量

矩阵 *X*，以矩阵或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 `Boolean` 标量形式返回。此控制信号指示输出端口 `X` 处的数据何时有效。当此值为 `1` (`true`) 时，模块已成功计算 *X* 的一行。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

### **readyA** — 模块是否准备好接受输入 A `Boolean` 标量

模块是否准备好接受输入 A，以 `Boolean` 标量形式返回。此控制信号指示模块何时准备好接受新输入数据。当此值为 1 (`true`) 且 `validInA` 值为 1 (`true`) 时，模块在下一时间步接受输入数据。当此值为 0 (`false`) 时，模块在下一时间步忽略输入数据。

在发送 `true` `validInA` 信号后，在 `readyA` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `readyA` 设置为 `false`，然后再发送另一个 `true` `validInA` 信号。

**数据类型：** `Boolean`

### **readyB** — 模块是否准备好接受输入 B `Boolean` 标量

模块是否准备好接受输入 B，以 `Boolean` 标量形式返回。此控制信号指示模块何时准备好接受新输入数据。当此值为 1 (`true`) 且 `validInB` 值为 1 (`true`) 时，模块在下一时间步接受输入数据。当此值为 0 (`false`) 时，模块在下一时间步忽略输入数据。

在发送 `true` `validInB` 信号后，在 `readyB` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `readyB` 设置为 `false`，然后再发送另一个 `true` `validInB` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 *A* 中的列数和矩阵 *B* 中的行数** — 矩阵 *A* 的列数和矩阵 *B* 的行数 `4`（默认）| 正整数值标量

矩阵 *A* 的列数和矩阵 *B* 的行数，指定为正整数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `n` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 *B* 中的列数** — 矩阵 *B* 的列数 `1`（默认）| 正整数值标量

矩阵 *B* 的列数，指定为正整数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `p` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `1` |

### **遗忘因子** — 在矩阵每一行被分解后应用的遗忘因子 0.99（默认）| 正实数标量

在矩阵每一行被分解后应用的遗忘因子，指定为正实数标量。随着 *A* 的每一行被无限输入，输出会更新。

#### 编程用法

|  |
| --- |
| **模块参数：** `forgettingFactor` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `0.99` |

### **正则化参数** — 正则化参数 0（默认）| 非负实数标量

正则化参数，指定为非负标量。正则化参数的较小正值可以改善问题的条件并减少估计的方差。尽管有偏，但与最小二乘估计相比，估计方差的减小通常会产生更小的均方误差。

#### 编程用法

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认值：** `0` |

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为 `fixdt(1,18,14)`、`double`、`single`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。该类型可直接指定，也可表示为数据类型对象，例如 `Simulink.NumericType`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputType` |
| **类型：** 字符向量 |
| **值：** `'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值：** `'fixdt(1,18,14)'` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参见 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以改进资源利用率

此模块依赖于一个部分脉动 QR 分解模块。自 23a 起，当您更新图时，QR 分解模块中构成部分脉动流水线的循环会被展开。此更新的内部架构移除了仿真和生成代码中的无用操作，因此需要更少的硬件资源。此模块在仿真时相对于以前版本中这些模块的库版本，具有时钟精确和位精确保真度。

### R2022a：支持 Tikhonov 正则化参数

Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor 模块现在支持 Tikhonov 正则化参数。

### R2021a：减少 HDL 资源使用

此模块现在具有改进的算法，可减少硬件受限目标平台上的资源使用。

## 描述

对于具有无限行数的复数值矩阵，使用 Q-less QR 分解计算方程 A ' A X = B 中 X 的值

Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor 模块使用 Q-less QR 分解求解线性方程组 *A*'*A**X* = *B*，其中 *A* 和 *B* 是复数值矩阵。*A* 是表示流式数据的无限高矩阵。

当正则化参数非零时，Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition with Forgetting Factor 在分解 *A* 的行之前，将第一个上三角因子 *R* 初始化为 *λ**In*，其中 *λ* 是正则化参数，*In* = `eye(n)`。
