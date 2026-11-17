---
type: simulink-block
title: 'Peltier Device'
family: 'sensors-transducers'
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

### 守恒

### **+** — 正电气端口 electrical

与正极端子关联的电气守恒端口。

### **-** — 负电气端口 electrical

与负极端子关联的电气守恒端口。

### **A** — 热端口 thermal

热守恒端口。当该模块用作冷却设备时，正电流会使热量从端口 **A** 流向端口 **B**，从而使端口 **A** 相对于端口 **B** 冷却。

### **B** — 热端口 thermal

热守恒端口。

## 参数

### 电气

### **Seebeck coefficient** — 热电灵敏度系数 `220e-6` `V/K`（默认）

材料两端存在温差时感应出的热电电压大小的量度。

### **Total electrical resistance** — 电气端口之间的电阻 `0.02` `Ω`（默认）

**+** 和 **-** 端口之间的总电阻。

### 热

### **Thermal conductance** — 热端口之间的热导 `1.5e-3` `W/K`（默认）

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

Peltier Device 模块表示使用珀尔帖效应和塞贝克效应的电热冷却器或热电发电机。该模块在电能与热能之间转换：

- 在没有电流流动的情况下，如果热端口 **B** 处的温度高于热端口 **A** 处的温度，则从正电气端口到负电气端口测得的电势差为正。
- 当该模块用作冷却设备时，正电流会使热量从端口 **A** 流向端口 **B**，从而使端口 **A** 相对于端口 **B** 冷却。

定义方程为：

QA=αTAI−12I2R+K(TA−TB)QB=−αTBI−12I2R+K(TB−TA)W=VIW+QA+QB=0

其中：

- *Q*A 是流入端口 **A** 的热流。
- *Q*B 是流入端口 **B** 的热流。
- *T*A 是端口 **A** 的温度。
- *T*B 是端口 **B** 的温度。
- *W* 是电功率（流入该模块时为正）。
- *V* 是 **+** 和 **-** 端口之间的电势差。
- *I* 是电流，从 **+** 端口到 **-** 端口为正。
- *R* 是总电阻。
- *α* 是塞贝克系数。
- *K* 是热导。

将功率代入并将所有项除以电流，可得到电气方程：

V=α(TB−TA)+IR

该模块有一个记录变量 `power_dissipated`（**Dissipated power**）。此变量报告直流电功率，也就是说，如果使用交流电源驱动该器件，则为一个交流周期内的平均电功率。就方程而言，它等于 *I*2*R* 的瞬时值，并且在冷却应用中可用于指示热流中的非生产性部分。在加热应用中，耗散功率的解释不太有用。
