---
type: simulink-block
title: 'Waveform From Wireless Waveform Generator App'
family: 'lte'
product_id: 'lte'
product_name: 'LTE Toolbox'
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

### **wf** — 时域无线波形复矩阵

时域无线波形，以复矩阵形式返回。矩阵的列数对应于发射天线数。您在应用中选择的波形类型决定输出波形类型。要访问波形配置参数，请使用 `UserData` 公共模块属性的 `WaveformConfig` 结构字段。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### 只读波形参数

模块会根据 **代码** 选项卡中的波形配置自动更新这些参数。

### **波形采样率 (Fs)** — 波形采样率数值标量

此参数为只读。

要访问此参数，请使用 `UserData` 公共模块属性的 `Fs` 结构字段。`Fs` 结构字段的单位为 Hz。

### **波形长度** — 波形长度正整数

此参数为只读。

要访问此参数，请使用 `UserData` 公共模块属性的 `WaveformLength` 结构字段。`WaveformLength` 结构字段的单位为 samples。

### 仿真参数

这些参数控制模块在仿真期间如何输出波形。

### **每帧样本数** — 每帧样本数 `1`（默认）| 正整数

此参数指定要缓冲到每个输出帧中的样本数。

### **在最终数据值之后形成输出的方式** — 最后一个波形样本之后的输出值 `Cyclic repetition`（默认）| `Setting to zero`

此参数指定在模块输出所有可用波形样本之后的输出值。

- 当您选择 `Cyclic Repetition` 时，模块在到达波形中的最后一个样本后从头重复波形。
- 当您选择 `Setting To Zero` 时，模块在生成波形的最后一帧后，在仿真持续时间内生成零值输出。

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

Waveform From Wireless Waveform Generator App 模块使用 Wireless Waveform Generator 应用生成。您可以将生成的模块用作 Simulink® 模型中的无线波形源。

**注意**

实际的模块名称和输出波形取决于您在生成模块之前在该应用中配置的波形。

有关可使用 LTE Toolbox™ 软件导出到 Simulink 的波形类型的概述，请参阅 LTE Waveform Generator 应用。

要生成模块：

1. 在应用工具条的 **波形类型** 部分中，点击要配置并导出到 Simulink 的波形。
2. 设置所选波形的参数。
3. 在应用工具条的 **导出** 部分中，点击 **导出**，然后选择 **导出到 Simulink**。

封装编辑器窗口的 **代码** 选项卡包含模块执行以输出所配置波形的 MATLAB® 代码。要访问只读模块参数和波形配置参数，请使用 `UserData` 公共模块属性，它是一个包含以下字段的结构体。

- `WaveformConfig` — 波形配置参数
- `WaveformLength` — 波形长度
- `Fs` — 波形采样率

有关如何使用生成的模块的更多信息，请参阅使用应用生成的模块在 Simulink 中生成无线波形。
