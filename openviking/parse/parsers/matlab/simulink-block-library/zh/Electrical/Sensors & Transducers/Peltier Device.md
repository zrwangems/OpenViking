---
type: simulink-block
title: 'Peltier Device'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'peltierdevice'
documentation_source_path: 'ref/peltierdevice.html'
language: zh-CN
chinese_source: worker-translation
---

# Peltier Device

## 端口
```yaml
ports:
- name: +
  summary: 正电气端口 electrical
  direction: conserving
- name: '-'
  summary: 负电气端口 electrical
  direction: conserving
- name: A
  summary: 热端口 thermal
  direction: conserving
- name: B
  summary: 热端口 thermal
  direction: conserving
```

### 守恒端口

### **+** — 正电气端口 electrical

与正极端子关联的电气守恒端口。

### **-** — 负电气端口 electrical

与负极端子关联的电气守恒端口。

### **A** — 热端口 thermal

热守恒端口。当该模块作为冷却设备工作时，正电流使热量从端口 **A** 流向端口 **B**，从而使端口 **A** 相对于端口 **B** 冷却。

### **B** — 热端口 thermal

热守恒端口。
## 参数
```yaml
parameters:
- name: Seebeck coefficient
  summary: 热电灵敏度系数 220e-6 V/K（默认值）
  group: 电气
- name: Total electrical resistance
  summary: 电气端口之间的电阻 0.02 Ω（默认值）
  group: 电气
- name: Thermal conductance
  summary: 热端口之间的热导 1.5e-3 W/K（默认值）
  group: 热
```

### 电气

### **Seebeck coefficient** — 热电灵敏度系数 `220e-6` `V/K`（默认值）

该材料两端温差所诱导的热电电压大小的度量。

### **Total electrical resistance** — 电气端口之间的电阻 `0.02` `Ω`（默认值）

**+** 和 **-** 端口之间的总电阻。

### 热

### **Thermal conductance** — 热端口之间的热导 `1.5e-3` `W/K`（默认值）

**A** 和 **B** 端口之间的热导。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

电热冷却器或热电发电机

Peltier Device 模块表示利用 Peltier 效应和 Seebeck 效应的电热冷却器或热电发电机。该模块在电能和热能之间进行转换：

- 在没有电流流动的情况下，如果热端口 **B** 处的温度高于热端口 **A** 处的温度，则从正电气端口到负电气端口测量存在正电势差。
- 当该模块作为冷却设备工作时，正电流使热量从端口 **A** 流向端口 **B**，从而使端口 **A** 相对于端口 **B** 冷却。

定义方程为：

QA=αTAI−12I2R+K(TA−TB)QB=−αTBI−12I2R+K(TB−TA)W=VIW+QA+QB=0

其中：

- *Q*A 是流入端口 **A** 的热量。
- *Q*B 是流入端口 **B** 的热量。
- *T*A 是端口 **A** 的温度。
- *T*B 是端口 **B** 的温度。
- *W* 是电功率（流入模块时为正）。
- *V* 是 **+** 和 **-** 端口之间的电势差。
- *I* 是电流，从 **+** 端口到 **-** 端口为正。
- *R* 是总电阻。
- *α* 是 Seebeck 系数。
- *K* 是热导。

代入功率并将所有项除以电流，得到电气方程：

V=α(TB−TA)+IR

该模块具有一个记录变量 `power_dissipated`（**Dissipated power**）。该变量报告直流电功率，即如果用交流电源驱动该设备，则为一个交流周期内的平均电功率。用方程表示，它等于 *I*2*R* 的瞬时值，在冷却应用中可用于指示热流中非生产性的部分。在加热应用中，耗散功率的解释不太有用。
