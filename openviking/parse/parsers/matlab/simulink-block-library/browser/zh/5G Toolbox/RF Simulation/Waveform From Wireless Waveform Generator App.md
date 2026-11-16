---
type: simulink-block
title: 'Waveform From Wireless Waveform Generator App'
family: '5g'
product_id: '5g'
product_name: '5G Toolbox'
documentation_release: R2025b
official_category: 'RF Simulation'
documentation_page: 'waveformfromwirelesswaveformgeneratorapp'
documentation_source_path: 'ref/waveformfromwirelesswaveformgeneratorapp.html'
language: zh-CN
chinese_source: official
---

# Waveform From Wireless Waveform Generator App

## 端口

### 输出

### **wf** — 时域无线波形 复矩阵

时域无线波形，以复矩阵形式返回。矩阵列的数量对应于发射天线的数量。您在该 App 中选择的波形类型决定了输出波形类型。要访问波形配置参数，请使用 `UserData` 通用模块属性的 `WaveformConfig` 结构体字段。

**数据类型:** `double`
**复数支持:** 是

## 参数

### 只读波形参数

模块会根据**代码**选项卡中的波形配置自动更新以下参数。

### **波形采样率(Fs)** — 波形采样率 数值标量

此参数为只读参数。

要访问此参数，请使用 `UserData` 通用模块属性的 `Fs` 结构体字段。`Fs` 结构体字段的单位为 Hz。

### **波形长度** — 波形长度 正整数

此参数为只读参数。

要访问此参数，请使用 `UserData` 通用模块属性的 `WaveformLength` 结构体字段。`WaveformLength` 结构体字段的单位为采样数。

### 仿真参数

这些参数控制模块在仿真期间如何输出波形。

### **每帧采样数** — 每帧采样数 `1` (默认) | 正整数

此参数指定缓冲到每个输出帧的采样数。

### **最终数据值之后的输出** — 最后一次波形采样后的输出值 **循环重复** (默认) | **设置为零**

此参数指定模块输出所有可用波形采样后的输出值。

- 当您选择**循环重复**时，模块在到达波形中的最后一个采样后，从头开始重复波形。
- 当您选择**设置为零**时，模块在生成波形的最后一帧后，在仿真的持续时间内生成零值输出。

## 所属库

None

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2021b 中推出**

## 描述

导出到 Simulink 的无线波形源

Waveform From Wireless Waveform Generator App 模块是使用无线波形发生器生成的。您可以将生成的模块用作 Simulink® 模型中的无线波形源。

**注意**

实际的模块名称和输出波形取决于您在生成模块之前在该 App 中配置的波形。

有关可使用 5G Toolbox™ 软件导出到 Simulink 的波形类型的概述，请参阅 5G 波形生成器。

要生成模块，请执行以下操作：

1. 在该 App 工具条的**波形类型**部分中，点击您想要配置并导出到 Simulink 的波形。
2. 设置所选波形的参数。
3. 在该 App 工具条的**导出**部分中，点击**导出**并选择**导出到 Simulink**。

封装编辑器窗口的**代码**选项卡包含执行模块以输出配置波形的 MATLAB® 代码。要访问只读模块参数和波形配置参数，请使用 `UserData` 通用模块属性，这是一个具有这些字段的结构体。

- `WaveformConfig` - 波形配置参数
- `WaveformLength` - 波形长度
- `Fs` - 波形采样率

有关如何使用生成的模块的详细信息，请参阅使用 App 生成的模块在 Simulink 中生成无线波形。
