---
type: simulink-block
title: 'CPM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'cpmdemodulatorbaseband'
documentation_source_path: 'ref/cpmdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# CPM Demodulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。输入信号的长度必须是 **Samples per symbol** 参数中指定的每符号样本数的整数倍。有关详细信息，请参阅 Integer-Valued and Binary-Valued Output Signals。

**数据类型：** `double` | `single`
### 输出

### **Out** — 输出信号 标量 | 列向量

输出信号，以标量或列向量形式返回。有关详细信息，请参阅 Integer-Valued and Binary-Valued Output Signals。

#### 支持的数据类型

- 双精度浮点
- 布尔值（当 **Output type** 设置为 `Bit` 时）
- 8 位、16 位和 32 位有符号整数（当 **Output type** 设置为 `Integer` 时）

**数据类型：** `double` | `Boolean` | `int8` | `int16` | `int32`

有关处理速率的详细信息，请参阅 Single-Rate Processing 和 Multirate Processing。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **M-ary number** — 调制阶数 `4`（默认）| 正整数

调制阶数，表示字母表大小，指定为 2 的非零幂的正整数。*M* 必须具有 2*K* 的形式，其中 *K* 为某个正整数，*K* 是每符号的比特数。

### **Output type** — 确定输出由整数还是比特组组成 `Integer`（默认）| `Bit`

确定输出由整数还是比特组组成，指定为 `Integer` 或 `Bit`。

### **Symbol set ordering** — 比特映射 `Binary`（默认）| `Gray`

比特映射，指定为 `Binary` 或 `Gray`。

- 将此参数设置为 `Binary` 以使用二进制编码顺序映射符号。
- 将此参数设置为 `Gray` 以使用格雷编码顺序映射符号。

有关详细信息，请参阅 Integer-Valued and Binary-Valued Output Signals。

#### 依赖关系

要启用此参数，请将 **Output type** 设置为 `Bit`。

### **Modulation index** — 调制指数 {*h*i} `0.5`（默认）| 非负标量 | 列向量

调制指数 {*h*i}，指定为非负标量或列向量。

{*h*} 表示调制指数序列。有关详细信息，请参阅 CPM Demodulation。

### **Frequency pulse shape** — 脉冲成形类型 `Rectangular`（默认）| `Raised Cosine` | `Spectral Raised Cosine` | `Gaussian` | `Tamed FM`

用于平滑调制信号相位过渡的脉冲成形类型，指定为 `Rectangular`、`Raised Cosine`、`Spectral Raised Cosine`、`Gaussian` 或 `Tamed FM`。有关滤波选项的详细信息，请参阅 Pulse Shape Filtering。

### **Main lobe pulse duration (symbol intervals)** — 主瓣持续时间 `1`（默认）| 正整数

频谱升余弦脉冲中最大瓣的主瓣持续时间，指定为正整数，表示解调器用于对调制信号进行脉冲成形的符号间隔数。

#### 依赖关系

要启用此参数，请将 **Frequency pulse shape** 设置为 `Spectral Raised Cosine`。

### **Rolloff** — 频谱升余弦脉冲形状的滚降因子 `0.2`（默认）| [0, 1] 范围内的标量

频谱升余弦脉冲的滚降因子，指定为 [0, 1] 范围内的标量。

#### 依赖关系

要启用此参数，请将 **Frequency pulse shape** 设置为 `Spectral Raised Cosine`。

### **BT product** — 高斯脉冲的带宽与符号时间之积 `0.3`（默认）| 正标量

高斯脉冲形状的带宽与符号时间之积，指定为正标量。使用 **BT product** 来减小带宽，代价是增加符号间干扰。

#### 依赖关系

要启用此参数，请将 **Frequency pulse shape** 设置为 `Gaussian`。

### **Pulse length (symbol intervals)** — 频率脉冲形状的长度 `1`（默认）| 正整数

频率脉冲形状长度，指定为正标量。有关频率脉冲长度的详细信息，请参阅 Pulse Shape Filtering 中的 *LT*。

### **Symbol prehistory** — 仿真开始前使用的数据符号 `1`（默认）| 标量 | 向量

仿真开始前使用的数据符号，指定为标量或向量，其元素为 [– (*M* – 1), (*M* – 1)] 范围内的奇整数。*M* 表示调制阶数，由 **M-ary number** 参数指定。**Symbol prehistory** 参数按时间倒序定义调制器在模块首次调用之前使用的数据符号。

- 标量值扩展为长度为 *L*P – 1 的向量。*L*P 表示脉冲长度，由 **Pulse length (symbol intervals)** 参数指定。
- 对于向量，长度必须为 *L*P – 1。

### **Phase offset (rad)** — 初始相位偏移 `0`（默认）| 标量

调制波形的初始相位偏移（以弧度为单位），指定为标量。

### **Samples per symbol** — 符号采样率 `8`（默认）| 正标量

符号采样率，指定为正标量。此参数表示每个整数或二进制字输入所输出的样本数。对于所有非二进制方案（如脉冲形状所定义），此值必须大于 1。

有关详细信息，请参阅 Signal Upsampling and Rate Changes。

### **Rate options** — 模块处理速率 `Enforce single-rate processing`（默认）| `Allow multirate processing`

模块处理速率，指定为以下选项之一：

- `Enforce single-rate processing` — 输入和输出信号具有相同的端口采样时间。该模块通过与输入相比在输出端进行大小更改来实现速率变化。输出宽度是符号数（当 **Output type** 参数设置为 `Integer` 时，由输入长度除以 **Samples per symbol** 参数值给出）。
- `Allow multirate processing` — 输入和输出信号具有不同的端口采样时间。输出周期与符号周期相同，等于输入周期与 **Samples per symbol** 参数值的乘积。

### **Traceback depth** — Viterbi 算法的回溯深度 `16`（默认）| 正整数

Viterbi 算法的回溯深度，指定为正整数，表示 Viterbi 算法用于构建每条回溯路径的网格分支数。此参数的值也是输出延迟以及在输出中第一个有意义的解调符号之前的前导零符号数。有关详细信息，请参阅 Traceback Depth and Output Delays。

### **Output data type** — 输出数据类型 `double`（默认）| `boolean` | `int8` | `int16` | `int32`

输出数据类型，指定为 `double`、`boolean`、`int8`、`int16` 或 `int32`。有关详细信息，请参阅 `Out` 中的 **Supported Data Types**。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / CPM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 CPM 方法和 Viterbi 算法解调信号

CPM Demodulator Baseband 模块解调使用连续相位调制 (CPM) 方法调制的输入信号。

CPM 是一种带记忆的调制方法。模块处理包括一个相关器，后跟一个最大似然序列检测器 (MLSD)，该检测器在状态网格中搜索具有最小欧几里得距离的路径。该模块使用 Viterbi 算法执行 MLSD。

有关此解调及所应用滤波的详细信息，请参阅 CPM Demodulation 和 Pulse Shape Filtering。
