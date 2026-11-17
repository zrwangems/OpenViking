---
type: simulink-block
title: 'Rotational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'rotationaldamper'
documentation_source_path: 'ref/rotationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Damper

## 端口
```yaml
ports:
- name: R
  summary: 杆接口机械旋转
  direction: unspecified
- name: C
  summary: 壳体接口机械旋转
  direction: unspecified
- name: H
  summary: 热流热
  direction: unspecified
```

### 守恒

### **R** — 杆接口机械旋转

与杆接口关联的机械旋转守恒端口。

### **C** — 壳体接口机械旋转

与壳体接口关联的机械旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流会影响阻尼器温度，从而影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Thermal port** 设置为 `Model`。
## 参数
```yaml
parameters:
- name: Damping coefficient
  summary: 阻尼系数 1e-3 N*m/(rad/s)（默认）| 正标量
  group: 主要
- name: Damping fault
  summary: 用于对阻尼故障建模的选项 Add fault
  group: 故障
- name: Faulted damping coefficient
  summary: 发生故障时的阻尼系数 100 N*m*s/rad（默认）| 正标量
  group: 故障
- name: Thermal port
  summary: 热建模 Omit（默认）| Model
  group: 热端口
- name: Thermal mass
  summary: 热质量 50 kJ/K（默认）| 正标量
  group: 热端口
```

### 主要

### **Damping coefficient** — 阻尼系数 `1e-3` `N*m/(rad/s)`（默认）| 正标量

如果未发生触发事件，模块因粘性摩擦而施加的减振扭矩。指定一个大于或等于零的值。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。在 Property Inspector 中，点击 **Fault behavior** 链接以打开故障。

### **Damping fault** — 用于对阻尼故障建模的选项 `Add fault`

是否对模块中的故障建模。要添加故障，请点击 **Add fault** 超链接。

### **Faulted damping coefficient** — 发生故障时的阻尼系数 `100` `N*m*s/rad`（默认）| 正标量

故障触发后的阻尼系数。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

### 热端口

### **Thermal port** — 热建模 `Omit`（默认）| `Model`

用于对热流和温度变化的影响建模的选项。

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

### R2024a：使用 Simscape 故障接口对故障建模

Rotational Damper 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

线性旋转阻尼器

Rotational Damper 模块表示线性旋转粘性阻尼器。该模块计算阻尼器传递的扭矩，使得

T=Dω

并且

ω=ωR−ωC，

其中

- *T* 是通过阻尼器传递的扭矩。
- *D* 是阻尼（粘性摩擦）系数。
- *ω* 是相对速度。
- *ωR* 和
  *ωC* 分别是端口 **R** 和 **C** 的绝对速度。

模块正方向是从端口 **R** 到端口 **C**。因此，如果扭矩沿从 **R** 到 **C** 的方向作用，则扭矩为正。

### 故障

要对 Rotational Damper 模块中的故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块将在仿真的剩余时间内应用 **Faulted damping coefficient** 参数的值。

### 热建模

您可以通过启用可选热端口来对热流和温度变化的影响建模。要启用该端口，请将 **Thermal port** 设置为 `Model`。

启用热建模会显示 **Thermal mass** 参数。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。
