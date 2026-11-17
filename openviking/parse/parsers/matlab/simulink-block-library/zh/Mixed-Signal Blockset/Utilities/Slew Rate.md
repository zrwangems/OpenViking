---
type: simulink-block
title: 'Slew Rate'
family: 'utilities'
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

### 输入

### **events** — 输入信号标量

可变步长、事件驱动的输入信号，指定为标量。**events** 端口处的信号来自逻辑门的输出，例如 Variable Pulse Delay 模块。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

### 输出

### **wave** — 输出信号标量

固定步长、均匀采样的输出信号，以标量形式返回。您可以为 **wave** 端口处的信号定义有限压摆率和传播延迟。

**数据类型：** `double`

## 参数

### **输出步长计算** — 定义如何计算输出步长 `Default`（默认） | `Advanced`

定义如何计算输出步长。

- 选择 `Default` 可基于上升/下降时间计算 **输出步长计算**。**输出采样间隔** (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 可基于感兴趣频率计算 **输出步长计算**。**输出采样间隔** (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 编程用法

- 使用 `get_param(gcb,'DefaultOrAdvanced')` 确定输出步长的计算方式。

### **感兴趣的最大频率 (Hz)** — 输出端感兴趣的最大频率 `11e9`（默认） | scalar

输出端感兴趣的最大频率，指定为以 Hz 为单位的标量。**感兴趣的最大频率** 用于计算 **输出采样间隔** 和 **最小 20%-80% 上升/下降时间**。

#### 依赖项

仅当为 **输出步长计算** 选择 `Advanced` 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **感兴趣的最大频率** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **感兴趣的最大频率** 设置为特定值。

### **输出采样间隔** — 输出采样间隔 `23ps`（默认） | scalar

输出采样间隔，指定为以 s 为单位的标量。此参数不可调。

**输出采样间隔** (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖项

仅当为 **输出步长计算** 选择 `Advanced` 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'OutputSampleTime')` 查看 **输出采样间隔** 的当前值。
- 使用 `set_param(gcb,'OutputSampleTime',value)` 将 **输出采样间隔** 设置为特定值。

### **最小 20%-80% 上升/下降时间** — 输出端进行有意义仿真所需的最小上升/下降时间 23ps（默认） | scalar

输出端进行有意义仿真所需的最小上升/下降时间，指定为以 ps 为单位的标量。这是一个不可调参数。

#### 依赖项

仅当为 **输出步长计算** 选择 `Advanced` 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'ConversionRiseFall')` 查看 **最小 20%-80% 上升/下降时间** 的当前值。
- 使用 `set_param(gcb,'ConversionRiseFall',value)` 将 **最小 20%-80% 上升/下降时间** 设置为特定值。

### **上升/下降时间 (s)** — 输出端 20%-80% 上升时间 `30e-12`（默认） | scalar

在输出端完整幅度边沿中，信号从 20% 变化到 80% 所需的时间，指定为标量。

#### 编程用法

- 使用 `get_param(gcb,'RiseTime')` 查看 **上升/下降时间** 的当前值。
- 使用 `set_param(gcb,'RiseTime',value)` 将 **上升/下降时间** 设置为特定值。

### **单位幅度信号 20%-80% 边沿的压摆率** — 输出端 20%-80% 边沿的压摆率 `56GHz`（默认） | scalar

输出端 20%-80% 边沿的压摆率，指定为标量。此参数不可调。

#### 编程用法

- 使用 `get_param(gcb,'RisingSlewRate')` 查看 **单位幅度信号 20%-80% 边沿的压摆率** 的当前值。
- 使用 `set_param(gcb,'RisingSlewRate',value)` 将 **单位幅度信号 20%-80% 边沿的压摆率** 设置为特定值。

### **最小传播延迟** — 进行有意义仿真所需的最小传播延迟 `48ps`（默认） | scalar

进行有意义仿真所需的最小传播延迟，指定为标量。此参数不可调。

最小传播延迟根据 **感兴趣的最大频率** 计算，其中 Minimum propagation delay =0.269Maximum frequency of interest。

#### 编程用法

- 使用 `get_param(gcb,'ConversionDelay')` 查看 **最小传播延迟** 的当前值。
- 使用 `set_param(gcb,'ConversionDelay',value)` 将 **最小传播延迟** 设置为特定值。

### **传播延迟 (s)** — 上升沿的传播延迟 `48e-12`（默认） | scalar

上升沿的传播延迟，指定为以 s 为单位的标量。**传播延迟** 在等于幅度一半的阈值处测量。

#### 编程用法

- 使用 `get_param(gcb,'RisepropDelay')` 查看 **传播延迟** 的当前值。
- 使用 `set_param(gcb,'RisePropDelay',value)` 将 **传播延迟** 设置为特定值。

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小按钮

选择以在仿真期间启用增大的缓冲区大小。这会增大 PLL 模型中属于 Mixed-Signal Blockset™/Utilities Simulink® 库的所有模块的缓冲区大小。默认情况下，此选项处于未选中状态。

### **缓冲区大小** — 模块的缓冲区大小 `10`（默认） | positive integer scaler

PLL 模型中属于 Mixed-Signal Blockset/Utilities Simulink 库的所有模块的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖项

仅当选中 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看 **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **缓冲区大小** 设置为特定值。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对逻辑门的幅度、上升和下降时间以及传播延迟进行建模

Slew Rate 模块将逻辑信号转换为具有用户定义的有限压摆率和传播延迟的信号。
