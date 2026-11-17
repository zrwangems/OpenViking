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
chinese_source: worker-translation
---

# Quadrature Decoder

## 端口
```yaml
ports:
- name: Cnt
  summary: 正交编码器计数器值 标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Idx
  summary: 上次索引脉冲时的正交编码器计数器值 标量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: CountsPerRev
  summary: 每转生成的计数数 标量
  direction: input
  data_types: uint8 | uint16 | uint32 | single | double | fixed point
- name: 1/CountsPerRev
  summary: 每转生成的计数数的倒数 标量
  direction: input
  data_types: single | double | fixed point
- name: θm
  summary: 正交编码器的角位置 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Cnt** — 正交编码器计数器值 标量

正交编码器计数器根据狭缝位置生成的值。该端口仅接受基于 **Counter size** 参数的无符号整数标量。例如，如果为 **Counter size** 选择 `8 bits`，则输入数据类型必须为 uint8。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Idx** — 上次索引脉冲时的正交编码器计数器值 标量

正交编码器计数器在上次索引脉冲时根据狭缝位置生成的值。该端口仅接受基于 **Counter size** 参数的无符号整数标量。例如，如果为 **Counter size** 选择 `8 bits`，则输入数据类型必须为 uint8。

#### 依赖关系

要启用此端口，请选择 **External index count** 参数。

**数据类型：** `uint8` | `uint16` | `uint32`

### **CountsPerRev** — 每转生成的计数数 标量

正交编码器每转生成的计数数。

**CountsPerRev** = **Encoder slits** ⨯ **Encoder counts per slit**

#### 依赖关系

要启用此端口，请选择 **Use input port for computed parameters (run-time motor swap)** 参数。

**数据类型：** `uint8` | `uint16` | `uint32` | `single` | `double` | `fixed point`

### **1/CountsPerRev** — 每转生成的计数数的倒数 标量

在此端口指定正交编码器每转生成的计数数的倒数。**Data type for 1/CountsPerRev input** 参数定义此输入的数据类型。

#### 依赖关系

要启用此端口，请选择 **Use input port for computed parameters (run-time motor swap)** 参数。

**数据类型：** `single` | `double` | `fixed point`

**注意**

**Cnt** 和 **Idx** 端口输入的数据类型必须相同。
### 输出

### **θm** — 正交编码器的角位置 标量

该模块基于 `Cnt` 和 `Idx` 输入计算得到的角位置。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Use input port for computed parameters (run-time motor swap)
  summary: 启用 CountsPerRev 和 1/CountsPerRev 输入端口 off（默认） | on
  group: ''
- name: Data type for 1/CountsPerRev input
  summary: 1/CountsPerRev 输入的数据类型 single（默认） | double | fixed point
  group: ''
- name: Encoder slits
  summary: 每相狭缝数 1000（默认） | 标量
  group: ''
- name: Encoder counts per slit
  summary: 每个狭缝生成的计数数 4（默认） | 1 | 2
  group: ''
- name: Counter size
  summary: 正交编码器计数器的位数 16 bits（默认）| 8 bits | 32 bits
  group: ''
- name: External index count
  summary: 启用 Idx 输入端口 on（默认）| off
  group: ''
- name: Position unit
  summary: 角位置输出的单位 Radians（默认）| Degrees | Per unit
  group: ''
- name: Position data type
  summary: 角位置输出的数据类型 single（默认）| double | fixed point
  group: ''
```

### **Use input port for computed parameters (run-time motor swap)** — 启用 `CountsPerRev` 和 `1/CountsPerRev` 输入端口 `off`（默认） | `on`

仅当选择此参数时，该模块才启用 `CountsPerRev` 和 `1/CountsPerRev` 输入端口。选择此参数时，该模块还会禁用 **Encoder slits** 和 **Encoder counts per slits** 参数。

### **Data type for 1/CountsPerRev input** — `1/CountsPerRev` 输入的数据类型 `single`（默认） | `double` | `fixed point`

指定 `1/CountsPerRev` 输入的数据类型。如果指定定点数据类型，可以使用此参数指定 `1/CountsPerRev` 输入的精度。

#### 依赖关系

要启用此参数，请选择 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Encoder slits** — 每相狭缝数 `1000`（默认） | 标量

正交编码器每相中可用的狭缝数。

#### 依赖关系

要启用此参数，请清除 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Encoder counts per slit** — 每个狭缝生成的计数数 `4`（默认） | `1` | `2`

正交编码器为每个狭缝生成的计数数。一个计数表示一个狭缝位置。例如，如果希望编码器生成对应于 00、10、11 和 01 狭缝位置或值的四个计数，请选择 4（正交模式）。如果选择正交模式：

每转编码器计数数（正交后）= **Encoder counts per slit** ✖ **Encoder slits**

#### 依赖关系

要启用此参数，请清除 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Counter size** — 正交编码器计数器的位数 `16 bits`（默认）| `8 bits` | `32 bits`

计数器位数表示处理器用于对正交编码器脉冲进行计数的计数器寄存器大小。例如，当使用基于 TI C2000™ 的硬件时，它是 C2000™ Microcontroller Blockset 中 eQEP 模块计数器输出的数据类型。

### **External index count** — 启用 `Idx` 输入端口 `on`（默认）| `off`

仅当您选择此参数时，该模块才会启用 **Idx** 输入端口。**Idx** 输入端口期望在索引脉冲时刻输入一个等于 **Cnt** 的值。

### **Position unit** — 角位置输出的单位 `Radians`（默认）| `Degrees` | `Per unit`

角位置输出的单位。

### **Position data type** — 角位置输出的数据类型 `single`（默认）| `double` | `fixed point`

角位置输出的数据类型。

**注意**

Quadrature Decoder 模块在需要时可以显示警告消息 `'Wrap on overflow detected'`。
## 所属库

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

当您将 **Position data type** 以及输入 **CountsPerRev** 和 **1/CountsPerRev** 设置为使用相同的数据类型（浮点或定点）时，该模块支持 HDL 代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算正交编码器的位置

Quadrature Decoder 模块计算正交编码器的位置。

要以度、弧度或标幺值计算正交编码器（以及转子）的角位置，该模块使用以下方法之一。

- 当前编码器计数器值与上一个索引脉冲时刻的编码器计数器值之间的差值（当索引脉冲可用时）。
- 当前编码器计数器值（当索引脉冲不可用时）。

下图显示了一个具有两个通道（QEPA 和 QEPB）以及一个索引脉冲（QEPI）的正交编码器圆盘：

在此示例中，由 QEP 驱动的定时器对每个狭缝递增四：

### 方程

该模块使用 `Cnt` 和 `Idx` 模块输入计算正交编码器的角位置（以计数为单位）：

当 *Cnt ≥ Idx* 时：

Position count=(Cnt−Idx)

当 *Cnt < Idx* 时：

Position count=Counts per revolution+(Cnt−Idx)

当 `Cnt`（无符号整数）超过所选计数器大小的最大值时，模块会在内部添加必要的补偿。

当您清除 **External index count** 复选框时，仅 `Cnt` 输入可用，因此：

Position count=Cnt

其中：

- Position count 是正交编码器以计数表示的角位置。
- Counts per revolution 是正交编码器一个旋转周期内的计数数 *(Counts per revolution = Encoder slits ⨯ Encoder counts per slit)*。

该模块计算输出 **θm** 如下：

θm=MaxPosition×(Position countEncoder slits×Encoder counts per slit)=MaxPosition×(Position countCounts per revolution)

其中，*MaxPosition* = 360（度）或 2π（弧度）或 1（标幺值），取决于 **Position unit** 参数的所选值。
