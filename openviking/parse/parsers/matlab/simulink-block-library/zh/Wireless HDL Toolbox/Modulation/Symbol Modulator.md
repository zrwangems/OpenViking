---
type: simulink-block
title: 'Symbol Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'symbolmodulator'
documentation_source_path: 'ref/symbolmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Symbol Modulator

## 端口

### 输入

### **data** — 数据位 标量 | 列向量

数据位，指定为标量或列向量。

输入数据位必须是 *NBPS* 的倍数，其中 *NBPS* 是每符号的位数。如果指定的输入数据位不是 *NBPS* 的倍数，模块将忽略位数不足或过多的输入。

当您将 **Modulation source** 参数设置为 `Property` 时：

- 对于标量输入，数据类型必须为 `Boolean`、`fixdt(0,1,0)` 或 `fixdt(0,NBPS,0)`。
- 对于向量输入，数据类型必须为 `Boolean` 或 `fixdt(0,1,0)`。向量的维度必须为 *NBPS*×1。

当您将 **Modulation source** 参数设置为 `Input port` 时，对于标量输入，数据类型必须为 `Boolean` 或 `fixdt(0,1,0)`。此参数设置不支持向量输入。

**数据类型：** `Boolean` | `unsigned fixed point`

### **valid** — 指示有效输入数据 标量

控制信号，用于指示输入数据是否有效。当此值为 `1`（true）时，模块接受 **data** 输入端口上的值。当此值为 `0`（false）时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **modArrIdx** — 调制数组索引 整数

调制数组索引，指定为整数。此值必须与 **Modulation array** 参数的索引相对应。对于 HDL 代码生成，请以 `fixdt(0,4,0)` 格式指定该值。

例如，如果 **Modulation array** 参数指定为 `{"QPSK","BPSK,"16-QAM"}`，并且您希望模块按以下顺序执行：BPSK、16-QAM、BPSK 和 QPSK，则必须按顺序分别指定 **modArrIdx** 值为 `1`、`2`、`1` 和 `0`。此处，索引值 `0`、`1` 和 `2` 分别对应 QPSK、BPSK 和 16-QAM。

如果您指定的值超过了 **Modulation array** 参数中指定的调制类型索引，模块将显示警告消息并：

- 当 **load** 为 `1`（true）时，应用 **Modulation array** 参数中第一个指定的调制。
- 当 **load** 为 `0`（false）时，继续使用先前的调制。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `double` | `single` | `fixdt(0,4,0)`

### **load** — 调制控制 标量

用于采样调制的调制控制信号，指定为 `Boolean` 标量。

当此值为 `1`（true）时，模块根据 **modArrIdx** 值应用调制。当此值为 `0`（false）时，模块忽略 **modArrIdx** 值的任何变化，并继续使用先前的调制，直到此值变为 `1`（true）。

如果 **load** 值在模块操作期间变为 `1`（true），模块将重新同步并使用 **modArrIdx** 的当前值重新开始调制。无论 **modArrIdx** 值是否发生变化，都会发生此重新启动。

例如，如果模块正在 256-QAM 模式下运行，并且在所需的八个输入位中的四个位发送到模块后 **load** 值变为 `1`（true），模块将丢弃前四个位并从第五个位重新开始操作。

如果您在模块操作开始时未将 **load** 值应用为 `1`（true），则默认情况下，模块应用 **Modulation array** 参数中第一个指定的调制。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

清除内部状态，指定为 `Boolean` 标量。当此值为 `1` 时，模块停止当前计算并清除所有内部状态。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Property`，然后选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 调制后的复数据符号 复标量

调制后的复数据符号，以复标量形式返回。

该模块在仿真中支持 `double` 和 `single` 数据类型，但不支持 HDL 代码生成。

对于 HDL 代码生成，请将 **Output data type** 参数设置为 `Custom` 并指定字长。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** 是

### **valid** — 有效输出数据指示 标量

控制信号，用于指示 **data** 输出端口的数据是否有效。当该值为 `1`（真）时，模块在 **data** 输出端口返回有效数据。当该值为 `0`（假）时，**data** 输出端口上的值无效。

**数据类型：** `Boolean`

## 参数

### 主要

### **Modulation source** — 调制类型的来源 `Property`（默认）| `Input port`

要通过 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时通过 **modArrIdx** 端口指定调制类型，请选择 `Input port`。

### **Modulation** — 调制类型 `BPSK`（默认）| `QPSK` | `8-PSK` | `16-PSK` | `16-QAM` | `32-PSK` | `64-QAM` | `256-QAM` | `1024-QAM` | `4096-QAM`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### **Modulation array** — 调制数组 `{"BPSK", "QPSK"}`（默认）| 所有支持的调制类型

以元胞数组格式的字符串指定调制类型。支持的调制类型包括：BPSK、QPSK、8-PSK、16-PSK、16-QAM、32-PSK、64-QAM、256-QAM、1024-QAM 和 4096-QAM。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`。

### **Constellation ordering type** — 星座排序类型 `Default`（默认）| `User-defined`

选择星座排序类型为 `Default` 或 `User-defined`。

### **Constellation mapping** — 星座映射 `[0 1]`（默认）| 行向量

以行向量指定星座映射。该行向量必须包含范围 [0, (*M* – 1)] 内的唯一元素，其中 *M* 为调制阶数。向量的维度必须为 1×*M*。

对于 QAM 调制，第一个元素对应星座图的左上点，后续元素按列从左到右依次排列。如果将 **Modulation** 参数设置为 `16-QAM`，则调制阶数为 16，向量维度为 1×16。该向量必须包含范围 [0, 15] 内的唯一元素。

**示例：** `[0 1 3 2 4 5 7 6 12 13 15 14 8 9 11 10]`

对于 PSK 调制，第一个元素对应 **Phase offset (rad)** 参数中指定角度所对应的星座点，后续元素按逆时针方向依次排列。如果将 **Modulation** 参数设置为 `8-PSK`，则调制阶数为 8，向量维度为 1×8。该向量必须包含范围 [0, 7] 内的唯一元素。

**示例：** `[0 1 3 2 6 7 5 4]`

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`，然后将 **Constellation ordering type** 参数设置为 `User-defined`。

### **Constellation mapping array** — 星座映射数组 `{[0 1],[0 1 3 2]}`（默认）| 元胞数组中的行向量

以元胞数组中的行向量指定星座映射数组。元胞数组的大小必须等于调制数组的大小。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，然后将 **Constellation ordering type** 参数设置为 `User-defined`。

### **Phase offset (rad)** — 相位偏移 `0`（默认）| `pi` | `pi/2` | `pi/4` | `pi/8` | `pi/16` | `pi/32` | `-pi/32` | `-pi/16` | `-pi/8` | `-pi/4` | `-pi/2`

选择相位偏移。此参数仅适用于 PSK 调制类型，即 BPSK、QPSK、8-PSK、16-PSK 和 32-PSK。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`，并将 **Modulation** 参数设置为 `BPSK`、`QPSK`、`8-PSK`、`16-PSK` 或 `32-PSK`。

### **Phase offset type** — 相位偏移类型 `Default`（默认）| `User-defined`

选择相位偏移类型为 `Default` 或 `User-defined`。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`。

### **Phase offset array (rad)** — 相位偏移数组 `[0 pi/4]`（默认）| 标量 | 支持的相位偏移值的行向量

指定相位偏移数组。支持的相位偏移值为：`pi`、`pi/2`、`pi/4`、`pi/8`、`pi/16`、`pi/32`、`0`、`-pi/2`、`-pi/4`、`-pi/8`、`-pi/16` 和 `-pi/32`。此参数仅适用于 PSK 调制。

**注意**

如果在 **Modulation array** 中指定 16-QAM、64-QAM、256-QAM、1024-QAM 或 4096-QAM，则必须在 **Phase offset array (rad)** 参数中为每个 QAM 指定 `0`。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，然后将 **Phase offset type** 参数设置为 `User-defined`。

### **Normalization method** — 缩放信号星座图 `Minimum distance between symbols`（默认）| `Average power`

选择模块如何缩放信号星座图。

- `Minimum distance between symbols` — 使您能够通过 **Minimum distance** 参数指定星座点之间的最小距离来归一化星座图。
- `Average power` — 使用 **Average power, referenced to 1 ohm (watts)** 参数将星座图归一化为平均功率。

#### 依赖关系

要启用此参数：

- 将 **Modulation source** 参数设置为 `Input port`。或
- 将 **Modulation source** 参数设置为 `Property`，然后将 **Modulation** 参数设置为 `16-QAM`、`64-QAM`、`256-QAM`、`1024-QAM` 或 `4096-QAM`。

### **Minimum distance** — 符号之间的最小距离 `0.125`（默认）| 范围从 1/32 到 1/8 的正标量

将符号之间的最小距离指定为范围从 1/32 到 1/8 的正标量。

#### 依赖关系

要启用此参数：

- 将 **Modulation source** 参数设置为 `Input port`，然后将 **Normalization method** 参数设置为 `Minimum distance between symbols`。或
- 将 **Modulation source** 参数设置为 `Property`，将 **Modulation** 参数设置为 `16-QAM`、`64-QAM`、`256-QAM`、`1024-QAM` 或 `4096-QAM`，然后将 **Normalization method** 参数设置为 `Minimum distance between symbols`。

### **Average power, referenced to 1 ohm (watts)** — 星座图中符号的平均功率 `1`（默认）| 范围从 1/32 到 10 的正标量

将星座图中符号的平均功率指定为范围从 1/32 到 10 的正标量。功率值假定标称阻抗为 1 欧姆。

#### 依赖关系

要启用此参数：

- 将 **Modulation source** 参数设置为 `Input port`，然后将 **Normalization method** 参数设置为 `Average power`。或
- 将 **Modulation source** 参数设置为 `Property`，将 **Modulation** 参数设置为 `16-QAM`、`64-QAM`、`256-QAM`、`1024-QAM` 或 `4096-QAM`，然后将 **Normalization method** 参数设置为 `Average power`。

### **Enable reset input port** — 复位输入端口 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### 数据类型

### **Output data type** — 输出数据类型选择 `Custom`（默认）| `double` | `single`

选择输出数据的数据类型。

`double` 和 `single` 数据类型支持仿真。对于仿真和 HDL 代码生成，请将此值设置为 `Custom`。

### **Word length** — 输出字长 `16`（默认）| 3 到 32 范围内的整数

指定输出字长。该值必须是 3 到 32 范围内的整数。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Custom`。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2025a 中引入**

## 描述

将数据比特调制为复数据符号

Symbol Modulator 模块将数据比特调制为复数据符号。该模块接受数据比特以及控制信号，并输出带有有效信号的调制复符号。每个复符号包含基于调制类型的标准比特数，如下表所示。调制阶数指定信号星座图中的点数。

| 调制类型 | 每符号比特数 (NBPS) | 调制阶数 |
| --- | --- | --- |
| BPSK | 1 | 2 |
| QPSK | 2 | 4 |
| 8-PSK | 3 | 8 |
| 16-PSK | 4 | 16 |
| 16-QAM | 4 | 16 |
| 32-PSK | 5 | 32 |
| 64-QAM | 6 | 64 |
| 256-QAM | 8 | 256 |
| 1024-QAM | 10 | 1024 |
| 4096-QAM | 12 | 4096 |

当您将 **Modulation source** 参数设置为 `Property` 时，该模块支持标量和向量输入。当您将 **Modulation source** 参数设置为 `Input port` 时，它仅支持标量输入。您可以使用此模块开发数字通信系统中的发射机。该模块提供适合 HDL 代码生成和硬件部署的架构。
