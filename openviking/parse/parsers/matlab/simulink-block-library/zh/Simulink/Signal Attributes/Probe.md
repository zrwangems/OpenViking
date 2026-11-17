---
type: simulink-block
title: 'Probe'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'probe'
documentation_source_path: 'slref/probe.html'
language: zh-CN
chinese_source: worker-translation
---

# Probe

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

要探测的输入信号，指定为标量、向量、矩阵或 N 维数组。该模块接受任何内置数据类型的实数或复数值信号。

您可以将总线数组用作 Probe 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1 (W)** — 信号宽度 标量

输入信号中的宽度（即元素数量），以标量形式指定。该宽度也会以 `W:` 的记号显示在模块图标上。

#### 依赖关系

要启用此端口，请选择 **Probe width**。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2 (Ts)** — 采样时间 向量

输入信号的采样时间，以二元素向量形式分别指定采样时间的周期和偏移量。该采样时间也会以 `Ts:` 的记号显示在模块图标上。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

要启用此端口，请选择 **Probe sample time**。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_3 (C)** — 信号复/实性 标量

输入信号复/实性的指示：

- 当输入信号为复数时，模块输出 `1`。
- 当输入信号为实数值时，模块输出 `0`。

信号复/实性的指示也会以 `C:` 的记号显示在模块图标上。

#### 依赖关系

要启用此端口，请选择 **Detect complex signal**。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_4 (D)** — 信号维度 标量 | 向量

输入信号的维度，以标量或向量形式输出。信号维度也会以 `D:` 的记号显示在模块图标上。

#### 依赖关系

要启用此端口，请选择 **Probe signal dimensions**。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Probe width** — 输入信号的输出宽度 `on`（默认）| `off`

选择此项以输出被探测信号的宽度（即元素数量）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeWidth` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **Probe sample time** — 输入信号的输出采样时间 `on`（默认）| `off`

选择此项以输出被探测信号的采样时间。输出是一个二元素向量，分别指定采样时间的周期和偏移量。有关详细信息，请参阅 Specify Sample Time。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeSampleTime` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **Detect complex signal** — 指示输入信号的复/实性 `on`（默认）| `off`

选择此项以在被探测信号为复数时输出 `1`；否则输出 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeComplexSignal` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### **Probe signal dimensions** — 输入信号的输出维度 `on`（默认）| `off`

选择此项以输出被探测信号的维度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeSignalDimensions` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'on'` |

### 信号属性

### **Data type for width** — 信号宽度输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Same as input`

选择信号宽度的输出数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeWidthDataType` |
| **类型：** 字符向量 |
| **值：** `'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'Same as input'` |
| **默认值：** `'double'` |

### **Data type for sample time** — 采样时间输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Same as input`

选择采样时间信息的输出数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeSampleTimeDataType` |
| **类型：** 字符向量 |
| **值：** `'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'Same as input'` |
| **默认值：** `'double'` |

### **Data type for signal complexity** — 复/实性输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean` | `Same as input`

选择复/实性信息的输出数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeComplexityDataType` |
| **类型：** 字符向量 |
| **值：** `'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'Same as input'` |
| **默认值：** `'double'` |

### **Data type for signal dimensions** — 信号维度输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Same as input`

选择信号维度输出的输出数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbeDimensionsDataType` |
| **类型：** 字符向量 |
| **值：** `'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'Same as input'` |
| **默认值：** `'double'` |

## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

输出信号属性，包括宽度、维度、采样时间和复数信号标志

Probe 模块输出有关其输入信号所选定的信息。该模块可以输出输入信号的以下属性：宽度、维度、采样时间，以及指示输入是否为复数值信号的标志。该模块有一个输入端口。输出端口的数量取决于您选择探测的信息，即信号维度、采样时间和/或复数信号标志。每个被探测的值作为单独的信号在单独的输出端口上输出，并具有独立的数据类型控制。在仿真期间，模块图标会显示被探测的数据。
