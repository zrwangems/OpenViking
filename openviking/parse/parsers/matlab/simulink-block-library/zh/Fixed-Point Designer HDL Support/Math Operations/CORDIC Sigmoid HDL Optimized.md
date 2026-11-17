---
type: simulink-block
title: 'CORDIC Sigmoid HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'cordicsigmoidhdloptimized'
documentation_source_path: '../fixedpoint/ref/cordicsigmoidhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# CORDIC Sigmoid HDL Optimized

## 端口

### 输入

### **u** — 输入数据 实值标量

输入数据，指定为实值标量。

如果 **u** 是定点或缩放双精度数据类型，则 **u** 必须使用二进制小数点缩放。定点数据类型不支持斜率-偏置表示。代码生成仅支持二进制小数点缩放的定点数据类型。

**数据类型：** `single` | `double` | `fixed point`

### **validIn** — 输入是否有效 `Boolean` 标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **u** 输入端口的数据何时有效。当此值为 `1`（`true`）时，模块捕获 **u** 输入端口上的值。当此值为 `0`（`false`）时，模块忽略输入采样。

**数据类型：** `Boolean`
### 输出

### **y** — `u` 的 Sigmoid 激活 标量

**u** 处值的 Sigmoid 激活，以标量形式返回。**y** 处的值是 **u** 的 Sigmoid 激活的基于 CORDIC 的近似。

当输入 **u** 为浮点时，输出 **y** 与输入具有相同的数据类型。当输入为定点数据类型时，输出与输入具有相同的字长，小数长度等于字长减 2。

**数据类型：** `single` | `double` | `fixed point`

### **validOut** — 输出数据是否有效 `Boolean`

输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1`（`true`）时，模块已成功计算输出 **y**。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

### **ready** — 模块是否就绪 `Boolean`

模块是否就绪，以布尔标量形式返回。此控制信号指示模块何时准备好接收新的输入数据。当此值为 1（`true`）且 **validIn** 值为 1（`true`）时，模块在下一个时钟周期接受输入数据。当此值为 0（`false`）时，模块在下一个时钟周期忽略输入数据。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

代码生成仅支持二进制小数点缩放的定点数据类型。

## 版本历史

**在 R2024a 中引入**

## 描述

计算基于 CORDIC 的 Sigmoid 激活并生成优化的 HDL 代码

CORDIC Sigmoid HDL Optimized 模块返回 *u* 的 Sigmoid 激活，使用针对 HDL 代码生成优化的基于 CORDIC 的实现进行计算。
