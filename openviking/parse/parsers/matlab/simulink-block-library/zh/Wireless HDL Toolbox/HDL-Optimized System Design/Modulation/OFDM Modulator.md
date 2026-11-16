---
type: simulink-block
title: 'OFDM Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Modulation'
documentation_page: 'ofdmmodulator'
documentation_source_path: 'ref/ofdmmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Modulator

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为实数或复数值的标量或列向量。向量大小必须为 2 的幂，并在范围 1 到 64 内，且小于或等于 FFT length。有关如何指定向量输入的详细信息，请参阅 Specifying Vector Input。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** Yes

### **valid** — 指示有效输入数据 标量

指示有效输入数据，指定为标量。

此端口是一个控制信号，指示来自 **data** 输入端口的样本何时有效。当此值为 `1` 时，模块捕获 **data** 输入端口上的值。当此值为 `0` 时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **FFTLen** — FFT 长度 标量

FFT 的长度，指定为标量。FFT length 必须为 2 的幂，并在范围 8 到 65,536 内。此值必须小于或等于 **Maximum FFT length** 参数值。

为了支持最小 FFT 长度为 8，**FFTLen** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 4。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPLen** — 循环前缀长度 标量

循环前缀的长度，指定为范围从 0 到 **FFTLen** 的标量。

为了支持最小 FFT 长度为 8，**CPLen** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 4。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numLgSc** — OFDM 符号的左侧保护载波数量 标量

OFDM 符号的左侧保护载波数量，指定为范围从 0 到 (**FFTLen**/2) – 1 的标量。

为了支持最小 FFT 长度为 8，**numLgSc** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numRgSc** — OFDM 符号的右侧保护载波数量 标量

OFDM 符号的右侧保护载波数量，指定为范围从 0 到 (**FFTLen**/2) – 1 的标量。

为了支持最小 FFT 长度为 8，**numRgSc** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **reset** — 清除内部状态 标量

清除内部状态，指定为 Boolean 标量。当此值为 `1` 时，模块停止当前计算并清除所有内部状态。

#### 依赖关系

要启用此端口，请选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`

### **winLen** — 窗口长度 标量

用于重叠相加相邻 OFDM 符号的窗口长度，指定为范围从 1 到 **Maximum window length** 的标量。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### 输出

### **data** — 调制输出数据 标量 | 列向量

调制输出数据，返回为复数值标量或列向量。输出的数据类型取决于输入 **data** 端口的数据类型。

- 当您将 **OFDM parameters source** 参数设置为
  `Property` 并清除 **Divide butterfly outputs by two** 参数时，输出字长增加
  log2(*FFTLength*) bits。
- 当您将 **OFDM parameters source** 参数设置为
  `Input port` 并清除 **Divide butterfly outputs by two** 参数时，输出字长增加
  log2(*MaxFFTLength*) bits。

为避免溢出，请选择 **Divide butterfly outputs by two** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** Yes

### **valid** — 指示有效输出数据 标量

指示有效输出数据，返回为标量。

此端口是一个控制信号，指示 **data** 输出端口何时有效。当 **data** 输出端口上有数据样本可用时，模块将此值设置为 `1`。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

指示模块已就绪，返回为标量。

这是一个控制信号，指示模块何时准备好接收新的输入数据。当此值为 `1` 时，模块在下一时间步接受输入数据。当此值为 `0` 时，模块在下一时间步忽略输入数据。

**数据类型：** `Boolean`

## 参数

### 主要

### **OFDM parameters source** — OFDM 参数的来源 `Property`（默认）| `Input port`

您可以通过输入端口或通过为参数选择值来设置 OFDM 参数。

选择 `Property` 以启用 **FFT length**、**Cyclic prefix length**、**Number of left guard subcarriers** 和 **Number of right guard subcarriers** 参数。

选择 `Input port` 以启用 **FFTLen**、**CPLen**、**numLgSc** 和 **numRgSc** 输入端口以及 **Maximum FFT length** 参数。**Maximum FFT length** 参数设置 **FFTLen** 输入端口有效值范围的上限。

### **Maximum FFT length** — FFT length 的最大长度 `64`（默认）| 范围从 8 到 65,536 的 2 的幂

指定 FFT 的最大长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Input port`。

### **FFT length** — FFT 的长度 `64`（默认）| 范围从 8 到 65, 536 的 2 的幂

指定 FFT length。

当您将 **OFDM parameters source** 参数设置为 `Property` 时，模块将 **FFT length** 值用作最大 FFT 长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Cyclic prefix length** — 循环前缀长度 `16`（默认）| 范围从 0 到 *FFTLength* 的整数

指定循环前缀的长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Number of left guard subcarriers** — OFDM 符号最左侧的保护频带子载波数量 `6`（默认）| 范围从 0 到 (*FFTLength*/2) – 1 的整数

指定左侧保护子载波的数量。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Number of right guard subcarriers** — OFDM 符号最右侧的保护频带子载波数量 `5`（默认）| 范围从 0 到 (*FFTLength*/2) – 1 的整数

指定右侧保护子载波的数量。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Insert DC Null** — 插入 DC 空值的选项 `on`（默认）| `off`

选择此参数以在 DC 子载波上插入空值。

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。

### **Windowing** — 频谱增长降低 `off`（默认）| `on`

选择此参数以执行加窗操作，该操作基于指定的窗口长度降低频谱增长。清除此参数以禁用加窗操作。有关加窗的详细信息，请参阅 Windowing。

### **Window length** — 窗口长度 `4`（默认）| 范围从 1 到 **Cyclic prefix length** 的偶数整数

指定窗口长度以重叠相加相邻的 OFDM 符号。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`，并选择 **Windowing** 参数。

### **Maximum window length** — 窗口的最大长度 `8`（默认）| 范围从 1 到 **CPLen** 的整数

指定窗口的最大长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Input port`，并选择 **Windowing** 参数。

### IFFT 参数

### **Divide butterfly outputs by two** — 将 FFT 蝶形输出除以二 `on`（默认）| `off`

此参数控制 OFDM Modulator 模块内部 IFFT 模块的缩放选项。

当您选择此参数时，FFT 通过将每个蝶形乘法的输出除以二来实现总体 1/*N* 缩放因子。此调整使 IFFT 的输出保持与其输入相同的幅度范围。如果清除此参数，则模块在每次蝶形乘法后将字长增加 one bit 以避免溢出。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。有关舍入模式的详细信息，请参阅 Rounding Modes。当输入为任何整数数据类型或定点数据类型时，FFT 算法使用定点算术进行内部计算。当输入的数据类型为 `single` 或 `double` 时，此参数不适用。舍入适用于旋转因子乘法和缩放操作。

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

**在 R2020a 中引入**

## 描述

为自定义通信协议将频域 OFDM 子载波调制为时域样本

OFDM Modulator 模块基于 OFDM 参数将频域正交频分复用 (OFDM) 子载波调制为时域样本。该模块支持 5G 新空口 (NR) 标准、长期演进 (LTE) [1]、无线局域网 (WLAN 802.11a/g/n/ac) [2]、WiMAX、数字视频广播 (DVB) 和数字音频广播 (DAB) 标准。

该模块接受输入数据以及 valid 控制信号和以下 OFDM 参数：FFT length、CP length 以及左右保护子载波的数量。该模块输出调制数据以及 valid 和 ready 控制信号。仅当 **ready** 端口为 `1`（高）且每个 OFDM 符号的第一个 **valid** 端口为 `1`（高）时，该模块才对相应的 OFDM 参数进行采样。

该模块支持标量和向量输入。您可以使用向量输入来提高数据吞吐量并实现每秒千兆采样 (GSPS) 吞吐量。该模块支持针对标量和向量输入的加窗，以降低 OFDM 信号的频谱再生或相邻信道泄漏比 (ACLR)。该模块提供适用于 HDL 代码生成和硬件部署的接口和架构。
