---
type: simulink-block
title: 'Complex Burst Matrix Solve Using Q-less QR Decomposition'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'complexburstmatrixsolveusingqlessqrdecomposition'
documentation_source_path: '../fixedpoint/ref/complexburstmatrixsolveusingqlessqrdecomposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Burst Matrix Solve Using Q-less QR Decomposition

## 端口

### 输入

### **A(i,:)** — 矩阵 *A* 的行向量

矩阵 *A* 的行，指定为向量。*A* 是 *m*×*n* 矩阵，其中 *m* ≥ 2 且 *m* ≥ *n*。如果 *B* 为 single 或 double，则 *A* 必须与 *B* 具有相同的数据类型。如果 *A* 是定点数据类型，则 *A* 必须为有符号、使用二进制小数点定标，并具有与 *B* 相同的字长。定点数据类型不支持 Slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

### **B(i,:)** — 矩阵 *B* 的行向量

矩阵 *B* 的行，指定为向量。*B* 是 *n*×*p* 矩阵，其中 *n* ≥ 2。如果 *A* 为 single 或 double，则 *B* 必须与 *A* 具有相同的数据类型。如果 *B* 是定点数据类型，则 *B* 必须为有符号、使用二进制小数点定标，并具有与 *A* 相同的字长。定点数据类型不支持 Slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 `A(i,:)` 和 `B(i,:)` 输入端口的数据何时有效。当此值为 `1` (`true`) 且 `ready` 值为 `1` (`true`) 时，模块捕获 `A(i,:)` 和 `B(i,:)` 输入端口处的值。当此值为 `0` (`false`) 时，模块忽略输入样本。

在发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `ready` 设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 `Boolean` 标量

是否清除内部状态，指定为 Boolean 标量。当此值为 1 (`true`) 时，模块停止当前计算并清除所有内部状态。当此值为 0 (`false`) 且 `validIn` 值为 1 (`true`) 时，模块开始新的子帧。

**数据类型：** `Boolean`

### 输出

### **X(i,:)** — 矩阵 *X* 的行 标量 | 向量

矩阵 *X* 的行，以标量或向量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。此控制信号指示输出端口 `X(i,:)` 处的数据何时有效。当此值为 `1` (`true`) 时，模块已成功计算出一行 *X*。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，以 Boolean 标量形式返回。此控制信号指示模块何时准备好接收新输入数据。当此值为 `1` (`true`) 且 `validIn` 值为 `1` (`true`) 时，模块在下一个时间步接受输入数据。当此值为 `0` (`false`) 时，模块在下一个时间步忽略输入数据。

在发送 `true` `validIn` 信号后，在 `ready` 设置为 `false` 之前可能会有一些延迟。为确保处理所有数据，必须先等待 `ready` 设置为 `false`，然后再发送另一个 `true` `validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **矩阵 A 的行数** — 矩阵 *A* 的行数 `4`（默认）| 正整数值标量

矩阵 *A* 的行数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `m` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 A 的列数和矩阵 B 的行数** — 矩阵 *A* 的列数和矩阵 *B* 的行数 `4`（默认）| 正整数值标量

矩阵 *A* 的列数和矩阵 *B* 的行数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `n` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `4` |

### **矩阵 B 的列数** — 矩阵 *B* 的列数 `1`（默认）| 正整数值标量

矩阵 *B* 的列数，指定为正整数值标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `p` |
| **类型：** character vector |
| **值：** 正整数值标量 |
| **默认值：** `1` |

### **正则化参数** — 正则化参数 0（默认）| 实数非负标量

正则化参数，指定为非负标量。较小的正正则化参数值可以改善问题的条件并减少估计的方差。虽然有偏，但与最小二乘估计相比，估计方差降低通常会得到更小的均方误差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `regularizationParameter` |
| **类型：** character vector |
| **值：** 实数非负标量 |
| **默认值：** `0` |

### **输出数据类型** — 输出矩阵 *X* 的数据类型 `fixdt(1,18,14)`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

输出矩阵 *X* 的数据类型，指定为 `fixdt(1,18,14)`、`double`、`single`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputType` |
| **类型：** character vector |
| **值：** `'fixdt(1,18,14)'` | `'double'` | `'single'` | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值：** `'fixdt(1,18,14)'` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Linear System Solvers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持 Slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020a 中引入**

### R2022a：支持 Tikhonov 正则化参数

Complex Burst Matrix Solve Using Q-less QR Decomposition 模块现在支持 Tikhonov 正则化参数。

### R2021a：减少 HDL 资源使用

此模块现在具有改进的算法，可减少硬件受限目标平台上的资源使用。

## 描述

使用无 Q QR 分解计算复值矩阵的方程 A ' A X = B 中 X 的值

Complex Burst Matrix Solve Using Q-less QR Decomposition 模块使用无 Q QR 分解求解线性方程组 *A*'*A**X* = *B*，其中 *A* 和 *B* 是复值矩阵。

当正则化参数非零时，Complex Burst Matrix Solve Using Q-less QR Decomposition 模块求解矩阵方程

[λInA]'⋅[λInA]X=(λ2In+A'A)X=B

其中 *λ* 是正则化参数，*A* 是 *m*×*n* 矩阵，且 *In* = `eye(n)`。
