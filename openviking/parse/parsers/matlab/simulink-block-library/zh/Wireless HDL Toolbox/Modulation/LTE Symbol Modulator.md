---
type: simulink-block
title: 'LTE Symbol Modulator'
family: 'wireless-hdl'
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
```yaml
ports:
- name: data
  summary: 输入数据比特 标量
  direction: input
  data_types: Boolean | fixdt(0,1,0)
- name: valid
  summary: 指示有效输入数据 标量
  direction: input
  data_types: Boolean
- name: modSel
  summary: 调制选择 整数
  direction: input
  data_types: fixdt(0,3,0) | double | single
- name: load
  summary: 调制控制 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 调制后的复数据符号 标量
  direction: output
  data_types: single | double | fixdt(1,wordlength,wordlength-2)
- name: valid
  summary: 有效输出数据指示 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据比特 标量

输入数据比特，指定为标量。该模块接受 `Boolean` 或 `ufix1` 数据比特。

**数据类型：** `Boolean` | `fixdt(0,1,0)`

### **valid** — 指示有效输入数据 标量

控制信号，用于指示输入数据是否有效。当该值为 `1`（true）时，模块接受 **data** 输入端口上的值。当该值为 `0`（false）时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **modSel** — 调制选择 整数

通过指定下表中所列的对应值来选择调制类型。

**modSel** 的值为 0 到 4。每个值代表一种特定的调制类型。

| 值 | 调制类型 |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 16-QAM |
| `3` | 64-QAM |
| `4` | 256-QAM |

如果指定的值不在此表所列范围内，模块将显示警告消息并：

- 当 **load** 为 `1`（true）时，应用 QPSK 调制。
- 当 **load** 为 `0`（false）时，继续使用当前调制。

对于 HDL 代码生成，请以 `fixdt(0,3,0)` 格式指定此值。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,3,0)` | `double` | `single`

### **load** — 调制控制 标量

用于采样调制的控制信号。

当该值为 `1`（true）时，模块根据 **modSel** 值应用调制。当该值为 `0`（false）时，模块忽略 **modSel** 值的任何变化，并继续使用当前调制，直到 **load** 变为 `1`（true）。

如果 **load** 值在模块运行期间变为 `1`（true），模块将重新同步并使用 **modSel** 的当前值重新开始调制。无论 **modSel** 值是否发生变化，此重启都会发生。例如，如果模块正在 256-QAM 模式下运行，并且在所需的八个输入比特中的四个发送到模块后 **load** 值变为 `1`（true），模块将丢弃前四个比特并从第五个比特重新开始其操作。

如果在模块运行开始时未将 **load** 值设为 `1`（true），则默认情况下，模块以 QPSK 调制运行。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `Boolean`
### 输出

### **data** — 调制后的复数据符号 标量

调制后的复数据符号，以标量形式返回。

**数据类型：** `single` | `double` | `fixdt(1,wordlength,wordlength-2)`
**支持复数：** 是

### **valid** — 有效输出数据指示 标量

控制信号，用于指示 **data** 输出端口的数据是否有效。当该值为 `1`（true）时，模块在 **data** 输出端口上返回有效数据。当该值为 `0`（false）时，模块忽略 **data** 输出端口上的值。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Modulation source
  summary: 调制类型的来源 Property（默认） | Input port
  group: 主要
- name: Modulation
  summary: 调制类型 BPSK（默认） | QPSK | 16-QAM | 64-QAM | 256-QAM
  group: 主要
- name: Output data type
  summary: 输出数据类型选择 Custom（默认） | double | single
  group: 数据类型
- name: Word length
  summary: 输出字长 16（默认） | [3, 32] 范围内的整数
  group: 数据类型
```

### 主要

### **Modulation source** — 调制类型的来源 `Property`（默认） | `Input port`

要通过 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时从 **modSel** 端口指定调制类型，请选择 `Input port`。

### **Modulation** — 调制类型 `BPSK`（默认） | `QPSK` | `16-QAM` | `64-QAM` | `256-QAM`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### 数据类型

### **Output data type** — 输出数据类型选择 `Custom`（默认） | `double` | `single`

指定输出数据的数据类型。

`double` 和 `single` 数据类型支持仿真。

对于仿真和 HDL 代码生成，请将此值设置为 `Custom`。

### **Word length** — 输出字长 `16`（默认） | [3, 32] 范围内的整数

指定输出字长。此值必须是 [3, 32] 范围内的整数。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Custom`。
## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

此模块没有任何 HDL Block Properties。

## 版本历史

**在 R2019a 中引入**

### R2023b：输出数据类型默认设置的更改

**Output data type** 参数的默认值现已更改为 `Custom`。要查看此更改，请双击模块，然后单击 **Data Types** 选项卡。

## 描述

将数据比特调制为复 LTE 数据符号

LTE Symbol Modulator 模块通过使用 LTE 标准 TS 36.211 [1] 支持的调制类型，将一组数据比特映射为复数据符号。该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在 LTE 发射机的开发中使用此模块。

该模块一次接受 1 位数据以及控制信号，并输出带有有效信号的调制复符号。每个复符号包含基于调制类型的标准比特数，如下表所示。如果您提供的输入不是调制阶数的倍数，则该模块会忽略比特不足或过多的输出符号。调制阶数是每符号的比特数。

| 调制类型 | 调制阶数 - 每符号比特数 |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |
