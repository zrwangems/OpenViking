---
type: simulink-block
title: 'PWM Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgenerator'
documentation_source_path: 'ref/pwmgenerator.html'
language: zh-CN
chinese_source: official
---

# PWM Generator

## 端口

### 输入

### **DC** — 占空比 标量

占空比在 `[0,1]` 范围内。

**数据类型:** `single` | `double`
### 输出

### **PWM** — PWM 信号 标量

脉冲宽度调制信号。

**数据类型:** `single` | `double`

## 参数

### **载波计数器** — 载波计数器策略 **递增** (默认) | **递减** | **增减**

使用载波计数器策略更改 PWM 输出的初始行为：

- 递增计数器 - PWM 输出在 `on` 状态开始时开始。
- 递减计数器 - PWM 输出在 `off` 状态开始时开始。
- 增减计数器 - PWM 输出在 `on` 状态的中间开始。

### **计时器周期(秒)** — PWM 周期 `0.001` (默认) | 正数

PWM 计时器周期。

如果您将**载波计数器**设置为**递增计数器**或**递减计数器**，则**计时器周期(秒)** 参数指定为 1fsw，其中 fsw 是开关频率。如果您将**载波计数器**设置为**增减计数器**，则**计时器周期(秒)** 参数指定为 12fsw。

### **相位延迟(秒)** — 相位延迟 `0` (默认) | 非负数

相位延迟，以秒为单位。添加相位延迟以更改计数器的初始状态。

### **采样时间** — 模块采样时间 `5e-5` (默认) | 正数

模块的采样时间。对于连续时间仿真，设置为零。对于离散时间仿真，为确保生成信号具有足够的分辨率，请指定一个小于或等于 `Tper/10` 的正值，其中 *Tper* 是**计时器周期(秒)**。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

生成脉冲宽度调制信号或波形

PWM Generator 模块实现 PWM 发生器。脉冲宽度调制技术通过在满功率传输和无功率传输之间快速切换，来控制从一个电气组件到另一个电气组件的功率传输。

### 工作原理

当占空比大于载波计数器值时，PWM Generator 模块输出 `1`，否则输出 `0`。您可以通过指定计时器周期 *Tper* 来设置每个周期的持续时间。您可以通过指定以下三种载波计数器类型之一来更改 PWM 输出的初始输出或相位：

- 递增计数器 - PWM 输出信号在 `on` 周期开始时初始化。下图显示了载波计数器信号和相应的 PWM 输出。
- 递减计数器 - PWM 输出信号在 `off` 周期开始时初始化。下图显示了载波计数器信号和相应的 PWM 输出。
- 增减计数器 - PWM 输出信号在 `on` 周期的中途初始化。下图显示了载波计数器信号和相应的 PWM 输出。
