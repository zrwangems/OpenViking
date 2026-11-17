---
type: simulink-block
title: 'Exponential Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'exponentialvoltagesource'
documentation_source_path: 'ref/exponentialvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Exponential Voltage Source

## 端口
```yaml
ports:
- name: +
  summary: 正电压电气
  direction: unspecified
- name: '-'
  summary: 负电压电气
  direction: unspecified
```

### 守恒

### **+** — 正电压电气

与直流电流源正电压相关联的电气守恒端口

### **-** — 负电压电气

与直流电流源负电压相关联的电气守恒端口
## 参数
```yaml
parameters:
- name: Initial value, V1
  summary: 输出电压初始值 0 V（默认）
  group: ''
- name: Pulse value, V2
  summary: 输出电压渐近值 0 V（默认）
  group: ''
- name: Rise delay time, TDR
  summary: 上升延迟时间 0 s（默认）
  group: ''
- name: Rise time, TR
  summary: 上升时间 1e-9 s（默认） | 正标量
  group: ''
- name: Fall delay time, TDF
  summary: 下降延迟时间 0 s（默认）
  group: ''
- name: Fall time, TF
  summary: 下降时间 1e-9 s（默认） | 正标量
  group: ''
```

### **Initial value, V1** — 输出电压初始值 `0` `V`（默认）

零时刻的输出电压值，单位为 V。

### **Pulse value, V2** — 输出电压渐近值 `0` `V`（默认）

输出为高电平时输出电压的渐近值，单位为 V。

### **Rise delay time, TDR** — 上升延迟时间 `0` `s`（默认）

上升时间延迟，单位为 s。

### **Rise time, TR** — 上升时间 `1e-9` `s`（默认） | 正标量

输出电流从 **Initial Value, V1** 值上升到 **Pulse Value, V2** 值所需的时间。

### **Fall delay time, TDF** — 下降延迟时间 `0` `s`（默认）

下降时间延迟。

### **Fall time, TF** — 下降时间 `1e-9` `s`（默认） | 正标量

输出电流从 **Pulse value, V2** 值下降到 **Initial value, V1** 值所需的时间。
## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

指数脉冲电压源

Exponential Voltage Source 模块表示一个电压源，其输出电压值是时间的指数脉冲函数，并且与流过该源的电流无关。以下方程描述了输出电压随时间的变化：

Vout(0≤Time≤TDR))=V1Vout(TDR<Time≤TDF)=V1+(V2-V1)\*(1-e-(Time-TDR)/TR)Vout(TDF<Time)=V1+(V2-V1)\*(e-(Time-TDF)/TF-e-(Time-TDR)/TR)

其中：

- *V1* 是 **Initial value, V1** 参数值。
- *V2* 是 **Pulse value, V2** 参数值。
- *TDR* 是 **Rise delay time, TDR** 参数值。
- *TR* 是 **Rise time, TR** 参数值。
- *TDF* 是 **Fall delay time, TDF** 参数值。
- *TF* 是 **Fall time, TF** 参数值。
