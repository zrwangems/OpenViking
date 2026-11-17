---
type: simulink-block
title: 'Smoothing (fast->slow)'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Network Couplers / Fundamental Components'
documentation_page: 'smoothingfastslow'
documentation_source_path: '../simscape/ref/smoothingfastslow.html'
language: zh-CN
chinese_source: worker-translation
---

# Smoothing (fast->slow)

## 端口

### 输入

### **u** — 采样较快的信号 实数标量

将此端口连接到较快的网络，即 Network 1，以捕获其输出。
### 输出

### **y** — 用于较慢网络的平滑信号 实数标量

将此端口连接到较慢网络，即 Network 2 的输入。

## 参数

### **Number of samples over which to smooth** — 指定用于对输出求平均的样本数 `1`（默认）| 正标量

指定用于对较快网络 Network 1 的输出求平均的样本数。

### **Port u discrete sample time (s)** — 指定较快网络的采样时间 `-1`（默认）| 正标量

指定较快网络 Network 1 的采样时间，以秒为单位。

### **Initial output** — 指定初始输出值 `0`（默认）| 标量

指定较快网络 Network 1 的初始输出值。

## 所属库

Simscape / Utilities / Network Couplers / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b：支持热节点数组

为支持热节点数组（这是 Network Coupler (Thermal Mass) 模块所需的），已将 For Each 子系统层添加到 Smoothing (fast->slow) 模块图中。

此更改没有兼容性影响。如果打开现有模型，仿真结果与之前版本相同。

## 描述

在连接具有不同步长的固定步长网络时应用输出平滑

**注意**

预测和平滑算法内置于 Network Coupler 模块中，您可以通过模块对话框中的复选框启用它们。Fundamental Components 子库中的预测和平滑模块仅供参考。

当采样较快的网络（Network 1）具有高于较慢网络（Network 2）可采样频率的高频活动时，对 Network 1 的输出应用平滑有时会很有优势，因为这有助于避免选取 Network 1 活动的局部峰值或谷值。Smoothing (fast->slow) 模块向 Network 2 提供 Network 1 输出的平均值。该模块的实现是一个掩码子系统，如第一个模块图所示。第二个图显示了第一个图中 For Each 子系统的内容。

Smoothing (fast->slow) 子系统图

For Each 子系统图

平滑的工作原理是对最后 *N* 个样本求平均。您可以使用 **Number of samples over which to smooth** 参数指定 *N*。
