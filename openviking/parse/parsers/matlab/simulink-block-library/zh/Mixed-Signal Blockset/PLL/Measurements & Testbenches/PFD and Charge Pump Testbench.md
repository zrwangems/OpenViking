---
type: simulink-block
title: 'PFD and Charge Pump Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'pfdandchargepumptestbench'
documentation_source_path: 'ref/pfdandchargepumptestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# PFD and Charge Pump Testbench

## 端口

### 输入

### **from PFD up** — 测量 PFD 参考频率标量

测量 PFD 模块的参考频率。

**数据类型：** `double`

### **from PFD down** — 测量 PFD 反馈频率标量

测量 PFD 模块的反馈频率。

**数据类型：** `double`

### **from charge pump** — 测量电荷泵输出电流标量

测量 Charge Pump 模块的输出电流。

**数据类型：** `double`
### 输出

### **to PFD reference** — 向 PFD 提供参考频率标量

向 PFD 提供参考频率以确定相位误差。

**数据类型：** `double`

### **to PFD feedback** — 向 PFD 提供反馈频率标量

向 PFD 模块提供反馈频率。

**数据类型：** `double`

## 参数

### 激励

### **Phase sweep (°)** — 相对于相位偏移的最大相位偏移量 `300`（默认）| 实正标量

相对于相位偏移的最大相位偏移量，以度为单位指定为实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'PhaseSweep')` 查看 **Phase sweep** 的当前值。
- 使用 `set_param(gcb,'PhaseSweep',value)` 将 **Phase sweep** 设置为特定值。

**数据类型：** `double`

### **Phase offset (°)** — 相位扫描中心的相对相位值 `0`（默认）| 实标量

相位扫描中心的相对相位值，以度为单位指定为实标量。

#### 程序化使用

- 使用 `get_param(gcb,'PhaseOffset')` 查看 **Phase offset** 的当前值。
- 使用 `set_param(gcb,'PhaseOffset',value)` 将 **Phase offset** 设置为特定值。

**数据类型：** `double`

### **Clock frequency (Hz)** — 期望的参考时钟频率 `2.5e9 Hz`（默认）| 实正标量

参考计数器输出的期望时钟频率，以 Hz 为单位指定为实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'ClockFrequency')` 查看 **Clock frequency** 的当前值。
- 使用 `set_param(gcb,'ClockFrequency',value)` 将 **Clock frequency** 设置为特定值。

**数据类型：** `double`

### **Number of phases in sweep** — 要仿真的均匀间隔相位偏移总数 `2000`（默认）| 实正标量

相位偏移扫描中均匀间隔的相位偏移数量，指定为实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'NPhases')` 查看 **Number of phases in sweep** 的当前值。
- 使用 `set_param(gcb,'NPhases',value)` 将 **Number of phases in sweep** 设置为特定值。

**数据类型：** `double`

### **Duty cycle (%)** — 激励时钟的占空比 `50`（默认）| 实正标量

参考端口和反馈端口处激励时钟的占空比，指定为实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'DutyCycle')` 查看 **Duty cycle** 的当前值。
- 使用 `set_param(gcb,'NPhases',value)` 将 **Duty cycle** 设置为特定值。

**数据类型：** `double`

### 设置

### **Plot figures on top after simulation** — 仿真后将图形绘制在最上层 on（默认）| off

选择此项可在仿真后将图形绘制在所有其他窗口的最上层。默认情况下，此选项处于选中状态。

### **Report PFD metrics** — 报告 PFD 指标 on（默认）| off

选择此项可在 PFD and Charge Pump Testbench 的图标上显示 PFD 指标（Deadband、Linear Range 和 Propagation delay）。默认情况下，此选项处于选中状态。

**数据类型：** `double`

### **Report Charge Pump metrics** — 报告 Charge Pump 指标 on（默认）| off

选择此项可在 PFD and Charge Pump Testbench 的图标上显示 Charge Pump 指标（Sensitivity、Phase offset 和 Spur current）。默认情况下，此选项处于选中状态。

**数据类型：** `double`

### **Logic Threshold (V)** — 电荷泵输入端的开关阈值 `0.5`（默认）| 实数标量

电荷泵输入端的开关阈值，指定为以 V 为单位的实数标量。它是测量上升沿和下降沿时序的电压。

#### 程序化使用

- 使用 `get_param(gcb,'VSwitch')` 查看 **Logic Threshold** 的当前值。
- 使用 `set_param(gcb,'VSwitch',value)` 将 **Logic Threshold** 设置为特定值。

**数据类型：** `double`

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 PFD and Charge Pump Testbench 内部 Variable Pulse Delay 和 Logic Decision 模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `5`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。这会设置 PFD and Charge Pump Testbench 内部的 Variable Pulse Delay 和 Logic Decision。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入采样。

#### 依赖关系

此参数仅在 **Configuration** 选项卡中选中 **Enable increased buffer size** 选项时可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBuffer')` 查看 **Buffer size** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **Buffer size** 设置为特定值。

### Target Metrics

#### PFD Metrics

### **Target deadband (°)** — 零相位偏移附近降低灵敏度区域的最大可接受大小 `0`（默认）| 实数非负标量

零相位偏移附近降低灵敏度区域的最大可接受大小，指定为以度为单位的实数非负标量。它指的是死区区域的大小。

#### 程序化使用

- 使用 `get_param(gcb,'TgtDeadband')` 查看 **Target deadband** 的当前值。
- 使用 `set_param(gcb,'TgtDeadband',value)` 将 **Target deadband** 设置为特定值。

**数据类型：** `double`

### **Target linear range (°)** — 输出保持近似等于输入偏移的最大相位偏移 `290`（默认）| 实数正标量

输出保持近似等于输入偏移的最大相位偏移，指定为以度为单位的实数正标量。

#### 程序化使用

- 使用 `get_param(gcb,'TgtRange')` 查看 **Target linear range** 的当前值。
- 使用 `set_param(gcb,'TgtRange',value)` 将 **Target linear range** 设置为特定值。

**数据类型：** `double`

### **Target propagation delay (s)** — 从输入到输出的最大可接受延迟 `60e-12`（默认）| 实数正标量

从输入到输出的最大可接受延迟，指定为以 s 为单位的实数正标量。

#### 程序化使用

- 使用 `get_param(gcb,'TgtPropDelay')` 查看 **Target propagation delay** 的当前值。
- 使用 `set_param(gcb,'TgtPropDelay',value)` 将 **Target propagation delay** 设置为特定值。

**数据类型：** `double`

### **Target rise/fall time (s)** — 最大可接受 20% – 80% 上升/下降时间 `30e-12`（默认）| 实数正标量

最大可接受 20% – 80% 上升/下降时间，指定为以 s 为单位的实数正标量。

#### 程序化使用

- 使用 `get_param(gcb,'TgtRiseFall')` 查看 **Target rise/fall time** 的当前值。
- 使用 `set_param(gcb,'TgtRiseFall',value)` 将 **Target rise/fall time** 设置为特定值。

**数据类型：** `double`

#### Charge Pump Metrics

### **目标灵敏度 (A/°)** — 最大可接受电荷泵灵敏度 `1e-9`（默认）| 实正标量

最大可接受电荷泵灵敏度，指定为以 A/° 为单位的实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'TgtSensitivity')`
  查看**目标灵敏度**的当前值。
- 使用
  `set_param(gcb,'TgtSensitivity',value)`
  将**目标灵敏度**设置为特定值。

**数据类型：** `double`

### **目标相位偏移 (°)** — 电荷泵输出端最大可接受相位偏移 `10`（默认）| 实正标量

电荷泵输出端的最大可接受相位偏移，指定为以度为单位的实正标量。

#### 程序化使用

- 使用 `get_param(gcb,'TgtOffset')` 查看**目标相位偏移**的当前值。
- 使用 `set_param(gcb,'TgtOffset',value)`
  将**目标相位偏移**设置为特定值。

**数据类型：** `double`

### **目标杂散电流 (A)** — 电荷泵输出电流幅度 `1e-7`（默认）

电荷泵在参考频率处的输出电流幅度。

#### 程序化使用

- 使用 `get_param(gcb,'TgtSpurCurrent')`
  查看**目标杂散电流**的当前值。
- 使用
  `set_param(gcb,'TgtSpurCurrent',value)`
  将**目标杂散电流**设置为特定值。

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

用于鉴相器/鉴频器和电荷泵的通用测试环境

PFD and Charge Pump Testbench 模块评估 PFD 和电荷泵的行为模型。单个激励发生器确定 PFD 是工作在相位偏移模式还是频率偏移模式。

PFD and Charge Pump Testbench 模块从**激励**选项卡生成激励以驱动被测设备（DUT）。用于验证 DUT 的设置参数在**设置**选项卡中定义，目标验证指标在**目标指标**选项卡中定义。

该测试平台测量 PFD 性能指标，如死区、线性范围和时序损伤。它还测量电荷泵性能指标，如灵敏度、相位偏移和杂散电流。
