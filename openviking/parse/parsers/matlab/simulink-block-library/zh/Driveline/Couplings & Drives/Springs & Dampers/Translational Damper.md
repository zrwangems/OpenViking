---
type: simulink-block
title: 'Translational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'translationaldamper'
documentation_source_path: 'ref/translationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Damper

## 端口

### 守恒

### **R** — 杆接口机械平移

与杆接口关联的机械平移守恒端口。

### **C** — 壳体接口机械平移

与壳体接口关联的机械平移守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流影响减振器温度，因此影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **Thermal port** 设置为 `Model`。

## 参数

#### 主

### **Damping coefficient** — Damping coefficient `100` `N/(m/s)` (default) | nonnegative scalar

由粘性摩擦引起的阻尼系数。

#### 故障

### **Damping fault** — 故障选项 `Add fault`

是否在模块中对故障建模。要添加故障，请单击 **Add fault** 超链接。

### **Faulted damping coefficient** — 故障阻尼系数 `1e6` `N*s/m` (default)

触发故障时的阻尼系数。

#### 依赖关系

要启用此参数，请首先通过单击 **Add fault** 超链接为该模块启用故障。

#### 热端口

### **Thermal port** — 热建模 `Omit` (default) | `Model`

对热流和温度变化影响建模的选项。

### **Thermal mass** — 热质量 `50` `kJ/K` (default) | positive scalar

使组件温度增加一个单位所需的热能。热质量表示减振器吸收和保持热能的能力。

## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：使用 Simscape faults 接口对故障建模

Translational Damper 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Simscape 故障简介。

## 描述

线性平移减振器

Translational Damper 模块对线性平移粘性减振器建模。从仿真开始，模块使用标称阻尼系数。如果为该模块启用故障，则阻尼系数会响应以下一个或两个触发条件而变化：

- 仿真时间 — 故障在指定时间发生。
- 仿真行为 — 如果平移加速度的幅值超过指定的最大值，模块会将冲击次数增加一。如果冲击次数超过指定的最大冲击次数，则发生故障。

定义方程为

F=Dv

和

v=vR−vC，

其中

- *F* 是通过减振器传递的力。
- *D* 是阻尼（粘性摩擦）系数。
- *v* 是相对速度。
- *vR* 和
  *vC* 分别是端子 **R** 和
  **C** 的绝对速度。

模块正方向是从端口 **R** 到端口 **C**。
因此，如果扭矩沿从 **R** 到
**C** 的方向作用，则扭矩为正。

### 故障

要对 Translational Damper 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

触发故障时，模块会在仿真剩余时间内应用 **Faulted damping coefficient** 参数的值。

### 热建模

您可以通过启用可选热端口来对热流和温度变化的影响建模。要启用该端口，请将 **Thermal port** 设置为 `Model`。

启用热建模会显示 **Thermal mass** 参数。
