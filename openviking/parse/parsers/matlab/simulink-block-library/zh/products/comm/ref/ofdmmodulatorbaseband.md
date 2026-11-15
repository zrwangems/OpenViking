---
type: simulink-block
title: 'OFDM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / OFDM Modulation'
documentation_page: 'ofdmmodulatorbaseband'
documentation_source_path: 'ref/ofdmmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Modulator Baseband

## 端口

### 输入

### **In** — 输入基带信号数组

输入基带信号，指定为 *N*DataSC×*N*Sym×*N*Streams 数组。

- *N*DataSC 是数据子载波数，使得 *N*DataSC = *N*FFT − *N*leftG − *N*rightG − *N*DCNull − *N*Pilot − *N*CustNull。

  - *N*FFT 是子载波数，由 **FFT length** 指定。
  - *N*leftG 是左保护频带中的子载波数，由 **Number of guard bands** 的第一个元素指定。
  - *N*rightG 是右保护频带中的子载波数，由 **Number of guard bands** 的第二个元素指定。
  - *N*DCNull 是 DC 空值中的子载波数，根据 **Insert DC null** 的选择指定为 `0` 或 `1`。
  - *N*Pilot 是每个符号中的导频子载波数。

    - 当您选择 **Pilot input port** 时，*N*Pilot = `size`(**Pilot subcarrier indices**,`1`)。
    - 当您未选择 **Pilot input port** 时，*N*Pilot = `0`。
  - *N*CustNull 是用于自定义空值的子载波数。要使用自定义空值，您必须将 **Pilot subcarrier indices** 指定为三维数组。
- *N*Sym 是符号数，由 **Number of OFDM symbols** 指定。
- *N*Streams 是发射流数，由 **Number of transmit antennas** 指定，并且必须小于或等于物理发射天线数。

有关详细信息，请参阅子载波分配、保护频带和保护间隔。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **Pilot** — 导频信号数组

导频信号，指定为 *N*Pilot×*N*Sym×*N*Streams 数组。

- *N*Pilot 是每个符号中的导频子载波数，由 `size`(**Pilot subcarrier indices**,`1`) 确定。
- *N*Sym 是 OFDM 符号数，由 **Number of OFDM symbols** 指定。
- *N*Streams 是发射流数，由 **Number of transmit antennas** 指定，并且必须小于或等于物理发射天线数。

有关详细信息，请参阅子载波分配、保护频带和保护间隔。

#### 依赖关系

当您选择 **Pilot input port** 时，此端口出现。

**数据类型：** `double` | `single`
**复数支持：** Yes

### 输出

### **Out** — OFDM 调制基带信号矩阵

OFDM 调制基带信号，返回为 (*osf* × *N*Out)×*N*Streams 矩阵，其数据类型与输入信号相同。

- *osf* 是过采样因子，由 `OversamplingFactor` 确定。
- 当 **Cyclic prefix length** 为标量时，*N*CP = `CyclicPrefixLength`，且 *N*Out = *N*Sym × (*N*FFT + *N*CP)。
- 当 **Cyclic prefix length** 为行向量时，*N*CPTotal = `sum`(**Cyclic prefix length**)，且 *N*Out = (*N*Sym × *N*FFT) + *N*CPTotal。
- *N*Sym 是符号数，由 **Number of OFDM symbols** 指定。
- *N*FFT 是子载波数，由 **FFT length** 指定。
- *N*Streams 是发射流数，由 **Number of transmit antennas** 指定，并且必须小于或等于物理发射天线数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，从 **准备** 库中选择 **属性检查器**。

### **FFT length** — FFT 点数 64（默认）| 正整数

FFT 点数，指定为正整数标量。FFT 的长度必须大于或等于 8，并且等于子载波数。

### **Number of guard bands** — 分配给左保护频带和右保护频带的子载波数 `[6; 5]`（默认）| 2×1 整数值向量

分配给左保护频带和右保护频带的子载波数，指定为 2×1 整数值向量。左保护频带和右保护频带子载波数 [*N*leftG; *N*rightG] 必须落在 [0,⌊*N*FFT/2⌋ − 1] 范围内，其中 *N*FFT 是由 **FFT length** 指定的 OFDM 信号中的总子载波数。有关详细信息，请参阅子载波分配、保护频带和保护间隔。

### **Insert DC null** — 插入 DC 空值的选项 `off`（默认）| `on`

选择此参数以在 DC 子载波上插入空值。插入后，空 DC 子载波位于频带中心，其索引值为：

- 当 *N*FFT 为偶数时，(*N*FFT / 2) + 1。
- 当 *N*FFT 为奇数时，(*N*FFT + 1) / 2。

*N*FFT 是由 **FFT length** 指定的 OFDM 信号中的总子载波数。

### **Pilot input port** — 输入导频子载波的选项 `off`（默认）| `on`

选择此参数以添加用于输入导频子载波的端口。将此参数设置为：

- `off` — 输入数据端口 **In** 可以包含嵌入的导频信息，但模块不分配导频子载波索引。
- `on` — 模块分配由 **Pilot subcarrier indices** 指定的子载波，用于在 **Pilot** 输入端口对信号进行导频调制。

### **Pilot subcarrier indices** — 导频子载波位置的索引 `[12; 26; 40; 54]`（默认）| 列向量 | 矩阵 | 三维数组

导频子载波位置的索引，指定为列向量、矩阵或三维数组，其元素值为整数，范围为

[NleftG+1, NFFT/2]∪[NFFT/2+2, NFFT−NrightG]，

其中 *N*FFT 是由 **FFT length** 指定的总子载波数，*N*leftG 和 *N*rightG 是由 **Number of guard bands** 指定的左保护频带和右保护频带。

您可以将 *N*Pilot 个导频载波索引分配给每个符号的相同或不同 *N*Sym 个子载波，并且可以跨 *N*Streams 个发射流分配。

- 当导频索引对于每个符号和发射流都相同时，该参数的维度为 NPilot×1。
- 当导频索引随符号变化时，该参数的维度为 *N*Pilot×*N*Sym。
- 如果 **Pilot** 端口只有一个符号，但模块配置分配了多个发射流，则该参数的维度为 *N*Pilot×1×*N*Streams。
- 如果索引随符号数和发射流数变化，则该参数的维度为 *N*Pilot×*N*Sym×*N*Streams。

**提示**

为了最小化多个发射流之间传输的干扰，每个符号的导频索引在各流之间必须互不相同。

#### 依赖关系

当您选择 **Pilot input port** 时，此参数适用。

### **Cyclic prefix length** — 循环前缀长度 16（默认）| 正整数 | 行向量

每个 OFDM 符号的循环前缀长度，指定为包含 **Number of OFDM symbols** 个元素的正整数值标量或行向量。循环前缀长度必须在 [0, *N*FFT] 范围内，其中 *N*FFT 是由 **FFT length** 指定的 OFDM 信号中的总子载波数。当您将循环前缀长度指定为：

- 标量 — 对于所有流中的所有符号，循环前缀长度相同。
- 行向量 — 循环前缀长度可以随符号变化，但不随流变化。

### **Apply raised cosine windowing between OFDM symbols** — 在 OFDM 符号之间应用升余弦窗的选项 `off`（默认）| `on`

选择此参数以在 OFDM 符号之间应用升余弦加窗。

为了降低由频谱再生引起的带外子载波功率，请应用加窗。有关详细信息，请参阅 OFDM 升余弦加窗。

### **Window length** — 升余弦窗长度 1（默认）| 正整数

升余弦窗长度，指定为正整数标量。此值必须小于或等于由 **Cyclic prefix length** 指定的最小循环前缀长度。例如，在四个符号且循环前缀长度分别为 12、14、16 和 18 的配置中，窗长度必须小于或等于 12。

#### 依赖关系

当您选择 **Apply raised cosine windowing between OFDM symbols** 时，此参数适用。

### **Oversampling factor** — 过采样因子 `1`（默认）| 正标量

过采样因子，指定为正标量。过采样因子必须满足以下约束：

- (**Oversampling factor**×**FFT length**) 必须为整数值。
- (**Oversampling factor**×**Cyclic prefix length**) 必须为整数值。
- 如果您选择 **Apply raised cosine windowing between OFDM symbols**，则 (**Oversampling factor**×**Window length**) 必须为整数值。

**提示**

如果将过采样因子设置为非整数有理数，请指定分数值而不是十进制值。例如，FFT 长度为 `12` 且过采样因子为 `4/3` 时，其乘积为整数 `16`。但是，如果在设置过采样因子时将 `4/3` 舍入为 `1.333`，则乘积为非整数 `15.9960`，这会导致代码错误。

### **Number of OFDM symbols** — OFDM 符号数 1（默认）| 正整数

时频网格中的 OFDM 符号数，指定为正整数标量。

### **Number of transmit antennas** — 发射流数 1（默认）| 正整数

发射流数，指定为小于或等于 `64` 的正整数标量。该值必须小于或等于物理发射天线数。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时更慢。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成（Simulink）。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / OFDM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

### R2023a：增加对过采样的支持

`OFDM Modulator Baseband` 现在支持过采样。

## 描述

使用 OFDM 方法进行调制

OFDM Modulator Baseband 模块使用正交频分复用（OFDM）方法对频域信号进行调制。有关详细信息，请参阅正交频分复用。输出是 OFDM 调制信号的基带表示。

此图标显示了启用所有端口的模块。

显示可选导频输入端的 OFDM Modulator 模块
