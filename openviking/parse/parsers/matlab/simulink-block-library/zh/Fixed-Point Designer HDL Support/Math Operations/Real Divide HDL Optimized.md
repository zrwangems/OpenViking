---
type: simulink-block
title: 'Real Divide HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'realdividehdloptimized'
documentation_source_path: '../fixedpoint/ref/realdividehdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Divide HDL Optimized

## 端口

### 输入

### **num** — 分子 标量 | 向量 | 矩阵

分子，指定为实数值标量、向量或矩阵。**num** 和 **den** 必须具有相同的维度。

定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **den** — 分母 标量 | 向量 | 矩阵

分母，指定为实数值标量、向量或矩阵。**num** 和 **den** 必须具有相同的维度。

定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **num** 和 **den** 输入端口的数据何时有效。当此值为 `1`（`true`）时，模块捕获输入端口 **num** 和 **den** 处的值。当此值为 `0`（`false`）时，模块忽略输入采样。

**数据类型：** `Boolean`
### 输出

### **y** — 输入相除计算得到的输出 实数标量

**num** 除以 **den** 计算得到的输出，即 **y** = **num**/**den**，以实数标量返回。

#### 提示

输出端口 **y** 处的数据类型由 **Output datatype** 参数指定。

**数据类型：** `single` | `double` | `fixed point`

### **divideByZero** — 输出值是否为除零的结果 `Boolean` 标量

*自 R2024b 起*

**y** 输出端口处的值是否为除零操作的结果，以布尔标量返回。当此信号的值为 `1`（`true`）时，**y** 端口处对应的输出值是除零的结果。当此信号的值为 `0`（`false`）时，**y** 端口处对应的输出值是非零值相除的结果。

有关默认除零行为的描述，请参阅 Division by Zero Behavior。

#### 依赖关系

要启用此端口，请选中 **Show divide by zero port** 参数。

**数据类型：** `Boolean`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以布尔标量返回。当此控制信号的值为 `1`（`true`）时，模块已成功计算出端口 **y** 处的输出。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

## 参数

### **Output datatype** — 输出的数据类型 `fixdt(1,18,10)`（默认）| `single` | `double` | `fixdt(1,16,0)` | `<data type expression>`

输出 **y** 的数据类型，指定为 `fixdt(1,18,10)`、`single`、`double`、`fixdt(1,16,0)` 或用户指定的数据类型表达式。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

*在 R2024b 中：此参数支持无符号数据类型。*

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutputType` |
| **值**：| `fixdt(1,18,10)`（默认）| `single` | `double` | `fixdt(1,16,0)` | `<data type expression>` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,"OutputType","fixdt(1,16,0)")`

### **Show divide by zero port** — 是否显示 `divideByZero` 端口 `off`（默认）| `on`

*自 R2024b 起*

选中此参数以显示 **divideByZero** 端口。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `dbzPort` |
| **值**：| `0` (false)（默认）| `1` (true) |
| **Data Types:** | `logical` |

**Example:** `set_param(gcb,"dbzPort",1)`

### **Automatically select CORDIC maximum shift value based on input word length** — 基于输入字长自动选择 CORDIC 最大移位值 `on`（默认）| `off`

*自 R2024b 起*

基于输入字长自动选择 CORDIC 最大移位值。选中此参数时，默认 CORDIC `maximumShiftValue` 等于 `wl - 1`，其中 `wl = max(num.WordLength + ~issigned(num), den.WordLength + ~issigned(den))`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `autoMaximumShiftVal` |
| **值**：| `on`（默认）| `off` |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,"autoMaximumShiftVal","off")`

### **CORDIC maximum shift value** — 双曲向量化 CORDIC 的最大移位值 `wl - 1`（默认）| `10` | 正整数值标量

*自 R2024b 起*

双曲向量化 CORDIC 的最大移位值，指定为正整数值标量。此参数的默认值为 `wl - 1`，其中 `wl = max(num.WordLength + ~issigned(num), den.WordLength + ~issigned(den))`。

#### 依赖关系

要启用此参数，请清除 **Automatically select CORDIC maximum shift value based on input word length** 参数。

#### 提示

有关更多信息，请参阅 Customizable Pipelining。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `maximumShiftValue` |
| **值**：| `10`（默认）| 正整数值标量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,"maximumShiftValue","10")`

### **Number of iterations per pipeline register** — 每个流水线级执行的 CORDIC 迭代次数 `1`（默认）| 正整数值标量

*自 R2024b 起*

每个流水线级执行的 CORDIC 迭代次数，指定为正整数值标量。

有关更多信息，请参阅 Customizable Pipelining。有关此参数如何影响延迟和硬件资源利用率的更多信息和示例，请参阅 How to Interface with the Real Divide HDL Optimized Block 和 Hardware Resource Utilization。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `nIterPerReg` |
| **值**：| `1`（默认）| 正整数值标量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,"nIterPerReg","2")`

## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| *在 R2024b 中：**FlattenHierarchy*** | 从生成的 HDL 代码中移除 PWM Reference Generator 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持二进制点缩放的定点数据类型。

## 版本历史

**在 R2021a 中引入**

### R2024b：自定义流水线、改进的延迟和资源利用率、可选的除零端口

对 Real Divide HDL Optimized 模块进行了多项改进：

- 通过新的 **CORDIC maximum shift value** 和 **Number of iterations per pipeline register** 参数支持自定义流水线。
- 此模块的延迟已降低。延迟取决于指定的数据类型和流水线配置。有关更多信息，请参阅 How to Interface with the Real Divide HDL Optimized Block。
- HDL 资源利用率已进一步优化，需要更少的硬件资源。有关示例综合结果，请参阅 Hardware Resource Utilization。
- 添加了可选的 **divideByZero** 端口，当对应输出为除零的结果时输出标志。

### R2024b：支持无符号输出

Real Divide HDL Optimized 模块现在支持 **Output datatype** 参数的无符号数据类型。

## 描述

使用 CORDIC 算法将一个实数输入除以另一个实数输入，并生成优化的 HDL 代码

Real Divide HDL Optimized 模块输出实数标量 **num** 除以实数标量 **den** 的结果，即 **y** = **num**/**den**。
