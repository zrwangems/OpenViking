---
type: simulink-block
title: 'Chirp'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'chirp'
documentation_source_path: 'ref/chirp.html'
language: zh-CN
chinese_source: worker-translation
---

# Chirp

## 端口

### 输出

### **Port\_1** — 扫频余弦（chirp）信号 标量 | 向量

扫频余弦（chirp）信号。在 `Linear`、`Logarithmic` 和 `Quadratic` 模式下（由 **Frequency sweep** 参数设置），该模块输出扫频余弦，其瞬时频率值由频率和时间参数指定。在 `Swept cosine` 模式下，该模块输出扫频余弦，其瞬时输出频率为线性，可能与频率和时间参数指定的瞬时频率不同。

有关该模块如何计算输出的详细信息，请参阅算法。

**数据类型：** `single` | `double`

## 参数

### **Frequency sweep** — 频率扫描的类型 `Linear`（默认） | `Swept cosine` | `Logarithmic` | `Quadratic`

输出瞬时频率扫描的类型，*fi*(*t*)：`Linear`、`Logarithmic`、`Quadratic` 或 `Swept cosine`。有关详细信息，请参阅频率扫描整形和算法。

#### 限制

当需要线性扫频 chirp 信号时，建议使用 `Linear` 频率扫描。尽管 `Swept cosine` 频率扫描也会产生线性扫频 chirp 信号，但输出可能包含意外的频率成分。

- 在 **Target time** 处的 swept cosine 扫描值不一定是 **Target frequency**。这是因为用户指定的扫描不是 swept cosine 输出的实际频率扫描，如扫频余弦频率扫描的输出计算方法中所述。有关在 **Target time** 处 swept cosine 扫描的实际值，请参见瞬时频率扫描值表。
- 在 **Swept cosine** 模式下，不要将参数设置为使 1/*T*sw 远大于 **Initial frequency** 和 **Target frequency** 参数的值。在这种情况下，swept cosine 扫描的实际频率成分可能更接近 1/*T*sw，远超 **Initial frequency** 和 **Target frequency** 参数值。

### **Sweep mode** — 扫描模式 `Unidirectional`（默认） | `Bidirectional`

**Sweep mode** 参数决定扫描是单向还是双向，这会影响输出频率扫描的形状（请参阅频率扫描整形）。下表描述了单向和双向扫描的特性。

| Sweep mode 参数设置 | 扫描特性 |
| --- | --- |
| `Unidirectional` | - 持续一个 **Sweep time**，*Tsw* - 每 *Tsw* 重复一次 |
| `Bidirectional` | - 持续两倍的 **Sweep time**，2*Tsw* - 每 2*Tsw* 重复一次 - 前半部分与其单向对应部分相同。 - 后半部分是前半部分的镜像。 |

下图说明了两种扫描模式下的线性扫描。有关设置扫描中频率值的信息，请参阅设置瞬时频率扫描值。

### **Initial frequency (Hz)** — 初始频率 `1000`（默认） | 标量

对于 `Linear`、`Quadratic` 和 `Swept cosine` 扫描，*f*0 是输出 chirp 信号的初始频率。你可以将 **Initial frequency (Hz)** 指定为大于或等于零的标量。对于 `Logarithmic` 扫描，**Initial frequency** 比扫描的实际初始频率小 1。此外，当扫描为 `Logarithmic` 时，必须将 **Initial frequency** 设置为小于 **Target frequency**。

有关详细信息，请参阅设置瞬时频率扫描值。

**可调：** Yes

### **Target frequency (Hz)** — 目标频率 `4000`（默认） | 标量

对于 `Linear`、`Quadratic` 和 `Logarithmic` 扫描，*fi*(*tg*) 是在 **Target time** *tg* 处输出的瞬时频率。你可以将 **Target frequency (Hz)** 指定为大于或等于零的标量。对于 `Swept cosine` 扫描，**Target frequency** 是在 **Target time** 的一半处（*tg*/2）输出的瞬时频率。当 **Frequency sweep** 为 `Logarithmic` 时，必须将 **Target frequency** 设置为大于 **Initial frequency**。

有关详细信息，请参阅设置瞬时频率扫描值。

**可调：** Yes

### **Target time (s)** — 扫描的目标时间 `1`（默认） | 标量

对于 `Linear`、`Quadratic` 和 `Logarithmic` 扫描，*tg* 是扫描达到 **Target frequency** *fi*(*tg*) 的时间。对于 `Swept cosine` 扫描，**Target time** 是扫描达到 2*fi*(*tg*) - *f0* 的时间。**Target time** 必须为大于或等于零且小于或等于 **Sweep time** 的标量，Tsw≥tg。

有关详细信息，请参阅设置瞬时频率扫描值。

**可调：** Yes

### **Sweep time (s)** — 扫描时间 `1`（默认） | 标量

在 `Unidirectional` **Sweep mode** 下，**Sweep time** *Tsw* 是输出频率扫描的周期。在 `Bidirectional` **Sweep mode** 下，**Sweep time** 是输出频率扫描周期的一半。**Sweep time** 必须为大于或等于 **Target time** 的标量，Tsw≥tg。

**可调：** Yes

### **Initial phase (rad)** — 余弦输出的初始相位 `0`（默认） | 标量

余弦输出在 *t*=0 处的相位 ϕ0；ychirp(t)=cos(ϕ0)。你可以将 **Initial phase (rad)** 指定为大于或等于零的标量。

**可调：** Yes

### **Sample time** — 输出采样周期 `1/8000`（默认） | 正标量

输出的采样周期 *Ts*。输出帧周期为 *Mo**Ts*，其中 *Mo* 是每帧的样本数。

### **Samples per frame** — 每帧样本数 `1`（默认） | 正整数

要缓冲到每个输出帧中的样本数 *Mo*，指定为正整数标量。

### **Output data type** — 输出数据类型 `Double`（默认） | `Single`

输出的数据类型，指定为 single precision 或 double precision。

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

Chirp 模块输出具有单位幅值和连续相位的扫频余弦（chirp）信号。要指定所需的输出 chirp 信号，必须定义其瞬时频率函数，也称为输出频率扫描。频率扫描可以是线性的、二次的或对数的，并且默认每 **Sweep time** 重复一次。有关 Chirp 模块所用算法的说明，请参阅算法。
