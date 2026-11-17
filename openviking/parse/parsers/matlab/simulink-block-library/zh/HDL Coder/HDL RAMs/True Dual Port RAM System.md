---
type: simulink-block
title: 'True Dual Port RAM System'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'truedualportramsystem'
documentation_source_path: 'ref/truedualportramsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# True Dual Port RAM System

## 端口

### 输入

### **din\_a** — 写入数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we\_a** 处的信号为 `true` 时，可以将数据写入 RAM 存储位置。该值可以是整数，也可以是 `double`、`single` 或 `half` 类型。该值也可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

可以使用非虚拟总线和总线数组进行 HDL 代码生成。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **addr\_a** — 写入地址 `scalar` | `vector`

要写入的地址，指定为标量或向量。使用此地址将 **din\_a** 端口的数据写入 RAM。该值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。**addr\_a** 和 **addr\_b** 端口的值不能相同。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we\_a** — 写使能 `scalar` | `vector`

写使能，指定为标量或向量。当端口 **we\_a** 处的信号为 `true` 时，模块将 **din\_a** 端口的数据写入由 **addr\_a** 端口指定的存储位置。

**注意**

要使用列写入方法，数据类型必须是 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **din\_b** — 写入数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we\_b** 处的信号为 `true` 时，可以将数据写入 RAM 存储位置。该值可以是整数，也可以是 `double`、`single` 或 `half` 类型。该值也可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

可以使用非虚拟总线和总线数组进行 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **addr\_b** — 写入地址 `scalar` | `vector`

要写入的地址，指定为标量或向量。使用此地址将 **din\_b** 端口的数据写入 RAM。该值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。**addr\_a** 和 **addr\_b** 端口的值不能相同。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we\_b** — 写使能 `scalar` | `vector`

写使能，指定为标量或向量。当端口 **we\_b** 处的信号为 `true` 时，模块将 **din\_b** 端口的数据写入由 **addr\_b** 端口指定的存储位置。

**注意**

要使用列写入方法，数据类型必须是 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **dout\_a** — 写入数据输出 `scalar` | `vector`

写入数据输出，以标量或向量形式返回。模块从 **addr\_a** 端口指定的存储位置读取新的或旧的输出数据。

### **dout\_b** — 写入数据输出 `scalar` | `vector`

写入数据输出，以标量或向量形式返回。模块从 **addr\_b** 端口指定的存储位置读取新的或旧的数据。

## 参数

### 主要

### **RAM 类型** — RAM 类型 `True dual port`（默认）| `Simple dual port` | `Single port` | `Dual port` | `Simple tri port`

RAM 类型，指定为以下之一：

- `Single port` — 创建单端口 RAM，写入数据、地址和写使能作为输入，读数据作为输出。
- `Simple dual port` — 创建简单双端口 RAM，写入数据、写地址、写使能和读地址作为输入，来自读地址的数据作为输出。
- `Dual port` — 创建双端口 RAM，写入数据、写地址、写使能和读地址作为输入，来自读地址和写地址的数据作为输出。
- `True dual port` — 创建真双端口 RAM，写入数据 `a` 和 `b`，`a` 和 `b` 的写地址和读地址，以及写使能 `a` 和 `b` 作为输入，来自写地址 `a` 和 `b` 的数据作为输出。
- `Simple tri port` — 创建简单三端口 RAM，写入数据、写地址、写使能和读地址 `a` 和 `b` 作为输入，来自读地址 `a` 和 `b` 的数据作为输出。

代码生成器根据您指定的 RAM 类型动态配置模块的输入和输出端口。

#### 编程使用

|  |
| --- |
| **模块参数：**`RAMType` |
| **类型：**  字符向量、字符串 |
| **值：**  `Dual port` | `Simple dual port` | `Single port` | `True dual port` | `Simple tri port` |
| **默认：**  `True dual port` |

### **写输出行为** — 写输出行为 `New data`（默认）| `Old data`

选择写输出行为为 `New data` 或 `Old data`：

- `New data` — 将地址处的新数据发送到输出。
- `Old data` — 将地址处的旧数据发送到输出。

#### 编程使用

|  |
| --- |
| **模块参数：**`WriteOutputValue` |
| **类型：**  字符向量、字符串 |
| **值：**  `New data` | `Old data` |
| **默认：**  `New data` |

### **RAM 初始输出** — RAM 的初始仿真输出 `'0.0'`（默认）| `Scalar` | `Vector`

使用以下选项之一指定 RAM 的初始仿真输出：

- 标量值。
- 初始值与 RAM 字之间一一对应的向量。
- *n*×*m* 矩阵，初始值与 RAM 组中的 RAM 字之间一一对应，其中 *n* 表示 RAM 组的数量，*m* 表示 RAM 块中的地址位置数量，反之亦然。

#### 编程使用

|  |
| --- |
| **模块参数：**`RAMInitialValue` |
| **类型：**  整数、浮点数 |
| **值：**  `0.0` | `Scalar` | `Vector` |
| **默认：**  `0.0` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 高级

### **RAM 建模带一个周期延迟** — RAM 建模带一个周期延迟 `on`（默认）| `off`

*自 R2024b 起*

- 当您选择此参数时，RAM 将输入数据延迟一个周期后输出才能读取。使用此选项可确保模块与生成的 HDL 代码周期精确一致。
- 当您清除此参数时，RAM 立即读取并输出输入数据，但在 HDL 代码生成期间增加一个周期的延迟。当您指定过采样值或使用多速率模型时，使用此选项可利用时钟速率流水线。

#### 依赖关系

要启用此参数，请清除 **在目标硬件中使用异步读取功能** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：**`ModelRAMDelay` |
| **类型：**  字符向量、字符串 |
| **值：**  `'on'` | `'off'` |
| **默认：**  `'on'` |

### **Specify vector input access** — 将向量输入访问指定为串行或并行 `serial`（默认）| `parallel`

*自 R2025a 起*

- 当您将此参数设置为 `serial` 时，代码生成器从 RAM System 模块的向量输入推断并行 RAM 存储体。
- 当您将此参数设置为 `parallel` 时：

  - 在生成 HDL 代码时，代码生成器不会随向量输入的大小扩展 RAM 消耗量。相反，它从第一个索引开始，一次一个地对输入信号执行每个操作。启用串行访问允许您在以数据速率对向量输入进行建模时，以更快的时钟速率利用多周期 RAM 访问。
  - 如果 RAM System 模块存在于时钟速率流水线区域中，则序列化使用时钟速率实现，而不是本地多速率实现。

#### 依赖关系

要启用此参数，请清除 **Model RAM with one cycle of delay** 参数或启用 **Use asynchronous read feature in target hardware** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`VectorAccess` |
| **类型**：character vector, string |
| **值**：`'serial'` | `'parallel'` |
| **默认值**：`'serial'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL Architecture**

该模块具有 `MATLAB System` 架构，这表明该模块实现使用 `hdl.RAM` System object™。

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 块映射到目标 FPGA 上的 RAM 块。对于 UltraRAM 映射，**Initial output of RAM** 必须设置为 `0`。有关更多详细信息，请参阅 RAMDirective。 |

**Complex Data Support**

该模块支持复数信号的代码生成。

## 版本历史

**在 R2023b 中引入**

### R2024b: Use clock-rate pipelining

您可以在数据速率反馈环路内使用 True Dual Port RAM System 模块，并使用时钟速率流水线优化。此模型设计对于需要可编程或可调查找表而无需重新生成比特流的应用非常有用。

使用新参数 **Model RAM with one cycle of delay** 在仿真中对延迟进行建模。**Model RAM with one cycle of delay** 默认启用。

### R2024b: Parameter name changes

这些参数已重命名：

| Previous Name | Current Name |
| --- | --- |
| **指定 RAM 的类型** | **RAM 类型** |
| **指定写操作的输出数据** | **写输出的行为** |
| **指定 RAM 的初始值** | **RAM 的初始输出** |

### R2024b：在 RAM System 模块中使用列写操作按列写入 RAM

在此模块中，您可以使用列写入方法在指定内存地址处选择性地修改存储器的特定部分，而不更改其余部分。

### R2024b：为向量数据输入使用唯一初始值初始化 RAM 存储体

在此模块中，您可以使用唯一初始值初始化 RAM 存储体。

### R2024a：总线数组输入支持

该模块现在支持对指定为总线数组的输入数据进行 HDL 代码生成。

### R2024a：半精度和布尔数据支持

该模块现在支持对类型为 `Half` 或 `Boolean` 的输入数据进行 HDL 代码生成。

## 描述

支持同时读写操作的真双端口 RAM

真双端口 RAM 系统模块对一个真双端口 RAM 进行建模，该 RAM 通过两个读数据输出端口支持同时读写操作。该模块允许对不同存储器地址进行并发的读写操作。要配置此模块，请打开该模块并将 **Type of RAM** 参数设置为 `True dual port`。通过使用此模块，您可以：

- 通过在 **din**、**addr** 和 **we** 端口使用向量数据来创建并行 RAM 存储体。
- 使用 **Initial output of RAM** 参数为 RAM 指定初始值。
- 通过选择 **Model RAM with one cycle of delay** 参数来执行周期精确的读操作。
- 使用列写入方法写入被寻址存储器位置中的指定比特。

**注意**

在写操作期间，如果在同一地址同时发生读操作，则旧数据会出现在读输出端口。
