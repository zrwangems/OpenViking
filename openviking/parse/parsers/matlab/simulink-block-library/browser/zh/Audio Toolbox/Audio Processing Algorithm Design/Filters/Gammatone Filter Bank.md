---
type: simulink-block
title: 'Gammatone Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Filters'
documentation_page: 'gammatonefilterbank'
documentation_source_path: 'ref/gammatonefilterbank.html'
language: zh-CN
chinese_source: worker-translation
---

# Gammatone Filter Bank

## 端口

### 输入

### **Port\_1** — 滤波器组的音频输入 标量 | 向量 | 矩阵

滤波器组的音频输入，指定为标量、向量或矩阵。如果将输入指定为矩阵，模块将各列视为独立的音频通道。如果将输入指定为向量，模块将输入视为包含单个通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 滤波器组的音频输出 标量 | 向量 | 矩阵 | 三维数组

滤波器组的音频输出，以标量、向量、矩阵或三维数组形式返回。输出信号的形状取决于输入信号的形状和 **滤波器数量**。如果输入是 *M*×*N* 矩阵，则输出是 *M*×滤波器数量×*N* 数组。如果 *N* 为 `1`，则输出是矩阵。

**数据类型：** `single` | `double`

## 参数

### **频率范围 (Hz)** — 滤波器组的频率范围 `[50 8000]`（默认） | 单调递增值的二元素行向量

滤波器组的频率范围，指定为以 Hz 为单位的单调递增值的二元素行向量。

**可调：** No

### **滤波器数量** — 滤波器数量 `32`（默认） | 正整数

滤波器组中滤波器的数量，指定为正整数。

**可调：** No

### **从输入继承采样率** — 从输入端口指定采样率 `off`（默认） | `on`

选择此参数以从输入端口指定采样率。

### **输入采样率 (Hz)** — 输入采样率 `16000`（默认） | 正整数

输入采样率，指定为以 Hz 为单位的正整数。

**可调：** No

#### 依赖关系

要启用此参数，请将 **从输入端口继承采样率** 设置为 `off`。

### **频带作为单独输出端口** — 每个滤波器输出使用单独端口 `off`（默认） | `on`

选择此参数可为每个滤波器输出使用单独端口。

**可调：** No

### **查看滤波器响应** — 可视化滤波器组响应 按钮

此按钮可视化 gammatone 滤波器组响应。

### **变量名** — 导出的滤波器组的变量名 `myFilt`（默认） | 有效变量名

基础工作区中用于在导出时包含滤波器组的变量名称。该名称必须是有效的 MATLAB® 变量名。

### **如果变量已存在则覆盖** — 如果变量已存在则覆盖 `on`（默认） | `off`

选中此参数时，导出滤波器组会覆盖 **变量名** 参数指定的变量（如果该变量已存在于基础工作区中）。如果未选中此参数，并且指定的变量已存在于工作区中，则导出滤波器组会创建一个新变量，并在变量名后附加下划线和数字。例如，如果变量名为 `var` 且已存在，则导出的变量将命名为 `var_1`。

### **将滤波器导出到工作区** — 将滤波器组导出到工作区 按钮

将滤波器组导出到基础工作区，并存储在 **变量名** 参数指定的变量中。

#### 提示

如果已启用 **从输入继承采样率** 参数且模型未运行，则无法导出滤波器。

### **仿真使用** — 指定要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

要运行的仿真类型，指定为以下之一：

- `Interpreted execution` –– 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，可以调试模块的源代码。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会复用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution`。

**可调：** No

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

**在 R2021b 中引入**

## 描述

Gammatone 滤波器组

Gammatone Filter Bank 模块通过将信号传递通过一组在等效矩形带宽 (ERB) 刻度上等间隔分布的 gammatone 滤波器来分解信号。Gammatone 滤波器组旨在模拟人类听觉系统。
