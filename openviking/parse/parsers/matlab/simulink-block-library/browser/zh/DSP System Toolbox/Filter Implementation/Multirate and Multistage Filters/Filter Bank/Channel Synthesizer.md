---
type: simulink-block
title: 'Channel Synthesizer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / Filter Bank'
documentation_page: 'channelsynthesizer'
documentation_source_path: 'ref/channelsynthesizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Channel Synthesizer

## 端口

### 输入

### **x** — 输入窄带信号 *Q*×*M* 矩阵 | *L*×*M*×*N* 数组

输入窄带信号，信道合成器将这些信号合并以形成宽带信号。每个窄带信号在输入信号中形成一列。输入中的列数对应于滤波器组的频带数。如果输入是三维的，则每个矩阵对应于一个单独的信道。

在将 **多相滤波器设定** 设置为 `Coefficients` 并选中 **从输入端口指定系数** 参数之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **coeffs** — 原型低通滤波器系数行向量

原型低通滤波器的系数。每个频带必须至少有一个系数。如果低通滤波器的长度小于频带数，则模块会对系数进行零填充。

如果指定复系数，则模块设计一个以非零频率为中心的原型滤波器，也称为带通滤波器。原型带通滤波器的调制版本相对于原型滤波器出现，并围绕频率范围 [−*F*s *F*s] 进行环绕。

#### 依赖关系

当您将 **多相滤波器设定** 设置为 `Coefficients` 并选中 **从输入端口指定系数** 参数时，此端口出现。

**数据类型：** `single` | `double`
**复数支持：** Yes
### 输出

### **Port\_1** — 宽带信号 *Q×M*×1 向量 | *L×M*×*N* 矩阵

信道合成器从多个输入窄子带形成的宽带信号。

如果输入是以下之一：

- *Q*×*M* 矩阵 — 输出为 *Q×M*×1 向量。*M* 是频带数。
- *Q*×*M*×*N* 矩阵 — 输出为 *Q×M*×*N* 矩阵。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

如果参数被列为可调，则可以在仿真期间更改其值。

### **InterpolationFactor** — 插值因子 `Number of frequency bands`（默认）| 正整数

*自 R2024a 起*

将插值因子 *L* 指定为以下之一：

- `Number of frequency bands` –– 当您更改频带数时，插值因子会自动更改。
- 大于或等于频带数 *M* 的正整数。

频带数等于输入信号中的通道数。如果插值因子 *L* 等于频带数 *M*，则 *L*/*M* 比率等于 1，并且该合成器称为临界采样信道合成器。

如果 *L* 大于 *M*，则 *L*/*M* 比率必须为整数。有关更多详细信息，请参阅算法。

### **多相滤波器设定** — 滤波器设计参数或系数 `Number of taps per band and stopband attenuation`（默认）| `Coefficients`

- `Number of taps per band and stopband attenuation` — 通过 **每个频带的滤波器抽头数** 和 **阻带衰减 (dB)** 参数指定滤波器设计参数。当您指定设计参数时，使用 `designMultirateFIR` 函数设计滤波器。
- `Coefficients` — 使用 **原型低通滤波器系数** 参数直接指定滤波器系数，或通过 **coeffs** 端口输入这些系数。

### **每个频带的滤波器抽头数** — 每个频带的滤波器系数个数 `12`（默认）| 正整数

每个多相分支使用的滤波器系数个数。多相分支数与频带数匹配。原型低通滤波器的滤波器系数总数由频带数与每个频带的滤波器抽头数的乘积给出。频带数等于输入中的列数。对于给定的阻带衰减，增加每个频带的抽头数会收窄滤波器的过渡宽度。因此，每个频带可用的带宽更大，但代价是计算量增加。

#### 依赖关系

要启用此参数，请将 **多相滤波器设定** 设置为 `Number of taps per band and stopband attenuation`。

### **阻带衰减 (dB)** — 阻带衰减 `80`（默认）| 正实数标量

低通滤波器的阻带衰减，以 dB 为单位。此值控制从一个频带到下一个频带的最大混叠量。随着阻带衰减增加，通带波纹减小。

#### 依赖关系

要启用此参数，请将 **多相滤波器设定** 设置为 `Number of taps per band and stopband attenuation`。

### **从输入端口指定系数** — 用于指定低通滤波器系数的标志 off（默认）| on

选中此复选框时，低通滤波器系数通过 **coeffs** 端口输入。清除此复选框时，系数通过 **原型低通滤波器系数** 参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **多相滤波器设定** 设置为 `Coefficients`。

### **原型低通滤波器系数** — 原型低通滤波器的系数 `rcosdesign(0.25,6,8,'sqrt')`（默认）| 行向量

此参数指定原型低通滤波器的系数。默认值是 `rcosdesign(0.25,6,8,'sqrt')` 返回的系数向量。每个频带必须至少有一个系数。如果低通滤波器的长度小于频带数，则模块会对系数进行零填充。

如果指定复系数，则模块设计一个以非零频率为中心的原型滤波器，也称为带通滤波器。原型带通滤波器的调制版本相对于原型滤波器出现，并围绕频率范围 [−*F*s *F*s] 进行环绕。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **多相滤波器设定** 设置为 `Coefficients`，并清除 **从输入端口指定系数** 参数。

**复数支持：** Yes

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2024a：支持整数过采样

使用新的 **插值因子** 参数指定大于或等于频带数 *M* 的插值因子 *L*。如果 *L* > *M*，则比率 *L*/*M* 必须为整数，并且该合成器称为过采样信道合成器。

## 描述

多相 FFT 合成滤波器组

Channel Synthesizer 模块通过使用基于 FFT 的合成滤波器组，将多个窄带信号合并为宽带信号。该滤波器组使用原型低通滤波器，并通过多相结构实现。您可以直接指定滤波器系数，也可以通过设计参数指定。当您指定设计参数时，使用 `designMultirateFIR` 函数设计滤波器。

此模块还接受可变大小输入。也就是说，在仿真期间，您可以更改每个输入通道的大小。通道数不能更改。
