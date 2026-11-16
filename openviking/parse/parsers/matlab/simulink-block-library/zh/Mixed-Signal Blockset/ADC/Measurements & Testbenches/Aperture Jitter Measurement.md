---
type: simulink-block
title: 'Aperture Jitter Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'aperturejittermeasurement'
documentation_source_path: 'ref/aperturejittermeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Aperture Jitter Measurement

## 端口

### 输入

### **clk** — 时钟信号输入标量

时钟信号输入，指定为以 volts 为单位的标量。

**数据类型：** `double`
### 输出

### **jitter** — 抖动输出标量

孔径抖动输出，以 seconds 为单位的标量形式返回。

**数据类型：** `double`

## 参数

### **Frequency** — 输入时钟频率 `1e6`（默认）| 实数正标量

输入时钟频率，指定为以 Hz 为单位的实数正标量。

#### 编程用法

- 使用 `get_param(gcb,'Frequency')` 查看 **Frequency** 的当前值。
- 使用 `set_param(gcb,'Frequency',value)` 将 **Frequency** 设置为特定值。

### **Recommended min. simulation stop time** — 仿真必须运行以获得有意义结果的最短时间 `9.901e-05`（默认）| 标量

仿真必须运行以获得有意义结果的最短时间，指定为以 seconds 为单位的标量。此值根据用于测量孔径抖动的 JEDEC Standards 计算。

#### 信号范围

### **Min** — 时钟信号的最小值 `0`（默认）| 实数标量

时钟信号的最小值，指定为以 volts 为单位的实数标量。

#### 编程用法

- 使用 `get_param(gcb,'InputMin')` 查看 **Min** 的当前值。
- 使用 `set_param(gcb,'InputMin',value)` 将 **Min** 设置为特定值。

### **Max** — 时钟信号的最大值 `1`（默认）| 实数标量

时钟信号的最大值，指定为以 volts 为单位的实数标量。

#### 编程用法

- 使用 `get_param(gcb,'InputMax')` 查看 **Max** 的当前值。
- 使用 `set_param(gcb,'InputMax',value)` 将 **Max** 设置为特定值。

### **Hold off time (s)** — 测量分析前的延迟 `0`（默认）| 非负实数标量

延迟测量分析，以避免瞬态导致测量结果损坏，指定为以 seconds 为单位的非负实数标量。

#### 编程用法

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **Hold off time (s)** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **Hold off time (s)** 设置为特定值。

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

测量周期信号的孔径抖动

Aperture Jitter Measurement 测量周期信号的孔径抖动。在实际数据转换器中，采样时钟信号的采样边沿与实际采集样本的时刻之间存在延迟。此延迟称为孔径延迟。孔径抖动是孔径延迟的逐样本变化。
