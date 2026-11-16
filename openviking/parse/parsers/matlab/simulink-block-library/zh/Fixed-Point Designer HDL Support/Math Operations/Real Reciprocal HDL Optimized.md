---
type: simulink-block
title: 'Real Reciprocal HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'realreciprocalhdloptimized'
documentation_source_path: '../fixedpoint/ref/realreciprocalhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Reciprocal HDL Optimized

## 端口

### 输入

### **u** — 要取倒数的值 标量 | 向量 | 矩阵

要取倒数的值，指定为实数值标量、向量或矩阵。

定点数据类型不支持 slope-bias 表示。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 **u** 输入端口的数据何时有效。当此值为 `1` (`true`) 时，模块捕获 **u** 输入端口处的值。当此值为 `0` (`false`) 时，模块忽略输入采样。

**数据类型：** `Boolean`

### 输出

### **y** — 倒数实数标量

倒数，返回为实数标量，其数据类型由 **输出数据类型** 参数指定。

**数据类型：** `single` | `double` | `fixed point`

### **divideByZero** — 输出处的值是否为除以零的结果 `Boolean` 标量

*自 R2024b*

**y** 输出端口处的值是否为除以零操作的结果，作为 Boolean 标量返回。当此信号值为 `1` (`true`) 时，**y** 端口处的对应输出值是除以零的结果。当此信号值为 `0` (`false`) 时，**y** 端口处的对应输出值是除以非零值的结果。

有关默认除以零行为的描述，请参阅 Division by Zero Behavior。

#### 依赖项

要启用此端口，请选择 **显示除以零端口** 参数。

**数据类型：** `Boolean`

### **validOut** — 输出数据是否有效 `Boolean` 标量

输出数据是否有效，作为 Boolean 标量返回。当此控制信号值为 `1` (`true`) 时，模块已成功计算端口 **y** 处的输出。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型：** `Boolean`

## 参数

### **输出数据类型** — 输出的数据类型 `fixdt(1,18,10)`（默认） | `single` | `double` | `fixdt(1,16,0)` | `<data type expression>`

输出 **y** 的数据类型，指定为 `fixdt(1,18,10)`、`single`、`double`、`fixdt(1,16,0)`，或用户指定的数据类型表达式。类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

*在 R2024b 中：此参数支持无符号数据类型。*

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputType` |
| **值：** | `fixdt(1,18,10)`（默认） | `single` | `double` | `fixdt(1,16,0)` | `<data type expression>` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"OutputType","fixdt(1,16,0)")`

### **显示除以零端口** — 是否显示 `divideByZero` 端口 `off`（默认） | `on`

*自 R2024b*

选择此参数以显示 **divideByZero** 端口。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dbzPort` |
| **值：** | `0`（false）（默认） | `1`（true） |
| **数据类型：** | `logical` |

**示例：** `set_param(gcb,"dbzPort",1)`

### **根据输入字长自动选择 CORDIC 最大移位值** — 根据输入字长自动选择 CORDIC 最大移位值 `on`（默认） | `off`

*自 R2024b*

根据输入字长自动选择 CORDIC 最大移位值。选中此参数时，默认 CORDIC `maximumShiftValue` 等于 `wl - 1`，其中 `wl = u.WordLength + ~issigned(u)`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `autoMaximumShiftVal` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"autoMaximumShiftVal","off")`

### **CORDIC 最大移位值** — 双曲向量化 CORDIC 的最大移位值 `wl - 1`（默认） | `10` | 正整数值标量

*自 R2024b*

双曲向量化 CORDIC 的最大移位值，指定为正整数值标量。此参数的默认值为 `wl - 1`，其中 `wl = u.WordLength + ~issigned(u)`。

#### 依赖项

要启用此参数，请清除 **根据输入字长自动选择 CORDIC 最大移位值** 参数。

#### 提示

有关详细信息，请参阅 Customizable Pipelining。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `maximumShiftValue` |
| **值：** | `10`（默认） | 正整数值标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"maximumShiftValue","10")`

### **每个流水线寄存器的迭代次数** — 每个流水线级执行的 CORDIC 迭代次数 `1`（默认） | 正整数值标量

*自 R2024b*

每个流水线级执行的 CORDIC 迭代次数，指定为正整数值标量。

有关详细信息，请参阅 Customizable Pipelining。有关此参数如何影响延迟和硬件资源利用率的更多信息和示例，请参阅 How to Interface with the Real Reciprocal HDL Optimized Block 和 Hardware Resource Utilization。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `nIterPerReg` |
| **值：** | `1`（默认） | 正整数值标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,"nIterPerReg","2")`

## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持 slope-bias 表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| *在 R2024b 中：**FlattenHierarchy*** | 从生成的 HDL 代码中删除 PWM Reference Generator 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

仅支持定点数据类型。

## 版本历史

**在 R2021a 中引入**

### R2024b：自定义流水线、改进的延迟和资源利用率、可选的除以零端口

已对 Real Reciprocal HDL Optimized 模块进行多项改进：

- 通过新的 **CORDIC 最大移位值** 和 **每个流水线寄存器的迭代次数** 参数支持自定义流水线。
- 此模块的延迟已降低。延迟取决于指定的数据类型和流水线配置。有关详细信息，请参阅 How to Interface with the Real Reciprocal HDL Optimized Block。
- HDL 资源利用率已进一步优化，需要更少的硬件资源。有关示例综合结果，请参阅 Hardware Resource Utilization。
- 添加了可选的 **divideByZero** 端口，当相应输出是除以零的结果时输出标志。

### R2024b：支持无符号输出

Real Reciprocal HDL Optimized 模块现在支持用于 **输出数据类型** 参数的无符号数据类型。

## 描述

使用 CORDIC 算法计算倒数并生成优化的 HDL 代码

Real Reciprocal HDL Optimized 模块计算 1/**u**，其中 **u** 是实数标量。
