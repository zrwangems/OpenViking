---
type: simulink-block
title: 'Sinusoidal Voltage Source'
family: 'additional-components'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'sinusoidalvoltagesource'
documentation_source_path: 'ref/sinusoidalvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Voltage Source

## 端口

### 守恒

### **+** — 正电压电气

与正弦电压源正电压关联的电气守恒端口

### **-** — 负电压电气

与正弦电压源负电压关联的电气守恒端口

## 参数

### **电压偏移，VO** — 电压偏移 `0` `V` （默认）

输出电压中与时间无关的部分的幅值。

### **正弦幅度，VA** — 正弦幅度 `0` `V` （默认）

输出电压中正弦部分的幅值。

### **正弦频率，FREQ** — 正弦频率 `1e6` `Hz` （默认）

输出正弦波的频率。该值可以小于 `0`。

### **时间延迟，TD** — 时间延迟 `0` `s` （默认）

正弦波首次开始的时间。小于 `0` 的值表示 180 度相移。

### **阻尼因子，DF** — 阻尼因子 `0` `1/s` （默认） | 非负标量

用于生成输出电压的正弦波的指数阻尼因子。如果 *DF* 大于或等于 `0`，则对于大于 *TD* 的时间，方程的指数部分始终是阻尼的。该值必须大于或等于 `0`。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

阻尼正弦电压源

Sinusoidal Voltage Source 模块表示一个阻尼正弦电压源，其输出电压与流过该源的电流无关。
以下方程将输出描述为时间的函数：

Vout(Time≤TD)=VOVout(Time>TD)=VO+VA\*e−(Time−TD)\*DF\*sin(2π\*FREQ\*(Time−TD))

其中：

- *V0* 是 **电压偏移，VO** 参数值。
- *VA* 是 **正弦幅度，VA** 参数值。
- *FREQ* 是 **正弦频率，FREQ** 参数值。
- *TD* 是 **时间延迟，TD** 参数值。
- *DF* 是 **阻尼因子，DF** 参数值。
