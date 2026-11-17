---
type: simulink-block
title: 'Chirp'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'chirp'
documentation_source_path: 'ref/chirp.html'
language: zh-CN
chinese_source: worker-translation
---

# Chirp

## 端口
```yaml
ports:
- name: Port_1
  summary: 扫频余弦（chirp）信号 标量 | 向量
  direction: output
  data_types: single | double
```

### 输出

### **Port\_1** — 扫频余弦（chirp）信号 标量 | 向量

扫频余弦（chirp）信号。在 `Linear`、`Logarithmic` 和 `Quadratic` 模式（由 **Frequency sweep** 参数设置）下，该模块输出一个扫频余弦信号，其瞬时频率值由频率和时间参数指定。在 `Swept cosine` 模式下，该模块输出一个扫频余弦信号，其瞬时输出频率为线性，可能与频率和时间参数指定的频率不同。

有关该模块如何计算输出的详细信息，请参阅算法。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Frequency sweep
  summary: 频率扫描类型 Linear（默认）| Swept cosine | Logarithmic | Quadratic
  group: ''
- name: Sweep mode
  summary: 扫描模式 Unidirectional（默认）| Bidirectional
  group: ''
- name: Initial frequency (Hz)
  summary: 初始频率 1000（默认）| 标量
  group: ''
- name: Target frequency (Hz)
  summary: 目标频率 4000（默认）| 标量
  group: ''
- name: Target time (s)
  summary: 扫描的目标时间 1（默认）| 标量
  group: ''
- name: Sweep time (s)
  summary: 扫描时间 1（默认）| 标量
  group: ''
- name: Initial phase (rad)
  summary: 余弦输出的初始相位 0（默认）| 标量
  group: ''
- name: Sample time
  summary: 输出采样周期 1/8000（默认）| 正标量
  group: ''
- name: Samples per frame
  summary: 每帧采样数 1（默认）| 正整数
  group: ''
- name: Output data type
  summary: 输出数据类型 Double（默认）| Single
  group: ''
```

### **Frequency sweep** — 频率扫描类型 `Linear`（默认）| `Swept cosine` | `Logarithmic` | `Quadratic`

输出瞬时频率扫描的类型，
*fi*(*t*)：
`Linear`、
`Logarithmic`、
`Quadratic` 或 `Swept
cosine`。有关详细信息，请参阅塑造频率扫描和算法。

#### 限制

当您需要线性扫频 chirp 信号时，我们建议您使用
`Linear` 频率扫描。尽管
`Swept cosine` 频率扫描也会产生线性扫频 chirp 信号，但输出可能包含意外的频率成分。

- 在 **Target
  time** 处的扫频余弦扫描值不一定是 **Target
  frequency**。这是因为用户指定的扫描不是扫频余弦输出的实际频率扫描，如扫频余弦频率扫描的输出计算方法中所述。有关 **Target
  time** 处扫频余弦扫描的实际值，请参阅瞬时频率扫描值表。
- 在 **Swept cosine** 模式下，不要将参数设置为使
  1/*T*sw 远大于 **Initial
  frequency** 和 **Target
  frequency** 参数的值。在这种情况下，扫频余弦扫描的实际频率成分可能更接近
  1/*T*sw，远超 **Initial frequency** 和
  **Target frequency** 参数值。

### **Sweep mode** — 扫描模式 `Unidirectional`（默认）| `Bidirectional`

**Sweep mode** 参数决定您的扫描是单向还是双向，这会影响输出频率扫描的形状（请参阅塑造频率扫描）。下表描述了单向和双向扫描的特性。

| 扫描模式参数设置 | 扫描特性 |
| --- | --- |
| `Unidirectional` | - 持续一个 **Sweep time**，   *Tsw* - 每   *Tsw* 重复一次 |
| `Bidirectional` | - 持续两倍的 **Sweep   time**，   2*Tsw* - 每   2*Tsw* 重复一次 - 前半部分与其单向对应部分相同。 - 后半部分是前半部分的镜像。 |

下图说明了两种扫描模式下的线性扫描。有关设置扫描中频率值的信息，请参阅设置瞬时频率扫描值。

### **Initial frequency (Hz)** — 初始频率 `1000`（默认）| 标量

对于 `Linear`、
`Quadratic` 和 `Swept
cosine` 扫描，输出 chirp 信号的初始频率，
*f*0。您可以将 **Initial frequency (Hz)** 指定为大于或等于零的标量。对于
`Logarithmic` 扫描，**Initial
frequency** 比扫描的实际初始频率小一。此外，当扫描为 `Logarithmic` 时，
您必须将 **Initial frequency** 设置为小于
**Target frequency**。

有关详细信息，请参阅设置瞬时频率扫描值。

**可调：** 是

### **Target frequency (Hz)** — 目标频率 `4000`（默认）| 标量

对于 `Linear`、
`Quadratic` 和
`Logarithmic` 扫描，输出在 **Target time**，
*tg* 处的瞬时频率，
*fi*(*tg*)。
您可以将
**Target frequency (Hz)** 指定为大于或等于零的标量。对于 `Swept cosine` 扫描，
**Target frequency** 是输出在 **Target time** 一半处，
*tg*/2 的瞬时频率。当
**Frequency sweep** 为
`Logarithmic` 时，您必须将
**Target frequency** 设置为大于
**Initial frequency**。

有关详细信息，请参阅设置瞬时频率扫描值。

**可调：** 是

### **Target time (s)** — 扫描的目标时间 `1`（默认）| 标量

对于 `Linear`、`Quadratic` 和
`Logarithmic` 扫描，扫描达到 **Target frequency**，
*fi*(*tg*) 的时间，
*tg*。
对于 `Swept cosine` 扫描，**Target
time** 是扫描达到
2*fi*(*tg*)
- *f0* 的时间。**Target
time** 必须是大于或等于零的标量，
且小于或等于 **Sweep time**，Tsw≥tg。

有关详细信息，请参阅设置瞬时频率扫描值。

**可调：** 是

### **Sweep time (s)** — 扫描时间 `1`（默认）| 标量

在 `Unidirectional` **Sweep
mode** 中，**Sweep time**，
*Tsw*，是输出频率扫描的周期。在
`Bidirectional` **Sweep
mode** 中，**Sweep time** 是输出频率扫描周期的一半。**Sweep time** 必须是大于或等于 **Target time** 的标量，Tsw≥tg。

**可调：** 是

### **Initial phase (rad)** — 余弦输出的初始相位 `0`（默认）| 标量

余弦输出在 *t*=0 处的相位，ϕ0；ychirp(t)=cos(ϕ0)。您可以将 **Initial phase
(rad)** 指定为大于或等于零的标量。

**可调：** 是

### **Sample time** — 输出采样周期 `1/8000`（默认）| 正标量

输出的采样周期，*Ts*。输出帧周期为
*Mo**Ts*，
其中 *Mo* 是每帧的采样数。

### **Samples per frame** — 每帧采样数 `1`（默认）| 正整数

要缓冲到每个输出帧中的采样数，*Mo*，
指定为正整数标量。

### **Output data type** — 输出数据类型 `Double`（默认）| `Single`

输出的数据类型，指定为单精度或双精度。
## 所属库

DSP System Toolbox / Sources

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

## 版本历史

**在 R2006a 之前引入**

## 描述

生成扫频余弦（chirp）信号

Chirp 模块输出一个幅度为单位值、相位连续的扫频余弦（chirp）信号。要指定所需的输出 chirp 信号，您必须定义其瞬时频率函数，也称为输出频率扫描。频率扫描可以是线性的、二次的或对数的，并且默认情况下每 **Sweep time** 重复一次。有关 Chirp 模块所用算法的描述，请参阅算法。
