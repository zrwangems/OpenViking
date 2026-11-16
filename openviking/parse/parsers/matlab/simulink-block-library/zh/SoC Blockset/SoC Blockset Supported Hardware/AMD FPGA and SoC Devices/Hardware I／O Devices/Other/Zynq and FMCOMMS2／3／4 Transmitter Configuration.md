---
type: simulink-block
title: 'Zynq and FMCOMMS2/3/4 Transmitter Configuration'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices / Other'
documentation_page: 'zynqandfmcomms234transmitterconfiguration'
documentation_source_path: 'ref/zynqandfmcomms234transmitterconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Zynq and FMCOMMS2/3/4 Transmitter Configuration

## 端口

### 输入

### **center frequency** — 外部 RF 中心频率非负有限标量

外部 RF 中心频率，指定为非负有限标量。有效的中心频率范围为 70 MHz 至 6 GHz。

#### 依赖关系

要启用此端口，请将 **Source of center frequency** 参数设置为 `Input Port`。

**数据类型：** `double`

### **gain** — 外部增益数值标量 | 1-by-2 数值向量

外部增益，指定为数值标量或 1-by-2 数值向量。有效增益范围为 –10 dB 至 77 dB。分辨率为 0.25 dB。

根据 **Channel mapping** 参数配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。
  模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为
  1-by-2 向量。向量的第 `i` 个元素应用于
  由 **Channel mapping** 参数指定的第 `i` 个通道。

#### 依赖关系

要启用此端口，请将 **Source of gain** 参数设置为
`Input Port`。

**数据类型：** `double`

## 参数

Zynq and FMCOMMS2/3/4 Transmitter Configuration 模块最多支持两个通道发送数据。使用 **Channel mapping** 参数指示使用单通道还是双通道。
对于每个通道，可以独立设置 **Gain (dB)** 参数，也可以对所有通道应用相同设置。如果为 **Data source select** 参数选择直接数字合成 (DDS)
传输，还可以独立设置所有基于 DDS 的参数。所有其他参数值将应用于每个使用中的通道。

### 主

### **Source of center frequency** — 中心频率来源 `Dialog`（默认）| `Input Port`

中心频率来源，指定为以下选项之一：

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input Port` — 使用 **center frequency** 输入端口设置中心频率。

### **Center frequency (Hz)** — RF 中心频率 `2400000000`（默认）| 非负标量

RF 中心频率，以 Hz 为单位，指定为非负标量。中心频率的有效范围为 70 MHz 至 6 GHz。

#### 依赖关系

要启用此参数，请将 **Source of center frequency** 设置为
`Dialog`。

**数据类型：** `double`

### **Source of gain** — 增益来源 `Dialog`（默认）| `Input Port`

增益来源，指定为以下选项之一：

- `Dialog` — 使用 **Gain (dB)** 参数指定增益。
- `Input Port` — 使用 **gain** 输入端口指定增益。

### **Gain (dB)** — 增益 `-10`（默认）| 数值标量 | 1-by-2 数值向量

增益，以 dB 为单位，指定为数值标量或 1-by-2 数值向量。有效增益范围为 –10 dB 至 77 dB。分辨率为 0.25 dB。

根据 **Channel mapping** 参数配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。
  模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为
  1-by-2 向量。向量的第 `i` 个元素应用于
  由 **Channel mapping** 参数指定的第 `i` 个通道。

#### 依赖关系

要启用此参数，请将 **Source of gain** 设置为
`Dialog`。

**数据类型：** `double`

### **Channel mapping** — 通道输入映射 `1`（默认）| `2` | `[1 2]`

通道输入映射，指定为以下值之一：

- `1` — 指定此选项以使用通道 1。
- `2` — 指定此选项以使用通道 2。
- `[1 2]` — 指定此选项以使用两个通道。

### **Baseband sample rate (Hz)** — 基带采样率 `4e6`（默认）| 正标量

基带采样率，以 Hz 为单位，指定为正标量。此参数的有效范围为 520.834 kHz 至 61.44
MHz。

**数据类型：** `double`

### 高级

### **Data source select** — 数据源 `Input Port`（默认）| `DDS`

数据源，指定为以下选项之一：

- `Input Port` — 启用 **data**
  输入端口。
- `DDS` — 启用无线电硬件上的 DDS 以生成传输数据。模块为每个通道使用两个加性音调。
  要设置音调的频率和缩放，请使用 **Tone 1 Frequency
  (Hz)**、**Tone 2 Frequency (Hz)**、**Tone 1
  Scale [0-1]** 和 **Tone 2 Scale [0-1]**
  参数。DDS 信号在 FPGA 上生成。

### **Tone 1 Frequency (Hz)** — 第一个 DDS 音调频率 `5000`（默认）| 数值标量 | 1-by-2 数值向量

第一个 DDS 音调频率，以 Hz 为单位，指定为以下选项之一：

- 数值标量 — 对于单通道使用此选项，或为所有使用中的通道指定相同
  频率。模块为 **Channel mapping** 参数指定的每个
  通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同频率。
  向量的第 `i` 个元素应用于由 **Channel
  mapping** 参数指定的第 `i` 个通道。

**Tone 1 Frequency (Hz)** 的有效范围为 0
到 **Baseband sample rate (Hz)** / 2。

#### 依赖关系

要启用此参数，请将 **Data source select** 设置为
`DDS`。

**数据类型：** `double`

### **Tone 2 Frequency (Hz)** — 第二个 DDS 音调频率 `10000`（默认）| 数值标量 | 1-by-2 数值向量

第二个 DDS 音调频率，以 Hz 为单位，指定为以下选项之一：

- 数值标量 — 对于单通道使用此选项，或为所有使用中的通道指定相同
  频率。模块为 **Channel mapping** 参数指定的每个
  通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同频率。
  向量的第 `i` 个元素应用于由 **Channel
  mapping** 参数指定的第 `i` 个通道。

**Tone 2 Frequency (Hz)** 的有效范围为 0
到 **Baseband sample rate (Hz)** / 2。

#### 依赖关系

要启用此参数，请将 **Data source select** 设置为
`DDS`。

**数据类型：** `double`

### **Tone 1 Scale [0-1]** — 第一个 DDS 音调缩放 `0.5`（默认）| 数值标量 | 1-by-2 数值向量

第一个 DDS 音调缩放，以满量程的百万分之一为单位，指定为以下选项之一：

- 数值标量 — 对于单通道使用此选项，或为所有使用中的通道指定相同
  缩放。模块为 **Channel mapping** 参数指定的每个
  通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同缩放。
  向量的第 `i` 个元素应用于由 **Channel
  mapping** 参数指定的第 `i` 个通道。

**Tone 1 Scale [0-1]** 的有效范围为 0 到
1。

#### 依赖关系

要启用此参数，请将 **Data source select** 设置为
`DDS`。

**数据类型：** `double`

### **Tone 2 Scale [0-1]** — 第二个 DDS 音调缩放 `0.25`（默认）| 数值标量 | 1-by-2 数值向量

第二个 DDS 音调缩放，以满量程的百万分之一为单位，指定为以下选项之一：

- 数值标量 — 对于单通道使用此选项，或为所有使用中的通道指定相同
  缩放。模块为 **Channel mapping** 参数指定的每个
  通道应用标量扩展。
- 1-by-2 数值向量 — 使用此选项为两个通道指定不同缩放。
  向量的第 `i` 个元素应用于由 **Channel
  mapping** 参数指定的第 `i` 个通道。

**Tone 2 Scale [0-1]** 的有效范围为 0 到
1。

#### 依赖关系

要启用此参数，请将 **Data source select** 设置为
`DDS`。

**数据类型：** `double`

## 所属库

SoC Blockset Support Package for Xilinx Devices / MPSoC / ZCU102 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZedBoard

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为设计自动生成处理器代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2019a 中引入**

### R2024b：不推荐

不建议使用此模块。请改用 AD936x Data Write。
新的 AD936x Data Write
模块包含此模块的功能，但支持 SoC builder 工作流和
IP 核生成工作流。有关 SoC 工作流的详细信息，请参阅 SoC Generation Workflows。

### R2024a：双通道支持

此模块现在支持两个发射通道。使用 **Channel mapping** 参数指示使用单通道还是双通道。

## 描述

将硬件逻辑连接到 FMCOMMS Zynq 无线电发射器硬件

Zynq and FMCOMMS2/3/4 Transmitter Configuration 模块将您的
硬件逻辑连接到 FMCOMMS2/3/4 无线电发射器硬件。在仿真中，此模块
为中心频率和增益提供可选端口，SoC Builder 工具会将这些端口
映射到硬件引脚。此模块不会在仿真中连接到无线电硬件。
