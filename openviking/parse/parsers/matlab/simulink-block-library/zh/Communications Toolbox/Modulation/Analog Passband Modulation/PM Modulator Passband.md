---
type: simulink-block
title: 'PM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'pmmodulatorpassband'
documentation_source_path: 'ref/pmmodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# PM Modulator Passband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。

此端口在模块上未命名。

**数据类型：** `double`

### 输出

### **Out** — 输出信号标量

输出信号，以标量形式返回。输出是已调制信号的通带表示。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **载波频率 (Hz)** — 载波频率，单位为 Hz `300`（默认）| 正标量

载波频率，单位为 Hz，指定为正标量。将载波频率 *f*c 与对应的 PM Demodulator Passband 模块匹配。

通常，合适的载波频率远高于输入信号的最高频率。根据 Nyquist 采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带与通带仿真。

### **初始相位 (rad)** — 初始相位偏移，单位为弧度 `0`（默认）| 标量

载波的初始相位偏移，以弧度为单位，指定为标量。

### **相位偏差 (rad)** — 载波频率的相位偏差，单位为弧度 `pi/2`（默认）| 标量

载波频率的相位偏差，以弧度为单位，指定为标量。也称为相位的*变化*。

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

使用相位调制进行调制

PM Modulator Passband 模块使用相位调制对信号进行调制。输出是已调制信号的通带表示。输出信号的频率随输入信号的幅度变化。输入和输出信号均为实标量信号。
