---
type: simulink-block
title: 'E3xx Receiver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Supported Hardware – Software-Defined Radio / USRP Embedded Series Radio / Radio Configuration'
documentation_page: 'e3xxreceiver'
documentation_source_path: 'usrpembeddedseriesradio/ug/e3xxreceiver.html'
language: zh-CN
chinese_source: worker-translation
---

# E3xx Receiver

## 端口

### 输入

### **center frequency** — 外部 RF 中心频率，非负有限标量

外部 RF 中心频率，指定为非负有限标量。有效的中心频率范围为 70 MHz 到 6 GHz。

#### 依赖关系

要启用此端口，请将 **Source of center frequency** 参数设置为 `Input port`。

**数据类型：** `double`

### **gain** — 外部增益，数值标量 | 1-by-2 数值向量

外部增益，指定为数值标量或 1-by-2 数值向量。有效的增益范围是 –10 dB 到 73 dB，并且取决于中心频率。不兼容的增益和中心频率组合会从无线电硬件返回错误。对于每个中心频率可接受的最小和最大增益值，请查看制造商的规格。

根据 **Channel mapping** 参数配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。模块通过标量扩展应用该增益。
- 对于使用不同增益值的两个通道，将增益指定为 1-by-2 向量。向量的第 *i* 个元素应用于由 **Channel mapping** 参数指定的第 *i* 个通道。

#### 依赖关系

要启用此端口，请将 **Source of gain** 参数设置为 `Input port`。

**数据类型：** `double`

### 输出

### **data** — 输出信号，复矩阵

从无线电硬件接收的输出信号，以复矩阵形式返回。矩阵中的列数取决于正在使用的通道数，由 **Channel mapping** 参数指定。每一列对应于在一个通道上接收的复数据。

此端口支持具有以下数据类型的复数值：

- 16 位有符号整数 — 复数值是来自板的原始 16 位 I 和 Q 样本。来自 AD9361 RF 芯片 ADC 的 12 位值被符号扩展为 16 位。
- 单精度浮点 — 复数值缩放到范围 [–1, 1]。模块从板接收到的符号扩展 16 位推导出此值。
- 双精度浮点 — 复数值缩放到范围 [–1, 1]。模块从板接收到的符号扩展 16 位推导出此值。

要指定数据类型，请使用 **Output data type** 参数。

要验证数据接收，请使用 **data valid** 端口。第一个有效数据帧可能包含瞬态值，导致数据包包含未定义数据。

**数据类型：** `int16` | `single` | `double`
**复数支持：** Yes

### **data valid** — 有效数据指示 `1` | `0`

有效数据指示，返回为以下值之一：

- `1` 表示模块已从无线电硬件接收到数据。
- `0` 表示模块尚未从无线电硬件接收到数据。

#### 依赖关系

要启用此端口，请在 **Advanced** 选项卡上，将 **Data timeout (sec)** 更新为 `Inf` 以外的值。

**数据类型：** `Boolean`

### **overflow** — 数据不连续标志 `1` | `0`

数据不连续标志，返回为以下值之一：

- `1` 表示存在溢出，导致数据不连续。
- `0` 表示无溢出。

您可以将此端口用作诊断工具，以确定 E3xx Receiver 模块的实时运行情况。如果您的模型未实时运行，请增加帧大小以接近或达到实时性能。或者，您可以降低基带采样率。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上，选择 **Enable output port for overflow indicator** 参数。

**数据类型：** `Boolean`

## 参数

E3xx Receiver 模块最多支持两个通道从 E3xx 无线电硬件接收数据。使用 **Channel mapping** 参数指示使用单通道还是两个通道。对于输出信号 **data** 中的每个通道，您可以独立设置 **Gain (dB)** 参数，也可以将相同设置应用于所有通道。所有其他参数值应用于每个正在使用的通道。

要检查模块与无线电硬件之间的连通性，并在它们之间同步无线电设置，请在 **Main** 选项卡上，点击 **Info**。

当您设置模块参数值时，E3xx Receiver 模块首先检查这些值是否具有正确的数据类型。如果这些值通过了这些检查，这些值仍可能超出无线电硬件的范围。在这种情况下，无线电硬件会将实际值设置为尽可能接近指定值。当您下次通过点击 **Info** 将模块与无线电硬件同步时，对话框将显示实际值。

如果参数被列为可调，则可以在仿真期间更改其值。

#### 主选项卡

### **Radio IP address** — 无线电硬件的 IP 地址 `192.168.3.2` (默认) | dotted-quad 表达式

无线电硬件的 IP 地址，指定为 dotted-quad 表达式。

此参数必须与硬件设置期间分配的无线电硬件物理 IP 地址匹配。有关更多信息，请参阅 Guided Host-Radio Hardware Setup。如果使用非默认 IP 地址配置无线电硬件，请相应更新 **Radio IP address**。

### **Source of center frequency** — 中心频率的来源 `Dialog` (默认) | `Input port`

中心频率的来源，指定为以下选项之一：

- `Dialog` — 通过使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input port` — 通过使用 **center frequency** 输入端口设置中心频率。

### **Center frequency (Hz)** — 以 Hz 为单位的 RF 中心频率 `2.4e9` (默认) | 非负标量

以 Hz 为单位的 RF 中心频率，指定为非负标量。中心频率的有效范围为 70 MHz 到 6 GHz。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Source of center frequency** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Source of gain** — 选择增益来源 `AGC Slow Attack` (默认) | `AGC Fast Attack` | `Dialog` | `Input port`

- `AGC Slow Attack`
  — 用于功率电平缓慢变化的信号。
- `AGC Fast Attack`
  — 用于功率电平快速变化的信号。
- `Dialog` —
  通过使用 **Gain (dB)** 参数指定增益。
- `Input port`
  — 通过使用 **gain** 输入端口指定增益。

### **Gain (dB)** — 增益 `10` (默认) | 数值标量 | 1-by-2 数值向量

以 dB 为单位的增益，指定为数值标量或 1-by-2 数值向量。有效的增益范围是 –10 dB 到 73 dB，并且取决于中心频率。不兼容的增益和中心频率组合会从无线电硬件返回错误。对于每个中心频率可接受的最小和最大增益值，请查看制造商的规格。

根据 **Channel mapping** 参数配置设置增益值。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。模块通过标量扩展应用该增益。
- 对于使用不同增益值的两个通道，将增益指定为 1-by-2 向量。向量的第 *i* 个元素应用于由 **Channel mapping** 参数指定的第 *i* 个通道。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Source of gain** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Channel Mapping** — 通道输出映射 `1` (默认) | `2` | `[1 2]`

通道输出映射，指定为标量或 1-by-2 向量：

- `1` — 仅通道 1 在使用。
- `2` — 仅通道 2 在使用。
- `[1 2]` — 两个通道都在使用。

### **Baseband sample rate (Hz)** — 以 Hz 为单位的基带采样率 `1e6` (默认) | 正标量

以 Hz 为单位的基带采样率，指定为正标量。此参数的有效范围是 520.834 kHz 到 30.72 MHz。

**注意**

要将模块与无线电硬件同步，请在 **Menu** 选项卡上，点击 **Info**。如果指定速率和实际速率存在小误差，请确认计算出的速率接近您实际想要的值。

**数据类型：** `double`

### **Output data type** — 数据端口上的复数数据类型 `int16` (默认) | `single` | `double`

选择输出数据类型，为以下选项之一：

- `int16` — 整数值是来自板的原始 16 位 I 和 Q 样本。来自 AD9361 RF 芯片 ADC 的 12 位值被符号扩展为 16 位。
- `single` — 单精度浮点值缩放到范围 [–1, 1]。模块从板接收到的符号扩展 16 位推导出此值。
- `double` — 双精度浮点值缩放到范围 [–1, 1]。模块从板接收到的符号扩展 16 位推导出此值。

### **Samples per frame** — 每帧样本数 `20000` (默认) | 正整数

每帧样本数，指定为正整数。在单通道模式下，每帧样本数必须为偶数。当流式传输到主机时，使用较大的帧大小可以提供更高效的性能。要确定对象的实时运行情况，请使用 **overflow** 输出端口。

### **Enable output port for overflow indicator** — 启用溢出控制信号 `on` (默认) | `off`

选择此参数可在主机-无线电硬件数据传输期间启用 **overflow** 输出端口。

### **Enable burst mode** — 启用突发模式 `off` (默认) | `on`

当您选择此参数时，模块会生成一组连续帧。此设置有助于仿真无法实时运行的模型。当您启用突发模式时，请使用 **Frames in burst** 参数指定连续数据的数量。有关如何使用此参数的更多信息，请参阅 Burst Mode。

### **Frames in burst** — 连续突发中的帧数 `1` (默认) | 正整数

连续突发中的帧数，指定为正整数。

#### 依赖关系

要启用此参数，请选择 **Enable burst mode** 参数。

**数据类型：** `double`

#### 滤波器选项卡

### **Use custom filter** — 启用自定义滤波器 `off` (默认) | `on`

当您选择此参数时，滤波器链使用自定义滤波器设计而不是默认滤波器设计。例如，如果默认滤波器的增益或带宽特性不满足您的应用要求，您可以设计满足您特定要求的自定义滤波器。如果 E3xx Receiver 模块尚未应用自定义滤波器设计，请点击 **Launch filter wizard** 打开 ADI 滤波器向导。该向导使您能够基于 **Baseband sample rate (Hz)** 参数为 Analog Devices® AD9361 RF 芯片设计自定义滤波器。您可以调整和优化用于计算模拟滤波器、内插和抽取滤波器以及 FIR 系数的设置。完成向导后，要将自定义滤波器设计应用于模块，请点击模块掩码上的 **Apply**。

**注意**

当使用 ADI 滤波器向导将自定义滤波器应用于 E3xx Receiver 模块时，**Use custom filter** 会自动选中。要在默认滤波器和您的自定义滤波器设计之间切换，请分别清除或选中 **Use custom filter**。然后点击模块掩码上的 **Apply**。

有关更多信息，请参阅 Baseband Sampling Rate and Filter Chains。

#### 高级选项卡

### **Bypass user logic** — 启用绕过用户逻辑 `off` (默认) | `on`

选择此参数可使无线电硬件数据路径绕过在 FPGA 目标生成或硬件-软件协同设计期间生成并编程的算法。有关更多信息，请参阅 FPGA Targeting Workflow 和 Hardware-Software Co-Design Workflow。

### **Enable quadrature correction** — 正交校正 `on` (默认) | `off`

当您选择此参数时，模块应用同相和正交 (IQ) 不平衡补偿。

### **Enable RF DC correction** — RF DC 校正 `on` (默认) | `off`

当您选择此参数时，模块应用 RF 直流 (DC) 阻断滤波器。

### **Enable baseband DC correction** — 基带 DC 校正 `on` (默认) | `off`

当您选择此参数时，模块应用基带 DC 阻断滤波器。

### **Override automatic sample time** — 更改模块的采样时间 `off` (默认) | `on`

当您选择此参数时，您可以使用 **Sample time** 参数更改模块的采样时间。有关更多信息，请参阅 SDR Receiver Sample Times。

### **Sample time** — 模块的采样时间 `0.02` (默认) | 正标量

模块的采样时间，指定为正标量。默认值对应于 **Samples per frame** 除以 **Baseband sample rate (Hz)**。仅当部署硬件-软件协同设计实现时，才考虑更改默认值。

#### 依赖关系

要启用此参数，请选择 **Override automatic sample time** 参数。

### **Data timeout (sec)** — I/O 操作的超时时间（秒） `Inf` (默认) | 非负标量

I/O 操作的超时时间（秒），指定为以下选项之一：

- `Inf` — 模块无限期等待以完成 I/O 操作。
- 非负标量 *N* — 模块等待 *N* 秒以完成 I/O 操作。零秒对应于非阻塞设置。

**数据类型：** `double`

### **Loopback** — 内置自检 (BIST) 环回模式 `Disabled` (默认) | `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

内置自检环回模式，指定为以下选项之一：

- `Disabled` — 禁用 BIST 环回。
- `Digital Tx -> Digital Rx` — 使数字信号在设备内部环回。这些信号绕过 RF 级。
- `RF Rx -> RF Tx` — 使传入的接收器 RF 信号环回到 RF 发射器端口。这些信号绕过 FPGA。

### **Test signal injection** — BIST 信号注入模式 `Disabled` (默认) | `Tone Inject Tx` | `Tone Inject Rx`

BIST 信号注入模式，指定为以下值之一：

- `Disabled` — 禁用 BIST 信号注入。
- `Tone Inject Tx` — 启用向发射路径的 BIST 信号注入。
- `Tone Inject Rx` — 启用向接收路径的 BIST 信号注入。

当您启用 BIST 信号注入时，可以使用 **Signal generator mode** 参数设置 BIST 信号生成的来源。

### **Signal generator mode** — BIST 信号生成的来源 `PRBS` (默认) | `Tone`

BIST 信号生成的来源，指定为以下选项之一：

- `PRBS` — 使用板的伪随机二进制序列 (PRBS) 生成器。
- `Tone` — 使用板的音调生成器。要设置音调频率和音调电平，请分别使用 **Tone frequency (Hz)** 和 **Tone level (dB)** 参数。

#### 依赖关系

要启用此参数，请将 **Test signal injection** 参数设置为 `Tone Inject Tx` 或 `Tone Inject Rx`。

### **Tone frequency (Hz)** — BIST 音调频率 `Fs/32` (默认) | `Fs/16` | `Fs*3/32` | `Fs/8`

BIST 音调频率，指定为 `Fs/32`、`Fs/16`、`Fs*3/32` 或 `Fs/8`。

#### 依赖关系

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

### **Tone level (dB)** — BIST 音调电平 `0` (默认) | `-6` | `-12` | `-18`

BIST 音调电平，指定为 `0`、`-6`、`-12` 或 `-18`。

#### 依赖关系

要启用此参数，请将 **Signal generator mode** 参数设置为 `Tone`。

## 所属库

Communications Toolbox Support Package for USRP Embedded Series Radio / E3xx

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

从 USRP E3xx 无线电硬件接收数据

E3xx Receiver 模块从 USRP™ E3xx 无线电硬件接收数据。

该模块支持以下无线电硬件设备：

- USRP E310
- USRP E312

您可以使用 E3xx Receiver 模块来仿真和开发各种软件定义无线电 (SDR) 应用。此图显示了使用 Communications Toolbox™ Support Package for USRP Embedded Series Radio 在 Simulink® 中发射和接收无线电信号的概念性概述。Simulink 与 E3xx Receiver 模块交互，以从无线电硬件接收信号。

要通过空中发射无线电信号，请将 Simulink 中生成的信号传递到发射器模块。发射器模块将信号转发到无线电硬件。要通过空中接收无线电信号，请使用接收器模块。接收器模块将接收自无线电硬件的信号转发到 Simulink 中进行后处理。
