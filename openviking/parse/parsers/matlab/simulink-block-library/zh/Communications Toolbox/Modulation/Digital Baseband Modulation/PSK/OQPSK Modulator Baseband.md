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

输入信号根据 **Input type** 所选设置进行处理。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — 输出基带波形 列向量

输出基带波形，返回为复数数据的列向量。
**Output data type** 参数指定输出信号的数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 调制

### **Input type** — 输入类型 `Integer`（默认）| `Bit`

输入类型，指定为 `Integer` 或 `Bit`。

- 当将 **Input type** 设置为 `Integer` 时，输入可以是标量值或列向量，其长度为输入符号的数量。
- 当将 **Input type** 设置为 `Bit` 时，输入宽度必须是二的整数倍。

输出采样周期是输入中每个整数或比特对的周期除以 Samples per symbol。

### **Symbol mapping** — 信号星座图比特映射 `Gray`（默认）| `Binary` | 自定义的 4 元素整数数值向量，取值范围为 0 到 3

信号星座图比特映射，指定为 `Gray`、`Binary` 或自定义的 4 元素整数数值向量，取值范围为 0 到 3。

| 设置 | 整数的星座图映射 | 比特的星座图映射 | 注释 |
| --- | --- | --- | --- |
| `Gray` | 整数顺序 Q1: 0, Q2: 1, Q3: 3, Q4: 2 | 比特顺序 Q1: 00, Q2: 01, Q3: 11, Q4: 10 | 信号星座图映射为格雷编码。 |
| `Binary` | 整数顺序 Q1: 0, Q2: 1, Q3: 2, Q4: 3 | 比特顺序 Q1: 00, Q2: 01, Q3: 10, Q4: 11 | 输入整数 `m`（0 ≤ `m` ≤ 3）的信号星座图映射为复数值 `e(j*(PhaseOffset+π/4) + j*2*π*m/4)`。 |
| 自定义的 4 元素整数数值向量，取值范围为 0 到 3 | 整数顺序 Q1: a, Q2: b, Q3: c, Q4: d | 比特顺序 Q1: a, Q2: b, Q3: c, Q4: d | 元素 [a b c d] 必须由值集合 [0, 1, 2, 3] 以任意顺序组成。 |

### **Phase offset (rad)** — 信号星座图零点相位 `0`（默认）| 标量

相对于 π/4 的相位偏移，指定为以弧度表示的标量。相位偏移在正交分量延迟之前应用于信号星座图的零点。在 OQPSK 虚分量延迟之后，信号以单位功率进行归一化。

**示例：** 将 **Phase offset (rad)** 设置为 `pi/4` 可使 QPSK 信号星座图零点对齐到坐标轴上的点 {(1,0), (0,j), (-1,0), (0,-j)}。

### **View Constellation** — 绘制参考星座图的选项 按钮

点击模块掩码上的 **View Constellation** 可可视化指定模块参数的信号星座图。在查看星座图之前，请应用参数设置。有关详细信息，请参阅 View Constellation of Modulator Block。

**注意**

显示的星座图不描绘 OQPSK 调制器引入的 IQ 延迟。

### 滤波

### **Pulse shape** — 滤波脉冲形状 `Half sine`（默认）| `Normal raised cosine` | `Root raised cosine` | `Custom`

选择滤波脉冲形状：`Half sine`、`Normal raised cosine`、`Root raised cosine` 或 `Custom`。

### **Rolloff factor** — 升余弦滤波器滚降因子 `0.2`（默认）| 标量

升余弦滤波器滚降因子，指定为范围 [`0`, `1`] 内的标量。

#### 依赖关系

当 **Pulse shape** 为 `Normal raised cosine` 或 `Root raised cosine` 时，此属性启用。

### **Filter span (in symbols)** — 滤波器长度 `10`（默认）| 标量

以符号为单位的滤波器长度，指定为标量。理想升余弦滤波器具有无限冲激响应。然而，为了实现此滤波器的实际实现，该对象将冲激响应截断为 **Filter span (in symbols)** 个符号。

#### 依赖关系

当 Pulse shape 为 `Normal raised cosine` 或 `Root raised cosine` 时，此属性启用。

### **Filter numerator** — 滤波器分子 `[0.7071 0.7071]`（默认）| 行向量

FIR 滤波器分子，指定为行向量。

#### 依赖关系

当 Pulse shape 为 `Custom` 时，此参数启用。

### **Filter Denominator** — 滤波器分母 `1`（默认）| 行向量

FIR 滤波器分母，指定为行向量。

#### 依赖关系

当 Pulse shape 为 `Custom` 时，此参数启用。

### **Samples per symbol** — 每个符号的采样数 `4`（默认）| 正偶整数

每个符号的采样数，指定为正偶整数。

### 其他参数

### **Rate options** — 处理速率选项 `Enforce single-rate processing`（默认）| `Allow multirate processing`

- `Enforce single-rate processing`
  — 执行模型，确保输入和输出信号具有相同的端口采样时间。该模块通过在输出端相对于输入端进行大小变化来实现速率变化。对于整数输入，输出宽度等于 Samples per symbol 乘以符号数。

  有关示例，请参阅 Single-Rate Processing with OQPSK Modulator Block。
- `Allow multirate processing`
  — 执行模型，允许输入和输出信号具有不同的端口采样时间。输出采样时间等于符号周期除以 Samples per symbol。

  有关示例，请参阅 Multirate Processing with OQPSK Modulator Block。

### **Output data type** — 输出数据类型 `double`（默认）| `single`

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

OQPSK Modulator Baseband 模块使用偏移正交相移键控（OQPSK）方法对输入信号进行调制，并对波形应用脉冲成形滤波。有关详细信息，请参阅 Pulse Shaping Filter。输出是调制信号的基带表示。

有关调制器-解调器对处理所产生的延迟的信息，请参阅 Modulation Delays。
