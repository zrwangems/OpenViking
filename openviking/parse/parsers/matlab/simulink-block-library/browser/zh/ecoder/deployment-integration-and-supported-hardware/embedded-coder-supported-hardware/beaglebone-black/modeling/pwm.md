---
type: simulink-block
title: 'PWM'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'pwm'
documentation_source_path: 'beaglebone/ref/pwm.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM

## 端口

### 输入

### **Port\_1** — 决定方波脉冲宽度的输入值，范围为 [`0`, `1`] 的正标量

模块输入继承上游模块的数据类型，并在内部将其转换为 double。发送到模块输入的值决定方波的宽度，称为 *占空比*，Raspberry Pi® 硬件在指定 PWM 引脚上输出该方波。模块输入接受从 `0` 到 `1` 的值范围（占空比的 0% 到 100%）。

例如：

- 最大输入值 `1` 将占空比设置为 100%，即全功率。
- 最小输入值 `0` 将占空比设置为 0%，即无功率。
- 中间输入值，例如 `0.333`，将占空比设置为 33.3%，即 1/3 功率。
- 超出范围的输入值，例如 `-0.2` 或 `1.2`，输出最小或最大功率。

**数据类型：** `double`

## 参数

### **Pin** — PWM 引脚编号 `P9_21`（默认） | `P9_34` | `P9_36` | `P9_45` | `P9_46` | `P9_13` | `P9_19` | `P9_42` | `P9_29` | `P9_31` | `P9_22` | `P9_28` | `P9_14` | `P9_16`

选择 PWM 输入信号连接到的 BeagleBone® 硬件板引脚编号。要打开 BeagleBone 板的引脚映射，请点击 **View pin map**。

**注意**

不要将同一引脚编号分配给模型中的多个模块。

### **Frequency (Hz)** — PWM 输出频率 2000（默认） | 非负标量

设置 PWM 信号的频率。如果有两个 PWM 模块，请将这两个模块设置为相同频率。

### **Polarity** — PWM 信号极性 `Positive`（默认） | `Negative`

设置 PWM 信号的极性。

- `Positive` — 选择此值可将数字脉冲在占空比期间设置为高电平（ON），并在周期剩余时间设置为 OFF。
- `Negative` — 选择此值可将数字脉冲在占空比期间设置为低电平（OFF），并在周期剩余时间设置为 ON。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

数字输出引脚的脉冲宽度调制

使用 PWM 模块改变数字输出引脚的功率输出。此模块使数字输出能够提供一系列不同的功率级别，类似于模拟输出的功率级别。

在没有硬件的仿真期间，此模块不执行任何操作。请参阅 Block Produces Zeros or Does Nothing in Simulation。
