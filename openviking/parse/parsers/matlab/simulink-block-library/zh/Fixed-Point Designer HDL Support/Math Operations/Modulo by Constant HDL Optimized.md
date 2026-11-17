---
type: simulink-block
title: 'Modulo by Constant HDL Optimized'
family: 'fixed-point-designer-hdl-support'
product_id: 'fixed-point-designer-hdl-support'
product_name: 'Fixed-Point Designer HDL Support'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'modulobyconstanthdloptimized'
documentation_source_path: '../fixedpoint/ref/modulobyconstanthdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Modulo by Constant HDL Optimized

## 端口

### 输入

### **X** — 被除数 实数值标量 | 向量 | 矩阵 | 多维数组

被除数，指定为实数值标量、向量、矩阵或多维数组。

如果 **X** 为定点数据类型，则必须使用二进制小数点定标。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **validIn** — 输入是否有效 布尔标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **X** 输入端口的数据何时有效。当此值为 `1`（`true`）时，模块采集 **X** 输入端口上的值。当此值为 `0`（`false`）时，模块忽略输入采样。

**数据类型：** `Boolean`
### 输出

### **Y** — 取模运算的结果 标量 | 向量 | 矩阵 | 多维数组

取模运算的结果，以标量、向量、矩阵或多维数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

### **validOut** — 输出数据是否有效 布尔标量

输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1`（`true`）时，模块已成功计算输出 **Y**。当此值为 `0`（`false`）时，输出数据无效。

**数据类型：** `Boolean`

## 参数

### **Denominator** — 除数 10（默认）| 实数值标量 | 向量 | 矩阵 | 多维数组

用于取模运算的除数，指定为正的实数值有限标量、向量、矩阵或多维数组。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Denominator` |
| **类型：** 字符向量 |
| **值：** 求值为正的实数值有限定点或数值的 MATLAB® 表达式 |
| **数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认值：** `'10'` |

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

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

定点数据类型不支持斜率-偏置表示。

## 版本历史

**在 R2021a 中引入**

### R2024a：Modulo by Constant HDL Optimized 模块的延迟降低

Modulo by Constant HDL Optimized 模块的延迟已从 9 个时钟周期降低到 4 个时钟周期。

### R2023b：支持向量和矩阵输入

Modulo by Constant HDL Optimized 模块现在支持向量和矩阵输入。

### R2023b：Modulo by Consant 模块支持在 For Each Subsystem 模块中使用

Modulo by Constant HDL Optimized 模块支持在 For Each Subsystem 模块内部使用。

## 描述

使用常量除数执行取模运算并生成优化的 HDL 代码

Modulo by Constant HDL Optimized 模块使用具有周期精确延迟的 HDL 优化架构，以常量除数执行取模运算（除法后的余数）。

Modulo by Constant 模块使用的算法在功能上类似于 Barrett Reduction。除法运算通过乘以逆元来计算，这通常在嵌入式系统上具有更好的性能。
