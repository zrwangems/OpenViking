---
type: simulink-block
title: 'Pluto Receiver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Supported Hardware – Software-Defined Radio / ADALM-Pluto Radio / Radio I/O'
documentation_page: 'plutoreceiver'
documentation_source_path: 'plutoradio/ref/plutoreceiver.html'
language: zh-CN
chinese_source: worker-translation
---

# Pluto Receiver

## 端口

### 输入

### **center frequency** — 以 Hz 为单位的 RF 中心频率设置 positive scalar

RF 中心频率设置，以 Hz 为单位，指定为从 `70.0e6` 到 `6.0e9` 的标量。

**注意**

Analog Devices 对 PLUTO 无线电在 325 MHz 至 3.8 GHz 的调谐范围内进行认证。此支持包使您能够通过将无线电配置为使用 AD9364 固件运行，从而在认证调谐范围之外使用 PLUTO 无线电。要扩展频率范围，请在 MATLAB 命令提示符下输入 `configurePlutoRadio`(`'AD9364'`)。

**示例：**
`88.9e6` 将接收器调谐到 88.9 MHz 的中心频率。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上，将 **Source of center frequency** 设置为 `Input Port`。

**数据类型：** `double`

### **gain** — 以 dB 为单位的接收器增益设置 scalar

接收器增益，以 dB 为单位，指定为从 `-10` 到 `73` 的标量，具体取决于中心频率，分辨率为 `1` dB。

| Center Frequency Range | Acceptable Minimum Gain | Acceptable Maximum Gain |
| --- | --- | --- |
| 70 MHz - 1300 MHz | `-1` dB | `73` dB |
| 1300 MHz - 4 GHz | `-3` dB | `71` dB |
| 4 GHz - 6 GHz | `-10` dB | `62` dB |

**注意**

可接受的最小和最大增益设置取决于中心频率。不兼容的增益和中心频率组合会返回错误。

**示例：**
`10` 将接收器增益水平设置为 10 dB。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上，将 **Source of gain** 设置为 `Input Port`。

**数据类型：** `double`

### 输出

### **data** — 接收数据向量，包含复数值

接收数据，以复数值向量形式返回。值范围取决于输出的数据类型。

- `int16` — 输出数据由范围 [–2048, 2047] 内的 16 位有符号整数值组成。AD936X RF 芯片具有 12 位 ADC。来自 ADC 的 12 位数据存储在输出值的低 12 位中，并符号扩展至 16 位。
- `double` — 输出数据由双精度浮点值组成，缩放到 [–1, 1] 范围。
- `single` — 输出数据由单精度浮点值组成，缩放到 [–1, 1] 范围。

**注意**

AD936X RF 芯片具有 12 位 ADC。接收数据值的双精度和单精度浮点表示直接由从板接收到的符号扩展 `int16` 值创建。这些表示仅占用 [–1, 1] 范围。

要指定接收数据的数据类型，请使用 **Output data type** 参数。

**数据类型：** `int16` | `single` | `double`
**复数支持：** 是

### **overflow** — 丢失样本指示 logical

丢失样本指示，以 logical 返回。

- `0` 表示未丢失样本。
- `1` 表示样本已丢失。

## 参数

### Main 选项卡

#### 无线电连接

### **Radio ID** — 无线电标识符 `usb:0` (默认) | character vector

无线电硬件的无线电标识符，指定为以下字符向量之一：

- （推荐）设备无关索引，带有前缀 `usb:`，例如 `'usb:0'`、`'usb:1'`、`'usb:2'`、…，分别表示第一个、第二个、第三个、… 连接的 ADALM-PLUTO 无线电
- IP 地址，带有前缀 `ip:`，例如 `'ip:192.168.3.2'`
- 序列号，由带有前缀 `sn:` 的十六进制字符串表示，例如 `'sn:100000235523730700230031090216eaeb'`

当在同一主机上运行多个无线电时，主机会为每个无线电分配不同的无线电 ID。当通过 USB ID 标识无线电时，第一个无线电被分配 `usb:0`，后续无线电的 ID 编号依次递增一。例如，以下配置显示了同一主机计算机上连接的两个无线电（一对 Pluto Receiver 和 Pluto Transmitter 模块）所分配的 ID。

为每个连接的无线电设置无线电 ID。

在 Windows® 上操作时，请记住以下注意事项。

- 当在同一主机上的单独 MATLAB 会话中运行多个无线电时，对于每个 MATLAB 会话，第一个无线电被分配 `usb:0`，后续无线电的 ID 编号依次递增一。
- 正在被一个 MATLAB 使用的无线电不会被其他 MATLAB 会话看到。使用 `findPlutoRadio` 并检查报告的序列号，以标识在特定 MATLAB 会话中看到的无线电。

有关详细信息，请参阅将两个无线电连接到一个主机的设置。

### **Info** — 无线电信息按钮

单击 **Info** 打开一个窗口，该窗口与连接的无线电硬件通信以获取基本无线电硬件信息。

**注意**

- 实际计算值可能与您指定的设置存在小偏差。要确认实际计算值足够接近您指定的设置，请单击模块上的 **Info**。此按钮会将模块与无线电硬件同步。
- 当 **Frequency correction (ppm)** 设置为 `0` 时，将使用无线电的出厂校准设置。
- **Frequency correction (ppm)** 参数会更改 **Baseband sample rate (Hz)** 和 **Center frequency (Hz)** 的实际无线电设置。

#### 无线电属性

### **Source of center frequency** — 中心频率源 `Dialog` (默认) | `Input Port`

中心频率源，指定为以下选项之一：

`Dialog`
:   在 **Center frequency (Hz)** 参数中指定中心频率。

`Input Port`
:   通过添加到 Pluto Receiver 模块的输入，以 Hz 为单位指定中心频率。

### **Center frequency (Hz)** — 以 Hz 为单位的 RF 中心频率设置 `2.4e9` (默认) | scalar

RF 中心频率设置，以 Hz 为单位，指定为从 `70.0e6` 到 `6.0e9` 的标量。

**注意**

Analog Devices 对 PLUTO 无线电在 325 MHz 至 3.8 GHz 的调谐范围内进行认证。此支持包使您能够通过将无线电配置为使用 AD9364 固件运行，从而在认证调谐范围之外使用 PLUTO 无线电。要扩展频率范围，请在 MATLAB 命令提示符下输入 `configurePlutoRadio`(`'AD9364'`)。

#### 依赖关系

要启用此参数，请将 **Source of center frequency** 设置为 `Dialog`。

### **Source of gain** — 增益源 `AGC Slow Attack` (默认) | `AGC Fast Attack` | `Dialog` | `Input Port`

增益源，指定为以下选项之一：

`AGC Slow Attack`
:   将此模式用于功率随时间缓慢变化的信号。

`AGC Fast Attack`
:   将此模式用于功率电平快速变化的信号。

`Dialog`
:   在 **Gain (dB)** 参数中指定增益。

`Input Port`
:   通过添加到 Pluto Receiver 模块的输入，以 dB 为单位指定增益。

### **Gain (dB)** — 无线电接收器增益 `10` (默认) | scalar

接收器增益，以 dB 为单位，指定为从 `-10` 到 `73` 的标量，具体取决于中心频率，分辨率为 `1` dB。

| Center Frequency Range | Acceptable Minimum Gain | Acceptable Maximum Gain |
| --- | --- | --- |
| 70 MHz - 1300 MHz | `-1` dB | `73` dB |
| 1300 MHz - 4 GHz | `-3` dB | `71` dB |
| 4 GHz - 6 GHz | `-10` dB | `62` dB |

**注意**

可接受的最小和最大增益设置取决于中心频率。不兼容的增益和中心频率组合会返回错误。

#### 依赖关系

要启用此参数，请将 **Source of gain** 设置为 `Dialog`。

### **Channel mapping** — 通道映射 只读：`1` (默认)

此参数为只读。

通道映射始终设置为 `1`。

### **Baseband sample rate (Hz)** — 基带采样率 `1e6` (默认) | scalar

基带采样率，以 Hz 为单位，指定为从 `65105` 到 `61.44e6` 的标量。

**注意**

实际计算值可能与您指定的设置存在小偏差。要确认实际计算值足够接近您指定的设置，请单击模块上的 **Info**。此按钮会将模块与无线电硬件同步。

#### 数据

### **Output data type** — 输出信号数据类型 `int16` (默认) | `double` | `single`

输出信号数据类型，指定为以下选项之一：

- `int16` — 16 位有符号整数
- `double` — 双精度浮点
- `single` — 单精度浮点

### **Samples per frame** — 每帧样本数 `20,000` (默认) | positive integer

每帧样本数，指定为从 2 到 16,777,216 的偶数正整数。使用小于 3660 的值可能会导致性能不佳。在流式传输到主机时，使用更大的帧大小可以获得更高效的性能。要确定对象的实时操作，请使用 **overflow** 输出端口。

### **Enable output port for overflow indicator** — 启用 overflow 指示输出端口 on (默认) | off

选择 **Enable output port for overflow indicator**，将 `overflow` 输出端口添加到模块。

### **Enable burst mode** — 启用或禁用突发模式 off (默认) | on

当您选择此参数时，Pluto Receiver 模块会生成一组连续帧。此设置可帮助仿真无法实时运行的模型。当您启用突发模式时，请使用 **Frames in burst** 参数指定连续数据的量。有关如何使用此参数的详细信息，请参阅 Burst Mode。

### **Frames in burst** — 连续突发中的帧数 `1` (默认) | strictly positive integer

连续突发中的帧数，指定为严格正整数。

#### 依赖关系

要启用此参数，请选择 **Enable burst mode**。

**数据类型：** `double`

### Filter 选项卡

### **Use custom filter** — 启用自定义滤波器 off (默认) | on

当您选择此参数时，滤波器链会使用自定义滤波器设计而不是默认设计。如果 Pluto Receiver 模块尚未应用自定义滤波器设计，请单击 **Launch filter wizard** 以设计并应用新滤波器。

**注意**

当使用 ADI filter wizard 将自定义滤波器应用于 Pluto Receiver 模块时，会自动选择 **Use custom filter**。要在默认滤波器设计和自定义滤波器设计之间切换，请在模块封装的 **Filter** 选项卡上，分别清除或选择 **Use custom filter**。

有关详细信息，请参阅 Baseband Sampling Rate and Filter Chains。

### Advanced 选项卡

#### 高级无线电属性

### **Enable quadrature correction** — 启用正交校正 on (默认) | off

默认启用正交校正。有关详细信息，请参阅 Quadrature Tracking。

### **Enable RF DC correction** — 启用 RF DC 校正 on (默认) | off

默认启用 RF DC 校正。有关详细信息，请参阅 DC Offset Tracking。

### **Enable baseband DC correction** — 启用基带 DC 校正 on (默认) | off

默认启用基带 DC 校正。有关详细信息，请参阅 DC Offset Tracking。

### **Frequency Correction (ppm)** — 频率校正 0 (默认) | scalar

频率校正，以百万分率 (ppm) 为单位，指定为从 -200 到 200 的标量。

**注意**

- 当 **Frequency correction (ppm)** 设置为 `0` 时，将使用无线电的出厂校准设置。
- **Frequency correction (ppm)** 参数会更改 **Baseband sample rate (Hz)** 和 **Center frequency (Hz)** 的实际无线电设置。

#### 依赖关系

此参数会更改 **Baseband sample rate (Hz)** 和 **Center frequency (Hz)** 的实际无线电设置。

#### 内置自检配置

### **Loopback** — 内置自检 (BIST) 回环模式 `Disabled` (默认) | `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

选择内置自检回环模式，指定为以下选项之一：

- `Disabled` — 禁用 BIST 回环。
- `Digital Tx -> Digital Rx` — 使数字信号在 AD936x 设备内回环。这些信号绕过 RF 级。
- `RF Rx -> RF Tx` — 使传入的接收器 RF 信号回环到 RF 发射器端口。这些信号绕过 FPGA。

### **Test signal injection** — BIST 信号注入模式 `Disabled` (默认) | `Tone Inject Tx` | `Tone Inject Rx`

选择 BIST 信号注入模式，指定为以下值之一：

- `Disabled` — 禁用 BIST 信号注入。
- `Tone Inject Tx` — 启用 BIST 信号注入到发射路径。
- `Tone Inject Rx` — 启用 BIST 信号注入到接收路径。

当您启用 BIST 信号注入时，可以使用 **Signal generator mode** 参数设置 BIST 信号生成源。

### **Signal generator mode** — BIST 信号生成源 `PRBS` (默认) | `Tone`

选择 BIST 信号生成源，指定为以下选项之一：

- `PRBS` — 使用板的伪随机二进制序列 (PRBS) 发生器。
- `Tone` — 使用板的音调发生器。要设置音调频率和音调电平，请分别使用 **Tone frequency (Hz)** 和 **Tone level (dB)** 参数。

#### 依赖关系

要启用此参数，请将 **Test signal injection** 设置为 `Tone Inject Tx` 或 `Tone Inject Rx`。

### **Tone frequency (Hz)** — BIST 音调频率 `Fs/32` (默认) | `Fs/16` | `Fs*3/32` | `Fs/8`

选择 BIST 音调频率，指定为 `Fs/32`、`Fs/16`、`Fs*3/32` 或 `Fs/8`。

#### 依赖关系

要启用此参数，请将 **Signal generator mode** 设置为 `Tone`。

### **Tone level (dB)** — BIST 音调电平 `0` (默认) | `-6` | `-12` | `-18`

选择 BIST 音调电平，指定为 `0`、`-6`、`-12` 或 `-18`。

#### 依赖关系

要启用此参数，请将 **Signal generator mode** 设置为 `Tone`。

## 所属库

Communications Toolbox Support Package for ADALM-PLUTO Radio

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

从 Analog Devices ADALM-PLUTO radio 接收数据

Pluto Receiver 模块是一个信号源，用于从 Analog Devices® ADALM-PLUTO radio 接收数据。此连接使您能够仿真和开发各种软件定义无线电应用。

下图显示了 Simulink®、Pluto Receiver 模块和无线电硬件之间的交互。

要通过空中传输无线电信号，请将 Simulink 中生成的信号传递给 PlutoSDR transmitter block。transmitter block 将信号转发到无线电硬件。要通过空中接收无线电信号，请使用 PlutoSDR receiver block。receiver block 将接收自无线电硬件的信号转发到 Simulink 中进行后处理。

如果主机未连接到无线电硬件，您仍可以使用此模块开发一个传播采样时间和数据类型信息的模型。要传播此信息，请更新您的图。

### 通道输出

ADALM-PLUTO radio 具有单个通道，用于接收数据并将其发送到 Pluto Receiver 模块。该模块输出固定长度的列向量信号。对模块的第一次调用可能包含瞬态值，这可能导致数据包包含未定义数据。

### 设计自定义滤波器

如果默认滤波器的增益或带宽特性不满足您的应用要求，请使用 ADI filter wizard 设计满足您特定要求的自定义滤波器。

通过使用 ADI filter wizard，您可以更改应用于 Pluto Receiver 模块中滤波器链的默认滤波器设计。要打开 filter wizard，请在模块的 **Advanced** 选项卡上，单击 **Design custom filter**。该向导使您能够基于 **Baseband sample rate (Hz)** 参数为 Analog Devices AD9361/AD9364 RF 芯片设计自定义滤波器。您可以调整和优化用于计算模拟滤波器、插值和抽取滤波器以及 FIR 系数的设置。完成向导后，要应用滤波器设置，请单击模块上的 **Apply**。

ADI filter wizard 需要以下 MathWorks® 产品：

- MATLAB®
- Signal Processing Toolbox™
- DSP System Toolbox™

有关操作 ADI filter wizard 的说明，请访问 Analog Devices 网站上的 MATLAB Filter Design Wizard for AD9361。

有关详细信息，请参阅 Baseband Sampling Rate and Filter Chains。
