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
```yaml
ports:
- name: R
  summary: 杆接口机械平动
  direction: conserving
- name: C
  summary: 壳体接口机械平动
  direction: conserving
- name: H
  summary: 热流热
  direction: conserving
```

### 守恒端口

### **R** — 杆接口机械平动

与杆接口关联的机械平动守恒端口。

### **C** — 壳体接口机械平动

与壳体接口关联的机械平动守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流影响阻尼器温度，因此影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Thermal port** 设置为
`Model`。
## 参数
```yaml
parameters:
- name: Damping coefficient
  summary: 阻尼系数 100 N/(m/s)（默认）| 非负标量
  group: ''
- name: Damping fault
  summary: 故障选项 Add fault
  group: ''
- name: Faulted damping coefficient
  summary: 故障阻尼系数 1e6 N*s/m（默认）
  group: ''
- name: Thermal port
  summary: 热建模 Omit（默认）| Model
  group: ''
- name: Thermal mass
  summary: 热质量 50 kJ/K（默认）| 正标量
  group: ''
```

#### 主

### **Damping coefficient** — 阻尼系数 `100` `N/(m/s)`（默认）| 非负标量

由粘性摩擦引起的阻尼系数。

#### 故障

### **Damping fault** — 故障选项 `Add fault`

是否在模块中建模故障。要添加故障，请点击
**Add fault** 超链接。

### **Faulted damping coefficient** — 故障阻尼系数 `1e6` `N*s/m`（默认）

触发故障时的阻尼系数。

#### 依赖关系

要启用此参数，请先通过点击 **Add fault** 超链接启用模块的故障。

#### 热端口

### **Thermal port** — 热建模 `Omit`（默认）| `Model`

用于建模热流和温度变化效应的选项。

### **Thermal mass** — 热质量 `50` `kJ/K`（默认）| 正标量

使组件温度升高一个单位所需的热能。热质量表示阻尼器吸收和保持热能的能力。
## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a：使用 Simscape 故障接口建模故障

Translational Damper 模块现在支持 Simscape 故障接口。要了解更多信息，
请参阅 Introduction to Simscape Faults。

## 描述

线性平动阻尼器

Translational Damper 模块建模线性平动粘性
阻尼器。从仿真开始，模块使用标称阻尼
系数。如果为模块启用故障，阻尼系数会
响应以下一个或两个触发条件而变化：

- 仿真时间 — 在指定时间发生故障。
- 仿真行为 — 如果平动
  加速度的幅值超过指定的最大值，模块将
  冲击次数加一。如果冲击次数超过
  指定的最大冲击次数，则发生故障。

定义方程为

F=Dv

以及

v=vR−vC，

其中

- *F* 是通过阻尼器传递的力。
- *D* 是阻尼（粘性摩擦）系数。
- *v* 是相对速度。
- *vR* 和
  *vC* 分别是端子 **R** 和 **C**
  的绝对速度。

模块正方向是从端口 **R** 到端口 **C**。
因此，如果力沿从 **R** 到
**C** 的方向作用，则为正。

### 故障

要在 Translational Damper 模块中建模故障，请在
**Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块将在仿真的剩余时间内应用 **Faulted
damping coefficient** 参数的值。

### 热建模

您可以通过启用可选热端口来建模热流和温度变化的效应。要启用该端口，请将 **Thermal port** 设置为
`Model`。

启用热建模会显示 **Thermal mass**
参数。
