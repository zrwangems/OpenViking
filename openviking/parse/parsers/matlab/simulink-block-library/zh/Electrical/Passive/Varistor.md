---
type: simulink-block
title: 'Varistor'
family: 'sps'
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
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与 varistor 正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与 varistor 负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: Varistor 工作模式 Linear（默认）| Power-law
  group: ''
- name: Clamping voltage
  summary: 阈值电压 260（默认）| 正数
  group: ''
- name: Off resistance
  summary: 低压电阻 3e8（默认）| 正数
  group: ''
- name: On resistance
  summary: 高压电阻 1（默认）| 正数
  group: ''
- name: Leakage to normal voltage transition
  summary: 第一阈值电压 130（默认）| 正数
  group: ''
- name: Normal to upturn voltage transition
  summary: 第二阈值电压 300（默认）| 正数
  group: ''
- name: Leakage-mode resistance
  summary: 低压电阻 3e8（默认）| 正数
  group: ''
- name: Normal-mode power-law exponent
  summary: 中压电阻 45（默认）| 正数
  group: ''
- name: Upturn-mode resistance
  summary: 高压电阻 0.07（默认）| 正数
  group: ''
- name: Terminal resistance
  summary: 端子电阻 100e-6（默认）| 非负数
  group: ''
- name: Capacitance
  summary: 并联电容 4.4（默认）| 非负数
  group: ''
```

### **Parameterization** — Varistor 工作模式 `Linear`（默认）| `Power-law`

选择 varistor 电阻随电压增加而变化的方式：

- `Linear` — 两个区域。低压区域具有高电阻，高压区域具有低电阻。
- `Power-law` — 三个区域。泄漏区域具有高电阻。正常区域具有指数下降的电阻。上翘区域具有低电阻。

### **Clamping voltage** — 阈值电压 `260`（默认）| 正数

线性 varistor 在关断状态和导通状态之间的过渡点电压 *vclamp*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Linear` 时启用。

### **Off resistance** — 低压电阻 `3e8`（默认）| 正数

varistor 在关断状态下的低压电阻 *Roff*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Linear` 时启用。

### **On resistance** — 高压电阻 `1`（默认）| 正数

varistor 在导通状态下的高压电阻 *Ron*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Linear` 时启用。

### **Leakage to normal voltage transition** — 第一阈值电压 `130`（默认）| 正数

功率律 varistor 的泄漏区域和正常区域之间的过渡点电压 *vLN*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Normal to upturn voltage transition** — 第二阈值电压 `300`（默认）| 正数

功率律 varistor 的正常区域和上翘区域之间的过渡点电压 *vNU*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Leakage-mode resistance** — 低压电阻 `3e8`（默认）| 正数

varistor 在泄漏区域中的低压电阻 *RL*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Normal-mode power-law exponent** — 中压电阻 `45`（默认）| 正数

决定 varistor 在正常区域中电流随电压增加而增加的速率的指数。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Upturn-mode resistance** — 高压电阻 `0.07`（默认）| 正数

varistor 在上翘区域中的高压电阻 *RU*。

#### 依赖关系

当 **Parameterization** 参数设置为 `Power-law` 时启用。

### **Terminal resistance** — 端子电阻 `100e-6`（默认）| 非负数

与 varistor 串联的小恒定电阻。将此值设置为零以从等效电路中移除该电阻。

### **Capacitance** — 并联电容 `4.4`（默认）| 非负数

与 varistor 并联的电容器。将此值设置为零以从等效电路中移除该电容器。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

电压相关电阻器

Varistor 模块表示电压相关电阻器（VDR）。该组件通常也称为金属氧化物 varistor（MOV）。该模块在低电压下呈现高电阻，在高电压下呈现低电阻。

通过将此模块与电路的一部分并联，可以保护它们免受高压浪涌的影响。当发生浪涌时，varistor 的电阻显著下降，使电流被分流通过 varistor，而不是通过电路。

使用 **Parameterization** 参数在此模块的两种不同行为之间进行选择。`Linear` 选项关注 varistor 的导通和关断状态，并在两个区域中使用电流和电压之间的线性关系。`Power-law` 选项在初始导通状态下使用电流和电压之间的指数关系。此选项还在更高电压下增加了第三个线性区域。

### 线性参数化

此参数化选项将电压-电流关系分为两个线性区域：

- 关断区域 — 电阻高，电流随电压增加而缓慢增加。
- 导通区域 — 电阻低，电流随电压增加而快速增加。

此图显示了导通和关断区域上的电压-电流关系。

在以下场景之一中使用线性参数化：

- 您正在对接近阈值电压的电压浪涌进行建模
- 您期望 varistor 在所有区域中均表现为线性

线性 varistor 的电压-电流关系为：

ivaristor={vvaristorRoff|vvaristor|<vclampvvaristorRon+c1sgn(vvaristor)|vvaristor|≥vclamp.

其中：

- *vvaristor* 和 *ivaristor* 分别是 varistor 电压和电流。
- *vclamp* 是分隔两个工作区域的阈值电压。使用 **Clamping voltage** 参数设置此值。
- *Ron* 和 *Roff* 分别是导通和关断区域中的电阻。分别使用 **On resistance** 和 **Off resistance** 设置这些值。
- *c1* 是用于强制两个区域之间电流连续性的常数：

  c1=vclamp(1Roff−1Ron).

### 功率律参数化

此参数化选项将电压-电流关系分为三个区域：

- 泄漏区域 — 电阻高，电流随电压增加而缓慢增加。
- 正常区域 — 电阻随电压增加而指数下降。
- 上翘区域 — 电阻低，电流随电压增加而快速增加。

此图显示了双对数尺度下的三个工作区域。

在以下场景之一中使用功率律参数化：

- 您正在对大范围电压下的电压浪涌进行建模
- 您期望 varistor 在第一个导通区域中表现为指数关系

功率律 varistor 的电压-电流关系为：

ivaristor={vvaristorRL|vvaristor|<vLNk(vvaristor)α+c1vLN≤|vvaristor|≤vNUvvaristorRU+c2|vvaristor|>vNU

其中：

- *vvaristor* 和 *ivaristor* 分别是 varistor 电压和电流。
- *α* 是功率律指数，它决定正常区域中电流随电压增加而增加的速率。使用 **Normal-mode power-law exponent** 参数设置此值。
- *vLN* 和 *vNU* 是对应于泄漏-正常和正常-上翘过渡点的阈值电压。分别使用 **Leakage to normal voltage transition** 和 **Normal to upturn voltage transition** 参数设置这些值。
- *RL* 和 *RU* 分别是泄漏区域和上翘区域中的电阻。分别使用 **Leakage-mode resistance** 和 **Upturn-mode resistance** 参数设置这些值。
- *k*、*c1* 和 *c2* 是用于强制区域之间电流连续性的常数：

  k=1αRUvNUα−1,

  c1=vLNRL−vLNααRUvNUα−1,

  以及

  c2=1αRUvNUα−1(vNUα−vLNα)−vNURU+vLNRL.

### 等效电路

除了 varistor 方程之外，您还可以指定恒定端子电阻 *Rt* 和器件电容 *C*。此图显示了任一参数化模式下 varistor 的等效电路。
