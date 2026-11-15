---
type: simulink-block
title: 'Cepstral Feature Extractor'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Feature Extraction'
documentation_page: 'cepstralfeatureextractor'
documentation_source_path: 'ref/cepstralfeatureextractor.html'
language: zh-CN
chinese_source: worker-translation
---

# Cepstral Feature Extractor

## 端口

### 输入

### **Port\_1** — 倒谱特征提取器的音频输入，列向量 | 矩阵

倒谱特征提取器的音频输入，指定为列向量或矩阵。如果指定为矩阵，则各列被视为独立的音频通道。

**数据类型：** `single` | `double`
### 输出

### **coeffs** — 倒谱系数，列向量 | 矩阵

倒谱系数，以列向量或矩阵形式返回。如果系数矩阵是 *N*×*M* 矩阵，则 *N* 由您在 **要返回的系数数量** 和 **对数能量使用** 参数中指定的值确定。*M* 等于输入音频通道数。

当 **对数能量使用** 参数设置为：

- `Append` –– 该模块将对数能量值添加到系数向量的前面。系数向量的长度为 1 + *NumCoeffs*，其中 *NumCoeffs* 是在 **要返回的系数数量** 参数中指定的值。
- `Replace` –– 该模块用信号的对数能量替换第一个系数。系数向量的长度为 *NumCoeffs*。
- `Ignore` –– 该模块不计算也不返回对数能量。

在选择 **输出 delta** 参数、**输出 delta-delta** 参数或同时选择两者之前，此端口未命名。

**数据类型：** `single` | `double`

### **delta** — 系数变化量，列向量 | 矩阵

连续调用算法时系数的变化量，以列向量或矩阵形式返回。**delta** 数组的大小和数据类型与 **coeffs** 数组相同。

#### 依赖关系

要启用此端口，请选择 **输出 delta** 参数。

**数据类型：** `single` | `double`

### **deltaDelta** — delta 值的变化量，列向量 | 矩阵

连续调用算法时 **delta** 值的变化量，以列向量或矩阵形式返回。**deltaDelta** 数组的大小和数据类型与 **coeffs** 和 **delta** 数组相同。

#### 依赖关系

要启用此端口，请选择 **输出 delta-delta** 参数。

**数据类型：** `single` | `double`

## 参数

如果某个参数列为可调，则您可以在仿真期间更改其值。

### **滤波器组类型** — 滤波器组类型 `Mel`（默认） | `Gammatone`

滤波器组类型，指定为 `Mel` 或 `Gammatone`：

- `Mel` –– 该模块计算梅尔频率倒谱系数 (MFCC)。
- `Gammatone` –– 该模块计算 gammatone 倒谱系数 (GTCC)。

**可调：** 否

### **输入信号的域** — 输入信号域 `Time`（默认） | `Frequency`

输入信号域，指定为 `Time` 或 `Frequency`。

**可调：** 否

### **要返回的系数数量** — 要返回的系数数量 `13`（默认） | 正整数

要返回的系数数量，指定为 [2, *v*] 范围内的整数，其中 *v* 是有效通带数。有效通带数取决于滤波器组类型：

- `Mel` –– 有效通带数定义为 `sum(κ <= floor(fs/2))-2`，其中 `κ` 是 mel 滤波器组中的频带边缘数，`fs` 是采样率。
- `Gammatone` –– 有效通带数定义为 `ceil(hz2erb(R(2))-hz2erb(R(1)))`，其中 `R` 是 gammatone 滤波器组的频率范围。

**可调：** 否

**数据类型：** `single` | `double`

### **非线性整流** — 非线性整流类型 `Log`（默认） | `Cubic-Root`

在离散余弦变换之前应用的非线性整流类型。

**可调：** 否

### **从输入维度继承 FFT 长度** — 从输入继承 FFT 长度 `on`（默认） | `off`

选择此参数时，FFT 长度等于输入信号的行数。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **输入信号的域** 设置为 `Time`。

### **FFTLength** — FFT 长度 `[]`（默认） | 正整数

FFT 长度，指定为正整数。默认值 `[]` 表示 FFT 长度等于输入信号的行数。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **输入信号的域** 设置为 `Time`，并选择 **从输入维度继承 FFT 长度** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **对数能量使用** — 指定对数能量的显示方式 `Append`（默认） | `Replace` | `Ignore`

指定对数能量在系数向量输出中的显示方式，指定为：

- `Append` –– 该模块将对数能量添加到系数向量的前面。系数向量的长度为 1 + *NumCoeffs*，其中 *NumCoeffs* 是在 **要返回的系数数量** 参数中指定的值。
- `Replace` –– 该模块用信号的对数能量替换第一个系数。系数向量的长度为 *NumCoeffs*。
- `Ignore` –– 该模块不计算也不返回对数能量。

**可调：** 否

### **输出 delta** — 输出 delta 值 `off`（默认） | `on`

选择此参数时，会向模块添加一个额外的输出端口 **delta**。此端口输出连续调用算法时系数的变化量。

**可调：** 否

### **输出 delta-delta** — 输出 delta-delta 值 `off`（默认） | `on`

选择此参数时，会向模块添加一个额外的输出端口 **deltaDelta**。此端口输出连续调用算法时 delta 值的变化量。

**可调：** 否

### **从输入继承采样率** — 指定输入采样率的来源 `off`（默认） | `on`

选择此参数时，模块从输入信号继承其采样率。清除此参数时，您在 **输入采样率 (Hz)** 参数中指定采样率。

**可调：** 否

### **输入采样率 (Hz)** — 输入的采样率 `16000`（默认） | 正标量

输入采样率，以 Hz 为单位，指定为实数正标量。

#### 依赖关系

要启用此参数，请清除 **从输入继承采样率** 参数。

### **仿真使用** — 指定要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

**可调：** 否

#### 高级选项卡

### **Gammatone 频率范围 (Hz)** — gammatone 滤波器组的频率范围 (Hz) `[50 8000]`（默认） | 二元素行向量

gammatone 滤波器组的频率范围，以 Hz 为单位，指定为正的、单调递增的二元素行向量。最大频率范围可以是任意有限数值。滤波器组的中心频率在 ERB 尺度上按频率范围等间隔分布。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **滤波器组类型** 设置为 `Gammatone`。

### **Mel 滤波器组的频带边缘 (Hz)** — mel 滤波器组的频带边缘 行向量

滤波器组的频带边缘，以 Hz 为单位，指定为在 [0, ∞) 范围内的非负单调递增行向量。最大频带边缘频率可以是任意有限数值。频带边缘数必须在 [4, 80] 范围内。

默认频带边缘前十个按线性间隔分布，之后按对数间隔分布。默认频带边缘按 [1] 推荐设置。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **滤波器组类型** 设置为 `Mel`。

### **Mel 滤波器组设计的域** — Mel 滤波器组设计域 `Hz`（默认） | `Bin`

Mel 滤波器组设计域，指定为 `Hz` 或 `Bin`。滤波器组设计为重叠三角形，其频带边缘由 **滤波器组的频带边缘 (Hz)** 参数指定。

频带边缘以 Hz 指定。当您将设计域设置为：

- `Hz` –– 滤波器组三角形以 Hz 为单位绘制，并映射到 bin 上。有关详细信息，请参阅 [1]。
- `Bin` –– 将 `Hz` 中的频带边缘频率转换为 bin。滤波器组三角形在 bin 中对称绘制。有关详细信息，请参阅 [2]。

**可调：** 否

#### 依赖关系

要启用此参数，请将 **滤波器组类型** 设置为 `Mel`。

### **滤波器组归一化** — 归一化滤波器组 `Bandwidth`（默认） | `Area` | `None`

用于归一化滤波器组权重的归一化技术，指定为：

- `Bandwidth` –– 每个带通滤波器的权重按该滤波器对应的带宽归一化。
- `Area` –– 每个带通滤波器的权重按该带通滤波器对应的面积归一化。
- `None` –– 滤波器权重不进行归一化。

**可调：** 否

## 所属库

Audio Toolbox / Measurements

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

**在 R2018a 中引入**

### R2022b：将删除

Cepstral Feature Extractor 模块将在未来版本中删除。请改用 MFCC 模块，或 Auditory Spectrogram、Cepstral Coefficients 和 Audio Delta 模块的组合。

| Cepstral Feature Extractor 配置 | 推荐的替代方案 |
| --- | --- |
| **滤波器组类型** 参数设置为 `Mel` | 使用 MFCC 模块。 |
| **滤波器组类型** 参数设置为 `Gammatone` | 使用 Auditory Spectrogram 模块与 Cepstral Coefficients 模块的组合。有关示例，请参阅 Extract GTCC from Audio in Simulink。 |
| 选择了 **输出 delta** 或 **输出 delta-delta** 参数 | 如果使用 MFCC 模块，请选择 **追加 delta** 或 **追加 delta-delta** 参数。如果改用 Cepstral Coefficients 模块，请使用 Audio Delta 模块提取 delta 特征。 |
| **对数能量使用** 参数设置为 `Append` 或 `Replace` | 无替代项 |
| 指定了 **Mel 滤波器组的频带边缘 (Hz)** 参数 | 无替代项 |
| **Mel 滤波器组设计的域** 参数设置为 `Bin` | 无替代项 |

## 描述

（将删除）从音频段提取倒谱特征

Cepstral Feature Extractor 模块从音频段中提取倒谱特征。倒谱特征通常用于表征语音和音乐信号。
