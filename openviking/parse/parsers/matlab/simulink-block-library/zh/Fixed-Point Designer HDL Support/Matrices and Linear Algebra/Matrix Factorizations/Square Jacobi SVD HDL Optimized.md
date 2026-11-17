---
type: simulink-block
title: 'Square Jacobi SVD HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'squarejacobisvdhdloptimized'
documentation_source_path: '../fixedpoint/ref/squarejacobisvdhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Square Jacobi SVD HDL Optimized

## 端口

### 输入

### **A** — 方阵 *A* 实数或复数方阵

方阵 `n`×`n` 矩阵 *A*，指定为实数或复数方阵。

如果矩阵 *A* 具有定点数据类型，则该矩阵必须使用有符号二进制小数点缩放。不支持斜率和偏置缩放以及无符号定点类型。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 `A` 输入端口的数据何时有效。当此值为 `1`（`true`）且 `ready` 处的值为 `1`（`true`）时，模块捕获 `A` 输入端口处的值。当此值为 `0`（`false`）时，模块忽略输入样本。

在发送 `true` 的 `validIn` 信号后，`ready` 信号变为 `false` 之前可能会出现延迟。为确保所有数据都被处理，您必须等待 `ready` 信号变为 `false` 后再发送另一个 `true` 的 `validIn` 信号。

**数据类型：** `Boolean`

### **readyIn** — 下游模块是否就绪 标量

下游模块是否就绪，指定为 `Boolean` 标量。此控制信号监测下游模块的 `ready` 端口。当 `readyIn` 值为 `1`（`true`）且 `validOut` 处的值为 `1`（`true`）时，模块向下游模块输出数据。当 `readyIn` 值为 `0`（`false`）时，下游模块未准备好接收数据。Square Jacobi SVD HDL Optimized 模块在输出阶段暂停，`ready` 信号保持为 `0`（`false`），直到 `readyIn` 信号为高电平。

**数据类型：** `Boolean`

### **restart** — 是否清除内部状态 标量

是否清除内部状态，指定为布尔标量。当此值为 1（`true`）时，模块停止当前计算并清除所有内部状态。当此值为 0（`false`）且 `validIn` 值为 1（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`
### 输出

### **s** — 奇异值 列向量

奇异值，返回为长度为 `n` 的列向量。奇异值为非负值，并按降序返回，使得 `s(1) >= s(2) >= ... >= s(n)`。奇异值返回的数据类型与输入矩阵 `A` 相同。

**数据类型：** `single` | `double` | `fixed point`

### **U** — 左奇异向量 酉 `n`×`n` 矩阵

左奇异向量，返回为酉 `n`×`n` 矩阵。

对于定点和缩放双精度输入，`U` 返回为有符号定点或缩放双精度 `fi`，其字长与 `A` 相同，小数长度等于字长减二。其中一个整数位用于符号。另一个整数位允许精确表示 `+1`。

对于浮点输入，`U` 的数据类型与 `A` 相同。

**数据类型：** `single` | `double` | `fixed point`

### **V** — 右奇异向量 酉 `n`×`n` 矩阵

右奇异向量，返回为酉 `n`×`n` 矩阵。

对于定点和缩放双精度输入，`V` 返回为有符号定点或缩放双精度 `fi`，其字长与 `A` 相同，小数长度等于字长减二。其中一个整数位用于符号。另一个整数位允许精确表示 `+1`。

对于浮点输入，`V` 的数据类型与 `A` 相同。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，返回为布尔标量。此控制信号指示输出端口 `U`、`S` 和 `V` 处的数据何时有效。当此值为 `1`（`true`）时，输出数据有效。当此值为 `0`（`false`）时，输出数据无效。仅当 `validOut` 和 `readyIn` 信号均为高电平时，才会向下游模块传输数据。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，返回为布尔标量。此控制信号指示模块何时准备好接收新的输入数据。当此值为 `1`（`true`）且 `validIn` 值为 `1`（`true`）时，模块在下一个时间步接受输入数据。当此值为 `0`（`false`）时，模块在下一个时间步忽略输入数据。

在发送 `true` 的 `validIn` 信号后，`ready` 信号变为 `false` 之前可能会有一些延迟。为确保所有数据都被处理，您必须等待 `ready` 信号变为 `false` 后再发送另一个 `true` 的 `validIn` 信号。

**数据类型：** `Boolean`

## 参数

### **Dimension of matrix A** — 方阵 *A* 的维度 `n`（默认）| 正整数值标量

方阵 *A* 的维度，指定为正整数值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`n` |
| **类型**：`string` |
| **值**：positive integer-valued scalar |
| **默认值**：`n` |

### **Number of Jacobi iterations** — Jacobi 算法的迭代次数 `10`（默认）| 正整数

Jacobi 算法的迭代次数，指定为正整数。大多数文献表明 10 次迭代足以使 Jacobi 算法收敛 [7][8][9][10]。

当输入为 2×2 矩阵时，SVD 具有闭式解，不需要迭代计算。在这种情况下，将 **Number of Jacobi iterations** 设置为 `1` 以最小化资源利用率和延迟。

#### 编程使用

|  |
| --- |
| **模块参数**：`nIterations` |
| **类型**：`string` |
| **值**：positive integer-valued scalar |
| **默认值**：`10` |

### **Select outputs** — 模块输出 `UsV`（默认）| `Us` | `sV` | `s`

模块输出，指定为 `UsV`、`Us`、`sV` 或 `s`。

#### 编程使用

|  |
| --- |
| **模块参数**：`outputOption` |
| **类型**：`string` |
| **值**：`UsV` | `Us` | `sV` | `s` |
| **默认值**：`UsV` |

### **Signal type** — 输入矩阵 *A* 的复杂度 `real`（默认）| `complex`

输入矩阵 *A* 的复杂度，指定为 `real` 或 `complex`。

#### 编程使用

|  |
| --- |
| **模块参数**：`complexity` |
| **类型**：`string` |
| **值**：`real` | `complex` |
| **默认值**：`real` |

## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

在为大型矩阵生成代码时，将配置参数 **HDL Code Generation > Global Settings > Ports** 选项卡中的 **Check for DUT pin count exceeding I/O Threshold** 设置为 `Warning` 或 `None`。要了解有关此设置的更多信息，请参阅 Check for DUT pin count exceeding I/O Threshold (HDL Coder)。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。定点数据类型必须使用有符号二进制小数点缩放。不支持斜率和偏置缩放以及无符号定点类型。

## 版本历史

**在 R2023a 中引入**

## 描述

定点奇异值分解

使用 Square Jacobi SVD HDL Optimized 模块通过双边 Jacobi 算法对方阵执行奇异值分解（SVD）。给定方阵 *A*，Square Jacobi SVD HDL Optimized 模块使用双边 Jacobi 方法生成非负元素向量 *s* 以及酉矩阵 *U* 和 *V*，使得 `A = U*diag(s)*V'`。

**注意**

对于非方阵，请使用 Non-Square Jacobi SVD HDL Optimized 模块。
