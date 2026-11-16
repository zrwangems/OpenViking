---
type: simulink-block
title: 'SFFM Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'sffmvoltagesource'
documentation_source_path: 'ref/sffmvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# SFFM Voltage Source

## 端口

### 守恒

### **+** — 正电压电气

与 SFFM Voltage Source 的正电压相关联的电气守恒端口

### **-** — 负电压电气

与 SFFM Voltage Source 的负电压相关联的电气守恒端口

## 参数

### **电压偏移，VO** — 电压偏移 `0` `V`（默认值）

输出电压中与时间无关部分的幅值。

### **电压幅度，VA** — 电压幅度 `0` `V`（默认值）

输出电压正弦部分的幅值。

### **载波频率，FC** — 载波频率 `0` `Hz`（默认值）| 非负标量

载波的频率。该值必须大于或等于 `0`。

### **调制指数，MI** — 调制指数 `0`（默认值）| 非负标量

调制信号围绕其未调制电平变化的量。该值必须大于或等于 `0`。

### **信号频率，FS** — 信号频率 `0` `Hz`（默认值）| 非负标量

调制信号的频率。该值必须大于或等于 `0`。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

单频频率调制电压源

SFFM Voltage Source 模块表示一个调频交流电压源，其输出电压值与通过源的电流无关。以下方程描述了输出电压随时间的变化：

Vout = VO+VA\*sin((2π\*FC\*Time)+MI\*sin(2π\*FS\*Time))

其中：

- *V0* 是 **电压偏移，VO** 参数值。
- *VA* 是 **电压幅度，VA** 参数值。
- *FC* 是 **载波频率，FC** 参数值。
- *MI* 是 **调制指数，MI** 参数值。
- *FS* 是 **信号频率，FS** 参数值。
