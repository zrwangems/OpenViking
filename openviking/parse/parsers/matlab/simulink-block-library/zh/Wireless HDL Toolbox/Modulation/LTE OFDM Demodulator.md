---
type: simulink-block
title: 'LTE OFDM Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'lteofdmdemodulator'
documentation_source_path: 'ref/lteofdmdemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE OFDM Demodulator

## 端口

### 输入

### **data** — 输入数据 标量

输入数据，指定为有符号实数或复数。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据 `Boolean` 标量

控制信号，指示 **data** 输入端口上的采样何时有效。当该值为 `1`（true）时，模块捕获 **data** 输入端口上的值。当该值为 `0`（false）时，模块忽略输入 **data** 采样。

**数据类型：** `Boolean`

### **NDLRB** — 下行资源块数量 `6` | `15` | `25` | `50` | `75` | `100`

下行资源块数量，指定为 `6`、`15`、`25`、`50`、`75` 或 `100`。NDLRB 必须是 LTE 标准 TS 36.212 [1] 规定的这六个值之一。模块在每个子帧开始时对该端口采样，并忽略子帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **NDLRB source** 参数设置为 `Input port`。

**数据类型：** `uint8` | `uint16` | `uint32` | `fixdt(0,K,0), K >= 7` | `single` | `double`

### **cyclicPrefixType** — CP 类型 标量

CP 类型，指定为 `Boolean` 标量。当该值为 `0`（false）时，模块选择常规 CP。当该值为 `1`（true）时，模块选择扩展 CP。模块在每个子帧开始时对该端口采样，并忽略子帧内的任何变化。

#### 依赖关系

要启用此端口，请将 **Cyclic prefix source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

清除内部状态，指定为 `Boolean` 标量。当该值为 `1`（true）时，模块停止当前计算并清除所有内部状态。当该值为 `0`（false）且 **valid** 输入值为 `1`（true）时，模块开始一个新的子帧。

#### 依赖关系

要启用此端口，请选中 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 输出数据 标量

输出数据，以有符号实数或复数形式返回。数据类型与输入 **data** 端口的数据类型相同。当您清除 **Divide butterfly outputs by two** 参数时，输出字长增加 11 位以避免溢出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

控制信号，指示 **data** 输出端口何时有效。当资源网格采样在 **data** 输出端口上可用时，模块将该值设置为 `1`（true）。当选中 **Remove DC subcarrier** 时，该值在输出采样的中心处设置为 `0`（false），以排除 DC 载波。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

控制信号，指示模块何时准备好接收新的输入数据。当该值为 `1`（true）时，模块在下一个时间步接受输入数据。当该值为 `0`（false）时，模块在下一个时间步忽略输入数据。

#### 依赖关系

要启用此端口，请将 **Input data sample rate** 参数设置为 `Match input data sample rate to NDLRB`。

**数据类型：** `Boolean`

## 参数

### 主要

### **NDLRB source** — NDLRB 的来源 `Property`（默认）| `Input port`

您可以通过输入端口设置 NDLRB，或通过为参数选择一个值来设置。要启用 **NDLRB** 参数，请选择 `Property`。要启用 **NDLRB** 端口，请选择 `Input port`。

### **NDLRB** — 下行资源块数量 `6`（默认）| `15` | `25` | `50` | `75` | `100`

下行资源块数量，指定为 `6`、`15`、`25`、`50`、`75` 或 `100`。NDLRB 必须是 LTE 标准 TS 36.212 [1] 规定的这六个值之一。

#### 依赖关系

要启用此参数，请将 **NDLRB source** 参数设置为 `Property`。

### **Cyclic prefix source** — 循环前缀类型的来源 `Property`（默认）| `Input port`

您可以通过选择参数值或使用输入端口来设置循环前缀。要启用 **Cyclic prefix type** 参数，请选择 `Property`。要启用 **cyclicPrefixType** 端口，请选择 `Input port`。

### **Cyclic prefix type** — 循环前缀的类型 `Normal`（默认）| `Extended`

循环前缀的类型，指定为 `Normal` 或 `Extended`。

#### 依赖关系

要启用此参数，请将 **Cyclic prefix source** 参数设置为 `Property`。

### **CP fraction** — 要移除的循环前缀百分比 `0.55`（默认）| 0 到 1 之间的值

循环前缀比例，指定为 0 到 1（含）之间的值。此参数指定模块从 OFDM 符号起始处移除的 CP 样本百分比。模块将剩余的 CP 样本移位到 OFDM 符号的末尾。

当此参数为 `0.55` 时，模块从符号起始处移除 55% 的 CP，并将 45% 移位到符号末尾。当您将此参数设置为 `1` 时，模块从 OFDM 符号起始处移除 100% 的 CP，并且不移位任何样本到末尾。

**CP fraction** 提供加窗 LTE 传输支持。当发射机应用加窗时，符号被循环扩展并重叠。在接收机设计中，移除前缀并提取符号的最佳位置取决于发射机的加窗设置。有关 LTE 发射机加窗的更多信息，请参阅 `lteOFDMModulate`（LTE Toolbox）函数的算法部分。

### **Remove DC subcarrier** — 排除或包含 DC 子载波 `off`（默认）| `on`

当您选择此参数时，模块在资源网格输出中排除 DC 子载波。DC 子载波存在于 12×NDLRB 个子载波的中心。模块通过将输出子载波中心周期的 **valid** 信号设置为低电平（`false`）来排除 DC 子载波。

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数以启用模块图标上的 **reset** 端口。

### **Input data sample rate** — 输入采样率 `Use maximum input data sample rate`（默认）| `Match input data sample rate to NDLRB`

此参数指定为输入数据选择的采样率类型。

- 要提供 30.72 MHz 的输入数据采样率，请选择 `Use maximum input data sample rate`。
- 要基于 **NDLRB** 参数提供输入数据采样率，请选择 `Match input data sample rate to NDLRB`。**NDLRB** 值 `6`、`15`、`25`、`50`、`75` 和 `100` 的输入采样率分别为 1.92 MHz、3.84 MHz、7.68 MHz、15.36 MHz、30.72 MHz 和 30.72 MHz。

有关更多信息，请参阅数据速率控制器。

### FFT 参数

### **Divide butterfly outputs by two** — 将 FFT 蝶形输出除以二 `off`（默认）| `on`

此参数控制 LTE OFDM 解调器内部 FFT 模块的缩放选项。

当您选择此参数时，FFT 通过将每个蝶形乘法的输出除以二来实现总体 1/*N* 比例因子。此调整使 FFT 的输出保持与其输入相同的幅度范围。如果您禁用此参数，模块通过在每次蝶形乘法后将字长增加一位来避免溢出。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。有关舍入模式的详细信息，请参阅舍入模式。当输入为任意整数数据类型或定点数据类型时，FFT 算法在内部计算中使用定点运算。当输入的数据类型为 `single` 或 `double` 时，此参数不适用。舍入适用于旋转因子乘法和缩放运算。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

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

**在 R2018a 中引入**

## 描述

解调时域 OFDM 采样并返回 LTE 资源网格

LTE OFDM Demodulator 模块实现了用于解调 LTE 标准 TS 36.212 [1] 所规定 LTE 信号的算法。该模块返回用于小区 ID 检测、主信息块（MIB）恢复、系统信息块（SIB）1 恢复以及进一步解码的 LTE 资源网格。

您可以选择下行资源块数量（NDLRB），并选择正常或扩展循环前缀（CP），如 LTE 标准所述。该模块实现了 CP 比例以支持加窗 LTE 传输，并提供一个参数来配置前缀移除的位置。

该模块提供适合 HDL 代码生成和硬件部署的接口和架构。

该模块接受最大速率为 30.72 MHz 的输入数据，或对应于 NDLRB 的采样率。NDLRB 为 6、15、25、50、75 和 100 时的输入采样率分别为 1.92 MHz、3.84 MHz、7.68 MHz、15.36 MHz、30.72 MHz 和 30.72 MHz。该模块对所有 NDLRB 值使用 2048 点快速傅里叶变换（FFT），并返回所选 NDLRB 所需的资源网格样本数。默认情况下，该模块排除直流（DC）载波。

从第一个输入样本到第一个输出样本的延迟取决于您对 NDLRB 和循环前缀类型的选择，如下表所示。

|  | 最大采样率 | | 对应于 NDLRB 采样率 | |
| --- | --- | --- | --- | --- |
| NDLRB | 延迟 — 正常 CP | 延迟 — 扩展 CP | 延迟 — 正常 CP | 延迟 — 扩展 CP |
| 6 | 5295 | 5647 | 6654 | 6676 |
| 15 | 5241 | 5593 | 6520 | 6564 |
| 25 | 5181 | 5533 | 6660 | 6748 |
| 50 | 5031 | 5383 | 6700 | 6876 |
| 75 | 4881 | 5233 | 6930 | 7282 |
| 100 | 4731 | 5083 | 6780 | 7132 |
