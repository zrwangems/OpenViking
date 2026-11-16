---
type: simulink-block
title: 'Dyadic Synthesis Filter Bank'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'dyadicsynthesisfilterbank'
documentation_source_path: 'ref/dyadicsynthesisfilterbank.html'
language: zh-CN
chinese_source: worker-translation
---

# Dyadic Synthesis Filter Bank

## 端口

### 输入

### **Input 1** — 数据输入列向量 | 矩阵

将数据输入指定为列向量或矩阵。

输入特性取决于模块参数设置，如下总结：

- **Number of levels** 参数设置为 *n*
- **Tree structure** 参数设置：

  - `Asymmetric` — 模块接受 *n*+1 个输入子带
  - `Symmetric` — 模块接受 2*n* 个输入子带
  - **Input** 参数设置可以是 `Multiple ports` 或 `Single port`。

    该模块的输入通常是 Dyadic Analysis Filter Bank 模块的输出。由于 Dyadic Analysis Filter Bank 模块可以从单个端口或多个端口输出，Dyadic Synthesis Filter Bank 模块接受单端口输入或多端口输入。

    当将 **Input** 参数设置为 `Multiple ports` 时，必须通过不同的输入端口将每个子带作为向量或矩阵提供给模块。应通过最顶部端口输入最高频带。当将 **Input** 参数设置为 `Single port` 时，模块输入必须是串联子带的向量或矩阵。

**注意**

Dyadic Analysis Filter Bank 模块的任何输出，只要其参数设置与此模块的对应设置匹配，就是此模块的有效输入。例如，Dyadic Analysis Filter Bank 模块参数 **Output** 的设置必须与此模块中的 **Input** 参数（`Single port` 或 `Multiple ports`）相同。

**Input 设置为 Single Port 时的有效输入**

- 输入必须是串联子带的向量或矩阵。
- 每个输入列包含一个独立信号的子带。
- 上方输入行包含高频子带，下方行包含低频子带。

**Input 设置为 Multiple Ports 时的有效输入**

- 每个子带必须作为向量或矩阵提供给单独的模块输入端口。
- 每个输入的列包含一个独立信号的子带。
- 最顶部输入端口的输入是包含最高频率的子带，最底部端口的输入是包含最低频率的子带。

此图说明了 3 级非对称二进合成滤波器组的两种设置之间的差异。

**3 级 Asymmetric Dyadic Synthesis Filter Bank 的有效输入**

有关滤波器组的一般信息，请参阅 Dyadic Synthesis Filter Banks。

**注意**

此模块始终执行基于帧的处理，并且其输入必须具有特定大小。要使用不符合此模块条件的输入子带，请使用 Two-Channel Synthesis Subband Filter 模块。您可以连接多个 Two-Channel Synthesis Subband Filter 模块副本来创建多级二进合成滤波器组。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **Output 1** — 重构信号列向量 | 矩阵

该模块将重构信号输出为列向量或矩阵。

此表总结了两种输入类型的输出特性。有关输出特性为何存在的图示，请参见图 Valid Inputs to a 3-Level Asymmetric Dyadic Synthesis Filter Bank。

|  | Input = Multiple ports | Input = Single port（串联子带输入） |
| --- | --- | --- |
| **输出帧速率** | 与输入帧速率相同。 | 与输入速率相同（串联子带输入的速率）。 |
| **输出帧维度** | - 输出与输入具有相同的列数。 - 输出行数取决于滤波器组的树结构：  - **Asymmetric** — 输出行数是顶部输入端口输入行数的两倍。   - **Symmetric** — 输出行数是输入端口数与任一输入端口输入行数的乘积。 | 输出与输入具有相同的行数和列数。 |

有关滤波器组的一般信息，请参阅 Dyadic Synthesis Filter Banks。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

模块对话框中显示的参数取决于 **Filter** 参数的设置。下面描述的参数中，在任一时刻只有部分参数在对话框中可见。

**注意**

要使用此模块重构由 Dyadic Analysis Filter Bank 模块分解的信号，此模块中的所有参数都必须与 Dyadic Analysis Filter Bank 模块中的对应参数相同（**Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 除外。请参阅这些参数的描述）。

### **Filter** — 滤波器组中使用的滤波器类型 `User-defined` (default) | `Haar` | `Daubechies` | `Symlets` | `Coiflets` | `Biorthogonal` | `Reverse Biorthogonal` | `Discrete Meyer`

要确定滤波器组中的高通和低通 FIR 滤波器：

- 选择 `User defined` 以在 **Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 参数中显式指定滤波器系数。
- 选择小波（如 `Biorthogonal` 或 `Daubechies`）以指定基于小波的滤波器。该模块使用 Wavelet Toolbox 的 `wfilters` 函数构造滤波器。**Wavelet order** 或 **Filter order [synthesis / analysis]** 等额外参数变为启用状态。有关支持的小波列表，请参见表 Specifying Filters with the Filter Parameter and Related Parameters。

  必须通过将 **Filter** 参数设置为以下选项之一来指定滤波器组中的高通和低通滤波器：

  - `User defined` — 允许您在 **Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 参数中使用两个滤波器系数向量显式指定滤波器。该模块在整个滤波器组中使用相同的低通和高通滤波器。这两个滤波器应为半带滤波器，其中每个滤波器通过另一个滤波器阻止的频带。要使用此模块完美重构由 Dyadic Analysis Filter Bank 模块分解的信号，此模块中的滤波器 *必须* 设计为完美重构分析滤波器组的输出。要了解如何设计您自己的完美重构滤波器，请参阅 References。
  - 小波（如 `Biorthogonal` 或 `Daubechies`）— 该模块使用指定的小波，通过 Wavelet Toolbox 函数 `wfilters` 构造低通和高通滤波器。根据小波的不同，该模块可能会启用 **Wavelet order** 或 **Filter order [synthesis / analysis]** 参数。（后一个参数允许您为分析滤波器级和合成滤波器级指定不同的小波阶数。）要使用此模块重构由 Dyadic Analysis Filter Bank 模块分解的信号，必须将两个模块设置为使用具有相同阶数的相同小波。您必须拥有 Wavelet Toolbox 许可证才能使用小波。

  **使用 Filter 参数和相关参数指定滤波器**

  | Filter | 相关滤波器指定参数的示例设置 | 对应小波函数语法 |
  | --- | --- | --- |
  | **User-defined** | 基于 Daubechies 小波且小波阶数为 `3` 的滤波器：  - **Lowpass FIR filter coefficients =**`[0.0352 -0.0854 -0.1350 0.4599   0.8069 0.3327]` - **Highpass FIR filter coefficients =**`[-0.3327 0.8069 -0.4599   -0.1350 0.0854 0.0352]` | None |
  | **Haar** | None | `wfilters('haar')` |
  | **Daubechies** | **Wavelet order =**`4` | `wfilters('db4')` |
  | **Symlets** | **Wavelet order =**`3` | `wfilters('sym3')` |
  | **Coiflets** | **Wavelet order =**`1` | `wfilters('coif1')` |
  | **Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('bior3.1')` |
  | **Reverse Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('rbio3.1')` |
  | **Discrete Meyer** | None | `wfilters('dmey')` |

### **Filter order [synthesis / analysis]** — 合成滤波器级的小波阶数 `[1 / 1]` (default) | `[1 / 3]` | `[1 / 5]` | `[2 / 2]` | `[2 / 4]` | `[2 / 6]` | `[2 / 8]` | `[3 / 1]` | `[3 / 3]` | `[3 / 5]` | `[3 / 7]` | `[3 / 9]` | `[4 / 4]` | `[5 / 5]` | `[6 / 8]`

合成和分析滤波器级的小波阶数。例如，当将 **Filter** 参数设置为 **Biorthogonal** 并将 **Filter order [synthesis / analysis]** 参数设置为 `[2 / 6]` 时，该模块调用 `wfilters` 函数，输入参数为 `'bior2.6'`。

#### 依赖项

要启用此参数，请将 **Filter** 参数设置为 `Biorthogonal` 或 `Reverse Biorthogonal`。

### **Wavelet order** — 小波阶数 `2` (default) | positive integer

设置 **Filter** 参数中所选小波的阶数。

#### 依赖项

要启用此参数，请将 **Filter** 参数设置为 `Daubechies`、`Symlets` 或 `Coiflets`。

### **Lowpass FIR filter coefficients** — 低通 FIR 滤波器系数 `[0.3327 0.8069 0.4599 -0.1350 -0.0854 0.0352]` (default)

使用滤波器系数向量（*z* 的降幂）指定滤波器组中所有低通滤波器使用的系数。当将 **Filter** 设置为 `User defined` 时，此参数启用。低通滤波器应为半带滤波器，它通过 **Highpass FIR filter coefficients** 参数中指定的滤波器所阻止的频带。要完美重构由 Dyadic Analysis Filter Bank 分解的信号，此模块中的滤波器必须设计为完美重构分析滤波器组的输出。否则，重构将不完美。此参数的默认值指定了适用于 Dyadic Analysis Filter Bank 默认设置（基于小波阶数为 `3` 的 Daubechies 小波）的完美重构滤波器。

#### 依赖项

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Highpass FIR filter coefficients** — 高通 FIR 滤波器系数 `[0.0352 0.0854 -0.1350 -0.4599 0.8069 -0.3327]` (default)

使用滤波器系数向量（*z* 的降幂）指定滤波器组中所有高通滤波器使用的系数。当将 **Filter** 设置为 `User defined` 时，此参数启用。高通滤波器应为半带滤波器，它通过 **Lowpass FIR filter coefficients** 参数中指定的滤波器所阻止的频带。要完美重构由 Dyadic Analysis Filter Bank 分解的信号，此模块中的滤波器必须设计为完美重构分析滤波器组的输出。否则，重构将不完美。此参数的默认值指定了适用于 Dyadic Analysis Filter Bank 默认设置（基于小波阶数为 `3` 的 Daubechies 小波）的完美重构滤波器。

#### 依赖项

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Number of levels** — 滤波器组级数 `2` (default) | positive integer

选择滤波器组的级数。如 Multilevel Filter Banks 所示，*n* 级非对称结构具有 *n*+1 个输入，*n* 级对称结构具有 2*n* 个输入。

### **Tree structure** — 滤波器组结构 `Asymmetric` (default) | `Symmetric`

选择滤波器组的结构：`Asymmetric` 或 `Symmetric`。有关这些结构的更多详细信息，请参见 Multilevel Filter Banks。

此参数的默认设置对于 Dyadic Synthesis Filter Bank 模块为 `Asymmetric`，对于 IDWT 模块为 `Symmetric`。

### **Input** — 输入 `Multiple ports` (default) | `Single port`

设置为 `Multiple ports` 以在单独端口接受每个输入子带。最顶部端口接受具有最高频带的子带。设置为 `Single port` 以在单个端口接受一个串联子带的向量或矩阵。有关更多信息，请参见输入端口描述。

此参数的默认设置对于 Dyadic Synthesis Filter Bank 模块为 `Multiple ports`，对于 IDWT 模块为 `Single port`。

当将 **Input** 参数设置为 `Multiple ports` 时，必须通过不同的输入端口将每个子带作为向量或矩阵提供给模块。应通过最顶部端口输入最高频带。当将 **Input** 参数设置为 `Single port` 时，模块输入必须是串联子带的向量或矩阵。

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**R2006a 之前引入**

## 描述

从带宽更小、采样率更慢的子带重构信号，或计算逆离散小波变换 (IDWT)

您可以将此模块配置为计算逆离散小波变换 (IDWT)，或从带宽更小、采样率更慢的子带重构信号。当该模块计算输入的逆离散小波变换 (IDWT) 时，输出与输入具有相同维度。输出的每一列是相应输入列的 IDWT。重构信号时，该模块使用一系列高通和低通 FIR 滤波器从输入子带重构信号，如 Multilevel Filter Banks（Asymmetric 那个）所示。重构信号比输入子带具有更宽的带宽和更快的采样率。

您可以通过提供滤波器系数向量来指定滤波器组的高通和低通滤波器。您可以直接在模块对话框中执行此操作。如果您拥有 Wavelet Toolbox™ 许可证，可以通过从 **Filter** 参数中选择小波来指定基于小波的滤波器。您必须将滤波器组结构设置为非对称或对称，并指定滤波器组中的级数。

**注意**

要使用二进合成滤波器组完美重构二进分析滤波器组的输出，两个滤波器组的级数和树结构必须相同。此外，合成滤波器组中的滤波器必须设计为完美重构分析滤波器组的输出。否则，重构将不完美。有关展示完美重构的示例，请参见 Wavelet Reconstruction and Noise Reduction。

当此模块 **Filter** 参数中的小波选择与对应 Dyadic Analysis Filter Bank 模块的 **Filter** 参数设置相同时，此模块会自动计算基于小波的完美重构滤波器。使用小波需要 Wavelet Toolbox 许可证。要了解如何设计您自己的完美重构滤波器，请参阅 References。
