---
type: simulink-block
title: 'SPDT Switch'
family: 'switches-breakers'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spdtswitch'
documentation_source_path: 'ref/spdtswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# SPDT Switch

## 端口

### 输入

### **vT** — 开关控制端口 physical signal

与打开和关闭开关的信号相关联的物理端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `PS control port`。
### 守恒

### **p** — Electrical port electrical

电气守恒端口。

### **n1** — Electrical port electrical

电气守恒端口。

### **n2** — Electrical port electrical

电气守恒端口。

### **+** — Electrical port electrical

与打开和关闭开关相关的正电压的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

### **-** — Electrical port electrical

与打开和关闭开关相关的负电压的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

## 参数

### **Modeling option** — 指定物理还是电气控制端口 `PS control port`（默认）| `Electrical control port`

指定开关门控的物理或电气控制端口。

### 主要

### **Closed resistance** — Closed resistance `0.01` `Ohm`（默认）| positive scalar

当开关闭合时，**p** 端口与 **n1** 和 **n2** 端口之间的电阻。值必须大于零。

### **Open conductance** — Open conductance `1e-6` `S`（默认）| positive scalar

当开关断开时，**p** 端口与 **n1** 和 **n2** 端口之间的电导。值必须大于零。

### **Threshold** — 阈值电压 `0.5` `V`（默认）

开关将接通的阈值电压。

### **Threshold width** — Threshold width `0` `V`（默认）

高于阈值电压的最小电压增量，该增量将使开关从完全断开移动到完全闭合。

### 动态

### **Model dynamics** — Model dynamics `No dynamics`（默认）| `Model turn-on and turn-off times`

选择模块是否对开关延迟建模：

- `No dynamics`
  — 不对延迟建模。这是默认选项。
- `Model turn-on and turn-off times` — 使用附加参数对电压在 **vT** 或 **+** 和 **-** 处通过阈值与开关打开或闭合之间的延迟进行建模。

### **Turn-on delay** — Turn-on delay `1e-3`（默认）| positive scalar

输入电压超过阈值电压与开关闭合之间的时间。值必须大于零。

#### 依赖项

仅当为 **Model dynamics** 参数选择 `Model turn-on and turn-off times` 时，此参数可见。

### **Turn-off delay** — Turn-off delay `1e-3`（默认）| positive scalar

输入电压降至阈值电压以下与开关打开之间的时间。值必须大于零。

#### 依赖项

仅当为 **Model dynamics** 参数选择 `Model turn-on and turn-off times` 时，此参数可见。

### **Initial input value, vT** — Initial input value, vT `0`（默认）

时间零时 physical signal 输入 `vT` 的值。此值用于在内部初始化延迟控制电压参数。

#### 依赖项

仅当为 **Model dynamics** 参数选择 `Model turn-on and turn-off times` 时，此参数可见。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

单刀双掷开关

SPDT Switch 模块对单刀双掷开关建模：

- 当开关断开时，端口 **p** 连接到端口 **n1**。
- 当开关闭合时，端口 **p** 连接到端口 **n2**。

断开的连接由阻值等于 **Open conductance** 参数值的倒数的电阻建模。闭合的连接由阻值等于 **Closed resistance** 参数值的电阻建模。

如果 **Threshold width** 参数设置为零，则当 **vT** 控制端口上呈现的电压超过 **Threshold** 参数的值时，开关闭合。

如果 **Threshold width** 参数大于零，则开关电导 *G* 在断态值和通态值之间平滑变化：

G=xRclosed+(1−x)Gopen

λ=vT−ThresholdThreshold width

x={0for λ≤03λ2−2λ3for 0<λ<11for λ≥1

该模块使用函数 3*λ*2 – 2*λ*3，因为其导数在 *λ* = 0 和 *λ* = 1 处为零。

定义较小的正 **Threshold width** 可以帮助某些模型中的求解器收敛，特别是当控制端口信号 *vT* 作为其他网络变量的函数连续变化时。然而，定义非零阈值宽度会阻止求解器利用切换线性优化。因此，如果网络的其余部分为切换线性，请将 **Threshold width** 设置为零。

可选地，可以在 **vT** 处的电压通过阈值的时间点与开关打开或闭合之间添加延迟。要启用该延迟，请在 **Dynamics** 选项卡上，将 **Model dynamics** 参数设置为 `Model turn-on and turn-off times`。

### 门控控制端口建模

您可以使用 physical signal 端口或电气守恒端口来控制开关门控。要选择门控控制端口，请将 **Modeling option** 参数设置为以下任一项：

- `PS control port` — 该模块包含一个与阈值电压关联的 physical signal 端口。
- `Electrical control port` — 该模块包含与阈值电压关联的电气守恒端口。
