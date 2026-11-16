---
type: simulink-block
title: 'HDL FIFO'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / RAM and ROM Blocks'
documentation_page: 'hdlfifo'
documentation_source_path: 'ref/hdlfifo.html'
language: zh-CN
chinese_source: worker-translation
---

# HDL FIFO

## 端口

### 输入

### **In** — 数据输入信号 `scalar`

到 FIFO 模块的数据输入信号。当你将数据写入 FIFO 时，最新的数据被压入 FIFO 寄存器的末尾。该模块将后续数据条目压入该条目的下方。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

### **Push** — 写控制信号 `scalar`

当该端口接收到值 `1` 时，模块将 `In` 端口上的输入压入 FIFO 寄存器的末尾。

**数据类型：** `Boolean`

### **Pop** — 读控制信号 `scalar`

当该端口接收到值 `1` 时，模块从 FIFO 寄存器中弹出第一个元素，并使 `Out` 端口保持在该值。

**数据类型：** `Boolean`

**注意**

如果在同一时间步内触发两个或更多控制输入端口，则先执行弹出操作，然后执行压入操作。

### **rst** — 复位控制信号 `scalar`

当复位端口接收到值 `1` 时，它会复位 HDL FIFO 模块的 Empty、Full 和 Num 输出。

#### 依赖关系

要启用此端口，请选择模块参数 **局部复位端口**。

**数据类型：** `Boolean`
### 输出

### **Out** — 数据输出信号 `scalar`

来自 FIFO 模块的数据输出信号。当你从 FIFO 读取数据时，最先写入 FIFO 寄存器的数据从 FIFO 中取出，并保持在输出端。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是

### **Empty** — 数据输出信号 `scalar`

来自 FIFO 的控制信号输出，当 FIFO 寄存器为空且不包含数据条目时变为 `1`。

#### 依赖关系

要启用此端口，必须选中 **显示空寄存器指示端口 (Empty)**。

**数据类型：** `Boolean`

### **Full** — 数据输出信号 `scalar`

来自 FIFO 的控制信号输出，当 FIFO 寄存器已满且无法再接收更多数据条目时变为 `1`。

#### 依赖关系

要启用此端口，必须选中 **显示满寄存器指示端口 (Full)**。

**数据类型：** `Boolean`

### **Num** — 条目数 `scalar`

当前位于 FIFO 寄存器内的数据条目数。对于你写入 FIFO 的每个数据，**Num** 递增 `1`。对于你从 FIFO 读取的每个数据，**Num** 递减 `1`。

#### 依赖关系

要启用此端口，必须选中 **显示寄存器条目数端口 (Num)**。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **寄存器大小** — 条目数 `10`（默认值）

指定 FIFO 寄存器可以容纳的条目数。**寄存器大小**的默认值为 `10`。**寄存器大小**的最小值为 `4`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fifo_size` |
| **类型：** 字符向量 |
| **值：** 大于或等于四的整数 |
| **默认：** `'10'` |

### **模式** — 操作模式 `'Classic'`（默认值）| `'FWFT'`

指定 FIFO 的操作模式。默认情况下，**模式**设置为 `Classic`。你会看到模块图标显示 `Classic FIFO`。你可以将**模式**更改为 `FWFT`。当你更改**模式**时，模块图标显示 `FWFT FIFO`。通过使用 `FWFT` 模式，你可以在不发出读请求的情况下前瞻并查看写入 FIFO 寄存器的第一个字。当你使用 AXI4-Stream 接口施加背压时，FWFT 模式尤其有用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mode` |
| **类型：** 字符向量 |
| **值：** `'Classic'` | `'FWFT'` | |
| **默认：** `'Classic'` |

### **输出采样时间与输入采样时间之比** — 采样率之比 `1`（默认值）

指定输出采样时间与输入采样时间之比。默认比值为 `1`，这意味着输入 `In` 和 `Push`，以及输出 `Out` 和 `Pop`，以相同的采样率运行。输入和输出可以以不同的采样时间运行。请使用正整数或 `1/N`，其中 `N` 为正整数。例如，如果你输入 `1/2`，则输出采样时间是输入采样时间的一半，或者说输出运行得更快。`Full`、`Empty` 和 `Num` 信号以较快的速率运行。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ratio` |
| **类型：** 字符向量 |
| **值：** 大于或等于一的整数 |
| **默认：** `'1'` |

### **压入满寄存器** — 溢出情况 `'Warning'`（默认值）| `'Ignore'` | `'Error'`

指定当你向已满的 FIFO 写入时，希望模块如何响应。默认值为 `Warning`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `push_msg` |
| **类型：** 字符向量 |
| **值：** `'Warning'` | `'Ignore'` | `'Error'` |
| **默认：** `'Warning'` |

### **弹出空寄存器** — 下溢情况 `'Warning'`（默认值）| `'Ignore'` | `'Error'`

指定当你从空 FIFO 读取时，希望模块如何响应。默认值为 `Warning`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pop_msg` |
| **类型：** 字符向量 |
| **值：** `'Warning'` | `'Ignore'` | `'Error'` |
| **默认：** `'Warning'` |

### **显示空寄存器指示端口 (Empty)** — 可选空端口 on（默认值）| off

指定是否启用 `Empty` 输出端口。当 FIFO 寄存器为空时，该端口输出 `1`；当 FIFO 包含一个或多个数据条目时，输出 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `show_empty` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **显示满寄存器指示端口 (Full)** — 可选满端口 on（默认值）| off

指定是否启用 `Full` 输出端口。当 FIFO 寄存器已满时，该端口输出 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `show_full` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **显示寄存器条目数端口 (Num)** — 可选 num 端口 on（默认值）| off

指定是否启用 `Num` 输出端口。该端口输出 FIFO 队列中当前可用的数据条目数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `show_num` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **局部复位端口** — 可选复位端口 off（默认值）| on

指定是否插入额外的 `rst` 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rst_port` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **常规** | |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 模块映射到目标 FPGA 上的存储器块，例如分布式 RAM、块 RAM 或 UltraRAM。默认值为 `empty string`。另请参阅 RAMDirective。 |

## 版本历史

**在 R2014a 中引入**

### R2024a：半精度和布尔数据支持

该模块现在支持使用 `Half` 或 `Boolean` 类型的输入数据进行 HDL 代码生成。

## 描述

将输入采样序列存储在先入先出 (FIFO) 寄存器中

HDL FIFO 模块将输入采样序列存储在先入先出 (FIFO) 寄存器中。最先写入 FIFO 寄存器的数据最先输出。该模块在功能和行为方面与硬件平台中的 FIFO 单元类似。

HDL FIFO 模块内部使用 Simple Dual Port RAM System 模块。你可以使用 HDL FIFO 模块生成可映射到大多数 FPGA 中 RAM 的 HDL 代码。
