---
type: simulink-block
title: 'PM Demodulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Analog Passband Modulation'
documentation_page: 'pmdemodulatorpassband'
documentation_source_path: 'ref/pmdemodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# PM Demodulator Passband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。输入是已调制信号的通带表示。

此端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 解调输出信号标量

解调输出信号，以标量形式返回。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **载波频率 (Hz)** — 以 Hz 为单位的载波频率 `300` (默认) | 正标量

载波频率，以 Hz 为单位，指定为正标量。

由于 Hilbert 变换是通过滤波器实现的，为获得最佳结果，请选择载波频率 *f*c，使其至少超过输入信号采样率的 10%。

通常，合适的载波频率远高于输入信号的最高频率。根据 Nyquist 采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带与通带仿真。

### **初始相位 (rad)** — 以弧度为单位的初始相位偏移量 `0` (默认) | 标量

载波的初始相位偏移量，以弧度为单位，指定为标量。

### **相位偏差 (rad)** — 以弧度为单位的载波频率相位偏差 `pi/2` (默认) | 标量

载波频率的相位偏差，以弧度为单位，指定为标量。也称为相位的 *变化*。

### **Hilbert 变换滤波器阶数（必须为偶数）** — Hilbert 变换滤波器阶数 `100` (默认) | 正标量

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

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 PM 调制数据

PM Demodulator Passband 模块对使用相位调制进行调制的信号进行解调。输入是已调制信号的通带表示。输入和输出信号均为实标量信号。
