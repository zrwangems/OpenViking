---
type: simulink-block
title: 'Sinusoidal Force Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Drivetrain Disturbances'
documentation_page: 'sinusoidalforcesource'
documentation_source_path: 'ref/sinusoidalforcesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Force Source

## 端口

### 守恒

### **B** — 基座接口机械平移

与基座接口关联的机械平移守恒端口。

### **F** — 从动接口机械平移

与从动接口关联的机械平移守恒端口。

## 参数

### **Offset** — 输出平均值 `0` `N`（默认）

输出正弦力围绕其振荡的平均值。

### **Sinusoid peak amplitude** — 输出峰值幅值 `1` `N`（默认）

输出正弦力的峰值幅值。

### **Phase shift** — 输出相移 `0` `deg`（默认）

输出正弦力的相移。

### **Frequency** — 输出频率 `1` `Hz`（默认）

输出正弦力的频率。频率必须大于或等于 0。

## 所属库

Simscape / Driveline / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成正弦力

Sinusoidal Force Source 模块生成具有恒定偏置的正弦力。正的力值会产生从端口 B 作用到端口 F 的力。

该模块生成的正弦力的定义方程为

F=Fo+A\*sin(2πft+φ),

其中：

- *F* 是输出力。
- *Fo* 是输出的偏置力。
- A 是正弦波的峰值幅值。
- *f* 是正弦波的频率，单位为 Hz。
- *t* 是时间。
- φ 是正弦波的相移。
