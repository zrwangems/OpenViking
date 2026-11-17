---
type: simulink-block
title: 'CPM Modulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / CPM'
documentation_page: 'cpmmodulatorbaseband'
documentation_source_path: 'ref/cpmmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# CPM Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

当 **Input type** 参数设置为 `Integer` 时，该模块接受范围 [ –(*M*–1), (*M*–1)] 内的奇数整数。*M* 是由 **M-ary number** 参数指定的调制阶数。

当 **Input type** 参数设置为 `Bit` 时，该模块接受表示整数的二进制值输入。该模块将二进制值信号收集为 *k* = log2(*M*) 位的组。*k* 是每个符号的位数，*M* 是调制阶数。输入向量长度必须是 *k* 的整数倍。该模块根据 **Symbol set ordering** 参数的指定，将每组 *k* 位映射到一个符号。对于每组 *k* 位，该模块输出一个调制符号，并由 **Samples per symbol** 参数值过采样。

#### 支持的数据类型

- 双精度浮点
- 当 **Input type** 设置为 `Bit` 时，允许 `Boolean`
- 当 **Input type** 设置为 `Integer` 时，允许 8-bit、16-bit 和 32-bit 有符号整数

**数据类型：** `double` | `Boolean` | `int8` | `int16` | `int32`

### 输出

### **Out** — 输出信号 标量 | 列向量

输出信号，返回为标量或列向量。

- 当 **Input type** 参数设置为 `Integer` 时，该模块为每个输入符号输出一个调制符号。
- 当 **Input type** 参数设置为 `Bit` 时，该模块为每组 *k* 位输出一个调制符号。

在两种情况下，调制符号都由 **Samples per symbol** 参数值过采样。

**数据类型：** `double` | `single`

有关处理速率的详细信息，请参阅单速率处理和多速率处理。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **M-ary number** — 调制阶数 `4` (默认) | 2 的幂标量

调制阶数，指定为 2 的幂标量。调制阶数 *M* = 2*k* 指定信号星座中的点数，其中 *k* 是正整数，表示每个符号的位数。

### **Input type** — 整数或位组输入指示符 `Integer` (默认) | `Bit`

指示输入由整数还是位组组成，指定为 `Integer` 或 `Bit`。

### **Symbol set ordering** — 符号映射 `Binary` (默认) | `Gray`

位输入的符号映射，指定为 `Binary` 或 `Gray`。

- 将此参数设置为 `Binary`，以使用二进制编码顺序映射符号。
- 将此参数设置为 `Gray`，以使用格雷编码顺序映射符号。

有关详细信息，请参阅符号集。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Bit`。

### **Modulation index** — 调制指数 {*h*i} `0.5` (默认) | 非负标量 | 列向量

调制指数 {*h*i}，指定为非负标量或列向量。

{*h*} 表示调制指数序列。有关详细信息，请参阅 CPM 调制。

### **Frequency pulse shape** — 脉冲成形类型 `Rectangular` (默认) | `Raised Cosine` | `Spectral Raised Cosine` | `Gaussian` | `Tamed FM`

用于平滑调制信号相位过渡的脉冲成形类型，指定为 `Rectangular`、`Raised Cosine`、`Spectral Raised Cosine`、`Gaussian` 或 `Tamed FM`。有关滤波选项的详细信息，请参阅脉冲成形滤波。

### **Main lobe pulse duration (symbol intervals)** — 主瓣持续时间 `1` (默认) | 正整数

频谱升余弦脉冲中最大瓣的主瓣持续时间，指定为正整数，表示调制器用于对调制信号进行脉冲成形所使用的 symbol intervals 数量。

#### 依赖关系

要启用此参数，请将 **Frequency pulse shape** 设置为 `Spectral Raised Cosine`。

### **Rolloff** — 频谱升余弦脉冲形状的滚降因子 `0.2` (默认) | 非负标量

频谱升余弦脉冲的滚降因子，指定为 0 到 1 的标量。

#### 依赖关系

要启用此参数，请将 **Frequency pulse shape** 设置为 `Spectral Raised Cosine`。

### **BT product** — 高斯脉冲形状的带宽与符号时间乘积 `0.3` (默认) | 正标量

高斯脉冲形状的带宽与符号时间的乘积，指定为正标量。使用 **BT product** 来减小带宽，代价是增加符号间干扰。

#### 依赖关系

要启用此参数，请将 **Frequency pulse shape** 设置为 `Gaussian`。

### **Pulse length (symbol intervals)** — 频率脉冲形状长度 `1` (默认) | 正整数

频率脉冲形状的长度（以 symbol intervals 为单位），指定为正整数。有关频率脉冲长度的详细信息，请参阅脉冲成形滤波中的 *LT*。

### **Symbol prehistory** — 仿真开始前使用的数据符号 `1` (默认) | 标量 | 向量

仿真开始前使用的数据符号，指定为标量或向量，其元素为范围 [– (**M-ary number** – 1), (**M-ary number** – 1)] 内的奇数整数。**Symbol prehistory** 参数按时间倒序定义调制器在模块第一次调用之前使用的数据符号。

- 标量值扩展为长度为 *L*P – 1 的向量。*L*P 表示脉冲长度，由 **Pulse length (symbol intervals)** 参数指定。
- 对于向量，长度必须为 *L*P – 1。

### **Phase offset (rad)** — 初始相位偏移 `0` (默认) | 标量

调制波形的初始相位偏移（以 rad 为单位），指定为标量。

### **Samples per symbol** — 符号采样率 `8` (默认) | 正标量

符号采样率，指定为正标量。此参数表示每个整数或二进制字输入输出的样本数。对于所有非二进制方案（由脉冲形状定义），此值必须大于 1。

有关详细信息，请参阅信号上采样和速率变化。

### **Rate options** — 模块处理速率 `Enforce single-rate processing` (默认) | `Allow multirate processing`

模块处理速率，指定为以下选项之一：

- `Enforce single-rate processing` — 输入和输出信号具有相同的采样时间。该模块通过使输出相对于输入发生大小变化来实现速率变化。输出宽度等于符号数与 **Samples per symbol** 参数值的乘积。
- `Allow multirate processing` — 输入和输出信号具有不同的采样时间。输出采样时间等于符号周期除以 **Samples per symbol** 参数值。

### **Output data type** — 输出数据类型 `double` (默认) | `single`

输出数据类型，指定为 `double` 或 `single`。

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

使用 CPM 方法调制信号

CPM Modulator Baseband 模块使用连续相位调制 (CPM) 方法调制输入信号。调制器的输出是调制信号的基带表示。

有关调制和所应用滤波的详细信息，请参阅 CPM 调制和脉冲成形滤波。
