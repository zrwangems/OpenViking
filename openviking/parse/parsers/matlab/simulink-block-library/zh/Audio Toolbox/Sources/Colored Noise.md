---
type: simulink-block
title: 'Colored Noise'
family: 'dsp'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'colorednoise'
documentation_source_path: '../dsp/ref/colorednoise.html'
language: zh-CN
chinese_source: worker-translation
---

# Colored Noise

## 端口

### 输出

### **Port\_1** — 有色噪声信号 标量 | 向量 | 矩阵

有色噪声输出信号。信号的大小和数据类型取决于 **Number of output channels**、**Number of samples per output channel** 和 **Output data type** 参数的值。

**数据类型：** `single` | `double`

## 参数

### **Noise color** — 生成噪声的颜色 `pink`（默认）| `white` | `brown` | `blue` | `purple` | `custom`

模块生成的噪声颜色。您可以将此参数设置为：

- `pink` — 生成粉红噪声。此选项等效于将 **Power of inverse frequency** 设置为 `1`。
- `white` — 生成白噪声（平坦功率谱密度）。此选项等效于将 **Power of inverse frequency** 设置为 `0`。
- `brown` — 生成布朗噪声。也称为红噪声或布朗运动噪声。此选项等效于将 **Power of inverse frequency** 设置为 `2`。
- `blue` — 生成蓝噪声。也称为天蓝噪声。此选项等效于将 **Power of inverse frequency** 设置为 `-1`。
- `purple` — 生成紫噪声。此选项等效于将 **Power of inverse frequency** 设置为 `-2`。
- `custom` — 使用 **Power of inverse frequency** 参数指定噪声的功率密度。

### **Power of inverse frequency** — 逆功率谱密度分量 `1`（默认）| `[-2 2]` 范围内的标量

逆功率谱密度分量，*α*，指定为区间 `[-2 2]` 内的实值标量。逆指数通过 1/|*f*|α 定义随机过程的功率谱密度。此属性的默认值为 `1`。当 **Power of inverse frequency** 大于 `0` 时，模块生成低通噪声，在 *f*`= 0` 处具有奇点（极点）。这些过程表现出长记忆性。当 **Power of inverse frequency** 小于 `0` 时，模块生成具有负相关增量的高通噪声。这些过程被称为反持久性的。在功率作为频率的函数的双对数图中，Colored Noise 模块生成的过程呈现近似线性关系，斜率等于 *–α*。

#### 依赖关系

要启用此参数，请将 **Noise color** 设置为 `custom`。

### **Guarantee the output is bounded (+/-1)** — 将输出边界设置为 +1 和 −1 `off`（默认）| `on`

选择此参数可使输出限定在 +1 和 −1 之间。

当您选择此参数时，生成噪声的内部随机源为均匀分布。如果 **Noise color** 设置为 `white`，则随机源的输出不应用着色滤波器。输出为幅度在 +1 和 −1 之间的均匀噪声。如果 **Noise color** 设置为任何其他选项，则对随机源的输出应用着色滤波器，然后应用增益以确保绝对最大输出不超过 `1`。

当您不选择此参数时，内部随机源为高斯分布。输出不受限。

### **Number of output channels** — 输出通道数 `1`（默认）| 正整数

输出通道数，指定为正整数标量。此参数定义生成信号的列数。

### **Output data type** — 输出数据类型 `double`（默认）| `single`

输出的数据类型，指定为 `double` 或 `single`。

### **Number of samples per output channel** — 每个输出通道的采样数 `1024`（默认）| 正整数

输出信号每帧的采样数，指定为正整数标量。此参数定义生成信号的行数。

### **Output sample time (s)** — 输出的采样时间 `1`（默认）| 正标量

输出信号的采样时间，指定为以秒为单位的正标量。

### **Initial seed** — 随机数生成器的初始种子 `67`（默认）| 正整数

随机数生成器算法的初始种子，指定为实值正整数标量。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

生成有色噪声信号

Colored Noise 模块在其整个频率范围内生成功率谱密度为 1/|*f*|α 的有色噪声信号。逆功率谱密度分量 *α* 可以是区间 `[-2 2]` 内的任意值。模块生成的有色噪声类型取决于您在模块对话框中选择的 **Noise color** 选项。当您将 **Noise color** 设置为 `custom` 时，可以通过 **Power of inverse frequency** 参数指定噪声的功率密度。
