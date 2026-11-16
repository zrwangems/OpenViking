---
type: simulink-block
title: 'Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'complexpartialsystolicmatrixsolveusingqlessqrdecomposition'
documentation_source_path: '../fixedpoint/ref/complexpartialsystolicmatrixsolveusingqlessqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行向量

矩阵 *A* 的行，指定为向量。*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *m* ≥ *n*。如果 *B* 是 single 或 double，则 *A* 必须与 *B* 具有相同的数据类型。如果 *A* 是 fixed point 数据类型，则 *A* 必须是有符号的，使用二进制小数点定标，并具有与 *B* 相同的字长。fixed-point 数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **B** — 矩阵 *B* 向量

矩阵 *B*，指定为向量。*B* 是 *n*×*p* 矩阵，其中 *n* ≥ 2。如果 *A* 是 single 或 double，则 *B* 必须与 *A* 具有相同的数据类型。如果 *B* 是 fixed-point 数据类型，则 *B* 必须是有符号的，使用二进制小数点定标，并具有与 *A* 相同的字长。fixed-point 数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **validInA** — 输入 A 是否有效 `Boolean` 标量

输入 `A` 是否有效，指定为 `Boolean` 标量。此控制信号指示来自 `A(i,:)` 输入端口的数据何时有效。当此值为 1（`true`）且 `readyA` 处的值为 1（`true`）时，模块捕获 `A(i,:)` 输入端口处的值。当此值为 0（`false`）时，模块忽略输入样本。

在发送 `true` `validInA` 信号后，在 `readyA` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须等到 `readyA` 设置为 `false` 后，再发送另一个 `true` `validInA` 信号。

**数据类型：** `Boolean`

### **validInB** — 输入 B 是否有效 `Boolean` 标量

输入 `B` 是否有效，指定为 `Boolean` 标量。此控制信号指示来自 `B` 输入端口的数据何时有效。当此值为 1（`true`）且 `readyB` 处的值为 1（`true`）时，模块捕获 `B` 输入端口处的值。当此值为 0（`false`）时，模块忽略输入样本。

在发送 `true` `validInB` 信号后，在 `readyB` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须等到 `readyB` 设置为 `false` 后，再发送另一个 `true` `validInB` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 `Boolean` 标量。当此值为 1（`true`）时，模块停止当前计算并清除所有内部状态。当此值为 0（`false`）且 `validIn` 值为 1（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **X** — 矩阵 *X* 矩阵 | 向量

矩阵 *X*，以向量或矩阵形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 `Boolean` 标量形式返回。此控制信号指示输出端口 `X` 处的数据何时有效。当此值为 1（`true`）时，模块已成功计算矩阵 *X* 的一行。当此值为 0（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **readyA** — 模块是否准备好接受输入 A `Boolean` 标量

模块是否准备好接受输入 A，以 `Boolean` 标量形式返回。此控制信号指示模块何时准备好接受新输入数据。当此值为 1（`true`）且 `validInA` 值为 1（`true`）时，模块在下一个时间步接受输入数据。当此值为 0（`false`）时，模块在下一个时间步忽略输入数据。

在发送 `true` `validInA` 信号后，在 `readyA` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须等到 `readyA` 设置为 `false` 后，再发送另一个 `true` `validInA` 信号。

**数据类型：** `Boolean`

### **readyB** — 模块是否准备好接受输入 B `Boolean` 标量

模块是否准备好接受输入 B，以 `Boolean` 标量形式返回。此控制信号指示模块何时准备好接受新输入数据。当此值为 1（`true`）且 `validInB` 值为 1（`true`）时，模块在下一个时间步接受输入数据。当此值为 0（`false`）时，模块在下一个时间步忽略输入数据。

在发送 `true` `validInB` 信号后，在 `readyB` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须等到 `readyB` 设置为 `false` 后，再发送另一个 `true` `validInB` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 中的行数** — 矩阵 *A* 中的行数 `4`（默认） | 正整数值标量

矩阵 *A* 中的行数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `m` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 A 中的列数和矩阵 B 中的行数** — 矩阵 *A* 中的列数和矩阵 *B* 中的行数 `4`（默认） | 正整数值标量

矩阵 *A* 中的列数和矩阵 *B* 中的行数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 B 中的列数** — 矩阵 *B* 中的列数 `1`（默认） | 正整数值标量

矩阵 *B* 中的列数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `p` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0（默认） | 实非负标量

正则化参数，指定为非负标量。小的正正则化参数值可以改善问题的条件并减少估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的减小通常会导致更小的均方误差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** 字符向量 |
| **值：** 实非负标量 |
| **默认值：** `0` |

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认） | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为 `fixdt(1,18,14)`、`double`、`single`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。该类型可以直接指定，也可以表示为数据类型对象，如 `Simulink.NumericType`。

#### 程序化使用

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

fixed-point 数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持 fixed-point 数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：用于改进资源利用率的智能展开

此模块依赖于 partial-systolic QR decomposition 模块。从 23a 开始，更新图时，QR decomposition 模块中组成 partial-systolic 流水线的循环会展开。这种更新的内部架构去除了仿真和生成代码中的无用操作，因此需要更少的硬件资源。相对于以前版本中这些模块的库版本，此模块以时钟和位真保真度进行仿真。

### R2022a：支持 Tikhonov 正则化参数

Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition 模块现在支持 Tikhonov Regularization 参数。

### R2021a：减少 HDL 资源利用

此模块现在具有改进的算法，以减少硬件受限目标平台上的资源利用。

## 描述

使用 Q-less QR 分解计算复值矩阵方程 A' A X = B 中 X 的值

Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition 模块使用 Q-less QR 分解求解线性方程组 *A*'*A**X* = *B*，其中 *A* 和 *B* 是复值矩阵。

当 Regularization parameter 非零时，Complex Partial-Systolic Matrix Solve Using Q-less QR Decomposition 模块求解矩阵方程

[λInA]'⋅[λInA]X=(λ2In+A'A)X=B

其中 *λ* 是正则化参数，*A* 是 *m*×*n* 矩阵，并且 *In* = `eye(n)`。
