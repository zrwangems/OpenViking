---
type: simulink-block
title: 'Sinusoid'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Sources'
documentation_page: 'sinusoid'
documentation_source_path: 'ref/sinusoid.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoid

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Source type
  summary: 波形类型 Ideal voltage（默认）| Ideal current
  group: ''
- name: Offset in-phase
  summary: 同相偏移 0 V（默认）| 0 A | 实数或复数向量 | V | mV | kV | A | mA | uA | kA
  group: ''
- name: Offset quadrature
  summary: 正交偏移 0 V（默认）| 0 A | 实数或复数向量 | V | mV | kV | A | mA | uA | kA
  group: ''
- name: Sinusoidal amplitude in-phase
  summary: 同相幅度 0（默认）| 实数或复数向量 | V | mV | kV | A | mA | uA | kA
  group: ''
- name: Sinusoidal amplitude quadrature
  summary: 正交幅度 0（默认）| 实数或复数向量 | V | mV | kV | A | mA | uA | kA
  group: ''
- name: Sinusoidal modulation frequency
  summary: 调制频率 0（默认）| 实数或复数向量 | Hz | kHz | MHz | GHz
  group: ''
- name: Time delay
  summary: 调制的时间延迟 0（默认）| 实数向量 | s | ms | us | ns
  group: ''
- name: Carrier frequencies
  summary: 载波频率 0（默认）| 正实数向量 | Hz | kHz | MHz | GHz
  group: ''
- name: Ground and hide negative terminals
  summary: 接地 RF 电路端子 on（默认）| off
  group: ''
```

### **Source type** — 波形类型 `Ideal voltage`（默认）| `Ideal current`

波形类型，指定为：

- `Ideal Voltage` —
  该模块在指定的 **Carrier frequencies** 处仿真电压包络 *v*(*t*)。
- `Ideal Current` —
  该模块在指定的 **Carrier frequencies** 处仿真电流包络 *i*(*t*)。

### **Offset in-phase** — 同相偏移 `0 V`（默认）| `0 A` | 实数或复数向量 | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

每个 RF 电路载波频率的同相偏移，指定为实数或复数向量。从相应的下拉列表指定单位。对于 `Ideal Voltage`，单位为伏特；对于 `Ideal Current`，单位为安培。

### **Offset quadrature** — 正交偏移 `0 V`（默认）| `0 A` | 实数或复数向量 | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

每个 RF 电路载波频率的正交偏移，指定为实数或复数向量。从相应的下拉列表指定单位。对于 `Ideal Voltage`，单位为伏特；对于 `Ideal Current`，单位为安培。

### **Sinusoidal amplitude in-phase** — 同相幅度 `0`（默认）| 实数或复数向量 | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

同相幅度，指定为实数向量或复数。从相应的下拉列表指定单位。对于 `Ideal Voltage`，单位为伏特；对于 `Ideal Current`，单位为安培。

### **Sinusoidal amplitude quadrature** — 正交幅度 `0`（默认）| 实数或复数向量 | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

正交幅度，指定为实数向量或复数。从相应的下拉列表指定单位。对于 `Ideal Voltage`，单位为伏特；对于 `Ideal Current`，单位为安培。

### **Sinusoidal modulation frequency** — 调制频率 `0`（默认）| 实数或复数向量 | `Hz` | `kHz` | `MHz` | `GHz`

每个 RF 电路载波频率处的调制频率，指定为实数向量或复数。从相应的下拉列表指定单位。Th

### **Time delay** — 调制的时间延迟 `0`（默认）| 实数向量 | `s` | `ms` | `us` | `ns`

调制的时间延迟，指定为正数向量。从相应的下拉列表指定单位。

### **Carrier frequencies** — 载波频率 `0`（默认）| 正实数向量 | `Hz` | `kHz` | `MHz` | `GHz`

载波频率，指定为正实数向量。载波频率中的元素是 Configuration 模块中基频音及其对应谐波的组合。默认值为 `0` `Hz`。

### **Ground and hide negative terminals** — 接地 RF 电路端子 `on`（默认）| `off`

选择此参数以将负端子接地并隐藏。要暴露负端子，请清除该参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。
## 所属库

RF Blockset / Circuit Envelope / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2021b：Sinusoid 模块图标已更新

从 R2021b 开始，Sinusoid 模块图标现已更新。当您打开在 R2021b 之前创建的包含 Sinusoid 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对直流偏移和正弦调制进行建模

Sinusoid 模块实现一个提供直流偏移和正弦波调制的电压源或电流源。该模块可与电路包络环境中列出的每个模块载波配合使用。

该模块为第 *k* 个所列模块载波的同相（*ui*）和正交（*uq*）分量实现以下电压（或电流）关系：

uk,i(t)=Di+Aisin(wk(t−τ))uk,q(t)=Dq+Aqsin(wk(t−τ))

其中：

- *Di* 和 *Dq* 是直流偏移。
- *Ai* 和 *Aq* 是同相和正交幅度。
- *τ* 是时间延迟。
- *ωk* 是给定载波频率 *fk* 下指定的调制频率。
- *t* 是时间。

**注意**

Sinusoid 模块不支持基于帧的处理（由 Configuration 模块支持），因为它使用 SL Sine wave 模块。如果配置模块中的 **Samples per frame** 大于 1，该模块将报错。

Sinusoid 模块的掩码图标是动态的，并显示当前的源类型。下表显示了该模块上的图标如何根据您在模块的 **Source type** 参数上设置的源类型而变化。

| Source type: `Ideal voltage` | Source type: `Ideal current` |
| --- | --- |
| Source type 设置为 Ideal voltage 时的 Sinusoid 模块图标。 | Source type 设置为 Ideal current 时的 Sinusoid 模块图标。 |
