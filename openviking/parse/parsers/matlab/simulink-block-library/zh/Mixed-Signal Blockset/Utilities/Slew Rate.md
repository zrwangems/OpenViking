---
type: simulink-block
title: 'Slew Rate'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'slewrate'
documentation_source_path: 'ref/slewrate.html'
language: zh-CN
chinese_source: worker-translation
---

# Slew Rate

## 端口
```yaml
ports:
- name: events
  summary: 输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
- name: wave
  summary: 输出信号 标量
  direction: output
  data_types: double
```

### 输入

### **events** — 输入信号 标量

可变步长、事件驱动的输入信号，指定为标量。**events** 端口处的信号来自逻辑门（例如 Variable Pulse Delay 模块）的输出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **wave** — 输出信号 标量

固定步长、均匀采样的输出信号，以标量形式返回。您可以为 **wave** 端口处的信号定义有限压摆率和传播延迟。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Output step size calculation
  summary: 定义如何计算输出步长 Default（默认）| Advanced
  group: ''
- name: Maximum frequency of interest (Hz)
  summary: 输出端的最大关注频率 11e9（默认）| 标量
  group: ''
- name: Output sample interval
  summary: 输出采样间隔 23ps（默认）| 标量
  group: ''
- name: Minimum 20%-80% rise/fall time
  summary: 输出端进行有意义仿真所需的最小上升/下降时间 23ps（默认）| 标量
  group: ''
- name: Rise/fall time (s)
  summary: 输出端的 20%-80% 上升时间 30e-12（默认）| 标量
  group: ''
- name: Slew rate for 20%-80% edge of unit amplitude signal
  summary: 输出端 20%-80% 边沿的压摆率 56GHz（默认）| 标量
  group: ''
- name: Minimum propagation delay
  summary: 用于有效仿真的最小传播延迟 48ps（默认）| 标量
  group: ''
- name: Propagation delay (s)
  summary: 上升沿的传播延迟 48e-12（默认）| 标量
  group: ''
- name: Enable increased buffer size
  summary: 启用增大缓冲区大小按钮
  group: ''
- name: Buffer size
  summary: 模块的缓冲区大小 10（默认）| 正整数标量
  group: ''
```

### **Output step size calculation** — 定义如何计算输出步长 `Default`（默认）| `Advanced`

定义如何计算输出步长。

- 选择 `Default` 以基于上升/下降时间计算 **Output step size calculation**。**Output sample interval**（ΔT）由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以基于关注频率计算 **Output step size calculation**。**Output sample interval**（ΔT）由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 程序化使用

- 使用 `get_param(gcb,'DefaultOrAdvanced')` 确定如何计算输出步长。

### **Maximum frequency of interest (Hz)** — 输出端的最大关注频率 `11e9`（默认）| 标量

输出端的最大关注频率，以 Hz 为单位的标量指定。**Maximum frequency of interest** 用于计算 **Output sample interval** 和 **Minimum 20%-80% rise/fall time**。

#### 依赖关系

此参数仅在 **Output step size calculation** 选择 `Advanced` 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **Maximum frequency of interest** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **Maximum frequency of interest** 设置为特定值。

### **Output sample interval** — 输出采样间隔 `23ps`（默认）| 标量

输出采样间隔，以 s 为单位的标量指定。此参数不可调。

**Output sample interval**（ΔT）由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

此参数仅在 **Output step size calculation** 选择 `Advanced` 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'OutputSampleTime')` 查看 **Output sample interval** 的当前值。
- 使用 `set_param(gcb,'OutputSampleTime',value)` 将 **Output sample interval** 设置为特定值。

### **Minimum 20%-80% rise/fall time** — 输出端进行有意义仿真所需的最小上升/下降时间 23ps（默认）| 标量

输出端进行有意义仿真所需的最小上升/下降时间，以 ps 为单位的标量指定。这是一个不可调参数。

#### 依赖关系

此参数仅在 **Output step size calculation** 选择 `Advanced` 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'ConversionRiseFall')` 查看 **Minimum 20%-80% rise/fall time** 的当前值。
- 使用 `set_param(gcb,'ConversionRiseFall',value)` 将 **Minimum 20%-80% rise/fall time** 设置为特定值。

### **Rise/fall time (s)** — 输出端的 20%-80% 上升时间 `30e-12`（默认）| 标量

在输出端全幅度边沿中，信号从 20% 变化到 80% 所需的时间，以标量指定。

#### 程序化使用

- 使用 `get_param(gcb,'RiseTime')` 查看 **Rise/fall time** 的当前值。
- 使用 `set_param(gcb,'RiseTime',value)` 将 **Rise/fall time** 设置为特定值。

### **Slew rate for 20%-80% edge of unit amplitude signal** — 输出端 20%-80% 边沿的压摆率 `56GHz`（默认）| 标量

输出端 20%-80% 边沿的压摆率，以标量指定。此参数不可调。

#### 程序化使用

- 使用 `get_param(gcb,'RisingSlewRate')` 查看 **Slew rate for 20%-80% edge of unit amplitude signal** 的当前值。
- 使用 `set_param(gcb,'RisingSlewRate',value)` 将 **Slew rate for 20%-80% edge of unit amplitude signal** 设置为特定值。

### **Minimum propagation delay** — 用于有效仿真的最小传播延迟 `48ps`（默认）| 标量

用于有效仿真的最小传播延迟，指定为标量。此参数不可调。

最小传播延迟根据 **Maximum frequency of interest** 计算，其中最小传播延迟 =0.269最大关注频率。

#### 程序化使用

- 使用 `get_param(gcb,'ConversionDelay')` 查看 **Minimum propagation delay** 的当前值。
- 使用 `set_param(gcb,'ConversionDelay',value)` 将 **Minimum propagation delay** 设置为特定值。

### **Propagation delay (s)** — 上升沿的传播延迟 `48e-12`（默认）| 标量

上升沿的传播延迟，以 s 为单位指定为标量。**Propagation delay** 在等于幅度一半的阈值处测量。

#### 程序化使用

- 使用 `get_param(gcb,'RisepropDelay')` 查看 **Propagation delay** 的当前值。
- 使用 `set_param(gcb,'RisePropDelay',value)` 将 **Propagation delay** 设置为特定值。

### **Enable increased buffer size** — 启用增大缓冲区大小按钮

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 PLL 模型中属于 Mixed-Signal Blockset™/Utilities Simulink® 库的所有模块的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 模块的缓冲区大小 `10`（默认）| 正整数标量

PLL 模型中属于 Mixed-Signal Blockset/Utilities Simulink 库的所有模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数量。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

此参数仅在选中 **Enable increased buffer size** 选项时可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBuffer')` 查看 **Buffer size** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **Buffer size** 设置为特定值。
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对逻辑门的幅度、上升和下降时间以及传播延迟进行建模

Slew Rate 模块将逻辑信号转换为具有用户定义的有限压摆率和传播延迟的信号。
