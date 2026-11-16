---
type: simulink-block
title: 'Prediction (slow->fast)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers / Fundamental Components'
documentation_page: 'predictionslowfast'
documentation_source_path: '../simscape/ref/predictionslowfast.html'
language: zh-CN
chinese_source: worker-translation
---

# Prediction (slow->fast)

## 端口

### 输入

### **u** — 具有较慢采样的信号 real scalar

将此端口连接到较慢的网络 Network 2，以采集其输出。

### 输出

### **y** — 对较快网络的预测 real scalar

将此端口连接到较快网络 Network 1 的输入。

## 参数

### **端口 u 离散采样时间 (s)** — 指定较慢网络的采样时间 `-1` (默认) | positive scalar

指定较慢网络 Network 2 的采样时间，以 seconds 为单位。

### **端口 y 离散采样时间 (s)** — 指定较快网络的采样时间 `-1` (默认) | positive scalar

指定较快网络 Network 1 的采样时间，以 seconds 为单位。

## 所属库

Simscape / Utilities / Network Couplers / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：支持电气节点数组

为了支持电气节点数组和三相连接，触发逻辑已更新。以前，仅输入 *u* 的第一个元素发生变化就会触发预测周期。现在，任一输入发生变化都会触发预测周期。因此，在 R2023b 中添加的两个 selector (U->Y) 模块已被移除。

对于具有热节点数组的电池模型，仿真结果与先前版本相同。但是，对于节点数组中的元素未物理耦合的模型，此更改可能会导致触发逻辑变化，从而导致仿真结果略有差异。

### R2023b：支持热节点数组

为了支持热节点数组（Network Coupler (Thermal Mass) 模块所需），已将两个 selector (U->Y) 模块添加到 Prediction (slow->fast) 模块图中，以保持触发信号为 scalar。

此更改没有兼容性影响。如果打开现有模型，仿真结果与先前版本相同。

## 描述

防止连接具有不同步长的定步长网络时出现精度损失

**注意**

预测和平滑算法内置于 Network Coupler 模块中，您可以通过模块对话框中的复选框启用它们。Fundamental Components 子库中的预测和平滑模块仅供参考。

将具有较快采样的网络 (Network 1) 连接到具有较慢采样的网络 (Network 2) 时，如果其采样时间介于 Network 2 的采样时间之间，则可能导致 Network 1 仿真中出现精度损失。Prediction (slow->fast) 模块有助于防止精度损失。它通过使用 Network 2 输出的最后计算导数，在 Network 2 的采样时间之间预测 Network 2 的输出。该模块实现是一个掩码子系统。

Prediction (slow->fast) 子系统图

该子系统包含以较慢和较快速率运行的模块。Delay 模块由较慢速率驱动，其输出变化用作触发，以便触发子系统捕获输入 *u* 的最新导数。discrete-time integrator 以较快速率运行，并使用此导数预测输出 *y*，直到下一个触发事件发生。
