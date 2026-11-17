---
type: simulink-block
title: 'Real Burst Matrix Solve Using QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'realburstmatrixsolveusingqrdecomposition'
documentation_source_path: '../fixedpoint/ref/realburstmatrixsolveusingqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Burst Matrix Solve Using QR Decomposition

## 端口
```yaml
ports:
- name: A(i,:)
  summary: 实矩阵 *A* 的行 向量
  direction: input
  data_types: single | double | fixed point
- name: B(i,:)
  summary: 实矩阵 *B* 的行 向量
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
- name: X(i,:)
  summary: 矩阵 *X* 的行 标量 | 向量
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
*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *m* ≥ *n*。如果 *B* 为 single 或 double 类型，*A*
必须与 *B* 具有相同的数据类型。如果 *A* 为
定点数据类型，*A* 必须为有符号类型，使用二进制小数点缩放，
并且与 *B* 具有相同的字长。定点数据类型不支持
斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **B(i,:)** — 实矩阵 *B* 的行 向量

实矩阵 *B* 的行，指定为向量。
*B* 是 *m*×*p* 矩阵，其中 *m* ≥ 2。如果 *A* 为 single 或 double 类型，*B*
必须与 *A* 具有相同的数据类型。如果 *B* 为
定点数据类型，*B* 必须为有符号类型，使用二进制小数点缩放，
并且与 *A* 具有相同的字长。定点数据类型不支持
斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号
指示来自 `A(i,:)` 和
`B(i,:)` 输入端口的数据何时有效。当此值为 1
（`true`）且 `ready` 处的值为 1
（`true`）时，模块捕获
`A(i,:)` 和 `B(i,:)` 输入端口上的值。当此
值为 0（`false`）时，模块忽略输入采样。

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
`validIn` 值为 1（`true`）时，模块开始
一个新的子帧。

**数据类型：** `Boolean`
### 输出

### **X(i,:)** — 矩阵 *X* 的行 标量 | 向量

矩阵 *X* 的行，以标量或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以布尔标量形式返回。此控制
信号指示输出端口 `X(i,:)` 处的数据何时
有效。当此值为 1（`true`）时，模块已成功
计算矩阵 *X* 的一行。当此值为 0
（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以布尔标量形式返回。此控制信号
指示模块何时准备好接收新的输入数据。当此值为 1
（`true`）且 `validIn` 值为 1
（`true`）时，模块在下一个时间步接受输入数据。当
此值为 0（`false`）时，模块在下一个
时间步忽略输入数据。

在发送 `true`
`validIn` 信号后，`ready` 被设置为 `false` 之前可能会有一些延迟。为确保所有数据
都被处理，您必须等待 `ready` 被设置为
`false` 后再发送另一个 `true`
`validIn` 信号。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Number of rows in matrices A and B
  summary: 矩阵 *A* 和 *B* 的行数 4（默认）| 正整数值标量
  group: ''
  block_parameter: m
  type: character vector
  values: positive integer-valued scalar
  default: '4'
- name: Number of columns in matrix A
  summary: 矩阵 *A* 的列数 4（默认）| 正整数值标量
  group: ''
  block_parameter: n
  type: character vector
  values: positive integer-valued scalar
  default: '4'
- name: Number of columns in matrix B
  summary: 矩阵 *B* 的列数 1（默认）| 正整数值标量
  group: ''
  block_parameter: p
  type: character vector
  values: positive integer-valued scalar
  default: '1'
- name: Regularization parameter
  summary: 正则化参数 0（默认）| 非负标量
  group: ''
  block_parameter: regularizationParameter
  type: character vector
  values: positive integer-valued scalar
  default: '0'
- name: Output datatype
  summary: 输出矩阵 *X* 的数据类型 fixdt(1,18,14)（默认）| double | single | fixdt(1,16,0) | <data type expression>
  group: ''
  block_parameter: OutputType
  type: character vector
  values: '''fixdt(1,18,14)'' | ''double'' | ''single'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''fixdt(1,18,14)'''
```

### **Number of rows in matrices A and B** — 矩阵 *A* 和 *B* 的行数 `4`（默认）| 正整数值标量

输入矩阵 *A* 和 *B* 的行数，
指定为正整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`m` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`4` |

### **Number of columns in matrix A** — 矩阵 *A* 的列数 `4`（默认）| 正整数值标量

输入矩阵 *A* 的列数，指定为正
整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`n` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`4` |

### **Number of columns in matrix B** — 矩阵 *B* 的列数 `1`（默认）| 正整数值标量

输入矩阵 *B* 的列数，指定为正
整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`p` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`1` |

### **Regularization parameter** — 正则化参数 0（默认）| 非负标量

正则化参数，指定为非负标量。正则化参数的较小正
值可以改善问题的条件数并减少
估计的方差。虽然有偏，但与最小二乘估计相比，估计方差的减少通常
导致更小的均方误差。

#### 编程使用

|  |
| --- |
| **模块参数**：`regularizationParameter` |
| **类型**：character vector |
| **值**：positive integer-valued scalar |
| **默认值**：`0` |

### **Output datatype** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为
`fixdt(1,18,14)`、`double`、
`single`、`fixdt(1,16,0)`，或用户指定的
数据类型表达式。该类型可以直接指定，也可以表示为数据类型
对象，如 `Simulink.NumericType`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputType` |
| **类型**：character vector |
| **值**：`'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值**：`'fixdt(1,18,14)'` |
## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

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

**在 R2019b 中引入**

### R2022a：支持 Tikhonov 正则化参数

Real Burst Matrix Solve Using QR Decomposition 模块现在支持
Tikhonov 正则化参数。

## 描述

使用 QR 分解计算实值矩阵方程 A x = B 中 x 的值

Real Burst Matrix Solve Using QR Decomposition 模块使用 QR 分解求解
线性方程组 *A**x* = *B*，其中 *A* 和 *B*
为实值矩阵。要计算 *x* =
*A*-1，将 *B* 设置为单位矩阵。

当 Regularization parameter 非零时，
Real Burst Matrix Solve Using QR Decomposition 模块计算
实值 [λInA]X=[0n,pB] 的矩阵解，其中 *λ* 是正则化参数，
*A* 是 *m*×*n* 矩阵，
*p* 是 *B* 的列数，
*In* =
`eye(n)`，且
*0n,p* =
`zeros(n,p)`。
