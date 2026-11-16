---
type: simulink-block
title: 'Complex Partial-Systolic Q-less QR Decomposition with Forgetting Factor'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Matrix Operations in Simulink / Matrix Factorizations / Q-less QR Decomposition with Forgetting Factor'
documentation_page: 'complexpartialsystolicqlessqrdecompositionwithforgettingfactor'
documentation_source_path: 'ref/complexpartialsystolicqlessqrdecompositionwithforgettingfactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Partial-Systolic Q-less QR Decomposition with Forgetting Factor

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行向量

矩阵 *A* 的行，指定为向量。*A* 是流数据的无限高矩阵。如果 *A* 是定点数据类型，则 *A* 必须为有符号、使用二进制点缩放，并具有与 *B* 相同的字长。定点数据类型不支持 slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示 `A(i,:)` 输入端口上的数据何时有效。当该值为 1 (`true`) 且 `ready` 处的值为 1 (`true`) 时，模块捕获 `A(i,:)` 输入端口处的值。当该值为 0 (`false`) 时，模块忽略输入样本。

发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，在发送另一个 `true` `validIn` 信号之前，必须等待直到 `ready` 设置为 `false`。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当该值为 1 (`true`) 时，模块停止当前计算并清除所有内部状态。当该值为 0 (`false`) 且 `validIn` 值为 1 (`true`) 时，模块开始一个新的子帧。

**数据类型：** `Boolean`

### 输出

### **R** — 矩阵 *R* 标量 | 向量

经济型 QR 分解矩阵 *R*，以标量或向量形式返回。*R* 是上三角矩阵。矩阵 *R* 的大小为 *n* 乘 *n*。*R* 具有与 *A* 相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为 Boolean 标量。此控制信号指示输出端口 `R` 上的数据何时有效。当该值为 1 (`true`) 时，模块已成功计算矩阵 *R*。当该值为 0 (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当该值为 `1` (`true`) 且 `validIn` 值为 `1` (`true`) 时，模块在下一个时间步接受输入数据。当该值为 `0` (`false`) 时，模块在下一个时间步忽略输入数据。

发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，在发送另一个 `true` `validIn` 信号之前，必须等待直到 `ready` 设置为 `false`。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 的列数** — 输入矩阵 *A* 的列数 `4`（默认） | 正整数值标量

输入矩阵 *A* 的列数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **遗忘因子** — 矩阵每一行分解后应用的遗忘因子 0.99（默认） | 实正标量

遗忘因子在矩阵每一行被分解后应用，指定为实正标量。当 *A* 的每一行无限期输入时，输出会更新。

#### 程序化使用

|  |
| --- |
| **模块参数：** `forgettingFactor` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `0.99` |

### **正则化参数** — 正则化参数 0（默认） | 实非负标量

正则化参数，指定为非负标量。较小的正正则化参数值可以改善问题的条件数并降低估计的方差。虽然会产生偏差，但与最小二乘估计相比，估计方差的降低通常会带来更小的均方误差。

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

定点数据类型不支持 slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以改进资源利用率

更新图时，构成部分脉动流水线的循环会被展开。此更新的内部架构移除了仿真和生成代码中的死操作，从而显著减少了所需的硬件资源数量。相对于以前版本中这些模块的库版本，此模块以时钟和位真保真度进行仿真。

| 资源 | R2022b | R2023a |
| --- | --- | --- |
| LUT | 162888 | 91496 |
| LUTRAM | 3620 | 2000 |
| Flip Flop | 100309 | 54609 |
| BRAM | 45 | 31 |

此示例数据是通过在 Xilinx Zynq-7 ZC706 评估板（-2 速度等级）上综合该模块生成的。

以下参数用于综合。

- 模块参数：

  - `m = 10`
  - `n = 10`
  - `p = 1`
  - 矩阵 *A* 维度：10×10
  - 矩阵 *B* 维度：10×1
- 输入数据类型：`sfix18_En12`

### R2022a：支持 Tikhonov 正则化参数

Complex Partial-Systolic Q-less QR Decomposition with Forgetting Factor 模块支持 Tikhonov 正则化参数。

### R2021a：降低 HDL 资源利用率

此模块现在具有改进的算法，可在硬件受限的目标平台上降低资源利用率。

## 描述

用于具有无限行数的复值矩阵的 Q-less QR 分解

Complex Partial-Systolic Q-less QR Decomposition with Forgetting Factor 模块使用 QR 分解来计算 QR 分解 *A* = *Q**R* 的经济型上三角 *R* 因子，而不计算 *Q*。*A* 是表示流数据的无限高复值矩阵。

当正则化参数非零时，Complex Partial-Systolic Q-less QR Decomposition with Forgetting Factor 模块在分解 *A* 的各行之前，将第一个上三角因子 *R* 初始化为 *λIn*，其中 *λ* 是正则化参数，*In* = `eye(n)`。
