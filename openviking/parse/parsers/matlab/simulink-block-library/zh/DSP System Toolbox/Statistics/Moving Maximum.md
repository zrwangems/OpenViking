---
type: simulink-block
title: 'Moving Maximum'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'movingmaximum'
documentation_source_path: 'ref/movingmaximum.html'
language: zh-CN
chinese_source: worker-translation
---

# Moving Maximum

## 端口
```yaml
ports:
- name: Port_1
  summary: 数据输入 列向量 | 行向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 移动最大值输出 列向量 | 行向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 数据输入 列向量 | 行向量 | 矩阵

使用滑动窗口方法确定移动最大值的数据。该模块接受实值或复值多通道输入，即
*m*×*n* 大小的输入，其中
*m* ≥ 1 且 *n* ≥ 1。该模块还接受可变大小输入。在仿真期间，您可以更改每个输入通道的大小。但是，通道数不能更改。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Port\_1** — 移动最大值输出 列向量 | 行向量 | 矩阵

使用滑动窗口方法确定的移动最大值输出。输出的大小与输入的大小匹配。窗口沿每个通道按列滑动，模块确定窗口中数据的最大值。有关更多详细信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Specify window length
  summary: 用于指定窗口长度的标志 开（默认） | 关
  group: ''
- name: Window length
  summary: 滑动窗口的长度 4（默认） | 正标量整数
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认） | Code generation
  group: ''
```

### **Specify window length** — 用于指定窗口长度的标志 开（默认） | 关

当您选中此复选框时，滑动窗口的长度等于您通过 **Window length** 参数指定的值。当您清除此复选框时，滑动窗口的长度为无限大。在此模式下，模块确定当前样本和通道中所有先前样本的最大值。

### **Window length** — 滑动窗口的长度 4（默认） | 正标量整数

**Window length** 指定滑动窗口的长度（以样本为单位）。

#### 依赖关系

此参数在您选中 **Specify window length** 复选框时显示。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：**Simulate using** 参数默认值的更改

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

移动最大值

Moving Maximum 模块随时间独立地确定输入信号沿每个通道的移动最大值。该模块使用滑动窗口方法确定移动最大值。在此方法中，指定长度的窗口逐个样本地在每个通道上移动，模块确定窗口中数据的最大值。有关更多详细信息，请参阅算法。
