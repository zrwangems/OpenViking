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

此端口在模块上未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — BPSK 调制基带信号 标量 | 向量

BPSK 调制基带信号，返回为复数值标量或向量。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **相位偏移 (rad)** — 第 0 个点的相位偏移 `0` (默认) | 标量

星座图第 0 个点的相位偏移，以 rad 为单位，指定为标量。

**示例：** `pi/4`

### **查看星座图** — 用于绘制参考星座图的按钮选项

单击模块封装上的 **查看星座图**，以可视化指定模块参数的信号星座图。在查看星座图之前，请应用参数设置。有关详细信息，请参阅查看调制器模块的星座图。

### 数据类型

### **输出数据类型** — 输出数据类型 `double` (默认) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit via back propagation` | `<data type expression>`

输出数据类型，指定为 `double`、`single`、`fixdt(1,16)`、`fixdt(1,16,0)`、`Inherit via back propagation` 或 `<data type expression>`。

将此参数设置为

- `fixdt(1,16)`、
  `fixdt(1,16,0)` 或
  `<data type expression>` 将启用
  可进一步指定详细信息的参数。
- `Inherit via back propagation` 会将
  输出数据类型和定标设置为匹配后续
  模块。

有关指定数据类型的信息，请参阅数据类型助手。

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
| a ufix(ceil(log2(M))) 仅在输入处用于 M 元调制。  b 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 BPSK 方法进行调制

BPSK Modulator Baseband 模块使用二进制相移键控 (BPSK) 方法对信号进行调制。输出是已调制信号的基带表示。输入信号必须是离散时间二值信号。如果输入位为 0 或 1，则已调制符号分别为 exp(jϕ) 或 -exp(jϕ)。`Phase offset (rad)` 参数指定 ϕ 的值，以 rad 为单位。
