---
type: simulink-block
title: 'Real Partial-Systolic QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'realpartialsystolicqrdecomposition'
documentation_source_path: '../fixedpoint/ref/realpartialsystolicqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Partial-Systolic QR Decomposition

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行向量

实矩阵 *A* 的行，指定为向量。
*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *n* ≥ 2。如果 *B* 是 single 或 double，则 *A*
必须与 *B* 具有相同的数据类型。如果 *A* 是
定点数据类型，则 *A* 必须为有符号，使用二进制小数点定标，
并具有与 *B* 相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **B(i,:)** — 矩阵 *B* 的行向量

实矩阵 *B* 的行，指定为向量。
*B* 是 *m*×*p* 矩阵，其中 *m* ≥ 2。如果 *A* 是 single 或 double，则 *B*
必须与 *A* 具有相同的数据类型。如果 *B* 是
定点数据类型，则 *B* 必须为有符号，使用二进制小数点定标，
并具有与 *A* 相同的字长。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号
指示来自 `A(i,:)` 和
`B(i,:)` 输入端口的數據何时有效。当此值为 1
（`true`）且 `ready` 处的值为 1
（`true`）时，模块捕获
`A(i,:)` 和 `B(i,:)` 输入端口上的值。当此
值为 0（`false`）时，模块忽略输入样本。

发送 `true`
`validIn` 信号后，在
`ready` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据都
得到处理，必须等到 `ready` 被设置为
`false` 后，再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为
1（`true`）时，模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validIn` 值为 1（`true`）时，模块开始
新的子帧。

**数据类型：** `Boolean`

### 输出

### **R** — 矩阵 *R* 标量 | 向量

经济型 QR 分解矩阵 *R*，以标量或
向量形式返回。*R* 是上三角矩阵。矩阵
*R* 的大小为 *n*×*n*。
*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **C** — 矩阵 *C = Q'B* 标量 | 向量

经济型 QR 分解矩阵 *C*=*Q*'*B*，以标量或向量形式返回。*C* 具有与
*R* 相同的行数。*C* 与
*B* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制信号
指示输出端口 `R` 和
`C` 处的数据何时有效。当此值为 1（`true`）时，
模块已成功计算 *R* 和 *C*
矩阵。当此值为 0（`false`）时，输出数据
无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号
指示模块何时准备好接收新的输入数据。当此值为 1
（`true`）且 `validIn` 值为 1
（`true`）时，模块在下一时间步接受输入数据。当
此值为 0（`false`）时，模块在下一时间步忽略输入数据。

发送 `true`
`validIn` 信号后，在
`ready` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据都
得到处理，必须等到 `ready` 被设置为
`false` 后，再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **输入矩阵 A 和 B 的行数** — 矩阵 *A* 和 *B* 的行数 `4`（默认）| 正整数标量

输入矩阵 *A* 和 *B* 的行数，
指定为正整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `m` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **矩阵 A 的列数** — 输入矩阵 *A* 的列数 `4`（默认）| 正整数标量

输入矩阵 *A* 的列数，指定为正整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `n` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **矩阵 B 的列数** — 输入矩阵 *B* 的列数 `1`（默认）| 正整数标量

输入矩阵 *B* 的列数，指定为正整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `p` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0（默认）| 实数非负标量

正则化参数，指定为非负标量。正则化参数的较小正值
可以改善问题的条件数并降低估计的方差。虽然估计有偏，
但与最小二乘估计相比，估计方差的降低通常会
带来更小的均方误差。

#### 编程用法

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** 字符向量 |
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

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以改善资源利用率

当您更新图时，构成部分脉动流水线的循环会被展开。此更新的内部架构移除了仿真和生成代码中的死操作，从而显著减少所需的硬件资源数量。此模块相对于以前版本中这些模块的库版本，以时钟精确和位真方式仿真。

| 资源 | R2022b | R2023a |
| --- | --- | --- |
| LUT | 58179 | 35455 |
| LUTRAM | 1330 | 1126 |
| Flip Flop | 37355 | 22334 |

此示例数据是通过在 Xilinx Zynq-7 ZC706 评估板（-2 速度等级）上综合该模块生成的。

以下参数用于综合。

- 模块参数：

  - `m = 10`
  - `n = 10`
  - `p = 1`
  - 矩阵 *A* 维度：10×10
  - 矩阵 *B* 维度：10×1
- 输入数据类型：`sfix18_En12`

## 描述

用于实值矩阵的 QR 分解

Real Partial-Systolic QR Decomposition 模块使用 QR 分解来
计算 *R* 和 *C* = *Q*'*B*，其中 *Q**R* = *A*，且 *A* 和 *B* 是实值矩阵。
*A**x* = *B* 的最小二乘解为 *x* = *R*\*C*。*R* 是上三角矩阵，*Q*
是正交矩阵。要计算 *C* = *Q'*，请将 *B* 设置为单位矩阵。

当正则化参数非零时，
Real Partial-Systolic QR Decomposition 模块将 [λInA] 原地变换为 R=Q'[λInA]，并将 [0n,pB] 原地变换为 C=Q'[0n,pB]，其中 *λ* 是正则化参数，QR 是
[λInA] 的经济型 QR 分解，*A* 是 *m*×*n*
矩阵，*p* 是 *B* 的列数，
*In* =
`eye(n)`，且
*0n,p* =
`zeros(n,p)`。
