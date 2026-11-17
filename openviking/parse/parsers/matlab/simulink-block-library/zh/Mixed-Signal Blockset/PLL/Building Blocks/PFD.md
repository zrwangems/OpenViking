---
type: simulink-block
title: 'PFD'
family: 'pll'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'pfd'
documentation_source_path: 'ref/pfd.html'
language: zh-CN
chinese_source: worker-translation
---

# PFD

## 端口

### 输入

### **reference** — 参考频率标量

输入端口，用于传输参考频率以确定相位误差。

**数据类型：** `double`

### **feedback** — 反馈频率标量

输出端口，用于传输反馈频率以确定相位误差。在 PLL 系统中，VCO 的输出经时钟分频器后通过 **feedback** 端口反馈到 PFD。

**数据类型：** `double`
### 输出

### **up** — 传输参考频率标量

输出端口，用于将参考频率传输到 Charge Pump，以将相位误差转换为电流。**up** 和 **down** 端口中信号的占空比之差与 **reference** 和 **feedback** 端口中信号之间的相位差成正比。

**数据类型：** `double`

### **down** — 传输反馈频率标量

输出端口，用于将反馈频率传输到 Charge Pump，以将相位误差转换为电流。**up** 和 **down** 端口中信号的占空比之差与 **reference** 和 **feedback** 端口中信号之间的相位差成正比。

**数据类型：** `double`

## 参数

### 配置

### **Deadband compensation (s)** — 为接近零相位偏移时的有效输出添加的延迟 `30e-12`（默认） | 正实数标量

为接近零相位偏移时的有效输出添加的延迟，指定为以秒为单位的正实数标量。死区是接近零相位偏移的相位偏移带，在该带内 PFD 输出可忽略不计。

#### 编程用法

- 使用
  `get_param(gcb,'DeadbandCompensation')`
  查看 **Deadband compensation** 的当前值。
- 使用
  `set_param(gcb,'DeadbandCompensation',value)`
  将 **up Rise/fall time** 设置为特定值。

**数据类型：** `double`

### **Enable increased buffer size** — 启用增加的缓冲区大小 off（默认） | on

选择此项可在仿真期间启用增加的缓冲区大小。这会增加 PFD 模块内部 Variable Pulse Delay、Logic Decision 和 Slew Rate 模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用输入缓冲的样本数 `10`（默认） | 正整数标量

仿真期间可用输入缓冲的样本数，指定为正整数标量。这会设置 PFD 模块内部 Variable Pulse Delay、Logic Decision 和 Slew Rate 模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在 **配置** 选项卡中选中 **Enable increased buffer size** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看 **Buffer size** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **Buffer size** 设置为特定值。

**数据类型：** `double`

### 损伤

### **Enable impairments** — 将电路损伤添加到仿真 on（默认） | off

选择此项可将电路损伤（例如上升/下降时间和传播延迟）添加到仿真。默认情况下，此选项已选中。

### **Output step size calculation** — 确定如何计算输出步长 `Default`（默认） | `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据感兴趣的最大频率计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **Enable Impairments**。

### **Maximum frequency of interest (Hz)** — 输出端的感兴趣最大频率 `10e9`（默认） | 正实数标量

输出端的感兴趣最大频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **Enable Impairments**，并为 **Output step size calculation** 选择 **Advanced**。

#### 编程用法

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **Maximum frequency of interest (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **Maximum frequency of interest (Hz)** 设置为特定值。

**数据类型：** `double`

### **Rise/fall time (s)** — PFD 的 up 输出端口的 20% – 80% 上升/下降时间 `3e-11`（默认） | 正实数标量

PFD 的 up 输出端口的 20% – 80% 上升/下降时间，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **Enable Impairments**。

#### 编程用法

- 使用 `get_param(gcb,'RiseFallTime')` 查看 **Rise/fall time (s)** 的当前值。
- 使用 `set_param(gcb,'RiseFallTime',value)` 将 **Impairments** 设置为特定值。

**数据类型：** `double`

### **Propagation Delay (s)** — 从 PFD 输入端口到输出端口的延迟 `50e-12`（默认） | 正实数标量

从 PFD 的输入端口到输出端口的延迟，指定为以秒为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **Enable Impairments**。

#### 编程用法

- 使用 `get_param(gcb,'PropDelay')` 查看 **Propagation Delay (s)** 的当前值。
- 使用 `set_param(gcb,'PropDelay',value)` 将 **Propagation Delay (s)** 设置为特定值。

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

比较两个信号之间相位和频率的相位/频率检测器

PFD 模块产生两个占空比不同的输出脉冲。占空比之差与输入信号之间的相位差成正比。在频率合成器电路（例如锁相环 (PLL)）中，PFD 模块比较参考信号与 VCO 模块生成的信号之间的相位和频率，并确定相位误差。
