---
type: simulink-block
title: 'Single Port RAM System'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'singleportramsystem'
documentation_source_path: 'ref/singleportramsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Single Port RAM System

## 端口

### 输入

### **din** — 要写入的数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we** 处的写使能信号为 `true` 时，可以将数据写入 RAM 存储器位置。此值可以是 integer，或者类型为 `double`、`single` 或 `half`。该值也可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

可以将非虚拟总线和总线数组用于 HDL 代码生成。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **addr** — 要写入或读取的地址 `scalar` | `vector`

要写入或读取的地址，指定为标量或向量。当端口 **we** 处的信号为 `true` 时，使用此地址将数据写入 RAM。当端口 **we** 处的信号为 false 时，该模块从指定存储器位置读取值。此值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须介于 `2` 和 `31` bits 之间。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we** — 写使能 `scalar` | `vector`

写使能，指定为标量或向量。当端口 **we** 处的信号为 `true` 时，该模块将数据写入指定存储器位置。当端口 **we** 处的信号为 `false` 时，该模块从 **addr** 端口指定的存储器位置读取值。

**注意**

要使用列写方法，数据类型必须是 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **dout** — 输出数据 `scalar` | `vector`

输出数据，以标量或向量形式返回。当端口 **we** 处的信号为 `false` 时，RAM 从 **addr** 端口指定的存储器位置读取数据。

## 参数

### 主要

### **Type of RAM** — RAM 类型 `Single port` (默认) | `Simple dual port` | `Dual port` | `True dual port` | `Simple tri port`

RAM 类型，指定为以下之一：

- `Single port` — 创建单端口 RAM，其中写入数据、地址和写使能数据作为输入，读取数据作为输出。
- `Simple dual port` — 创建简单双端口 RAM，其中写入数据、写地址、写使能和读地址作为输入，来自读地址的数据作为输出。
- `Dual port` — 创建双端口 RAM，其中写入数据、写地址、写使能和读地址作为输入，来自读地址和写地址的数据作为输出。
- `True dual port` — 创建真双端口 RAM，其中写入数据 `a` 和 `b`，`a` 和 `b` 的写地址与读地址，以及写使能 `a` 和 `b` 作为输入，来自写地址 `a` 和 `b` 的数据作为输出。
- `Simple tri port` — 创建简单三端口 RAM，其中写入数据、写地址、写使能和读地址 `a` 和 `b` 作为输入，来自读地址 `a` 和 `b` 的数据作为输出。

代码生成器会根据指定的 RAM 类型动态配置模块的输入和输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`RAMType` |
| **类型：**  character vector, string |
| **值：**  `Dual port` | `Simple dual port` | `Single port` | `True dual port` | `Simple tri port` |
| **默认值：**  `Single port` |

### **Use asynchronous read feature in target hardware** — 用于在目标硬件中启用异步读取功能的选项 `off` (默认) | `on`

启用此选项以允许硬件立即执行读取指令，而无需等待一个周期。

#### 编程用法

|  |
| --- |
| **模块参数：**`AsyncRead` |
| **类型：**  character vector, string |
| **值：**  `'on'` | `'off'` |
| **默认值：**  `'off'` |

### **Behavior for write output** — 写输出行为 `New data` (默认) | `Old data`

选择写输出行为为 `New data` 或 `Old data`：

- `New data` — 在地址处将新数据发送到输出。
- `Old data` — 在地址处将旧数据发送到输出。

#### 依赖关系

要启用此参数，请清除 **Use asynchronous read feature in target hardware** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`WriteOutputValue` |
| **类型：**  character vector, string |
| **值：**  `New data` | `Old data` |
| **默认值：**  `New data` |

### **Initial output of RAM** — RAM 的初始仿真输出 `'0.0'` (默认) | `Scalar` | `Vector`

使用以下选项之一指定 RAM 的初始仿真输出：

- 一个标量值。
- 一个向量，其初始值与 RAM 字之间一一映射。
- 一个 *n*-by-*m* 矩阵，其初始值与 RAM 存储体中的 RAM 字之间一一映射，其中 *n* 表示 RAM 存储体的数量，*m* 表示 RAM 模块中地址位置的数量，或反之。

#### 编程用法

|  |
| --- |
| **模块参数：**`RAMInitialValue` |
| **类型：**  integer, floating point |
| **值：**  `0.0` | `Scalar` | `Vector` |
| **默认值：**  `0.0` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 高级

### **Model RAM with one cycle of delay** — 用一个周期延迟对 RAM 建模 `on` (默认) | `off`

*自 R2024b 起*

- 选择此参数时，RAM 会将输入数据延迟一个周期，然后输出才能读取它。使用此选项可确保该模块与生成的 HDL 代码周期精确。
- 清除此参数时，RAM 会立即读取并输出输入数据，但在 HDL 代码生成期间会增加一个周期的延迟。当指定过采样值或使用多速率模型时，使用此选项可利用时钟速率流水线。

#### 依赖关系

要启用此参数，请清除 **Use asynchronous read feature in target hardware** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`ModelRAMDelay` |
| **类型：**  character vector, string |
| **值：**  `'on'` | `'off'` |
| **默认值：**  `'on'` |

### **Specify vector input access** — 将向量输入访问指定为 `serial` 或 `parallel` `serial` (默认) | `parallel`

*自 R2025a 起*

- 当将此参数设置为 `serial` 时，代码生成器会根据到 RAM System 模块的向量输入推断并行 RAM 存储体。
- 当将此参数设置为 `parallel` 时：

  - 生成 HDL Code 时，代码生成器不会随向量输入的大小扩展 RAM 消耗量。相反，它会从第一个索引开始，一次应用一个输入信号的每个操作。启用 `serial` 访问允许你在以数据速率对向量输入建模时，以更快的时钟速率利用多周期 RAM 访问。
  - 如果 RAM System 模块存在于时钟速率流水线区域中，则序列化使用时钟速率实现，而不是本地多速率实现。

#### 依赖关系

要启用此参数，请清除 **Model RAM with one cycle of delay** 参数或启用 **Use asynchronous read feature in target hardware** 参数。

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

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

该模块具有 `MATLABSystem` 架构，这表明模块实现使用 `hdl.RAM` System object™。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 块映射到目标 FPGA 上的 RAM 块。对于 UltraRAM 映射，**Initial output of RAM** 必须设置为 `0`。另请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

该模块不支持：

- 数据端口处的嵌套总线。
- 当对数据端口使用非虚拟总线输入时，**Initial output of RAM** 为非零值。

## 版本历史

**在 R2017b 中引入**

### R2024b：使用时钟速率流水线

可以在数据速率反馈环路内使用 Single Port RAM System 模块，并使用时钟速率流水线优化。此模型设计对于需要可编程或可调查找表而无需重新生成比特流的应用很有帮助。

使用新参数 **Model RAM with one cycle of delay** 在仿真中对延迟建模。**Model RAM with one cycle of delay** 默认启用，并且当 **Use asynchronous read feature in target hardware** 启用时禁用。

### R2024b：参数名称更改

这些参数已重命名：

| 先前名称 | 当前名称 |
| --- | --- |
| **Specify the type of RAM** | **Type of RAM** |
| **Enable asynchronous reads** | **Use asynchronous read feature in target hardware** |
| **Specify the output data for a write operation** | **Behavior for write output** |
| **Specify the RAM initial value** | **Initial output of RAM** |

### R2024b：在 RAM System 模块中使用列写操作按列写入 RAM

在此模块中，可以使用列写方法在指定存储器地址处选择性地修改存储器的特定部分，而不改变其余部分。

### R2024b：为向量数据输入使用唯一初始值初始化 RAM 存储体

在此模块中，可以使用唯一初始值初始化 RAM 存储体。

### R2024a：数组总线输入支持

该模块现在支持为指定为总线数组的输入数据生成 HDL 代码。

### R2024a：半精度和布尔数据支持

该模块现在支持使用类型为 `Half` 或 `Boolean` 的输入数据进行 HDL 代码生成。

## 描述

支持顺序读写操作的单端口 RAM

Single Port RAM System 模块对支持顺序读写操作的单端口 RAM 进行建模。要配置此模块，请打开该模块，并将 **Type of RAM** 参数设置为 `Single port`。通过使用此模块，你可以：

- 通过在 **din**、**addr** 和 **we** 端口使用向量数据来创建并行 RAM 存储体。
- 使用 **Initial output of RAM** 参数为 RAM 指定初始值。
- 通过选择 **Use asynchronous read feature in target hardware** 参数，在目标硬件中执行异步读取。
- 通过选择 **Model RAM with one cycle of delay** 参数，执行周期精确的读取操作。
- 使用列写方法写入已寻址存储器位置中的指定位。
