---
type: simulink-block
title: 'OQPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
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

该模块根据 **Output type** 设置处理输入信号。

**数据类型：** `double`
**复数支持：** 是
### 输出

### **Out** — 输出数据 整数列向量 | 位列向量

输出数据，以整数或位列向量形式返回。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 调制

### **Output type** — 输出类型 `Integer`（默认）| `Bit`

输出类型，指定为 `Integer` 或 `Bit`。

- 当将 **Output type** 设置为 `Integer` 时，该模块输出一个整数符号向量，其值从 0 到 3，其长度等于输出符号的数量。
- 当将 **Output type** 设置为 `Bit` 时，该模块以二值、偶数长度向量形式输出整数的 2 位二进制表示。

每个整数或位对的输入周期为每符号采样数乘以输出采样周期。

### **Phase offset (rad)** — 信号星座图零点相位 `0`（默认）| 标量

相对于 π/4 的相位偏移，以弧度指定为标量。在正交分量延迟之前，相位偏移应用于信号星座图的零点。在 OQPSK 虚分量延迟之后，信号以单位功率归一化。

**示例：** 将 **Phase offset (rad)** 设置为 `pi/4` 可使 QPSK 信号星座图零点对齐到坐标轴上的点，{(1,0), (0,j), (-1,0), (0,-j)}。

### **Symbol mapping** — 信号星座图位映射 `Gray`（默认）| `Binary` | 自定义的 4 元素整数数值向量，其值从 0 到 3

信号星座图位映射，指定为 `Gray`、`Binary` 或自定义的 4 元素整数数值向量，其值从 0 到 3。

| 设置 | 整数的星座图映射 | 位的星座图映射 | 注释 |
| --- | --- | --- | --- |
| `Gray` | 整数顺序 Q1: 0, Q2: 1, Q3: 3, Q4: 2 | 位顺序 Q1: 00, Q2: 01, Q3: 11, Q4: 10 | 信号星座图映射为格雷编码。 |
| `Binary` | 整数顺序 Q1: 0, Q2: 1, Q3: 2, Q4: 3 | 位顺序 Q1: 00, Q2: 01, Q3: 10, Q4: 11 | 输入整数 `m`（0 ≤ `m` ≤ 3）的信号星座图映射为复数值 `e(j*(PhaseOffset+π/4) + j*2*π*m/4)`。 |
| 自定义的 4 元素整数数值向量，其值从 0 到 3 | 整数顺序 Q1: a, Q2: b, Q3: c, Q4: d | 位顺序 Q1: a, Q2: b, Q3: c, Q4: d | 元素 [a b c d] 必须由值集合 [0, 1, 2, 3] 以任意顺序组成。 |

### 滤波

### **Pulse shape** — 滤波脉冲形状 `Half sine`（默认）| `Normal raised cosine` | `Root raised cosine` | `Custom`

选择滤波脉冲形状：`Half sine`、`Normal raised cosine`、`Root raised cosine` 或 `Custom`。

### **Rolloff factor** — 升余弦滤波器滚降因子 `0.2`（默认）| 标量

升余弦滤波器滚降因子，指定为从 `0` 到 `1` 的标量。

#### 依赖关系

当 Pulse shape 为 `Normal raised cosine` 或 `Root raised cosine` 时，此属性启用。

### **Filter span (in symbols)** — 滤波器长度 `10`（默认）| 标量

以符号为单位的滤波器长度，指定为标量。理想升余弦滤波器具有无限冲激响应。然而，为实现该滤波器的实际实现，该对象将冲激响应截断为 **Filter span (in symbols)** 个符号。

#### 依赖关系

当 Pulse shape 为 `Normal raised cosine` 或 `Root raised cosine` 时，此属性启用。

### **Filter numerator** — FIR 滤波器分子 `[0.7071 0.7071]`（默认）| 行向量

FIR 滤波器分子，指定为行向量。

#### 依赖关系

当 Pulse shape 为 `Custom` 时，此参数启用。

### **Samples per symbol** — 每符号采样数 `4`（默认）| 正偶数整数

每符号采样数，指定为正偶数整数。

### 其他参数

### **Rate options** — 处理速率选项 `Enforce single-rate processing`（默认）| `Allow multirate processing`

- `Enforce single-rate processing` — 执行模型，确保输入和输出信号具有相同的端口采样时间。该模块通过在输出端相对于输入端进行大小变化来实现速率变化。对于整数输出，输出宽度等于 1/每符号采样数乘以输入宽度。

  有关示例，请参阅 Single-Rate Processing with OQPSK Demodulator Block。
- `Allow multirate processing` — 执行模型，允许输入和输出信号具有不同的端口采样时间。输出符号时间等于每符号采样数乘以输入采样时间。

  有关示例，请参阅 Multirate Processing with OQPSK Demodulator Block。

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `uint8`

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

OQPSK Demodulator Baseband 模块对输入波形应用脉冲成形滤波，并使用偏移正交相移键控（OQPSK）方法对其进行解调。有关详细信息，请参阅 Pulse Shaping Filter。输入是调制信号的基带表示。

有关调制器-解调器对处理所产生延迟的信息，请参阅 Modulation Delays。
