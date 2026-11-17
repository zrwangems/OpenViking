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
```yaml
ports:
- name: Input 1
  summary: 数据输入 列向量 | 矩阵
  direction: input
  data_types: single | double
- name: Output 1
  summary: 重构信号 列向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Input 1** — 数据输入 列向量 | 矩阵

将数据输入指定为列向量或矩阵。

输入特性因模块参数设置而异，总结如下：

- **Number of levels** 参数设置为 *n*
- **Tree structure** 参数设置：

  - `Asymmetric` — 模块接受 *n*+1 个输入子带
  - `Symmetric` — 模块接受 2*n* 个输入子带
  - **Input** 参数设置可以是 `Multiple ports` 或 `Single port`。

    此模块的输入通常是 Dyadic Analysis Filter Bank 模块的输出。由于 Dyadic Analysis Filter Bank 模块可以从单个端口或多个端口输出，因此 Dyadic Synthesis Filter Bank 模块接受单个端口或多个端口的输入。

    当您将 **Input** 参数设置为 `Multiple ports` 时，必须通过不同的输入端口将每个子带以向量或矩阵的形式提供给模块。您应该通过最顶部的端口输入最高频带。当您将 **Input** 参数设置为 `Single port` 时，模块输入必须是拼接子带的向量或矩阵。

**注意**

Dyadic Analysis Filter Bank 模块的任何输出，只要其参数设置与此模块的相应设置匹配，就是此模块的有效输入。例如，Dyadic Analysis Filter Bank 模块参数 **Output** 的设置必须与此模块中的 **Input** 参数（`Single port` 或 `Multiple ports`）相同。

**Input 设置为 Single Port 时的有效输入**

- 输入必须是拼接子带的向量或矩阵。
- 每个输入列包含独立信号的子带。
- 上方输入行包含高频子带，下方行包含低频子带。

**Input 设置为 Multiple Ports 时的有效输入**

- 每个子带必须以向量或矩阵的形式提供给单独的模块输入端口。
- 每个输入的列包含独立信号的子带。
- 最顶部输入端口的输入是包含最高频率的子带，最底部端口的输入是包含最低频率的子带。

下图说明了 3 级非对称双通道合成滤波器组的两种设置之间的差异。

**3 级非对称双通道合成滤波器组的有效输入**

有关滤波器组的一般信息，请参阅 Dyadic Synthesis Filter Banks。

**注意**

此模块始终执行基于帧的处理，其输入必须具有特定的大小。要使用不符合此模块标准的输入子带，请使用 Two-Channel Synthesis Subband Filter 模块。您可以连接多个 Two-Channel Synthesis Subband Filter 模块的副本，以创建多级双通道合成滤波器组。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Output 1** — 重构信号 列向量 | 矩阵

模块将重构信号输出为列向量或矩阵。

下表总结了两种输入类型的输出特性。有关输出特性存在原因的说明，请参阅图 3 级非对称双通道合成滤波器组的有效输入。

|  | Input = Multiple ports | Input = Single port（拼接子带输入） |
| --- | --- | --- |
| **输出帧速率** | 与输入帧速率相同。 | 与输入速率相同（拼接子带输入的速率）。 |
| **输出帧维度** | - 输出的列数与输入相同。 - 输出行数取决于滤波器组的树结构：  - **Asymmetric** — 输出行数是最顶部输入端口输入行数的两倍。   - **Symmetric** — 输出行数是输入端口数与任一输入端口输入行数的乘积。 | 输出的行数和列数与输入相同。 |

有关滤波器组的一般信息，请参阅 Dyadic Synthesis Filter Banks。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter
  summary: 滤波器组中使用的滤波器类型 User-defined（默认）| Haar | Daubechies | Symlets | Coiflets | Biorthogonal | Reverse Biorthogonal |
    Discrete Meyer
  group: ''
- name: Filter order [synthesis / analysis]
  summary: 合成滤波器级的小波阶数 [1 / 1]（默认）| [1 / 3] | [1 / 5] | [2 / 2] | [2 / 4] | [2 / 6] | [2 / 8] | [3 / 1] | [3 / 3] | [3 / 5]
    | [3 / 7] | [3 / 9] | [4 / 4] | [5 / 5] | [6 / 8]
  group: ''
- name: Wavelet order
  summary: 小波阶数 2（默认）| 正整数
  group: ''
- name: Lowpass FIR filter coefficients
  summary: 低通 FIR 滤波器系数 [0.3327 0.8069 0.4599 -0.1350 -0.0854 0.0352]（默认）
  group: ''
- name: Highpass FIR filter coefficients
  summary: 高通 FIR 滤波器系数 [0.0352 0.0854 -0.1350 -0.4599 0.8069 -0.3327]（默认）
  group: ''
- name: Number of levels
  summary: 滤波器组级数 2（默认）| 正整数
  group: ''
- name: Tree structure
  summary: 滤波器组结构 Asymmetric（默认）| Symmetric
  group: ''
- name: Input
  summary: 输入 Multiple ports（默认）| Single port
  group: ''
```

模块对话框中显示的参数因 **Filter** 参数的设置而异。下面描述的参数中只有一部分在任何时候都可见于对话框中。

**注意**

要使用此模块重构由 Dyadic Analysis Filter Bank 模块分解的信号，此模块中的所有参数必须与 Dyadic Analysis Filter Bank 模块中的相应参数相同（**Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 除外。请参阅这些参数的描述）。

### **Filter** — 滤波器组中使用的滤波器类型 `User-defined`（默认）| `Haar` | `Daubechies` | `Symlets` | `Coiflets` | `Biorthogonal` | `Reverse Biorthogonal` | `Discrete Meyer`

要确定滤波器组中的高通和低通 FIR 滤波器：

- 选择 `User defined` 以在 **Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 参数中显式指定滤波器系数。
- 选择小波（如 `Biorthogonal` 或 `Daubechies`）以指定基于小波的滤波器。模块使用 Wavelet Toolbox 的 `wfilters` 函数来构造滤波器。**Wavelet order** 或 **Filter order [synthesis / analysis]** 等额外参数将变为可用。有关支持的小波列表，请参阅表 使用 Filter 参数及相关参数指定滤波器。

  您必须通过将 **Filter** 参数设置为以下选项之一来指定滤波器组中的高通和低通滤波器：

  - `User defined` — 允许您通过 **Lowpass FIR filter coefficients** 和 **Highpass FIR filter coefficients** 参数中的两个滤波器系数向量显式指定滤波器。模块在整个滤波器组中使用相同的低通和高通滤波器。这两个滤波器应为半带滤波器，其中每个滤波器通过另一个滤波器阻带的频带。要使用此模块完美重构由 Dyadic Analysis Filter Bank 模块分解的信号，此模块中的滤波器*必须*设计为完美重构分析滤波器组的输出。要了解如何设计自己的完美重构滤波器，请参阅 References。
  - 小波（如 `Biorthogonal` 或 `Daubechies`）— 模块使用指定的小波通过 Wavelet Toolbox 函数 `wfilters` 构造低通和高通滤波器。根据小波的不同，模块可能启用 **Wavelet order** 或 **Filter order [synthesis / analysis]** 参数。（后者参数允许您为分析和合成滤波器级指定不同的小波阶数。）要使用此模块重构由 Dyadic Analysis Filter Bank 模块分解的信号，您必须将两个模块设置为使用相同小波且阶数相同。您必须拥有 Wavelet Toolbox 许可证才能使用小波。

  **使用 Filter 参数及相关参数指定滤波器**

  | Filter | 相关滤波器规格参数的示例设置 | 对应的小波函数语法 |
  | --- | --- | --- |
  | **User-defined** | 基于 Daubechies 小波且小波阶数为 `3` 的滤波器： - **Lowpass FIR filter coefficients =**`[0.0352 -0.0854 -0.1350 0.4599   0.8069 0.3327]` - **Highpass FIR filter coefficients =**`[-0.3327 0.8069 -0.4599   -0.1350 0.0854 0.0352]` | 无 |
  | **Haar** | 无 | `wfilters('haar')` |
  | **Daubechies** | **Wavelet order =**`4` | `wfilters('db4')` |
  | **Symlets** | **Wavelet order =**`3` | `wfilters('sym3')` |
  | **Coiflets** | **Wavelet order =**`1` | `wfilters('coif1')` |
  | **Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('bior3.1')` |
  | **Reverse Biorthogonal** | **Filter order [synthesis / analysis] =**`[3/1]` | `wfilters('rbio3.1')` |
  | **Discrete Meyer** | 无 | `wfilters('dmey')` |

### **Filter order [synthesis / analysis]** — 合成滤波器级的小波阶数 `[1 / 1]`（默认）| `[1 / 3]` | `[1 / 5]` | `[2 / 2]` | `[2 / 4]` | `[2 / 6]` | `[2 / 8]` | `[3 / 1]` | `[3 / 3]` | `[3 / 5]` | `[3 / 7]` | `[3 / 9]` | `[4 / 4]` | `[5 / 5]` | `[6 / 8]`

合成和分析滤波器级的小波阶数。例如，当您将 **Filter** 参数设置为 **Biorthogonal** 并将 **Filter order [synthesis / analysis]** 参数设置为 `[2 / 6]` 时，模块使用输入参数 `'bior2.6'` 调用 `wfilters` 函数。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `Biorthogonal` 或 `Reverse Biorthogonal`。

### **Wavelet order** — 小波阶数 `2`（默认）| 正整数

设置 **Filter** 参数中所选小波的阶数。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `Daubechies`、`Symlets` 或 `Coiflets`。

### **Lowpass FIR filter coefficients** — 低通 FIR 滤波器系数 `[0.3327 0.8069 0.4599 -0.1350 -0.0854 0.0352]`（默认）

使用滤波器系数向量（*z* 的降幂）指定滤波器组中所有低通滤波器使用的系数。当您将 **Filter** 设置为 `User defined` 时，此参数启用。低通滤波器应为半带滤波器，其通过的频带是 **Highpass FIR filter coefficients** 参数中指定的滤波器的阻带。要完美重构由 Dyadic Analysis Filter Bank 分解的信号，此模块中的滤波器必须设计为完美重构分析滤波器组的输出。否则，重构不完美。此参数的默认值指定了 Dyadic Analysis Filter Bank 默认设置（基于小波阶数为 `3` 的 Daubechies 小波）的完美重构滤波器。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Highpass FIR filter coefficients** — 高通 FIR 滤波器系数 `[0.0352 0.0854 -0.1350 -0.4599 0.8069 -0.3327]`（默认）

使用滤波器系数向量（*z* 的降幂）指定滤波器组中所有高通滤波器使用的系数。当您将 **Filter** 设置为 `User defined` 时，此参数启用。高通滤波器应为半带滤波器，其通过的频带是 **Lowpass FIR filter coefficients** 参数中指定的滤波器的阻带。要完美重构由 Dyadic Analysis Filter Bank 分解的信号，此模块中的滤波器必须设计为完美重构分析滤波器组的输出。否则，重构不完美。此参数的默认值指定了 Dyadic Analysis Filter Bank 默认设置（基于小波阶数为 `3` 的 Daubechies 小波）的完美重构滤波器。

#### 依赖关系

要启用此参数，请将 **Filter** 参数设置为 `User-defined`。

### **Number of levels** — 滤波器组级数 `2`（默认）| 正整数

选择滤波器组的级数。*n* 级非对称结构有 *n*+1 个输入，*n* 级对称结构有 2*n* 个输入，如 Multilevel Filter Banks 所示。

### **Tree structure** — 滤波器组结构 `Asymmetric`（默认）| `Symmetric`

选择滤波器组的结构：`Asymmetric` 或 `Symmetric`。有关这些结构的更多详细信息，请参阅 Multilevel Filter Banks。

此参数的默认设置为：Dyadic Synthesis Filter Bank 模块为 `Asymmetric`，IDWT 模块为 `Symmetric`。

### **Input** — 输入 `Multiple ports`（默认）| `Single port`

设置为 `Multiple ports` 以在单独的端口接受每个输入子带。最顶部的端口接受具有最高频带的子带。设置为 `Single port` 以在单个端口接受一个拼接子带的向量或矩阵。有关更多信息，请参阅输入端口描述。

此参数的默认设置为：Dyadic Synthesis Filter Bank 模块为 `Multiple ports`，IDWT 模块为 `Single port`。

当您将 **Input** 参数设置为 `Multiple ports` 时，必须通过不同的输入端口将每个子带以向量或矩阵的形式提供给模块。您应该通过最顶部的端口输入最高频带。当您将 **Input** 参数设置为 `Single port` 时，模块输入必须是拼接子带的向量或矩阵。
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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

从具有较小带宽和较慢采样率的子带重构信号，或计算逆离散小波变换（IDWT）

您可以将此模块配置为计算逆离散小波变换（IDWT）或从具有较小带宽和较慢采样率的子带重构信号。当模块计算输入的逆离散小波变换（IDWT）时，输出具有与输入相同的维度。输出的每一列是相应输入列的 IDWT。当重构信号时，模块使用一系列高通和低通 FIR 滤波器从输入子带重构信号，如 Multilevel Filter Banks（非对称的那个）所示。重构信号具有比输入子带更宽的带宽和更快的采样率。

您可以通过提供滤波器系数向量来指定滤波器组的高通和低通滤波器。您可以直接在模块对话框中执行此操作。如果您拥有 Wavelet Toolbox™ 许可证，可以通过从 **Filter** 参数中选择小波来指定基于小波的滤波器。您必须将滤波器组结构设置为非对称或对称，并指定滤波器组中的级数。

**注意**

要使用双通道合成滤波器组完美重构双通道分析滤波器组的输出，两个滤波器组的级数和树结构必须相同。此外，合成滤波器组中的滤波器必须设计为完美重构分析滤波器组的输出。否则，重构不完美。有关展示完美重构的示例，请参阅 Wavelet Reconstruction and Noise Reduction。

当此模块的 **Filter** 参数中的小波选择与相应 Dyadic Analysis Filter Bank 模块的 **Filter** 参数设置相同时，此模块会自动计算基于小波的完美重构滤波器。使用小波需要 Wavelet Toolbox 许可证。要了解如何设计自己的完美重构滤波器，请参阅 References。
