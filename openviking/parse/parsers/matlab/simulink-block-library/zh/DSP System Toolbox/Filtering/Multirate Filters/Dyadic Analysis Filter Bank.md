---
type: simulink-block
title: 'Dyadic Analysis Filter Bank'
family: 'dsp'
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
```yaml
ports:
- name: Input 1
  summary: 数据输入 列向量 | 矩阵
  direction: input
  data_types: single | double
- name: Output 1
  summary: 二进子带分解输出 列向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Input 1** — 数据输入 列向量 | 矩阵

将数据输入指定为列向量或矩阵。

该模块始终将输入信号解释为帧，并沿列方向进行操作。它将输入的每一列视为一个独立通道，每个通道的行数必须是 2*n* 的倍数，其中 *n* 是您在 **Number of levels** 参数中指定的滤波器组级数。例如，对于三级树结构，帧大小 16 是合适的（16 是 2³ 的倍数）。

有关输入数据为何必须满足这些要求的更多信息，请参阅 Outputs of a 3-Level Asymmetric Dyadic Analysis Filter Bank 中的图。

该模块将输入信号分解为 *n* + 1 个或 2*n* 个子带。要分解帧大小不是 2*n* 倍数的信号，请使用 Two-Channel Analysis Subband Filter 模块。您可以连接多个 Two-Channel Analysis Subband Filter 模块的副本，以创建多级二进分析滤波器组。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Output 1** — 二进子带分解输出 列向量 | 矩阵

该模块将二进子带分解输出为列向量或矩阵。分解输出包含的元素以最高频子带在前，随后是频率递减的子带。

输出特性因模块参数设置的不同而有所变化，如下列表和图所示：

- **Number of levels** 参数设置为 *n*
- **Tree structure** 参数设置：

  - `Asymmetric` — 模块产生 *n*+1 个输出子带
  - `Symmetric` — 模块产生 2*n* 个输出子带
- **Output** 参数设置可以为 `Multiple ports` 或 `Single port`。当您将 **Output** 参数设置为 `Single port` 时，模块输出一个由串联子带组成的向量或矩阵。下图说明了三级非对称二进分析滤波器组两种设置之间的差异。有关图示输出特性的说明，请参阅表 Output Characteristics for an n-Level Dyadic Analysis Filter Bank。

有关滤波器组级数和结构的更多信息，请参阅 Dyadic Analysis Filter Banks。

**Outputs of a 3-Level Asymmetric Dyadic Analysis Filter Bank**

下表总结了当您将模块设置为从单端口或多端口输出时，模块的不同输出特性。

**n 级二进分析滤波器组的输出特性**

|  | 单输出端口 | 多输出端口 |
| --- | --- | --- |
| **输出描述** | 模块将所有子带串联为一个向量或矩阵，并从单个输出端口输出串联后的子带。每个输出列包含对应输入通道的子带。 | 模块从单独的输出端口输出每个子带。最顶部的端口输出频率最高的子带。每个输出列包含对应输入通道的一个子带。 |
| **输出帧率** | *不适用* | 与输入帧率相同（但是，输出帧大小可能不同，因此输出采样率可能不同。） |
| **输出维度（帧大小）** | 与输入具有相同的行数和列数。 | 输出的列数与输入相同。输出行数为输出帧大小。对于帧大小为 *M*i 的输入，输出 *yk* 的帧大小为 *Mo,k*： - `Symmetric` — 所有输出的帧大小为 *M*i / 2*n*。 - `Asymmetric` — 每个输出（最后一个除外）的帧大小是前一级输出的一半。最后两个输出端口的输出具有相同的帧大小，因为它们源自滤波器组中的同一级。 Mo,k={Mi/2k(1≤k≤n)Mi/2n(k=n+1) |
| **输出采样率** | 与输入采样率相同。 | 虽然输出具有与输入相同的帧率，但它们的帧大小与输入不同。因此，输出采样率 *Fso,k* 与输入采样率 *Fsi* 不同： - `Symmetric` — 所有输出的采样率为 *Fsi* / 2*n*。 - `Asymmetric` —  Fso,k={Fsi/2k(1≤k≤n)Fsi/2n(k=n+1) |

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter
  summary: 子带分解中使用的滤波器类型 User-defined（默认）| Haar | Daubechies | Symlets | Coiflets | Biorthogonal | Reverse Biorthogonal |
    Discrete Meyer
  group: ''
- name: Filter order [synthesis / analysis]
  summary: 双正交滤波器的分析和合成滤波器阶数 [1 / 1]（默认）| [1 / 3] | [1 / 5] | [2 / 2] | [2 / 4] | [2 / 6] | [2 / 8] | [3 / 1] | [3 / 3] |
    [3 / 5] | [3 / 7] | [3 / 9] | [4 / 4] | [5 / 5] | [6 / 8]
  group: ''
- name: Wavelet order
  summary: 正交小波的阶数 2（默认）| 正整数
  group: ''
- name: Lowpass FIR filter coefficients
  summary: 低通 FIR 滤波器系数 [0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]（默认）| 行向量
  group: ''
- name: Highpass FIR filter coefficients
  summary: 高通 FIR 滤波器系数 [-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]（默认）| 行向量
  group: ''
- name: Number of levels
  summary: 分析（分解）中使用的滤波器组级数 2（默认）| 大于或等于 1 的整数
  group: ''
- name: Tree structure
  summary: 滤波器组的结构 Asymmetric（默认）| Symmetric
  group: ''
- name: Output
  summary: 单端口或多端口 Multiple ports（默认）| Single port
  group: ''
```

模块对话框中显示的参数因 **Filter** 参数的设置而异。以下描述的参数中只有一部分会在任何时候显示在对话框中。

### **Filter** — 子带分解中使用的滤波器类型 `User-defined`（默认）| `Haar` | `Daubechies` | `Symlets` | `Coiflets` | `Biorthogonal` | `Reverse Biorthogonal` | `Discrete Meyer`

通过将 **Filter** 参数设置为以下选项之一，指定滤波器组中的高通和低通滤波器：

- `User defined` — 允许您通过 **Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 参数中的两个滤波器系数向量显式指定滤波器。模块在整个滤波器组中使用相同的低通和高通滤波器。这两个滤波器应为半带滤波器，其中每个滤波器通过的频带是另一个滤波器所阻止的。
- 小波，例如 `Biorthogonal` 或 `Daubechies` — 模块使用指定的小波，通过 Wavelet Toolbox 的 `wfilters` 函数构造低通和高通滤波器。根据小波的不同，模块会启用 **Wavelet order** 或 **Filter order [synthesis / analysis]** 参数。**Filter order [synthesis / analysis]** 参数允许您为分析滤波器级和合成滤波器级指定不同的小波阶数。您必须拥有 Wavelet Toolbox 许可证才能使用小波。

有关支持的小波列表，请参阅此表。

**使用 Filter 参数及相关参数指定滤波器**

| Filter | 相关滤波器规格参数的示例设置 | 对应的小波函数语法 |
| --- | --- | --- |
| **User-defined** | 基于小波阶数为 `3` 的 Daubechies 小波的滤波器： - **Lowpass FIR filter coefficients =**`[0.0352 -0.0854 -0.1350 0.4599   0.8069 0.3327]` - **Highpass FIR filter coefficients =**`[-0.3327 0.8069 -0.4599   -0.1350 0.0854 0.0352]` | 无 |
| **Haar** | 无 | `wfilters('haar')` |
| **Daubechies** | **Wavelet order =**`4` | `wfilters('db4')` |
| **Symlets** | **Wavelet order =**`3` | `wfilters('sym3')` |
| **Coiflets** | **Wavelet order =**`1` | `wfilters('coif1')` |
| **Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('bior3.1')` |
| **Reverse Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('rbio3.1')` |
| **Discrete Meyer** | 无 | `wfilters('dmey')` |

### **Filter order [synthesis / analysis]** — 双正交滤波器的分析和合成滤波器阶数 `[1 / 1]`（默认）| `[1 / 3]` | `[1 / 5]` | `[2 / 2]` | `[2 / 4]` | `[2 / 6]` | `[2 / 8]` | `[3 / 1]` | `[3 / 3]` | `[3 / 5]` | `[3 / 7]` | `[3 / 9]` | `[4 / 4]` | `[5 / 5]` | `[6 / 8]`

设置合成滤波器级和分析滤波器级的小波阶数。例如，当您将 **Filter** 参数设置为 `Biorthogonal` 并将 **Filter order [synthesis / analysis]** 参数设置为 `[2 / 6]` 时，模块会以输入参数 `'bior2.6'` 调用 `wfilters` 函数。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `Biorthogonal` 或 `Reverse Biorthogonal`。

### **Wavelet order** — 正交小波的阶数 `2`（默认）| 正整数

设置 **Filter** 参数中所选小波的阶数。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `Daubechies`、`Symlets` 或 `Coiflets`。

### **Lowpass FIR filter coefficients** — 低通 FIR 滤波器系数 `[0.0352 -0.0854 -0.1350 0.4599 0.8069 0.3327]`（默认）| 行向量

使用滤波器系数向量（按 *z* 的降幂排列）指定滤波器组中所有低通滤波器使用的系数。低通滤波器应为半带滤波器，其通过的频带被 **Highpass FIR filter coefficients** 参数指定的滤波器所阻止。该参数的默认值指定了一个基于 Daubechies 小波的滤波器，小波阶数为 `3`。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Highpass FIR filter coefficients** — 高通 FIR 滤波器系数 `[-0.3327 0.8069 -0.4599 -0.1350 0.0854 0.0352]`（默认）| 行向量

使用滤波器系数向量（按 *z* 的降幂排列）指定滤波器组中所有高通滤波器使用的系数。当您将 **Filter** 设置为 `User defined` 时，此参数启用。高通滤波器应为半带滤波器，其通过的频带被 **Lowpass FIR filter coefficients** 参数指定的滤波器所阻止。该参数的默认值指定了一个基于 Daubechies 小波的滤波器，小波阶数为 `3`。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Number of levels** — 分析（分解）中使用的滤波器组级数 `2`（默认）| 大于或等于 1 的整数

选择滤波器组的级数。*n* 级非对称结构有 *n*+1 个输出，*n* 级对称结构有 2*n* 个输出，如 Multilevel Filter Banks 中所示。模块图标会根据此参数的值而变化。

### **Tree structure** — 滤波器组的结构 `Asymmetric`（默认）| `Symmetric`

选择滤波器组的结构：`Asymmetric` 或 `Symmetric`。有关详细信息，请参阅 Multilevel Filter Banks。

此参数的默认设置为：Dyadic Analysis Filter Bank 模块为 `Asymmetric`，DWT 模块为 `Symmetric`。

### **Output** — 单端口或多端口 `Multiple ports`（默认）| `Single port`

设置为 `Multiple ports` 以在单独的端口上输出每个输出子带。最顶部的端口输出具有最高频带的子带。设置为 `Single port` 以将子带连接成一个向量或矩阵，并在单个端口上输出连接后的子带。有关详细信息，请参阅 Output 端口描述。

此参数的默认设置为：Dyadic Analysis Filter Bank 模块为 `Multiple ports`，DWT 模块为 `Single port`。
## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

将信号分解为具有更小带宽和更慢采样率的子带，或计算离散小波变换（DWT）

您可以将此模块配置为将宽带信号分解为一组具有更小带宽和更慢采样率的子带。该模块使用一系列高通和低通 FIR 滤波器反复划分输入频率范围，如 Multilevel Filter Banks（非对称结构）中所示。

您可以通过提供滤波器系数向量来指定滤波器组的高通和低通滤波器。您可以直接在模块掩码上执行此操作。如果您拥有 Wavelet Toolbox™ 许可证，可以通过从 **Filter** 参数中选择小波来指定基于小波的滤波器。您必须将滤波器组结构设置为非对称或对称，并指定滤波器组中的级数。

对于相同的输入，此模块的 DWT 配置不会产生与 Wavelet Toolbox `dwt` 函数相同的结果。由于 DSP System Toolbox™ 专为实时实现而设计，而 Wavelet Toolbox 专为分析而设计，这两个产品对边界条件和滤波器状态的处理方式不同。要使 `dwt` 函数的输出与此模块的 DWT 输出匹配，请完成以下步骤：

1. 将 `dwt` 函数的边界条件设置为零填充。为此，请在 MATLAB® 命令行中键入 `dwtmode('zpd')`。
2. 要匹配模块的延迟（使用 FIR 滤波器实现），请向 `dwt` 函数的输入添加零。您添加的零的数量必须等于滤波器长度的一半。

Dyadic Analysis Filter Bank 模块与 DWT 模块相同，但默认设置不同。
