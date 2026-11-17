---
type: simulink-block
title: 'Varistor'
family: 'passive'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'varistor'
documentation_source_path: 'ref/varistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Varistor

## 端口

### 守恒

### **+** — 正极端子电气

与压敏电阻正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与压敏电阻负极端子关联的电气守恒端口。

## 参数

### **Parameterization** — Varistor 运行模式 `Linear`（默认）| `Power-law`

选择压敏电阻的电阻随电压增加而变化的方式：

- `Linear` — 两个区域。低电压区域具有高电阻，高电压区域具有低电阻。
- `Power-law` — 三个区域。泄漏区具有高电阻。正常区的电阻呈指数下降。上翘区具有低电阻。

### **Clamping voltage** — 阈值电压 `260`（默认）| 正数

线性压敏电阻的 off 状态和 on 状态之间的转变点电压，*vclamp*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Linear` 时启用。

### **Off resistance** — 低电压电阻 `3e8`（默认）| 正数

压敏电阻在 off 状态下的低电压电阻，*Roff*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Linear` 时启用。

### **On resistance** — 高电压电阻 `1`（默认）| 正数

压敏电阻在 on 状态下的高电压电阻，*Ron*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Linear` 时启用。

### **Leakage to normal voltage transition** — 第一阈值电压 `130`（默认）| 正数

Power-law 压敏电阻的泄漏区和正常区之间的转变点电压，*vLN*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Normal to upturn voltage transition** — 第二阈值电压 `300`（默认）| 正数

Power-law 压敏电阻的正常区和上翘区之间的转变点电压，*vNU*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Leakage-mode resistance** — 低电压电阻 `3e8`（默认）| 正数

压敏电阻在泄漏区中的低电压电阻，*RL*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Normal-mode power-law exponent** — 中电压电阻 `45`（默认）| 正数

确定正常区中压敏电阻电流随电压增加的增加速率的指数。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Upturn-mode resistance** — 高电压电阻 `0.07`（默认）| 正数

压敏电阻在上翘区中的高电压电阻，*RU*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Terminal resistance** — 端子电阻 `100e-6`（默认）| 非负数

与压敏电阻串联的小的恒定电阻。将此值设置为零，以从等效电路中移除该电阻。

### **Capacitance** — 并联电容 `4.4`（默认）| 非负数

与压敏电阻并联的电容器。将此值设置为零，以从等效电路中移除该电容器。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2018a 中引入**

## 描述

电压相关电阻器

Varistor 模块表示电压相关电阻器（VDR）。该组件通常也称为金属氧化物压敏电阻（MOV）。该模块在低电压下呈现高电阻，在高电压下呈现低电阻。

通过将此模块与电路中的某些部分并联，可以保护它们免受高电压浪涌的影响。发生浪涌时，压敏电阻的电阻显著下降，导致电流被分流经过压敏电阻，而不是经过电路。

使用 **Parameterization** 参数在此模块的两种不同行为之间进行选择。`Linear` 选项侧重于压敏电阻的 on 状态和 off 状态，并在两个区域中使用电流和电压之间的线性关系。`Power-law` 选项在初始 on 状态中使用电流和电压之间的指数关系。此选项还在更高电压下添加第三个线性区域。

### Linear 参数化

此参数化选项将电压-电流关系分为两个线性区域：

- off 区 — 电阻高，并且电流随电压增加而缓慢增加。
- on 区 — 电阻低，并且电流随电压增加而快速增加。

此图展示了跨 on 区和 off 区的电压-电流关系。

在以下其中一种场景中使用线性参数化：

- 您正在对接近阈值电压的电压浪涌进行建模
- 您预计您的压敏电阻在所有区域中均呈线性行为

线性压敏电阻的电压-电流关系为：

ivaristor={vvaristorRoff|vvaristor|<vclampvvaristorRon+c1sgn(vvaristor)|vvaristor|≥vclamp.

其中：

- *vvaristor* 和 *ivaristor* 分别是压敏电阻电压和电流。
- *vclamp* 是分隔两个工作区域的阈值电压。使用 **Clamping voltage** 参数设置此值。
- *Ron* 和 *Roff* 是 on 区和 off 区中的电阻。分别使用 **On resistance** 和 **Off resistance** 参数设置这些值。
- *c1* 是用于强制两个区域之间电流连续性的常数：

  c1=vclamp(1Roff−1Ron).

### Power-Law 参数化

此参数化选项将电压-电流关系分为三个区域：

- 泄漏区 — 电阻高，并且电流随电压增加而缓慢增加。
- 正常区 — 电阻随电压增加呈指数下降。
- 上翘区 — 电阻低，并且电流随电压增加而快速增加。

此图以双对数尺度展示了三个工作区域。

在以下其中一种场景中使用幂律参数化：

- 您正在对较大电压范围内的电压浪涌进行建模
- 您预计您的压敏电阻在第一个 on 区中呈指数行为

幂律压敏电阻的电压-电流关系为：

ivaristor={vvaristorRL|vvaristor|<vLNk(vvaristor)α+c1vLN≤|vvaristor|≤vNUvvaristorRU+c2|vvaristor|>vNU

其中：

- *vvaristor* 和 *ivaristor* 分别是压敏电阻电压和电流。
- *α* 是幂律指数，用于确定正常区中电流随电压增加的增加速率。使用 **Normal-mode power-law exponent** 参数设置此值。
- *vLN* 和 *vNU* 是对应于泄漏-正常和正常-上翘转变点的阈值电压。分别使用 **Leakage to normal voltage transition** 和 **Normal to upturn voltage transition** 参数设置这些值。
- *RL* 和 *RU* 是泄漏区和上翘区中的电阻。分别使用 **Leakage-mode resistance** 和 **Upturn-mode resistance** 参数设置这些值。
- *k*、*c1* 和 *c2* 是用于强制区域之间电流连续性的常数：

  k=1αRUvNUα−1,

  c1=vLNRL−vLNααRUvNUα−1,

  以及

  c2=1αRUvNUα−1(vNUα−vLNα)−vNURU+vLNRL.

### 等效电路

除了压敏电阻方程之外，您还可以指定恒定端子电阻 *Rt* 和器件电容 *C*。此图展示了在任一参数化模式下压敏电阻的等效电路。
