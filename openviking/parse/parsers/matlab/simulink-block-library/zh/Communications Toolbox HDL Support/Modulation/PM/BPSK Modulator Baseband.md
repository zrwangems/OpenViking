---
type: simulink-block
title: 'BPSK Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'bpskmodulatorbaseband'
documentation_source_path: '../comm/ref/bpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# BPSK Modulator Baseband

## 端口

### 输入

### **In** — 输入数据 标量 | 向量

输入信号，指定为标量或向量，其元素值在范围 [0,1] 内。

该端口在模块上未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — BPSK 调制基带信号 标量 | 向量

BPSK 调制基带信号，返回为复值标量或向量。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Phase offset (rad)** — 零点相位偏移 `0`（默认）| 标量

星座图零点的相位偏移，以弧度为单位，指定为标量。

**示例：** `pi/4`

### **View constellation** — 绘制参考星座图的选项 按钮

单击模块掩码上的 **View Constellation**，以可视化指定模块参数下的信号星座图。在查看星座图之前，请先应用参数设置。有关详细信息，请参阅 View Constellation of Modulator Block。

### 数据类型

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit via back propagation` | `<data type expression>`

输出数据类型，指定为 `double`、`single`、`fixdt(1,16)`、`fixdt(1,16,0)`、`Inherit via back propagation` 或 `<data type expression>`。

将此参数设置为

- `fixdt(1,16)`、`fixdt(1,16,0)` 或 `<data type expression>` 会启用相应参数，您可以在其中进一步指定详细信息。
- `Inherit via back propagation` 会将输出数据类型和定标设置为与后续模块匹配。

有关指定数据类型的信息，请参阅 Data Type Assistant。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅对于 M 元调制的输入为 ufix(ceil(log2(M)))。  b 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 BPSK 方法进行调制

BPSK Modulator Baseband 模块使用二进制相移键控 (BPSK) 方法对信号进行调制。输出是调制信号的基带表示。输入信号必须是离散时间二值信号。如果输入比特为 0 或 1，则调制符号分别为 exp(jϕ) 或 -exp(jϕ)。`Phase offset (rad)` 参数指定 ϕ 的值，以弧度为单位。
