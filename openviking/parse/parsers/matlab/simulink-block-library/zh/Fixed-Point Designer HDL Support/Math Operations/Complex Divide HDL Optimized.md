---
type: simulink-block
title: 'Complex Divide HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'complexdividehdloptimized'
documentation_source_path: '../fixedpoint/ref/complexdividehdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Divide HDL Optimized

## 端口

### 输入

### **num** — 分子 标量 | 向量 | 矩阵

分子，指定为标量、向量或矩阵。**num** 和 **den** 必须具有相同的维度。

定点数据类型不支持斜率偏置表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **den** — 分母 标量 | 向量 | 矩阵

分母，指定为标量、向量或矩阵。**num** 和 **den** 必须具有相同的维度。

定点数据类型不支持斜率偏置表示。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 **num** 和 **den** 输入端口的数据何时有效。当此值为 `1` (`true`) 时，模块捕获输入端口 **num** 和 **den** 处的值。当此值为 `0` (`false`) 时，模块忽略输入样本。

**数据类型：** `Boolean`
### 输出

### **y** — 通过将输入相除计算得到的输出 复标量

通过将 **num** 除以 **den** 计算得到的输出，使得 **y** = **num**/**den**，以复标量形式返回。

#### 提示

输出端口 **y** 的数据类型由 **输出数据类型** 参数指定。

**数据类型：** `single` | `double` | `fixed point`

### **divideByZero** — 输出处的值是否为除零的结果 `Boolean` 标量

*自 R2024b 起*

**y** 输出端口处的值是否为除零操作的结果，以 Boolean 标量形式返回。当此信号的值为 `1` (`true`) 时，**y** 端口处对应的输出值是除零的结果。当此信号的值为 `0` (`false`) 时，**y** 端口处对应的输出值是非零值除法的结果。

有关默认除零行为的说明，请参阅“除零行为”。

#### 依赖关系

要启用此端口，请选择 **显示除零端口** 参数。

**数据类型：** `Boolean`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，以 Boolean 标量形式返回。当此控制信号的值为 `1` (`true`) 时，模块已成功计算端口 **y** 处的输出。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

## 参数

### **输出数据类型** — 输出的数据类型 `fixdt(1,18,10)`（默认） | `single` | `double` | `fixdt(1,16,0)` | `<数据类型表达式>`

输出 **y** 的数据类型，指定为 `fixdt(1,18,10)`、`single`、`double`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputType` |
| **值：** | `fixdt(1,18,10)`（默认） | `single` | `double` | `fixdt(1,16,0)` | `<数据类型表达式>` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"OutputType","fixdt(1,16,0)")`

### **显示除零端口** — 是否显示 `divideByZero` 端口 `off`（默认） | `on`

*自 R2024b 起*

选择此参数以显示 **divideByZero** 端口。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dbzPort` |
| **值：** | `0` (false)（默认） | `1` (true) |
| **数据类型：** | `logical` |

**示例：** `set_param(gcb,"dbzPort",1)`

### **基于输入字长自动选择 CORDIC 最大移位值** — 基于输入字长自动选择 CORDIC 最大移位值 `on`（默认） | `off`

*自 R2024b 起*

基于输入字长自动选择 CORDIC 最大移位值。选择此参数后，默认 CORDIC `maximumShiftValue` 等于 `wl - 1`，其中 `wl = max(num.WordLength + ~issigned(num), den.WordLength + ~issigned(den))`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `autoMaximumShiftVal` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"autoMaximumShiftVal","off")`

### **CORDIC 最大移位值** — 双曲向量化 CORDIC 的最大移位值 `wl - 1`（默认） | `10` | 正整数标量

*自 R2024b 起*

双曲向量化 CORDIC 的最大移位值，指定为正整数标量。此参数的默认值为 `wl - 1`，其中 `wl = max(num.WordLength + ~issigned(num), den.WordLength + ~issigned(den))`。

#### 依赖关系

要启用此参数，请清除 **基于输入字长自动选择 CORDIC 最大移位值** 参数。

#### 提示

有关更多信息，请参阅可自定义流水线。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `maximumShiftValue` |
| **值：** | `10`（默认） | 正整数标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"maximumShiftValue","10")`

### **每个流水线寄存器的迭代次数** — 每个流水线级要执行的 CORDIC 迭代次数 `1`（默认） | 正整数标量

*自 R2024b 起*

每个流水线级要执行的 CORDIC 迭代次数，指定为正整数标量。

有关更多信息，请参阅可自定义流水线。有关更多信息和示例（展示此参数如何影响延迟和硬件资源利用率），请参阅如何与 Complex Divide HDL Optimized 模块连接以及硬件资源利用率。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `nIterPerReg` |
| **值：** | `1`（默认） | 正整数标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"nIterPerReg","2")`

## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供会影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| *在 R2024b 中：**FlattenHierarchy*** | 从生成的 HDL 代码中移除 PWM Reference Generator 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持二进制小数点定标的定点数据类型。

## 版本历史

**在 R2021a 中引入**

### R2024b：自定义流水线、改进的延迟和资源利用率、可选的除零端口

已对 Complex Divide HDL Optimized 模块进行多项改进：

- 通过新的 **CORDIC 最大移位值** 和 **每个流水线寄存器的迭代次数** 参数支持自定义流水线。
- 此模块的延迟已降低。延迟取决于指定的数据类型和流水线配置。有关更多信息，请参阅如何与 Complex Divide HDL Optimized 模块连接。
- HDL 资源利用率已进一步优化，以减少所需的硬件资源。有关示例综合结果，请参阅硬件资源利用率。
- 添加了可选的 **divideByZero** 端口，用于在对应输出为除零结果时输出标志。

## 描述

使用 CORDIC 算法将一个输入除以另一个输入，并生成优化的 HDL 代码

Complex Divide HDL Optimized 模块输出标量 **num** 除以标量 **den** 的结果，使得 **y** = **num**/**den**。
