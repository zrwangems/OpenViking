---
type: simulink-block
title: 'CORDIC Sigmoid HDL Optimized'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Activation Functions'
documentation_page: 'cordicsigmoidhdloptimized'
documentation_source_path: 'ref/cordicsigmoidhdloptimized.html'
language: zh-CN
chinese_source: official
---

# CORDIC Sigmoid HDL Optimized

## 端口

### 输入

### **u** — 输入数据 实数值标量

输入数据，指定为实数值标量。

如果 **u** 是定点或定标的双精度数据类型，则 **u** 必须使用二进制小数点定标。定点数据类型不支持斜率偏置表示。代码生成仅支持二进制小数点定标定点数据类型。

**数据类型:** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **u** 输入端口的数据是否有效。当此值为 `1` (`true`) 时，此模块捕获 **u** 输入端口上的值。当此值为 `0` (`false`) 时，模块忽略输入样本。

**数据类型:** `Boolean`
### 输出

### **y** — `u` 的 sigmoid 激活 标量

在 **u** 处的值的 sigmoid 激活，以标量形式返回。在 **y** 处的值是基于 CORDIC 的对 **u** 的 sigmoid 激活的逼近。

当输入 **u** 是浮点类型时，输出 **y** 具有与输入相同的数据类型。当输入为定点数据类型时，输出的字长与输入字长相同，小数长度比字长小 2。

**数据类型:** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean`

指示输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1` (`true`) 时，此模块已成功计算出输出 **y**。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型:** `Boolean`

### **ready** — 模块是否准备就绪 `Boolean`

指示模块是否准备就绪，以布尔标量形式返回。此控制信号指示模块是否已准备好接受新的输入数据。当此值为 1 (`true`) 并且 **validIn** 值为 1 (`true`) 时，此模块在下一个时钟周期中接受输入数据。当此值为 0 (`false`) 时，模块忽略下一个时钟周期中的输入数据。

**数据类型:** `Boolean`

## 参数

R2025b 官方文档未提供。

## 所属库

Fixed-Point Designer HDL Support / Math Operations

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

定点数据类型不支持斜率偏置表示。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**限制**

代码生成仅支持二进制小数点定标定点数据类型。

## 版本历史

**在 R2024a 中推出**

## 描述

计算基于 CORDIC 的 sigmoid 激活并生成优化的 HDL 代码

CORDIC Sigmoid HDL Optimized 模块返回 *u* 的 sigmoid 激活，使用针对 HDL 代码生成进行了优化的 CORDIC 实现进行计算。
