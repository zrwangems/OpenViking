---
type: simulink-block
title: 'Design Auditory Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'designauditoryfilterbankblock'
documentation_source_path: 'ref/designauditoryfilterbankblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Design Auditory Filter Bank

## 端口

### 输出

### **fb** — 滤波器组列向量 | 矩阵

听觉滤波器组，返回为 *M*×*N* 矩阵，其中：

- *M* 是频带数，由 **自动确定频带数** 和 **频带数** 参数确定。
- *N* 是频谱中的点数。如果选择 **设计单边滤波器组**，则 *N* 等于 `ceil(NFFT/2)`，其中 `NFFT` 是 **FFT 长度**。如果不选择 **设计单边滤波器组**，则 *N* 等于 **FFT 长度**。

在选择 **输出中心频率** 参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **fvec** — 中心频率行向量

带通滤波器的中心频率，以 Hz 为单位，返回为行向量，其元素数等于频带数。

#### 依赖关系

要启用此端口，请选择 **输出中心频率** 参数。

**数据类型：** `single` | `double`

## 参数

### **频率刻度** — 滤波器组的频率刻度 `mel` (默认) | `bark` | `erb`

用于设计听觉滤波器组的频率刻度，指定为 `mel`、`bark` 或 `erb`。

- `mel` –– 将滤波器组设计为在 mel 刻度上等间隔的半重叠三角形。
- `bark` –– 将滤波器组设计为在 Bark 刻度上等间隔的半重叠三角形。
- `erb` –– 将滤波器组设计为 gammatone 滤波器，其中心频率在 ERB 刻度上等间隔。

### **Mel 样式** — Mel 样式 `oshaughnessy` (默认) | `slaney`

mel 刻度的样式，指定为 `oshaughnessy` 或 `slaney`。

#### 依赖关系

要启用此参数，请将 **频率刻度** 参数设置为 `mel`。

### **FFT 长度** — DFT 点数 `1024` (默认) | 正整数

用于计算 DFT 的点数，指定为正整数。

### **设计单边滤波器组** — 设计单边或双边滤波器组 `on` (默认) | `off`

选择此参数时，模块设计单边滤波器组。否则，滤波器组为双边。

### **自动确定频带数** — 自动确定带通滤波器数 `on` (默认) | `off`

选择此参数时，模块基于 **频率刻度** 参数自动确定带通滤波器数。

- 如果将 **频率刻度** 设置为 `mel` 或 `bark`，则频带数为 `32`。
- 如果将 **频率刻度** 设置为 `erb`，则频带数等于 `ceil(hz2erb(fr(2))-hz2erb(fr(1)))`，其中 `fr` 使用 **频率范围 (Hz)** 指定。

### **频带数** — 带通滤波器数 `32` (默认) | 正整数

带通滤波器数，指定为正整数。

#### 依赖关系

要启用此参数，请清除 **自动确定频带数** 参数。

### **自动确定频率范围** — 自动确定频率范围 `on` (默认) | `off`

选择此参数时，模块将 **频率范围** 设置为 `[0,fs/2]`，其中 `fs` 使用 **采样率 (Hz)** 指定。

### **频率范围 (Hz)** — 设计听觉滤波器组的频率范围 `[0,22050]` (默认) | 二元素行向量

用于设计听觉滤波器组的频率范围，以 Hz 为单位，指定为二元素行向量。

#### 依赖关系

要启用此参数，请清除 **自动确定频率范围** 参数。

### **滤波器组设计域** — 设计滤波器组的域 `linear` (默认) | `warped`

模块设计滤波器组所在的域，指定为 `linear` 或 `warped`。将滤波器组设计域设置为 `linear`，以在 linear (Hz) 域中设计带通滤波器。将滤波器组设计域设置为 `warped`，以在 warped (mel 或 Bark) 域中设计带通滤波器。

#### 依赖关系

要启用此参数，请将 **频率刻度** 设置为 `mel` 或 `bark`。

### **滤波器组归一化** — 滤波器组的归一化技术 `bandwidth` (默认) | `area` | `none`

用于滤波器组权重的归一化技术，指定为 `bandwidth`、`area` 或 `none`。

- `bandwidth` –– 按滤波器对应的带宽对每个带通滤波器的权重进行归一化。
- `area` –– 按带通滤波器对应的面积对每个带通滤波器的权重进行归一化。
- `none` –– 模块不对滤波器的权重进行归一化。

### **输出数据类型** — 输出的数据类型 `double` (默认) | `single`

输出的数据类型，指定为 `double` 或 `single`。

### **采样率 (Hz)** — 采样率 `44.1e3` (默认) | 正标量

滤波器设计的采样率，以 Hz 为单位，指定为正标量。

### **可视化滤波器组** — 打开绘图以可视化滤波器组按钮

打开绘图以在频域中可视化滤波器。

### **输出中心频率** — 指定中心频率的附加输出端口 `off` (默认) | `on`

选择此参数时，模块显示附加输出端口 **fvec**。此端口输出带通滤波器的中心频率。

## 所属库

Audio Toolbox / Features

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b：支持 Slaney 风格的 mel 刻度

将 **Mel 样式** 参数设置为 `slaney`，以使用 Slaney 风格的 mel 刻度。

## 描述

设计频域听觉滤波器组

Design Auditory Filter Bank 模块输出频域听觉滤波器组。您可以使用听觉滤波器组将音频信号分解为单独的频带，以进行特征提取。
