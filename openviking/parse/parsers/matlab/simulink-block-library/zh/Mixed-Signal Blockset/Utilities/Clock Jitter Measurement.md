---
type: simulink-block
title: 'Clock Jitter Measurement'
family: 'utilities'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'clockjittermeasurement'
documentation_source_path: 'ref/clockjittermeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Clock Jitter Measurement

## 端口

### 输入

### **clock** — 输入时钟信号标量

输入时钟信号，指定为标量。输入信号在每个周期内必须只有一个阈值交叉。

**数据类型：** `double`

### 输出

### **Period Jitter** — 周期抖动的运行 RMS 值标量

截至当前时间步计算出的周期抖动运行 RMS 值，以标量形式返回。周期抖动是时钟信号的周期时间相对于理想周期的偏差。

**数据类型：** `double`

### **C2C** — 周期到周期抖动的运行 RMS 值标量

截至当前时间步计算出的周期到周期抖动运行 RMS 值，以标量形式返回。周期到周期抖动是时钟连续两个周期之间的周期差。

#### 依赖关系

要启用此端口，请选择 **Cycle-2-Cycle (C2C) Jitter**。

**数据类型：** `double`

### **DCD** — 实际占空比与 50% 值之差标量

实际占空比（以百分比表示）与理想 50% 值之差，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Duty Cycle Distortion (DCD)**。

**数据类型：** `double`

## 参数

### **Clock Frequency** — 输入时钟信号的频率 `1e6`（默认）| 正实数标量

输入时钟信号的频率，指定为以 Hz 为单位的正实数标量。**Clock Frequency** 用于计算输入信号周期的理想值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Frequency` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1e6` |

### **Threshold** — 阈值信号电平 `0`（默认）| 实数标量

用于计算信号上升沿和下降沿的阈值信号电平，指定为实数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Threshold` |
| **类型：** character vector |
| **值：** 实数标量 |
| **默认值：** `0` |

### **Period Jitter** — RMS 周期抖动 on（默认）| off

选择以计算 RMS 周期抖动。默认情况下选中此选项。

周期抖动是时钟信号的周期时间相对于理想周期的偏差。

### **Cycle-2-Cycle (C2C) Jitter** — RMS 周期到周期抖动 off（默认）| on

选择以计算 RMS 周期到周期（C2C）抖动。默认情况下取消选中此选项。

周期到周期抖动是时钟连续两个周期之间的周期差。

### **Duty Cycle Distortion (DCD)** — 每个周期的占空比失真 off（默认）| on

选择以计算每个周期的占空比失真。默认情况下取消选中此选项。

占空比失真是实际占空比（以百分比表示）与理想 50% 值之差。

### **Simulate using** — 选择仿真模式 `Code generation`（默认）| `Interpreted execution`

选择仿真模式。此选择会影响仿真性能。

使用 `Code generation` 方法对模型进行仿真需要额外的启动时间，但后续仿真运行更快。使用 `Interpreted execution` 方法对模型进行仿真可能会减少启动时间，但后续仿真运行更慢。有关详细信息，请参阅 Interpreted Execution vs. Code Generation。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

测量周期性信号中的抖动

使用 Clock Jitter Measurement 模块测量时钟信号中的 RMS（均方根）周期性抖动。还可以测量周期到周期（C2C）抖动和占空比失真（DCD）。
