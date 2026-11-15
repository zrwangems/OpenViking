---
type: simulink-block
title: 'OFDM Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Modulation'
documentation_page: 'ofdmdemodulator'
documentation_source_path: 'ref/ofdmdemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Demodulator

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为实数或复数值的标量或列向量。向量大小必须是 2 的幂，范围为 1 到 64，并且小于或等于 FFT 长度。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** Yes

### **valid** — 指示有效输入数据 标量

指示有效输入数据，指定为标量。

此端口是一个控制信号，用于指示来自 **data** 输入端的样本何时有效。当该值为 `1` 时，模块捕获 **data** 输入端口上的值。当该值为 `0` 时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **FFTLen** — FFT 长度 标量

FFT 的长度，指定为标量。FFT 长度必须是 2 的幂，范围为 8 到 65,536。该值必须小于或等于 **最大 FFT 长度** 参数值。

为了支持最小 FFT 长度 8，**FFTLen** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 4。

#### 依赖关系

要启用此端口，请将 **OFDM 参数来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPLen** — 循环前缀长度 标量

循环前缀的长度，指定为范围从 0 到 **FFTLen** 的标量。

为了支持最小 FFT 长度 8，**CPLen** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 4。

#### 依赖关系

要启用此端口，请将 **OFDM 参数来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numLgSc** — OFDM 符号的左侧保护载波数量 标量

OFDM 符号的左侧保护载波数量，指定为范围从 0 到 (**FFTLen**/2) – 1 的标量。

为了支持最小 FFT 长度 8，**numLgSc** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请将 **OFDM 参数来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numRgSc** — OFDM 符号的右侧保护载波数量 标量

OFDM 符号的右侧保护载波数量，指定为范围从 0 到 (**FFTLen**/2) – 1 的标量。

为了支持最小 FFT 长度 8，**numRgSc** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请将 **OFDM 参数来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPFraction** — CP 比例 实数正标量

CP 比例，指定为范围 [0, 1] 内的实数正标量。

为了支持最大精度，**CPFraction** 数据类型必须为 `fixdt(0,k,p)`，其中 *k* 小于或等于 16，且 *p* 等于 *k* - 1。

#### 依赖关系

要启用此端口，请选择 **启用 CP 比例** 参数，并将 **CP 比例来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `unsigned fixed point`

### **reset** — 清除内部状态 标量

清除内部状态，指定为标量。当该值为 `1`（true）时，模块停止当前计算并清除所有内部状态。

#### 依赖关系

要启用此端口，请选择 **启用 reset 输入端口** 参数。

**数据类型：** `Boolean`

### 输出

### **data** — 解调输出数据 标量 | 列向量

解调输出数据，返回为复数值标量或列向量。输出数据类型取决于输入 **data** 端口的数据类型。

- 当将 **OFDM 参数来源** 参数设置为 `Property` 并清除 **将蝶形输出除以二** 参数时，输出字长增加 log2(*FFTLength*) 位。
- 当将 **OFDM 参数来源** 参数设置为 `Input port` 并清除 **将蝶形输出除以二** 参数时，输出字长增加 log2(*MaxFFTLength*) 位。

为避免溢出，请选择 **将蝶形输出除以二** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** Yes

### **valid** — 指示有效输出数据 标量

指示有效输入数据，返回为标量。

此端口是一个控制信号，用于指示 **data** 输出端口何时有效。当数据样本在 **data** 输出端口上可用时，模块将该值设置为 `1`。当选择 **移除 DC 子载波** 参数时，该值在输出样本中心处设置为 `0`，以排除 DC 载波。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

控制信号，用于指示模块何时准备好接收新输入数据。当该值为 `1` 时，模块在下一时间步接受输入数据。当该值为 `0` 时，模块在下一时间步忽略输入数据。

#### 依赖关系

要启用此端口，请将 **OFDM 参数来源** 参数设置为 `Input port`。

**数据类型：** `Boolean`

## 参数

### 主要

### **OFDM 参数来源** — OFDM 参数的来源 `Property`（默认）| `Input port`

您可以通过输入端口设置 OFDM 参数，或通过为该参数选择值来设置。

选择 `Property` 以启用 **FFT 长度**、**循环前缀长度**、**左侧保护子载波数量** 和 **右侧保护子载波数量** 参数。

选择 `Input port` 以启用 **FFTLen**、**CPLen**、**numLgSc**、**numRgSc** 输入端口以及 **最大 FFT 长度** 参数。**最大 FFT 长度** 参数设置 **FFTLen** 输入端口的有效值范围上限。

### **最大 FFT 长度** — FFT 长度的最大值 `64`（默认）| 范围为 8 到 65,536 的 2 的幂

指定 FFT 的最大长度。

#### 依赖关系

要启用此参数，请将 **OFDM 参数来源** 参数设置为 `Input port`。

### **FFT 长度** — FFT 的长度 `64`（默认）| 范围为 8 到 65,536 的 2 的幂

指定 FFT 长度。当将 **OFDM 参数来源** 参数设置为 `Property` 时，模块使用此 FFT 长度值作为最大 FFT 长度。

#### 依赖关系

要启用此参数，请将 **OFDM 参数来源** 参数设置为 `Property`。

### **循环前缀长度** — 循环前缀的长度 `16`（默认）| 范围为 0 到 *FFTLength* 的整数

指定循环前缀的长度。

#### 依赖关系

要启用此参数，请将 **OFDM 参数来源** 参数设置为 `Property`。

### **左侧保护子载波数量** — OFDM 符号最左侧的保护频带子载波数量 `6`（默认）| 范围为 0 到 (*FFTLength*/2) – 1 的整数

指定左侧保护子载波数量。

#### 依赖关系

要启用此参数，请将 **OFDM 参数来源** 参数设置为 `Property`。

### **右侧保护子载波数量** — OFDM 符号最右侧的保护频带子载波数量 `5`（默认）| 范围为 0 到 (*FFTLength*/2) – 1 的整数

指定右侧保护子载波数量。

#### 依赖关系

要启用此参数，请将 **OFDM 参数来源** 参数设置为 `Property`。

### **启用 CP 比例** — CP 比例启用器 `off`（默认）| `on`

选择此参数可通过 `Property` 或 `Input port` 启用 CP 比例。

### **CP 比例来源** — CP 比例来源类型 `Property`（默认）| `Input port`

您可以通过输入端口设置 CP 比例，或通过为该参数选择值来设置。

选择 `Property` 以启用 **CP 比例** 参数。

选择 `Input port` 以启用 **CPFraction** 输入端口。

#### 依赖关系

要启用此参数，请选择 **启用 CP 比例** 参数。

### **CP 比例** — 要移除的循环前缀百分比 `0.55`（默认）| 范围从 0 到 1

循环前缀比例，指定为从 0 到 1（含）的值。此参数指定模块从 OFDM 符号起始处移除的 CP 样本百分比。模块将剩余的 CP 样本移到 OFDM 符号末尾。

当此参数为 `0.55` 时，模块从符号起始处移除 55% 的 CP，并将 45% 移到符号末尾。当将此参数设置为 `1` 时，模块从 OFDM 符号起始处移除 100% 的 CP，并且不将任何样本移到末尾。

#### 依赖关系

要启用此参数，请选择 **启用 CP 比例** 参数，并将 **CP 比例来源** 参数设置为 `Property`。

### **移除 DC 子载波** — 排除或包括 DC 子载波 `on`（默认）| `off`

选择此参数时，模块通过将输出子载波中心处的输出 valid 信号设置为 `0`，在输出中排除 DC 子载波。

### **启用 reset 输入端口** — Reset 信号 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。

### FFT 参数

### **将蝶形输出除以二** — 将 FFT 蝶形输出除以二 `off`（默认）| `on`

此参数控制 OFDM Demodulator 模块内部 FFT 模块的缩放选项。

选择此参数时，FFT 通过将每个蝶形乘法的输出除以二来实现总体 1/*N* 缩放因子。此调整使 FFT 的输出保持与其输入相同的幅度范围。如果清除此参数，模块会在每次蝶形乘法后将字长增加一位以避免溢出。

### **舍入方法** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。有关舍入模式的详细信息，请参阅舍入模式。当输入为任何整数数据类型或定点数据类型时，FFT 算法使用定点算术进行内部计算。当输入的数据类型为 `single` 或 `double` 时，此参数不适用。舍入适用于旋转因子乘法和缩放运算。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

此模块没有任何 HDL 模块属性。

## 版本历史

**在 R2019b 中引入**

### R2023a：CP 比例作为输入端口

现在可以通过端口指定 CP 比例。要启用此端口，请选择 **启用 CP 比例** 参数，并将 **CP 比例来源** 参数设置为 `Input port`。

## 描述

解调时域 OFDM 样本并返回用于自定义通信协议的子载波

OFDM Demodulator 模块解调时域正交频分复用 (OFDM) 样本，并基于 OFDM 参数输出子载波。该模块支持 5G 新空口 (NR) 标准、长期演进 (LTE) [1]、无线局域网 (WLAN 802.11a/g/n/ac) [2]、WiMAX、数字视频广播 (DVB) 和数字音频广播 (DAB) 标准。

该模块接受输入数据以及 valid 控制信号和以下 OFDM 参数：FFT 长度、CP 长度以及右侧和左侧保护子载波数量。该模块输出解调数据以及 valid 和 ready 控制信号。仅当这些 OFDM 参数通过输入端口提供给模块时，模块才会启用 **ready** 输出端口。仅当 **ready** 端口为 `1`（高）且每个 OFDM 符号的第一个 **valid** 端口为 `1`（高）时，模块才会对相应的 OFDM 参数进行采样。

该模块支持标量和向量输入。您可以使用向量输入来提高数据吞吐量，并实现每秒千兆采样 (GSPS) 吞吐量。该模块提供适合 HDL 代码生成和硬件部署的接口与架构。
