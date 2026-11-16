---
type: simulink-block
title: 'Crossover Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Filters'
documentation_page: 'crossoverfilter'
documentation_source_path: 'ref/crossoverfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Crossover Filter

## 端口

### 输入

### **x** — 输入信号矩阵 | 一维向量

- 矩阵输入 –– 输入的每一列被视为独立通道。
- 一维向量输入 –– 输入被视为单个通道。

除非指定其他输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **F1** — Crossover frequency (Hz) 范围 `20` 到 `20000` 内的实数标量

#### 依赖关系

要启用此端口，请为 Crossover frequency (Hz) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **O1** — Crossover order 范围 `0` 到 `8` 内的整数

#### 依赖关系

要启用此端口，请为 Crossover order 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **F2** — Crossover frequency (Hz) 范围 `20` 到 `20000` 内的实数标量

#### 依赖关系

要启用此端口，需要同时满足以下两个条件：

- 为 Crossover frequency (Hz) 参数选择 **Specify from input port**。
- 将 Number of crossovers 设置为 `2`、`3` 或 `4`。

**数据类型：** `single` | `double`

### **O2** — Crossover order 范围 `0` 到 `8` 内的整数

#### 依赖关系

要启用此端口，需要同时满足以下两个条件：

- 为 Crossover order 参数选择 **Specify from input port**。
- 将 Number of crossovers 设置为 `2`、`3` 或 `4`。

**数据类型：** `single` | `double`

### **F3** — Crossover frequency (Hz) 范围 `20` 到 `20000` 内的实数标量

#### 依赖关系

要启用此端口，需要同时满足以下两个条件：

- 为 Crossover frequency (Hz) 参数选择 **Specify from input port**。
- 将 Number of crossovers 设置为 `3` 或 `4`。

**数据类型：** `single` | `double`

### **O3** — Crossover order 范围 `0` 到 `8` 内的整数

#### 依赖关系

要启用此端口，需要同时满足以下两个条件：

- 为 Crossover order 参数选择 **Specify from input port**。
- 将 Number of crossovers 设置为 `3` 或 `4`。

**数据类型：** `single` | `double`

### **F4** — Crossover frequency (Hz) 范围 `20` 到 `20000` 内的实数标量

#### 依赖关系

要启用此端口，需要同时满足以下两个条件：

- 为 Crossover frequency (Hz) 参数选择 **Specify from input port**。
- 将 Number of crossovers 设置为 `4`。

**数据类型：** `single` | `double`

### **O4** — Crossover order 范围 `0` 到 `8` 内的整数

#### 依赖关系

要启用此端口，需要同时满足以下两个条件：

- 为 Crossover order 参数选择 **Specify from input port**。
- 将 Number of crossovers 设置为 `4`。

**数据类型：** `single` | `double`

### 输出

### **Y1** — 输出信号矩阵

端口 **Y1** 始终对应低通滤波器。

#### 依赖关系

如果 **Number of crossovers** 设置为 `1`、`2`、`3` 或 `4`，则可用。

**数据类型：** `single` | `double`

### **Y2** — 输出信号矩阵

根据指定的分频数量，端口 **Y2** 输出经过带通或高通滤波器后的原始音频信号。

#### 依赖关系

如果 **Number of crossovers** 设置为 `1`、`2`、`3` 或 `4`，则可用。

**数据类型：** `single` | `double`

### **Y3** — 输出信号矩阵

根据指定的分频数量，端口 **Y3** 对应原始音频信号的带通或高通滤波器。

#### 依赖关系

如果 **Number of crossovers** 设置为 `2`、`3` 或 `4`，则可用。

**数据类型：** `single` | `double`

### **Y4** — 输出信号矩阵

#### 依赖关系

如果 **Number of crossovers** 设置为 `3` 或 `4`，则可用。

**数据类型：** `single` | `double`

### **Y5** — 输出信号矩阵

#### 依赖关系

如果 **Number of crossovers** 设置为 `4`，则可用。

**数据类型：** `single` | `double`

## 参数

如果参数被列为可调，则可以在仿真期间更改其值。

### **Number of crossovers** — 幅频响应频带交叉的数量 `1`（默认）| `2` | `3` | `4`

如果指定多个分频，对应的 **Crossover frequency (Hz)** 和 **Crossover order** 参数会自动填充到对话框中。

Crossover Filter 模块输出的频带数量比 **Number of crossovers** 多一。

| **Number of Crossovers** | 输出中的频带数量 |
| --- | --- |
| `1` | 两个 |
| `2` | 三个 |
| `3` | 四个 |
| `4` | 五个 |

### **Crossover frequency (Hz)** — 幅频响应频带的交点 `100`（默认）| 范围 `20` 到 `20000` 内的实数标量

分频频率是多频带分频滤波器中使用的各个双频带分频滤波器的幅度响应频带的交点。

**可调：** 是

### **Crossover order** — 单个分频滤波器的阶数 `2`（默认）| 范围 [0, 8] 内的整数

分频滤波器阶数与分频滤波器斜率（以 dB/octave 为单位）相关：slope=N×6，其中 *N* 是分频阶数。

**可调：** 是

### **View filter response** — 打开每个滤波器频带的幅频响应图按钮

当 Crossover Filter 模块的参数发生变化时，该图会自动更新。

**可调：** 是

### **Variable name** — 导出的滤波器的变量名称 `myFilt`（默认）| 有效变量名称

导出滤波器时，基础工作区中用于包含该滤波器的变量名称。该名称必须是有效的 MATLAB® 变量名称。

### **Overwrite variable if it already exists** — 如果变量已存在则覆盖 `on`（默认）| `off`

选择此参数时，如果 **Variable name** 参数指定的变量已在基础工作区中存在，则导出滤波器会覆盖该变量。如果不选择此参数，并且指定的变量已在工作区中存在，则导出滤波器会创建一个新变量，并在变量名称后追加下划线和数字。例如，如果变量名称为 `var` 且它已存在，则导出的变量将命名为 `var_1`。

### **Export filter to workspace** — 将滤波器导出到工作区按钮

将滤波器导出到基础工作区中由 **Variable name** 参数指定的变量。

#### 提示

- 如果已启用 **Inherit sample rate from input** 参数且模型未运行，则无法导出滤波器。
- 如果从输入端口指定滤波器特性，则无法导出滤波器。

### **Inherit sample rate from input** — 指定输入采样率的来源 off（默认）| on

选择此参数时，模块从输入信号继承其采样率。清除此参数时，请在 **Input sample rate (Hz)** 中指定采样率。

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认）| 正标量

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` – 使用 MATLAB 解释器仿真模型。此选项可减少启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，可以调试模块的源代码。
- `Code generation` – 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否

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

**R2016a 中引入**

## 描述

音频分频滤波器

Crossover Filter 模块实现一个音频分频滤波器，用于将音频信号分成两个或多个频带。分频滤波器是多频带滤波器，其整体幅频响应是平坦的。
