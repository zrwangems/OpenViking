---
type: simulink-block
title: 'OQPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Phase Modulation'
documentation_page: 'oqpskdemodulatorbaseband'
documentation_source_path: 'ref/oqpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# OQPSK Demodulator Baseband

## 端口

### 输入

### **In** — 输入基带波形 标量 | 列向量

输入基带波形，指定为离散时间复标量或列向量。

该模块根据 Output type 设置处理输入信号。

**数据类型：** `double`
**复数支持：** Yes
### 输出

### **Out** — 输出数据 整数列向量 | 比特列向量

输出数据，返回为整数或比特列向量。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 调制

### **Output type** — 输出类型 `Integer` (默认) | `Bit`

输出类型，指定为 `Integer` 或 `Bit`。

- 当将 **Output type** 设置为 `Integer` 时，该模块输出一个由取值从 0 到 3 的整数符号组成的向量，其长度为输出符号数。
- 当将 **Output type** 设置为 `Bit` 时，该模块输出整数的 2 比特二进制表示，为二值、偶数长度向量。

每个整数或比特对的输入周期是 Samples per symbol 乘以输出采样周期。

### **Phase offset (rad)** — 信号星座第零点的相位 `0` (默认) | 标量

相对于 π/4 的相位偏移，指定为以 radians 为单位的标量。相位偏移在正交分量延迟之前应用于信号星座的第零点。在 OQPSK 虚部分量延迟之后，信号以单位功率归一化。

**示例：** 将 **Phase offset (rad)** 设置为 `pi/4`，可使 QPSK 信号星座点的第零点对齐到坐标轴上的 {(1,0), (0,j), (-1,0), (0,-j)}。

### **Symbol mapping** — 信号星座比特映射 `Gray` (默认) | `Binary` | 自定义的由取值 0 到 3 的整数组成的 4 元素数值向量

信号星座比特映射，指定为 `Gray`、`Binary` 或由取值 0 到 3 的整数组成的自定义 4 元素数值向量。

| 设置 | 整数的星座映射 | 比特的星座映射 | 注释 |
| --- | --- | --- | --- |
| `Gray` | 整数顺序 Q1: 0、Q2: 1、Q3: 3 和 Q4: 2 | 比特顺序 Q1: 00、Q2: 01、Q3: 11 和 Q4: 10 | 信号星座映射采用格雷编码。 |
| `Binary` | 整数顺序 Q1: 0、Q2: 1、Q3: 2 和 Q4: 3 | 比特顺序 Q1: 00、Q2: 01、Q3: 10 和 Q4: 11 | 对于输入整数 `m` (0 ≤ `m` ≤ 3)，信号星座映射为复数值 `e(j*(PhaseOffset+π/4) + j*2*π*m/4)`。 |
| 由取值 0 到 3 的整数组成的自定义 4 元素数值向量 | 整数顺序 Q1: a、Q2: b、Q3: c 和 Q4: d | 比特顺序 Q1: a、Q2: b、Q3: c 和 Q4: d | 元素 [a b c d] 必须由值集合 [0, 1, 2, 3] 以任意顺序组成。 |

### 滤波

### **Pulse shape** — 滤波脉冲形状 `Half sine` (默认) | `Normal raised cosine` | `Root raised cosine` | `Custom`

选择滤波脉冲形状：`Half sine`、`Normal raised cosine`、`Root raised cosine` 或 `Custom`。

### **Rolloff factor** — 升余弦滤波器滚降因子 `0.2` (默认) | 标量

升余弦滤波器滚降因子，指定为从 `0` 到 `1` 的标量。

#### 依赖关系

当 Pulse shape 为 `Normal raised cosine` 或 `Root raised cosine` 时，此属性启用。

### **Filter span (in symbols)** — 滤波器长度 `10` (默认) | 标量

以符号为单位的滤波器长度，指定为标量。理想升余弦滤波器具有无限冲激响应。然而，为了实现该滤波器的实际实现，该对象将冲激响应截断为 **Filter span (in symbols)** 个符号。

#### 依赖关系

当 Pulse shape 为 `Normal raised cosine` 或 `Root raised cosine` 时，此属性启用。

### **Filter numerator** — FIR 滤波器分子 `[0.7071 0.7071]` (默认) | 行向量

FIR 滤波器分子，指定为行向量。

#### 依赖关系

当 Pulse shape 为 `Custom` 时，此参数启用。

### **Samples per symbol** — 每个符号的采样数 `4` (默认) | 正偶数

每个符号的采样数，指定为正偶数。

### 其他参数

### **Rate options** — 处理速率选项 `Enforce single-rate processing` (默认) | `Allow multirate processing`

- `Enforce single-rate processing`
  — 执行模型，确保输入和输出信号具有相同的端口采样时间。该模块通过使输出大小相对于输入发生变化来实现速率变化。对于整数输出，输出宽度等于 1/Samples per symbol 乘以输入宽度。

  有关示例，请参阅 Single-Rate Processing with OQPSK Demodulator Block。
- `Allow multirate processing`
  — 执行模型，允许输入和输出信号具有不同的端口采样时间。输出符号时间是 Samples per symbol 乘以输入采样时间。

  有关示例，请参阅 Multirate Processing with OQPSK Demodulator Block。

### **Output data type** — 输出数据类型 `double` (默认) | `single` | `uint8`

选择输出数据类型：`double`、`single` 或 `uint8`。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK

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

使用 OQPSK 方法进行解调

OQPSK Demodulator Baseband 模块对输入波形应用脉冲成形滤波，并使用偏移正交相移键控 (OQPSK) 方法对其进行解调。有关详细信息，请参阅 Pulse Shaping Filter。输入是已调信号的基带表示。

有关调制器-解调器对处理所引入延迟的信息，请参阅 Modulation Delays。
