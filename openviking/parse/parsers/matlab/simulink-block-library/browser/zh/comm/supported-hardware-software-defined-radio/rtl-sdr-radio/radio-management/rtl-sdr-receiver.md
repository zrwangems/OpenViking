---
type: simulink-block
title: 'RTL-SDR Receiver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Supported Hardware – Software-Defined Radio / RTL-SDR Radio / Radio Management'
documentation_page: 'rtlsdrreceiver'
documentation_source_path: 'rtlsdrradio/ug/rtlsdrreceiver.html'
language: zh-CN
chinese_source: worker-translation
---

# RTL-SDR Receiver

## 端口

### 输入

### **fc** — 中心频率 正标量

中心频率，以 Hz 为单位，指定为正标量。

**数据类型：** `double`

### **gain** — 接收机增益 标量

接收机增益，以 dB 为单位，指定为标量。

**数据类型：** `double`
### 输出

### **Data** — 从 RTL-SDR 设备接收的数据 复 `int16` 值的列向量 | 复单精度值的列向量 | 复双精度值的列向量

从 RTL-SDR 设备接收的数据，返回为以下值之一。

- 复 `int16` 值的列向量 — 这些复数值是来自 RTL-SDR 设备的原始 16 位 I 和 Q 样本。
- 复单精度值的列向量 — 这些复数值缩放至范围 [–1, 1]。
- 复双精度值的列向量 — 这些复数值缩放至范围 [–1, 1]。

要指定基础类型，请使用 **Output data type** 参数。

**数据类型：** `int16` | `single` | `double`
**复数支持：** 是

### **lost** — 丢失样本数 非负整数

丢失样本数，返回为非负整数。当 RTL-SDR 设备报告没有丢失样本时，**lost** 为 `0`。

如果您的模型实时运行，**lost** 为 `0`。您可以将此输出值用作诊断工具，以确定模块的实时执行情况。有关实时操作的详细信息，请参阅实时操作。

#### 依赖关系

要启用此端口，请选择 **Lost samples output port** 参数。

### **late** — 接收数据的延迟（以帧为单位） 非负整数

接收数据的延迟（以帧为单位），返回为非负整数。当接收的数据帧没有延迟时，**late** 小于或等于 `1`。

即使您的模型实时运行，接收信号也可能经历延迟。您可以将此输出值用作诊断工具，以确定模块的实时执行情况。有关实时操作的详细信息，请参阅实时操作。

#### 依赖关系

要启用此端口，请选择 **Latency output port** 参数。

## 参数

#### 无线电连接

### **Radio address** — RTL-SDR 设备的 USB 地址 `0`（默认值）| 非负整数

指定要与哪台 RTL-SDR 设备通信的 USB 地址，以非负整数表示。要更新与 **Radio address** 指定的设备关联的模型中的模块参数，请使用 **Info** 参数进行更新。

**USB 端口地址分配**

USB 端口地址的分配可能违反直觉。如果 RTL-SDR 设备插入第一个 USB 端口，则其地址为 0。但是，如果 RTL-SDR 设备插入第一个端口之后的任何端口，则地址会变化，具体取决于之前的任一端口是否插入了设备。此图显示了当以先进先出 (FIFO) 顺序添加然后移除设备时，USB 端口地址的分配方式。

多个无线电的 USB 端口地址分配以 FIFO 方式完成。

此图显示了当从端口 0 添加然后移除设备时，USB 端口地址的分配方式。第二个 RTL-SDR 设备的无线电地址会根据第一个端口是否有 RTL-SDR 设备而变化。要使用正确的无线电地址访问无线电，您必须按顺序跟踪已插入的设备。

多个无线电的 USB 端口地址分配。要使用正确的无线电地址访问无线电，您必须按顺序跟踪已插入的设备。

### **Info** — 更新模块参数 按钮

单击此参数可更新模型中与 **Radio address** 参数指定的设备关联的模块参数。当您单击 **Info** 时，将打开一个对话框，显示与该设备关联的信息和参数设置。使用此参数可检查模块与无线电之间的连接，并在二者之间同步无线电设置。如果模块未连接到无线电设备，请单击 **Info**，在 **RadioName** 字段中返回以下消息：`'Cannot find radio'`。

#### 无线电配置

### **Source of center frequency** — 中心频率来源 `Dialog`（默认值）| `Input port`

选择中心频率的来源。

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input port` — 使用 **fc** 输入端口设置中心频率。

### **Center frequency (Hz)** — 中心频率 `102.5e6`（默认值）| 正标量

将中心频率以 Hz 为单位指定为正标量。此参数的有效范围取决于 RTL-SDR 设备的调谐器芯片。有关调谐器芯片及其频率范围的列表，请参阅 [1]。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **Source of center frequency** 参数设置为 `Dialog`。

### **Source of gain** — 增益来源 `Dialog`（默认值）| `Input port` | `AGC`

选择增益的来源。

- `Dialog` — 使用 **Tuner gain (dB)** 参数设置增益。
- `Input port` — 使用 **gain** 输入端口设置增益。
- `AGC` — RTL-SDR 设备使用内部自动增益控制 (AGC) 算法来优化接收机增益设置。

### **Tuner gain (dB)** — 调谐器增益（以 dB 为单位） `0`（默认值）| 标量

调谐器增益，以 dB 为单位，指定为标量。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **Source of gain** 参数设置为 `Dialog`。

### **Sampling rate (Hz)** — ADC 采样率 `250e3`（默认值）| 正标量

将模数转换器 (ADC) 采样率以 Hz 为单位指定为正标量。有效采样率范围为 [225, 300] kHz 和 [900, 3200] kHz。如果将此参数设置为大于 2560 kHz，可能会观察到样本丢失。有关最大可靠采样率的详细信息，请参阅 [1]。

**可调：** 否

### **Frequency correction (ppm)** — 频率校正 `0`（默认值）| 从 –1e4 到 1e4 的整数

将频率校正以 ppm 为单位指定为从 –1e4 到 1e4 的整数。此参数校正由于本振频率偏移或时钟速率不准确而导致的接收数据中的频率偏移。

**可调：** 是

#### 数据传输配置

### **Lost samples output port** — 启用丢失样本输出端口的选项 `off`（默认值）| `on`

选择此参数可启用 **lost** 输出端口。

### **Latency output port** — 启用延迟输出端口的选项 `off`（默认值）| `on`

选择此参数可启用 **late** 输出端口。

### **Output data type** — 输出信号的数据类型 `int16`（默认值）| `single` | `double`

选择输出信号的数据类型。

- `double` 或 `single` — 这些复数值缩放至范围 [–1, 1]。
- `int16` — 这些复数值是来自 RTL-SDR 设备的原始 16 位 I 和 Q 样本。

**可调：** 否

### **Samples per frame** — 每帧样本数 `1024`（默认值）| 正整数

将每帧样本数指定为正整数。

**可调：** 否

### **Enable burst mode** — 启用突发模式的选项 `off`（默认值）| `on`

要在无无线电溢出的情况下生成一组连续帧，请选择此参数。启用突发模式可以帮助您仿真无法实时运行的模型。

选择此参数后，请使用 **Number of frames in burst** 和 **Samples per frame** 参数指定所需的连续数据量。

### **Number of frames in burst** — 突发中的帧数 `20`（默认值）| 正整数

将突发中的帧数指定为正整数。

**可调：** 否

#### 依赖关系

要启用此参数，请选择 **Enable burst mode** 参数。

## 所属库

Communications Toolbox Support Package for RTL-SDR Radio

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

从 RTL-SDR 设备接收数据

RTL-SDR Receiver 模块支持 Simulink® 与 RTL-SDR 设备之间的通信，从而支持各种软件定义无线电 (SDR) 应用的仿真和开发。RTL-SDR Receiver 模块是一个 Simulink 源，它从 RTL-SDR 设备接收数据，并输出固定长度的列向量信号。

此图显示了使用 Communications Toolbox™ Support Package for RTL-SDR Radio 在 Simulink 中接收无线电信号的概念性概述。Simulink 与 RTL-SDR Receiver 模块交互，以从无线电接收信号。

当主机计算机未连接到无线电时，您仍可使用该模块开发模型，以传播采样时间和数据类型信息。要传播此信息，您必须更新模型。

此图标显示了所有已启用的端口，包括可选端口。
