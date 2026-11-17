---
type: simulink-block
title: 'PS Uniform Random Number'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psuniformrandomnumber'
documentation_source_path: 'ref/psuniformrandomnumber.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Uniform Random Number

## 端口

### 输出

### **Y** — 输出物理信号，无量纲物理信号

输出物理信号。

## 参数

### **Minimum** — 最小输出值 `0`（默认）

模块生成的最小输出值。

### **Maximum** — 最大输出值 `1`（默认）

模块生成的最大输出值。

### **Seed** — 起始种子 `0`（默认）

随机数生成器的起始种子。对于给定的种子，输出是可重复的。种子必须是 0 到 (2^32 – 1) 范围内的整数。

### **Sample time** — 采样时间间隔 `1 s`（默认）

时间 *`step`* 间隔的值。默认 *`step`* 值为 `1` s。要指定初始时间偏移，请将参数值输入为 `[step, offset]`，否则 *`offset`* 值假定为 `0`。偏移量必须小于步长。

## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

为物理建模生成均匀分布的随机数

PS Random Number 模块在您指定的区间内生成均匀分布的随机数。要生成正态（高斯）分布的随机数，请使用 PS Random Number 模块。

模块行为与 Simulink® Uniform Random Number 模块相同（不同之处在于它生成物理信号而非 Simulink 信号）。

您可以选择将初始时间偏移指定为 **Sample time** 参数的一部分。在这种情况下，模块在仿真时间达到 *`offset`* 值之前输出 0，此时随机序列开始。

使用相同种子和参数的 PS Uniform Random Number 模块生成可重复的序列。每次仿真开始时，种子都会重置为指定的值。
