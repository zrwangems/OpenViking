---
type: simulink-block
title: 'DSBSC AM Modulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'dsbscammodulatorpassband'
documentation_source_path: 'ref/dsbscammodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# DSBSC AM Modulator Passband

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量
  direction: input
  data_types: double
- name: Out
  summary: 输出信号 标量
  direction: output
  data_types: double
```

### 输入

### **In** — 输入信号 标量

输入信号，指定为标量。

该端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 输出信号 标量

输出信号，以标量形式返回。输出是调制信号的通带表示。

该端口在模块上未命名。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Carrier frequency (Hz)
  summary: 载波频率，以 Hz 为单位 300（默认）| 正标量
  group: ''
- name: Initial phase (rad)
  summary: 初始相位偏移，以弧度为单位 0（默认）| 标量
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Carrier frequency (Hz)** — 载波频率，以 Hz 为单位 `300`（默认）| 正标量

载波频率，以 Hz 为单位，指定为正标量。

通常，合适的载波频率远高于输入信号的最高频率。根据奈奎斯特采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带与通带仿真。

### **Initial phase (rad)** — 初始相位偏移，以弧度为单位 `0`（默认）| 标量

载波的初始相位偏移，以弧度为单位，指定为标量。
## 所属库

Communications Toolbox / Modulation / Analog Passband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用双边带抑制载波幅度调制进行调制

DSBSC AM Modulator Passband 模块使用双边带抑制载波幅度调制对信号进行调制。输入和输出信号均为实标量信号。
