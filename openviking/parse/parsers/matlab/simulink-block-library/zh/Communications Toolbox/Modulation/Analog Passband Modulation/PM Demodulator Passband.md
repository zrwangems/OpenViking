---
type: simulink-block
title: 'PM Demodulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'pmdemodulatorpassband'
documentation_source_path: 'ref/pmdemodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# PM Demodulator Passband

## 端口

### 输入

### **In** — 输入信号 标量

输入信号，指定为标量。输入是已调制信号的通带表示。

该端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 解调输出信号 标量

解调输出信号，以标量形式返回。

该端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Carrier frequency (Hz)** — 载波频率，单位为 Hz `300`（默认）| 正标量

载波频率，单位为 Hz，指定为正标量。

由于希尔伯特变换是通过滤波器实现的，为获得最佳结果，请选择载波频率 *f*c，使其至少比输入信号的采样率高出 10%。

通常，合适的载波频率远高于输入信号的最高频率。根据奈奎斯特采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带与通带仿真。

### **Initial phase (rad)** — 初始相位偏移，单位为弧度 `0`（默认）| 标量

载波的初始相位偏移，单位为弧度，指定为标量。

### **Phase deviation (rad)** — 载波频率的相位偏差，单位为弧度 `pi/2`（默认）| 标量

载波频率的相位偏差，单位为弧度，指定为标量。也称为相位的*变化*。

### **Hilbert transform filter order (must be even)** — 希尔伯特变换滤波器阶数 `100`（默认）| 正标量

希尔伯特变换滤波器阶数，指定为大于 `2` 的偶数正标量。该参数值定义了用于计算希尔伯特变换的 FIR 滤波器的长度。

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

**在 R2006a 之前推出**

## 描述

解调 PM 调制数据

PM Demodulator Passband 模块解调使用相位调制进行调制的信号。输入是已调制信号的通带表示。输入和输出信号均为实标量信号。
