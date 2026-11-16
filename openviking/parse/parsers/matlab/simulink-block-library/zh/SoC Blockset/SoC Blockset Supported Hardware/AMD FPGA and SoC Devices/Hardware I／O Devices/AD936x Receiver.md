---
type: simulink-block
title: 'AD936x Receiver'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'ad936xreceiver'
documentation_source_path: 'ref/ad936xreceiver.html'
language: zh-CN
chinese_source: worker-translation
---

# AD936x Receiver

## 端口

### 输入

### **data** — 仿真输入数据复数矩阵

输入信号，模拟无线电硬件，指定为复数矩阵。矩阵中的列数取决于使用的通道数，由无线电信道属性指定。每一列对应在一个通道上接收的复数数据的一个通道。

当您选择 **Concatenated complex signal** 参数时，数据类型表示为 `uint32`，而不是 `int16` complex。

#### 依赖关系

- 要启用此仿真端口，必须将 **Simulation input** 设置为 `From input port`。

**数据类型：** `int16`
**复数支持：** 是

### **center frequency** — 外部 RF 中心频率 非负有限标量

外部 RF 中心频率，指定为非负有限标量。有效中心频率范围为 70 MHz 到 6 GHz。

#### 依赖关系

要启用此端口，将 **Simulation input** 参数设置为 `From connected IO`，并将 **Source of gain** 参数设置为 `Input port`。

**数据类型：** `double`

### **gain** — 外部增益 数值标量 | 1-by-2 数值向量

外部增益，指定为数值标量或 1-by-2 数值向量。有效增益范围为 –10 dB 到 73 dB，并且取决于中心频率。不兼容的增益和中心频率组合会从无线电硬件返回错误。对于每个中心频率可接受的最小和最大增益值，请查看制造商的规范。

根据无线电信道配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1-by-2 向量。向量的第 `i` 个元素应用于由无线电信道参数指定的第 `i` 个通道。

#### 依赖关系

要启用此端口，将 **Simulation input** 参数设置为 `From connected IO`，并将 **Source of gain** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **data** — 输出信号复数矩阵

从无线电硬件接收的输出信号，返回为复数矩阵。矩阵中的列数取决于使用的通道数，由无线电信道属性指定。每一列对应在一个通道上接收的复数数据的一个通道。

此端口支持具有以下数据类型的复数值：

- 16-bit 有符号整数 — 复数值是来自板的原始 16-bit I 和 Q 样本。来自 AD9361/AD9364 RF 芯片 ADC 的 12-bit 值符号扩展为 16 bits。
- 单精度浮点 — 复数值缩放到 [–1, 1] 范围。模块从板接收的符号扩展 16 bits 推导出此值。
- 双精度浮点 — 复数值缩放到 [–1, 1] 范围。模块从板接收的符号扩展 16 bits 推导出此值。

要指定数据类型，请使用 **Output data type** 参数。

当您选择 **Concatenated complex signal** 参数时，数据类型表示为 `uint32`，而不是 `int16` complex。

要验证数据接收，请使用 **data valid** 端口。第一个有效数据帧可能包含瞬态值，导致数据包包含未定义数据。

**数据类型：** `int16` | `single` | `double`
**复数支持：** 是

### **valid** — 有效数据指示 `1` | `0`

有效数据指示，返回为以下值之一：

- `1` 表示模块已从无线电硬件接收到数据。
- `0` 表示模块尚未从无线电硬件接收到数据。

**数据类型：** `Boolean`

### **overflow** — 数据不连续标志 `1` | `0`

数据不连续标志，返回为以下值之一：

- `1` 表示存在溢出，导致数据不连续。
- `0` 表示无溢出。

您可以将此端口用作诊断工具，以确定 AD936x Receiver 模块的实时操作。如果您的模型未实时运行，请增大帧大小以接近或实现实时性能。或者，您可以降低基带采样率。

#### 依赖关系

要启用此端口，在 **主要** 选项卡上，将 **Simulation input** 设置为 **From connected IO**，并选择 **Enable output port for overflow indicator** 参数。

**数据类型：** `Boolean`

## 参数

AD936x Receiver 模块支持最多两个通道从基于 AD936x 的 Zynq 无线电硬件接收数据。使用无线电信道参数指示使用单通道还是两个通道。对于输出信号 **data** 中的每个通道，您可以独立设置 **Gain (dB)** 参数，也可以将相同设置应用于所有通道。所有其他参数值应用于每个使用中的通道。

### **Simulation input** — 仿真输入源 `Zeros` (默认) | `From input port` | `From connected IO`

选择仿真输入源：

- `Zeros` — 模块的输出数据是零向量，类型为 `int16` complex。
- `From input port` — 此选项向模块添加输入端口 **data**。将该端口连接到数据源。输入数据直通到输出。来自 AD9361 RF 芯片 ADC 的 12-bit 值符号扩展为 16 bits。
- `From connected IO` — 使用此选项从板接收实时输入数据。

### 主要

### **Enable Channel 1** — 使用通道 1 on (默认) | off

选择此选项以启用通道 1 上的数据接收。

### **Enable Channel 2** — 使用通道 2 off (默认) | on

选择此选项以启用通道 2 上的数据接收。

无线电硬件的 RF 芯片决定您可用于接收数据的通道数。

| 支持的无线电硬件 | RF 芯片 | 通道数 | 支持的 RF 端口 |
| --- | --- | --- | --- |
| ADI RF SOM  ZC706 and FMCOMMS2 or FMCOMMS3  ZedBoard and FMCOMMS2 or FMCOMMS3  ZCU102 and FMCOMMS2 or FMCOMMS3 | AD9361 | 2 | TX1A, RX1A, TX2A, RX2A |
| ZC706 and FMCOMMS4  ZedBoard and FMCOMMS4  ZCU102 and FMCOMMS4 | AD9364 | 1 | TXA, RXA |

### **Radio IP address** — 无线电硬件的 IP 地址 `192.168.3.2` (默认) | 点分四段表达式

无线电硬件的 IP 地址，指定为点分四段表达式。

此参数必须与硬件设置期间分配的无线电硬件的物理 IP 地址匹配。有关更多信息，请参阅设置 AMD FPGA 和 SoC 设备。如果使用非默认 IP 地址配置无线电硬件，请相应地更新 **Radio IP address**。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

### **Info** — SDR 无线电信息按钮

单击此按钮以检查模块与无线电硬件之间的连接，并同步它们之间的无线电设置。

当您设置模块参数值时，AD936x Receiver 模块首先检查值是否具有正确的数据类型。如果值通过这些检查，这些值仍可能超出无线电硬件的范围。在这种情况下，无线电硬件会将实际值设置为尽可能接近指定值。当您下次通过单击 **Info** 同步模块与无线电硬件时，对话框会显示实际值。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

### **Source of center frequency** — 中心频率源 `Dialog` (默认) | `Input port`

中心频率源，指定为以下选项之一：

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input port` — 使用 **center frequency** 输入端口设置中心频率。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

### **Center frequency (Hz)** — 以 Hz 为单位的 RF 中心频率 `2.4e9` (默认) | 非负标量

以 Hz 为单位的 RF 中心频率，指定为非负标量。中心频率的有效范围为 70 MHz 到 6 GHz。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`，并将 **Source of center frequency** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Source of gain** — 增益源 `AGC Slow Attack` (默认) | `AGC Fast Attack` | `Dialog` | `Input port`

增益源，指定为以下值之一：

- `AGC Slow Attack` — 适用于功率电平缓慢变化的信号。
- `AGC Fast Attack` — 适用于功率电平快速变化的信号。
- `Dialog` — 使用 **Gain (dB)** 参数指定增益。
- `Input port` — 使用 **gain** 输入端口指定增益。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

### **Gain (dB)** — 增益 `10` (默认) | 数值标量 | 1-by-2 数值向量

以 dB 为单位的增益，指定为数值标量或 1-by-2 数值向量。有效增益范围为 –10 dB 到 73 dB，并且取决于中心频率。不兼容的增益和中心频率组合会从无线电硬件返回错误。对于每个中心频率可接受的最小和最大增益值，请查看制造商的规范。

根据无线电属性配置设置增益值。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1-by-2 向量。向量的第 *i* 个元素应用于由无线电属性指定的第 *i* 个通道。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`，并将 **Source of gain** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Baseband sample rate (Hz)** — 以 Hz 为单位的基带采样率 `1e6` (默认) | 正标量

以 Hz 为单位的基带采样率，指定为正标量。此参数的有效范围为 520.834 kHz 到 61.44 MHz。

**注意**

要将模块与无线电硬件同步，在 **菜单** 选项卡上，单击 **Info**。如果指定速率和实际速率存在小差异，请验证计算的速率是否接近您实际想要的值。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

**数据类型：** `double`

### **Output data type** — data 端口上的复数数据类型 `int16` (默认) | `single` | `double`

选择输出数据类型，作为以下选项之一：

- `int16` — 整数值是来自板的原始 16-bit I 和 Q 样本。来自 AD9361/AD9364 RF 芯片 ADC 的 12-bit 值符号扩展为 16 bits。
- `single` — 单精度浮点值缩放到 [–1, 1] 范围。模块从板接收的符号扩展 16 bits 推导出此值。
- `double` — 双精度浮点值缩放到 [–1, 1] 范围。模块从板接收的符号扩展 16 bits 推导出此值。

### **Samples per frame** — 每帧样本数 `2000` (默认) | 正整数

每帧样本数，指定为正整数。在单通道模式下，每帧样本数必须为偶数。当流式传输到主机时，使用大帧大小可以提供更高效的性能。要确定对象的实时操作，请使用 **overflow** 输出端口。

要使用每帧奇数个样本捕获每帧偶数个样本，请启用突发模式。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO` 或 `Zeros`。

### **Enable output port for overflow indicator** — 启用溢出控制信号 `on` (默认) | `off`

选择此参数以在主机-无线电硬件数据传输期间启用 **overflow** 输出端口。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

### **Enable burst mode** — 启用突发模式 `off` (默认) | `on`

当您选择此参数时，模块会生成一组连续帧。此设置有助于仿真无法实时运行的模型。启用突发模式时，使用 **Frames in burst** 参数指定连续数据量。有关如何使用此参数的更多信息，请参阅突发模式。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`。

### **Frames in burst** — 连续突发中的帧数 `1` (默认) | 正整数

连续突发中的帧数，指定为正整数。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `From connected IO`，并选择 **Enable burst mode** 参数。

**数据类型：** `double`

### **Concatenated complex signal** — 拼接复数信号 off (默认) | on

当输入和输出信号表示为 `unit32` 而不是实部为 `int16`、虚部为 `int16` 的复数时，选择此选项。

#### 依赖关系

要启用此参数，将 **Output data type** 参数设置为 `int16` complex。对于其他选项，此参数灰显。

### **Sample time** — 模块的采样时间 `0.02` (默认) | 正标量

模块的采样时间，指定为正标量。默认值对应于 **Samples per frame** 除以 **Baseband sample rate (Hz)**。

#### 依赖关系

要启用此参数，将 **Simulation input** 参数设置为 `Zeros`。

当 **Simulation input** 参数为 `From connected IO` 时，此参数在 **高级** 选项卡中可见。

**数据类型：** `double`

### 滤波器

此选项卡中的参数仅在 **Simulation input** 设置为 `From connected IO` 时可见。

### **Use custom filter** — 启用自定义滤波器 `off` (默认) | `on`

当您选择此参数时，滤波器链使用自定义滤波器设计而不是默认滤波器设计。例如，如果默认滤波器的增益或带宽特性不满足您的应用要求，您可以设计满足您特定要求的自定义滤波器。如果 AD936x Receiver 模块尚未应用自定义滤波器设计，请单击 **Launch filter wizard** 以打开 ADI filter wizard。该向导使您能够基于 **Baseband sample rate (Hz)** 参数为 Analog Devices AD9361/AD9364 RF 芯片设计自定义滤波器。您可以调整和优化用于计算模拟滤波器、插值和抽取滤波器以及 FIR 系数的设置。完成向导后，要将自定义滤波器设计应用于模块，请单击模块掩码上的 **Apply**。

**注意**

当您使用 ADI filter wizard 将自定义滤波器应用于 AD936x Receiver 模块时，**Use custom filter** 会自动选中。要在默认滤波器设计和自定义滤波器设计之间切换，请分别清除或选择 **Use custom filter**。然后单击模块掩码上的 **Apply**。

有关更多信息，请参阅基带采样率和滤波器链。

### 高级

此选项卡中的参数仅在 **Simulation input** 设置为 `From connected IO` 时可见。

### **Bypass user logic** — 启用旁路用户逻辑 `off` (默认) | `on`

选择此参数以使无线电硬件数据路径绕过在 FPGA 目标或硬件-软件协同设计期间生成和编程的算法。有关更多信息，请参阅 FPGA 目标工作流和硬件-软件协同设计工作流。

### **Enable quadrature correction** — 正交校正 `on` (默认) | `off`

当您选择此参数时，模块会应用同相和正交 (IQ) 不平衡补偿。

### **Enable RF DC correction** — RF DC 校正 `on` (默认) | `off`

当您选择此参数时，模块会应用 RF 直流 (DC) 阻断滤波器。

### **Enable baseband DC correction** — 基带 DC 校正 `on` (默认) | `off`

当您选择此参数时，模块会应用基带 DC 阻断滤波器。

### **Override automatic sample time** — 更改模块的采样时间 `off` (默认) | `on`

当您选择此参数时，可以使用 **Sample time** 参数更改模块的采样时间。有关详细信息，请参阅 SDR Receiver Sample Times。

### **Sample time** — 模块的采样时间 `0.02` (默认) | positive scalar

模块的采样时间，指定为正标量。默认值对应于 **Samples per frame** 除以 **Baseband sample rate (Hz)**。仅当部署硬件-软件协同设计实现时，才考虑更改默认值。

#### 依赖项

要启用此参数，请选择 **Override automatic sample time** 参数。

**数据类型：** `double`

### **Data timeout (sec)** — I/O 操作超时（秒） `Inf` (默认) | nonnegative scalar

I/O 操作超时（秒），指定为以下选项之一：

- `Inf` — 模块无限期等待以完成 I/O 操作。
- 非负标量 *N* — 模块等待 *N* 秒以完成 I/O 操作。零秒对应于非阻塞设置。

**数据类型：** `double`

### **Loopback** — 内置自检 (BIST) 环回模式 `Disabled` (默认) | `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

内置自检环回模式，指定为以下选项之一：

- `Disabled` — 禁用 BIST 环回。
- `Digital Tx -> Digital Rx` — 启用数字信号在设备内环回。这些信号绕过 RF 级。
- `RF Rx -> RF Tx` — 启用传入的接收器 RF 信号环回到 RF 发射器端口。这些信号绕过 FPGA。

### **Test signal injection** — BIST 信号注入模式 `Disabled` (默认) | `Tone Inject Tx` | `Tone Inject Rx`

BIST 信号注入模式，指定为以下值之一：

- `Disabled` — 禁用 BIST 信号注入。
- `Tone Inject Tx` — 启用 BIST 信号注入到发射路径。
- `Tone Inject Rx` — 启用 BIST 信号注入到接收路径。

当您启用 BIST 信号注入时，可以使用 **Signal generator mode** 参数设置 BIST 信号生成的来源。

### **Signal generator mode** — BIST 信号生成的来源 `PRBS` (默认) | `Tone`

BIST 信号生成的来源，指定为以下选项之一：

- `PRBS` — 使用板上的伪随机二进制序列 (PRBS) 生成器。
- `Tone` — 使用板上的音调生成器。要设置音调频率和音调电平，请分别使用 **Tone frequency (Hz)** 和 **Tone level (dB)** 参数。

#### 依赖项

要启用此参数，请将 **Test signal injection** 参数设置为 `Tone Inject Tx` 或 `Tone Inject Rx`。

### **Tone frequency (Hz)** — BIST 音调频率 `Fs/32` (默认) | `Fs/16` | `Fs*3/32` | `Fs/8`

BIST 音调频率，指定为 `Fs/32`、`Fs/16`、`Fs*3/32` 或 `Fs/8`。

#### 依赖项

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

### **Tone level (dB)** — BIST 音调电平 `0` (默认) | `-6` | `-12` | `-18`

BIST 音调电平，指定为 `0`、`-6`、`-12` 或 `-18`。

#### 依赖项

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ADI RF SOM SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

若要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具或 IP Core Generation (HDL Coder) 工作流。

## 版本历史

**在 R2024b 中引入**

## 描述

从基于 AD936x 的 Zynq 无线电硬件接收数据

AD936x Receiver 模块从基于 AD936x 的 Zynq® 无线电硬件接收数据。

您可以使用 AD936x Receiver 模块来仿真和开发各种软件定义无线电 (SDR) 应用。此图显示了使用 SoC Blockset™ Support Package for AMD FPGA and SoC Devices 在 Simulink® 中接收无线电信号的概念概述。Simulink 与 AD936x Receiver 模块交互，以从无线电硬件接收信号。

框图显示了从天线到 Zynq 板，再到 AD936c Receiver 模块，然后到 FPGA 设计模块的流程
