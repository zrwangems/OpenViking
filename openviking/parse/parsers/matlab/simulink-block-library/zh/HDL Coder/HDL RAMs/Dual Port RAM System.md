---
type: simulink-block
title: 'Dual Port RAM System'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'dualportramsystem'
documentation_source_path: 'ref/dualportramsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Dual Port RAM System

## 端口
```yaml
ports:
- name: din
  summary: 要写入的数据 scalar | vector
  direction: input
  data_types: single | double | half | int8 | int16 | uint8 | uint16 | Boolean | fixed point
- name: wr_addr
  summary: 要写入的地址 scalar | vector
  direction: input
  data_types: uint8 | uint16 | fixed point
- name: we
  summary: 写使能 scalar | Vector
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: rd_addr
  summary: 要读取的地址 scalar | vector
  direction: input
  data_types: uint8 | uint16 | fixed point
- name: rd_dout
  summary: 读取输出数据 scalar | vector
  direction: output
- name: wr_dout
  summary: 写入输出数据 scalar | vector
  direction: output
```

### 输入

### **din** — 要写入的数据 `scalar` | `vector`

要写入的数据，指定为标量或向量。当端口 **we** 处的写使能信号为 `true` 时，您可以将数据写入 RAM 存储位置。该值可以是整数，也可以是 `double`、`single` 或 `half` 类型。该值还可以是 `fi` 对象，并且可以是实数或复数。

#### 总线支持：

您可以使用非虚拟总线和总线数组进行 HDL 代码生成。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **wr\_addr** — 要写入的地址 `scalar` | `vector`

要写入的地址，指定为标量或向量。当端口 **we** 处的信号为 `true` 时，使用此地址写入 RAM。该值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we** — 写使能 `scalar` | `Vector`

写使能，指定为标量或向量。当端口 **we** 处的信号为 `true` 时，模块将数据写入指定的存储位置。当端口 **we** 处的信号为 `false` 时，模块从 **rd\_addr** 端口指定的存储位置读取值。

**注意**

要使用列写入方法，数据类型必须是 `integer` 或 `fixed-point`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **rd\_addr** — 要读取的地址 `scalar` | `vector`

要读取的地址，指定为标量或向量。使用此地址从 RAM 中读取数据。该值可以是 `fixed-point (fi)` 或无符号 `integer`，并且长度必须在 `2` 到 `31` 位之间。

**数据类型：** `uint8` | `uint16` | `fixed point`
### 输出

### **rd\_dout** — 读取输出数据 `scalar` | `vector`

读取输出数据，以标量或向量形式返回。模块从 **rd\_addr** 端口指定的存储位置读取旧数据。

### **wr\_dout** — 写入输出数据 `scalar` | `vector`

写入输出数据，以标量或向量形式返回。模块从 **wr\_addr** 端口指定的存储位置读取新数据或旧数据。
## 参数
```yaml
parameters:
- name: Type of RAM
  summary: RAM 类型 Dual port（默认）| Simple dual port | Single port | True dual port | Simple tri port
  group: 主要
  block_parameter: RAMType
  type: character vector, string
  values: Dual port | Simple dual port | Single port | True dual port | Simple tri port
  default: Dual port
- name: Use asynchronous read feature in target hardware
  summary: 用于在目标硬件中启用异步读取功能的选项 off（默认）| on
  group: 主要
  block_parameter: AsyncRead
  type: 字符向量、字符串
  values: '''on'' | ''off'''
  default: '''off'''
- name: 写输出行为
  summary: 写输出行为 New data（默认）| Old data
  group: 主要
  block_parameter: WriteOutputValue
  type: 字符向量、字符串
  values: New data | Old data
  default: New data
- name: RAM 初始输出
  summary: RAM 的初始仿真输出 '0.0'（默认）| Scalar | Vector
  group: 主要
  block_parameter: RAMInitialValue
  type: 整数、浮点数
  values: 0.0 | Scalar | Vector
  default: '0.0'
- name: 使用一个延迟周期对 RAM 建模
  summary: 使用一个延迟周期对 RAM 建模 on（默认）| off
  group: 高级
  block_parameter: ModelRAMDelay
  type: 字符向量、字符串
  values: '''on'' | ''off'''
  default: '''on'''
- name: 指定向量输入访问方式
  summary: 将向量输入访问方式指定为串行或并行 serial（默认）| parallel
  group: 高级
  block_parameter: VectorAccess
  type: 字符向量、字符串
  values: '''serial'' | ''parallel'''
  default: '''serial'''
```

### 主要

### **Type of RAM** — RAM 类型 `Dual port`（默认）| `Simple dual port` | `Single port` | `True dual port` | `Simple tri port`

RAM 类型，指定为以下之一：

- `Single port` — 创建单端口 RAM，以写数据、地址和写使能数据作为输入，以读数据作为输出。
- `Simple dual port` — 创建简单双端口 RAM，以写数据、写地址、写使能和读地址作为输入，以来自读地址的数据作为输出。
- `Dual port` — 创建双端口 RAM，以写数据、写地址、写使能和读地址作为输入，以来自读地址和写地址的数据作为输出。
- `True dual port` — 创建真双端口 RAM，以写数据 `a` 和 `b`、`a` 和 `b` 的写地址和读地址、以及写使能 `a` 和 `b` 作为输入，以来自写地址 `a` 和 `b` 的数据作为输出。
- `Simple tri port` — 创建简单三端口 RAM，以写数据、写地址、写使能以及读地址 `a` 和 `b` 作为输入，以来自读地址 `a` 和 `b` 的数据作为输出。

代码生成器根据您指定的 RAM 类型动态配置模块的输入和输出端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`RAMType` |
| **类型**：character vector, string |
| **值**：`Dual port` | `Simple dual port` | `Single port` | `True dual port` | `Simple tri port` |
| **默认值**：`Dual port` |

### **Use asynchronous read feature in target hardware** — 用于在目标硬件中启用异步读取功能的选项 `off`（默认）| `on`

启用此选项以允许硬件立即执行读取指令，而无需等待一个周期。

#### 程序化使用

|  |
| --- |
| **模块参数：**`AsyncRead` |
| **类型：**  字符向量、字符串 |
| **值：**  `'on'` | `'off'` |
| **默认值：**  `'off'` |

### **写输出行为** — 写输出行为 `New data`（默认）| `Old data`

选择写输出的行为为 `New data` 或 `Old data`：

- `New data` — 将地址处的新数据发送到输出。
- `Old data` — 将地址处的旧数据发送到输出。

#### 依赖关系

要启用此参数，请清除 **在目标硬件中使用异步读取功能** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**`WriteOutputValue` |
| **类型：**  字符向量、字符串 |
| **值：**  `New data` | `Old data` |
| **默认值：**  `New data` |

### **RAM 初始输出** — RAM 的初始仿真输出 `'0.0'`（默认）| `Scalar` | `Vector`

使用以下选项之一指定 RAM 的初始仿真输出：

- 标量值。
- 初始值与 RAM 字之间一一对应的向量。
- *n*×*m* 矩阵，初始值与 RAM 存储体中的 RAM 字之间一一对应，其中 *n* 表示 RAM 存储体的数量，*m* 表示 RAM 块中的地址位置数量，反之亦然。

#### 程序化使用

|  |
| --- |
| **模块参数：**`RAMInitialValue` |
| **类型：**  整数、浮点数 |
| **值：**  `0.0` | `Scalar` | `Vector` |
| **默认值：**  `0.0` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 高级

### **使用一个延迟周期对 RAM 建模** — 使用一个延迟周期对 RAM 建模 `on`（默认）| `off`

*自 R2024b 起*

- 选中此参数时，RAM 将输入数据延迟一个周期后，输出才能读取该数据。使用此选项可确保模块与生成的 HDL 代码在周期上精确一致。
- 清除此参数时，RAM 立即读取并输出输入数据，但在 HDL 代码生成期间增加一个周期的延迟。使用此选项可在指定过采样值或处理多速率模型时利用时钟速率流水线。

#### 依赖关系

要启用此参数，请清除 **在目标硬件中使用异步读取功能** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ModelRAMDelay` |
| **类型：**  字符向量、字符串 |
| **值：**  `'on'` | `'off'` |
| **默认值：**  `'on'` |

### **指定向量输入访问方式** — 将向量输入访问方式指定为串行或并行 `serial`（默认）| `parallel`

*自 R2025a 起*

- 将此参数设置为 `serial` 时，代码生成器从 RAM System 模块的向量输入推断并行 RAM 存储体。
- 将此参数设置为 `parallel` 时：

  - 生成 HDL 代码时，代码生成器不会随向量输入的大小按比例增加 RAM 消耗量。相反，它从第一个索引开始，一次对输入信号执行一个操作。启用串行访问允许您在以数据速率对向量输入进行建模的同时，以更快的时钟速率利用多周期 RAM 访问。
  - 如果 RAM System 模块位于时钟速率流水线区域中，则串行化使用时钟速率实现，而不是本地多速率实现。

#### 依赖关系

要启用此参数，请清除 **使用一个延迟周期对 RAM 建模** 参数或启用 **在目标硬件中使用异步读取功能** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：**`VectorAccess` |
| **类型：**  字符向量、字符串 |
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

该模块具有 `MATLABSystem` 架构，表示该模块实现使用 `hdl.RAM` System object™。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 块映射到目标 FPGA 上的 RAM 块。对于 UltraRAM 映射，**Initial output of RAM** 必须设置为 `0`。更多详细信息，请参阅 RAMDirective。 |

**复数数据支持**

该模块支持复数信号的代码生成。

**限制**

该模块不支持：

- 数据端口上的嵌套总线。
- 当数据端口使用非虚拟总线输入时，**Initial output of RAM** 为非零值。

## 版本历史

**在 R2017b 中引入**

### R2024b：使用时钟速率流水线

您可以在数据速率反馈环路内使用 Dual Port RAM System 模块，并使用时钟速率流水线优化。此模型设计适用于需要可编程或可调查找表而无需重新生成比特流的应用。

使用新参数 **Model RAM with one cycle of delay** 在仿真中对延迟进行建模。**Model RAM with one cycle of delay** 默认启用，当 **Use asynchronous read feature in target hardware** 启用时，该参数被禁用。

### R2024b：参数名称变更

以下参数已重命名：

| 旧名称 | 当前名称 |
| --- | --- |
| **指定 RAM 的类型** | **RAM 类型** |
| **Enable asynchronous reads** | **Use asynchronous read feature in target hardware** |
| **指定写操作的输出数据** | **写输出的行为** |
| **指定 RAM 的初始值** | **RAM 的初始输出** |

### R2024b：在 RAM System 模块中使用列写操作按列写入 RAM

在此模块中，您可以使用列写方法在指定内存地址处选择性地修改存储器的特定部分，而不改变其余部分。

### R2024b：为向量数据输入使用唯一初始值初始化 RAM 存储体

在此模块中，您可以使用唯一初始值初始化 RAM 存储体。

### R2024a：支持总线数组输入

该模块现在支持对指定为总线数组的输入数据进行 HDL 代码生成。

### R2024a：半精度和布尔数据支持

该模块现在支持使用 `Half` 或 `Boolean` 类型的输入数据进行 HDL 代码生成。

## 描述

支持同时读写操作的双端口 RAM

Dual Port RAM System 模块对双端口 RAM 进行建模，通过读数据和写数据的输出端口支持同时读写操作。要配置此模块，请打开该模块并将 **Type of RAM** 参数设置为 `dual port`。通过使用此模块，您可以：

- 通过在 **din**、**addr** 和 **we** 端口使用向量数据来创建并行 RAM 组。
- 使用 **Initial output of RAM** 参数为 RAM 指定初始值。
- 通过在目标硬件中选择 **Use asynchronous read feature in target hardware** 参数来执行异步读取。
- 通过选择 **Model RAM with one cycle of delay** 参数来执行周期精确的读操作。
- 使用列写入方法写入被寻址内存位置中的指定比特。

**注意**

在写入期间，新数据出现在 Dual Port RAM System 模块写端口 **wr\_dout** 的输出处。如果读操作与写操作同时发生在同一地址，则旧数据出现在读输出端口 **rd\_dout**。
