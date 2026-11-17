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
```yaml
ports:
- name: u
  summary: 采样较慢的信号 实数标量
  direction: input
- name: y
  summary: 较快网络的预测 实数标量
  direction: output
```

### 输入

### **u** — 采样较慢的信号 实数标量

将此端口连接到较慢的网络，即网络 2，以捕获其输出。
### 输出

### **y** — 较快网络的预测 实数标量

将此端口连接到较快网络，即网络 1 的输入。
## 参数
```yaml
parameters:
- name: 端口 u 离散采样时间 (s)
  summary: 指定较慢网络的采样时间 -1（默认）| 正标量
  group: ''
- name: 端口 y 离散采样时间 (s)
  summary: 指定较快网络的采样时间 -1（默认）| 正标量
  group: ''
```

### **端口 u 离散采样时间 (s)** — 指定较慢网络的采样时间 `-1`（默认）| 正标量

以秒为单位指定较慢网络，即网络 2 的采样时间。

### **端口 y 离散采样时间 (s)** — 指定较快网络的采样时间 `-1`（默认）| 正标量

以秒为单位指定较快网络，即网络 1 的采样时间。
## 所属库

Simscape / Utilities / Network Couplers / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：支持电气节点数组

为支持电气节点数组和三相连接，触发逻辑已更新。此前，仅输入 *u* 的第一个元素发生变化就会触发预测周期。现在，任何输入发生变化都会触发预测周期。因此，R2023b 中添加的两个选择器 (U->Y) 模块已被移除。

对于具有热节点数组的电池模型，仿真结果与之前版本相同。然而，对于节点数组元素之间没有物理耦合的模型，此更改可能导致触发逻辑发生变化，从而导致仿真结果出现轻微差异。

### R2023b：支持热节点数组

为支持热节点数组（Network Coupler (Thermal Mass) 模块所需），已在 Prediction (slow->fast) 模块图中添加两个选择器 (U->Y) 模块，以保持触发信号为标量。

此更改没有兼容性影响。如果打开现有模型，仿真结果与之前版本相同。

## 描述

防止连接具有不同步长的定步长网络时出现精度损失

**注意**

预测和平滑算法内置于 Network Coupler 模块中，您可以通过模块对话框中的复选框启用它们。Fundamental Components 子库中的预测和平滑模块仅供参考。

将采样较快的网络（网络 1）连接到采样较慢的网络（网络 2）时，如果网络 1 的采样时间介于网络 2 的采样时间之间，可能导致网络 1 仿真出现精度损失。Prediction (slow->fast) 模块有助于防止精度损失。它利用网络 2 输出的最后计算导数来预测网络 2 在其采样时间之间的输出。该模块实现为一个掩码子系统。

Prediction (slow->fast) 子系统图

该子系统包含以较慢和较快两种速率运行的模块。Delay 模块由较慢速率驱动，其输出的变化用作触发，使触发子系统捕获输入 *u* 的最新导数。离散时间积分器以较快速率运行，并使用此导数来预测输出 *y*，直到下一次触发事件发生。
