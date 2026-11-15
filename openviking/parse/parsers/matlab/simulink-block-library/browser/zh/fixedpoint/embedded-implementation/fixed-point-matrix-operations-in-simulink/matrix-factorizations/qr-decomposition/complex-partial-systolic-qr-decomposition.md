---
type: simulink-block
title: 'Complex Partial-Systolic QR Decomposition'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Matrix Factorizations / QR Decomposition'
documentation_page: 'complexpartialsystolicqrdecomposition'
documentation_source_path: 'ref/complexpartialsystolicqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Partial-Systolic QR Decomposition

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行向量

矩阵 *A* 的行，指定为向量。*A* 是 *m*-by-*n* 矩阵，其中 *m* ≥ 2 且 *n* ≥ 2。如果 *B* 是 single 或 double，则 *A* 必须与 *B* 具有相同的数据类型。如果 *A* 是 fixed-point 数据类型，则 *A* 必须是有符号的、使用 binary-point 缩放，并且与 *B* 具有相同的字长。fixed-point 数据类型不支持 slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **B(i,:)** — 矩阵 *B* 的行向量

矩阵 *B* 的行，指定为向量。*B* 是 *m*-by-*p* 矩阵，其中 *m* ≥ 2。如果 *A* 是 single 或 double，则 *B* 必须与 *A* 具有相同的数据类型。如果 *B* 是 fixed-point 数据类型，则 *B* 必须是有符号的、使用 binary-point 缩放，并且与 *A* 具有相同的字长。fixed-point 数据类型不支持 slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 和 `B(i,:)` 输入端口的数据何时有效。当此值为 1（`true`）且 `ready` 处的值为 1（`true`）时，模块捕获 `A(i,:)` 和 `B(i,:)` 输入端口上的值。当此值为 0（`false`）时，模块忽略输入样本。

发送 `true` `validIn` 信号后，在 `ready` 被设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，您必须等待直到 `ready` 被设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1（`true`）时，模块停止当前计算并清除所有内部状态。当此值为 0（`false`）且 `validIn` 值为 1（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **R** — 矩阵 *R*

经济型 QR 分解矩阵 *R*，以矩阵形式返回。*R* 是上三角矩阵。矩阵 *R* 的大小为 *n*-by-*n*。*R* 的数据类型与 *A* 相同。

**数据类型：** `single` | `double` | `fixed point`

### **C** — 矩阵 *C*=*Q*'*B*

经济型 QR 分解矩阵 *C*=*Q*'*B*，以矩阵或向量形式返回。*C* 的行数与 *R* 相同。*C* 的数据类型与 *B* 相同。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制信号指示输出端口 `R` 和 `C` 上的数据何时有效。当此值为 1（`true`）时，模块已成功计算 *R* 和 *C* 矩阵。当此值为 0（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 1（`true`）且 `validIn` 值为 1（`true`）时，模块在下一个时间步接受输入数据。当此值为 0（`false`）时，模块在下一个时间步忽略输入数据。

发送 `true` `validIn` 信号后，在 `ready` 被设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，您必须等待直到 `ready` 被设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **Number of rows in matrices A and B** — 输入矩阵 A 和 B 的行数 `4`（默认）| 正整数值标量

输入矩阵 *A* 和 *B* 的行数，指定为正整数值标量。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `m` |
| **类型：** character vector |
| **值：** positive integer-valued scalar |
| **默认值：** `4` |

### **Number of columns in matrix A** — 输入矩阵 A 的列数 `4`（默认）| 正整数值标量

输入矩阵 *A* 的列数，指定为正整数值标量。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** positive integer-valued scalar |
| **默认值：** `4` |

### **Number of columns in matrix B** — 输入矩阵 B 的列数 `1`（默认）| 正整数值标量

输入矩阵 *B* 的列数，指定为正整数值标量。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `p` |
| **类型：** character vector |
| **值：** positive integer-valued scalar |
| **默认值：** `1` |

### **Regularization parameter** — 正则化参数 0（默认）| 非负标量

正则化参数，指定为非负标量。正则化参数的较小正值可以改善问题的条件并减少估计的方差。虽然有偏，但与最小二乘估计相比，估计的方差减小通常会导致更小的均方误差。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** positive integer-valued scalar |
| **默认值：** `0` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

fixed-point 数据类型不支持 slope-bias 表示。

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持 fixed-point 数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以提高资源利用率

当您更新图时，构成 partial-systolic 流水线的循环会被展开。此更新的内部架构去除了仿真和生成代码中的死操作，从而显著减少了所需的硬件资源数量。此模块在时钟和 bit-true 保真度方面与先前版本中这些模块的库版本进行仿真。

| 资源 | R2022b 中的使用量 | R2023a 中的使用量 |
| --- | --- | --- |
| LUT | 177813 | 108464 |
| LUTRAM | 6620 | 5000 |
| Flip Flop | 113857 | 68404 |

此示例数据是通过在 Xilinx Zynq-7 ZC706 评估板（-2 speed grade）上综合该模块生成的。

综合使用了以下参数。

- 模块参数：

  - `m = 10`
  - `n = 10`
  - `p = 1`
  - 矩阵 *A* 维度：10-by-10
  - 矩阵 *B* 维度：10-by-1
- 输入数据类型：`sfix18_En12`

### R2021a：减少 HDL 资源使用量

此模块现在具有改进的算法，可在硬件受限的目标平台上减少资源使用量。

## 描述

复值矩阵的 QR 分解

Complex Partial-Systolic QR Decomposition 模块使用 QR 分解来计算 *R* 和 *C* = *Q*'*B*，其中 *Q**R* = *A*，且 *A* 和 *B* 是复值矩阵。*A**x* = *B* 的最小二乘解为 *x* = *R*\*C*。*R* 是上三角矩阵，*Q* 是正交矩阵。要计算 *C* = *Q'*，将 *B* 设置为单位矩阵。

当 Regularization parameter 非零时，Complex Partial-Systolic QR Decomposition 模块将 [λInA] 原地变换为 R=Q'[λInA]，并将 [0n,pB] 原地变换为 C=Q'[0n,pB]，其中 *λ* 是正则化参数，QR 是 [λInA] 的经济型 QR 分解，*A* 是 *m*-by-*n* 矩阵，*p* 是 *B* 中的列数，*In* = `eye(n)`，*0n,p* = `zeros(n,p)`。
