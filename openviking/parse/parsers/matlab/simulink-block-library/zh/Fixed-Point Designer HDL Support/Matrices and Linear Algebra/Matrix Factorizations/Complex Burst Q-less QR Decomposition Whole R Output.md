---
type: simulink-block
title: 'Complex Burst Q-less QR Decomposition Whole R Output'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'complexburstqlessqrdecompositionwholeroutput'
documentation_source_path: '../fixedpoint/ref/complexburstqlessqrdecompositionwholeroutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst Q-less QR Decomposition Whole R Output

## 端口

### 输入

### **A(i,:)** — 复矩阵 *A* 的行，向量

复矩阵 *A* 的行，指定为向量。
*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *n* ≥ 2。如果 *A* 是定点数据类型，
*A* 必须是有符号的并使用二进制小数点定标。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 输入端口的数据何时有效。当
此值为 1（`true`）且 `ready` 的值为
1（`true`）时，模块捕获
`A(i,:)` 输入端口处的值。当此值为 0
（`false`）时，模块忽略输入样本。

发送 `true`
`validIn` 信号后，在
`ready` 设置为 `false` 之前可能会有一些延迟。为确保所有数据
都已处理，您必须等待 `ready` 设置为
`false` 后，再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为
1（`true`）时，模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validIn` 处的值为 1（`true`）时，模块开始新的
子帧。

**数据类型：** `Boolean`
### 输出

### **R** — 经济型 QR 分解矩阵 *R*，向量

经济型 QR 分解矩阵 *R*，以向量形式返回。
*R* 是上三角矩阵。矩阵
*R* 的大小为 `min(m,n)`×`n`。
*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为 Boolean 标量。此控制
信号指示输出端口 `R(i,:)` 处的数据何时有效。当
此值为 1（`true`）时，模块已成功计算矩阵
*R*。当此值为 0（`false`）时，
输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号
指示模块何时准备好接收新的输入数据。当此值为
`1`（`true`）且 `validIn` 为
`1`（`true`）时，模块在下一时间步接受输入数据。当此值为 `0`（`false`）时，
模块在下一时间步忽略输入数据。

发送 `true`
`validIn` 信号后，在
`ready` 设置为 `false` 之前可能会有一些延迟。为确保所有数据
都已处理，您必须等待 `ready` 设置为
`false` 后，再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 中的行数** — 输入矩阵 *A* 的行数 `4`（默认）| 正整数值标量

输入矩阵 *A* 的行数，指定为正
整数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `m` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 A 中的列数** — 输入矩阵 *A* 的列数 `4`（默认）| 正整数值标量

输入矩阵 *A* 的列数，指定为正
整数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `n` |
| **类型：** 字符向量 |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **正则化参数** — 正则化参数 `0`（默认）| 实非负标量

正则化参数，指定为实非负标量。正则化参数的较小正
值可以改善问题的条件并
降低估计的方差。虽然有偏，但估计方差的降低
通常会在与最小二乘估计
比较时产生更小的均方误差。

#### 编程用法

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** 字符向量 |
| **值：** 实非负标量 |
| **默认值：** `0` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，这些选项会影响 HDL 实现和
综合逻辑。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

用于复值矩阵的 Q-less QR 分解

Complex Burst Q-less QR Decomposition Whole R Output 模块使用 QR
分解来计算 QR 分解 *A* = *Q**R* 的经济型上三角 *R* 因子，其中 *A* 是复值矩阵，而不计算
*Q*。*A*'*A**x* =
*B* 的解为 *x* =
*R*\*R*'\*b*。

当正则化参数非零时，
Complex Burst Q-less QR Decomposition Whole R Output 模块计算
[λInA] 的经济型 QR 分解的上三角因子 *R*，其中 *λ* 是正则化参数。
