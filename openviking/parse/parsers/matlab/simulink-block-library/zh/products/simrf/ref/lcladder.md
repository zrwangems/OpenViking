---
type: simulink-block
title: 'LC Ladder'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / RF Compound Components'
documentation_page: 'lcladder'
documentation_source_path: 'ref/lcladder.html'
language: zh-CN
chinese_source: worker-translation
---

# LC Ladder

## 端口

R2025b 中未记录。

## 参数

### **Ladder topology** — 梯形拓扑的类型 `LC Lowpass Tee`（默认）

梯形拓扑的类型，指定为以下之一：

**梯形拓扑**

|  |  |
| --- | --- |
| LC Lowpass Tee | LC Lowpass Tee |
| LC Lowpass Pi | LC Lowpass pi |
| LC Highpass Tee | LC highpass tee |
| LC Highpass Pi | LC highpass pi |
| LC Bandpass Tee | LC bandpass Tee |
| LC Bandpass Pi | LC Bandpass pi |
| LC Bandstop Tee | LC Bandstop Tee |
| LC Bandstop Pi | LC Bandstop pi |

### **Inductance** — 电感值 `[1.3324e-5 1.3324e-5] H`（默认）| 实数

电感值，指定为以 Henries 为单位的实数。从相应的下拉菜单中指定电感的单位。

**数据类型：** `double`

### **Capacitance** — 电容值 `1.1327e-9 F`（默认）| 实数

电容值，指定为以 Farads 为单位的实数。从相应的下拉菜单中指定电容的单位。

### **Ground and hide negative terminals** — 在内部将负端子接地并隐藏 `on`（默认）| `off`

选择此选项可在内部将负端子接地并隐藏。清除此选项可暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其它部分。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2015b 中引入**

## 描述

对 LC 梯形网络进行建模

LC Ladder 模块对常见的二端口 LC 无损网络进行建模。要了解如何使用 LC Ladder 比较输入和输出信号幅度以研究信号衰减，请参阅 Model RF Filter Using Circuit Envelope。
