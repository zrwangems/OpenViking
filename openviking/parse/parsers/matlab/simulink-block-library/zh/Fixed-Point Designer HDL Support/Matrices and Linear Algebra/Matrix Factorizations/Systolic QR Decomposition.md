---
type: simulink-block
title: 'Systolic QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'systolicqrdecomposition'
documentation_source_path: '../fixedpoint/ref/systolicqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Systolic QR Decomposition

## 端口

### 输入

### **A** — 矩阵 *A* 矩阵

矩阵 *A*，指定为矩阵。*A* 是一个
*m*×*n* 矩阵，其中 *m* ≥ 2 且 *n* ≥ 2。如果 *B* 为 single 或 double 类型，*A*
必须与 *B* 具有相同的数据类型。如果 *A* 为
定点数据类型，*A* 必须为有符号类型，使用二进制小数点缩放，
并且与 *B* 具有相同的字长。定点数据类型不支持
斜率-偏置表示。

#### 依赖关系

使用 **Signal
type** 参数指定输入数据的复杂度。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **B** — 矩阵 *B* 矩阵

矩阵 *B*，指定为矩阵。*B* 是一个
*m*×*p* 矩阵，其中 *m* ≥ 2。如果 *A* 为 single 或 double 类型，*B*
必须与 *A* 具有相同的数据类型。如果 *B* 为
定点数据类型，*B* 必须为有符号类型，使用二进制小数点缩放，
并且与 *A* 具有相同的字长。定点数据类型不支持
斜率-偏置表示。

#### 依赖关系

使用 **Signal
type** 参数指定输入数据的复杂度。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **validIn** — 输入是否有效 标量

输入是否有效，指定为布尔标量。此控制信号
指示来自 **A** 和 **B** 输入端口的数据何时
有效。当此值为 1（`true`）且
**readyIn** 处的值为 1（`true`）时，该模块捕获
**A** 和 **B** 输入端口上的值。当此值为 0
（`false`）时，该模块忽略输入采样。

#### 提示

在发送 `true`
**validIn** 信号后，**readyIn** 被
设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等待
**readyIn** 被设置为 `false` 后再发送另一个
`true`
**validIn** 信号。

**数据类型：** `Boolean`

### **readyIn** — 下游模块是否就绪 标量

下游模块是否就绪，指定为布尔标量。此控制
信号监视下游模块的 **ready** 端口。当
**readyIn** 值为 `1`（`true`）且
**validOut** 处的值为 `1`（`true`）时，
该模块向下游模块输出数据。当 **readyIn** 值为
`0`（`false`）时，下游模块未准备好
接受数据。Systolic QR Decomposition 模块在
输出阶段暂停，**ready** 信号保持为 `0`
（`false`），直到 **readyIn** 信号为高电平。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 标量

是否清除内部状态，指定为布尔标量。当此值为
`1`（`true`）时，该模块停止当前
计算并清除所有内部状态。当此值为 `0`
（`false`）且 **validIn** 值为 1
（`true`）时，该模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **R** — 矩阵 *R* 矩阵

经济型 QR 分解矩阵 *R*，以矩阵形式返回。
*R* 是上三角矩阵。矩阵
*R* 的大小为 *n*×*n*。
*R* 与 *A* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **C** — 矩阵 *C = Q'B* 矩阵

经济型 QR 分解矩阵 *C*=*Q*'*B*，以矩阵形式返回。*C* 与
*R* 具有相同的行数。*C* 与
*B* 具有相同的数据类型。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **validOut** — 输出数据是否有效 标量

输出数据是否有效，以布尔标量形式返回。此控制信号
指示输出端口 **R** 和 **C** 处的数据何时有效。
当此值为 `1`（`true`）时，该模块已
成功计算 **R** 和 **C** 矩阵。当此值为
`0`（`false`）时，输出数据
无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 标量

模块是否就绪，以布尔标量形式返回。此控制信号
指示该模块何时准备好接收新的输入数据。当此值为
`1`（`true`）且 **validIn** 值为
`1`（`true`）时，该模块在
下一个时间步接受输入数据。当此值为 `0`（`false`）时，
该模块在下一个时间步忽略输入数据。

#### 提示

在发送 `true`
**validIn** 信号后，**ready** 被
设置为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等待
**ready** 被设置为 `false` 后再发送另一个
`true`
**validIn** 信号。

**数据类型：** `Boolean`

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Number of rows in matrices A and B** — 矩阵 *A* 和 *B* 的行数 `2`（默认）| 正整数值标量

输入矩阵 *A* 和 *B* 的行数，
指定为正整数值标量。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `m` |
| **值**：| `2`（默认）| 正整数值标量 |
| **Data Types:** | `char` |

### **Number of columns in matrix A** — 矩阵 *A* 的列数 `2`（默认）| 正整数值标量

矩阵 *A* 的列数，指定为正
整数值标量。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `n` |
| **值**：| `2`（默认）| 正整数值标量 |
| **Data Types:** | `char` |

### **Number of columns in matrix B** — 矩阵 *B* 的列数 `1`（默认）| 正整数值标量

矩阵 *B* 的列数，指定为正
整数值标量。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `p` |
| **值**：| `1`（默认）| 正整数值标量 |
| **Data Types:** | `char` |

### **Signal type** — 矩阵 *A* 和 *B* 的复杂度 `real`（默认）| `complex`

矩阵 *A* 和 *B* 的复杂度，指定为
`real` 或 `complex`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `complexity` |
| **值**：| `real`（默认）| `complex` |
| **Data Types:** | `char` |

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。定点数据类型必须使用有符号
二进制小数点缩放。不支持斜率-偏置缩放类型。

## 版本历史

**在 R2024a 中引入**

## 描述

矩阵的 QR 分解

Systolic QR Decomposition 模块使用 QR 分解来计算
*R* 和 *C* = *Q*'*B*，其中 *Q**R* = *A*，且 *A* 和 *B* 为矩阵。
*A**X* = *B* 的最小二乘解为 *X* = *R*\*C*。*R* 是上三角矩阵，*Q*
是正交矩阵。要计算 *C* = *Q'*，请将 *B* 设置为单位矩阵。

脉动实现可最小化系统延迟并提高吞吐量。
脉动实现比突发或部分脉动
实现需要更多的硬件资源。
