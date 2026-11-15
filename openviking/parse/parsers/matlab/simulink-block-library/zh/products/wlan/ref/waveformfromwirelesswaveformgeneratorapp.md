---
type: simulink-block
title: 'Waveform From Wireless Waveform Generator App'
family: 'wlan'
product_id: 'wlan'
product_name: 'WLAN Toolbox'
documentation_release: R2025b
official_category: 'Test and Measurement'
documentation_page: 'waveformfromwirelesswaveformgeneratorapp'
documentation_source_path: 'ref/waveformfromwirelesswaveformgeneratorapp.html'
language: zh-CN
chinese_source: worker-translation
---

# Waveform From Wireless Waveform Generator App

## 端口

### 输出

### **wf** — 时域无线波形 complex matrix

时域无线波形，返回为 complex matrix。矩阵列数对应于发射天线数量。您在应用中选择的波形类型决定输出波形类型。要访问波形配置参数，请使用 `UserData` 公共模块属性的 `WaveformConfig` 结构体字段。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### 只读波形参数

该模块会根据 **Code** 选项卡中的波形配置自动更新这些参数。

### **Waveform sample rate (Fs)** — 波形采样率 numeric scalar

此参数为只读。

要访问此参数，请使用 `UserData` 公共模块属性的 `Fs` 结构体字段。`Fs` 结构体字段的单位为 Hz。

### **Waveform length** — 波形长度 positive integer

此参数为只读。

要访问此参数，请使用 `UserData` 公共模块属性的 `WaveformLength` 结构体字段。`WaveformLength` 结构体字段的单位为 samples。

### 仿真参数

这些参数控制模块在仿真期间如何输出波形。

### **Samples per frame** — 每帧采样数 `1`（默认）| positive integer

此参数指定要缓冲到每个输出帧中的采样数。

### **Form output after final data value by** — 最后一个波形采样后的输出值 `Cyclic repetition`（默认）| `Setting to zero`

此参数指定模块输出完所有可用波形采样后的输出值。

- 当您选择 `Cyclic Repetition` 时，模块在到达波形中的最后一个采样后从头重复波形。
- 当您选择 `Setting To Zero` 时，模块在生成最后一帧波形后，在仿真持续时间内生成零值输出。

## 所属库

无

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

导出到 Simulink 的无线波形源

Waveform From Wireless Waveform Generator App 模块是使用 Wireless Waveform Generator 应用生成的。您可以将生成的模块用作 Simulink® 模型中的无线波形源。

**注意**

实际模块名称和输出波形取决于您在生成模块之前在应用中配置的波形。

有关可使用 WLAN Toolbox™ 软件导出到 Simulink 的波形类型的概述，请参阅 WLAN Waveform Generator 应用。

要生成模块：

1. 在应用工具条上的 **Waveform Type** 部分，单击要配置并导出到 Simulink 的波形。
2. 设置所选波形的参数。
3. 在应用工具条上的 **Export** 部分，单击 **Export**，然后选择 **Export to Simulink**。

Mask Editor 窗口的 **Code** 选项卡包含模块执行以输出已配置波形的 MATLAB® 代码。要访问只读模块参数和波形配置参数，请使用 `UserData` 公共模块属性，该属性是一个包含以下字段的结构体。

- `WaveformConfig` — 波形配置参数
- `WaveformLength` — 波形长度
- `Fs` — 波形采样率

有关如何使用生成的模块的详细信息，请参阅使用 App 生成的模块在 Simulink 中生成无线波形。
