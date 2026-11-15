---
type: simulink-block
title: 'Piecewise Linear Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'piecewiselinearvoltagesource'
documentation_source_path: 'ref/piecewiselinearvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Piecewise Linear Voltage Source

## 端口

### 守恒

### **+** — 正电压电气

与 Piecewise Linear Voltage Source 正电压相关联的电气守恒端口

### **-** — 负电压电气

与 Piecewise Linear Voltage Source 负电压相关联的电气守恒端口

## 参数

### **时间规范** — 时间值向量 `[0, 1, 2, 3, 4]` `s` (默认)

时间值向量为表格形式的 1-by-*n* 数组。时间值向量必须严格单调递增。

### **指定时间的电流** — 电流值向量 `[0, 0, 0, 0, 0]` `V` (默认)

电压值向量为表格形式的 1-by-*n* 数组。电压值向量必须与时间值向量大小相同。

### **插值方法** — 插值方法 `Linear` (默认) | `Smooth`

选择模块用于确定在未在前述向量中指定的中间时间点处输出电流值的方法：

- `Linear` — 通过使用线性函数优先考虑性能。
- `Smooth` — 通过生成具有连续一阶导数的连续曲线优先考虑精度。

### **外推方法** — 外推方法 `Nearest` (默认) | `Linear`

选择模块用于确定在前述向量中指定的时间范围之外的时间点处输出电流值的方法：

- `Nearest` — 选择此选项以使用最近的输入值进行外推。
- `Linear` — 选择此选项以使用线性函数。

## 所属库

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

使用查找表的时变电压源

Piecewise Linear Voltage Source 模块表示一个电压源，您使用时间值向量和对应电压值向量以查找表形式指定该电压源。您必须至少指定两对时间-电流值对。该模块基于这些时间-电压值，使用选定的插值方法和外推方法生成随时间变化的电压。您可以选择两种插值方法和外推方法。输出电压与流过该源的电流无关。
