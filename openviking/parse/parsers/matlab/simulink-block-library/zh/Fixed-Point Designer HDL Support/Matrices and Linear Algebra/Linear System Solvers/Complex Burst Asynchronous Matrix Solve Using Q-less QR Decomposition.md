---
type: simulink-block
title: 'Complex Burst Asynchronous Matrix Solve Using Q-less QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'complexburstasynchronousmatrixsolveusingqlessqrdecomposition'
documentation_source_path: '../fixedpoint/ref/complexburstasynchronousmatrixsolveusingqlessqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst Asynchronous Matrix Solve Using Q-less QR Decomposition

## 端口

### 输入

### **A(i,:)** — 复矩阵 *A* 的行向量

复矩阵 *A* 的行，指定为向量。
*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *m* ≥ *n*。如果 *B* 为 single 或 double，则 *A*
必须与 *B* 具有相同的数据类型。如果 *A* 为
定点数据类型，则 *A* 必须为有符号、使用二进制小数点缩放，
并具有与 *B* 相同的字长。定点数据类型不支持
斜率偏差表示。

**数据类型：** `single` | `double` | `fixed point`

### **B** — 复矩阵 *B* 的行向量

复矩阵 *B* 的行，指定为向量。
*B* 是 *n*×*p* 矩阵，其中 *n* ≥ 2。如果 *A* 为 single 或 double，则 *B*
必须与 *A* 具有相同的数据类型。如果 *B* 为
定点数据类型，则 *B* 必须为有符号、使用二进制小数点缩放，
并具有与 *A* 相同的字长。定点数据类型不支持
斜率偏差表示。

**数据类型：** `single` | `double` | `fixed point`

### **validInA** — `A(i,:)` 输入是否有效 `Boolean` 标量

`A(i,:)` 输入是否有效，指定为 Boolean 标量。
此控制信号指示来自 `A(i,:)` 输入端口的
数据何时有效。当此值为 `1`（`true`）且
`readyA` 值为 `1`（`true`）时，
该模块捕获 `A(i,:)` 输入端口处的值。当此
值为 `0`（`false`）时，该模块忽略输入
样本。

发送 `true`
`validInA` 信号后，在
`readyA` 设置为 `false` 之前可能会有一些延迟。为确保所有数据
均得到处理，必须等待 `readyA` 设置为
`false` 后，再发送另一个 `true`
`validInA` 信号。

**数据类型：** `Boolean`

### **validInB** — `B` 输入是否有效 `Boolean` 标量

`B` 输入是否有效，指定为 Boolean 标量。此
控制信号指示来自 `B` 输入端口的数据何时
有效。当此值为 `1`（`true`）且
`readyB` 值为 `1`（`true`）时，
该模块捕获 `B` 输入端口处的值。当此值
为 `0`（`false`）时，该模块忽略输入
样本。

发送 `true`
`validInB` 信号后，在
`readyB` 设置为 `false` 之前可能会有一些延迟。为确保所有数据
均得到处理，必须等待 `readyB` 设置为
`false` 后，再发送另一个 `true`
`validInB` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值
为 1（`true`）时，该模块停止当前计算并清除所有
内部状态。当此值为 0（`false`）且
`validIn` 处的值为 1（`true`）时，该模块开始新的
子帧。

**数据类型：** `Boolean`
### 输出

### **X** — 矩阵 *X*，矩阵 | 向量

矩阵 *X*，返回为矩阵或向量。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，指定为 Boolean 标量。此控制
信号指示输出端口 `X` 处的数据何时有效。当此
值为 1（`true`）时，该模块已成功计算矩阵
*X*。当此值为 0（`false`）时，输出
数据无效。

**数据类型：** `Boolean`

### **readyA** — 模块是否已准备好接受输入 `A(i,:)` `Boolean` 标量

模块是否已准备好接受输入 `A(i,:)`，返回为 Boolean
标量。此控制信号指示该模块何时准备好接受新的输入数据。当
此值为 `1`（`true`）且
`validInA` 为 `1`（`true`）时，该
模块在下一时间步接受输入数据。当此值为
`0`（`false`）时，该模块在下一时间步忽略输入数据。

发送 `true`
`validInA` 信号后，在
`readyA` 设置为 `false` 之前可能会有一些延迟。为确保所有数据
均得到处理，必须等待 `readyA` 设置为
`false` 后，再发送另一个 `true`
`validInA` 信号。

**数据类型：** `Boolean`

### **readyB** — 模块是否已准备好接受输入 `B` `Boolean` 标量

模块是否已准备好接受输入 `B`，返回为 Boolean
标量。此控制信号指示该模块何时准备好接受新的输入数据。当
此值为 `1`（`true`）且
`validInB` 为 `1`（`true`）时，该
模块在下一时间步接受输入数据。当此值为
`0`（`false`）时，该模块在下一时间步忽略输入数据。

发送 `true`
`validInB` 信号后，在
`readyB` 设置为 `false` 之前可能会有一些延迟。为确保所有数据
均得到处理，必须等待 `readyB` 设置为
`false` 后，再发送另一个 `true`
`validInB` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 的行数** — 矩阵 *A* 的行数 `4`（默认）| 正整数标量

矩阵 *A* 的行数，指定为正整数
标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `m` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **矩阵 A 的列数和矩阵 B 的行数** — 矩阵 *A* 的列数和矩阵 *B* 的行数 `4`（默认）| 正整数标量

矩阵 *A* 的列数和矩阵
*B* 的行数，指定为正整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `n` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `4` |

### **矩阵 B 的列数** — 矩阵 *B* 的列数 `1`（默认）| 正整数标量

矩阵 *B* 的列数，指定为正整数
标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `p` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0（默认）| 实数非负标量

正则化参数，指定为非负标量。正则化参数的较小正值
可以改善问题的条件并减小估计的方差。虽然有偏，
但与最小二乘估计相比，估计方差的减小通常
会带来更小的均方误差。

#### 编程用法

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** 字符向量 |
| **值：** 实数非负标量 |
| **默认值：** `0` |

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为
`fixdt(1,18,14)`、`double`、
`single`、`fixdt(1,16,0)`，或指定为用户自定义的
数据类型表达式。该类型可以直接指定，也可以表示为数据类型
对象，例如 `Simulink.NumericType`。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputType` |
| **类型：** 字符向量 |
| **值：** `'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值：** `'fixdt(1,18,14)'` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率偏差表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

使用异步无 Q QR 分解，计算复值矩阵方程 A ' A X = B 中 X 的值

Complex Burst Asynchronous Matrix Solve Using Q-less QR Decomposition
模块使用异步无 Q QR 分解求解线性方程组 *A*'*A**X* =
*B*，其中 *A* 和
*B* 为复值矩阵。

当正则化参数非零时，
Complex Burst Asynchronous Matrix Solve Using Q-less QR Decomposition 模块
求解矩阵方程

[λInA]'⋅[λInA]X=(λ2In+A'A)X=B

其中 *λ* 是正则化参数，
*A* 是 *m*×*n* 矩阵，且
*In* =
`eye(n)`。

此模块异步运行。前向代入和回代以及无 Q QR
分解使用最新的 *R* 和 *B*
矩阵独立运行。
