---
type: simulink-block
title: 'Divide by Constant HDL Optimized'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Arithmetic Operations'
documentation_page: 'dividebyconstanthdloptimized'
documentation_source_path: 'ref/dividebyconstanthdloptimized.html'
language: zh-CN
chinese_source: official
---

# Divide by Constant HDL Optimized

## 端口

### 输入

### **X** — 被除数 实数标量

被除数，指定为实数标量。

定点数据类型不支持斜率偏置表示。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **validIn** — 输入是否有效 布尔标量

输入是否有效，指定为布尔标量。此控制信号指示来自 **X** 输入端口的数据是否有效。当此值为 `1` (`true`) 时，此模块捕获 **X** 输入端口上的值。当此值为 `0` (`false`) 时，模块忽略输入样本。

**数据类型:** `Boolean`
### 输出

### **Y** — 除法和舍入运算的结果 标量

除法和舍入运算的结果，以标量形式返回。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **validOut** — 输出数据是否有效 布尔标量

指示输出数据是否有效，以布尔标量形式返回。当此控制信号的值为 `1` (`true`) 时，模块已成功计算输出 **Y**。当此值为 `0` (`false`) 时，输出数据无效。

**数据类型:** `Boolean`

## 参数

### **有理除法的分母** — 除数 10 (默认) | 标量

除数，指定为正实数值有限标量。

#### 编程用法

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型：**字符向量 |
| **值：**计算结果为正实数值有限定点或数值的 MATLAB® 表达式 |
| **数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认值：**`'10'` |

### **舍入方法** — 要使用的舍入方法 **向下** (默认) | **向上** | **最邻近值** | **零** | **收敛**

要使用的舍入方法，指定为以下值之一：

- **向下** - 朝负无穷方向舍入到最接近的整数。
- **向上** - 向正无穷方向舍入到最接近的整数。
- **最邻近值** - 舍入到最接近的整数。结值向正无穷方向舍入到最接近的整数。
- **零** - 向零方向舍入到最接近的整数。
- **收敛** - 舍入到最接近的整数。结值舍入到最接近的偶数。

#### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：** `'Floor'` | `'Ceiling'` | `'Nearest'` | `'Zero'` | `'Convergent'` |
| **默认值：**`'Floor'` |

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

定点数据类型不支持斜率偏置表示。

## 版本历史

**在 R2021a 中推出**

## 描述

将输入除以常量并舍入到整数并生成优化的 HDL 代码

Divide by Constant HDL Optimized 模块使用具有周期精确延迟的 HDL 优化架构，输出输入除以一个常量的结果，并使用指定的舍入方法将结果舍入为整数。

Divide by Constant HDL Optimized 模块使用的算法在功能上类似于 Granlund-Montgomery-Warren 方法。除法运算是通过与倒数相乘计算的，这通常有助于在嵌入式系统上实现更好的性能。
