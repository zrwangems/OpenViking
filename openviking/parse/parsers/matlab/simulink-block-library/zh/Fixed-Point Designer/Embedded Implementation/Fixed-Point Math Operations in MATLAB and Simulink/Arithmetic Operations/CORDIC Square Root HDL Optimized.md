---
type: simulink-block
title: 'CORDIC Square Root HDL Optimized'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Arithmetic Operations'
documentation_page: 'cordicsquareroothdloptimized'
documentation_source_path: 'ref/cordicsquareroothdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# CORDIC Square Root HDL Optimized

## 端口

### 输入

### **u** — 要取平方根的值，非负实值标量

要取平方根的值，指定为非负实值标量。

如果 **u** 是 fixed-point 或 scaled double 数据类型，则 **u** 必须使用二进制小数点定标。fixed-point 数据类型不支持斜率和偏置表示。代码生成仅支持二进制小数点定标的 fixed-point 数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为 Boolean 标量。此控制信号指示来自 **u** 输入端口的数据何时有效。当该值为 `1`（`true`）时，模块采集 **u** 输入端口处的值。当该值为 `0`（`false`）时，模块忽略输入样本。

**数据类型：** `Boolean`

### **restart** — 是否清除内部寄存器 `Boolean`

是否清除内部寄存器，指定为 Boolean 标量。当该值为 `1`（`true`）时，模块停止当前计算并清除所有内部寄存器。当该值为 `0`（`false`）且 **validIn** 值为 `1`（`true`）时，模块开始新的子帧。

**数据类型：** `Boolean`

### 输出

### **y** — 基于 CORDIC 的输入实值标量平方根近似值

基于 CORDIC 的输入实值标量平方根近似值，以实值标量形式返回。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean`

输出数据是否有效，以 Boolean 标量形式返回。此控制信号指示输出端口 **y** 处的数据何时有效。当该值为 `1`（`true`）时，输出数据有效。当该值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，从 **Prepare** 库中选择 **Property Inspector**。

### **根据输入字长自动选择 CORDIC 最大移位值** — 根据输入字长自动选择 CORDIC 最大移位值 `on`（默认） | `off`

根据输入字长自动选择 CORDIC 最大移位值。选中此参数时，默认 CORDIC 最大移位值取决于输入 **u** 的字长：

- 如果输入 **u** 是 fixed-point 或 scaled double，则默认值为字长减 1。
- 如果输入 **u** 是 `single`，则默认值为 `23`。
- 如果输入 **u** 是 `double`，则默认值为 `52`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `autoMaximumShiftVal` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `char` | `string` |

### **CORDIC 最大移位值** — 双曲向量化 CORDIC 的最大移位值 `10`（默认） | 正整数值标量

双曲向量化 CORDIC 的最大移位值，指定为正整数值标量。

#### 依赖关系

- 要启用此参数，请清除 **根据输入字长自动选择 CORDIC 最大移位值** 参数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `maximumShiftValue` |
| **值：** | `10`（默认） | 正整数值标量 |
| **数据类型：** | `char` | `string` |

### **每个流水线寄存器的迭代次数** — 在流水线级中执行的 CORDIC 迭代次数 `1`（默认） | 正整数值标量

在流水线级中执行的 CORDIC 迭代次数，指定为正整数值标量。有关详细信息，请参阅可自定义流水线。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `nIterPerReg` |
| **值：** | `1`（默认） | 正整数值标量 |
| **数据类型：** | `char` | `string` |

## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

代码生成仅支持二进制小数点定标的 fixed-point 数据类型。

## 版本历史

**在 R2024a 中引入**

## 描述

基于 CORDIC 的平方根近似

CORDIC Square Root HDL Optimized 模块返回 `u` 的平方根，该平方根使用针对 HDL 代码生成优化的基于 CORDIC 的实现计算。
