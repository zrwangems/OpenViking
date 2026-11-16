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

### **Port\_1** — 输入信号矩阵 | 1-D 向量

- 矩阵输入 –– 输入的每一列被视为一个独立通道。
- 1-D 向量输入 –– 输入被视为单个通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号矩阵

Weighting Filter 模块输出的信号与输入信号具有相同的数据类型。输出的大小取决于输入的大小：

- 矩阵输入 –– 模块输出与输入信号大小和数据类型相同的矩阵。
- 1-D 向量输入 –– 模块输出 *N*×1 矩阵（列向量），其中 *N* 是 1-D 向量中的元素数。

**数据类型：** `single` | `double`

## 参数

如果参数被列为可调，则可以在仿真期间更改其值。

### **加权方法** — 频率加权的类型 `A-weighting` (默认) | `C-weighting` | `K-weighting`

有关加权曲线的定义，请参阅 A-Weighting、C-Weighting 和 K-Weighting。

**可调：** No

### **从输入继承采样率** — 指定输入采样率的来源 `off` (默认) | `on`

选择此参数时，模块从输入信号继承其采样率。清除此参数时，请在 **输入采样率 (Hz)** 中指定采样率。

**可调：** No

### **输入采样率 (Hz)** — 输入的采样率 `44100` (默认) | `positive scalar`

**可调：** Yes

#### 依赖关系

要启用此参数，请清除 **从输入继承采样率** 参数。

### **仿真方式** — 指定要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

- `Code generation` –– 使用生成的 C 代码对模型进行仿真。第一次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 更快。
- `Interpreted execution` –– 使用 MATLAB® 解释器对模型进行仿真。此选项可缩短启动时间，但与 `Code generation` 相比仿真速度较慢。在此模式下，您可以调试模块的源代码。

**可调：** No

### **衰减限值掩模** — 创建用于滤波器响应可视化的掩模 `No mask` (默认) | `Class 1` | `Class 2`

掩模衰减限值在 IEC 61672-1:2002 标准中定义。

- 如果掩模为绿色，则设计合规。
- 如果掩模为红色，则设计不合规。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **加权方法** 设置为 `A-weighting` 或 `C-weighting`。

### **可视化滤波器响应** — 打开绘图以可视化幅度响应和合规掩模按钮

使用 2048 点 FFT 计算幅度响应。

**可调：** Yes

### **变量名称** — 导出滤波器的变量名称 `myFilt` (默认) | 有效的变量名称

导出时，基本工作区中用于包含该滤波器的变量名称。该名称必须是有效的 MATLAB 变量名称。

### **如果变量已存在则覆盖变量** — 如果变量已存在则覆盖变量 `on` (默认) | `off`

选择此参数时，如果 **变量名称** 参数指定的变量已在基本工作区中存在，则导出滤波器会覆盖该变量。如果未选择此参数，且指定的变量已在工作区中存在，则导出滤波器会创建一个新变量，并在变量名称后追加下划线和数字。例如，如果变量名称为 `var` 且已存在，则导出的变量将命名为 `var_1`。

### **将滤波器导出到工作区** — 将滤波器导出到工作区按钮

将滤波器导出到基本工作区中 **变量名称** 参数指定的变量。

#### 提示

如果已启用 **从输入继承采样率** 参数且模型未运行，则无法导出滤波器。

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

Weighting Filter 模块对每个输入通道独立执行频率加权滤波。
