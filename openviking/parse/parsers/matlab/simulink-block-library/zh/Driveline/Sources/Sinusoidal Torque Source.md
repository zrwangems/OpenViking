---
type: simulink-block
title: 'Sinusoidal Torque Source'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'sinusoidaltorquesource'
documentation_source_path: 'ref/sinusoidaltorquesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Torque Source

## 端口
```yaml
ports:
- name: B
  summary: 基座接口机械旋转
  direction: conserving
- name: F
  summary: 从动接口机械旋转
  direction: conserving
```

### 守恒端口

### **B** — 基座接口机械旋转

与基座接口关联的机械旋转守恒端口。

### **F** — 从动接口机械旋转

与从动接口关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Offset
  summary: 输出平均值 0 N*m（默认值）
  group: ''
- name: Sinusoid peak amplitude
  summary: 输出峰值幅度 1 N*m（默认值）
  group: ''
- name: Phase shift
  summary: 输出相移 0 deg（默认值）
  group: ''
- name: Frequency
  summary: 输出频率 1 Hz（默认值）
  group: ''
```

### **Offset** — 输出平均值 `0` `N*m`（默认值）

正弦输出转矩围绕其振荡的平均值。

### **Sinusoid peak amplitude** — 输出峰值幅度 `1` `N*m`（默认值）

正弦输出转矩的峰值幅度。

### **Phase shift** — 输出相移 `0` `deg`（默认值）

正弦输出转矩的峰值幅度。

### **Frequency** — 输出频率 `1` `Hz`（默认值）

正弦输出转矩的频率。频率必须大于或等于 0。
## 所属库

Simscape / Driveline / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

产生正弦转矩

Sinusoidal Torque Source 模块产生具有恒定偏移的正弦转矩。正转矩值产生从端口 B 作用到端口 F 的转矩。

该模块产生的正弦转矩的定义方程为

T=To+A\*sin(2πft+φ)，

其中：

- T 是输出转矩。
- *To* 是输出的偏移转矩。
- *A* 是正弦波的峰值幅度。
- *f* 是正弦波的频率，单位为 Hz。
- *t* 是时间。
- φ 是正弦波的相移。
