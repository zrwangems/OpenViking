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
```yaml
ports:
- name: Port_1
  summary: 数据输入 列向量 | 行向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 滑动中位数输出 列向量 | 行向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 数据输入 列向量 | 行向量 | 矩阵

模块计算滑动中位数的数据。该模块接受实值或复值多通道输入，即
*m*×*n* 大小的输入，其中
*m* ≥ 1，*n* ≥ 1。该模块
也接受可变大小输入。在仿真期间，您可以更改
每个输入通道的大小。但是，通道数不能
更改。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Port\_1** — 滑动中位数输出 列向量 | 行向量 | 矩阵

滑动中位数输出的大小与输入的大小匹配。
该模块使用滑动窗口方法计算滑动中位数。
有关更多详细信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Window length
  summary: 滑动窗口的长度 5 （默认） | 正整数标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution （默认） | Code generation
  group: ''
```

### **Window length** — 滑动窗口的长度 5 （默认） | 正整数标量

**Window length** 指定滑动
窗口的长度（以采样数为单位）。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` （默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用
  MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会在
  后续仿真中重用。此选项
  需要额外的启动时间，但可提供更快的后续
  仿真。
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

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为
`Interpreted execution`。通过此更改，该模块默认使用
MATLAB 解释器进行仿真。

## 描述

中位数滤波器

Median Filter 模块沿每个通道独立地随时间计算输入信号的
滑动中位数。该模块使用滑动窗口方法
计算滑动中位数。在此方法中，指定长度的窗口逐个采样地移动过每个
通道，模块计算窗口中数据的中位数。
该模块对输入数据随时间执行中位数滤波。有关更多详细信息，请参阅
算法。
