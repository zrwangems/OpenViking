---
type: simulink-block
title: 'Weighting Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'weightingfilter'
documentation_source_path: 'ref/weightingfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Weighting Filter

## 端口

### 输入

### **Port\_1** — 输入信号矩阵 | 一维向量

- 矩阵输入 –– 输入的每一列被视为一个独立通道。
- 一维向量输入 –– 输入被视为单通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号矩阵

Weighting Filter 模块输出的信号与输入信号具有相同的数据类型。输出的大小取决于输入的大小：

- 矩阵输入 –– 模块输出与输入信号大小和数据类型相同的矩阵。
- 一维向量输入 –– 模块输出 *N*×1 矩阵（列向量），其中 *N* 是一维向量中的元素个数。

**数据类型：** `single` | `double`

## 参数

如果参数被列为可调，则可以在仿真期间更改其值。

### **Weighting method** — 频率加权的类型 `A-weighting`（默认）| `C-weighting` | `K-weighting`

有关加权曲线的定义，请参阅 A-Weighting、C-Weighting 和 K-Weighting。

**可调：** 否

### **Inherit sample rate from input** — 指定输入采样率的来源 `off`（默认）| `on`

选中此参数时，模块从输入信号继承其采样率。清除此参数时，需在 **Input sample rate (Hz)** 中指定采样率。

**可调：** 否

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认）| `positive scalar`

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不发生变化，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution`。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。

**可调：** 否

### **Mask for attenuation limits** — 为滤波器响应可视化创建掩膜 `No mask`（默认）| `Class 1` | `Class 2`

掩膜衰减限值在 IEC 61672-1:2002 标准中定义。

- 如果掩膜为绿色，则设计符合要求。
- 如果掩膜为红色，则设计不符合要求。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Weighting method** 设置为 `A-weighting` 或 `C-weighting`。

### **Visualize filter response** — 打开绘图以可视化幅值响应和合规掩膜 按钮

使用 2048 点 FFT 计算幅值响应。

**可调：** 是

### **Variable name** — 导出滤波器的变量名 `myFilt`（默认）| 有效变量名

导出时，基础工作区中用于存放滤波器的变量名称。该名称必须是有效的 MATLAB 变量名。

### **Overwrite variable if it already exists** — 如果变量已存在则覆盖 `on`（默认）| `off`

选中此参数时，如果 **Variable name** 参数指定的变量已存在于基础工作区中，则导出滤波器会覆盖该变量。如果未选中此参数且指定的变量已存在于工作区中，则导出滤波器会创建一个新变量，在变量名后附加下划线和数字。例如，如果变量名为 `var` 且已存在，则导出的变量将命名为 `var_1`。

### **Export filter to workspace** — 将滤波器导出到工作区 按钮

将滤波器导出到基础工作区中由 **Variable name** 参数指定的变量中。

#### 提示

如果启用了 **Inherit sample rate from input** 参数且模型未运行，则无法导出滤波器。

## 所属库

Audio Toolbox / Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

加权频率响应滤波器

Weighting Filter 模块在每个输入通道上独立执行频率加权滤波。
