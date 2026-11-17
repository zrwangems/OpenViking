---
type: simulink-block
title: 'SPST Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spstswitch'
documentation_source_path: 'ref/spstswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# SPST Switch

## 端口
```yaml
ports:
- name: vT
  summary: 开关控制端口物理信号
  direction: input
- name: p
  summary: 电气端口 electrical
  direction: input
- name: n
  summary: 电气端口 electrical
  direction: input
- name: +
  summary: 电气端口 electrical
  direction: input
- name: '-'
  summary: 电气端口 electrical
  direction: input
```

### 输入

### **vT** — 开关控制端口物理信号

与打开和关闭开关的信号相关联的物理端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `PS control port`。
### 守恒

### **p** — 电气端口 electrical

电气守恒端口。

### **n** — 电气端口 electrical

电气守恒端口。

### **+** — 电气端口 electrical

与打开和关闭开关相关的正电压的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

### **-** — 电气端口 electrical

与打开和关闭开关相关的负电压的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 指定物理控制端口还是电气控制端口 PS control port（默认）| Electrical control port
  group: ''
- name: Closed resistance
  summary: 闭合电阻 0.01 Ohm（默认）| 正标量
  group: 主要
- name: Open conductance
  summary: 断开电导 1e-6 S（默认）| 正标量
  group: 主要
- name: Threshold
  summary: 阈值电压 0.5 V（默认）
  group: 主要
- name: Threshold width
  summary: 阈值宽度 0 V（默认）
  group: 主要
- name: Model dynamics
  summary: 模型动态特性 No dynamics（默认）| Model turn-on and turn-off times
  group: 动态特性
- name: Turn-on delay
  summary: 导通延迟 1e-3（默认）| 正标量
  group: 动态特性
- name: Turn-off delay
  summary: 关断延迟 1e-3（默认）| 正标量
  group: 动态特性
- name: Initial input value, vT
  summary: 初始输入值，*vT* 0（默认）
  group: 动态特性
```

### **Modeling option** — 指定物理控制端口还是电气控制端口 `PS control port`（默认）| `Electrical control port`

指定开关栅极使用物理控制端口还是电气控制端口。

### 主要

### **Closed resistance** — 闭合电阻 `0.01` `Ohm`（默认）| 正标量

开关闭合时 **p** 端口与 **n** 端口之间的电阻。该值必须大于零。

### **Open conductance** — 断开电导 `1e-6` `S`（默认）| 正标量

开关断开时 **p** 端口与 **n** 端口之间的电导。该值必须大于零。

### **Threshold** — 阈值电压 `0.5` `V`（默认）

使开关导通的阈值电压。

### **Threshold width** — 阈值宽度 `0` `V`（默认）

使开关从完全断开变为完全闭合所需的高于阈值电压的最小电压增量。

### 动态特性

### **Model dynamics** — 模型动态特性 `No dynamics`（默认）| `Model turn-on and turn-off times`

选择模块是否对开关延迟进行建模：

- `No dynamics`
  — 不对延迟进行建模。这是默认选项。
- `模型开启和关闭`
  times` — 使用附加参数对 **vT** 或 **+** 和 **-**
  处的电压超过阈值到开关打开或闭合之间的延迟进行建模。

### **Turn-on delay** — 导通延迟 `1e-3`（默认）| 正标量

输入电压超过阈值电压到开关闭合之间的时间。该值必须大于零。

#### 依赖关系

仅当为 **Model dynamics** 参数选择 `Model turn-on and turn-off
times` 时，此参数才可见。

### **Turn-off delay** — 关断延迟 `1e-3`（默认）| 正标量

输入电压降至阈值电压以下到开关打开之间的时间。该值必须大于零。

#### 依赖关系

仅当为 **Model dynamics** 参数选择 `Model turn-on and turn-off
times` 时，此参数才可见。

### **Initial input value, vT** — 初始输入值，*vT* `0`（默认）

物理信号输入 *vT* 在零时刻的值。此值用于在内部初始化延迟控制电压参数。

#### 依赖关系

仅当为 **Model dynamics** 参数选择 `Model turn-on and turn-off
times` 时，此参数才可见。
## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

单刀单掷开关

SPST Switch 模块对单刀单掷开关进行建模：

- 当开关断开时，端口 **p** 通过一个电阻连接到端口 **n**，该电阻的值等于 **Open conductance** 参数值的倒数。
- 当开关闭合时，端口 **p** 通过一个电阻连接到端口 **n**，该电阻的值等于 **Closed resistance** 参数值。

如果 **Threshold width** 参数设置为零，则当 **vT** 控制端口处呈现的电压超过 **Threshold** 参数的值时，开关闭合。

如果 **Threshold width** 参数大于零，则开关电导 *G* 在断态值和通态值之间平滑变化：

G=xRclosed+(1−x)Gopen

λ=vT−ThresholdThreshold width

x={0for λ≤03λ2−2λ3for 0<λ<11for λ≥1

该模块使用函数 3*λ*2 –
2*λ*3，因为其导数在 *λ* =
0 和 *λ* =
1 处为零。

定义较小的正 **Threshold width** 在某些模型中可以帮助求解器收敛，特别是当控制端口信号 *vT* 作为其他网络变量的函数连续变化时。然而，定义非零阈值宽度会阻止求解器利用切换线性优化。因此，如果网络的其余部分是切换线性的，请将 **Threshold width** 设置为零。

可选地，您可以在 **vT** 处的电压超过阈值到开关打开或闭合之间添加延迟。要启用延迟，请在 **Dynamics** 选项卡上，将 **Model dynamics** 参数设置为 `Model
turn-on and turn-off times`。

### 模型栅极控制端口

您可以使用物理信号端口或电气守恒端口来控制开关栅极。要选择栅极控制端口，请将 **Modeling option** 参数设置为以下之一：

- `PS control port` — 模块包含与阈值电压相关联的物理信号端口。
- `Electrical control port` — 模块包含与阈值电压相关联的电气守恒端口。
