---
type: simulink-block
title: 'Piecewise Linear Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'piecewiselinearvoltagesource'
documentation_source_path: 'ref/piecewiselinearvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Piecewise Linear Voltage Source

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

与分段线性电压源正电压相关联的电气守恒端口

### **-** — 负电压电气端口

与分段线性电压源负电压相关联的电气守恒端口
## 参数
```yaml
parameters:
- name: Time specification
  summary: 时间值向量 [0, 1, 2, 3, 4] s（默认）
  group: ''
- name: Current at specified time
  summary: 电流值向量 [0, 0, 0, 0, 0] V（默认）
  group: ''
- name: Interpolation method
  summary: 插值方法 Linear（默认）| Smooth
  group: ''
- name: Extrapolation method
  summary: 外插方法 Nearest（默认）| Linear
  group: ''
```

### **Time specification** — 时间值向量 `[0, 1, 2, 3, 4]` `s`（默认）

以表格形式表示的 1×*n* 数组的时间值向量。时间值向量必须严格单调递增。

### **Current at specified time** — 电流值向量 `[0, 0, 0, 0, 0]` `V`（默认）

以表格形式表示的 1×*n* 数组的电压值向量。电压值向量的大小必须与时间值向量相同。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

选择模块用于确定未在前述向量中指定的中间时间点处输出电压值的方法：

- `Linear` — 通过使用线性函数优先考虑性能。
- `Smooth` — 通过生成具有连续一阶导数的连续曲线优先考虑精度。

### **Extrapolation method** — 外插方法 `Nearest`（默认）| `Linear`

选择模块用于确定在前述向量中指定的时间范围之外的时间点处输出电压值的方法：

- `Nearest` — 选择此选项以使用最近的输入值进行外插。
- `Linear` — 选择此选项以使用线性函数。
## 所属库

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

使用查找表的时变电压源

Piecewise Linear Voltage Source 模块表示一个电压源，您可以通过时间值向量和相应的电压值向量以查找表形式指定该电压源。您必须至少指定两对时间-电流值。该模块使用选定的插值方法和外插方法，基于这些时间-电压值生成时变电压。您可以选择两种插值方法和外插方法。输出电压与流过电源的电流无关。
