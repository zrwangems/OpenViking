---
type: simulink-block
title: 'True Dual Port RAM System'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / RAM and ROM Blocks'
documentation_page: 'truedualportramsystem'
documentation_source_path: 'ref/truedualportramsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# True Dual Port RAM System

## 端口

### 输入

### **din\_a** — 要写入的数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we\_a** 处的信号为 `true` 时，您可以将数据写入 RAM 内存位置。该值可以是整数，也可以是 `double`、`single` 或 `half` 类型。该值也可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

您可以在 HDL 代码生成中使用非虚拟总线和总线数组。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **addr\_a** — 要写入的地址 `scalar` | `vector`

要写入的地址，指定为标量或向量。使用此地址将数据从 **din\_a** 端口写入 RAM。该值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须介于 `2` 到 `31` 位之间。**addr\_a** 和 **addr\_b** 端口处的值不能相同。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we\_a** — 写使能 `scalar` | `vector`

写使能，指定为标量或向量。当端口 **we\_a** 处的信号为 `true` 时，模块将数据从 **din\_a** 端口写入由 **addr\_a** 端口指定的内存位置。

**注意**

要使用列写方法，数据类型必须为 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **din\_b** — 要写入的数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we\_b** 处的信号为 `true` 时，您可以将数据写入 RAM 内存位置。该值可以是整数，也可以是 `double`、`single` 或 `half` 类型。该值也可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

您可以在 HDL 代码生成中使用非虚拟总线和总线数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **addr\_b** — 要写入的地址 `scalar` | `vector`

要写入的地址，指定为标量或向量。使用此地址将数据从 **din\_b** 端口写入 RAM。该值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须介于 `2` 到 `31` 位之间。**addr\_a** 和 **addr\_b** 端口处的值不能相同。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we\_b** — 写使能 `scalar` | `vector`

写使能，指定为标量或向量。当端口 **we\_b** 处的信号为 `true` 时，模块将数据从 **din\_b** 端口写入由 **addr\_b** 端口指定的内存位置。

**注意**

要使用列写方法，数据类型必须为 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **dout\_a** — 写数据输出 `scalar` | `vector`

写数据输出，以标量或向量形式返回。模块从由 **addr\_a** 端口指定的内存位置读取新的或旧的输出数据。

### **dout\_b** — 写数据输出 `scalar` | `vector`

写数据输出，以标量或向量形式返回。模块从由 **addr\_b** 端口指定的内存位置读取新的或旧的数据。

## 参数

### 主要

### **RAM 类型** — RAM 类型 `True dual port` (default) | `Simple dual port` | `Single port` | `Dual port` | `Simple tri port`

RAM 类型，指定为以下之一：

- `Single port` — 创建单端口 RAM，其中写数据、地址和写使能数据作为输入，读数据作为输出。
- `Simple dual port` — 创建简单双端口 RAM，其中写数据、写地址、写使能和读地址作为输入，来自读地址的数据作为输出。
- `Dual port` — 创建双端口 RAM，其中写数据、写地址、写使能和读地址作为输入，来自读地址和写地址的数据作为输出。
- `True dual port` — 创建真双端口 RAM，其中写数据 `a` 和 `b`、`a` 和 `b` 的写地址和读地址、写使能 `a` 和 `b` 作为输入，来自写地址 `a` 和 `b` 的数据作为输出。
- `Simple tri port` — 创建简单三端口 RAM，其中写数据、写地址、写使能以及读地址 `a` 和 `b` 作为输入，来自读地址 `a` 和 `b` 的数据作为输出。

代码生成器会根据您指定的 RAM 类型动态配置模块的输入和输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`RAMType` |
| **类型：**  character vector, string |
| **值：**  `Dual port` | `Simple dual port` | `Single port` | `True dual port` | `Simple tri port` |
| **默认值：**  `True dual port` |

### **写输出行为** — 写输出行为 `New data` (default) | `Old data`

将写输出行为选择为 `New data` 或 `Old data`：

- `New data` — 在输出端发送该地址处的新数据。
- `Old data` — 在输出端发送该地址处的旧数据。

#### 编程用法

|  |
| --- |
| **模块参数：**`WriteOutputValue` |
| **类型：**  character vector, string |
| **值：**  `New data` | `Old data` |
| **默认值：**  `New data` |

### **RAM 的初始输出** — RAM 的初始仿真输出 `'0.0'` (default) | `Scalar` | `Vector`

使用以下选项之一指定 RAM 的初始仿真输出：

- 标量值。
- 向量，其中初始值与 RAM 字之间一一映射。
- *n*×*m* 矩阵，其中初始值与 RAM 组中的 RAM 字之间一一映射，*n* 表示 RAM 组的数量，*m* 表示 RAM 模块中的地址位置数量，反之亦然。

#### 编程用法

|  |
| --- |
| **模块参数：**`RAMInitialValue` |
| **类型：**  integer, floating point |
| **值：**  `0.0` | `Scalar` | `Vector` |
| **默认值：**  `0.0` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 高级

### **用一个周期延迟对 RAM 建模** — 用一个周期延迟对 RAM 建模 `on` (default) | `off`

*自 R2024b 起*

- 当您选择此参数时，RAM 会在输出可以读取输入数据之前将输入数据延迟一个周期。使用此选项可确保模块与生成的 HDL 代码周期精确一致。
- 当您清除此参数时，RAM 会立即读取并输出输入数据，但在 HDL 代码生成期间会增加一个周期的延迟。当您指定过采样值或处理多速率模型时，使用此选项可利用时钟速率流水线。

#### 依赖关系

要启用此参数，请清除 **在目标硬件中使用异步读取功能** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`ModelRAMDelay` |
| **类型：**  character vector, string |
| **值：**  `'on'` | `'off'` |
| **默认值：**  `'on'` |

### **指定向量输入访问** — 将向量输入访问指定为串行或并行 `serial` (default) | `parallel`

*自 R2025a 起*

- 当您将此参数设置为 `serial` 时，代码生成器会从到 RAM System 模块的向量输入推断并行 RAM 组。
- 当您将此参数设置为 `parallel` 时：

  - 在生成 HDL 代码时，代码生成器不会随向量输入的大小扩展 RAM 消耗量。相反，它会一次一个地应用输入信号的每个操作，从第一个索引开始。启用串行访问允许您在数据速率下使用向量输入进行建模时，以更快的时钟速率利用多周期 RAM 访问。
  - 如果 RAM System 模块存在于时钟速率流水线区域中，则序列化会使用时钟速率实现，而不是局部多速率实现。

#### 依赖关系

要启用此参数，请清除 **用一个周期延迟对 RAM 建模** 参数或启用 **在目标硬件中使用异步读取功能** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`VectorAccess` |
| **类型：**  character vector, string |
| **值：**  `'serial'` | `'parallel'` |
| **默认值：**  `'serial'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

此模块具有 `MATLAB System` 架构，这表示模块实现使用 `hdl.RAM` System object™。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 模块映射到目标 FPGA 上的 RAM 模块。对于 UltraRAM 映射，**RAM 的初始输出**必须设置为 `0`。有关详细信息，请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

## 版本历史

**在 R2023b 中引入**

### R2024b：使用时钟速率流水线

您可以在数据速率反馈环路内使用 True Dual Port RAM System 模块，并使用时钟速率流水线优化。对于需要可编程或可调查找表而无需重新生成比特流的应用，此模型设计非常有用。

使用新参数 **用一个周期延迟对 RAM 建模** 对仿真中的延迟进行建模。**用一个周期延迟对 RAM 建模** 默认启用。

### R2024b：参数名称变更

这些参数已重命名：

| 先前名称 | 当前名称 |
| --- | --- |
| **指定 RAM 类型** | **RAM 类型** |
| **指定写操作的输出数据** | **写输出行为** |
| **指定 RAM 初始值** | **RAM 的初始输出** |

### R2024b：在 RAM System 模块中使用列写操作按列写入 RAM

在此模块中，您可以使用列写方法，在指定内存地址处选择性地修改内存的特定部分，而不更改其余部分。

### R2024b：为向量数据输入使用唯一初始值初始化 RAM 组

在此模块中，您可以使用唯一初始值初始化 RAM 组。

### R2024a：总线数组输入支持

此模块现在支持对指定为总线数组的输入数据进行 HDL 代码生成。

### R2024a：半精度和布尔数据支持

此模块现在支持对类型为 `Half` 或 `Boolean` 的输入数据进行 HDL 代码生成。

## 描述

支持同时读写操作的真双端口 RAM

True Dual Port RAM System 模块对真双端口 RAM 进行建模，该 RAM 通过两个读数据输出端口支持同时读写操作。此模块允许对不同内存地址进行并发读写访问。要配置此模块，请打开该模块，并将 **RAM 类型** 参数设置为 `True dual port`。通过使用此模块，您可以：

- 通过在 **din**、**addr** 和 **we** 端口使用向量数据来创建并行 RAM 组。
- 使用 **RAM 的初始输出** 参数为 RAM 指定初始值。
- 通过选择 **用一个周期延迟对 RAM 建模** 参数来执行周期精确的读操作。
- 使用列写方法写入寻址内存位置中的指定位。

**注意**

在写操作期间，如果读操作同时发生在同一地址，则读输出端口会出现旧数据。
