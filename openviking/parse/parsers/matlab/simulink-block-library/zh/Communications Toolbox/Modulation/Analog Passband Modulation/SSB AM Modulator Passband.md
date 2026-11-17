---
type: simulink-block
title: 'SSB AM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'ssbammodulatorpassband'
documentation_source_path: 'ref/ssbammodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# SSB AM Modulator Passband

## 端口

### 输入

### **In** — 输入信号 标量

输入信号，指定为标量。

此端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 输出信号 标量

输出信号，以标量形式返回。输出是调制信号的通带表示。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Carrier frequency (Hz)** — 载波频率，单位为 Hz `300`（默认）| 正标量

载波频率，单位为 Hz，指定为正标量。

由于 Hilbert 变换是通过滤波器实现的，为获得最佳结果，请选择载波频率 *f*c，使其至少超过输入信号采样率的 10%。有关详细信息，请参阅 Hilbert Transform Filter。

通常，合适的载波频率远高于输入信号的最高频率。根据 Nyquist 采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅 Baseband vs. Passband Simulation。

### **Initial phase (rad)** — 初始相位偏移，单位为弧度 `0`（默认）| 标量

调制信号的初始相位偏移，单位为弧度，指定为标量。

### **Sideband to modulate** — 要调制的边带 `Upper`（默认）| `Lower`

要调制的边带，指定为 `Upper` 或 `Lower`。

### **Hilbert Transform filter order (must be even)** — Hilbert 变换滤波器阶数 `100`（默认）| 正标量

Hilbert 变换滤波器阶数，指定为大于 `2` 的偶数正标量。此参数值定义用于计算 Hilbert 变换的 FIR 滤波器的长度。

## 所属库

Communications Toolbox / Modulation / Analog Passband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用单边带幅度调制进行调制

SSB AM Modulator Passband 模块使用带有 Hilbert 变换滤波器的单边带幅度调制对信号进行调制。输入和输出信号均为实标量信号。
