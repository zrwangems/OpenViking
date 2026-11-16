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

### **u** — 要取其归一化倒数的值，实数标量

要取其归一化倒数的值，指定为实数标量。

fixed-point 数据类型不支持斜率偏置表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 **u** 输入端口的数据何时有效。当此值为 `1` (`true`) 时，模块捕获 **u** 输入端口处的值。当此值为 `0` (`false`) 时，模块忽略输入样本。

**数据类型：** `Boolean`

### 输出

### **y** — 归一化倒数标量

满足 0.5 < |**y**| ≤ 1 且 2**e****y** =
1/**u** 的归一化倒数，返回为标量。

- 如果端口 **u** 处的输入是字长为 *w* 的 signed fixed-point 或 scaled-double
  数据类型，则 **y** 是字长为 *w* 且小数长度为 *w* – 2 的 signed
  fixed-point 或 scaled-double 数据类型。
- 如果端口 **u** 处的输入是字长为 *w* 的 unsigned fixed-point 或
  scaled-double 数据类型，则 **y** 是字长为 *w* 且小数长度为 *w* – 1 的
  unsigned fixed-point 或 scaled-double 数据类型。
- 如果端口 **u** 处的输入是 double，则 **y** 是 double。
- 如果端口 **u** 处的输入是 single，则 **y** 是 single。

**数据类型：** `single` | `double` | `fixed point`

### **e** — 指数整数标量

满足 0.5 < |**y**| ≤ 1 且 2*e***y** =
1/**u** 的指数，返回为整数标量。

**数据类型：** `int32`

### **divideByZero** — 输出值是否为除零结果 `Boolean` 标量

*自 R2024b 起*

**y** 和 **e** 输出端口处的值是否为除零运算的结果，返回为 Boolean 标量。当此信号的值为 `1` (`true`) 时，**y** 和 **e** 端口处的对应输出值是除零的结果。当此信号的值为 `0` (`false`) 时，**y** 和 **e** 端口处的对应输出值是非零值除法的结果。

除数 **u** 是否为零，返回为 Boolean 标量。当此信号的值为 `1` (`true`) 时，**u** 端口处的输入为零，导致除零运算。当此信号的值为 `0` (`false`) 时，**u** 端口处的输入为非零值。

#### 依赖项

- 要启用此端口，请选择 **显示除零端口** 参数。

#### 提示

- 有关默认除零行为的描述，请参阅 Division by Zero Behavior。

**数据类型：** `Boolean`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，返回为 Boolean 标量。当此控制信号的值为 `1` (`true`) 时，模块已成功计算端口 **y** 和 **e** 处的输出。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

## 参数

### **显示除零端口** — 是否显示 `divideByZero` 端口 `off`（默认） | `on`

*自 R2024b 起*

选择此参数以显示 **divideByZero** 端口。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dbzPort` |
| **值：** | `0` (false)（默认） | `1` (true) |
| **数据类型：** | `logical` |

**示例：** `set_param(gcb,"dbzPort",1)`

### **根据输入字长自动选择 CORDIC 最大移位值** — 根据输入字长自动选择 CORDIC 最大移位值 `on`（默认） | `off`

*自 R2024b 起*

根据输入字长自动选择 CORDIC 最大移位值。选中此参数时，默认 CORDIC `maximumShiftValue` 等于 `wl - 1`，其中 `wl = u.WordLength + ~issigned(u)`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `autoMaximumShiftVal` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"autoMaximumShiftVal","off")`

### **CORDIC 最大移位值** — 双曲向量化 CORDIC 的最大移位值 `wl - 1`（默认） | `10` | 正整数值标量

*自 R2024b 起*

双曲向量化 CORDIC 的最大移位值，指定为正整数值标量。此参数的默认值为 `wl - 1`，其中 `wl = u.WordLength + ~issigned(u)`。

#### 依赖项

要启用此参数，请取消选择 **根据输入字长自动选择 CORDIC 最大移位值** 参数。

#### 提示

有关更多信息，请参阅 Customizable Pipelining。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `maximumShiftValue` |
| **值：** | `10`（默认） | 正整数值标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"maximumShiftValue","10")`

### **每个流水线寄存器的迭代次数** — 每个流水线级执行的 CORDIC 迭代次数 `1`（默认） | 正整数值标量

*自 R2024b 起*

每个流水线级执行的 CORDIC 迭代次数，指定为正整数值标量。

#### 提示

- 有关更多信息，请参阅 Customizable Pipelining。
- 有关更多信息以及展示此参数如何影响延迟和硬件资源利用率的示例，请参阅 How to Interface with the Normalized Reciprocal HDL Optimized Block 和 Hardware Resource Utilization。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `nIterPerReg` |
| **值：** | `1`（默认） | 正整数值标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"nIterPerReg","2")`

## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

fixed-point 数据类型不支持斜率偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| *在 R2024b 中：**FlattenHierarchy*** | 从生成的 HDL 代码中移除 PWM Reference Generator 模块层次结构。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持 fixed-point 数据类型。

## 版本历史

**在 R2020a 中引入**

### R2024b：自定义流水线、改进的延迟和资源利用率、可选的除零端口

已对 Normalized Reciprocal HDL Optimized 模块进行了多项改进：

- 通过新的 **CORDIC 最大移位值** 和 **每个流水线寄存器的迭代次数** 参数支持自定义流水线。
- 此模块的延迟已降低。延迟取决于指定的数据
  类型和流水线配置。有关更多信息，请参阅 How to Interface with the Normalized Reciprocal HDL Optimized Block。
- HDL 资源利用率已进一步优化，以需要更少的硬件
  资源。有关示例综合结果，请参阅 Hardware Resource Utilization。
- 新增了一个可选的 **divideByZero** 端口，用于在相应
  输出是除零结果时输出标志。

## 描述

使用 CORDIC 算法计算归一化倒数并生成优化的 HDL 代码

Normalized Reciprocal HDL Optimized 模块计算 **u** 的归一化倒数，返回为 **y** 和 **e**，使得 0.5 < |**y**| ≤ 1 且 2*e***y** =
1/**u**。

- 如果 **u** = 0 且 **u** 是 fixed-point 或 scaled-double 数据类型，则 **y** = 1 – eps(**y**) 且 **e** =
  2nextpow2(*w*) – *w*
  + *f*，其中 `w` 是 **u** 的字长，且
  *f* 是 **u** 的小数长度。
- 如果 **u** = 0 且 **u** 是 floating-point 数据类型，则 **y** = `Inf` 且 **e** = 1。
