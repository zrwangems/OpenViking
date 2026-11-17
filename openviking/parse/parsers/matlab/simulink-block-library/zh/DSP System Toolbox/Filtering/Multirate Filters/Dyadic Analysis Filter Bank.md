---
type: simulink-block
title: 'Dyadic Analysis Filter Bank'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'dyadicanalysisfilterbank'
documentation_source_path: 'ref/dyadicanalysisfilterbank.html'
language: zh-CN
chinese_source: worker-translation
---

# Dyadic Analysis Filter Bank

## 端口

### 输入

### **Input 1** — 数据输入列向量 | 矩阵

将数据输入指定为列向量或矩阵。

该模块始终将输入信号解释为帧，并沿列进行操作。它将输入的每一列视为独立通道，每个通道的行数必须是 2^n 的倍数，其中 *n* 是您在 **Number of levels** 参数中指定的滤波器组级数。例如，帧大小 16 适用于三级树（16 是 2^3 的倍数）。

有关输入数据为何必须满足这些要求的更多信息，请参见 3 级非对称 Dyadic Analysis Filter Bank 的输出中的图。

该模块将输入信号分解为 *n* + 1 个或 2*n* 个子带。要分解帧大小不是 2^n 的倍数的信号，请使用 Two-Channel Analysis Subband Filter 模块。您可以连接多个 Two-Channel Analysis Subband Filter 模块副本来创建多级二进分析滤波器组。

**数据类型:** `single` | `double`
**复数支持:** Yes

### 输出

### **Output 1** — 二进子带分解输出列向量 | 矩阵

该模块将二进子带分解输出为列向量或矩阵。分解输出包含的元素从最高频子带开始，随后是按频率递减的子带。

输出特性根据模块参数设置而变化，如下列表和图所示：

- **Number of levels** 参数设置为 *n*
- **Tree structure** 参数设置：

  - `Asymmetric` — 模块产生 *n*+1 个输出子带
  - `Symmetric` — 模块产生 2*n* 个输出子带
- **Output** 参数可设置为 `Multiple ports` 或 `Single port`。当您将 **Output** 参数设置为 `Single port` 时，模块输出一个由串联子带组成的向量或矩阵。下图说明了 3 级非对称二进分析滤波器组的两种设置之间的差异。有关所示输出特性的说明，请参见表 n 级 Dyadic Analysis Filter Bank 的输出特性。

有关滤波器组级和结构的更多信息，请参见二进分析滤波器组。

**3 级非对称 Dyadic Analysis Filter Bank 的输出**

下表总结了当您将模块设置为从单端口或多端口输出时，模块的不同输出特性。

**n 级 Dyadic Analysis Filter Bank 的输出特性**

|  | 单输出端口 | 多输出端口 |
| --- | --- | --- |
| **输出描述** | 模块将所有子带串联成一个向量或矩阵，并从单个输出端口输出串联后的子带。每个输出列包含对应输入通道的子带。 | 模块从单独的输出端口输出每个子带。最顶部的端口输出频率最高的子带。每个输出列包含对应输入通道的一个子带。 |
| **输出帧率** | *不适用* | 与输入帧率相同（但是，输出帧大小可能不同，因此输出采样率可能不同。） |
| **输出维度（帧大小）** | 与输入具有相同的行数和列数。 | 输出具有与输入相同的列数。输出行数是输出帧大小。对于帧大小为 *M*i 的输入，输出 *yk* 的帧大小为 *Mo,k*：  - `Symmetric` — 所有输出都具有帧大小 *M*i / 2^n。 - `Asymmetric` — 每个输出（最后一个除外）的帧大小是上一级输出的一半。最后两个输出端口的输出具有相同的帧大小，因为它们来自滤波器组中的同一级。  *Mo,k*={*M*i/2^k(1≤k≤n), *M*i/2^n(k=n+1)} |
| **输出采样率** | 与输入采样率相同。 | 尽管输出与输入具有相同的帧率，但它们的帧大小与输入不同。因此，输出采样率 *Fso,k* 与输入采样率 *Fsi* 不同：  - `Symmetric` — 所有输出都具有采样率 *Fsi* / 2^n。 - `Asymmetric` —  *Fso,k*={*Fsi*/2^k(1≤k≤n), *Fsi*/2^n(k=n+1)} |

**数据类型:** `single` | `double`
**复数支持:** Yes

## 参数

模块对话框中显示的参数根据 **Filter** 参数的设置而变化。下面描述的参数中，每次只有部分参数会显示在对话框中。

### **Filter** — 子带分解中使用的滤波器类型 `User-defined` (默认) | `Haar` | `Daubechies` | `Symlets` | `Coiflets` | `Biorthogonal` | `Reverse Biorthogonal` | `Discrete Meyer`

通过将 **Filter** 参数设置为以下选项之一，指定滤波器组中的高通和低通滤波器：

- `User defined` — 允许您使用 **Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 参数中的两个滤波器系数向量显式指定滤波器。该模块在整个滤波器组中使用相同的低通和高通滤波器。这两个滤波器应为半带滤波器，其中每个滤波器通过另一个滤波器所阻止的频带。
- 小波（例如 `Biorthogonal` 或 `Daubechies`）— 该模块使用指定的小波通过 Wavelet Toolbox `wfilters` 函数构造低通和高通滤波器。根据小波的不同，该模块启用 **Wavelet order** 或 **Filter order [synthesis / analysis]** 参数。**Filter order [synthesis / analysis]** 参数允许您为分析滤波器级和合成滤波器级指定不同的小波阶数。您必须拥有 Wavelet Toolbox 许可证才能使用小波。

有关支持的小波列表，请参见下表。

**使用 Filter 参数及相关参数指定滤波器**

| Filter | 相关滤波器指定参数的示例设置 | 对应的小波函数语法 |
| --- | --- | --- |
| **User-defined** | 基于 Daubechies 小波且小波阶数为 `3` 的滤波器：  - **Lowpass FIR filter coefficients =**`[0.0352 -0.0854 -0.1350 0.4599   0.8069 0.3327]` - **Highpass FIR filter coefficients =**`[-0.3327 0.8069 -0.4599   -0.1350 0.0854 0.0352]` | 无 |
| **Haar** | 无 | `wfilters('haar')` |
| **Daubechies** | **Wavelet order =**`4` | `wfilters('db4')` |
| **Symlets** | **Wavelet order =**`3` | `wfilters('sym3')` |
| **Coiflets** | **Wavelet order =**`1` | `wfilters('coif1')` |
| **Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('bior3.1')` |
| **Reverse Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('rbio3.1')` |
| **Discrete Meyer** | 无 | `wfilters('dmey')` |

### **Filter order [synthesis / analysis]** — 双正交滤波器的分析和合成滤波器阶数 `[1 / 1]` (默认) | `[1 / 3]` | `[1 / 5]` | `[2 / 2]` | `[2 / 4]` | `[2 / 6]` | `[2 / 8]` | `[3 / 1]` | `[3 / 3]` | `[3 / 5]` | `[3 / 7]` | `[3 / 9]` | `[4 / 4]` | `[5 / 5]` | `[6 / 8]`

设置合成和分析滤波器级的小波阶数。例如，当您将 **Filter** 参数设置为 `Biorthogonal`，并将 **Filter order [synthesis / analysis]** 参数设置为 `[2 / 6]` 时，该模块使用输入参数 `'bior2.6'` 调用 `wfilters` 函数。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `Biorthogonal` 或 `Reverse Biorthogonal`。

### **Wavelet order** — 正交小波的阶数 `2` (默认) | 正整数

设置 **Filter** 参数中所选小波的阶数。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `Daubechies`、`Symlets` 或 `Coiflets`。

### **Lowpass FIR filter coefficients** — 低通 FIR 滤波器系数 `[0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]` (默认) | 行向量

使用滤波器系数向量（*z* 的降幂）指定滤波器组中所有低通滤波器使用的系数。低通滤波器应为半带滤波器，它通过 **Highpass FIR filter coefficients** 参数中指定的滤波器所阻止的频带。此参数的默认值指定基于 Daubechies 小波且小波阶数为 `3` 的滤波器。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Highpass FIR filter coefficients** — 高通 FIR 滤波器系数 `[-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]` (默认) | 行向量

使用滤波器系数向量（*z* 的降幂）指定滤波器组中所有高通滤波器使用的系数。当您将 **Filter** 设置为 `User defined` 时，此参数启用。高通滤波器应为半带滤波器，它通过 **Lowpass FIR filter coefficients** 参数中指定的滤波器所阻止的频带。此参数的默认值指定基于 Daubechies 小波且小波阶数为 `3` 的滤波器。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Number of levels** — 分析（分解）中使用的滤波器组级数 `2` (默认) | 大于或等于 1 的整数

选择滤波器组级数。*n* 级非对称结构有 *n*+1 个输出，*n* 级对称结构有 2*n* 个输出，如多级滤波器组所示。模块图标会根据此参数的值而变化。

### **Tree structure** — 滤波器组的结构 `Asymmetric` (默认) | `Symmetric`

选择滤波器组的结构：`Asymmetric` 或 `Symmetric`。有关更多信息，请参见多级滤波器组。

对于 Dyadic Analysis Filter Bank 模块，此参数的默认设置为 `Asymmetric`；对于 DWT 模块，默认设置为 `Symmetric`。

### **Output** — 单端口或多端口 `Multiple ports` (默认) | `Single port`

设置为 `Multiple ports` 以在单独的端口上输出每个输出子带。最顶部的端口输出具有最高频带的子带。设置为 `Single port` 以将子带串联成一个向量或矩阵，并在单个端口上输出串联后的子带。有关更多信息，请参见 Output 端口说明。

对于 Dyadic Analysis Filter Bank 模块，此参数的默认设置为 `Multiple ports`；对于 DWT 模块，默认设置为 `Single port`。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**R2006a 之前引入**

## 描述

将信号分解为具有更小带宽和更慢采样率的子带，或计算离散小波变换 (DWT)

您可以配置此模块，将宽带信号分解为具有更小带宽和更慢采样率的子带集合。该模块使用一系列高通和低通 FIR 滤波器反复划分输入频率范围，如多级滤波器组（非对称的那个）所示。

您可以通过提供滤波器系数向量来指定滤波器组的高通和低通滤波器。您可以直接在模块封装上执行此操作。如果您拥有 Wavelet Toolbox™ 许可证，可以通过从 **Filter** 参数中选择小波来指定基于小波的滤波器。您必须将滤波器组结构设置为非对称或对称，并指定滤波器组中的级数。

对于相同的输入，此模块的 DWT 配置产生的结果与 Wavelet Toolbox `dwt` 函数不同。由于 DSP System Toolbox™ 针对实时实现设计，而 Wavelet Toolbox 针对分析设计，这两个产品对边界条件和滤波器状态的处理方式不同。要使 `dwt` 函数的输出与此模块的 DWT 输出匹配，请完成以下步骤：

1. 将 `dwt` 函数的边界条件设置为零填充。为此，请在 MATLAB® 命令行中键入 `dwtmode('zpd')`。
2. 为匹配该模块（使用 FIR 滤波器实现）的延迟，请在 `dwt` 函数的输入中添加零。添加的零的数量必须等于滤波器长度的一半。

Dyadic Analysis Filter Bank 模块与 DWT 模块相同，但默认设置不同。
