---
type: simulink-block
title: 'OQPSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'oqpskmodulatorbaseband'
documentation_source_path: 'ref/oqpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# OQPSK Modulator Baseband

## 端口

### 输入

### **In** — 输入数据 整数列向量 | 位列向量

输入数据，指定为整数或位列向量。

输入信号根据为 **Input type** 选择的设置进行处理。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — 输出基带波形 列向量

输出基带波形，返回为复数数据列向量。**Output data type** 参数指定输出信号的数据类型。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### 调制

### **Input type** — 输入类型 `Integer`（默认） | `Bit`

输入类型，指定为 `Integer` 或 `Bit`。

- 当将 **Input type** 设置为 `Integer` 时，输入可以是标量值或列向量，其长度为输入符号数。
- 当将 **Input type** 设置为 `Bit` 时，输入宽度必须是 2 的整数倍。

输出采样周期是输入中每个整数或位对的周期除以 Samples per symbol。

### **Symbol mapping** — 信号星座位映射 `Gray`（默认） | `Binary` | 自定义 4 元素整数数值向量，值从 0 到 3

信号星座位映射，指定为 `Gray`、`Binary` 或由值从 0 到 3 的整数组成的自定义 4 元素数值向量。

| 设置 | 整数的星座映射 | 位的星座映射 | 注释 |
| --- | --- | --- | --- |
| `Gray` | 整数顺序 Q1: 0, Q2: 1, Q3: 3 和 Q4: 2 | 位顺序 Q1: 00, Q2: 01, Q3: 11 和 Q4: 10 | 信号星座映射采用 Gray 编码。 |
| `Binary` | 整数顺序 Q1: 0, Q2: 1, Q3: 2 和 Q4: 3 | 位顺序 Q1: 00, Q2: 01, Q3: 10 和 Q4: 11 | 输入整数 `m` (0 ≤ `m` ≤ 3) 的信号星座映射为复数值 `e(j*(PhaseOffset+π/4) + j*2*π*m/4)`。 |
| 自定义 4 元素整数数值向量，值从 0 到 3 | 整数顺序 Q1: a, Q2: b, Q3: c 和 Q4: d | 位顺序 Q1: a, Q2: b, Q3: c 和 Q4: d | 元素 [a b c d] 必须由值集 [0, 1, 2, 3] 以任意顺序组成。 |

### **Phase offset (rad)** — 信号星座第零点的相位 `0`（默认） | 标量

相对于 π/4 的相位偏移，指定为以 rad 为单位的标量。该相位偏移应用于信号星座的第零点，然后才延迟正交分量。经过 OQPSK 虚部分量延迟后，信号归一化为单位功率。

**示例：** 将 **Phase offset (rad)** 设置为 `pi/4` 会使 QPSK 信号星座的第零点对齐到坐标轴上的点 {(1,0), (0,j), (-1,0), (0,-j)}。

### **View Constellation** — 用于绘制参考星座的选项按钮

点击模块封装上的 **View Constellation**，以可视化指定模块参数的信号星座。查看星座之前，请应用参数设置。有关详细信息，请参阅 View Constellation of Modulator Block。

**注意**

显示的星座未描述由 OQPSK 调制器引入的 IQ 延迟。

### 滤波

### **Pulse shape** — 滤波脉冲形状 `Half sine`（默认） | `Normal raised cosine` | `Root raised cosine` | `Custom`

选择滤波脉冲形状：`Half sine`、`Normal raised cosine`、`Root raised cosine` 或 `Custom`。

### **Rolloff factor** — 升余弦滤波器滚降因子 `0.2`（默认） | 标量

升余弦滤波器滚降因子，指定为范围 [`0`, `1`] 内的标量。

#### 依赖关系

当 **Pulse shape** 为 `Normal raised cosine` 或 `Root raised cosine` 时，启用此属性。

### **Filter span (in symbols)** — 滤波器长度 `10`（默认） | 标量

以符号为单位的滤波器长度，指定为标量。理想升余弦滤波器具有无限脉冲响应。然而，为了实现该滤波器的实际实现，对象将脉冲响应截断为 **Filter span (in symbols)** 个符号。

#### 依赖关系

当 Pulse shape 为 `Normal raised cosine` 或 `Root raised cosine` 时，启用此属性。

### **Filter numerator** — 滤波器分子 `[0.7071 0.7071]`（默认） | 行向量

FIR 滤波器分子，指定为行向量。

#### 依赖关系

当 Pulse shape 为 `Custom` 时，启用此参数。

### **Filter Denominator** — 滤波器分母 `1`（默认） | 行向量

FIR 滤波器分母，指定为行向量。

#### 依赖关系

当 Pulse shape 为 `Custom` 时，启用此参数。

### **Samples per symbol** — 每符号采样数 `4`（默认） | 正偶数

每符号采样数，指定为正偶数。

### 其他参数

### **Rate options** — 处理速率选项 `Enforce single-rate processing`（默认） | `Allow multirate processing`

- `Enforce single-rate processing` — 执行模型，确保输入和输出信号具有相同的端口采样时间。该模块通过使输出相较于输入发生大小变化来实现速率变化。对于整数输入，输出宽度等于 Samples per symbol 乘以符号数。

  有关示例，请参阅 Single-Rate Processing with OQPSK Modulator Block。
- `Allow multirate processing` — 执行模型，允许输入和输出信号具有不同的端口采样时间。输出采样时间等于符号周期除以 Samples per symbol。

  有关示例，请参阅 Multirate Processing with OQPSK Modulator Block。

### **Output data type** — 输出数据类型 `double`（默认） | `single`

选择输出数据类型：`double` 或 `single`。

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

使用 OQPSK 方法进行调制

OQPSK Modulator Baseband 模块使用偏移正交相移键控（OQPSK）方法对输入信号进行调制，并对波形应用脉冲成形滤波。有关详细信息，请参阅 Pulse Shaping Filter。输出是已调制信号的基带表示。

有关调制器-解调器对处理所产生的延迟的信息，请参阅 Modulation Delays。
