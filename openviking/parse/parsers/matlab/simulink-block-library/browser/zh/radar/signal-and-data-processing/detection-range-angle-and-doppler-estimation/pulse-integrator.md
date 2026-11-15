---
type: simulink-block
title: 'Pulse Integrator'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'pulseintegrator'
documentation_source_path: '../phased/ref/pulseintegrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Integrator

## 端口

### 输入

### **x** — 脉冲输入数据矩阵

脉冲输入数据，指定为矩阵。`x` 的每一列是一个脉冲。

**数据类型：** `double`
### 输出

### **∑x** — 积分后的脉冲列向量

积分后的脉冲，返回为 *N*×1 列向量，其中 *N* 是输入 `x` 的行数。

**数据类型：** `double`

## 参数

### **积分方法** — 积分方法 `Coherent` (默认) | `Noncoherent`

将积分方法指定为 `Coherent` 或 `Noncoherent`。

### **要积分的脉冲数** — 要积分的脉冲数 `10` (默认)

将要积分的脉冲数指定为整数。

### **积分重叠（以 pulses 为单位）** — 积分重叠 `0` (默认)

将连续积分中重叠脉冲的数量指定为整数。此数字必须小于 **要积分的脉冲数** 中指定的值。

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

相干或非相干脉冲积分

Pulse Integrator 模块对信号的连续脉冲执行相干或非相干积分，并输出积分结果。您可以指定要积分的脉冲数以及连续积分中的重叠脉冲数。
