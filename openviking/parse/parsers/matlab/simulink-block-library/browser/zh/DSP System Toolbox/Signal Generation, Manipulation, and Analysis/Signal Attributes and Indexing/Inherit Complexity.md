---
type: simulink-block
title: 'Inherit Complexity'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Attributes and Indexing'
documentation_page: 'inheritcomplexity'
documentation_source_path: 'ref/inheritcomplexity.html'
language: zh-CN
chinese_source: worker-translation
---

# Inherit Complexity

## 端口

### 输入

### **Data** — 数据输入 标量 | 向量 | *N*-D 数组

将数据输入指定为标量、向量或 *N*-D 数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Ref** — 参考输入 标量 | 向量 | *N*-D 数组

将参考输入指定为标量、向量或 *N*-D 数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes
### 输出

### **Output** — 输出 标量 | 向量 | *N*-D 数组

Inherit Complexity 模块的输出，以标量、向量或 *N*-D 数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

## 参数

未在 R2025b 中记录。

## 所属库

DSP System Toolbox / Signal Management / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

Inherit Complexity 模块支持为以下输入类型生成 HDL 代码：

- 数据和参考端口处的输入复/实性，例如 real 或 complex
- 向量、矩阵和总线输入

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

此模块具有以下 HDL 代码生成限制：

- 不支持 half-precision 数据类型。
- 不支持 non-virtual 总线输入。

## 版本历史

**在 R2006a 之前引入**

## 描述

更改输入的复/实性以匹配参考信号

Inherit Complexity 模块复制 **Data** 输入端口处的数据，并采用 **Ref** 端口处参考信号的复/实性。当数据输入为 real 且参考输入为 complex 时，该模块会将零值虚部分量 `0i` 追加到 **Data** 输入端口中数据的每个元素。

当数据输入为 complex 且参考输入为 real 时，该模块输出数据输入的实部分量。

当数据输入和参考输入均为 real，或数据输入和参考输入均为 complex 时，该模块按原样传播数据输入，不做任何更改。
