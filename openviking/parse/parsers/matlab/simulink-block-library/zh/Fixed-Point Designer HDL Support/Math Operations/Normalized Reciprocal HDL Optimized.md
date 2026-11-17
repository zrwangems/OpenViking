---
type: simulink-block
title: 'Normalized Reciprocal HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'normalizedreciprocalhdloptimized'
documentation_source_path: '../fixedpoint/ref/normalizedreciprocalhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Normalized Reciprocal HDL Optimized

## 端口

### 输入

### **u** — 取归一化倒数的值 实数标量

取归一化倒数的值，指定为实数标量。

定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **u** 输入端口的数据何时有效。当此值为 `1`（`true`）时，模块捕获 **u** 输入端口处的值。当此值为 `0`（`false`）时，模块忽略输入采样。

**数据类型：** `Boolean`
### 输出

### **y** — 归一化倒数 标量

满足 0.5 < |**y**| ≤ 1 且 2**e****y** = 1/**u** 的归一化倒数，以标量形式返回。

- 如果 **u** 端口处的输入为字长 *w* 的有符号定点或缩放双精度数据类型，则 **y** 为字长 *w*、小数长度 *w* – 2 的有符号定点或缩放双精度数据类型。
- 如果 **u** 端口处的输入为字长 *w* 的无符号定点或缩放双精度数据类型，则 **y** 为字长 *w*、小数长度 *w* – 1 的无符号定点或缩放双精度数据类型。
- 如果 **u** 端口处的输入为 double，则 **y** 为 double。
- 如果 **u** 端口处的输入为 single，则 **y** 为 single。

**数据类型：** `single` | `double` | `fixed point`

### **e** — 指数 整数标量

满足 0.5 < |**y**| ≤ 1 且 2*e***y** = 1/**u** 的指数，以整数标量形式返回。

**数据类型：** `int32`

### **divideByZero** — 输出值是否为除零的结果 `Boolean` 标量

*自 R2024b 起*

**y** 和 **e** 输出端口处的值是否为除零操作的结果，以布尔标量形式返回。当此信号的值为 `1`（`true`）时，**y** 和 **e** 端口处对应的输出值为除零的结果。当此信号的值为 `0`（`false`）时，**y** 和 **e** 端口处对应的输出值为除以非零值的结果。

除数 **u** 是否为零，以布尔标量形式返回。当此信号的值为 `1`（`true`）时，**u** 端口处的输入为零，导致除零操作。当此信号的值为 `0`（`false`）时，**u** 端口处的输入为非零值。

#### 依赖关系

- 要启用此端口，请选中 **Show divide by zero port** 参数。

#### 提示

- 有关默认除零行为的描述，请参阅 Division by Zero Behavior。

**数据类型：** `Boolean`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1`（`true`）时，模块已成功计算 **y** 和 **e** 端口处的输出。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

## 参数

### **Show divide by zero port** — 是否显示 `divideByZero` 端口 `off`（默认）| `on`

*自 R2024b 起*

选中此参数以显示 **divideByZero** 端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dbzPort` |
| **值：** | `0`（false）（默认）| `1`（true） |
| **数据类型：** | `logical` |

**示例：** `set_param(gcb,"dbzPort",1)`

### **Automatically select CORDIC maximum shift value based on input word length** — 基于输入字长自动选择 CORDIC 最大移位值 `on`（默认）| `off`

*自 R2024b 起*

基于输入字长自动选择 CORDIC 最大移位值。选中此参数时，默认 CORDIC `maximumShiftValue` 等于 `wl - 1`，其中 `wl = u.WordLength + ~issigned(u)`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `autoMaximumShiftVal` |
| **值：** | `on`（默认）| `off` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"autoMaximumShiftVal","off")`

### **CORDIC maximum shift value** — 双曲向量 CORDIC 的最大移位值 `wl - 1`（默认）| `10` | 正整数值标量

*自 R2024b 起*

双曲向量 CORDIC 的最大移位值，指定为正整数值标量。此参数的默认值为 `wl - 1`，其中 `wl = u.WordLength + ~issigned(u)`。

#### 依赖关系

要启用此参数，请取消选中 **Automatically select CORDIC maximum shift value based on input word length** 参数。

#### 提示

有关详细信息，请参阅 Customizable Pipelining。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `maximumShiftValue` |
| **值：** | `10`（默认）| 正整数值标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"maximumShiftValue","10")`

### **Number of iterations per pipeline register** — 每个流水线级执行的 CORDIC 迭代次数 `1`（默认）| 正整数值标量

*自 R2024b 起*

每个流水线级执行的 CORDIC 迭代次数，指定为正整数值标量。

#### 提示

- 有关详细信息，请参阅 Customizable Pipelining。
- 有关此参数如何影响延迟和硬件资源利用率的更多信息和示例，请参阅 How to Interface with the Normalized Reciprocal HDL Optimized Block 和 Hardware Resource Utilization。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `nIterPerReg` |
| **值：** | `1`（默认）| 正整数值标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"nIterPerReg","2")`

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

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| *在 R2024b 中：**FlattenHierarchy*** | 从生成的 HDL 代码中移除 PWM Reference Generator 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2020a 中引入**

### R2024b：自定义流水线、改进的延迟和资源利用率、可选的除零端口

对 Normalized Reciprocal HDL Optimized 模块进行了多项改进：

- 通过新的 **CORDIC maximum shift value** 和 **Number of iterations per pipeline register** 参数支持自定义流水线。
- 此模块的延迟已减少。延迟取决于指定的数据类型和流水线配置。有关更多信息，请参阅 How to Interface with the Normalized Reciprocal HDL Optimized Block。
- HDL 资源利用率已进一步优化，所需硬件资源更少。有关示例综合结果，请参阅 Hardware Resource Utilization。
- 添加了可选的 **divideByZero** 端口，当对应输出为除零的结果时输出标志。

## 描述

使用 CORDIC 算法计算归一化倒数并生成优化的 HDL 代码

Normalized Reciprocal HDL Optimized 模块计算 **u** 的归一化倒数，以 **y** 和 **e** 形式返回，满足 0.5 < |**y**| ≤ 1 且 2*e***y** = 1/**u**。

- 如果 **u** = 0 且 **u** 为定点或缩放双精度数据类型，则 **y** = 1 – eps(**y**) 且 **e** = 2nextpow2(*w*) – *w* + *f*，其中 `w` 是 **u** 的字长，*f* 是 **u** 的小数长度。
- 如果 **u** = 0 且 **u** 为浮点数据类型，则 **y** = `Inf` 且 **e** = 1。
