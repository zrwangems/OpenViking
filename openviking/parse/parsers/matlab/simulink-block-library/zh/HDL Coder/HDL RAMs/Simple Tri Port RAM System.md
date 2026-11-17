---
type: simulink-block
title: 'Simple Tri Port RAM System'
family: 'hdl-rams'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'simpletriportramsystem'
documentation_source_path: 'ref/simpletriportramsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Tri Port RAM System

## 端口

### 输入

### **din** — 要写入的数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we** 处的写使能信号为 `true` 时，您可以将数据写入 RAM 存储器位置。此值可以是 integer，也可以是 `double`、`single` 或 `half` 类型。此值也可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

您可以将非虚拟总线和总线数组用于 HDL 代码生成。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **wr_addr** — 要写入的地址 `scalar` | `vector`

要写入的地址，指定为标量或向量。当端口 **we** 处的信号为 `true` 时，使用此地址写入 RAM。此值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we** — 写使能 `scalar` | `Vector`

写使能，指定为标量或向量。当端口 **we** 处的信号为 `true` 时，模块将数据写入由 **wr_addr** 端口指定的存储器位置。

**注意**

要使用列写方法，数据类型必须是 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **rd_addr_a** — 要读取的地址 `scalar` | `vector`

要读取的地址，指定为标量或向量。使用此地址从 RAM 读取数据，数据在 **dout_a** 端口输出。此值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **rd_addr_b** — 要读取的地址 `scalar` | `vector`

要读取的地址，指定为标量或向量。使用此地址从 RAM 读取数据，数据在 **dout_b** 端口输出。此值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。

**数据类型：** `uint8` | `uint16` | `fixed point`
### 输出

### **dout_a** — 读取输出数据 `scalar` | `vector`

读取输出数据，以标量或向量形式返回。模块从 **rd_addr_a** 端口指定的存储器位置读取旧输出数据。

### **dout_b** — 读取输出数据 `scalar` | `vector`

读取输出数据，以标量或向量形式返回。模块从 **rd_addr_b** 端口指定的存储器位置读取旧输出数据。

## 参数

### 主要

### **Type of RAM** — RAM 类型 `Simple tri port` (默认) | `Simple dual port` | `Single port` | `True dual port` | `Dual port`

RAM 类型，指定为以下之一：

- `Single port` — 创建单端口 RAM，其中写入数据、地址和写使能数据作为输入，读取数据作为输出。
- `Simple dual port` — 创建简单双端口 RAM，其中写入数据、写地址、写使能和读地址作为输入，来自读地址的数据作为输出。
- `Dual port` — 创建双端口 RAM，其中写入数据、写地址、写使能和读地址作为输入，来自读地址和写地址的数据作为输出。
- `True dual port` — 创建真双端口 RAM，其中写入数据 `a` 和 `b`、`a` 和 `b` 的写地址和读地址、以及写使能 `a` 和 `b` 作为输入，来自写地址 `a` 和 `b` 的数据作为输出。
- `Simple tri port` — 创建简单三端口 RAM，其中写入数据、写地址、写使能、以及读地址 `a` 和 `b` 作为输入，来自读地址 `a` 和 `b` 的数据作为输出。

代码生成器根据您指定的 RAM 类型动态配置模块的输入和输出端口。

#### 程序化使用

|  |
| --- |
| **模块参数：**`RAMType` |
| **类型：**  character vector, string |
| **值：**  `Dual port` | `Simple dual port` | `Single port` | `True dual port` | `Simple tri port` |
| **默认：**  `Simple tri port` |

### **Use asynchronous read feature in target hardware** — 用于启用目标硬件中异步读取功能的选项 `off` (默认) | `on`

启用此选项可允许硬件立即执行读取指令，而无需等待一个周期。

#### 程序化使用

|  |
| --- |
| **模块参数：**`AsyncRead` |
| **类型：**  character vector, string |
| **值：**  `'on'` | `'off'` |
| **默认：**  `'off'` |

### **Initial output of RAM** — RAM 的初始仿真输出 `'0.0'` (默认) | `Scalar` | `Vector`

通过以下选项之一指定 RAM 的初始仿真输出：

- 一个标量值。
- 一个向量，其初始值与 RAM 字之间一一映射。
- 一个 *n* 乘 *m* 矩阵，其初始值与 RAM 存储体中的 RAM 字之间一一映射，其中
  *n* 表示 RAM 存储体的数量，*m* 表示 RAM 块中地址位置的数量，反之亦然。

#### 程序化使用

|  |
| --- |
| **模块参数：**`RAMInitialValue` |
| **类型：**  integer, floating point |
| **值：**  `0.0` | `Scalar` | `Vector` |
| **默认：**  `0.0` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 高级

### **Model RAM with one cycle of delay** — 使用一个周期延迟对 RAM 建模 `on` (默认) | `off`

*从 R2024b 开始*

- 选择此参数时，RAM 会将输入数据延迟一个周期，然后输出才能读取它。使用此选项可确保模块与生成的 HDL 代码周期精确一致。
- 清除此参数时，RAM 会立即读取并输出输入数据，但在 HDL 代码生成期间会增加一个周期的延迟。当您指定过采样值或处理多速率模型时，使用此选项可利用时钟速率流水线。

#### 依赖关系

要启用此参数，请清除 **Use asynchronous read feature in target hardware** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ModelRAMDelay` |
| **类型：**  character vector, string |
| **值：**  `'on'` | `'off'` |
| **默认：**  `'on'` |

### **Specify vector input access** — 将向量输入访问指定为串行或并行 `serial` (默认) | `parallel`

*从 R2025a 开始*

- 将此参数设置为 `serial` 时，代码生成器会从 RAM System 模块的向量输入推断并行 RAM 存储体。
- 将此参数设置为 `parallel` 时：

  - 生成 HDL 代码时，代码生成器不会随向量输入的大小扩展 RAM 消耗。相反，它会一次一个地应用输入信号的每个操作，从第一个索引开始。启用串行访问允许您在以数据速率使用向量输入建模时，以更快的时钟速率利用多周期 RAM 访问。
  - 如果 RAM System 模块存在于时钟速率流水线区域中，则序列化使用时钟速率实现，而不是本地多速率实现。

#### 依赖关系

要启用此参数，请清除 **Model RAM with one cycle of delay** 参数，或启用 **Use asynchronous read feature in target hardware** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**`VectorAccess` |
| **类型：**  character vector, string |
| **值：**  `'serial'` | `'parallel'` |
| **默认：**  `'serial'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

该模块具有 `MATLAB System` 架构，这表示模块实现使用 `hdl.RAM` System object™。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 块映射到目标 FPGA 上的 RAM 块。对于 UltraRAM 映射，**Initial output of RAM** 必须设置为 `0`。有关更多详细信息，请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2023b 中引入**

### R2024b：使用时钟速率流水线

您可以在数据速率反馈环内使用 Simple Tri Port RAM System 模块，并使用时钟速率流水线优化。此模型设计对于需要可编程或可调查找表而无需重新生成比特流的应用很有帮助。

使用新参数 **Model RAM with one cycle of delay** 在仿真中对延迟建模。**Model RAM with one cycle of delay** 默认启用，并且当 **Use asynchronous read feature in target hardware** 启用时禁用。

### R2024b：参数名称更改

这些参数已重命名：

| 先前名称 | 当前名称 |
| --- | --- |
| **Specify the type of RAM** | **Type of RAM** |
| **Enable asynchronous reads** | **Use asynchronous read feature in target hardware** |
| **Specify the RAM initial value** | **Initial output of RAM** |

### R2024b：在 RAM System 模块中使用列写操作按列写入 RAM

在此模块中，您可以使用列写方法选择性地修改存储器的特定部分，而不更改指定存储器地址处的其余部分。

### R2024b：为向量数据输入使用唯一初始值初始化 RAM 存储体

在此模块中，您可以使用唯一初始值初始化 RAM 存储体。

### R2024a：总线数组输入支持

该模块现在支持为指定为总线数组的输入数据生成 HDL 代码。

### R2024a：半精度和 Boolean 数据支持

该模块现在支持使用 `Half` 或 `Boolean` 类型的输入数据进行 HDL 代码生成。

## 描述

支持同时读写操作的简单三端口 RAM

Simple Tri Port RAM System 模块对简单三端口 RAM 进行建模，该 RAM 通过两个用于读取数据的输出端口支持同时读写操作。此模块允许并发访问不同的存储器地址。要配置此模块，请打开该模块并将 **Type of RAM** 参数设置为 `Simple tri port`。通过使用此模块，您可以：

- 通过在 **din**、**addr** 和 **we** 端口使用向量数据来创建并行 RAM 存储体。
- 使用 **Initial output of RAM** 参数指定 RAM 的初始值。
- 通过选择 **Use asynchronous read feature in target hardware** 参数在目标硬件中执行异步读取。
- 通过选择 **Model RAM with one cycle of delay** 参数执行周期精确的读取操作。
- 使用列写方法写入寻址存储器位置中的指定位。

**注意**

在写操作期间，如果在同一地址同时发生读操作，则旧数据会出现在读输出端口。
