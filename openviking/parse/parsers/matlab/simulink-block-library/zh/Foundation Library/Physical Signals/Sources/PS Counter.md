---
type: simulink-block
title: 'PS Counter'
family: 'physical-signals'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'pscounter'
documentation_source_path: 'ref/pscounter.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Counter

## 端口

### 输出

### **Y** — 输出物理信号，无量纲物理信号

输出物理信号。

## 参数

### **采样时间** — 采样时间间隔 `1 s`（默认）

时间 *`step`* 间隔的值和单位。默认 *`step`* 值为 `1` s。要指定初始时间偏移，请将参数值输入为 `[ step , offset ]`，否则 *`offset`* 值假定为 `0`。

### **初始值** — 时间零点的输出 `0`（默认）

第一个计数周期开始时输出信号的值。如果通过 **采样时间** 参数指定初始时间偏移，则模块的输出保持此值，直到仿真时间达到 *`offset`* 值，之后第一个计数周期开始。该值必须为整数。

### **复位值** — 最小输出 `0`（默认）

除第一个计数周期外，每个计数周期开始时输出信号的值。模块的输出保持此值一个时间 *`step`*，由 **采样时间** 参数指定。该值必须为整数。

### **最大值** — 最大输出 `intmax`（默认）

计数周期结束时输出信号的值。模块的输出保持此值一个时间 *`step`*，由 **采样时间** 参数指定，此时信号返回到 **复位值**，循环重新开始。该值必须为整数。默认值为 `intmax`（2147483647，MATLAB® 软件中可用 32 位整数表示的最大正值）。

## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019a: 单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

每个时间步将输出信号递增 1

PS Counter 模块在每个时间步将输出信号 *Y* 递增 1，在最小值（复位值）和最大值之间反复递增。您可以选择指定一个不同于复位值的初始信号值，以及一个初始时间偏移。模块生成的输出信号如下图所示。

如果指定了初始时间偏移，则模块输出初始信号值 *`init`*，直到仿真时间达到 *`offset`* 值，此时计数周期开始。模块输出当前值一个时间步，然后重复将信号值递增 1 并输出一个时间步，直到达到最大值 *`max`*。模块输出 *`max`* 值一个时间步，然后返回到 *`reset`* 值，计数周期重新开始。

将此模块与其他物理信号模块结合使用，以对离散行为进行建模。

Discrete-Time PWM Voltage Source 示例说明了如何使用 PS Counter 模块构建具有更复杂行为的组件。有关替代的异步实现，请参阅 Asynchronous PWM Voltage Source 示例。离散时间版本更适合固定步长求解器和硬件在环应用，而异步实现更适合使用变步长求解器进行快速桌面仿真。
