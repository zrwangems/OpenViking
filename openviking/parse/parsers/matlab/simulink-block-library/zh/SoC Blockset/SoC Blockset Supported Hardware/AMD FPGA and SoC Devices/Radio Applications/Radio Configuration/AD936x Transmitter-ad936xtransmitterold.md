---
type: simulink-block
title: 'AD936x Transmitter'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Radio Applications / Radio Configuration'
documentation_page: 'ad936xtransmitterold'
documentation_source_path: 'ref/ad936xtransmitterold.html'
language: zh-CN
chinese_source: worker-translation
---

# AD936x Transmitter

## 端口

### 输入

### **data** — 输入信号复矩阵

发送到无线电硬件的输入信号，指定为复矩阵。矩阵中的列数取决于正在使用的通道数，由 **Channel mapping** 参数指定。每列对应于通过一个通道发送的复数数据通道。在单通道模式下，一列中的元素数必须为偶数。

此端口支持以下数据类型的复数值：

- 16 位有符号整数 — 由于 AD9361/AD9364 RF 芯片具有 12 位 DAC，仅使用 I 和 Q 样本的 12 个最高有效位。
- 单精度浮点 — 范围为 [–1, 1] 的复数值。由于 AD9361/AD9364 RF 芯片具有 12 位 DAC，幅值小于 0.0625 的数会丢失。
- 双精度浮点 — 范围为 [–1, 1] 的复数值。由于 AD9361/AD9364 RF 芯片具有 12 位 DAC，幅值小于 0.0625 的数会丢失。

要确定数据是否已成功传输，请启用 **underflow** 端口。

#### 依赖项

要启用此端口，请将 **Data source select** 参数设置为 `Input port`。

**数据类型：** `int16` | `single` | `double`
**复数支持：** 是

### **center frequency** — 外部 RF 中心频率 非负有限标量

外部 RF 中心频率，指定为非负有限标量。有效中心频率范围为 70 MHz 到 6 GHz。

#### 依赖项

要启用此端口，请将 **Source of center frequency** 参数设置为 `Input port`。

**数据类型：** `double`

### **gain** — 外部增益 数值标量 | 1-by-2 数值向量

外部增益源，指定为数值标量或 1-by-2 数值向量。有效增益范围为 –89.75 dB 到 0 dB。分辨率为 0.25 dB。

根据 **Channel mapping** 参数配置设置增益。

- 对于单个通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1-by-2 向量。向量的第 `i` 个元素应用于由 **Channel mapping** 参数指定的第 `i` 个通道。

#### 依赖项

要启用此端口，请将 **Source of gain** 参数设置为 `Input port`。

**数据类型：** `double`

### 输出

### **underflow** — 数据不连续标志 `1` | `0`

数据不连续标志，返回为以下值之一：

- `1` 表示存在下溢，导致非连续数据。
- `0` 表示无下溢。

可以将此端口用作诊断工具，以确定 AD936x Transmitter 模块的实时运行情况。如果模型未实时运行，请增大帧大小以接近或实现实时性能。或者，可以降低基带采样率。

**注意**

首次运行该模块会初始化无线电。由于此初始化可能导致下溢，请忽略第一次运行时的 **underflow** 输出端口值。

#### 依赖项

要启用此端口，请在 **Main** 选项卡上选择 **Enable output port for underflow indicator** 参数。

**数据类型：** `Boolean`

## 参数

AD936x Transmitter 模块支持最多两个通道向基于 AD936x 的 Zynq 无线电硬件发送数据。使用 **Channel mapping** 参数指示使用单通道还是两个通道。对于输入信号 **data** 的每个通道，可以独立设置 **Gain (dB)** 参数，也可以将相同设置应用于所有通道。如果为 **Data source select** 参数选择直接数字合成（DDS）传输，则还可以独立设置所有基于 DDS 的参数。所有其他参数值都应用于所使用的每个通道。

要检查模块和无线电硬件之间的连通性，并同步它们之间的无线电设置，请在 **Main** 选项卡上点击 **Info**。

设置模块参数值时，AD936x Transmitter 模块首先检查值是否具有正确的数据类型。如果这些值通过检查，这些值仍可能超出无线电硬件的范围。在这种情况下，无线电硬件会将实际值设置为尽可能接近指定值。下次通过点击 **Info** 同步模块与无线电硬件时，对话框会显示实际值。

如果某参数列出为可调，则可在仿真期间更改其值。

#### 主选项卡

### **Radio IP address** — 无线电硬件的 IP 地址 `192.168.3.2`（默认） | 点分四段表达式

无线电硬件的 IP 地址，指定为点分四段表达式。

此参数必须与硬件设置期间分配的无线电硬件物理 IP 地址匹配。更多信息，请参阅 Set Up AMD FPGA and SoC Devices。如果使用非默认 IP 地址配置无线电硬件，请相应更新 **Radio IP address**。

### **Source of center frequency** — 中心频率源 `Dialog`（默认） | `Input port`

中心频率源，指定为以下选项之一：

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input port` — 使用 **center frequency** 输入端口设置中心频率。

### **Center frequency (Hz)** — RF 中心频率（Hz） `2.4e9`（默认） | 非负标量

RF 中心频率（Hz），指定为非负标量。中心频率的有效范围为 70 MHz 到 6 GHz。

**可调：** 是

#### 依赖项

要启用此参数，请将 **Source of center frequency** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Source of gain** — 选择增益源 `Dialog`（默认） | `Input port`

- `Dialog` — 使用 **Gain (dB)** 参数指定增益。
- `Input port` — 使用 **gain** 输入端口指定增益。

### **Gain (dB)** — 增益 `-10`（默认） | 数值标量 | 1-by-2 数值向量

增益（dB），指定为数值标量或 1-by-2 数值向量。有效增益范围为 –89.75 dB 到 0 dB。分辨率为 0.25 dB。

根据 **Channel mapping** 参数配置设置增益。

- 对于单个通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1-by-2 向量。向量的第 *i* 个元素应用于由 **Channel mapping** 参数指定的第 *i* 个通道。

**可调：** 是

#### 依赖项

要启用此参数，请将 **Source of gain** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Channel mapping** — 通道输入映射 `1`（默认） | `2` | `[1 2]`

通道输入映射，指定为以下值之一：

- `1` — 仅使用通道 1。
- `2` — 仅使用通道 2。
- `[1 2]` — 两个通道均使用。

无线电硬件的 RF 芯片决定可用于发送数据的通道数。

| 支持的无线电硬件 | RF 芯片 | 通道数 | 支持的 RF 端口 |
| --- | --- | --- | --- |
| ADI RF SOM  ZC706 and FMCOMMS2 or FMCOMMS3  ZedBoard and FMCOMMS2 or FMCOMMS3  ZCU102 and FMCOMMS2 or FMCOMMS3 | AD9361 | 2 | TX1A, RX1A, TX2A, RX2A |
| ZC706 and FMCOMMS4  ZedBoard and FMCOMMS4  ZCU102 and FMCOMMS4 | AD9364 | 1 | TXA, RXA |

### **Baseband sample rate (Hz)** — 基带采样率（Hz） `1e6`（默认） | 正标量

基带采样率（Hz），指定为正标量。此参数的有效范围为 520.834 kHz 到 61.44 MHz。

**注意**

要将模块与无线电硬件同步，请在 **Menu** 选项卡上点击 **Info**。如果指定速率与实际速率存在小偏差，请验证计算出的速率接近实际所需的值。

**数据类型：** `double`

### **Enable output port for underflow indicator** — 启用下溢控制信号 `on`（默认） | `off`

选择此参数可在主机-无线电硬件数据传输期间启用 **underflow** 输出端口。

#### 滤波器选项卡

### **Use custom filter** — 启用自定义滤波器 `off`（默认） | `on`

当选择此参数时，滤波器链使用自定义滤波器设计，而不是默认滤波器设计。例如，如果默认滤波器的增益或带宽特性不满足应用需求，可以设计满足特定需求的自定义滤波器。如果 AD936x Transmitter 模块尚未应用自定义滤波器设计，请点击 **Launch filter wizard** 打开 ADI 滤波器向导。该向导使你能够基于 **Baseband sample rate (Hz)** 参数为 Analog Devices AD9361/AD9364 RF 芯片设计自定义滤波器。可以调整和优化用于计算模拟滤波器、插值和抽取滤波器以及 FIR 系数的设置。完成向导后，要将自定义滤波器设计应用于模块，请点击模块掩码上的 **Apply**。

**注意**

当使用 ADI 滤波器向导将自定义滤波器应用于 AD936x Transmitter 模块时，会自动选择 **Use custom filter**。要在默认滤波器设计与自定义滤波器设计之间切换，请分别清除或选择 **Use custom filter**。然后点击模块掩码上的 **Apply**。

更多信息，请参阅 Baseband Sampling Rate and Filter Chains。

#### 高级选项卡

### **Bypass user logic** — 启用绕过用户逻辑 `off`（默认） | `on`

选择此参数可使无线电硬件数据路径绕过在 FPGA 目标定位或硬件-软件协同设计期间生成并编程的算法。更多信息，请参阅 FPGA Targeting Workflow 和 Hardware-Software Co-Design Workflow。

### **Data source select** — 数据源 `Input Port`（默认） | `DDS`

数据源，指定为以下值之一：

- `Input Port` — 此选择启用 **data** 输入端口。
- `DDS` — 此选择启用 DDS 传输。模块为每个通道使用两个相加音调。要设置这些音调的音调频率和音调缩放，请使用 **Tone 1 Frequency (Hz)**、**Tone 2 Frequency (Hz)**、**Tone 1 Scale [0-1]** 和 **Tone 2 Scale [0-1]** 参数。DDS 信号在 FPGA 上生成。

### **Tone 1 Frequency (Hz)** — 第一 DDS 音调频率（Hz） `5000`（默认） | 数值标量 | 1-by-2 数值向量

第一 DDS 音调频率（Hz），指定为以下选项之一：

- 数值标量 — 对于单个通道，或要为两个通道指定相同频率时，使用此选项。对象会为由 **Channel mapping** 参数指定的每个通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同频率。向量的第 `i` 个元素应用于由 **Channel mapping** 参数指定的第 `i` 个通道。

**Tone 1 Frequency (Hz)** 的有效范围为 0 到 `BasebandSampleRate` / 2。

#### 依赖项

要启用此参数，请将 **Data source select** 参数设置为 `DDS`。

**数据类型：** `double`

### **Tone 2 Frequency (Hz)** — 第二 DDS 音调频率（Hz） `10000`（默认） | 数值标量 | 1-by-2 数值向量

第二 DDS 音调频率（Hz），指定为以下选项之一：

- 数值标量 — 对于单个通道，或要为两个通道指定相同频率时，使用此选项。对象会为由 **Channel mapping** 参数指定的每个通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同频率。向量的第 `i` 个元素应用于由 **Channel mapping** 参数指定的第 `i` 个通道。

**Tone 2 Frequency (Hz)** 的有效范围为 0 到 `BasebandSampleRate` / 2。

#### 依赖项

要启用此参数，请将 **Data source select** 参数设置为 `DDS`。

**数据类型：** `double`

### **Tone 1 Scale [0-1]** — 第一 DDS 音调缩放 `0.5`（默认） | 数值标量 | 1-by-2 数值向量

第一 DDS 音调缩放，以满量程的百万分之一为单位，指定为以下选项之一：

- 数值标量 — 对于单个通道，或要为两个通道指定相同缩放时，使用此选项。对象会为由 **Channel mapping** 参数指定的每个通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同缩放。向量的第 `i` 个元素应用于由 **Channel mapping** 参数指定的第 `i` 个通道。

**Tone 1 Scale [0-1]** 的有效范围为 0 到 1。

#### 依赖项

要启用此参数，请将 **Data source select** 参数设置为 `DDS`。

**数据类型：** `double`

### **Tone 2 Scale [0-1]** — 第二 DDS 音调缩放 `0.25`（默认） | 数值标量 | 1-by-2 数值向量

第二 DDS 音调缩放，以满量程的百万分之一为单位，指定为以下选项之一：

- 数值标量 — 对于单个通道，或要为两个通道指定相同缩放时，使用此选项。对象会为由 **Channel mapping** 参数指定的每个通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同缩放。向量的第 `i` 个元素应用于由 **Channel mapping** 参数指定的第 `i` 个通道。

**Tone 2 Scale [0-1]** 的有效范围为 0 到 1。

#### 依赖项

要启用此参数，请将 **Data source select** 参数设置为 `DDS`。

**数据类型：** `double`

### **Data timeout (sec)** — I/O 操作的超时时间（秒） `Inf`（默认） | 非负标量

I/O 操作的超时时间（秒），指定为以下选项之一：

- `Inf` — 模块无限期等待以完成 I/O 操作。
- 非负标量，*N* — 模块等待 *N* 秒以完成 I/O 操作。零秒对应于非阻塞设置。

**数据类型：** `double`

### **Loopback** — 内置自检（BIST）环回模式 `Disabled`（默认） | `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

内置自检环回模式，指定为以下选项之一：

- `Disabled` — 禁用 BIST 环回。
- `Digital Tx -> Digital Rx` — 使数字信号在设备内环回。信号绕过 RF 级。
- `RF Rx -> RF Tx` — 使传入的接收器 RF 信号环回至 RF 发射器端口。信号绕过 FPGA。

### **Test signal injection** — BIST 信号注入模式 `Disabled`（默认） | `Tone Inject Tx` | `Tone Inject Rx`

BIST 信号注入模式，指定为以下值之一：

- `Disabled` — 禁用 BIST 信号注入。
- `Tone Inject Tx` — 启用向发射路径注入 BIST 信号。
- `Tone Inject Rx` — 启用向接收路径注入 BIST 信号。

启用 BIST 信号注入后，可以使用 **Signal generator mode** 参数设置 BIST 信号生成的来源。

### **Signal generator mode** — BIST 信号生成的来源 `PRBS`（默认） | `Tone`

BIST 信号生成的来源，指定为以下选项之一：

- `PRBS` — 使用板的伪随机二进制序列（PRBS）生成器。
- `Tone` — 使用板的音调生成器。要设置音调频率和音调电平，请分别使用 **Tone frequency (Hz)** 和 **Tone level (dB)** 参数。

#### 依赖项

要启用此参数，请将 **Test signal injection** 参数设置为 `Tone Inject Tx` 或 `Tone Inject Rx`。

### **Tone frequency (Hz)** — BIST 音调频率 `Fs/32`（默认） | `Fs/16` | `Fs*3/32` | `Fs/8`

BIST 音调频率，指定为 `Fs/32`、`Fs/16`、`Fs*3/32` 或 `Fs/8`。

#### 依赖项

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

### **Tone level (dB)** — BIST 音调电平 `0`（默认） | `-6` | `-12` | `-18`

BIST 音调电平，指定为 `0`、
`-6`、`-12` 或
`-18`。

#### 依赖关系

要启用此参数，请将
**Signal generator mode** 参数设置为
`Tone`。

## 所属库

SoC Blockset Support Package for Xilinx Devices / MPSoC / ZCU102 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ADI RF SOM SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZedBoard

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

向基于 AD936x 的 Zynq 无线电硬件发送数据

AD936x Transmitter 模块将数据发送到基于 AD936x 的 Zynq® 无线电硬件。

您可以使用 AD936x Transmitter 模块来仿真和开发各种软件定义无线电
(SDR) 应用。此图显示了使用 SoC Blockset™ Support Package for AMD FPGA and SoC Devices 在 Simulink® 中发射和接收
无线电信号的概念概述。Simulink 与 AD936x Transmitter 模块交互，以将数据发送到无线电硬件。

要通过无线方式发射无线电信号，请将在 Simulink 中生成的信号传递给发射器模块。发射器模块将信号转发到无线电硬件。要通过无线方式接收无线电信号，请使用接收器模块。接收器模块将从无线电硬件接收到的信号转发到 Simulink 中进行后处理。
