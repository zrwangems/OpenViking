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
```yaml
ports:
- name: u
  summary: 具有固定步长采样的信号 real scalar
  direction: input
- name: y
  summary: 对变步长网络的预测 real scalar
  direction: output
```

### 输入

### **u** — 具有固定步长采样的信号 real scalar

将此端口连接到固定步长网络，即 Network 2，以捕获其输出。
### 输出

### **y** — 对变步长网络的预测 real scalar

将此端口连接到变步长网络，即 Network 1 的输入。
## 参数
```yaml
parameters:
- name: Port u discrete sample time (s)
  summary: 指定固定步长网络的采样时间 -1 (default) | positive scalar
  group: ''
```

### **Port u discrete sample time (s)** — 指定固定步长网络的采样时间 `-1` (default) | positive scalar

以秒为单位指定固定步长网络，即 Network 2，的采样时间。
## 所属库

Simscape / Utilities / Network Couplers / Fundamental Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

在将固定步长网络连接到变步长网络时防止精度损失

**注意**

预测和平滑算法内置于 Network Coupler 模块中，您
可以通过模块对话框中的复选框启用它们。Fundamental Components 子库中的预测和平滑
模块仅供您参考。

将变步长网络（Network 1）连接到固定步长网络（Network 2）时，当 Network 1 的采样时间介于 Network 2 的采样时间之间时，可能会导致 Network 1 仿真中的精度损失。Prediction (discrete->continuous) 模块有助于
防止精度损失。它通过使用 Network 2 输出的最后计算导数来预测 Network 2 在其采样时间之间的输出，并将采样间
预测提供给 Network 1。该模块实现是一个掩码子系统。

Prediction (discrete->continuous) 子系统图
