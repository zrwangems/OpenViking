---
type: simulink-block
title: 'Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R Output'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'complexburstqlessqrdecompositionwithforgettingfactorwholeroutput'
documentation_source_path: '../fixedpoint/ref/complexburstqlessqrdecompositionwithforgettingfactorwholeroutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R Output

## 端口
```yaml
ports:
- name: A(i,:)
  summary: 复矩阵 *A* 的行 向量
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
  summary: 经济型 QR 分解矩阵 *R* 向量
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

### **A(i,:)** — 复矩阵 *A* 的行 向量

复矩阵 *A* 的行，指定为向量。
*A* 是流数据构成的无限高矩阵。如果
*A* 使用定点数据类型，则 *A* 必须为
有符号类型并使用二进制小数点定标。定点数据类型不支持
斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号
指示来自 `A(i,:)` 输入端口的数据何时有效。当
此值为 1（`true`）且 `ready` 的值为
1（`true`）时，模块在
`A(i,:)` 输入端口捕获值。当此值为 0
（`false`）时，模块忽略输入采样。

在发送 `true`
`validIn` 信号后，`ready` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，你必须等到 `ready` 被设置为
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

### **R** — 经济型 QR 分解矩阵 *R* 向量

经济型 QR 分解矩阵 *R*，以向量形式返回。
*R* 是上三角矩阵。矩阵
*R* 的大小为 `n`×`n`。
*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为布尔标量。此控制
信号指示输出端口 `R(i,:)` 处的数据何时有效。当
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
都被处理，你必须等到 `ready` 被设置为
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
  summary: 对矩阵每一行进行分解后应用的遗忘因子 0.99（默认）| 实正标量
  group: ''
  block_parameter: forgetting_factor
  type: character vector
  values: real positive scalar
  default: '0'
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

### **Forgetting factor** — 对矩阵每一行进行分解后应用的遗忘因子 `0.99`（默认）| 实正标量

对矩阵每一行进行分解后应用的遗忘因子，指定为
实正标量。当 *A* 的每一行被无限输入时，输出会随之更新。

#### 编程使用

|  |
| --- |
| **模块参数**：`forgetting_factor` |
| **类型**：character vector |
| **值**：real positive scalar |
| **默认值**：`0` |

### **Regularization parameter** — 正则化参数 `0`（默认）| 实非负标量

正则化参数，指定为实非负标量。正则化参数的较小正
值可以改善问题的条件数并
减小估计的方差。虽然有偏，但与最小二乘
估计相比，估计方差的减小通常会产生更小的均方误差。

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

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

用于具有无限行数的复值矩阵的无 Q QR 分解

Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R
Output 模块使用 QR 分解来计算 QR 分解 *A* = *Q**R* 的经济型上三角
*R* 因子，而不计算 *Q*。*A* 是表示流数据的
无限高复值矩阵。

当正则化参数非零时，Complex Burst Q-less QR Decomposition with Forgetting Factor Whole R Output 模块在分解 *A* 的行之前，将第一个
上三角因子 *R* 初始化为 *λ**I**n*，其中
*λ* 是正则化参数，*I**n* =
eye(*n*)
