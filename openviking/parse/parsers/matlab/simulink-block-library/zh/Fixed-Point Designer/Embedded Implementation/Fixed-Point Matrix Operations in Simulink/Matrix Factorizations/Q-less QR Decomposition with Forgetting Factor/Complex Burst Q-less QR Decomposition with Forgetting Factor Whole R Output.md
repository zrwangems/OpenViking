---
type: simulink-block
title: 'Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R Output'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Matrix Factorizations / Q-less QR Decomposition with Forgetting Factor'
documentation_page: 'complexburstqlessqrdecompositionwithforgettingfactorwholeroutput'
documentation_source_path: 'ref/complexburstqlessqrdecompositionwithforgettingfactorwholeroutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R Output

## 端口

### 输入

### **A(i,:)** — 复数矩阵 *A* 的行向量

复数矩阵 *A* 的行，指定为向量。
*A* 是流式数据的无限高矩阵。如果 *A* 使用 fixed-point 数据类型，则 *A* 必须是有符号的并使用 binary-point scaling。fixed-point 数据类型不支持 slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 输入端口的数据何时有效。当此值为 1 (`true`) 且 `ready` 的值为 1 (`true`) 时，模块捕获 `A(i,:)` 输入端口处的值。当此值为 0 (`false`) 时，模块忽略输入样本。

在发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，你必须等到 `ready` 设置为 `false` 后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1 (`true`) 时，模块停止当前计算并清除所有内部状态。当此值为 0 (`false`) 且 `validIn` 处的值为 1 (`true`) 时，模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **R** — 经济型 QR 分解矩阵 *R* 向量

经济型 QR 分解矩阵 *R*，以向量形式返回。*R* 是上三角矩阵。矩阵 *R* 的大小为 `n`-by-`n`。*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为 Boolean 标量。此控制信号指示输出端口 `R(i,:)` 处的数据何时有效。当此值为 1 (`true`) 时，模块已成功计算矩阵 *R*。当此值为 0 (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 `1` (`true`) 且 `validIn` 为 `1` (`true`) 时，模块在下一个时间步接受输入数据。当此值为 `0` (`false`) 时，模块在下一个时间步忽略输入数据。

在发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，你必须等到 `ready` 设置为 `false` 后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 的列数** — 输入矩阵 *A* 的列数 `4`（默认） | 正整数标量

输入矩阵 *A* 的列数，指定为正整数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **遗忘因子** — 矩阵每一行被分解后应用的遗忘因子 `0.99`（默认） | 实正标量

在矩阵每一行被分解后应用的遗忘因子，指定为实正标量。随着 *A* 的每一行无限期输入，输出会更新。

#### 程序化使用

|  |
| --- |
| **模块参数：** `forgetting_factor` |
| **类型：** character vector |
| **值：** 实正标量 |
| **默认值：** `0` |

### **正则化参数** — 正则化参数 `0`（默认） | 实非负标量

正则化参数，指定为实非负标量。正则化参数的较小正值可以改善问题的条件数并降低估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的降低通常会产生更小的均方误差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** 实非负标量 |
| **默认值：** `0` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

fixed-point 数据类型不支持 slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持 fixed-point 数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真 fixed-point 系统。

## 版本历史

**在 R2022b 中引入**

## 描述

用于具有无限行数的复值矩阵的无 Q QR 分解

Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R
Output 模块使用 QR 分解来计算 QR 分解 *A* = *Q**R* 的经济型上三角 *R* 因子，而不计算 *Q*。*A* 是表示流式数据的无限高复值矩阵。

当正则化参数非零时，Complex Burst Q-less QR
Decomposition with Forgetting Factor Whole R Output 模块在分解 *A* 的行之前，将第一个上三角因子 *R* 初始化为 *λ**I**n*，其中 *λ* 是正则化参数，且 *I**n* =
eye(*n*)
