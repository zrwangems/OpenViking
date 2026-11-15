---
type: simulink-block
title: 'Real Burst Q-less QR Decomposition Whole R Output'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Matrix Factorizations / Q-less QR Decomposition'
documentation_page: 'realburstqlessqrdecompositionwholeroutput'
documentation_source_path: 'ref/realburstqlessqrdecompositionwholeroutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Burst Q-less QR Decomposition Whole R Output

## 端口

### 输入

### **A(i,:)** — 实矩阵 *A* 的行 向量

实矩阵 *A* 的行，指定为向量。*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *n* ≥ 2。如果 *A* 是定点数据类型，则 *A* 必须为有符号并使用二进制小数点定标。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 输入端口的数据何时有效。当此值为 1 (`true`) 且 `ready` 的值为 1 (`true`) 时，模块捕获 `A(i,:)` 输入端口处的值。当此值为 0 (`false`) 时，模块忽略输入采样。

发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能有一些延迟。为确保处理所有数据，必须先等到 `ready` 设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1 (`true`) 时，模块停止当前计算并清除所有内部状态。当此值为 0 (`false`) 且 `validIn` 处的值为 1 (`true`) 时，模块开始新的子帧。

**数据类型：** `Boolean`

### 输出

### **R** — 经济型 QR 分解矩阵 *R* 向量

经济型 QR 分解矩阵 *R*，以向量形式返回。*R* 是上三角矩阵。矩阵 *R* 的大小为 `min(m,n)`×`n`。*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为 Boolean 标量。此控制信号指示输出端口 `R(i,:)` 处的数据何时有效。当此值为 1 (`true`) 时，模块已成功计算矩阵 *R*。当此值为 0 (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 `1` (`true`) 且 `validIn` 为 `1` (`true`) 时，模块在下一时间步接受输入数据。当此值为 `0` (`false`) 时，模块在下一时间步忽略输入数据。

发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能有一些延迟。为确保处理所有数据，必须先等到 `ready` 设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 的行数** — 输入矩阵 *A* 的行数 `4` (默认) | 正整数值标量

输入矩阵 *A* 的行数，指定为正整数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `m` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 A 的列数** — 输入矩阵 *A* 的列数 `4` (默认) | 正整数值标量

输入矩阵 *A* 的列数，指定为正整数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **正则化参数** — 正则化参数 `0` (默认) | 实数非负标量

正则化参数，指定为实数非负标量。正则化参数的较小正值可以改善问题的条件并减小估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的减小通常会导致更小的均方误差。

#### 编程用法

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** 实数非负标量 |
| **默认值：** `0` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

用于实值矩阵的无 Q QR 分解

Real Burst Q-less QR Decomposition Whole R Output 模块使用 QR 分解来计算 QR 分解 *A* = *Q**R* 的经济型上三角 *R* 因子，其中 *A* 是实值矩阵，而不计算 *Q*。*A*'*A**x* = *B* 的解为 *x* = *R*\*R*'\*b*。

当正则化参数非零时，Real Burst Q-less QR Decomposition Whole R Output 模块计算 [λInA] 的经济型 QR 分解的上三角因子 *R*，其中 *λ* 是正则化参数。
