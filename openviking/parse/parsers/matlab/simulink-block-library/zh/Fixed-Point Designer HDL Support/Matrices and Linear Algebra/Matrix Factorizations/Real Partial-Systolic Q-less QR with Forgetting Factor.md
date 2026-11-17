---
type: simulink-block
title: 'Real Partial-Systolic Q-less QR with Forgetting Factor Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'realpartialsystolicqlessqrdecompositionwithforgettingfactor'
documentation_source_path: '../fixedpoint/ref/realpartialsystolicqlessqrdecompositionwithforgettingfactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Partial-Systolic Q-less QR with Forgetting Factor Decomposition

## 端口
```yaml
ports:
- name: A(i,:)
  summary: 实矩阵 *A* 的行 向量
  direction: input
  data_types: single | double | fixed point
- name: validIn
  summary: 输入是否有效 Boolean 标量
  direction: input
  data_types: Boolean
- name: restart
  summary: 是否清除内部状态 Boolean 标量
  direction: input
  data_types: Boolean
- name: R
  summary: 上三角矩阵 *R* 矩阵
  direction: output
  data_types: single | double | fixed point
- name: validOut
  summary: 输出数据是否有效 Boolean 标量
  direction: output
  data_types: Boolean
- name: ready
  summary: 模块是否就绪 Boolean 标量
  direction: output
  data_types: Boolean
```

### 输入

### **A(i,:)** — 实矩阵 *A* 的行 向量

实矩阵 *A* 的行，指定为向量。
*A* 是流式数据的无限高矩阵。如果
*A* 使用定点数据类型，则 *A* 必须为
有符号类型并使用二进制小数点定标。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号
指示来自 `A(i,:)` 输入端口的数据何时有效。当
此值为 1（`true`）且 `ready`
的值为 1（`true`）时，模块捕获
`A(i,:)` 输入端口的值。当此值为 0
（`false`）时，模块忽略输入采样。

在发送 `true`
`validIn` 信号后，`ready` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待 `ready` 被设置为
`false` 后再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为布尔标量。当此值为
1（`true`）时，模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validIn` 处的值为 1（`true`）时，模块开始一个新的
子帧。

**数据类型：** `Boolean`
### 输出

### **R** — 上三角矩阵 *R* 矩阵

经济型 QR 分解矩阵 *R* 乘以
`Forgetting factor` 参数，以矩阵形式返回。
*R* 是上三角矩阵。矩阵
*R* 的大小为 *n*×*n*。`R`
处的输出与 `A(i,:)` 处的输入具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为布尔标量。此控制
信号指示输出端口 `R` 处的数据何时有效。当
此值为 1（`true`）时，模块已成功计算
矩阵 *R*。当此值为 0（`false`）时，
输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以布尔标量形式返回。此控制信号
指示模块何时准备好接收新的输入数据。当此值为
`1`（`true`）且 `validIn` 为
`1`（`true`）时，模块在
下一个时间步接受输入数据。当此值为 `0`（`false`）时，
模块在下一个时间步忽略输入数据。

在发送 `true`
`validIn` 信号后，`ready` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待 `ready` 被设置为
`false` 后再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Number of columns in matrix A
  summary: 输入矩阵 *A* 的列数 4（默认）| 正整数值标量
  group: ''
  block_parameter: n
  type: character vector
  values: positive integer-valued scalar
  default: '4'
- name: Forgetting factor
  summary: 矩阵每一行被分解后应用的遗忘因子 0.99（默认）| 实正标量
  group: ''
  block_parameter: forgetting_factor
  type: character vector
  values: positive integer-valued scalar
  default: '0.99'
- name: Regularization parameter
  summary: 正则化参数 0（默认）| 实非负标量
  group: ''
  block_parameter: regularizationParameter
  type: character vector
  values: real nonnegative scalar
  default: '0'
```

### **Number of columns in matrix A** — 输入矩阵 *A* 的列数 `4`（默认）| 正整数值标量

输入矩阵 *A* 的列数，指定为正
整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`n` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`4` |

### **Forgetting factor** — 矩阵每一行被分解后应用的遗忘因子 0.99（默认）| 实正标量

矩阵每一行被分解后应用的遗忘因子，指定为
实正标量。当 *A* 的每一行被无限期输入时，输出会被更新。

#### 编程使用

|  |
| --- |
| **模块参数**：`forgetting_factor` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`0.99` |

### **Regularization parameter** — 正则化参数 0（默认）| 实非负标量

正则化参数，指定为非负标量。正则化参数的较小正值
可以改善问题的条件数并减小
估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的减小通常
会带来更小的均方误差。

#### 编程使用

|  |
| --- |
| **模块参数**：`regularizationParameter` |
| **类型**：character vector |
| **值**：real nonnegative scalar |
| **默认值**：`0` |
## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020b 中引入**

### R2023a：智能展开以改进资源利用率

当您更新图时，构成部分脉动流水线的循环会被
展开。此更新的内部架构移除了仿真和
生成代码中的死操作，从而显著减少了所需的硬件资源
数量。此模块在时钟和位真保真度方面与先前版本中这些模块的库
版本仿真一致。

| 资源 | R2022b | R2023a |
| --- | --- | --- |
| LUT | 55482 | 30190 |
| LUTRAM | 10 | 10 |
| Flip Flop | 32375 | 17570 |
| BRAM | 45 | 31 |

此示例数据通过在 Xilinx
Zynq-7 ZC706 评估板（-2 速度等级）上综合该模块生成。

以下参数用于综合。

- 模块参数：

  - `m = 10`
  - `n = 10`
  - `p = 1`
  - 矩阵 *A* 维度：10×10
  - 矩阵 *B* 维度：10×1
- 输入数据类型：`sfix18_En12`

### R2022a：支持 Tikhonov 正则化参数

Real Partial-Systolic Q-less QR Decomposition with Forgetting Factor
模块现在支持 Tikhonov 正则化参数。

## 描述

用于具有无限行数的实值矩阵的无 Q QR 分解

Real Partial-Systolic Q-less QR Decomposition with Forgetting Factor
模块使用 QR 分解来计算 QR 分解 *A* = *Q**R* 的经济型上三角 *R*
因子，而不计算 *Q*。*A* 是表示流式数据的
无限高实值矩阵。

当正则化参数非零时，Real Partial-Systolic Q-less QR
Decomposition with Forgetting Factor 模块在将
*A* 的行分解之前，将第一个上三角
因子 *R* 初始化为 *λIn*，其中 *λ* 是正则化
参数，*In* =
`eye(n)`。
