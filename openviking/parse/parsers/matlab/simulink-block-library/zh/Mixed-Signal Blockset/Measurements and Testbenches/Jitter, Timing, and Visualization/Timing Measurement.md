---
type: simulink-block
title: 'Timing Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Measurements and Testbenches / Jitter, Timing, and Visualization'
documentation_page: 'timingmeasurement'
documentation_source_path: 'ref/timingmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Timing Measurement

## 端口

### 输入

### **reference** — 输入信号标量

正在测量其时序指标的输入信号，指定为标量。

**数据类型：** `double`

### **test** — 测试信号标量

用于测量输入信号 delay 所对照的测试信号，指定为标量。

#### 依赖项

要启用此端口，请在 **Selection** 选项卡中选择 **Delay** 作为测量选项。

**数据类型：** `double`

### 输出

### **period** — 输入信号的 period 标量

输入信号的 period，以标量形式返回。

**数据类型：** `double`

### **frequency** — 输入信号的 frequency 标量

输入信号的 frequency，以标量形式返回。

#### 依赖项

要启用此端口，请在 **Selection** 选项卡中选择 **Frequency** 作为测量选项。

**数据类型：** `double`

### **rise time** — 输入信号的 rise time 标量

输入信号的 rise time，以标量形式返回。

#### 依赖项

要启用此端口，请在 **Selection** 选项卡中选择 **Rise Time** 作为测量选项。

**数据类型：** `double`

### **fall time** — 输入信号的 fall time 标量

输入信号的 fall time，以标量形式返回。

#### 依赖项

要启用此端口，请在 **Selection** 选项卡中选择 **Fall time** 作为测量选项。

**数据类型：** `double`

### **duty cycle** — 输入信号的 duty cycle 标量

输入信号的 duty cycle，以标量形式返回。

#### 依赖项

要启用此端口，请在 **Selection** 选项卡中选择 **Duty Cycle** 作为测量选项。

**数据类型：** `double`

### **delay** — 输入信号的 delay 标量

输入信号的 delay，以标量形式返回。

#### 依赖项

要启用此端口，请在 **Selection** 选项卡中选择 **Delay** 作为测量选项。

**数据类型：** `double`

## 参数

### 选择

### **Period** — 测量输入信号的 period on（默认） | off

选择此项以测量输入信号的 period。

Period 定义为周期信号完成一个完整周期所需的时间，以 seconds 为单位指定。

### **Frequency** — 测量输入信号的 frequency off（默认） | on

选择此项以测量输入信号的 frequency。

Frequency 定义为周期信号在单位时间内完成的周期数，以 hertz 为单位指定。它是 **Period** 的倒数。

### **Rise Time** — 测量输入信号的 rise time off（默认） | on

选择此项以测量输入信号的 rise time。

Rise time 定义为信号的上升沿从其稳态值的 10% 达到 90%（或从 20% 达到 80%）所需的时间，以 seconds 为单位指定。

### **Fall Time** — 测量输入信号的 fall time off（默认） | on

选择此项以测量输入信号的 fall time。

Fall time 定义为信号的下降沿从其稳态值的 90% 下降到 10%（或从 80% 下降到 20%）所需的时间，以 seconds 为单位指定。

### **Duty Cycle** — 测量输入信号的 duty cycle off（默认） | on

选择此项以测量输入信号的 duty cycle。

Duty cycle 定义为正脉冲宽度与周期的比值，以分数形式指定。

### **Delay** — 测量输入信号的 delay off（默认） | on

选择此项以测量输入信号的 delay。

Delay 定义为目标信号相对于测试信号的阈值交叉点之间的时间差，以 seconds 为单位指定。

### 配置

### **Use same reference threshold for all measurements** — 使用相同的参考阈值测量所有 timing metrics on（默认） | off

选择此项以使用相同的参考阈值测量所有时序指标。

### **Reference threshold (V)** — 用于测量 timing metrics 的参考阈值 `0`（默认） | 标量

用于测量所有时序指标的参考阈值电压，以 volts 为单位指定为标量。

#### 依赖项

要启用此参数，请在 **Configuration** 选项卡中选择 **Use same reference threshold for all measurements**。

#### 程序化使用

- 使用 `get_param(gcb,'SameRefThreshold')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'SameRefThreshold',value)` 将 **Reference threshold (V)** 设置为特定值。

#### Period/Frequency

### **Reference threshold (V)** — 用于测量 period 和/或 frequency 的参考阈值电压 `0`（默认） | 标量

用于测量目标信号的 period 和/或 frequency 的参考阈值电压，以 volts 为单位指定为标量。

#### 依赖项

要启用此参数，请在 **Configuration** 选项卡中取消选择 **Use same reference threshold for all measurements**，并在 **Selection** 选项卡中选择 **Period** 和/或 **Frequency**。

#### 程序化使用

- 使用 `get_param(gcb,'PeriodRefThreshold')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'PeriodRefThreshold',value)` 将 **Reference threshold (V)** 设置为特定值。

#### Rise/Fall Time

### **Input range (V)** — 输入信号的峰峰值 `[-1 1]`（默认） | 2 元素行向量

输入信号的峰峰值，以 volts 为单位指定为 2 元素行向量。第一个元素定义输入信号的谷值，第二个元素定义峰值。**Input range (V)** 用于计算上限和下限阈值电平，以计算 rise/fall times。

#### 依赖项

要启用此参数，请在 **Selection** 选项卡中选择 **Rise Time** 和/或 **Fall Time**。

#### 程序化使用

- 使用 `get_param(gcb,'Range')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'Range',value)` 将 **Reference threshold (V)** 设置为特定值。

### **Type** — 用于测量 rise/fall times 的输入阈值电平 `80%/20%`（默认） | `90%/10%`

确定用于测量 rise/fall times 的输入阈值电平，指定为 `80%/20%` 或 `90%/10%`。

#### 依赖项

要启用此参数，请在 **Selection** 选项卡中选择 **Rise Time** 和/或 **Fall Time**。

#### 程序化使用

- 使用 `get_param(gcb,'MeasurementType')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'MeasurementType',value)` 将 **Reference threshold (V)** 设置为特定值。

#### Duty Cycle

### **Reference threshold (V)** — 用于测量 duty cycle 的参考阈值电压 `0`（默认） | 标量

用于测量目标信号的 duty cycle 的参考阈值电压，以 volts 为单位指定为标量。

#### 依赖项

要启用此参数，请在 **Configuration** 选项卡中取消选择 **Use same reference threshold for all measurements**，并在 **Selection** 选项卡中选择 **Duty Cycle**。

#### 程序化使用

- 使用 `get_param(gcb,'DcRefThreshold')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'DcRefThreshold',value)` 将 **Reference threshold (V)** 设置为特定值。

#### Delay

### **Reference threshold (V)** — 目标信号中用于测量 delay 的阈值电压电平 `0`（默认） | 标量

正在测量其 delay 的目标参考信号中的阈值电压电平，以 volts 为单位指定为标量。

#### 依赖项

要启用此参数，请在 **Configuration** 选项卡中取消选择 **Use same reference threshold for all measurements**，并在 **Selection** 选项卡中选择 **Delay**。

#### 程序化使用

- 使用 `get_param(gcb,'DelayRefThreshold')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'DelayRefThreshold',value)` 将 **Reference threshold (V)** 设置为特定值。

### **Test threshold (V)** — 测试信号中用于测量 delay 的阈值电压电平 `0`（默认） | 标量

测试信号中的阈值电压电平，参考信号的 delay 相对于该测试信号进行测量，以 volts 为单位指定为标量。

#### 依赖项

要启用此参数，请在 **Configuration** 选项卡中取消选择 **Use same reference threshold for all measurements**，并在 **Selection** 选项卡中选择 **Delay**。

#### 程序化使用

- 使用 `get_param(gcb,'DelayTstThreshold')` 查看 **Reference threshold (V)** 的当前值。
- 使用 `set_param(gcb,'DelayTstThreshold',value)` 将 **Reference threshold (V)** 设置为特定值。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

测量信号的 period、frequency、duty cycle、rise time、fall time 和 delay

Timing Measurement 模块测量信号的基本时序指标，例如 period、frequency、duty cycle、rise time、fall time 和 delay。
