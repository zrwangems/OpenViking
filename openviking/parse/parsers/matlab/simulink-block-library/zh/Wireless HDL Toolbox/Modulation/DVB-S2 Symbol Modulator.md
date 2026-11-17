---
type: simulink-block
title: 'DVB-S2 Symbol Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'dvbs2symbolmodulator'
documentation_source_path: 'ref/dvbs2symbolmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# DVB-S2 Symbol Modulator

## 端口

### 输入

### **data** — 数据比特 布尔标量 | 实数标量

输入数据比特，指定为布尔标量或实数标量。该模块接受
`Boolean` 或 `ufix1` 数据比特。

**数据类型：** `Boolean` | `fixdt(0,1,0)`

### **valid** — 输入数据是否有效的指示 `0` | `1`

控制信号，用于指示输入数据是否有效。当该值为
`1` 时，模块接受 **data**
输入端口上的值。当该值为 `0` 时，模块忽略
**data** 输入端口上的值。

**数据类型：** `Boolean`

### **modIdx** — 调制索引 `0` | `1` | `2` | `3` | `4`

调制索引，指定为 `0`、`1`、
`2`、`3` 或 `4`。每个值
代表一种特定的调制类型，如下表所示。

| 调制索引 | 调制类型 |
| --- | --- |
| `0` | QPSK |
| `1` | 8-PSK |
| `2` | 16-APSK |
| `3` | 32-APSK |
| `4` | π/2-BPSK |

对于 HDL 代码生成，请以 `fixdt(0,3,0)`
格式指定该值。

如果指定的值不是此表中列出的值，模块将显示一条警告消息，并且：

- 当 **load** 为
  `1` 时，应用 QPSK 调制。
- 当 **load** 为
  `0` 时，继续使用当前调制。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为
`Input port`。

**数据类型：** `single` | `double` | `fixdt(0,3,0)`

### **codeRateIdx** — 码率索引 `5` | `6` | `7` | `8` | `9` | `10`

码率索引，指定为 `5`、`6`、
`7`、`8`、`9` 或
`10`。每个值代表一种特定的码率，如下表所示。

| 码率索引 | 码率 |
| --- | --- |
| `5` | 2/3 |
| `6` | 3/4 |
| `7` | 4/5 |
| `8` | 5/6 |
| `9` | 8/9 |
| `10` | 9/10 |

如果为 16-APSK 指定的值不是 `5`、`6`、
`7`、`8`、`9` 或
`10`，或者为 32-APSK 指定的值不是 `6`、
`7`、`8`、`9` 或
`10`，模块将显示一条警告消息并应用
码率 3/4。对于 HDL 代码生成，请以
`fixdt(0,4,0)` 格式指定该值。

此表中的码率适用于 **modIdx** 输入端口
值 `2` 和 `3`，它们分别表示 16-APSK 和
32-APSK 调制。当您将 **modIdx** 端口
值设置为 `0`、`1` 或 `4` 时，
模块忽略 **codeRateIdx** 输入端口值。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为
`Input port`。

**数据类型：** `single` | `double` | `fixdt(0,4,0)`

### **load** — 调制和码率控制 `0` | `1`

调制和码率控制，指定为布尔标量。

当该值为 `1` 时，模块采样
**modIdx** 和 **codeRateIdx** 值。当该
值为 `0` 时，模块忽略
**modIdx** 和 **codeRateIdx** 中的任何变化，并继续
使用当前调制索引和码率，直到 **load** 变为
`1`。

如果 **load** 值在模块运行期间变为 `1`，模块将重新同步并使用当前
**modIdx** 值重新开始调制。无论
**modIdx** 值是否变化，都会发生此重启。

如果在模块运行开始时未将 **load** 值指定为 `1`，
则默认情况下，模块以 QPSK
调制运行。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为
`Input port`。

**数据类型：** `Boolean`
### 输出

### **data** — 调制星座数据符号 复标量

调制星座数据符号，以复标量形式返回。

该模块支持 `double` 和
`single` 数据类型用于仿真，但不支持用于 HDL 代码
生成。

对于 HDL 代码生成，请将 **Output data type** 参数
设置为 `Custom` 并指定字长。

**数据类型：** `single` | `double` | `fixdt(1,wordlength,wordlength-2)`
**支持复数：** 是

### **valid** — 有效输出数据指示 `0` | `1`

控制信号，用于指示 **data** 输出端口的数据是否有效。当该值为 `1` 时，模块在 **data** 输出端口返回有效数据。当该值为 `0` 时，**data** 输出端口上的值无效。

**数据类型：** `Boolean`

## 参数

### 主

### **Modulation source** — 调制类型的来源 `Property`（默认）| `Input port`

要使用 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时使用 **modIdx** 端口指定调制，请选择 `Input port`。

### **Modulation** — 调制类型 `QPSK`（默认）| `8-PSK` | `16-APSK` | `32-APSK` | `pi/2-BPSK`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### **Code rate** — 码率 `3/4`（默认）| `2/3` | `4/5` | `5/6` | `8/9` | `9/10`

选择码率。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`，并将 **Modulation** 参数设置为 `16-APSK` 或 `32-APSK`。

### **Unit average power** — 频谱增长降低 `off`（默认）| `on`

选择此参数以使用归一化星座图执行符号调制。清除此参数以使用标准 [1] 中定义的星座图执行符号调制。

当您在 **modIdx** 输入端口指定 `0`、`1` 或 `4`，或将 **Modulation** 参数设置为 `QPSK`、`8-PSK` 或 `pi/2-BPSK` 时，模块在其操作期间忽略此参数。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，或将 **Modulation source** 设置为 `Property` 并将 **Modulation** 参数设置为 `16-APSK` 或 `32-APSK`。

### 数据类型

### **Output data type** — 输出数据类型 `Custom`（默认）| `double` | `single`

指定输出数据的数据类型。

模块支持 `double` 和 `single` 数据类型用于仿真。

对于仿真和 HDL 代码生成，请将此值设置为 `Custom`。

### **Word length** — 字长 `16`（默认）| 范围 [3, 32] 内的整数

指定输出字长。此值必须是范围 [3, 32] 内的整数。

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

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2022b 中引入**

### R2023b：输出数据类型默认设置的变更

**Output data type** 参数的默认值现在更改为 `Custom`。要查看此变更，请双击该模块，然后单击 **Data Types** 选项卡。

## 描述

根据 DVB-S2 标准将数据比特调制为复星座符号

DVB-S2 Symbol Modulator 模块基于数字视频广播卫星第二代（DVB-S2）标准 [1] 所支持的调制类型，将数据比特调制为复数据符号。该模块接受数据比特和 `valid` 信号，并输出调制后的复星座符号和 `valid` 信号。

每个复输出符号包含基于调制类型的标准数据比特数，如下表所示。如果您提供的输入数据比特数不是每符号数据比特数的整数倍，则该模块会忽略比特数不足或多余的输出符号。

| 调制类型 | 每符号数据比特数 |
| --- | --- |
| π/2-BPSK | 1 |
| QPSK | 2 |
| 8-PSK | 3 |
| 16-APSK | 4 |
| 32-APSK | 5 |

该模块提供适用于 HDL 代码生成和硬件部署的架构。您可以在 DVB-S2 发射机的开发中使用该模块。
