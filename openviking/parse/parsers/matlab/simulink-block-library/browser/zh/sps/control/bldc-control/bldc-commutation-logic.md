---
type: simulink-block
title: 'BLDC Commutation Logic'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control\u200b'
documentation_page: 'bldccommutationlogic'
documentation_source_path: 'ref/bldccommutationlogic.html'
language: zh-CN
chinese_source: official
---

# BLDC Commutation Logic

## 端口

### 输入

### **Hall** — 霍尔传感器 向量

霍尔传感器数据。

**数据类型:** `single` | `double`

### **Direction** — 电机方向 标量

电机旋转的方向。

**数据类型:** `single` | `double`
### 输出

### **abc** — 电机相 向量

换相逻辑指示的电机相。

**数据类型:** `single` | `double`

## 参数

### **采样时间(-1 表示继承)** — 模块采样时间 `-1` (默认) | 正标量

连续两次模块执行之间的时间，以秒为单位。在执行期间，模块产生输出，并在需要时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

如果此模块位于触发子系统内，则通过将此参数设置为 `-1` 来继承采样时间。如果此模块位于连续变步长模型内，则使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / BLDC Control

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

无刷 DC 电机的开关换相逻辑

作为此控制算法的一部分，BLDC Commutation Logic 模块实现无刷 DC 电机的换相逻辑。

换向逻辑基于霍尔信号，如下表所总结。

| 霍尔传感器 | | | 电机相 | | |
| --- | --- | --- | --- | --- | --- |
| 霍尔 a | 霍尔 b | 霍尔 c | a 相 | b 相 | c 相 |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | -1 |
| 0 | 1 | 0 | -1 | 1 | 0 |
| 0 | 1 | 1 | -1 | 0 | 1 |
| 0 | 0 | 1 | 0 | -1 | 1 |
| 1 | 0 | 1 | 1 | -1 | 0 |
| 1 | 0 | 0 | 1 | 0 | -1 |
| 1 | 1 | 1 | 0 | 0 | 0 |
