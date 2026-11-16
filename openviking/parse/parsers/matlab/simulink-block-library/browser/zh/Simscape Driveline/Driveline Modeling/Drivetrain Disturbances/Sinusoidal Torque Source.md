---
type: simulink-block
title: 'Sinusoidal Torque Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Drivetrain Disturbances'
documentation_page: 'sinusoidaltorquesource'
documentation_source_path: 'ref/sinusoidaltorquesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Torque Source

## 端口

### 守恒

### **B** — 基座接口机械旋转

与基座接口关联的机械旋转守恒端口。

### **F** — 从动接口机械旋转

与从动接口关联的机械旋转守恒端口。

## 参数

### **Offset** — 输出平均值 `0` `N*m` (默认)

正弦输出扭矩围绕其振荡的平均值。

### **Sinusoid peak amplitude** — 输出峰值振幅 `1` `N*m` (默认)

正弦输出扭矩的峰值振幅。

### **Phase shift** — 输出相移 `0` `deg` (默认)

正弦输出扭矩的峰值振幅。

### **Frequency** — 输出频率 `1` `Hz` (默认)

正弦输出扭矩的频率。频率必须大于或等于 0。

## 所属库

Simscape / Driveline / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成正弦扭矩

Sinusoidal Torque Source 模块生成具有恒定偏移的正弦扭矩。正扭矩值生成的扭矩从端口 B 作用到端口 F。

该模块生成的正弦扭矩的定义方程为

T=To+A\*sin(2πft+φ),

其中：

- T 是输出扭矩。
- *To* 是输出的偏移扭矩。
- *A* 是正弦曲线的峰值振幅。
- *f* 是正弦曲线的频率，以 Hz 为单位。
- *t* 是时间。
- φ 是正弦曲线的相移。
