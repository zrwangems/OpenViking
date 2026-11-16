---
type: simulink-block
title: 'Multiphase Clock'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'multiphaseclock'
documentation_source_path: 'ref/multiphaseclock.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiphase Clock

## 端口

### 输出

### **Port\_1** — 时钟信号向量 vector

1-by-*N* 时钟信号向量，其中使用 **Number of phases** 参数指定 *N*。有关详细信息，请参阅描述。

**数据类型：** `single` | `double` | `Boolean`

## 参数

### **Clock frequency (Hz)** — 所有时钟信号的频率 `1` (默认值) | 正标量

所有输出时钟信号的频率，指定为正标量。

### **Number of phases, N** — 输出向量中的相位数量 `4` (默认值) | 正整数

输出向量中不同相位的数量 *N*，指定为正整数标量。

### **Starting phase (1 to N)** — 起始相位对应的向量索引 `1` (默认值) | 从 1 到 *N* 的整数

最先变为有效的输出信号的向量索引，指定为从 `1` 到 *N* 的标量整数。

### **Number of phase intervals over which clock is active (1 to N-1)** — 每个输出的有效电平持续时间 `3` (默认值) | 从 1 到 *N*-1 的整数

每个输出信号的有效电平持续时间 *D*，指定为从 1 到 *N*-1 的标量整数。指定的值决定每个信号在变为有效后保持有效状态的相位间隔数。信号的有效占空比为 *D*/*N*。

### **Active level (polarity)** — 有效电平 `High (1)` (默认值) | `Low (0)`

输出的有效电平，指定为 `High (1)` 或 `Low (0)`。

### **Output data type** — 输出数据类型 `Logical` (默认值) | `Boolean`

输出数据类型，指定为 `Logical` 或 `Boolean`。

## 所属库

DSP System Toolbox / Signal Management / Switches and Counters DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` | `Boolean` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

生成多个二值时钟信号

Multiphase Clock 模块生成 1-by-*N* 时钟信号向量，其中在 **Number of phases** 参数中指定整数 *N*。*N* 个相位中的每一个都具有相同的频率 *f*，以赫兹为单位由 **Clock frequency** 参数指定。

由 **Starting phase** 参数索引的时钟信号最先变为有效，在 *t*=0 时。输出向量中的其他信号依次变为有效，每个信号比前一个信号的激活滞后 1/(*N**f*) 秒，即相位间隔。因此输出的周期为 1/(*N**f*) 秒。

有效电平可以是高 (`1`) 或低 (`0`)，由 **Active level (polarity)** 参数指定。使用 **Number of phase intervals over which the clock is active** 参数将有效电平的持续时间 *D* 指定为 1 到 *N*-1 之间的整数。此值指定每个信号在变为有效后保持有效状态的相位间隔数。信号的有效占空比为 *D*/*N*。
