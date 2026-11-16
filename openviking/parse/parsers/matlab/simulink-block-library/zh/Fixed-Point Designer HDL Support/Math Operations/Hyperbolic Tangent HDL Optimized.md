---
type: simulink-block
title: 'Hyperbolic Tangent HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'hyperbolictangenthdloptimized'
documentation_source_path: '../fixedpoint/ref/hyperbolictangenthdloptimized.html'
language: zh-CN
chinese_source: official
---

# Hyperbolic Tangent HDL Optimized

## 端口

### 输入

### **x** — 以弧度为单位的角 有限实数标量

以弧度为单位的角，指定为有限实数标量。如果 **x** 是定点或定标的双精度数据类型，则 **x** 必须使用二进制小数点定标。定点数据类型不支持斜率偏置表示。

**数据类型:** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **x** 输入端口的数据是否有效。当此值为 `1` (`true`) 时，此模块捕获 **x** 输入端口上的值。当此值为 `0` (`false`) 时，模块忽略输入样本。

**数据类型:** `Boolean`
### 输出

### **y** — `x` 的双曲正切 标量

值在 **x** 处的双曲正切值，以标量形式返回。在 **y** 处的值是基于 CORDIC 的 **x** 双曲正切的逼近。当函数的输入是浮点数时，输出数据类型与输入数据类型相同。当输入为定点数据类型时，输出的字长与输入字长相同，小数长度比字长小 2。

**数据类型:** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean` 标量

指示输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1` (`true`) 时，此模块已成功计算出输出 **y**。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型:** `Boolean`

### **ready** — 模块是否准备就绪 `Boolean` 标量

指示模块是否准备就绪，以布尔标量形式返回。此控制信号指示模块是否已准备好接受新的输入数据。当此值为 1 (`true`) 并且 **validIn** 值为 1 (`true`) 时，此模块在下一个时间步中接受输入数据。当此值为 0 (`false`) 时，模块忽略下一个时间步中的输入数据。

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

仅支持定点数据类型。

## 版本历史

**在 R2020a 中推出**

## 描述

计算基于 CORDIC 的双曲正切并生成优化的 HDL 代码

Hyperbolic Tangent HDL Optimized 模块返回 *x* 的双曲正切值，使用针对 HDL 代码生成进行了优化的 CORDIC 实现进行计算。
