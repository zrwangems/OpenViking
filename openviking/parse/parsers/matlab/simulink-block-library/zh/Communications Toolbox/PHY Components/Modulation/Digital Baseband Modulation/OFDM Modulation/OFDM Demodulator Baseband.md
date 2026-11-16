---
type: simulink-block
title: 'OFDM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / OFDM Modulation'
documentation_page: 'ofdmdemodulatorbaseband'
documentation_source_path: 'ref/ofdmdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Demodulator Baseband

## 端口

### 输入

### **In** — OFDM 调制基带信号矩阵

OFDM 调制基带信号，指定为 (*osf* × *N*In)×*N*Streams 矩阵。

- *osf* 是过采样因子，由 **Oversampling factor** 确定。
- 当 `CyclicPrefixLength` 为标量时，*N*CP = **Cyclic prefix length**，并且 *N*In = *N*Sym × (*N*FFT + *N*CP)。
- 当 **Cyclic prefix length** 为行向量时，*N*CPTotal = `sum`(**Cyclic prefix length**)，并且 *N*In = (*N*Sym × *N*FFT) + *N*CPTotal。
- *N*Sym 是符号数量，由 **Number of OFDM symbols** 指定。
- *N*FFT 是子载波数量，由 **FFT length** 指定。
- *N*Streams 是由 **Number of receive antennas** 指定的接收流数量，并且必须小于或等于物理接收天线数量。

**数据类型：** `double` | `single`
**复数支持：** Yes
### 输出

### **Out** — 输出基带信号矩阵 | 三维数组

输出基带信号，返回为矩阵或 *N*DataSC×*N*Sym×*N*Streams 数组，其数据类型与输入信号相同。当 *N*Streams 为 `1` 时，输出降为矩阵。

- *N*DataSC 是数据子载波数量，使得 *N*DataSC = *N*FFT − *N*leftG − *N*rightG − *N*DCNull − *N*Pilot − *N*CustNull。

  - *N*FFT 是子载波数量，由 **FFT length** 指定。
  - *N*leftG 是左保护带中的子载波数量，由 **Number of guard bands** 的第一个元素指定。
  - *N*rightG 是右保护带中的子载波数量，由 **Number of guard bands** 的第二个元素指定。
  - *N*DCNull 是 DC 空子载波中的子载波数量，通过选择 **Remove DC carrier** 指定为 `0` 或 `1`。
  - *N*Pilot 是每个符号中的导频子载波数量。

    - 当您选择 **Pilot output port** 时，*N*Pilot = `size`(**Pilot subcarrier indices**,`1`)。
    - 当您未选择 **Pilot output port** 时，对于 *N*Out 的计算，*N*Pilot = `0`。
  - *N*CustNull 是用于自定义空子载波的子载波数量。要使用自定义空子载波，必须将 **Pilot subcarrier indices** 指定为三维数组。
- *N*Sym 是符号数量，由 **Number of OFDM symbols** 指定。
- *N*Streams 是由 **Number of receive antennas** 指定的接收流数量，并且小于或等于物理接收天线数量。

有关详细信息，请参阅子载波分配、保护带和保护间隔。

### **Pilot** — 导频信号三维数组

导频信号，返回为 *N*Pilot×*N*Sym×*N*Streams 数组。

- *N*Pilot 是每个符号中的导频子载波数量，由 `size`(**Pilot subcarrier indices**,`1`) 确定
- *N*Sym 是符号数量，由 **Number of OFDM symbols** 指定。
- *N*Streams 是由 **Number of receive antennas** 指定的接收流数量，并且小于或等于物理接收天线数量。

#### 依赖关系

要返回此输出，请选择 **Pilot output port**。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **FFT length** — FFT 点数 64（默认值）| 正整数

FFT 点数，指定为正整数标量。FFT 长度必须大于或等于 8，并且等同于子载波数量。

### **Number of guard bands** — 分配给左保护带和右保护带的子载波数量 `[6; 5]`（默认值）| 2×1 整数向量

分配给左保护带和右保护带的子载波数量，指定为 2×1 整数向量。左保护带和右保护带子载波数量 [*N*leftG; *N*rightG] 必须落在 [0,⌊*N*FFT/2⌋ − 1] 范围内，其中 *N*FFT 是由 **FFT length** 指定的 OFDM 信号中的子载波总数。有关详细信息，请参阅子载波分配、保护带和保护间隔。

### **Remove DC carrier** — 用于移除 DC 子载波的选项 `off`（默认值）| `on`

选择此参数以移除空 DC 子载波。空 DC 子载波位于频带中心，其索引值为：

- 当 *N*FFT 为偶数时，为 (*N*FFT / 2) + 1。
- 当 *N*FFT 为奇数时，为 (*N*FFT + 1) / 2。

*N*FFT 是由 **FFT length** 指定的 OFDM 信号中的子载波总数。

### **Pilot output port** — 用于输出导频子载波的选项 `off`（默认值）| `on`

选择此参数以添加用于输出导频子载波的端口。将此参数设置为：

- `off` — 导频信息可能存在，但仍嵌入在输出数据中。
- `on` — 模块将 **Pilot subcarrier indices** 指定的子载波从输出数据中分离出来，并将解调后的导频信号输出到 **Pilot** 端口。

### **Pilot subcarrier indices** — 导频子载波位置的索引 `[12; 26; 40; 54]`（默认值）| 列向量 | 矩阵 | 三维数组

导频子载波位置的索引，指定为列向量、矩阵或三维数组，其整数元素值在以下范围内

[NleftG+1, NFFT/2]∪[NFFT/2+2, NFFT−NrightG]，

其中 *N*FFT 是由 **FFT length** 指定的子载波总数，*N*leftG 和 *N*rightG 是由 **Number of guard bands** 指定的左保护带和右保护带。

您可以将 *N*Pilot 个导频载波索引分配给每个符号的相同或不同 *N*Sym 个子载波，以及跨 *N*TxStreams 个发射流分配。

- 当导频索引对于每个符号和发射天线都相同时，该参数的维度为 NPilot×1。
- 当导频索引随符号变化时，该参数的维度为 *N*Pilot×*N*Sym。
- 如果接收信号将一个符号分配给多个发射流，则该参数的维度为 *N*Pilot×1×*N*TxStreams。
- 如果索引随符号数量和发射流变化，则该参数的维度为 *N*Pilot×*N*Sym×*N*TxStreams。

**提示**

为了最小化多个发射流之间传输的干扰，每个符号的导频索引在流之间必须互不相同。

#### 依赖关系

当您选择 **Pilot output port** 时，此参数适用。

### **Cyclic prefix length** — 循环前缀长度 `16`（默认值）| 正整数 | 行向量

每个 OFDM 符号的循环前缀长度，指定为正整数标量或包含 **Number of OFDM symbols** 个元素的行向量。循环前缀长度必须在 [0, *N*FFT] 范围内，其中 *N*FFT 是由 **FFT length** 指定的 OFDM 信号中的子载波总数。当您将循环前缀长度指定为：

- 标量 — 对于所有流中的所有符号，循环前缀长度相同。
- 行向量 — 循环前缀长度可能随符号变化，但不会随流变化。

### **Oversampling factor** — 过采样因子 `1`（默认值）| 正标量

过采样因子，指定为正标量。过采样因子必须满足以下约束：

- (**Oversampling factor**×**FFT length**) 必须为整数值。
- (**Oversampling factor**×**Cyclic prefix length**) 必须为整数值。

**提示**

如果将过采样因子设置为非整数有理数，请指定分数值而不是小数值。例如，当 FFT 长度为 `12` 且过采样因子为 `4/3` 时，它们的乘积为整数 `16`。但是，在设置过采样因子时，将 `4/3` 舍入为 `1.333` 会导致乘积为非整数 `15.9960`，从而产生代码错误。

### **Number of OFDM symbols** — OFDM 符号数量 `1`（默认值）| 正整数

时频网格中的 OFDM 符号数量，指定为正整数标量。

### **Number of receive antennas** — 接收流数量 1（默认值）| 正整数

用于接收 OFDM 调制信号的接收流数量，指定为小于或等于 `64` 的正整数标量。该值必须小于或等于物理接收天线数量。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认值）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比使用 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型更改，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

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

`OFDM Demodulator Baseband` 现在支持过采样。

## 描述

使用 OFDM 方法解调

OFDM Demodulator Baseband 模块使用正交频分复用 (OFDM) 方法解调输入时域信号。有关详细信息，请参阅 OFDM 解调。该模块接受单个输入，并根据 **Pilot output port** 的状态具有一个或两个输出端口。

此图标显示启用了所有端口的模块。显示可选 Pilot 输出端口的 OFDM Demodulator Baseband 模块
