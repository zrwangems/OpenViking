---
type: simulink-block
title: 'Complex Burst QR Decomposition'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Matrix Factorizations / QR Decomposition'
documentation_page: 'complexburstqrdecomposition'
documentation_source_path: 'ref/complexburstqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst QR Decomposition

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行 向量

矩阵 *A* 的行，指定为向量。*A*
是一个 *m* 乘 *n* 矩阵，其中 *m* ≥ 2 且 *n* ≥ 2。如果 *B* 是 single 或 double，则 *A*
必须与 *B* 具有相同的数据类型。如果 *A* 是
fixed-point 数据类型，则 *A* 必须为有符号、使用 binary-point 缩放，
并且与 *B* 具有相同的字长。fixed-point 数据类型不支持
slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **B(i,:)** — 矩阵 *B* 的行 向量

矩阵 *B* 的行，指定为向量。*B*
是一个 *m* 乘 *p* 矩阵，其中 *m* ≥ 2。如果 *A* 是 single 或 double，则 *B*
必须与 *A* 具有相同的数据类型。如果 *B* 是
fixed-point 数据类型，则 *B* 必须为有符号、使用 binary-point 缩放，
并且与 *A* 具有相同的字长。fixed-point 数据类型不支持
slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号
指示来自 `A(i,:)` 和
`B(i,:)` 输入端口的數據是否有效。当此值为 1
（`true`）且 `ready` 处的值为 1
（`true`）时，模块捕获
`A(i,:)` 和 `B(i,:)` 输入端口上的值。当此
值为 0（`false`）时，模块忽略输入样本。

发送 `true`
`validIn` 信号后，在
`ready` 设置为 `false` 之前可能会有一些延迟。为确保所有数据均
得到处理，必须等到 `ready` 设置为
`false` 后，再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值
为 1（`true`）时，模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validIn` 值为 1（`true`）时，模块开始
新的子帧。

**数据类型：** `Boolean`
### 输出

### **R(i,:)** — 矩阵 *R* 的行 标量 | 向量

经济大小 QR 分解矩阵 *R* 的行，返回为
标量或向量。*R* 是上三角矩阵。矩阵 *R* 的大小
为 min(*m*,*n*) 乘 *n*。*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **C(i,:)** — 矩阵 *C*=*Q*'*B* 的行 标量 | 向量

经济大小 QR 分解矩阵 *C*=*Q*'*B* 的行，返回为标量或向量。*C* 与
*R* 具有相同的行数。*C* 与 *B* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，返回为 Boolean 标量。此控制
信号指示输出端口 `R(i,:)` 和
`C(i,:)` 处的数据何时有效。当此值为 1
（`true`）时，模块已成功计算
*R* 和 *C* 矩阵。当此值为 0
（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，返回为 Boolean 标量。此控制信号
指示模块何时准备好接收新输入数据。当此值为 1
（`true`）且 `validIn` 值为 1
（`true`）时，模块在下一时间步接受输入数据。当
此值为 0（`false`）时，模块在下一
时间步忽略输入数据。

发送 `true`
`validIn` 信号后，在
`ready` 设置为 `false` 之前可能会有一些延迟。为确保所有数据均
得到处理，必须等到 `ready` 设置为
`false` 后，再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 和 B 的行数** — 矩阵 A 和 B 的行数 `4`（默认） | 正整数值标量

矩阵 *A* 和 *B* 的行数，
指定为正整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `m` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 A 的列数** — 矩阵 A 的列数 `4`（默认） | 正整数值标量

输入矩阵 *A* 的列数，指定为正
整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 B 的列数** — 矩阵 B 的列数 `1`（默认） | 正整数值标量

输入矩阵 *B* 的列数，指定为正
整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `p` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0（默认） | 实非负标量

正则化参数，指定为非负标量。正则化参数的较小正值
可以改善问题的条件数并降低
估计的方差。虽然有偏，但与最小二乘估计相比，
估计方差的降低通常会得到更小的均方误差。

#### 编程使用

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** 实非负标量 |
| **默认值：** `0` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

fixed-point 数据类型不支持 slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持 fixed-point 数据类型。

## 版本历史

**在 R2019b 中引入**

### R2022a：支持 Tikhonov 正则化参数

Complex Burst QR Decomposition 模块现在支持 Tikhonov 正则化参数。

### R2021a：降低 HDL 资源利用率

此模块现在具有改进的算法，以减少
硬件受限目标平台上的资源利用率。

## 描述

复值矩阵的 QR 分解

Complex Burst QR Decomposition 模块使用 QR 分解来计算
*R* 和 *C* = *Q*'*B*，其中 *Q**R* = *A*，并且 *A* 和 *B* 是复值
矩阵。*A**x* = *B* 的最小二乘解为 *x* = *R*\*C*。*R* 是上三角矩阵，*Q*
是正交矩阵。要计算 *C* = *Q'*，请将 *B* 设置为单位矩阵。

当正则化参数非零时，
Complex Burst QR Decomposition 模块将 [λInA] 原地变换为 R=Q'[λInA]，并将 [0n,pB] 原地变换为 C=Q'[0n,pB]，其中 *λ* 是正则化参数，QR 是
[λInA] 的经济大小 QR 分解，*A* 是 *m* 乘 *n*
矩阵，*p* 是 *B* 的列数，
*In* =
`eye(n)`，并且
*0n,p* =
`zeros(n,p)`。
