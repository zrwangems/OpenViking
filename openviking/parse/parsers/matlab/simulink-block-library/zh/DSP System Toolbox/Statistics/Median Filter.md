---
type: simulink-block
title: 'Median Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'medianfilter'
documentation_source_path: 'ref/medianfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Median Filter

## 端口

### 输入

### **Port\_1** — 数据输入 列向量 | 行向量 | 矩阵

模块计算移动中位数所依据的数据。该模块接受实值或复值多通道输入，即大小为 *m*×*n* 的输入，其中 *m* ≥ 1，且 *n* ≥ 1。该模块还接受可变大小输入。在仿真期间，您可以更改每个输入通道的大小。但是，通道数不能更改。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Port\_1** — 移动中位数输出 列向量 | 行向量 | 矩阵

移动中位数输出的大小与输入的大小匹配。该模块使用滑动窗口方法计算移动中位数。有关详细信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **Window length** — 滑动窗口的长度 5（默认值） | 正整数标量

**Window length** 指定滑动窗口的长度（以采样数为单位）。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认值） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真速度更快。

## 所属库

DSP System Toolbox / Filtering / Filter Designs DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：**Simulate using** 参数默认值的更改

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

中值滤波

Median Filter 模块沿每个通道随时间独立计算输入信号的移动中位数。该模块使用滑动窗口方法计算移动中位数。在此方法中，指定长度的窗口逐个样本地在每个通道上移动，模块计算窗口中数据的中位数。该模块随时间对输入数据执行中值滤波。有关详细信息，请参阅算法。
