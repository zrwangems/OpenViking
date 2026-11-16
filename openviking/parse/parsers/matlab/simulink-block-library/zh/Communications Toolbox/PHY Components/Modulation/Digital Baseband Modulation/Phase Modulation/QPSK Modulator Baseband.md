---
type: simulink-block
title: 'QPSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Phase Modulation'
documentation_page: 'qpskmodulatorbaseband'
documentation_source_path: 'ref/qpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# QPSK Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

- 当您将 **Input type** 设置为 `Integer` 时，请将输入信号元素指定为范围 [0, 3] 内的整数。
- 当您将 **Input type** 设置为 `Bit` 时，请将输入信号指定为包含偶数个元素的二进制向量，以确保得到整数个 2-bit QPSK 调制符号。

此端口在模块上未命名。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### 输出

### **Out** — QPSK 调制基带信号 标量 | 向量

QPSK 调制基带信号，返回为复数值标量或向量。输出是 QPSK 调制信号的复基带表示。

此端口在模块上未命名。

**数据类型：** `double` | `single` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Input type** — 整数或位对输入指示符 `Integer` (默认) | `Bit`

整数或位对输入指示符，指定为 `Integer` 或 `Bit`。

### **Constellation ordering** — 符号映射 `Gray` (默认) | `Binary`

整数或位对输入的符号映射，指定为 `Gray` 或 `Binary`。

- 要使用 Gray 编码顺序映射符号，请将此参数设置为 `Gray`。
- 要使用二进制编码顺序映射符号，请将此参数设置为 `Binary`。

有关详细信息，请参阅 Integer-Valued Signals and Binary-Valued Signals。

### **Phase offset (rad)** — 第零点的相位偏移 `pi/4` (默认) | 标量

信号星座第零点的相位，以弧度为单位，指定为标量。

### **View constellation** — 用于绘制参考星座的按钮选项

点击模块封装上的 **View Constellation**，可视化指定模块参数的信号星座。查看星座之前，请应用参数设置。有关详细信息，请参阅 View Constellation of Modulator Block。

### 数据类型

### **Output data type** — 输出数据类型 `double` (默认) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit via back propagation` | `<data type expression>`

输出数据类型，指定为 `double`、`single`、`fixdt(1,16)`、`fixdt(1,16,0)`、`Inherit via back propagation` 或 `<data type expression>`。

- `fixdt(1,16)`、`fixdt(1,16,0)` 或 `<data type expression>` 会启用可在其中进一步指定详细信息的参数。
- `Inherit via back propagation` 将输出数据类型和定标设置为匹配后续模块。

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
| a 如果 ''input type'' 设置为 ''bit''，则在输入处为 ufix(1)。如果 ''input type'' 设置为 ''integer'' 以进行 M-ary 调制，则在输入处为 ufix(ceil(log2(M)))。  b 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**R2006a 之前引入**

## 描述

使用正交相移键控方法进行调制

QPSK Modulator Baseband 模块使用正交相移键控 (QPSK) 方法调制信号。输出是调制信号的基带表示。此模块接受标量或列向量输入信号。有关数据类型的信息，请参阅 Supported Data Types。
