---
type: simulink-block
title: 'NR Symbol Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'nrsymboldemodulator'
documentation_source_path: 'ref/nrsymboldemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# NR Symbol Demodulator

## 端口
```yaml
ports:
- name: data
  summary: 输入数据符号 复标量
  direction: input
  data_types: single | double | signed fixed point
- name: valid
  summary: 指示有效输入数据 标量
  direction: input
  data_types: Boolean
- name: modSel
  summary: 调制选择 从 0 到 5 的整数
  direction: input
  data_types: single | double | signed fixed point
- name: data
  summary: 解调数据位或 LLR 值 标量
  direction: output
  data_types: single | double | signed fixed point | Boolean
- name: valid
  summary: 有效输出数据指示 标量
  direction: output
  data_types: Boolean
- name: ready
  summary: 指示模块已就绪的标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据符号 复标量

输入数据符号，指定为复标量。该模块执行解调时假设输入星座图功率归一化符合 NR 标准 TS 38.211 第 5.1 节 [1]。归一化值基于调制类型。

- BPSK、QPSK 和 pi/2-BPSK 为 1/√2
- 16-QAM 为 1/√10
- 64-QAM 为 1/√42
- 256-QAM 为 1/√170

**示例：** 对于 BPSK 调制，输入值可以是 `[0.707 +0.707i;
-0.707 -0.707i]`

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

对于 HDL 代码生成，输入数据类型必须为 `signed fixed
point`，且该模块支持的最大输入字长为 32 位。

**数据类型：** `single` | `double` | `signed fixed point`
**支持复数：** 是

### **valid** — 指示有效输入数据 标量

控制信号，用于指示输入数据是否有效。当该值为 `1`（真）时，模块接受 **data** 输入端口上的值。当该值为 `0`（假）时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **modSel** — 调制选择 从 0 到 5 的整数

通过指定下表中对应的值来选择调制类型。有效的 **modSel** 值为 0 到 5。每个值代表一种特定的调制类型，如下表所示。

| 值 | 调制类型 |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 16-QAM |
| `3` | 64-QAM |
| `4` | 256-QAM |
| `5` | pi/2-BPSK |

如果指定的值不在此表中，模块将显示警告消息并应用 QPSK 调制。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

对于 HDL 代码生成，请以 `fixdt(0,3,0)` 格式指定此值。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `signed fixed point`
### 输出

### **data** — 解调数据位或 LLR 值 标量

输出解调数据位或 LLR 值，以标量形式返回。

- 当将 **Decision type** 参数设置为 `Soft` 时，模块输出解调后的 LLR 值。正的 LLR 输出值被视为 0，负的 LLR 输出值被视为 1。输出的幅度给出了解调比特 LLR 的分段线性近似。用于 LLR 近似的算法在 [1] 中描述。模块根据调制类型使用相应的缩放因子对返回的 LLR 进行缩放，如下表所示。

  | 调制类型 | 缩放因子 |
  | --- | --- |
  | BPSK | 4/√2 |
  | QPSK | 4/√2 |
  | 16-QAM | [4 8]/√10 |
  | 64-QAM | [4 8 12 16]/√42 |
  | 256-QAM | [4 8 12 16 20 24 28 32]/√170 |
  | pi/2-BPSK | 4/√2 |

  对于数据类型为 `signed fixed point` 的输入，输出字长增加 3 位。对于数据类型为 `double` 或 `single` 的输入，输出数据类型与输入数据类型相同。
- 当将 **Decision type** 参数设置为 `Hard` 时，模块输出的结果包含与输入最接近的星座点对应的比特序列。此输出的数据类型为 `Boolean`。

**数据类型：** `single` | `double` | `signed fixed point` | `Boolean`

### **valid** — 有效输出数据指示 标量

控制信号，用于指示 **data** 输出端口的数据是否有效。当该值为 `1`（真）时，模块在 **data** 输出端口上返回有效数据。当该值为 `0`（假）时，**data** 输出端口上的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪的标量

控制信号，指示模块何时准备好接受新的输入数据。
当该值为 `1`（true）时，模块在下一个时间步接受输入数据。当该值为 `0`（false）时，模块在下一个时间步忽略输入数据。

**ready** 信号保持为 `0`（false），直到模块输出对应输入数据符号的数据。**ready** 信号保持为 `0`（false）的时钟周期数取决于所选的调制类型。如果所选调制类型为 16-QAM，则 **ready** 信号保持为 `0`（false）3 个时钟周期，计算方式为 *NBPS* – 1，然后变为 `1`（true），表示模块已准备好在下个时间步接受数据。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Modulation source
  summary: 调制类型的来源 Property（默认）| Input port
  group: ''
- name: Modulation
  summary: 调制类型 BPSK（默认）| QPSK | 16-QAM | 64-QAM | 256-QAM | pi/2-BPSK
  group: ''
- name: Decision type
  summary: 解映射类型 Soft（默认）| Hard
  group: ''
- name: Rounding Method
  summary: 内部定点计算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: ''
```

### **Modulation source** — 调制类型的来源 `Property`（默认）| `Input port`

要通过 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时从 **modSel** 端口指定调制类型，请选择 `Input port`。

### **Modulation** — 调制类型 `BPSK`（默认）| `QPSK` | `16-QAM` | `64-QAM` | `256-QAM` | `pi/2-BPSK`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### **Decision type** — 解映射类型 `Soft`（默认）| `Hard`

选择解映射类型。

- `Soft` — 将数据符号解映射为 LLR 值。每个比特的 LLR 值指示该比特为 `1` 或 `0` 的可能性。
- `Hard` — 将数据符号解映射为比特 `1` 或 `0`。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。有关舍入模式的详细信息，请参阅舍入模式。当输入数据类型为 `double` 或 `single` 时，此参数不适用。
## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

此模块没有任何 HDL Block Properties。

## 版本历史

**在 R2019b 中引入**

## 描述

将复 NR 数据符号解调为数据比特或 LLR 值

NR Symbol Demodulator 模块基于 5G 新无线电（NR）标准 TS 38.211 [1] 支持的调制类型，将复数据符号解调为数据比特或对数似然比（LLR）值。该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在 NR 接收机的开发中使用此模块。

该模块接受数据符号以及有效信号，并输出带有 valid 和 ready 信号的解调比特或 LLR 值。给定符号的解调比特或 LLR 值的数量取决于调制类型，如下表所示。

| 调制类型 | 每符号比特数（NBPS） |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |
| pi/2-BPSK | 1 |

**ready** 输出端口指示模块何时可以接受输入数据样本。您可以使用 **ready** 输出端口来控制进入模块的上游数据。
