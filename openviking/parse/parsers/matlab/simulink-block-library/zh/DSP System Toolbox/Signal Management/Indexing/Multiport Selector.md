---
type: simulink-block
title: 'Multiport Selector'
family: 'signal-management'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Indexing'
documentation_page: 'multiportselector'
documentation_source_path: 'ref/multiportselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiport Selector

## 端口

### 输入

### **Input** — 输入向量 | 矩阵

将输入 *u* 指定为大小为 *M*×*N* 的向量或矩阵。该模块将未定向的长度为 *M* 的向量输入视为 *M*×1 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Output(s)** — 输入向量 | 矩阵的行或列子集

输入的行或列子集，传播到每个输出端口。**Indices to output** 数组中的每个元胞确定要传播到相应输出端口的输入行或列子集。**Indices to output** 数组中的元胞总数确定该模块上的输出端口数量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **Select** — 选择输入维度 `Rows`（默认） | `Columns`

选择输入维度为：

- `Rows` –– 该模块使用您指定的一维索引选择矩阵行，并且包含所选行上的所有元素。
- `Columns` –– 该模块使用您指定的一维索引选择矩阵列，并且包含所选列上的所有元素。

给定的输入行或列可以在任何输出中出现任意次数，或者完全不出现。

当索引引用输入中不存在的行或列时，该模块将使用您通过 **Invalid index** 参数指定的操作进行响应。

### **Indices to output** — 输出索引 `{ 4, [1:2 5], [7; 8], 10:-1:6 }`（默认） | 元胞数组

将传播到每个输出端口的行或列子集指定为元胞数组。第 *k* 个元胞包含一个一维索引表达式，指定要传播到第 *k* 个输出端口的输入行或列的子集。数组中的元胞总数确定该模块上的输出端口数量。

考虑以下 **Indices to output** 元胞数组。这是一个四元胞数组，要求该模块生成四个独立输出（每个位于不同的端口）。

```
{4,[1:2 5],[7;8],10:-1:6}
```

下表显示了当 **Select** = `Rows` 且输入维度为 *M*×*N* 时这些输出的维度。

| 元胞 | 表达式 | 描述 | 输出大小 |
| --- | --- | --- | --- |
| 1 | `4` | 输入的第 4 行 | 1×*N* |
| 2 | `[1:2 5]` | 输入的第 1、2 和 5 行 | 3×*N* |
| 3 | `[7;8]` | 输入的第 7 和 8 行 | 2×*N* |
| 4 | `10:-1:6` | 输入的第 10、9、8、7 和 6 行 | 5×*N* |

### **Invalid index** — 对无效索引采取的操作 `Clip Index`（默认） | `Clip and Warn` | `Generate Error`

指定当存在无效索引值时要采取的操作。您可以选择以下选项之一：

- `Clip index` — 该模块将索引裁剪到最接近的有效值，并且不发出警报。

  例如，如果该模块接收一个 `64`×`4` 输入，并且 **Select** 参数设置为 `Rows`，则该模块将索引 `72` 裁剪为 `64`。对于相同的输入，如果 **Select** 参数设置为 `Columns`，则该模块将索引 `72` 裁剪为 `4`。在两种情况下，该模块都将索引 `-2` 裁剪为 `1`。
- `Clip and warn` — 该模块将索引裁剪到最接近的有效值，并在 MATLAB® 命令行显示警告消息。
- `Generate error` — 该模块显示错误对话框并终止仿真。

## 所属库

DSP System Toolbox / Signal Management / Indexing DSP System Toolbox HDL Support / Signal Management

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**R2006a 之前引入**

## 描述

将输入行或列的任意子集分配到多个输出端口

Multiport Selector 模块从 *M*×*N* 输入矩阵 *u* 中提取行或列的多个子集，并将每个新的子矩阵传播到不同的输出端口。有关更多详细信息，请参阅 **Select** 和 **Indices to output** 参数的描述。
