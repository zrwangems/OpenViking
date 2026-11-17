---
type: simulink-block
title: 'Inherit Complexity'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'inheritcomplexity'
documentation_source_path: '../dsp/ref/inheritcomplexity.html'
language: zh-CN
chinese_source: worker-translation
---

# Inherit Complexity

## 端口
```yaml
ports:
- name: Data
  summary: 数据输入 标量 | 向量 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Ref
  summary: 参考输入 标量 | 向量 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Output
  summary: 输出 标量 | 向量 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **Data** — 数据输入 标量 | 向量 | *N* 维数组

将数据输入指定为标量、向量或 *N* 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

### **Ref** — 参考输入 标量 | 向量 | *N* 维数组

将参考输入指定为标量、向量或 *N* 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — 输出 标量 | 向量 | *N* 维数组

Inherit Complexity 模块的输出，以标量、向量或 *N* 维数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
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

Inherit Complexity 模块支持以下输入类型的 HDL 代码生成：

- 数据和参考端口处的输入复数性，例如实数或复数
- 向量、矩阵和总线输入

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

此模块具有以下 HDL 代码生成限制：

- 不支持半精度数据类型。
- 不支持非虚拟总线输入。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入的复数性更改为与参考信号匹配

Inherit Complexity 模块复制 **Data** 输入端口处的数据，并采用 **Ref** 端口处参考信号的复数性。当数据输入为实数且参考输入为复数时，该模块会在 **Data** 输入端口处数据的每个元素后附加一个零值虚部分量 `0i`。

当数据输入为复数且参考输入为实数时，该模块输出数据输入的实部分量。

当数据输入和参考输入均为实数，或数据输入和参考输入均为复数时，该模块原样传播数据输入，不做任何更改。
