---
type: simulink-block
title: 'Demux'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'demux'
documentation_source_path: '../simulink/slref/demux.html'
language: zh-CN
chinese_source: worker-translation
---

# Demux

## 端口

### 输入

### **Port\_1** — 接受非总线向量信号，以从 Simulink® 软件支持的任何非总线数据类型的实数或复数值中提取并输出信号

向量输入信号，Demux 模块从中选择标量信号或较小的向量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
### 输出

### **Port\_1** — 从输入向量信号中提取的输出信号，为非总线信号，具有 Simulink 软件支持的任何数据类型的实数或复数值

从输入向量中提取的输出信号。输出信号端口从上到下排列。有关各种模块方向下端口顺序的说明，请参阅 Identify Port Location on Rotated or Flipped Block。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

## 参数

### **Number of outputs** — 输出数量 2 （默认） | 标量 | 向量

指定输出数量，并可选地指定每个输出端口的维度。

该值可以是指定输出数量的标量，也可以是其元素指定模块输出端口宽度的向量。模块根据输入信号的大小和 **Number of outputs** 参数的值来确定其输出的大小。

如果为 **Number of outputs** 参数指定标量，并且所有输出端口都已连接，则当您在 Demux 模块输出侧附近绘制新的信号线时，软件会添加一个端口并更新 **Number of outputs** 参数。

对于宽度为 `n` 的输入向量，下表描述了模块的输出。

| 参数值 | 模块输出 | 示例和注释 |
| --- | --- | --- |
| `p = n` | `p` 个标量信号 | 如果输入是三元素向量并且您指定三个输出，则模块输出三个标量信号。 |
| `p > n` | 错误 | 不支持此值。 |
| `p < n`  `n mod p = 0` | `p` 个向量信号，每个具有 `n/p` 个元素 | 如果输入是六元素向量并且您指定三个输出，则模块输出三个二元素向量。 |
| `p < n`  `n mod p = m` | `m` 个向量信号，每个具有 `(n/p)+1` 个元素，以及 `p-m` 个具有 `n/p` 个元素的信号 | 如果输入是五元素向量并且您指定三个输出，则模块输出两个二元素向量信号和一个标量信号。 |
| `[p`1`p`2 `... p`m`]`  `p`1`+p`2`+...+p`m`=n`  `p`i`> 0` | `m` 个向量信号，宽度分别为 `p1`、`p2`、... `pm` | 如果输入是五元素向量并且您指定 `[3, 2]` 作为输出，则模块在一个端口上输出三个输入元素，在另一个端口上输出另外两个元素。 |
| 一个数组，其中 `m` 个元素中有一个或多个值为 `-1`，表示软件推断该元素的大小。例如，假设您有一个总宽度为 14 的四元素数组，并将参数指定为 `[p`1`p`2 `-1``p`4`]`。第三个元素（`-1` 元素）的值为 `14 -` `(p1 + p2 + p4)` | `m` 个向量信号 | 如果 `p`i 大于零，则对应输出的宽度为 `p`i。如果 `p`i 为 -1，则对应输出的宽度动态计算。 |
| `[p`1`p`2 `... p`m`]`  `p`1`+p`2`+...+p`m`!=n`  `p`i`= > 0` | 错误 | 不支持此值。 |

如果指定的输出数量小于输入元素的数量，则模块尽可能均匀地将元素分配到各输出上。

不支持指定非 double 值，例如 `single(3)`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Outputs` |
| **值**：| `'2'` （默认） | 带引号的标量 | 带引号的向量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'Outputs','4')`

### **Display option** — 显示的模块图标 `bar` （默认） | `none`

默认情况下，模块图标是模块前景色的实心条。要将图标显示为包含模块类型名称的框，请选择 `none`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `DisplayOption` |
| **值**：| `'bar'` （默认） | `'none'` |

**Example:** `set_param(gcb,'DisplayOption','none')`

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 之前引入**

## 描述

提取并输出虚拟向量信号的元素

Demux 模块提取输入向量信号的各分量并输出单独的信号。输出信号端口从上到下排列。
