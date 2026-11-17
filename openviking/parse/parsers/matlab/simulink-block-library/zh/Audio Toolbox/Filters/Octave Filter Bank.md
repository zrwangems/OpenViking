---
type: simulink-block
title: 'Octave Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'octavefilterbank'
documentation_source_path: 'ref/octavefilterbank.html'
language: zh-CN
chinese_source: worker-translation
---

# Octave Filter Bank

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 输出信号矩阵 | 三维数组
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 输入信号向量 | 矩阵

- 向量输入 –– 模块将输入视为单通道。
- 矩阵输入 –– 模块将输入的每一列视为独立通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号矩阵 | 三维数组

Octave Filter Bank 模块输出的信号与输入信号具有相同的数据类型。输出的形状取决于输入的形状、滤波器组中滤波器的数量，以及是否启用 **Bands as separate output ports** 参数。

如果 *F* 是滤波器组中滤波器的数量，输入信号是 *L*×*C* 矩阵，则模块返回 *L*×*F*×*C* 数组。如果 *C* 为 1，则模块输出矩阵。

- 向量输入 –– 当提供向量输入时，模块输出 *L*×*F* 矩阵，其中 *L* 是向量中元素的数量，*F* 是滤波器组中滤波器的数量。
- 矩阵输入 –– 当提供矩阵输入时，模块输出大小为 *L*×*F*×*C* 的三维数组，其中 *C* 是矩阵输入中的通道数。

**注意**

当启用 **Bands as separate output ports** 参数时，每个输出与输入大小相同。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Bandwidth (octaves)
  summary: 以倍频程指定的滤波器带宽 1 octave（默认）| 2/3 octave | 1/2 octave | 1/3 octave | 1/6 octave | 1/12 octave | 1/24 octave | 1/48
    octave
  group: ''
- name: Frequency range (Hz)
  summary: 滤波器组的频率范围（Hz） [22 22050]（默认）| 由正单调递增值组成的二元素行向量
  group: ''
- name: Reference frequency (Hz)
  summary: 滤波器组的参考频率（Hz） 1000（默认）| 正整数标量
  group: ''
- name: Filter order
  summary: 倍频程滤波器的阶数 12（默认）| 正偶数整数
  group: ''
- name: Octave ratio
  summary: 滤波器之间的间距 Base ten (ANSI S1.11 preferred)（默认）| Base two (musical scale)
  group: ''
- name: Inherit sample rate from input
  summary: 允许由输入信号设置采样率 off（默认）| on
  group: ''
- name: Input sample rate (Hz)
  summary: 输入的采样率 44100（默认）| 正标量
  group: ''
- name: Bands as separate output ports
  summary: 每个滤波器频带一个输出端口 off（默认）| on
  group: ''
- name: Simulate using
  summary: 指定要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
- name: View filter response
  summary: 打开绘图以可视化幅度响应 按钮
  group: ''
- name: Variable name
  summary: 导出的滤波器组的变量名称 myFilt（默认）| 有效变量名
  group: ''
- name: Overwrite variable if it already exists
  summary: 如果变量已存在则覆盖 on（默认）| off
  group: ''
- name: Export filter to workspace
  summary: 将滤波器组导出到工作区 按钮
  group: ''
```

### **Bandwidth (octaves)** — 以倍频程指定的滤波器带宽 `1 octave`（默认）| `2/3 octave` | `1/2 octave` | `1/3 octave` | `1/6 octave` | `1/12 octave` | `1/24 octave` | `1/48 octave`

以倍频程表示的滤波器带宽，指定为 `1 octave`、`2/3 octave`、`1/2 octave`、`1/3 octave`、`1/6 octave`、`1/12 octave`、`1/24 octave`、`1/48 octave`。

### **Frequency range (Hz)** — 滤波器组的频率范围（Hz） `[22 22050]`（默认）| 由正单调递增值组成的二元素行向量

滤波器组的频率范围，以 Hz 为单位，指定为包含正单调递增值的二元素行向量。模块根据 **Bandwidth (octaves)**、**Reference frequency (Hz)** 和 **Octave ratio base** 参数放置滤波器组的中心频率。中心频率超出 **Frequency range (Hz)** 的滤波器将被忽略。

### **Reference frequency (Hz)** — 滤波器组的参考频率（Hz） `1000`（默认）| 正整数标量

滤波器组的参考频率，以 Hz 为单位，指定为正整数标量。ANSI S1.11-2004 标准定义了倍频程滤波器相对于参考频率的中心频率。有关详细信息，请参阅 Center Frequencies and Band Edges。

### **Filter order** — 倍频程滤波器的阶数 `12`（默认）| 正偶数整数

倍频程滤波器的阶数，指定为正偶数整数。滤波器阶数适用于滤波器组中的每个单独滤波器。

**注意**

`octaveFilterBank` 对象的默认滤波器阶数为 `2`。

### **Octave ratio** — 滤波器之间的间距 `Base ten (ANSI S1.11 preferred)`（默认）| `Base two (musical scale)`

倍频程比率基数，指定为 `Base ten (ANSI S1.11 preferred)` 或 `Base two (musical scale)`。倍频程比率基数决定倍频程滤波器中心频率的分布。ANSI S1.11 标准推荐使用基数 10。基数 2 在音乐应用中很流行。**Base two (musical scale)** 将倍频程定义为因子 2，**Base ten (ANSI S1.11 preferred)** 将倍频程定义为因子 10 0.3。

### **Inherit sample rate from input** — 允许由输入信号设置采样率 `off`（默认）| `on`

当选择此参数时，模块从输入信号继承采样率。当清除此参数时，在 **Input sample rate (Hz)** 参数中指定采样率。

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认）| 正标量

当选择此参数时，模块接受用户提供的采样率。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Bands as separate output ports** — 每个滤波器频带一个输出端口 `off`（默认）| `on`

当选择此参数时，模块为滤波器组中的每个滤波器提供一个输出端口。每个输出端口以滤波器的中心频率标记，并且大小与输入信号相同。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。在此模式下，可以调试模块的源代码。

### **View filter response** — 打开绘图以可视化幅度响应 按钮

倍频程滤波器在对数刻度上查看时最容易理解，这模拟了人耳对频谱的加权方式。模块使用 2048 点 FFT 计算幅度响应。滤波器组的响应显示在对数频率刻度上，并带有图例以指示每个滤波器的中心频率。

### **Variable name** — 导出的滤波器组的变量名称 `myFilt`（默认）| 有效变量名

基础工作区中用于在导出时包含滤波器组的变量名称。名称必须是有效的 MATLAB 变量名。

### **Overwrite variable if it already exists** — 如果变量已存在则覆盖 `on`（默认）| `off`

当选择此参数时，如果 **Variable name** 参数指定的变量已存在于基础工作区中，导出滤波器组将覆盖该变量。如果未选择此参数且指定的变量已存在于工作区中，导出滤波器组将创建一个新变量，在变量名后附加下划线和数字。例如，如果变量名为 `var` 且已存在，则导出的变量将命名为 `var_1`。

### **Export filter to workspace** — 将滤波器组导出到工作区 按钮

将滤波器组导出到基础工作区中由 **Variable name** 参数指定的变量。

#### 提示

如果启用了 **Inherit sample rate from input** 参数且模型未运行，则无法导出滤波器组。
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

**在 R2021a 中引入**

## 描述

倍频程频带和分数倍频程频带滤波器组

Octave Filter Bank 模块将信号分解为倍频程或分数倍频程子带。倍频程频带是最高频率为最低频率两倍的频带。倍频程频带和分数倍频程频带滤波器通常用于模拟人类感知响度的方式。
