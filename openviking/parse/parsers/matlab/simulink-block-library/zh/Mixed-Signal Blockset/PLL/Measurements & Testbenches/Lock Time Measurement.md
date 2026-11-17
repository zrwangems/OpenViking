---
type: simulink-block
title: 'Lock Time Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'locktimemeasurement'
documentation_source_path: 'ref/locktimemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Lock Time Measurement

## 端口

### 输入

### **pll out** — 输入时钟信号 标量

输入到 Lock Time Measurement 模块的输入时钟信号，指定为标量。**pll out** 端口连接到 PLL 系统的输出。

**数据类型：** `double`
### 输出

### **lock time** — PLL 实现锁定所需的时间 实正标量

PLL 系统中实现锁定所需的时间，以秒为单位返回为实正标量。

**数据类型：** `double`

## 参数

### **Target frequency (Hz)** — 用于测量锁定时间的 PLL 目标工作频率 `2.1e9`（默认值）| 实正标量

被测 PLL 器件（DUT）的目标工作频率，用于测量 PLL 的锁定时间，以 Hz 为单位指定为实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'TargetFreq')` 查看 **Target frequency** 的当前值。
- 使用 `set_param(gcb,'TargetFreq',value)` 将 **Target frequency** 设置为特定值。

### **Error tolerance (Hz)** — 锁定时间测量的误差容限 `1e5`（默认值）| 实正标量

锁定时间测量的误差容限，以 Hz 为单位指定为实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'FreqErrorTol')` 查看 **Error tolerance** 的当前值。
- 使用 `set_param(gcb,'FreqErrorTol',value)` 将 **Error tolerance** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

测量 PLL 在给定容限内达到目标频率所需的时间

Lock Time Measurement 模块测量锁相环（PLL）系统的锁定时间。锁定时间是 PLL 在给定误差容限内达到目标频率所需的时间。
