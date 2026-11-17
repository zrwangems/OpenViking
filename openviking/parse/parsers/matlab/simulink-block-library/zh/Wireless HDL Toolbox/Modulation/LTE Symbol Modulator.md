---
type: simulink-block
title: 'LTE Symbol Modulator'
family: 'modulation'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ltesymbolmodulator'
documentation_source_path: 'ref/ltesymbolmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Symbol Modulator

## 端口

### 输入

### **data** — 输入数据比特标量

输入数据比特，指定为标量。该模块接受 `Boolean` 或 `ufix1` 数据比特。

**数据类型：** `Boolean` | `fixdt(0,1,0)`

### **valid** — 指示有效输入数据标量

控制信号，用于指示输入数据是否有效。当此值为 `1` (true) 时，该模块接受 **data** 输入端口上的值。当此值为 `0` (false) 时，该模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **modSel** — 调制选择整数

通过指定下表中显示的对应值来选择调制类型。

**modSel** 值为 0 到 4。每个值代表一种特定调制类型。

| 值 | 调制类型 |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 16-QAM |
| `3` | 64-QAM |
| `4` | 256-QAM |

如果您指定的值不是此表中列出的值，则该模块会显示警告消息，并且：

- 当 **load** 为 `1` (true) 时应用 QPSK 调制。
- 当 **load** 为 `0` (false) 时继续使用当前调制。

对于 HDL 代码生成，请以 `fixdt(0,3,0)` 格式指定此值。

#### 依赖关系

要启用此端口，请将 **调制源** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,3,0)` | `double` | `single`

### **load** — 调制控制标量

用于采样调制的控制信号。

当此值为 `1` (true) 时，该模块基于 **modSel** 值应用调制。当此值为 `0` (false) 时，该模块忽略 **modSel** 值的任何变化，并继续使用当前调制，直到 **load** 变为 `1` (true)。

如果 **load** 值在模块操作期间变为 `1` (true)，则该模块会重新同步并使用 **modSel** 的当前值重新开始调制。无论 **modSel** 值是否已更改，都会发生此重新开始。例如，如果该模块正在 256-QAM 模式下运行，并且在发送八个所需输入比特中的四个之后 **load** 值变为 `1` (true)，则该模块会丢弃前四个比特，并从第五个比特重新开始其操作。

如果您在模块操作开始时未将 **load** 值应用为 `1` (true)，则默认情况下，该模块以 QPSK 调制运行。

#### 依赖关系

要启用此端口，请将 **调制源** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### 输出

### **data** — 调制复数据符号标量

调制复数据符号，以标量形式返回。

**数据类型：** `single` | `double` | `fixdt(1,wordlength,wordlength-2)`  
**复数支持：** Yes

### **valid** — 有效输出数据指示标量

控制信号，用于指示来自 **data** 输出端口的数据是否有效。当此值为 `1` (true) 时，该模块在 **data** 输出端口上返回有效数据。当此值为 `0` (false) 时，该模块忽略 **data** 输出端口上的值。

**数据类型：** `Boolean`

## 参数

### 主要

### **调制源** — 调制类型的源 `Property` (默认) | `Input port`

要使用 **调制** 参数指定调制类型，请选择 `Property`。要在运行时从 **modSel** 端口指定调制类型，请选择 `Input port`。

### **调制** — 调制类型 `BPSK` (默认) | `QPSK` | `16-QAM` | `64-QAM` | `256-QAM`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **调制源** 参数设置为 `Property`。

### 数据类型

### **输出数据类型** — 输出数据类型选择 `Custom` (默认) | `double` | `single`

指定输出数据的数据类型。

`double` 和 `single` 数据类型支持仿真。

对于仿真和 HDL 代码生成，请将此值设置为 `Custom`。

### **字长** — 输出字长 `16` (默认) | [3, 32] 范围内的整数

指定输出字长。此值必须是 [3, 32] 范围内的整数。

#### 依赖关系

要启用此参数，请将 **输出数据类型** 参数设置为 `Custom`。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink® 加速器和快速加速器模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

此模块没有任何 HDL Block Properties。

## 版本历史

**在 R2019a 中引入**

### R2023b：输出数据类型默认设置更改

**输出数据类型** 参数的默认值现已更改为 `Custom`。要查看此更改，请双击该模块，然后单击 **数据类型** 选项卡。

## 描述

将数据比特调制为复 LTE 数据符号

LTE Symbol Modulator 模块使用 LTE 标准 TS 36.211 [1] 支持的调制类型，将一组数据比特映射为复数据符号。该模块提供适用于 HDL 代码生成和硬件部署的架构。您可以在 LTE 发射机的开发中使用此模块。

该模块一次接受 1 位数据以及控制信号，并输出带 valid 信号的调制复符号。每个复符号包含基于调制类型的标准比特数，如下表所示。如果您提供的输入不是调制阶数的倍数个比特，则该模块会忽略比特不足或过多的输出符号。调制阶数是每个符号的比特数。

| 调制类型 | 调制阶数 - 每个符号的比特数 |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |
