---
type: simulink-block
title: 'Real Partial-Systolic Matrix Solve Using QR Decomposition'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Linear System Solvers / Solve AX = B'
documentation_page: 'realpartialsystolicmatrixsolveusingqrdecomposition'
documentation_source_path: 'ref/realpartialsystolicmatrixsolveusingqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Partial-Systolic Matrix Solve Using QR Decomposition

## 端口

### 输入

### **A(i,:)** — 实矩阵 *A* 的行向量

实矩阵 *A* 的行，指定为向量。
*A* 是一个 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *m* ≥ *n*。如果 *B* 为 single 或 double，则 *A*
必须与 *B* 具有相同的数据类型。如果 *A* 为
fixed-point 数据类型，则 *A* 必须为有符号、使用 binary-point scaling，
并且与 *B* 具有相同的字长。fixed-point 数据类型不支持
slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`

### **B(i,:)** — 实矩阵 *B* 的行向量

实矩阵 *B* 的行，指定为向量。
*B* 是一个 *m*×*p* 矩阵，其中 *m* ≥ 2。如果 *A* 为 single 或 double，则 *B*
必须与 *A* 具有相同的数据类型。如果 *B* 为
fixed-point 数据类型，则 *B* 必须为有符号、使用 binary-point scaling，
并且与 *A* 具有相同的字长。fixed-point 数据类型不支持
slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号
指示来自 `A(i,:)` 和
`B(i,:)` 输入端口的数据何时有效。当该值为 1
(`true`) 且 `ready` 处的值为 1
(`true`) 时，模块捕获
`A(i,:)` 和 `B(i,:)` 输入端口上的值。当该
值为 0 (`false`) 时，模块忽略输入样本。

发送 `true`
`validIn` 信号后，在
`ready` 被设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，
必须先等待 `ready` 被设置为
`false`，然后再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当该值
为 1 (`true`) 时，模块停止当前计算并清除所有
内部状态。当该值为 0 (`false`) 且
`validIn` 值为 1 (`true`) 时，模块开始
新的子帧。

**数据类型：** `Boolean`

### 输出

### **X(i,:)** — 矩阵 *X* 的行 标量 | 向量

矩阵 *X* 的行，以标量或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制
信号指示输出端口 `X(i,:)` 处的数据何时
有效。当该值为 1 (`true`) 时，模块已成功
计算矩阵 *X* 的一行。当该值为 0
(`false`) 时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号
指示模块何时准备好接收新输入数据。当该值为 1
(`true`) 且 `validIn` 值为 1
(`true`) 时，模块在下一个时间步接受输入数据。当
该值为 0 (`false`) 时，模块在下一个时间步忽略输入数据。

发送 `true`
`validIn` 信号后，在
`ready` 被设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，
必须先等待 `ready` 被设置为
`false`，然后再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 和 B 中的行数** — 矩阵 *A* 和 *B* 中的行数 `4` (默认) | 正整数标量

输入矩阵 *A* 和 *B* 的行数，
指定为正整数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `m` |
| **类型：** character vector |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **矩阵 A 中的列数** — 矩阵 *A* 中的列数 `4` (默认) | 正整数标量

输入矩阵 *A* 的列数，指定为正
整数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **矩阵 B 中的列数** — 矩阵 *B* 中的列数 `1` (默认) | 正整数标量

输入矩阵 *B* 的列数，指定为正
整数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `p` |
| **类型：** character vector |
| **值：** 正整数标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0 (默认) | 实非负标量

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

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)` (默认) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为
`fixdt(1,18,14)`、`double`、
`single`、`fixdt(1,16,0)`，或用户指定的
数据类型表达式。该类型可以直接指定，也可以表示为数据类型
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

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

fixed-point 数据类型不支持 slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持 fixed-point 数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：用于改进资源利用率的智能展开

此模块依赖于 partial-systolic QR decomposition 模块。自 23a 起，当
更新图时，QR decomposition 模块中构成 partial-systolic 流水线的循环
会被展开。此更新的内部架构会移除仿真和生成代码中的
死操作，从而需要更少的硬件资源。与之前版本中这些模块的库版本相比，
此模块以时钟和位真保真度进行仿真。

## 描述

计算实值矩阵方程 A x = B 中 x 的值，使用 QR 分解

Real Partial-Systolic Matrix Solve Using QR Decomposition 模块使用 QR 分解求解
线性方程组 *A**x* = *B*，其中 *A* 和 *B*
为实值矩阵。要计算 *x* =
*A*-1，请将 *B* 设置为单位矩阵。

当正则化参数非零时，
Real Partial-Systolic Matrix Solve Using QR Decomposition 模块计算
实值 [λInA]X=[0n,pB] 的矩阵解，其中 *λ* 是正则化参数，
*A* 是 *m*×*n* 矩阵，
*p* 是 *B* 中的列数，
*In* =
`eye(n)`，且
*0n,p* =
`zeros(n,p)`。
