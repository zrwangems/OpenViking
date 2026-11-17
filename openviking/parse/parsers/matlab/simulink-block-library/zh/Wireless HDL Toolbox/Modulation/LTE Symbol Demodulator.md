---
type: simulink-block
title: 'LTE Symbol Demodulator'
family: 'modulation'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ltesymboldemodulator'
documentation_source_path: 'ref/ltesymboldemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Symbol Demodulator

## 端口

### 输入

### **data** — 输入数据符号，复标量

输入数据符号，指定为复标量。该模块执行解调，假设输入星座功率归一化符合 LTE 标准 TS 36.211 第 7.1 节 [1]。归一化值基于调制类型。

- BPSK 和 QPSK 为 1/√2
- 16-QAM 为 1/√10
- 64-QAM 为 1/√42
- 256-QAM 为 1/√170

**示例：** 对于 BPSK 调制，输入值可以为 `[0.707 +0.707i; -0.707 -0.707i]`

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

对于 HDL 代码生成，输入数据类型必须为 `signed fixed point`，并且该模块支持的最大输入字长为 32 bits。

**数据类型：** `single` | `double` | `signed fixed point`
**复数支持：** Yes

### **valid** — 有效输入数据指示，标量

控制信号，指示输入数据是否有效。当此值为 `1` (true) 时，该模块接受 **data** 输入端口上的值。当此值为 `0` (false) 时，该模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **modSel** — 调制选择，0 到 4 的整数

通过指定此表中显示的对应值来选择调制类型。有效的 **modSel** 值为 0 到 4。每个值表示一种特定调制类型，如此表所示。

| Value | Modulation Type |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 16-QAM |
| `3` | 64-QAM |
| `4` | 256-QAM |

如果您指定的值不是此表中列出的值，该模块将显示警告消息并应用 QPSK 调制。

对于 HDL 代码生成，请以 `fixdt(0,3,0)` 格式指定此值。`double` 和 `single` 数据类型支持用于仿真，但不支持 HDL 代码生成。

#### 依赖项

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `signed fixed point`

### 输出

### **data** — 输出解调数据位或 LLR 值，标量

输出解调数据位或 LLR 值，以标量形式返回。

- 当您将 **Decision type** 参数设置为 `Soft` 时，该模块输出解调后的 LLR 值。正的 LLR 输出值被视为 1，负的 LLR 输出值被视为 0。输出幅度给出解调位的 LLR 的分段线性近似。用于 LLR 近似的算法在 [1] 中描述。对于位于这些星座点上的输入信号，返回的 LLR 值处于这些幅度范围内。

  - BPSK 为 1
  - QPSK 为 1/√2
  - 16-QAM 为 [1 3]/√10
  - 64-QAM 为 [1 3 5 7]/√42
  - 256-QAM 为 [1 3 5 7 9 11 13 15]/√170

  对于数据类型为 `signed fixed point` 的输入，输出字长增加 2 bits。对于数据类型为 `double` 或 `single` 的输入，输出数据类型与输入数据类型相同。

- 当您将 **Decision type** 参数设置为 `Hard` 时，该模块的输出包含与输入最接近的星座点相对应的位序列。此输出的数据类型为 `Boolean`。

**数据类型：** `single` | `double` | `signed fixed point` | `Boolean`

### **valid** — 有效输出数据指示，标量

控制信号，指示来自 **data** 输出端口的数据是否有效。当此值为 `1` (true) 时，该模块在 **data** 输出端口上返回有效数据。当此值为 `0` (false) 时，**data** 输出端口上的值无效。

**数据类型：** `Boolean`

### **ready** — 模块就绪指示，标量

控制信号，指示该模块何时准备好接受新的输入数据。当此值为 `1` (true) 时，该模块在下一时间步接受输入数据。当此值为 `0` (false) 时，该模块在下一时间步忽略输入数据。

**ready** 信号保持 `0` (false)，直到该模块输出对应输入数据符号的数据。**ready** 信号保持 `0` (false) 的 clock cycles 数取决于所选的调制类型。如果所选调制类型为 16-QAM，**ready** 信号保持 `0` (false) 3 clock cycles，计算为 *NBPS* – 1，然后变为 `1` (true)，指示该模块已准备好在下一时间步接受数据。

**数据类型：** `Boolean`

## 参数

### **Modulation source** — 调制类型的来源 `Property` (default) | `Input port`

要使用 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时从 **modSel** 端口指定调制类型，请选择 `Input port`。

### **Modulation** — 调制类型 `BPSK` (default) | `QPSK` | `16-QAM` | `64-QAM` | `256-QAM`

选择调制类型。

#### 依赖项

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### **Decision type** — 解映射类型 `Soft` (default) | `Hard`

选择解映射类型。

- `Soft` — 将数据符号解映射为 LLR 值。每个位的此 LLR 值指示该位为 `1` 或 `0` 的可能性。
- `Hard` — 将数据符号解映射为位 `1` 或 `0`。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。有关舍入模式的详细信息，请参阅 Rounding Modes。当输入的数据类型为 `double` 或 `single` 时，此参数不适用。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

此模块没有任何 HDL Block Properties。

## 版本历史

**在 R2019b 中引入**

## 描述

将复 LTE 数据符号解调为数据位或 LLR 值

LTE Symbol Demodulator 模块基于 LTE 标准 TS 36.211 [1] 支持的调制类型，将复数据符号解调为数据位或对数似然比 (LLR) 值。该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在 LTE 接收机开发中使用此模块。

该模块接受数据符号以及 valid 信号，并输出带有 valid 和 ready 信号的解调位或 LLR 值。给定符号的解调位或 LLR 值的数量取决于调制类型，如下表所示。

| 调制类型 | 每个符号的 Bits 数 (NBPS) |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |

**ready** 输出端口指示该模块何时可以接受输入数据样本。您可以使用 **ready** 输出端口控制进入该模块的上游数据。
