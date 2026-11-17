---
type: simulink-block
title: 'Quadrature Decoder'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'quadraturedecoder'
documentation_source_path: 'ref/quadraturedecoder.html'
language: zh-CN
chinese_source: official
---

# Quadrature Decoder

## 端口

### 输入

### **Cnt** — 正交编码器计数器值 标量

正交编码器计数器针对刻度线位置生成的值。该端口只接受基于**计数器大小**参数的无符号标量整数。例如，如果您为**计数器大小**选择 **8 位**，则输入数据类型必须为 uint8。

**数据类型:** `uint8` | `uint16` | `uint32`

### **Idx** — 最后一个索引脉冲的正交编码器计数器值 标量

正交编码器计数器在最后一次索引脉冲时针对刻度线位置生成的值。该端口只接受基于**计数器大小**参数的无符号标量整数。例如，如果您为**计数器大小**选择 **8 位**，则输入数据类型必须为 uint8。

#### 依赖关系

要启用此端口，请选择**外部索引计数**参数。

**数据类型:** `uint8` | `uint16` | `uint32`

### **CountsPerRev** — 为每次旋转生成的计数数量 标量

正交编码器为每次旋转生成的计数数量。

**CountsPerRev** = **编码器刻线** ⨯ **每个刻线的编码器计数**

#### 依赖关系

要启用此端口，请选择**使用输入端口提供计算参数(运行时电机更换)** 参数。

**数据类型:** `uint8` | `uint16` | `uint32` | `single` | `double` | `fixed point`

### **1/CountsPerRev** — 为每次旋转生成的计数数量的倒数 标量

指定正交编码器在此端口为每次旋转生成的计数数量的倒数。**1/CountsPerRev 输入的数据类型**参数定义此输入的数据类型。

#### 依赖关系

要启用此端口，请选择**使用输入端口提供计算参数(运行时电机更换)** 参数。

**数据类型:** `single` | `double` | `fixed point`

**注意**

**Cnt** 和 **Idx** 端口上输入的数据类型必须相同。
### 输出

### **θm** — 正交编码器的角位置 标量

模块根据 `Cnt` 和 `Idx` 输入计算的角位置。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **使用输入端口提供计算参数(运行时电机更换)** — 启用 `CountsPerRev` 和 `1/CountsPerRev` 输入端口 `off` (默认) | `on`

仅当您选择此参数时，该模块才会启用 `CountsPerRev` 和 `1/CountsPerRev` 输入端口。选择此参数时，该模块还会禁用**编码器刻线**和**每个刻线的编码器计数**参数。

### **1/CountsPerRev 输入的数据类型** — `1/CountsPerRev` 输入的数据类型 **单精度** (默认) | **双精度** | **定点**

指定 `1/CountsPerRev` 输入的数据类型。如果指定定点数据类型，则可以使用此参数指定 `1/CountsPerRev` 输入的精度。

#### 依赖关系

要启用此参数，请选择**使用输入端口提供计算参数(运行时电机更换)** 参数。

### **编码器刻线** — 每个相位的刻度线数 `1000` (默认) | 标量

正交编码器的每个相位中可用的刻度线数。

#### 依赖关系

要启用此参数，请清除**使用输入端口提供计算参数(运行时电机更换)** 参数。

### **每个刻线的编码器计数** — 为每个刻度线生成的计数数 **4** (默认) | **1** | **2**

正交编码器为每个刻度线生成的计数数。一个计数表示一个刻度线位置。例如，如果您要编码器生成对应于 00、10、11 和 01 刻度线位置或值的四个计数，请选择 4（正交模式）。如果选择正交模式：

每次旋转的编码器计数（正交后）= **每个刻线的编码器计数**✖**编码器刻线**

#### 依赖关系

要启用此参数，请清除**使用输入端口提供计算参数(运行时电机更换)** 参数。

### **计数器大小** — 正交编码器计数器的大小 **16 位** (默认) | **8 位** | **32 位**

计数器大小表示处理器用于对正交编码器脉冲进行计数的计数器的寄存器大小。例如，当使用基于 TI’s C2000™ 的硬件时，它是来自 C2000™ Microcontroller Blockset 的 eQEP 模块的计数器输出的数据类型。

### **外部索引计数** — 启用 `Idx` 输入端口 `on` (默认) | `off`

仅当您选择此参数时，该模块才会启用 **Idx** 输入端口。**Idx** 输入端口期望在索引脉冲时有等于 **Cnt** 的值。

### **位置单位** — 角位置输出的单位 **弧度** (默认) | **度** | **标幺**

角位置输出的单位。

### **位置数据类型** — 角位置输出的数据类型 **单精度** (默认) | **双精度** | **定点**

角位置输出的数据类型。

**注意**

Quadrature Decoder 模块可以在需要时显示警告消息 `'Wrap on overflow detected'`。

## 所属库

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

当您设置**位置数据类型**以及 **CountsPerRev** 和 **1/CountsPerRev** 输入值以使用相同的数据类型（浮点或定点）时，模块支持 HDL 代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

计算正交编码器的位置

Quadrature Decoder 模块用于计算正交编码器的位置。

在计算正交编码器（和转子）的角位置（以度、弧度或标幺为单位）时，该模块会使用以下方法之一。

- 当前编码器计数值和前一个索引脉冲（如果索引脉冲可用）时编码器计数值之间的差值。
- 当前编码器计数器值（索引脉冲不可用时）。

下图显示了具有两个通道（QEPA 和 QEPB）和一个索引脉冲 (QEPI) 的正交编码器盘：

在此示例中，每通过编码器盘上的一个刻度线时，由 QEP 驱动的计时器数值会增加 4：

### 方程

该模块使用 `Cnt` 和 `Idx` 模块输入来计算正交编码器的角位置（以计数为单位）：

当 *Cnt ≥ Idx* 时：

Position count=(Cnt−Idx)

当 *Cnt < Idx* 时：

Position count=Counts per revolution+(Cnt−Idx)

当 `Cnt`（无符号整数）超出所选计数器大小的最大值时，该模块会在内部添加必要的补偿。

当您清除**外部索引计数**复选框时，只有 `Cnt` 输入可用，因此：

Position count=Cnt

其中：

- Position count 是正交编码器的角位置，以计数为单位。
- Counts per revolution 是正交编码器的一个旋转周期中的计数 *(Counts per revolution = Encoder slits ⨯ Encoder counts per slit)*。

该模块将输出 **θm** 计算为：

θm=MaxPosition×(Position countEncoder slits×Encoder counts per slit)=MaxPosition×(Position countCounts per revolution)

其中，*MaxPosition* = 360（度）或 2π（弧度）或 1（标幺），具体取决于所选的**位置单位**参数值。
