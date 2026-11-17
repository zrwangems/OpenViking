---
type: simulink-block
title: 'PFD and Charge Pump Testbench'
family: 'pll'
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

向 PFD 提供参考频率，以确定相位误差。

**数据类型：** `double`

### **to PFD feedback** — 向 PFD 提供反馈频率标量

向 PFD 模块提供反馈频率。

**数据类型：** `double`

## 参数

### 激励

### **相位扫描 (°)** — 距相位偏移的最大相位偏移量 `300` (默认) | 实正标量

距相位偏移的最大相位偏移量，指定为以度为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'PhaseSweep')` 查看 **相位扫描** 的当前值。
- 使用 `set_param(gcb,'PhaseSweep',value)` 将 **相位扫描** 设置为特定值。

**数据类型：** `double`

### **相位偏移 (°)** — 相位扫描中心处的相对相位值 `0` (默认) | 实数标量

相位扫描中心处的相对相位值，指定为以度为单位的实数标量。

#### 编程用法

- 使用 `get_param(gcb,'PhaseOffset')` 查看 **相位偏移** 的当前值。
- 使用 `set_param(gcb,'PhaseOffset',value)` 将 **相位偏移** 设置为特定值。

**数据类型：** `double`

### **时钟频率 (Hz)** — 期望的参考时钟频率 `2.5e9 Hz` (默认) | 实正标量

参考计数器输出的所需时钟频率，指定为以 Hz 为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'ClockFrequency')` 查看 **时钟频率** 的当前值。
- 使用 `set_param(gcb,'ClockFrequency',value)` 将 **时钟频率** 设置为特定值。

**数据类型：** `double`

### **扫描中的相位数** — 要仿真的等间隔相位偏移总数 `2000` (默认) | 实正标量

相位偏移扫描中等间隔相位偏移的数量，指定为实正标量。

#### 编程用法

- 使用 `get_param(gcb,'NPhases')` 查看 **扫描中的相位数** 的当前值。
- 使用 `set_param(gcb,'NPhases',value)` 将 **扫描中的相位数** 设置为特定值。

**数据类型：** `double`

### **占空比 (%)** — 激励时钟的占空比 `50` (默认) | 实正标量

参考端口和反馈端口处激励时钟的占空比，指定为实正标量。

#### 编程用法

- 使用 `get_param(gcb,'DutyCycle')` 查看 **占空比** 的当前值。
- 使用 `set_param(gcb,'NPhases',value)` 将 **占空比** 设置为特定值。

**数据类型：** `double`

### 设置

### **仿真后将图窗置于顶层** — 仿真后将图窗置于顶层 on (默认) | off

选择以在仿真后将图窗置于所有其他窗口的顶层。默认情况下，此选项处于选中状态。

### **报告 PFD 指标** — 报告 PFD 指标 on (默认) | off

选择以在 PFD and Charge Pump Testbench 的图标上显示 PFD 指标（死区、线性范围和传播延迟）。默认情况下，此选项处于选中状态。

**数据类型：** `double`

### **报告 Charge Pump 指标** — 报告 Charge Pump 指标 on (默认) | off

选择以在 PFD and Charge Pump Testbench 的图标上显示 Charge Pump 指标（灵敏度、相位偏移和杂散电流）。默认情况下，此选项处于选中状态。

**数据类型：** `double`

### **逻辑阈值 (V)** — 电荷泵输入端的开关阈值 `0.5` (默认) | 实数标量

电荷泵输入端的开关阈值，指定为以 V 为单位的实数标量。它是在其中测量上升沿和下降沿时序的电压。

#### 编程用法

- 使用 `get_param(gcb,'VSwitch')` 查看 **逻辑阈值** 的当前值。
- 使用 `set_param(gcb,'VSwitch',value)` 将 **逻辑阈值** 设置为特定值。

**数据类型：** `double`

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小 off (默认) | on

选择以在仿真期间启用增大的缓冲区大小。这会增大 PFD and Charge Pump Testbench 内 Variable Pulse Delay 和 Logic Decision 模块的缓冲区大小。默认情况下，此选项处于未选中状态。

### **缓冲区大小** — 仿真期间可用的输入缓冲的样本数 `5` (默认) | 正整数标量

仿真期间可用的输入缓冲的样本数，指定为正整数标量。这会设置 PFD and Charge Pump Testbench 内的 Variable Pulse Delay 和 Logic Decision。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在 **配置** 选项卡中选中 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看 **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **缓冲区大小** 设置为特定值。

### 目标指标

#### PFD 指标

### **目标死区 (°)** — 零相位偏移附近降低灵敏度区域的最大可接受大小 `0` (默认) | 实非负标量

零相位偏移附近降低灵敏度区域的最大可接受大小，指定为以度为单位的实非负标量。它指死区区域的大小。

#### 编程用法

- 使用 `get_param(gcb,'TgtDeadband')` 查看 **目标死区** 的当前值。
- 使用 `set_param(gcb,'TgtDeadband',value)` 将 **目标死区** 设置为特定值。

**数据类型：** `double`

### **目标线性范围 (°)** — 输出保持近似等于输入偏移的最大相位偏移 `290` (默认) | 实正标量

输出保持近似等于输入偏移的最大相位偏移，指定为以度为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'TgtRange')` 查看 **目标线性范围** 的当前值。
- 使用 `set_param(gcb,'TgtRange',value)` 将 **目标线性范围** 设置为特定值。

**数据类型：** `double`

### **目标传播延迟 (s)** — 从输入到输出的最大可接受延迟 `60e-12` (默认) | 实正标量

从输入到输出的最大可接受延迟，指定为以 s 为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'TgtPropDelay')` 查看 **目标传播延迟** 的当前值。
- 使用 `set_param(gcb,'TgtPropDelay',value)` 将 **目标传播延迟** 设置为特定值。

**数据类型：** `double`

### **目标上升/下降时间 (s)** — 最大可接受的 20% – 80% 上升/下降时间 `30e-12` (默认) | 实正标量

最大可接受的 20% – 80% 上升/下降时间，指定为以 s 为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'TgtRiseFall')` 查看 **目标上升/下降时间** 的当前值。
- 使用 `set_param(gcb,'TgtRiseFall',value)` 将 **目标上升/下降时间** 设置为特定值。

**数据类型：** `double`

#### Charge Pump 指标

### **目标灵敏度 (A/°)** — 最大可接受电荷泵灵敏度 `1e-9` (默认) | 实正标量

最大可接受电荷泵灵敏度，指定为以 A/° 为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'TgtSensitivity')` 查看 **目标灵敏度** 的当前值。
- 使用 `set_param(gcb,'TgtSensitivity',value)` 将 **目标灵敏度** 设置为特定值。

**数据类型：** `double`

### **目标相位偏移 (°)** — 电荷泵输出处的最大可接受相位偏移 `10` (默认) | 实正标量

电荷泵输出处的最大可接受相位偏移，指定为以度为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'TgtOffset')` 查看 **目标相位偏移** 的当前值。
- 使用 `set_param(gcb,'TgtOffset',value)` 将 **目标相位偏移** 设置为特定值。

**数据类型：** `double`

### **目标杂散电流 (A)** — 电荷泵输出电流幅度 `1e-7` (默认)

参考频率下电荷泵输出电流的幅度。

#### 编程用法

- 使用 `get_param(gcb,'TgtSpurCurrent')` 查看 **目标杂散电流** 的当前值。
- 使用 `set_param(gcb,'TgtSpurCurrent',value)` 将 **目标杂散电流** 设置为特定值。

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

用于相位/频率检测器和电荷泵的通用测试环境

PFD and Charge Pump Testbench 模块评估 PFD 和电荷泵的行为模型。单个激励生成器确定 PFD 是工作在相位偏移模式还是频率偏移模式。

PFD and Charge Pump Testbench 模块从 **激励** 选项卡生成用于驱动被测设备 (DUT) 的激励。用于验证 DUT 的设置参数在 **设置** 选项卡中定义，目标验证指标在 **目标指标** 选项卡中定义。

该测试平台测量 PFD 性能指标，例如死区、线性范围和时序损伤。它还测量电荷泵性能指标，例如灵敏度、相位偏移和杂散电流。
