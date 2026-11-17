---
type: simulink-block
title: 'Clock Jitter Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'clockjittermeasurement'
documentation_source_path: 'ref/clockjittermeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Clock Jitter Measurement

## 端口
```yaml
ports:
- name: clock
  summary: 输入时钟信号 标量
  direction: input
  data_types: double
- name: Period Jitter
  summary: 周期抖动的运行 RMS 值 标量
  direction: output
  data_types: double
- name: C2C
  summary: 周期间抖动的运行 RMS 值 标量
  direction: output
  data_types: double
- name: DCD
  summary: 实际占空比与 50% 值之间的差值 标量
  direction: output
  data_types: double
```

### 输入

### **clock** — 输入时钟信号 标量

输入时钟信号，指定为标量。输入信号在每个周期内必须只有一个阈值穿越。

**数据类型：** `double`
### 输出

### **Period Jitter** — 周期抖动的运行 RMS 值 标量

计算到当前时间步为止的周期抖动的运行 RMS 值，以标量形式返回。周期抖动是时钟信号的周期时间相对于理想周期的偏差。

**数据类型：** `double`

### **C2C** — 周期间抖动的运行 RMS 值 标量

计算到当前时间步为止的周期间抖动的运行 RMS 值，以标量形式返回。周期间抖动是时钟两个连续周期之间的周期差。

#### 依赖关系

要启用此端口，请选择 **Cycle-2-Cycle (C2C) Jitter**。

**数据类型：** `double`

### **DCD** — 实际占空比与 50% 值之间的差值 标量

实际占空比百分比与理想 50% 值之间的差值，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **Duty Cycle Distortion (DCD)**。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Clock Frequency
  summary: 输入时钟信号的频率 1e6（默认）| 正实数标量
  group: ''
  block_parameter: Frequency
  type: 字符向量
  values: 正实数标量
- name: Threshold
  summary: 阈值信号电平 0（默认）| 实数标量
  group: ''
  block_parameter: Threshold
  type: 字符向量
  values: 实数标量
- name: Period Jitter
  summary: RMS 周期抖动 开（默认）| 关
  group: ''
- name: Cycle-2-Cycle (C2C) Jitter
  summary: RMS 周期间抖动 关（默认）| 开
  group: ''
- name: Duty Cycle Distortion (DCD)
  summary: 每个周期的占空比失真 关（默认）| 开
  group: ''
- name: Simulate using
  summary: 选择仿真模式 Code generation（默认）| Interpreted execution
  group: ''
```

### **Clock Frequency** — 输入时钟信号的频率 `1e6`（默认）| 正实数标量

输入时钟信号的频率，指定为以 Hz 为单位的正实数标量。**Clock Frequency** 用于计算输入信号周期的理想值。

#### 编程使用

|  |
| --- |
| **模块参数：** `Frequency` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1e6` |

### **Threshold** — 阈值信号电平 `0`（默认）| 实数标量

用于计算信号上升沿和下降沿的阈值信号电平，指定为实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Threshold` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0` |

### **Period Jitter** — RMS 周期抖动 开（默认）| 关

选择以计算 RMS 周期抖动。默认情况下选中此选项。

周期抖动是时钟信号的周期时间相对于理想周期的偏差。

### **Cycle-2-Cycle (C2C) Jitter** — RMS 周期间抖动 关（默认）| 开

选择以计算 RMS 周期间（C2C）抖动。默认情况下取消选中此选项。

周期间抖动是时钟两个连续周期之间的周期差。

### **Duty Cycle Distortion (DCD)** — 每个周期的占空比失真 关（默认）| 开

选择以计算每个周期的占空比失真。默认情况下取消选中此选项。

占空比失真是实际占空比百分比与理想 50% 值之间的差值。

### **Simulate using** — 选择仿真模式 `Code generation`（默认）| `Interpreted execution`

选择仿真模式。此选择会影响仿真性能。

使用 `Code generation` 方法仿真模型需要额外的启动时间，但后续仿真运行更快。使用 `Interpreted execution` 方法仿真模型可能会减少启动时间，但后续仿真运行更慢。有关详细信息，请参阅 Interpreted Execution vs. Code Generation。
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

测量周期信号中的抖动

使用 Clock Jitter Measurement 模块测量时钟信号中的 RMS（均方根）周期抖动。您还可以测量周期间（C2C）抖动和占空比失真（DCD）。
