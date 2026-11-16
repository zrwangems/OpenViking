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

### **闭合电阻** — 闭合电阻 `0.01` `Ohm`（默认值）

当开关闭合时，**p** 和 **n** 电气端口之间的电阻。

### **断开电导** — 断开电导 `1e-6` `S`（默认值）

当开关断开时，**p** 和 **n** 电气端口之间的电导。该值必须大于零。

### **阈值** — 阈值电压 `0.5` `V`（默认值）

控制物理信号输入 *vT* 的阈值电压，高于该值时开关将导通。

### **阈值宽度** — 阈值宽度 `0` `V`（默认值）

控制信号 *vT* 高于阈值的最小增量，该增量将使开关从完全断开变为完全闭合。

### 动态

### **模型动态** — 模型动态 `No dynamics`（默认值） | `Model turn-on and turn-off times`

选择模块是否对开关延迟建模：

- `No dynamics`
  — 不对延迟建模。这是默认选项。
- `Model turn-on and turn-off times` — 使用附加参数对 **vT** 处电压超过阈值的时刻与开关断开或闭合之间的延迟进行建模。

### **导通延迟** — 导通延迟 `1e-3`（默认值） | 正标量

输入电压超过阈值电压与开关闭合之间的时间。该值必须大于零。

#### 依赖项

仅当您为 **模型动态** 参数选择 `Model turn-on and turn-off times` 时，此参数才可见。

### **关断延迟** — 关断延迟 `1e-3`（默认值） | 正标量

输入电压降至阈值电压以下与开关断开之间的时间。该值必须大于零。

#### 依赖项

仅当您为 **模型动态** 参数选择 `Model turn-on and turn-off times` 时，此参数才可见。

### **初始输入值, vT** — 初始输入值, *vT* `0`（默认值）

物理信号输入 *vT* 在时间为零时的值。此值用于在内部初始化延迟控制电压参数。

#### 依赖项

仅当您为 **模型动态** 参数选择 `Model turn-on and turn-off times` 时，此参数才可见。

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

闭合连接由阻值等于 **闭合电阻** 参数值的电阻建模。断开连接由阻值等于 **断开电导** 参数值倒数的电阻建模。

如果 **阈值宽度** 参数设置为零，则当 **vT** 控制端口提供的电压超过 **阈值** 参数的值时，开关闭合。

如果 **阈值宽度** 参数大于零，则开关电导 *G* 在关断状态值和导通状态值之间平滑变化：

G=xRclosed+(1−x)Gopen

λ=vT−ThresholdThreshold width

x={0for λ≤03λ2−2λ3for 0<λ<11for λ≥1

该模块使用函数 3*λ*2 – 2*λ*3，因为其导数在 *λ* = 0 和 *λ* = 1 时为零。

定义较小的正 **阈值宽度** 有助于某些模型中的求解器收敛，特别是当控制端口信号 *vT* 作为其他网络变量的函数连续变化时。然而，定义非零阈值宽度会阻止求解器利用切换线性优化。因此，如果网络的其余部分是切换线性的，请将 **阈值宽度** 设置为零。

可选地，您可以在 **vT** 处电压超过阈值的时刻与开关断开或闭合之间添加延迟。要启用该延迟，请在 **动态** 选项卡上，将 **模型动态** 参数设置为 `Model turn-on and turn-off times`。
