---
type: simulink-block
title: 'Prediction (discrete->continuous)'
family: 'network-couplers'
product_id: 'network-couplers'
product_name: 'Network Couplers'
documentation_release: R2025b
official_category: 'Fundamental Components'
documentation_page: 'predictiondiscretecontinuous'
documentation_source_path: '../simscape/ref/predictiondiscretecontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Prediction (discrete->continuous)

## 端口

### 输入

### **u** — 具有固定步长采样的 real scalar 信号

将该端口连接到固定步长网络 Network 2，以捕获其输出。

### 输出

### **y** — 对变步长网络的预测 real scalar

将该端口连接到变步长网络 Network 1 的输入。

## 参数

### **Port u 离散采样时间 (s)** — 指定固定步长网络的采样时间 `-1` (默认) | 正标量

以秒为单位指定固定步长网络 Network 2 的采样时间。

## 所属库

Simscape / Utilities / Network Couplers / Fundamental Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

在将固定步长网络连接到变步长网络时防止精度损失

**注意**

预测和平滑算法内置于 Network Coupler 模块中，您可以通过模块对话框中的复选框启用它们。Fundamental Components 子库中的预测和平滑模块仅供参考。

当变步长网络（Network 1）的采样时间介于固定步长网络（Network 2）的采样时间之间时，将变步长网络（Network 1）连接到固定步长网络（Network 2）可能会导致 Network 1 仿真中出现精度损失。Prediction (discrete->continuous) 模块有助于防止该精度损失。它通过使用 Network 2 输出的最近一次计算得到的导数，预测 Network 2 在其采样时间之间的输出，并将采样间预测提供给 Network 1。该模块实现为一个掩码子系统。

Prediction (discrete->continuous) 子系统图
