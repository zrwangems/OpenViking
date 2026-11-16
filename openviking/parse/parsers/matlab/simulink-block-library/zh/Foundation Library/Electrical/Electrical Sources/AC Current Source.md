---
type: simulink-block
title: 'AC Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'accurrentsource'
documentation_source_path: 'ref/accurrentsource.html'
language: zh-CN
chinese_source: official
---

# AC Current Source

## 端口

### 守恒

### **+** — 正极端子 电气

与电气源正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电气源负极端子相关联的电气守恒端口。

## 参数

### **峰值振幅** — 峰值电流振幅 `1 A` (默认) | 标量

峰值电流振幅。

### **相移** — 以角度单位表示的相移 `0 deg` (默认) | 标量

以角度单位表示的相移。

### **频率** — 电流频率 `60 Hz` (默认) | 正标量

以 Hz 为单位或以可直接转换为 Hz 的单位（其中 Hz 定义为 1/s）为单位指定的电流频率。例如，kHz 和 MHz 是有效的单位，rad/s 则不是。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

理想的正弦电流源

AC Current Source 模块表示理想的电流源，它保持通过的正弦电流不变，与其端子之间的电压无关。

输出电流由以下方程定义：

I=I0⋅sin(2π⋅f⋅t+φ)

其中：

- *I* 是电流。
- *I*0 是峰值振幅。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

箭头指示电流的正方向。
