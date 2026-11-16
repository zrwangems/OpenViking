---
type: simulink-block
title: 'Strain Gauge'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'straingauge'
documentation_source_path: 'ref/straingauge.html'
language: zh-CN
chinese_source: worker-translation
---

# Strain Gauge

## 端口

### 输入

### **E** — 应变输入物理信号

与应变输入关联的物理信号端口。

### 守恒

### **+** — 正端口（电气）

与应变片正端口关联的电气守恒端口。

### **-** — 负端口（电气）

与应变片负端口关联的电气守恒端口。

## 参数

### **应变片电阻** — 未受力应变片电阻 `100` `Ohm`（默认）

未受力应变片电阻。

### **应变片灵敏系数** — 应变片灵敏系数 `2`（默认）

*K* 是电阻相对变化量与长度相对变化量之比。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

形变传感器

Strain Gauge 模块表示一个传感器，该传感器使用以下方程根据应变产生电阻变化：

ΔR/R=Kε

其中：

- Δ*R*/*R* 是电阻的相对变化量。
- ε 是端口 E 处的应变。
- *K* 是 **应变片灵敏系数** 参数值。
