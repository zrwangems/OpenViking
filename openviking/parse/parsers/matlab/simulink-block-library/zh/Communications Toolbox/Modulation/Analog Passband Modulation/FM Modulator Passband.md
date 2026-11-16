---
type: simulink-block
title: 'FM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'fmmodulatorpassband'
documentation_source_path: 'ref/fmmodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# FM Modulator Passband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。

此端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 输出信号标量

输出信号，以标量形式返回。输出是调制信号的通带表示。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

若要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中，选择**属性检查器**。

### **载波频率 (Hz)** — 以 Hz 为单位的载波频率 `300` (默认) | 正标量

以 Hz 为单位的载波频率，指定为正标量。将载波频率 *f*c 与对应的 FM Demodulator Passband 模块匹配。

通常，合适的载波频率远高于输入信号的最高频率。根据奈奎斯特采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带与通带仿真。

### **初始相位 (rad)** — 以弧度为单位的初始相位偏移 `0` (默认) | 标量

载波的初始相位偏移，以弧度为单位，指定为标量。

### **频率偏差 (Hz)** — 以 Hz 为单位的载波频率的频率偏差 `50` (默认) | 标量

以 Hz 为单位的载波频率的频率偏差，指定为标量。也称为频率的 *变化*。

## 所属库

Communications Toolbox / Modulation / Analog Baseband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用频率调制进行调制

FM Modulator Passband 模块使用频率调制对信号进行调制。输出是调制信号的通带表示。输出信号的频率随输入信号的幅度而变化。输入和输出信号均为实标量信号。
