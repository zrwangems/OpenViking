---
type: simulink-block
title: 'Pluto Transmitter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Supported Hardware – Software-Defined Radio / ADALM-Pluto Radio / Radio I/O'
documentation_page: 'plutotransmitter'
documentation_source_path: 'plutoradio/ref/plutotransmitter.html'
language: zh-CN
chinese_source: worker-translation
---

# Pluto Transmitter

## 端口

### 输入

### **data** — 要发送的数据列向量

要发送的数据，指定为包含偶数个元素（从 2 到 16,777,216）的列向量。发送数据必须为复数。之所以强制此要求，是因为当输入发送信号为实值时，无线电硬件的 IQ 不平衡校正可能会损坏输入信号。有关详细信息，请参阅 Quadrature Tracking。

以下数据类型对发送数据有效：

- `double` — 双精度浮点数，值缩放到 [–1,1] 范围。
- `single` — 单精度浮点数，值缩放到 [–1,1] 范围。
- `int16` — 16 位有符号整数。取值范围为 [-32768,32767]，但 ADALM-PLUTO 无线电发送的数据会丢失 4 个 LSB 精度。

**注意**

- AD936X RF 芯片具有 12 位 DAC。仅使用发送数据中最高 12 位。幅度小于 0.0625 的值会丢失。
- 对于 `double` 和 `single` 数据类型，如果输入数据超出指定的 [-1,1] 范围，System object 会将数据转换为定点格式 (int16)。因此，当信号超出范围时会发生饱和。为避免这些问题，请在将信号提供给发射器 System object 之前对其进行归一化。请参阅 Transmit Signals with Pluto Radio 和 comm.SDRTxPluto System Object 示例，了解如何对信号进行归一化。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上，将 **Data source select** 设置为 `Input Port`。

**数据类型：** `double` | `single` | `int16`
**复数支持：** Yes

### **center frequency** — 以 Hz 为单位的 RF 中心频率设置，正标量

以 Hz 为单位的 RF 中心频率设置，指定为从 `70.0e6` 到 `6.0e9` 的标量。

**注意**

Analog Devices 对 PLUTO 无线电在 325 MHz 至 3.8 GHz 的调谐范围内进行了认证。此支持包使你能够通过将无线电配置为使用 AD9364 固件运行，在认证调谐范围之外使用 PLUTO 无线电。要扩展频率范围，请在 MATLAB 命令提示符下输入 `configurePlutoRadio`(`'AD9364'`)。

**示例：** `88.9e6` 将发射器调谐到 88.9 MHz 的中心频率。

#### 依赖项

要启用此端口，请在 **Main** 选项卡上，将 **Source of center frequency** 设置为 `Input Port`。

**数据类型：** `double`

### **gain** — 以 dB 为单位的发射器增益设置，标量

以 dB 为单位的发射器增益设置，指定为标量。

**示例：** `10` 将发射器增益电平设置为 10 dB。

#### 依赖项

要启用此端口，请在 **Main** 选项卡上，将 **Source of gain** 设置为 `Input Port`。

**数据类型：** `double`

### 输出

### **underflow** — 丢失样本指示符 `logical`

丢失样本指示符，返回为 logical。

- `0` 表示未丢失样本。
- `1` 表示丢失了样本。

**注意**

首次运行该模块会初始化无线电。由于此初始化可能导致 underflow，请忽略第一次运行的 **underflow** 输出端口值。

## 参数

### Main 选项卡

#### 无线电连接

### **Radio ID** — 无线电标识符 `usb:0`（默认）| character vector

无线电硬件的无线电标识符，指定为以下 character vector 之一：

- （推荐）与设备无关的索引，前缀为 `usb:`，例如 `'usb:0'`、`'usb:1'`、`'usb:2'`、…，分别表示第一个、第二个、第三个、... 连接上的 ADALM-PLUTO 无线电
- IP 地址，前缀为 `ip:`，例如 `'ip:192.168.3.2'`
- 序列号，由前缀为 `sn:` 的十六进制字符串表示，例如`'sn:100000235523730700230031090216eaeb'`

在同一主机上运行多个无线电时，主机会为每个无线电分配不同的无线电 ID。通过 USB ID 标识无线电时，第一个无线电分配为 `usb:0`，后续无线电的 ID 编号依次递增一。例如，以下配置显示了在同一台主机计算机上连接的两个无线电（一对 Pluto Receiver 和 Pluto Transmitter 模块）所分配的 ID。

为每个已连接的无线电设置无线电 ID。

在 Windows® 上运行时，请记住以下注意事项。

- 在单独 MATLAB 会话中于同一主机上运行多个无线电时，对于每个 MATLAB 会话，第一个无线电分配为 `usb:0`，后续无线电的 ID 编号依次递增一。
- 一个 MATLAB 正在使用的无线电不会被其他 MATLAB 会话看到。使用 `findPlutoRadio` 并检查报告的序列号，以标识特定 MATLAB 会话中可见的无线电。

有关详细信息，请参阅 Setup for Two Radios Connecting to One Host。

### **Info** — 无线电信息按钮

点击 **Info** 打开一个窗口，该窗口与连接的无线电硬件通信，以获取基本无线电硬件信息。

**注意**

- 实际计算值和您指定的设置可能会有小偏差。要确认实际计算值足够接近您指定的设置，请点击模块上的 **Info**。此按钮会将模块与无线电硬件同步。
- 当 **Frequency correction (ppm)** 设置为 `0` 时，将使用无线电的出厂校准设置。
- **Frequency correction (ppm)** 参数会更改 **Baseband sample rate (Hz)** 和 **Center frequency (Hz)** 的实际无线电设置。

#### 无线电属性

### **Source of center frequency** — 中心频率来源 `Dialog`（默认）| `Input Port`

中心频率来源，指定为以下之一：

`Dialog`
:   在 **Center frequency (Hz)** 参数中指定中心频率。

`Input Port`
:   通过使用添加到模块的输入，以 Hz 为单位指定中心频率。

### **Center frequency (Hz)** — 以 Hz 为单位的 RF 中心频率设置 `2.4e9`（默认）| 标量

以 Hz 为单位的 RF 中心频率设置，指定为从 `70.0e6` 到 `6.0e9` 的标量。

**注意**

Analog Devices 对 PLUTO 无线电在 325 MHz 至 3.8 GHz 的调谐范围内进行了认证。此支持包使你能够通过将无线电配置为使用 AD9364 固件运行，在认证调谐范围之外使用 PLUTO 无线电。要扩展频率范围，请在 MATLAB 命令提示符下输入 `configurePlutoRadio`(`'AD9364'`)。

#### 依赖项

要启用此参数，请将 **Source of center frequency** 设置为 `Dialog`。

### **Source of gain** — 增益来源 `Dialog`（默认）| `Input Port`

增益来源，指定为以下之一：

`Dialog`
:   在 **Gain (dB)** 参数中指定增益。

`Input Port`
:   通过使用添加到模块的输入，以 dB 为单位指定增益。

### **Gain (dB)** — 无线电发射器增益 `-10`（默认）| 标量

以 dB 为单位的无线电发射器增益，指定为从 `-87.5` 到 `0` 的标量。分辨率为 `0.25` dB。

#### 依赖项

要启用此参数，请将 **Source of gain** 设置为 `Dialog`。

### **Channel mapping** — 通道映射 只读：`1`（默认）

此参数为只读。

通道映射始终设置为 `1`。

### **Baseband sample rate (Hz)** — 基带采样率 `1e6`（默认）| 非负标量

以 Hz 为单位的基带采样率，指定为从 `65105` 到 `61.44e6` 的标量。

**注意**

实际计算值和您指定的设置可能会有小偏差。要确认实际计算值足够接近您指定的设置，请点击模块上的 **Info**。此按钮会将模块与无线电硬件同步。

#### 数据

### **Enable output port for underflow indicator** — 启用 underflow 指示符的输出端口 on（默认）| off

选择 **Enable output port for underflow indicator** 可将 `underflow` 输出端口添加到 Pluto Transmitter 模块。

### Filter 选项卡

### **Use custom filter** — 启用自定义滤波器 off（默认）| on

选择此参数后，滤波器链将使用自定义滤波器设计，而不是默认设计。如果 Pluto Transmitter 模块尚未应用自定义滤波器设计，请点击 **Launch filter wizard** 以设计并应用新滤波器。

**注意**

使用 ADI filter wizard 将自定义滤波器应用到 Pluto Transmitter 模块时，会自动选择 **Use custom filter**。要在默认滤波器设计和自定义滤波器设计之间切换，请在模块封装（block mask）的 **Filter** 选项卡上，分别清除或选择 **Use custom filter**。

有关详细信息，请参阅 Baseband Sampling Rate and Filter Chains。

### Advanced 选项卡

#### 数据

### **Data source select** — 选择数据源 `Input port`（默认）| `DDS`

选择数据源，指定为：

- `Input port` — 发送信号的来源是 **data** 输入端口
- `DDS` — 发送信号的来源是无线电硬件上的直接数字合成 (DDS)。发射器具有两个相加的单音。要设置这些单音的单音频率和单音缩放，请使用 **Tone 1 Frequency (Hz)**、**Tone 2 Frequency (Hz)**、**Tone 1 Scale [0-1]** 和 **Tone 2 Scale [0-1]** 参数。

### **Tone 1 Frequency (Hz)** — 第一个 DDS 单音的频率 5e3（默认）| 标量

以 Hz 为单位的第一个 DDS 单音频率，指定为范围 [0, (**Baseband sample rate** / 2)] 内的标量。

#### 依赖项

要启用此参数，请将 **Data source select** 设置为 `DDS`。

### **Tone 2 Frequency (Hz)** — 第二个 DDS 单音的频率 10e3（默认）| 标量

以 Hz 为单位的第二个 DDS 单音频率，指定为范围 [0, (**Baseband sample rate** / 2)] 内的标量。

#### 依赖项

要启用此参数，请将 **Data source select** 设置为 `DDS`。

### **Tone 1 Scale [0-1]** — 第一个 DDS 单音的缩放 0.5（默认）| 标量

第一个 DDS 单音的缩放，以满量程的百万分之一为单位，指定为范围 [0,1] 内的标量。这些值相对于 DAC 输出幅度，其中 `0` 为零幅度，`1` 为 1e6，即最大 DAC 输出幅度。

#### 依赖项

要启用此参数，请将 **Data source select** 设置为 `DDS`。

### **Tone 2 Scale [0-1]** — 第二个 DDS 单音的缩放 0.5（默认）| 标量

第二个 DDS 单音的缩放，以满量程的百万分之一为单位，指定为范围 [0,1] 内的标量。这些值相对于 DAC 输出幅度，其中 `0` 为零幅度，`1` 为 1e6，即最大 DAC 输出幅度。

#### 依赖项

要启用此参数，请将 **Data source select** 设置为 `DDS`。

### **Frequency Correction (ppm)** — 频率校正 0（默认）| 标量

以百万分率 (ppm) 为单位的频率校正，指定为从 -200 到 200 的标量。

**注意**

- 当 **Frequency correction (ppm)** 设置为 `0` 时，将使用无线电的出厂校准设置。
- **Frequency correction (ppm)** 参数会更改 **Baseband sample rate (Hz)** 和 **Center frequency (Hz)** 的实际无线电设置。

#### 内置自检配置

### **Loopback** — 内置自检 (BIST) 环回模式 `Disabled`（默认）| `Digital Tx -> Digital Rx` | `RF Rx -> RF Tx`

选择内置自检环回模式，指定为以下选项之一：

- `Disabled` — 禁用 BIST 环回。
- `Digital Tx -> Digital Rx` — 使数字信号在 AD936x 器件内环回。这些信号绕过 RF 级。
- `RF Rx -> RF Tx` — 使传入的接收器 RF 信号环回到 RF 发射器端口。这些信号绕过 FPGA。

### **Test signal injection** — BIST 信号注入模式 `Disabled`（默认）| `Tone Inject Tx` | `Tone Inject Rx`

选择 BIST 信号注入模式，指定为以下值之一：

- `Disabled` — 禁用 BIST 信号注入。
- `Tone Inject Tx` — 启用向发射路径的 BIST 信号注入。
- `Tone Inject Rx` — 启用向接收路径的 BIST 信号注入。

启用 BIST 信号注入时，可以使用 **Signal generator mode** 参数设置 BIST 信号生成的来源。

### **Signal generator mode** — BIST 信号生成的来源 `PRBS`（默认）| `Tone`

选择 BIST 信号生成的来源，指定为以下选项之一：

- `PRBS` — 使用板的伪随机二进制序列 (PRBS) 发生器。
- `Tone` — 使用板的单音发生器。要分别设置单音频率和单音电平，请使用 **Tone frequency (Hz)** 和 **Tone level (dB)** 参数。

#### 依赖项

要启用此参数，请将 **Test signal injection** 设置为 `Tone Inject Tx` 或 `Tone Inject Rx`。

### **Tone frequency (Hz)** — BIST 单音频率 `Fs/32`（默认）| `Fs/16` | `Fs*3/32` | `Fs/8`

选择 BIST 单音频率，指定为 `Fs/32`、`Fs/16`、`Fs*3/32` 或 `Fs/8`。

#### 依赖项

要启用此参数，请将 **Signal generator mode** 设置为 `Tone`。

### **Tone level (dB)** — BIST 单音电平 `0`（默认）| `-6` | `-12` | `-18`

选择 BIST 单音电平，指定为 `0`、`-6`、`-12` 或 `-18`。

#### 依赖项

要启用此参数，请将 **Signal generator mode** 设置为 `Tone`。

## 所属库

Communications Toolbox Support Package for ADALM-PLUTO Radio

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将数据发送到 Analog Devices ADALM-PLUTO 无线电

Pluto Transmitter 模块是一个信号源，用于将数据发送到 Analog Devices® ADALM-PLUTO 无线电。此连接使您能够仿真和开发各种 SDR 应用。

下图显示了 Simulink®、Pluto Transmitter 模块和无线电硬件之间的交互。

要通过空中传输无线电信号，请将 Simulink 中生成的信号传递给 PlutoSDR transmitter block。发射器模块将信号转发到无线电硬件。要通过空中接收无线电信号，请使用 PlutoSDR receiver block。接收器模块将从无线电硬件接收的信号转发到 Simulink 中进行后处理。

如果主机未连接到无线电硬件，您仍可以使用此模块开发模型，以传播采样时间和数据类型信息。要传播此信息，请更新您的图。

### 通道输入

ADALM-PLUTO 无线电具有单个通道，用于从 Pluto Transmitter 模块发送数据。该模块接受固定长度的列向量信号。

在仿真期间调用 Pluto Transmitter 模块时，主机可能未向无线电硬件发送有效数据。要确定何时存在有效数据，请使用 `underflow` 端口。

### 设计自定义滤波器

如果默认滤波器的增益或带宽特性不满足您的应用要求，请使用 ADI filter wizard 设计满足您特定要求的自定义滤波器。

通过使用 ADI filter wizard，您可以更改应用于 Pluto Transmitter 模块中滤波器链的默认滤波器设计。要打开滤波器向导，请在模块的 **Advanced** 选项卡上，点击 **Design custom filter**。该向导使您能够基于 **Baseband sample rate (Hz)** 参数为 Analog Devices AD9361/AD9364 RF 芯片设计自定义滤波器。您可以调整和优化用于计算模拟滤波器、内插和抽取滤波器以及 FIR 系数的设置。完成向导后，要应用滤波器设置，请点击模块上的 **Apply**。

ADI filter wizard 需要以下 MathWorks® 产品：

- MATLAB®
- Signal Processing Toolbox™
- DSP System Toolbox™

有关操作 ADI filter wizard 的说明，请访问 Analog Devices 网站上的 MATLAB Filter Design Wizard for AD9361。

有关详细信息，请参阅 Baseband Sampling Rate and Filter Chains。
