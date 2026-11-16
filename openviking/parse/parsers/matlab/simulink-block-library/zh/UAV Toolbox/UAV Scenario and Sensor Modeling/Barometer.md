---
type: simulink-block
title: 'Barometer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'barometer'
documentation_source_path: 'ref/barometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Barometer

## 端口

### 输入

### **True pressure** — 真实气压标量 | 向量

真实气压，单位为 Pa，指定为标量或 *N* 元向量，其中 *N* 是气压测量值的数量。

**数据类型：** `single` | `double`
### 输出

### **Measured pressure** — 测量气压标量 | 向量

测量气压，单位为 Pa，以非负标量或 *N* 元向量形式返回。Measured pressure 的长度与 True pressure 的长度匹配。

**数据类型：** `single` | `double`

## 参数

### **Constant bias** — 恒定测量偏差 0（默认）| 有限标量

将恒定测量偏差指定为有限标量，单位为 Pa。

### **Noise density** — 白噪声标准方差 1（默认）| 非负有限标量

将白噪声标准方差指定为非负有限标量。此参数指定传感器噪声的功率谱密度，单位为 Pa/√Hz。

### **Bias instability** — 相关噪声标准方差 1（默认）| 非负有限标量

将相关噪声标准方差指定为非负有限标量，单位为 Pa

### **Decay factor** — 相关噪声衰减因子 0.99（默认）| 范围 (0,1) 内的正标量

将相关噪声衰减因子指定为范围 (0, 1) 内的标量。

指定较小的衰减因子会将相关噪声建模为更接近白噪声，而指定较大的衰减因子会将相关噪声建模为更接近随机游走过程。

### **Seed** — 随机数初始种子 `67`（默认）| 非负整数标量

将 mt19937ar 随机数生成器算法的初始种子指定为实数非负整数标量。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅解释执行与代码生成 (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。

## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

带噪声的气压计传感器模型

Barometer 模块对气压计传感器进行建模，该传感器生成带有测量噪声的气压读数，测量噪声由恒定测量偏差、不相关白噪声和相关噪声组成 [1]。有关噪声模型的详细信息，请参阅噪声模型。
