---
type: simulink-block
title: 'DSB AM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Analog Passband Modulation'
documentation_page: 'dsbammodulatorpassband'
documentation_source_path: 'ref/dsbammodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# DSB AM Modulator Passband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。

该端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 输出信号标量

输出信号，以标量形式返回。输出是已调信号的通带表示。

该端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### **输入信号偏移** — 输入信号偏移因子 `1`（默认）| 标量

输入信号偏移因子，指定为标量。此值应大于或等于输入信号最小值的绝对值。

### **载波频率 (Hz)** — 载波频率，以 Hz 为单位 `300`（默认）| 正标量

载波频率，以 Hz 为单位，指定为正标量。

通常，合适的载波频率远高于输入信号的最高频率。根据 Nyquist 采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带仿真与通带仿真。

### **初始相位 (rad)** — 载波初始相位偏移，以弧度为单位 `0`（默认）| 标量

载波的初始相位偏移，以弧度为单位，指定为标量。

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

使用双边带幅度调制进行调制

DSB AM Modulator Passband 模块使用双边带幅度调制对信号进行调制。
