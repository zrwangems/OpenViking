---
type: simulink-block
title: 'AC Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'acvoltagesource'
documentation_source_path: 'ref/acvoltagesource.html'
language: zh-CN
chinese_source: official
---

# AC Voltage Source

## 端口

### 守恒

### **+** — 正极端子 电气

与电气源正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电气源负极端子相关联的电气守恒端口。

## 参数

### **峰值振幅** — 峰值电压振幅 `1 V` (默认) | 标量

峰值电压振幅。

### **相移** — 以角度单位表示的相移 `0 deg` (默认) | 标量

以角度单位表示的相移。

### **频率** — 电压频率 `60 Hz` (默认) | 正标量

以 Hz 为单位或以可直接转换为 Hz 的单位（其中 Hz 定义为 1/s）为单位指定的电压频率。例如，kHz 和 MHz 是有效的单位，rad/s 则不是。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

理想的恒定电压源

AC Voltage Source 模块表示理想的电压源，它能保持其输出端子上的正弦电压不变，与流过该电压源的电流无关。

输出电压由以下方程定义：

V=V0⋅sin(2π⋅f⋅t+φ)

其中：

- *V* 是电压。
- *V*0 是峰值振幅。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

连接端 **+** 和 **-** 是分别对应于电压源的正极端子和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，电压源两端的电压等于正极端子电压与负极端子电压之差，即 *V*(+) – *V*(-)。
