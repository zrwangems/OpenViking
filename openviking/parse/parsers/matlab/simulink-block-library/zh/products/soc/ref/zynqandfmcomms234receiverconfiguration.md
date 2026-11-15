---
type: simulink-block
title: 'Zynq and FMCOMMS2/3/4 Receiver Configuration'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices / Other'
documentation_page: 'zynqandfmcomms234receiverconfiguration'
documentation_source_path: 'ref/zynqandfmcomms234receiverconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Zynq and FMCOMMS2/3/4 Receiver Configuration

## 端口

### 输入

### **center frequency** — 外部 RF 中心频率非负有限标量

外部 RF 中心频率，指定为端口上的非负有限标量。有效的中心频率范围是从 70 MHz 到 6 GHz。

#### 依赖项

要启用此端口，请将 **Source of center frequency** 参数设置为 `Input Port`。

**数据类型：** `double`

### **gain** — 外部增益数值标量 | 1×2 数值向量

外部增益，指定为数值标量或 1×2 数值向量。有效增益范围是 –10 dB 到 77 dB。分辨率为 0.25 dB。

根据 **Channel mapping** 参数配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。该模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1×2 向量。向量的第 `i` 个元素应用于 **Channel mapping** 参数指定的第 `i` 个通道。

#### 依赖项

要启用此端口，请将 **Source of gain** 参数设置为 `Input Port`。

**数据类型：** `double`

## 参数

Zynq and FMCOMMS2/3/4 Receiver Configuration 模块最多支持两个通道接收数据。使用 **Channel mapping** 参数指示使用单通道还是双通道。对于每个通道，您可以独立设置 **Gain (dB)** 参数，也可以将相同设置应用于所有通道。所有其他参数值均应用于每个正在使用的通道。

### 主要

### **Source of center frequency** — 中心频率源 `Dialog` (默认) | `Input Port`

中心频率源，指定为以下选项之一：

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input Port` — 使用 **center frequency** 输入端口设置中心频率。

### **Center frequency (Hz)** — RF 中心频率 `2400000000` (默认) | 非负标量

RF 中心频率，以 Hz 为单位，指定为非负标量。中心频率的有效范围是 70 MHz 到 6 GHz。

#### 依赖项

要启用此参数，请将 **Source of center frequency** 设置为 `Dialog`。

**数据类型：** `double`

### **Source of gain** — 增益源 `AGC Slow Attack` (默认) | `AGC Fast Attack` | `Dialog` | `Input Port`

增益源，指定为以下选项之一：

- `AGC Slow Attack` –– 将此模式用于功率电平缓慢变化的信号。
- `AGC Fast Attack` –– 将此模式用于功率电平快速变化的信号。
- `Dialog` — 使用 **Gain (dB)** 参数指定增益。
- `Input Port` — 使用 **gain** 输入端口指定增益。

### **Gain (dB)** — 增益 `10` (默认) | 数值标量

增益，以 dB 为单位，指定为数值标量或 1×2 数值向量。有效增益范围是 –10 dB 到 77 dB。分辨率为 0.25 dB。

根据 **Channel mapping** 参数配置设置增益。

- 对于单通道，将增益指定为标量。
- 对于使用相同增益值的两个通道，将增益指定为标量。该模块通过标量扩展应用增益。
- 对于使用不同增益值的两个通道，将增益指定为 1×2 向量。向量的第 `i` 个元素应用于 **Channel mapping** 参数指定的第 `i` 个通道。

#### 依赖项

要启用此参数，请将 **Source of gain** 设置为 `Dialog`。

**数据类型：** `double`

### **Channel mapping** — 通道输出映射 `1` (默认) | `2` | `[1 2]`

通道输出映射，指定为以下值之一：

- `1` — 指定此选项以使用通道 1。
- `2` — 指定此选项以使用通道 2。
- `[1 2]` — 指定此选项以使用两个通道。

### **Baseband sample rate (Hz)** — 基带采样率 `4e6` (默认) | 正标量

基带采样率，以 Hz 为单位，指定为正标量。此参数的有效范围是 520.834 kHz 到 61.44 MHz。

**数据类型：** `double`

### 高级

### **Enable quadrature tracking** — 正交跟踪 `on` (默认) | `off`

选择此参数时，模块会应用同相和正交 (IQ) 不平衡补偿。

### **Enable RF DC tracking** — RF DC 跟踪 `on` (默认) | `off`

选择此参数时，模块会应用 RF 直流 (DC) 阻塞滤波器。

### **Enable baseband DC tracking** — 基带 DC 跟踪 `on` (默认) | `off`

选择此参数时，模块会应用基带 DC 阻塞滤波器。

## 所属库

SoC Blockset Support Package for Xilinx Devices / MPSoC / ZCU102 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for Xilinx Devices / Zynq-7000 / ZedBoard

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要自动为您的设计生成处理器代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**R2019a 中引入**

### R2024b：不推荐

不建议使用此模块。请改用 AD936x Data Read。新的 AD936x Data Read 模块包含此模块的功能，但支持 SoC builder 工作流和 IP core generation 工作流。有关 SoC 工作流的详细信息，请参阅 SoC Generation Workflows。

### R2024a：双通道支持

该模块现在支持两个接收通道。使用 **Channel mapping** 参数指示使用单通道还是双通道。

## 描述

将硬件逻辑连接到 FMCOMMS Zynq 无线电接收器硬件

Zynq and FMCOMMS2/3/4 Receiver Configuration 模块连接到硬件逻辑中的 FMCOMMS2/3/4 无线电接收器硬件。在仿真中，此模块为 center frequency 和 gain 提供可选端口，SoC Builder 工具将这些端口映射到硬件引脚。该模块在仿真中不会连接到无线电硬件。
