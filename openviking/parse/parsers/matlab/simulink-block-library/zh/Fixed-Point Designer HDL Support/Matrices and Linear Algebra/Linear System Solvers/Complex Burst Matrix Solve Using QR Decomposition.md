---
type: simulink-block
title: 'Complex Burst Matrix Solve Using QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'complexburstmatrixsolveusingqrdecomposition'
documentation_source_path: '../fixedpoint/ref/complexburstmatrixsolveusingqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst Matrix Solve Using QR Decomposition

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行向量

矩阵 *A* 的行，指定为向量。*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *m* ≥ *n*。如果 *B* 是 single 或 double，*A* 必须与 *B* 具有相同的数据类型。如果 *A* 是 fixed point 数据类型，*A* 必须是有符号的、使用 binary-point scaling，并且具有与 *B* 相同的字长。fixed-point 数据类型不支持 Slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **B(i,:)** — 矩阵 *B* 的行向量

矩阵 *B* 的行，指定为向量。*B* 是 *m*×*p* 矩阵，其中 *m* ≥ 2。如果 *A* 是 single 或 double，*B* 必须与 *A* 具有相同的数据类型。如果 *B* 是 fixed-point 数据类型，*B* 必须是有符号的、使用 binary-point scaling，并且具有与 *A* 相同的字长。fixed-point 数据类型不支持 Slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 和 `B(i,:)` 输入端口的数据何时有效。当此值为 1（`true`）且 `ready` 处的值为 1（`true`）时，模块捕获 `A(i,:)` 和 `B(i,:)` 输入端口处的值。当此值为 0（`false`）时，模块忽略输入采样。

发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `ready` 设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1（`true`）时，模块停止当前计算并清除所有内部状态。当此值为 0（`false`）且 `validIn` 值为 1（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`

### 输出

### **X(i,:)** — 矩阵 *X* 的行 标量 | 向量

矩阵 *X* 的行，以标量或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制信号指示输出端口 `X(i,:)` 处的数据何时有效。当此值为 1（`true`）时，模块已成功计算矩阵 *X* 的一行。当此值为 0（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 1（`true`）且 `validIn` 值为 1（`true`）时，模块在下一时间步接受输入数据。当此值为 0（`false`）时，模块在下一时间步忽略输入数据。

发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `ready` 设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 和 B 中的行数** — 矩阵 *A* 和 *B* 中的行数 `4`（默认值） | 正整数值标量

输入矩阵 *A* 和 *B* 中的行数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `m` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 A 中的列数** — 矩阵 *A* 中的列数 `4`（默认值） | 正整数值标量

输入矩阵 *A* 中的列数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 B 中的列数** — 矩阵 *B* 中的列数 `1`（默认值） | 正整数值标量

输入矩阵 *B* 中的列数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `p` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0（默认值） | 非负标量

正则化参数，指定为非负标量。正则化参数的较小正值可以改善问题的条件并降低估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的降低通常会产生更小的均方误差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `0` |

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认值） | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为 `fixdt(1,18,14)`、`double`、`single`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

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

fixed-point 数据类型不支持 Slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2019b 中引入**

### R2022a：支持 Tikhonov 正则化参数

Complex Burst Matrix Solve Using QR Decomposition 模块现在支持 Tikhonov 正则化参数。

### R2021a：降低 HDL 资源利用率

此模块现在具有改进的算法，可降低硬件受限目标平台上的资源利用率。

## 描述

使用 QR 分解计算复值矩阵方程 A x = B 中 x 的值

Complex Burst Matrix Solve Using QR Decomposition 模块使用 QR 分解求解线性方程组 *A**x* = *B*，其中 *A* 和 *B* 是复值矩阵。要计算 *x* = *A*-1，将 *B* 设为单位矩阵。

当正则化参数非零时，Complex Burst Matrix Solve Using QR Decomposition 模块计算复值 [λInA]X=[0n,pB] 的矩阵解，其中 *λ* 是正则化参数，*A* 是 *m*×*n* 矩阵，*p* 是 *B* 中的列数，*In* = `eye(n)`，且 *0n,p* = `zeros(n,p)`。
