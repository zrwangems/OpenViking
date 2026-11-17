---
type: simulink-block
title: 'Sinusoidal Translational Velocity Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinusoidaltranslationalvelocitysource'
documentation_source_path: 'ref/sinusoidaltranslationalvelocitysource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Translational Velocity Source

## 端口

### 守恒

### **B** — 基座接口机械平移

与基座接口关联的机械平移守恒端口。

### **F** — 从动接口机械平移

与从动接口关联的机械平移守恒端口。

## 参数

### **Offset** — 输出平均值 `0` `m/s`（默认）

输出正弦平移速度围绕其振荡的平均值。

### **Sinusoid peak amplitude** — 输出峰值幅度 `1` `m/s`（默认）

输出正弦平移速度的峰值幅度。

### **Phase shift** — 输出相移 `0` `deg`（默认）

输出正弦平移速度的相移

### **Frequency** — 输出频率 `1` `Hz`（默认）

输出正弦平移速度的频率。频率必须大于或等于 0。

## 所属库

Simscape / Driveline / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

产生正弦平移速度

Sinusoidal Translational Velocity Source 模块产生具有恒定偏移的正弦平移速度。

基座接口与从动接口之间的相对平移速度为

vFB=vF−vB，

其中：

- *v FB* 是相对平移速度。
- *vF* 是从动接口处的绝对平移速度。
- *vB* 是基座接口处的绝对平移速度。

该模块生成的正弦平移速度的定义方程为

v=vo+A\*sin(2πft+φ)，

其中：

- *v* 是输出平移速度。
- *vo* 是输出的偏移平移速度。
- *A* 是正弦波的峰值幅度。
- *f* 是正弦波的频率，单位为 Hz。
- *t* 是时间。
- φ 是正弦波的相移。
