---
type: simulink-block
title: 'Shelving Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'shelvingfilterblock'
documentation_source_path: 'ref/shelvingfilterblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Shelving Filter

## 端口

### 输入

### **x** — 输入信号 列向量 | 矩阵

要滤波的输入信号，指定为列向量或矩阵。如果输入是矩阵，则每一列被视为一个独立通道。

**数据类型：** `single` | `double`

### **G** — 峰值增益 (dB) 实数标量

此端口指定 **Gain (dB)** 参数的值。

#### 依赖关系

要启用此端口，请选中 **Specify gain from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **S** — 斜率 正标量

此端口指定 **Slope** 参数的值。

#### 依赖关系

要启用此端口，请选中 **Specify slope from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **F** — 截止频率 非负标量

此端口指定 **Cutoff frequency (Hz)** 参数的值。

#### 依赖关系

要启用此端口，请选中 **Specify cutoff frequency from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Port\_1** — 输出信号 列向量 | 矩阵

滤波后的输出信号，以与输入信号大小和数据类型相同的列向量或矩阵形式返回。

**数据类型：** `single` | `double`

## 参数

### **Specify gain from input port** — 使用附加输入端口指定增益 `off`（默认）| `on`

选中此参数时，会向模块添加一个附加输入端口 **G**。此端口指定滤波器的增益。

### **Gain (dB)** — 峰值增益 (dB) `0`（默认）| 实数标量

滤波器的峰值增益，以 dB 为单位，指定为实数标量。增益指定滤波器将对输入信号的频谱进行提升（如果增益为正）或衰减（如果增益为负）的程度。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify gain from input port** 参数。

### **Specify slope from input port** — 使用附加输入端口指定斜率 `off`（默认）| `on`

选中此参数时，会向模块添加一个附加输入端口 **S**。此端口指定滤波器的斜率。

### **Slope** — 滤波器斜率 `1.5`（默认）| 正标量

滤波器的斜率，指定为正标量。斜率控制滤波器响应中过渡带的宽度。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify slope from input port** 参数。

### **Specify cutoff frequency from input port** — 使用附加输入端口指定截止频率 `off`（默认）| `on`

选中此参数时，会向模块添加一个附加输入端口 **F**。此端口指定滤波器的截止频率。

### **Cutoff frequency (Hz)** — 滤波器截止频率 `200`（默认）| 非负标量

滤波器的截止频率，以 Hz 为单位，指定为范围 [0,`Fs`/2] 内的非负标量，其中 `Fs` 是由 **Input sample rate (Hz)** 和 **Inherit sample rate from input** 参数指定的采样率。截止频率指定滤波器峰值增益一半处的频率，即 `G`/2 dB，其中 `G` 是峰值增益。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify cutoff frequency from input port** 参数。

### **Type** — 滤波器类型 `lowpass`（默认）| `highpass`

斜架滤波器的类型，指定为 `lowpass` 或 `highpass`。

- `lowpass` — 提升或衰减截止频率以下的频谱。
- `highpass` — 提升或衰减截止频率以上的频谱。

### **Inherit sample rate from input** — 指定输入采样率的来源 `off`（默认）| `on`

选中此参数时，模块从输入信号继承其采样率。清除此参数时，您需要在 **Input sample rate (Hz)** 中指定采样率。

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认）| 正标量

输入的采样率，指定为正标量。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Visualize filter response** — 打开绘图以可视化滤波器响应 按钮

打开绘图以可视化滤波器的幅值响应。

### **Variable name** — 导出滤波器的变量名 `myFilt`（默认）| 有效变量名

基础工作区中用于包含导出时滤波器的变量名称。该名称必须是有效的 MATLAB® 变量名。

### **Overwrite variable if it already exists** — 如果变量已存在则覆盖 `on`（默认）| `off`

选中此参数时，如果 **Variable name** 参数指定的变量已存在于基础工作区中，则导出滤波器会覆盖该变量。如果您未选中此参数且指定的变量已存在于工作区中，则导出滤波器会创建一个新变量，其名称是在变量名后附加下划线和数字。例如，如果变量名为 `var` 且已存在，则导出的变量将命名为 `var_1`。

### **Export filter to workspace** — 将滤波器导出到工作区 按钮

将滤波器导出到基础工作区中由 **Variable name** 参数指定的变量。

#### 提示

- 如果您已启用 **Inherit sample rate from input** 参数且模型未运行，则无法导出滤波器。
- 如果您从输入端口指定滤波器特性，则无法导出滤波器。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

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

**在 R2022a 中引入**

## 描述

二阶 IIR 斜架滤波器

Shelving Filter 模块对输入信号应用斜架滤波器。斜架滤波器在给定截止频率以上或以下提升或衰减输入信号的频谱。
