---
type: simulink-block
title: 'Demux'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'demux'
language: zh-CN
chinese_source: official
---

# Demux

## 端口

### 输入

### **Port\_1** — 接受要从中提取和输出信号的非总线向量信号 Simulink® 软件支持的任何非总线数据类型的实数或复数值

Demux 模块从中选择标量信号或更小向量的向量输入信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
### 输出

### **Port\_1** — 输出从输入向量信号中提取的信号 Simulink 软件支持的任何数据类型的实数或复数值的非总线信号

输出从输入向量中提取的信号。输出信号端口从上到下排列。有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

## 参数

### **输出数目** — 输出数目 2 (默认) | 标量 | 向量

指定输出数目以及每个输出端口的维度（可选）。

值可以是指定输出数目的标量，也可以是通过元素指定模块输出端口宽度的向量。模块根据输入信号的大小以及**输出数目**参数的值来确定输出的大小。

如果您为**输出数目**参数指定了标量，而所有输出端口都已连接，则当您在靠近 Demux 模块输出端的位置绘制新的信号线时，软件会添加一个端口并更新**输出数目**参数。

对于宽度为 `n` 的输入向量，下表描述模块输出的内容。

| 参数值 | 模块输出 | 示例和注释 |
| --- | --- | --- |
| `p = n` | `p` 个标量信号 | 如果输入是一个三元素向量，而您指定了三个输出，则模块将输出三个标量信号。 |
| `p > n` | 错误 | 不支持此值。 |
| `p < n`  `n mod p = 0` | `p` 个向量信号，每个信号具有 `n/p` 个元素 | 如果输入是一个六元素向量，而您指定了三个输出，则模块将输出三个二元素向量。 |
| `p < n`  `n mod p = m` | `m` 个向量信号，每个信号具有 `(n/p)+1` 个元素；以及 `p-m` 个信号，具有 `n/p`  个元素 | 如果输入是一个五元素向量，而您指定了三个输出，则模块将输出两个二元素向量信号和一个标量信号。 |
| `[p`1 `p`2 `... p`m`]`  `p`1`+p`2`+...+p`m`=n`  `p`i `> 0` | `m` 个向量信号，宽度分别为 `p1`、`p2`... `pm` | 如果输入是一个五元素向量，而您指定了 `[3, 2]` 作为输出，则模块将在一个端口输出三个输入元素，在另一个端口输出另外两个元素。 |
| 一个数组，其中的一个或多个 `m` 元素的值为 `-1`，该数组指定由该软件推断元素的大小。  例如，假设您有一个四元素数组，总宽度为 14，您将参数指定为 `[p`1 `p`2 `-1` `p`4`]`。  那么第三个元素（`-1` 元素）的值为 `14 -` `(p1 + p2 + p4)` | `m` 个向量信号 | 如果 `p`i 大于零，对应的输出宽度为 `p`i。如果 `p`i 为 -1，则会动态计算对应的输出宽度。 |
| `[p`1 `p`2 `... p`m`]`  `p`1`+p`2`+...+p`m`!=n`  `p`i `= > 0` | 错误 | 不支持此值。 |

如果您指定的输出数目少于输入元素的数目，则模块会尽可能将这些元素均匀地分配给各个输出。

不支持指定非双精度值，例如 `single(3)`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Outputs` |
| **值:** | `'2'` (默认) | scalar in quotes | vector in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,'Outputs','4')`

### **显示选项** — 显示的模块图标 **bar** (默认) | **无**

默认情况下，模块图标是一个填充了模块前景颜色的实心条形。要将图标显示为一个包含模块类型名称的框，请选择**无**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `DisplayOption` |
| **值:** | `'bar'` (默认) | `'none'` |

**示例:** `set_param(gcb,'DisplayOption','none')`

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 之前推出**

## 描述

提取并输出虚拟向量信号的元素

Demux 模块提取输入向量信号的分量，再将它们输出为单独的信号。输出信号端口从上到下排列。
