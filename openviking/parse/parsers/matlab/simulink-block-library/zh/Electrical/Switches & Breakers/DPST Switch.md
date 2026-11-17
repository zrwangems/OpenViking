---
type: simulink-block
title: 'DPST Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'dpstswitch'
documentation_source_path: 'ref/dpstswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# DPST Switch

## 端口

### 输入

### **vT** — 开关控制端口物理信号

与打开和关闭开关的信号相关联的物理端口。
### 守恒

### **p1** — 电气端口 electrical

电气守恒端口。

### **p2** — 电气端口 electrical

电气守恒端口。

### **n1** — 电气端口 electrical

电气守恒端口。

### **n2** — 电气端口 electrical

电气守恒端口。

## 参数

### 主要

### **Closed resistance** — 闭合电阻 `0.01` `Ohm`（默认）

当开关闭合时，**p** 和 **n** 电气端口之间的电阻。

### **Open conductance** — 断开电导 `1e-6` `S`（默认）

当开关断开时，**p** 和 **n** 电气端口之间的电导。该值必须大于零。

### **Threshold** — 阈值电压 `0.5` `V`（默认）

控制物理信号输入 *vT* 的阈值电压，高于该值时开关将导通。

### **Threshold width** — 阈值宽度 `0` `V`（默认）

控制信号 *vT* 超过阈值的最小增量，该增量将使开关从完全断开变为完全闭合。

### 动态特性

### **Model dynamics** — 模型动态特性 `No dynamics`（默认） | `Model turn-on and turn-off times`

选择模块是否对开关延迟进行建模：

- `No dynamics`
  — 不对延迟进行建模。这是默认选项。
- `模型开启和关闭`
  times` — 使用附加参数对 **vT** 处电压越过阈值与开关打开或闭合之间的延迟进行建模。

### **Turn-on delay** — 导通延迟 `1e-3`（默认） | 正标量

输入电压超过阈值电压与开关闭合之间的时间。该值必须大于零。

#### 依赖关系

此参数仅在 **Model dynamics** 参数选择 `Model turn-on and turn-off
times` 时可见。

### **Turn-off delay** — 关断延迟 `1e-3`（默认） | 正标量

输入电压降至阈值电压以下与开关打开之间的时间。该值必须大于零。

#### 依赖关系

此参数仅在 **Model dynamics** 参数选择 `Model turn-on and turn-off
times` 时可见。

### **Initial input value, vT** — 初始输入值，*vT* `0`（默认）

物理信号输入 *vT* 在零时刻的值。该值用于在内部初始化延迟控制电压参数。

#### 依赖关系

此参数仅在 **Model dynamics** 参数选择 `Model turn-on and turn-off
times` 时可见。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

双刀单掷开关

DPST Switch 模块对双刀单掷开关进行建模。

当开关闭合时，端口 **p1** 和 **p2** 分别连接到端口 **n1** 和 **n2**。

闭合连接由阻值等于 **Closed resistance** 参数值的电阻建模。断开连接由阻值等于 **Open conductance** 参数值倒数的电阻建模。

如果 **Threshold width** 参数设置为零，则当 **vT** 控制端口处呈现的电压超过 **Threshold** 参数值时，开关闭合。

如果 **Threshold width** 参数大于零，则开关电导 *G* 在断态值和通态值之间平滑变化：

G=xRclosed+(1−x)Gopen

λ=vT−ThresholdThreshold width

x={0for λ≤03λ2−2λ3for 0<λ<11for λ≥1

该模块使用函数 3*λ*2 – 2*λ*3，因为其导数在 *λ* = 0 和 *λ* = 1 时为零。

定义较小的正 **Threshold width** 有助于某些模型中的求解器收敛，特别是当控制端口信号 *vT* 作为其他网络变量的函数连续变化时。然而，定义非零阈值宽度会阻止求解器利用切换线性优化。因此，如果网络的其余部分是切换线性的，请将 **Threshold width** 设置为零。

或者，您可以在 **vT** 处电压越过阈值与开关打开或闭合之间添加延迟。要启用延迟，请在 **Dynamics** 选项卡上将 **Model dynamics** 参数设置为 `Model
turn-on and turn-off times`。
