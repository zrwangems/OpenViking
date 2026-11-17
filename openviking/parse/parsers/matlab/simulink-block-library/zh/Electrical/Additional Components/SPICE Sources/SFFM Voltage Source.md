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
```yaml
ports:
- name: +
  summary: 正电压电气端口
  direction: conserving
- name: '-'
  summary: 负电压电气端口
  direction: conserving
```

### 守恒端口

### **+** — 正电压电气端口

与 SFFM 电压源正电压相关联的电气守恒端口

### **-** — 负电压电气端口

与 SFFM 电压源负电压相关联的电气守恒端口
## 参数
```yaml
parameters:
- name: Voltage offset, VO
  summary: 电压偏置 0 V（默认值）
  group: ''
- name: Voltage amplitude, VA
  summary: 电压幅值 0 V（默认值）
  group: ''
- name: Carrier frequency, FC
  summary: 载波频率 0 Hz（默认值）| 非负标量
  group: ''
- name: Modulation index, MI
  summary: 调制指数 0（默认值）| 非负标量
  group: ''
- name: Signal frequency, FS
  summary: 信号频率 0 Hz（默认值）| 非负标量
  group: ''
```

### **Voltage offset, VO** — 电压偏置 `0` `V`（默认值）

输出电压中与时间无关部分的幅值。

### **Voltage amplitude, VA** — 电压幅值 `0` `V`（默认值）

输出电压中正弦部分的幅值。

### **Carrier frequency, FC** — 载波频率 `0` `Hz`（默认值）| 非负标量

载波的频率。该值必须大于或等于 `0`。

### **Modulation index, MI** — 调制指数 `0`（默认值）| 非负标量

调制信号围绕其未调制电平变化的量。该值必须大于或等于 `0`。

### **Signal frequency, FS** — 信号频率 `0` `Hz`（默认值）| 非负标量

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

单频调频电压源

SFFM Voltage Source 模块表示一个调频交流电压源，其输出电压值与流过该源的电流无关。以下方程描述了输出电压随时间的变化：

Vout = VO+VA\*sin((2π\*FC\*Time)+MI\*sin(2π\*FS\*Time))

其中：

- *V0* 是 **Voltage offset, VO** 参数值。
- *VA* 是 **Voltage amplitude, VA** 参数值。
- *FC* 是 **Carrier frequency, FC** 参数值。
- *MI* 是 **Modulation index, MI** 参数值。
- *FS* 是 **Signal frequency, FS** 参数值。
