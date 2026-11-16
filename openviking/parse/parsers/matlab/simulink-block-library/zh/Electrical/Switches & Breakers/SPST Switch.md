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

### 输入

### **vT** — 开关控制端口物理信号

与使开关断开和闭合的信号关联的物理端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `PS control port`。
### 守恒

### **p** — 电气端口 electrical

电气守恒端口。

### **n** — 电气端口 electrical

电气守恒端口。

### **+** — 电气端口 electrical

与断开和闭合开关关联的正电压的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

### **-** — 电气端口 electrical

与断开和闭合开关关联的负电压的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

## 参数

### **Modeling option** — 指定物理控制端口还是电气控制端口 `PS control port` (默认) | `Electrical control port`

为开关门极指定物理控制端口还是电气控制端口。

### 主要

### **Closed resistance** — 闭合电阻 `0.01` `Ohm` (默认) | 正标量

当开关闭合时，**p** 端口与 **n** 端口之间的电阻。该值必须大于零。

### **Open conductance** — 断开电导 `1e-6` `S` (默认) | 正标量

当开关断开时，**p** 端口与 **n** 端口之间的电导。该值必须大于零。

### **Threshold** — 阈值电压 `0.5` `V` (默认)

阈值电压，超过该电压时开关将导通。

### **Threshold width** — 阈值宽度 `0` `V` (默认)

高于阈值电压且将使开关从完全断开变为完全闭合的最小电压增量。

### 动态

### **Model dynamics** — 模型动态 `No dynamics` (默认) | `Model turn-on and turn-off times`

选择该模块是否对开关延迟建模：

- `No dynamics` — 不对延迟建模。这是默认选项。
- `Model turn-on and turn-off times` — 使用附加参数对 **vT** 处或 **+** 与 **-** 处的电压越过阈值的时刻与开关断开或闭合之间的延迟建模。

### **Turn-on delay** — 导通延迟 `1e-3` (默认) | 正标量

输入电压超过阈值电压与开关闭合之间的时间。该值必须大于零。

#### 依赖关系

仅当你为 **Model dynamics** 参数选择 `Model turn-on and turn-off times` 时，此参数才可见。

### **Turn-off delay** — 关断延迟 `1e-3` (默认) | 正标量

输入电压降至阈值电压以下与开关断开之间的时间。该值必须大于零。

#### 依赖关系

仅当你为 **Model dynamics** 参数选择 `Model turn-on and turn-off times` 时，此参数才可见。

### **Initial input value, vT** — 初始输入值，*vT* `0` (默认)

零时刻时物理信号输入 *vT* 的值。此值用于在内部初始化延迟控制电压参数。

#### 依赖关系

仅当你为 **Model dynamics** 参数选择 `Model turn-on and turn-off times` 时，此参数才可见。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

单刀单掷开关

SPST Switch 模块对单刀单掷开关建模：

- 当开关断开时，端口 **p** 通过一个电阻连接到端口 **n**，其电阻值等于 **Open conductance** 参数值的倒数。
- 当开关闭合时，端口 **p** 通过一个电阻连接到端口 **n**，其电阻值等于 **Closed resistance** 参数值。

如果 **Threshold width** 参数设置为零，则当呈现于 **vT** 控制端口的电压超过 **Threshold** 参数值时，开关闭合。

如果 **Threshold width** 参数大于零，则开关电导 *G* 在断态和通态值之间平滑变化：

G=xRclosed+(1−x)Gopen

λ=vT−ThresholdThreshold width

x={0for λ≤03λ2−2λ3for 0<λ<11for λ≥1

该模块使用函数 3*λ*2 – 2*λ*3，因为其导数在 *λ* = 0 和 *λ* = 1 时为零。

定义小的正 **Threshold width** 有助于某些模型中的求解器收敛，特别是如果控制端口信号 *vT* 作为其他网络变量的函数连续变化。然而，定义非零阈值宽度会阻止求解器利用开关线性优化。因此，如果你网络的其余部分是开关线性，请将 **Threshold width** 设置为零。

可选地，你可以在 **vT** 处电压越过阈值的点与开关断开或闭合之间添加延迟。要启用延迟，请在 **Dynamics** 选项卡上，将 **Model dynamics** 参数设置为 `Model turn-on and turn-off times`。

### 门极控制端口建模

你可以通过使用物理信号端口或电气守恒端口来控制开关门极。要选择门极控制端口，请将 **Modeling option** 参数设置为以下之一：

- `PS control port` — 该模块包含一个与阈值电压关联的物理信号端口。
- `Electrical control port` — 该模块包含与阈值电压关联的电气守恒端口。
