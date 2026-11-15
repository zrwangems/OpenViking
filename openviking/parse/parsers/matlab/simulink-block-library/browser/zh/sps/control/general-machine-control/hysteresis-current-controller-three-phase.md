---
type: simulink-block
title: 'Hysteresis Current Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control\u200b'
documentation_page: 'hysteresiscurrentcontrollerthreephase'
documentation_source_path: 'ref/hysteresiscurrentcontrollerthreephase.html'
language: zh-CN
chinese_source: official
---

# Hysteresis Current Controller (Three-Phase)

## 端口

### 输入

### **iabc\*** — 电流 向量

三相滞后参考电流。

**数据类型:** `single` | `double`

### **iabc** — 电流 向量

测得的三相电流。

**数据类型:** `single` | `double`
### 输出

### **S** — 控制器输出 向量

用于功率转换器控制的六脉冲向量。

**数据类型:** `single` | `double`

## 参数

### **电流滞后带(A)** — 滞后带 `1` (默认) | 正数

电流控制器的滞后带 *h*。导通点为 *h*/2，关断点为 -*h*/2。

### **采样时间(-1 表示继承)** — 模块采样时间 `-1` (默认) | 正标量

连续两次模块执行之间的时间，以秒为单位。在执行期间，模块产生输出，并在需要时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

如果此模块位于触发子系统内，则通过将此参数设置为 `-1` 来继承采样时间。如果此模块位于连续变步长模型内，则使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / General Machine Control

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

三相滞后电流控制

Hysteresis Current Controller (Three-Phase) 模块实现功率转换器的三相滞后电流控制。
