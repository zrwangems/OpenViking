---
type: simulink-block
title: 'Lock Time Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Measurements and Testbenches / PLL'
documentation_page: 'locktimemeasurement'
documentation_source_path: 'ref/locktimemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Lock Time Measurement

## 端口

### 输入

### **pll out** — 输入时钟信号 scalar

Lock Time Measurement 模块的输入时钟信号，指定为 scalar。**pll out** 端口连接到 PLL 系统的输出。

**数据类型：** `double`

### 输出

### **lock time** — 在 PLL 中实现锁定所需的时间，real positive scalar

在 PLL 系统中发生锁定的时间，以 seconds 为单位作为 real positive scalar 返回。

**数据类型：** `double`

## 参数

### **目标频率 (Hz)** — 用于测量锁定时间的 PLL 目标工作频率 `2.1e9` (默认) | real positive scalar

被测 PLL 设备 (DUT) 的目标工作频率，用于测量 PLL 的锁定时间，指定为以 Hz 为单位的 real positive scalar。

#### 编程用法

- 使用 `get_param(gcb,'TargetFreq')` 查看 **目标频率** 的当前值。
- 使用 `set_param(gcb,'TargetFreq',value)` 将 **目标频率** 设置为特定值。

### **误差容限 (Hz)** — 锁定时间测量的误差容限 `1e5` (默认) | real positive scalar

用于锁定时间测量的误差容限，指定为以 Hz 为单位的 real positive scalar。

#### 编程用法

- 使用 `get_param(gcb,'FreqErrorTol')` 查看 **误差容限** 的当前值。
- 使用 `set_param(gcb,'FreqErrorTol',value)` 将 **误差容限** 设置为特定值。

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

Lock Time Measurement 模块测量锁相环 (PLL) 系统的锁定时间。锁定时间是 PLL 在给定误差容限内达到目标频率所需的时间。
