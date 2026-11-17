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
```yaml
ports:
- name: E
  summary: 应变输入物理信号
  direction: input
- name: +
  summary: 正端口电气
  direction: input
- name: '-'
  summary: 负端口电气
  direction: input
```

### 输入

### **E** — 应变输入物理信号

与应变输入关联的物理信号端口。
### 守恒

### **+** — 正端口电气

与应变计正端口关联的电气守恒端口。

### **-** — 负端口电气

与应变计负端口关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Gauge resistance
  summary: 无应力应变计电阻 100 Ohm（默认值）
  group: ''
- name: Gauge factor
  summary: 应变计因子 2（默认值）
  group: ''
```

### **Gauge resistance** — 无应力应变计电阻 `100` `Ohm`（默认值）

无应力应变计电阻。

### **Gauge factor** — 应变计因子 `2`（默认值）

电阻相对变化与长度相对变化之比 *K*。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

变形传感器

Strain Gauge 模块表示一种传感器，它使用以下方程根据应变产生电阻变化：

ΔRR=Kε

其中：

- Δ*R*/*R* 是电阻的相对变化。
- ε 是端口 E 处的应变。
- *K* 是 **Gauge factor** 参数值。
