---
type: simulink-block
title: 'Exponential Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'exponentialvoltagesource'
documentation_source_path: 'ref/exponentialvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Exponential Voltage Source

## 端口

### 守恒

### **+** — 正电压电气

与 DC current source 正电压相关联的电气守恒端口

### **-** — 负电压电气

与 DC current source 负电压相关联的电气守恒端口

## 参数

### **初始值，V1** — 输出电压初始值 `0` `V`（默认）

时间零点的输出电压值，单位为 V。

### **脉冲值，V2** — 输出电压渐近值 `0` `V`（默认）

输出为高时输出电压的渐近值，单位为 V。

### **上升延迟时间，TDR** — 上升延迟时间 `0` `s`（默认）

上升时间延迟，单位为 s。

### **上升时间，TR** — 上升时间 `1e-9` `s`（默认） | 正标量

输出电流从 **初始值，V1** 值上升到 **脉冲值，V2** 值所需的时间。

### **下降延迟时间，TDF** — 下降延迟时间 `0` `s`（默认）

下降时间延迟。

### **下降时间，TF** — 下降时间 `1e-9` `s`（默认） | 正标量

输出电流从 **脉冲值，V2** 值下降到 **初始值，V1** 值所需的时间。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2008a 中引入**

## 描述

指数脉冲电压源

Exponential Voltage Source 模块表示一个电压源，其输出电压值是随时间变化的指数脉冲，并且与通过源的电流无关。以下方程描述输出电流随时间变化：

Vout(0≤Time≤TDR))=V1Vout(TDR<Time≤TDF)=V1+(V2-V1)\*(1-e-(Time-TDR)/TR)Vout(TDF<Time)=V1+(V2-V1)\*(e-(Time-TDF)/TF-e-(Time-TDR)/TR)

其中：

- *V1* 是 **初始值，V1**
  参数值。
- *V2* 是 **脉冲值，V2**
  参数值。
- *TDR* 是 **上升延迟时间，TDR**
  参数值。
- *TR* 是 **上升时间，TR** 参数
  值。
- *TDF* 是 **下降延迟时间，TDF**
  参数值。
- *TF* 是 **下降时间，TF**
  参数值。
