---
type: simulink-block
title: 'Sinusoidal Rotational Velocity Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Drivetrain Disturbances'
documentation_page: 'sinusoidalrotationalvelocitysource'
documentation_source_path: 'ref/sinusoidalrotationalvelocitysource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Rotational Velocity Source

## 端口

### 守恒

### **B** — 基座接口机械旋转

与基座接口关联的机械旋转守恒端口。

### **F** — 从动接口机械旋转

与从动接口关联的机械旋转守恒端口。

## 参数

### **Offset** — 输出平均值 `0` `rad/s`（默认）

输出正弦旋转速度围绕其振荡的平均值。

### **Sinusoid peak amplitude** — 输出峰值幅值 `1` `rad/s`（默认）

输出正弦旋转速度的峰值幅值。

### **Phase shift** — 输出相位偏移 `0` `deg`（默认）

输出正弦旋转速度的相位偏移。

### **Frequency** — 输出频率 `1` `Hz`（默认）

输出正弦旋转速度的频率。频率必须大于或等于 0。

## 所属库

Simscape / Driveline / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成正弦旋转速度

Sinusoidal Rotational Velocity Source 模块生成具有恒定偏移的正弦旋转速度。

基座接口与从动接口之间的相对旋转速度为

vFB=vF−vB,

其中：

- *v FB* 是相对旋转速度。
- *vF* 是从动接口处的绝对旋转速度。
- *vB* 是基座接口处的绝对旋转速度。

该模块生成的正弦旋转速度的定义方程为

v=vo+A\*sin(2πft+φ),

其中：

- *v* 是输出旋转速度。
- *vo* 是输出的偏移旋转速度。
- *A* 是正弦波的峰值幅值。
- *f* 是正弦波的频率，以 Hz 为单位。
- *t* 是时间。
- φ 是正弦波的相位偏移。
