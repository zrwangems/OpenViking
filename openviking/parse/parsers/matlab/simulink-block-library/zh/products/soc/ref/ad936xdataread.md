---
type: simulink-block
title: 'AD936x Data Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'ad936xdataread'
documentation_source_path: 'ref/ad936xdataread.html'
language: zh-CN
chinese_source: worker-translation
---

# AD936x Data Read

## 端口

### 输入

### **center frequency** — 外部射频中心频率，非负有限标量

外部射频中心频率，指定为非负有限标量。有效中心频率范围为 70 MHz 至 6 GHz。

#### 依赖项

要启用此端口，请将 **增益源** 参数设置为 `Input port`。

**数据类型:** `double`

### **gain** — 外部增益，数值标量 | 1×2 数值向量

外部增益，指定为数值标量或 1×2 数值向量。有效增益范围为 –10 dB 至 73 dB，并且取决于中心频率。不兼容的增益和中心频率组合会从无线电硬件返回错误。对于每个中心频率可接受的最小和最大增益值，请查看制造商规范。

根据无线电通道配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。该模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1×2 向量。向量的第 `i` 个元素应用于由无线电通道参数指定的第 `i` 个通道。

#### 依赖项

要启用此端口，请将 **增益源** 参数设置为 `Input port`。

**数据类型:** `double`

### 输出

### **data** — 输出信号，复矩阵

从无线电硬件接收的输出信号，返回为复矩阵。矩阵中的列数取决于使用的通道数，由无线电通道属性指定。每一列对应于在一个通道上接收的复数据的一个通道。

此端口支持具有以下数据类型的复数值：

- 16 位有符号整数 — 复数值是来自板的原始 16 位 I 和 Q 样本。AD9361/AD9364 RF 芯片 ADC 的 12 位值被符号扩展为 16 位。
- 单精度浮点 — 复数值缩放到 [–1, 1] 范围。该模块从板接收的符号扩展 16 位推导此值。
- 双精度浮点 — 复数值缩放到 [–1, 1] 范围。该模块从板接收的符号扩展 16 位推导此值。

要指定数据类型，请使用 **输出数据类型** 参数。

#### 依赖项

要启用此端口，请在 **主要** 选项卡上，将 **仿真输入** 设置为 `From connected IO` 或 `Zeros`。

**数据类型:** `int16` | `single` | `double`
**复数支持:** Yes

### **valid** — 有效数据指示符 `1` | `0`

有效数据指示符，返回为以下值之一：

- `1` 表示该模块已从无线电硬件接收到数据。
- `0` 表示该模块尚未从无线电硬件接收到数据。

#### 依赖项

要启用此端口，请在 **主要** 选项卡上，将 **仿真输入** 设置为 `From connected IO` 或 `Zeros`。在 **高级** 选项卡上，将 **数据超时 (sec)** 参数设置为 `Inf` 以外的值。

**数据类型:** `Boolean`

### **overflow** — 数据不连续标志 `1` | `0`

数据不连续标志，返回为以下值之一：

- `1` 表示存在溢出，导致数据不连续。
- `0` 表示无溢出。

您可以将此端口用作诊断工具，以确定 AD936x Data Read 模块的实时操作。如果您的模型未实时运行，请增加帧大小以接近或达到实时性能。或者，您可以降低基带采样率。

#### 依赖项

要启用此端口，请在 **主要** 选项卡上，将 **仿真输入** 设置为 `From connected IO` 或 `Zeros`，并选择 **启用溢出指示器的输出端口** 参数。

**数据类型:** `Boolean`

## 参数

AD936x Data Read 模块最多支持
两个
通道从基于 AD936x 的 Zynq 无线电硬件接收数据。使用无线电通道参数指示是使用
单通道还是
两个
通道。对于输出信号 **data** 中的每个通道，您可以独立设置
**增益 (dB)** 参数，也可以将相同设置应用于
所有通道。所有其他参数值都应用于每个使用中的通道。

### **仿真输入** — 仿真输入源 `Zeros` (默认) | `No data (configuration only)` | `From connected IO`

- `No data (configuration only)` — 此选项允许您
  创建并编译模型，而不向其驱动任何输入。
- `Zeros` — 模块的输出数据是
  零向量，类型为 `int16` 复数。
- `From connected IO` — 使用此选项从板接收实时输入
  数据。

### 主要

### **启用通道 1** — 使用通道 1 on (默认) | off

选择此选项以启用通道 1 上的数据接收。

### **启用通道 2** — 使用通道 2 off (默认) | on

选择此选项以启用通道 2 上的数据接收。

无线电硬件的 RF 芯片决定了您可用于接收数据的通道数。

| 支持的无线电硬件 | RF 芯片 | 通道数 | 支持的 RF 端口 |
| --- | --- | --- | --- |
| ADI RF SOM  ZC706 和 FMCOMMS2 或 FMCOMMS3  ZedBoard™ 和 FMCOMMS2 或 FMCOMMS3  ZCU102 和 FMCOMMS2 或 FMCOMMS3 | AD9361 | 2 | TX1A, RX1A, TX2A, RX2A |
| ZC706 和 FMCOMMS4  ZedBoard 和 FMCOMMS4  ZCU102 和 FMCOMMS4 | AD9364 | 1 | TXA, RXA |

### **无线电 IP 地址** — 无线电硬件的 IP 地址 `192.168.3.2` (默认) | 点分四段表达式

无线电硬件的 IP 地址，指定为点分四段表达式。

此参数必须与硬件设置期间分配的无线电硬件的物理 IP 地址匹配。有关详细信息，请参阅 Set Up AMD FPGA and SoC Devices。如果使用非默认 IP 地址配置无线电硬件，请相应更新 **无线电 IP 地址**。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO`。

### **Info** — SDR 无线电信息按钮

单击此按钮以检查模块与无线电硬件之间的连接，并在它们之间同步无线电设置。

当您设置模块参数值时，AD936x Receiver 模块首先检查这些值是否具有正确的数据类型。如果这些值通过了这些检查，这些值仍然可能超出无线电硬件的范围。在这种情况下，无线电硬件会将实际值设置为尽可能接近指定值。当您下次通过单击 **Info** 将模块与无线电硬件同步时，对话框将显示实际值。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO`。

### **中心频率源** — 中心频率源 `Dialog` (默认) | `Input port`

中心频率源，指定为以下选项之一：

- `Dialog` — 使用 **中心频率 (Hz)** 参数设置中心频率。
- `Input port` — 使用 **center frequency** 输入端口设置中心频率。

### **中心频率 (Hz)** — 以 Hz 为单位的射频中心频率 `2.4e9` (默认) | 非负标量

以 Hz 为单位的射频中心频率，指定为非负标量。中心频率的有效范围为 70 MHz 至 6 GHz。

**可调:** Yes

#### 依赖项

要启用此参数，请将 **中心频率源** 参数设置为 `Dialog`。

**数据类型:** `double`

### **增益源** — 增益源 `AGC Slow Attack` (默认) | `AGC Fast Attack` | `Dialog` | `Input port`

增益源，指定为以下值之一：

- `AGC Slow Attack` — 用于功率电平缓慢变化的信号。
- `AGC Fast Attack` — 用于功率电平快速变化的信号。
- `Dialog` — 使用 **增益 (dB)** 参数指定增益。
- `Input port` — 使用 **gain** 输入端口指定增益。

### **增益 (dB)** — 增益 `10` (默认) | 数值标量 | 1×2 数值向量

以 dB 为单位的增益，指定为数值标量或 1×2 数值向量。有效增益范围为 –10 dB 至 73 dB，并且取决于中心频率。不兼容的增益和中心频率组合会从无线电硬件返回错误。对于每个中心频率可接受的最小和最大增益值，请查看制造商规范。

根据无线电属性配置设置增益值。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。该模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1×2 向量。向量的第 *i* 个元素应用于由无线电属性指定的第 *i* 个通道。

**可调:** Yes

#### 依赖项

要启用此参数，请将 **增益源** 参数设置为 `Dialog`。

**数据类型:** `double`

### **基带采样率 (Hz)** — 以 Hz 为单位的基带采样率 `1e6` (默认) | 正标量

以 Hz 为单位的基带采样率，指定为正标量。此参数的有效范围为 520.834 kHz 至 61.44 MHz。

**注意**

要将模块与无线电硬件同步，请在 **菜单** 选项卡上，单击 **Info**。如果指定速率和实际速率存在小偏差，请验证计算出的速率接近您实际想要的值。

**数据类型:** `double`

### **输出数据类型** — 数据端口上的复数数据类型 `int16` (默认) | `single` | `double`

选择输出数据类型，为以下选项之一：

- `int16` — 整数值是来自板的原始 16 位 I 和 Q 样本。AD9361/AD9364 RF 芯片 ADC 的 12 位值被符号扩展为 16 位。
- `single` — 单精度浮点值缩放到 [–1, 1] 范围。该模块从板接收的符号扩展 16 位推导此值。
- `double` — 双精度浮点值缩放到 [–1, 1] 范围。该模块从板接收的符号扩展 16 位推导此值。

### **每帧采样数** — 每帧的采样数 `2000` (默认) | 正整数

每帧的采样数，指定为正整数。在单通道模式下：

- 每帧的采样数必须为偶数。
- 您可以指定奇数个每帧采样数并启用突发模式。然后捕获的总采样数为偶数。

当流式传输到主机时，使用较大的帧大小可以提供更高效的性能。要确定对象的实时操作，请使用 **overflow** 输出端口。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`。

### **启用溢出指示器的输出端口** — 启用溢出控制信号 `on` (默认) | `off`

选择此参数以在主机-无线电硬件数据传输期间启用 **overflow** 输出端口。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`。

### **启用突发模式** — 启用突发模式 `off` (默认) | `on`

当您选择此参数时，该模块会生成一组连续帧。此设置有助于仿真无法实时运行的模型。当您启用突发模式时，请使用 **突发中的帧数** 参数指定连续数据量。有关如何使用此参数的详细信息，请参阅 Burst Mode。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`。

### **突发中的帧数** — 连续突发中的帧数 `1` (默认) | 正整数

连续突发中的帧数，指定为正整数。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`，并选择 **启用突发模式** 参数。

**数据类型:** `double`

### 滤波器

### **使用自定义滤波器** — 启用自定义滤波器 `off` (默认) | `on`

当您选择此参数时，滤波器链使用自定义滤波器设计，而不是默认滤波器设计。例如，如果默认滤波器的增益或带宽特性不满足您的应用要求，您可以设计满足您特定要求的自定义滤波器。如果 AD936x Data Read 模块尚未应用自定义滤波器设计，请单击 **Launch filter wizard** 以打开 ADI filter wizard。该向导使您能够基于 **基带采样率 (Hz)** 参数为 Analog Devices® AD9361/AD9364 RF 芯片设计自定义滤波器。您可以调整和优化用于计算模拟滤波器、插值和抽取滤波器以及 FIR 系数的设置。完成向导后，要将自定义滤波器设计应用于模块，请单击模块掩码上的 **Apply**。

**注意**

当使用 ADI filter wizard 将自定义滤波器应用于 AD936x Data Read 模块时，**使用自定义滤波器** 会自动选中。要在默认滤波器设计和您的自定义滤波器设计之间切换，请分别清除或选中 **使用自定义滤波器**。然后，单击模块掩码上的 **Apply**。

有关详细信息，请参阅 Baseband Sampling Rate and Filter Chains。

### 高级

### **绕过用户逻辑** — 启用绕过用户逻辑 `off` (默认) | `on`

选择此参数以使无线电硬件数据路径绕过在 FPGA 目标化或硬件-软件协同设计期间生成和编程的算法。有关详细信息，请参阅 FPGA Targeting Workflow 和 Hardware-Software Co-Design Workflow。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`。

### **启用正交校正** — 正交校正 `on` (默认) | `off`

当您选择此参数时，该模块应用同相和正交 (IQ) 不平衡补偿。

### **启用射频直流校正** — 射频直流校正 `on` (默认) | `off`

当您选择此参数时，该模块应用射频直流 (DC) 阻断滤波器。

### **启用基带直流校正** — 基带直流校正 `on` (默认) | `off`

当您选择此参数时，该模块应用基带直流阻断滤波器。

### **覆盖自动采样时间** — 更改模块的采样时间 `off` (默认) | `on`

当您选择此参数时，可以使用 **采样时间** 参数更改模块的采样时间。有关详细信息，请参阅 SDR Receiver Sample Times。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`。

### **采样时间** — 模块的采样时间 `0.02` (默认) | 正标量

模块的采样时间，指定为正标量。默认值对应于 **每帧采样数** 除以 **基带采样率 (Hz)**。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`，并选择 **覆盖自动采样时间**。

**数据类型:** `double`

### **数据超时 (sec)** — I/O 操作的超时时间，以秒为单位 `Inf` (默认) | 非负标量

I/O 操作的超时时间，以秒为单位，指定为以下选项之一：

- `Inf` — 模块无限期等待以完成 I/O
  操作。
- 非负标量，*N* — 模块等待
  *N* 秒以完成 I/O 操作。零秒
  对应于非阻塞设置。

#### 依赖项

要启用此参数，请将 **仿真输入** 参数设置为 `From connected IO` 或 `Zeros`。

**数据类型:** `double`

### **Loopback** — 内置自检 (BIST) 环回模式 `Disabled`（默认） | `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

内置自检环回模式，指定为以下选项之一：

- `Disabled` — 禁用 BIST 环回。
- `Digital Tx -> Digital Rx` — 使数字信号在设备内环回。这些信号绕过 RF 级。
- `RF Rx -> RF Tx` — 使传入的接收器 RF 信号环回到 RF 发射器端口。这些信号绕过 FPGA。

#### 依赖关系

要启用此参数，请将 **Simulation input** 参数设置为 `From connected IO` 或 `Zeros`。

### **Test signal injection** — BIST 信号注入模式 `Disabled`（默认） | `Tone Inject Tx` | `Tone Inject Rx`

BIST 信号注入模式，指定为以下值之一：

- `Disabled` — 禁用 BIST 信号注入。
- `Tone Inject Tx` — 启用 BIST 信号注入到发射路径。
- `Tone Inject Rx` — 启用 BIST 信号注入到接收路径。

启用 BIST 信号注入后，可以使用 **Signal generator mode** 参数设置 BIST 信号生成的源。

#### 依赖关系

要启用此参数，请将 **Simulation input** 参数设置为 `From connected IO` 或 `Zeros`。

### **Signal generator mode** — BIST 信号生成的源 `PRBS`（默认） | `Tone`

BIST 信号生成的源，指定为以下选项之一：

- `PRBS` — 使用板的伪随机二进制序列 (PRBS) 生成器。
- `Tone` — 使用板的单音生成器。要设置单音频率和单音电平，请分别使用 **Tone frequency (Hz)** 和 **Tone level (dB)** 参数。

#### 依赖关系

要启用此参数，请将 **Test signal injection** 参数设置为 `Tone Inject Tx` 或 `Tone Inject Rx`。

### **Tone frequency (Hz)** — BIST 单音频率 `Fs/32`（默认） | `Fs/16` | `Fs*3/32` | `Fs/8`

BIST 单音频率，指定为 `Fs/32`、`Fs/16`、`Fs*3/32` 或 `Fs/8`。

#### 依赖关系

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

### **Tone level (dB)** — BIST 单音电平 `0`（默认） | `-6` | `-12` | `-18`

BIST 单音电平，指定为 `0`、`-6`、`-12` 或 `-18`。

#### 依赖关系

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq 7000 / ADI RF SOM SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq 7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq 7000 / ZedBoard

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要自动为您的设计生成处理器代码，并在 SoC 设备上执行，请使用 SoC Builder 工具或 IP Core Generation (HDL Coder) 工作流。

## 版本历史

**在 R2024b 中引入**

## 描述

从基于 AD936x 的 Zynq 无线电硬件读取数据

AD936x Data Read 模块从基于 AD936x 的 Zynq® 无线电硬件接收数据。它表示您的无线电应用的软件接口。

您可以使用 AD936x Data Read 模块来仿真和开发各种软件定义无线电 (SDR) 应用。此图显示了使用 SoC Blockset™ Support Package for AMD FPGA and SoC Devices 在 Simulink® 中接收无线电信号的概念概述。Simulink 与 AD936x Data Read 模块交互以从无线电硬件接收信号。

框图显示了从天线到 Zynq 板，再到 FPGA 设计模块、AD936c Data Read 模块，然后到软件设计 Simulink 模型的流程。
