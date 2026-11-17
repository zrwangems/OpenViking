---
type: simulink-block
title: 'PS Random Number'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psrandomnumber'
documentation_source_path: 'ref/psrandomnumber.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Random Number

## 端口
```yaml
ports:
- name: Y
  summary: 输出物理信号，无量纲物理信号
  direction: output
```

### 输出

### **Y** — 输出物理信号，无量纲物理信号

输出物理信号。
## 参数
```yaml
parameters:
- name: Mean
  summary: 随机数的均值 0（默认值）
  group: ''
- name: Variance
  summary: 随机数的方差 1（默认值）
  group: ''
- name: Seed
  summary: 起始种子 0（默认值）
  group: ''
- name: Sample time
  summary: 采样时间间隔 1 s（默认值）
  group: ''
```

### **Mean** — 随机数的均值 `0`（默认值）

模块生成的随机数的均值。

### **Variance** — 随机数的方差 `1`（默认值）

模块生成的随机数的方差。

### **Seed** — 起始种子 `0`（默认值）

随机数生成器的起始种子。对于给定的种子，输出是可重复的。种子必须是 0 到 (2^32 – 1) 范围内的整数。

### **Sample time** — 采样时间间隔 `1 s`（默认值）

时间 *`step`* 间隔的值。默认的 *`step`* 值为 `1` s。要指定初始时间偏移，请将参数值输入为 `[step, offset]`，否则 *`offset`* 值假定为 `0`。偏移量必须小于步长。
## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

为物理建模生成正态分布随机数

PS Random Number 模块生成正态（高斯）分布随机数。要生成均匀分布随机数，请使用 PS Uniform Random Number 模块。

该模块的行为与 Simulink® Random Number 模块相同（不同之处在于它生成物理信号而非 Simulink 信号），并基于极值拒绝法（[1]、[2]）。

您可以选择在 **Sample time** 参数中指定初始时间偏移。在这种情况下，模块在仿真时间达到 *`offset`* 值之前输出 0，此时随机序列开始。

使用相同种子和参数的 PS Random Number 模块生成可重复的序列。每次仿真开始时，种子都会重置为指定值。默认情况下，模块生成的序列均值为 0，方差为 1。
