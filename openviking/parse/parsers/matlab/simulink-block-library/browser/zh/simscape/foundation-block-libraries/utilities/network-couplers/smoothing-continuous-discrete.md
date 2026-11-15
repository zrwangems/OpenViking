---
type: simulink-block
title: 'Smoothing (continuous->discrete)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Network Couplers'
documentation_page: 'smoothingcontinuousdiscrete'
documentation_source_path: 'ref/smoothingcontinuousdiscrete.html'
language: zh-CN
chinese_source: worker-translation
---

# Smoothing (continuous->discrete)

## 端口

### 输入

### **u** — 具有高频活动的信号 real scalar

将此端口连接至变步长网络 Network 1，以捕获其输出。
### 输出

### **y** — 用于定步长网络的平滑信号 real scalar

将此端口连接至定步长网络 Network 2 的输入。

## 参数

### **平滑时间常数 (s)** — 指定一阶滤波器的时间常数 `0.001` (默认) | positive scalar

指定一阶滤波器的时间常数，以秒为单位。通常，平滑时间常数至少要比定步长网络 Network 2 的步长大 10 倍。

### **初始输出** — 指定初始输出值 `0` (默认) | scalar

指定变步长网络 Network 1 的初始输出值。

## 所属库

Simscape / Utilities / Network Couplers / Fundamental Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

将变步长网络连接到定步长网络时应用输出平滑

**注意**

预测和平滑算法内置于 Network Coupler 模块中，您可以通过使用模块对话框中的复选框来启用它们。Fundamental Components 子库中的预测和平滑模块仅供您参考。

当变步长网络（Network 1）具有高于定步长网络（Network 2）可采样的高频活动时，对 Network 1 的输出应用平滑有时是有利的，因为它有助于您避免选取 Network 1 活动的局部峰值或谷值。Smoothing (continuous->discrete) 模块使用一阶滤波器从 Network 1 输出中移除不需要的高频信息，然后再将值提供给 Network 2。该模块实现是一个掩码子系统。

Smoothing (continuous->discrete) 子系统图
