---
type: simulink-block
title: 'Non-Square Jacobi SVD HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'nonsquarejacobisvdhdloptimized'
documentation_source_path: '../fixedpoint/ref/nonsquarejacobisvdhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Non-Square Jacobi SVD HDL Optimized

## 端口
```yaml
ports:
- name: A(i,:)
  summary: 矩阵 *A* 的行 向量
  direction: input
  data_types: single | double | fixed point
- name: validIn
  summary: 输入是否有效 标量
  direction: input
  data_types: Boolean
- name: readyIn
  summary: 下游模块是否就绪 标量
  direction: input
  data_types: Boolean
- name: restart
  summary: 是否清除内部状态 标量
  direction: input
  data_types: Boolean
- name: s
  summary: 奇异值 列向量
  direction: output
  data_types: single | double | fixed point
- name: U
  summary: 左奇异向量 酉 n×n 矩阵
  direction: output
  data_types: single | double | fixed point
- name: V
  summary: 右奇异向量 酉 n×n 矩阵
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

### **A(i,:)** — 矩阵 *A* 的行 向量

矩阵 *A* 的行，指定为向量。*A* 是一个 *m*×*n* 矩阵，其中 *m* > 2，*n* ≥ 2，且 *m* > *n*。

如果 *A* 是定点数据类型，则 *A* 必须为有符号类型并使用二进制小数点定标。定点数据类型不支持斜率-偏置表示。

#### 提示

输出 **U** 矩阵在输入矩阵 *A* 的秩范围内是正交归一的。有关更多信息，请参阅限制。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **validIn** — 输入是否有效 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 `A` 输入端口的数据何时有效。当此值为 `1`（`true`）且 `ready` 处的值为 `1`（`true`）时，模块捕获 `A` 输入端口处的值。当此值为 `0`（`false`）时，模块忽略输入样本。

#### 提示

在发送 `true` 的 `validIn` 信号后，`ready` 信号可能延迟变为 `false`。为确保所有数据都被处理，您必须等待 `ready` 信号变为 `false` 后再发送另一个 `true` 的 `validIn` 信号。

**数据类型：** `Boolean`

### **readyIn** — 下游模块是否就绪 标量

下游模块是否就绪，指定为 `Boolean` 标量。此控制信号监测下游模块的 `ready` 端口。当 `readyIn` 值为 `1`（`true`）且 `validOut` 处的值为 `1`（`true`）时，模块向下游模块输出数据。当 `readyIn` 值为 `0`（`false`）时，下游模块未准备好接收数据。Non-Square Jacobi SVD HDL Optimized 模块在输出阶段暂停，`ready` 信号保持 `0`（`false`），直到 `readyIn` 信号为高电平。

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

#### 提示

输出 **U** 矩阵在输入矩阵 *A* 的秩范围内是正交归一的。有关更多信息，请参阅限制。

#### 依赖关系

要启用此端口，请将 **Select outputs** 参数设置为 `UsV` 或 `Us`。

**数据类型：** `single` | `double` | `fixed point`

### **V** — 右奇异向量 酉 `n`×`n` 矩阵

右奇异向量，返回为酉 `n`×`n` 矩阵。

对于定点和缩放双精度输入，`V` 返回为有符号定点或缩放双精度 `fi`，其字长与 `A` 相同，小数长度等于字长减二。其中一个整数位用于符号。另一个整数位允许精确表示 `+1`。

对于浮点输入，`V` 的数据类型与 `A` 相同。

#### 依赖关系

要启用此端口，请将 **Select outputs** 参数设置为 `UsV` 或 `sV`。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，返回为布尔标量。此控制信号指示输出端口 `U`、`S` 和 `V` 处的数据何时有效。当此值为 `1`（`true`）时，输出数据有效。当此值为 `0`（`false`）时，输出数据无效。仅当 `validOut` 和 `readyIn` 信号均为高电平时，才会向下游模块传输数据。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean` 标量

模块是否就绪，返回为布尔标量。此控制信号指示模块何时准备好接收新的输入数据。当此值为 `1`（`true`）且 `validIn` 值为 `1`（`true`）时，模块在下一个时间步接受输入数据。当此值为 `0`（`false`）时，模块在下一个时间步忽略输入数据。

#### 提示

在发送 `true` 的 `validIn` 信号后，`ready` 信号可能延迟变为 `false`。为确保所有数据都被处理，您必须等待 `ready` 信号变为 `false` 后再发送另一个 `true` 的 `validIn` 信号。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Number of rows in matrix A
  summary: '*m*×*n* 矩阵 *A* 的行数 8（默认）| 满足 m > 2 且 m > n 的整数值标量'
  group: ''
  block_parameter: m
  values: 8（默认）| 满足 m > 2 且 m > n 的整数值标量
- name: Number of columns in matrix A
  summary: '*m*×*n* 矩阵 *A* 的列数 4（默认）| 满足 n ≥ 2 且 m > n 的整数值标量'
  group: ''
  block_parameter: n
  values: 4（默认）| 满足 n ≥ 2 且 m > n 的整数值标量
- name: Number of Jacobi iterations
  summary: Jacobi 算法的迭代次数 10（默认）| 正整数
  group: ''
  block_parameter: nIterations
  values: 10（默认）| 正整数
- name: Select outputs
  summary: 模块输出 UsV（默认）| Us | sV | s
  group: ''
  block_parameter: outputOption
  values: UsV（默认）| Us | sV | s
- name: Signal type
  summary: 输入矩阵 *A* 的复数性 real（默认）| complex
  group: ''
  block_parameter: complexity
  values: real（默认）| complex
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Number of rows in matrix A** — *m*×*n* 矩阵 *A* 的行数 `8`（默认）| 满足 `m > 2` 且 `m > n` 的整数值标量

*m*×*n* 矩阵 *A* 的行数，指定为满足 *m* > 2 且 *m* > *n* 的整数值标量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `m` |
| **值**：| 8（默认）| 满足 `m > 2` 且 `m > n` 的整数值标量 |
| **Data Types:** | `char` | `string` |

### **Number of columns in matrix A** — *m*×*n* 矩阵 *A* 的列数 `4`（默认）| 满足 `n ≥ 2` 且 `m > n` 的整数值标量

*m*×*n* 矩阵 *A* 的列数，指定为满足 *n* ≥ 2 且 *m* > *n* 的整数值标量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `n` |
| **值**：| 4（默认）| 满足 `n ≥ 2` 且 `m > n` 的整数值标量 |
| **Data Types:** | `char` | `string` |

### **Number of Jacobi iterations** — Jacobi 算法的迭代次数 `10`（默认）| 正整数

Jacobi 算法的迭代次数，指定为正整数。

#### 提示

- 大多数文献表明，10 次迭代足以使 Jacobi 算法收敛 [7][8][9][10]。
- 当输入为 *m*×2 矩阵时，SVD 具有闭式解，不需要迭代计算。在这种情况下，将 **Number of Jacobi iterations** 设置为 `1` 以最小化资源利用率和延迟。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `nIterations` |
| **值**：| `10`（默认）| 正整数 |
| **Data Types:** | `char` | `string` |

### **Select outputs** — 模块输出 `UsV`（默认）| `Us` | `sV` | `s`

模块输出，指定为 `UsV`、`Us`、`sV` 或 `s`。

#### 提示

此参数决定模块上的输出数量。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `outputOption` |
| **值**：| `UsV`（默认）| `Us` | `sV` | `s` |
| **Data Types:** | `char` | `string` |

### **Signal type** — 输入矩阵 *A* 的复数性 `real`（默认）| `complex`

输入矩阵 *A* 的复数性，指定为 `real` 或 `complex`。

#### 提示

此参数决定 Non-Square Jacobi SVD HDL Optimized 模块使用 Real Partial-Systolic QR Decomposition 模块还是 Complex Partial-Systolic QR Decomposition 模块来预处理输入。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `complexity` |
| **值**：| `real`（默认）| `complex` |
| **Data Types:** | `char` | `string` |
## 所属库

Fixed-Point Designer HDL Support / Matrices and Linear Algebra / Matrix Factorizations

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

在为大型矩阵生成代码时，将配置参数 **HDL Code Generation > Global Settings > Ports** 选项卡中的 **Check for DUT pin count exceeding I/O Threshold** 设置为 `Warning` 或 `None`。要了解有关此设置的更多信息，请参阅 Check for DUT pin count exceeding I/O Threshold (HDL Coder)。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。定点数据类型必须使用有符号二进制小数点定标。不支持斜率-偏置定标和无符号定点类型。

## 版本历史

**在 R2023b 中引入**

## 描述

定点奇异值分解

使用 Non-Square Jacobi SVD HDL Optimized 模块，通过 QR 分解和双边 Jacobi 算法对非方阵执行奇异值分解（SVD）。此模块由 Real Partial-Systolic QR Decomposition 或 Complex Partial-Systolic QR Decomposition 模块（取决于您的配置）以及 Square Jacobi SVD HDL Optimized 组成。给定一个行数多于列数的矩阵 *A*，Non-Square Jacobi SVD HDL Optimized 模块使用 QR 分解预处理输入，然后使用双边 Jacobi 方法生成非负元素的向量 *s* 以及酉矩阵 *U* 和 *V*，使得 `A = U*diag(s)*V'`。

**注意**

对于方阵，请使用 Square Jacobi SVD HDL Optimized 模块。
