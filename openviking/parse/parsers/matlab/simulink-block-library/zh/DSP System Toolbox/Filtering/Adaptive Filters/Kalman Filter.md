---
type: simulink-block
title: 'Kalman Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'kalmanfilter'
documentation_source_path: 'ref/kalmanfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Kalman Filter

## 端口

R2025b 中未记录。

## 参数

**Number of filters**
:   指定用于预测或估计当前值的滤波器数量。

**Enable filters**
:   指定每个时间步中哪些滤波器被启用或禁用。如果选择 `Always`，则滤波器始终启用。如果选择 `Specify via input port <Enable>`，则模块上会出现 Enable 端口。

**当滤波器被禁用时，重置估计状态和估计误差协方差**
:   如果选中此复选框，则与已禁用滤波器对应的估计状态和预测状态以及估计误差协方差将重置为其初始值。如果对于 **Enable filters** 参数选择了 `Specify via input port <Enable>`，则此参数可见。

**Initial condition for estimated state**
:   输入估计状态的初始条件。

**Initial condition for estimated error covariance**
:   输入估计误差协方差的初始条件。

**State transition matrix**
:   输入状态转移矩阵。

**Process noise covariance**
:   输入过程噪声协方差。

**Measurement matrix source**
:   指定如何输入测量矩阵值。如果选择 `Specify via dialog`，则对话框中会出现 **Measurement matrix** 参数。如果选择 `Input port <H>`，则模块上会出现 H 端口。

**Measurement matrix**
:   输入测量矩阵值。如果对于 **Measurement matrix source** 参数选择了 `Specify via dialog`，则此参数可见。

**Measurement noise covariance**
:   输入测量噪声协方差。

**Output estimated measurement <Z\_est>**
:   如果希望模块输出估计测量值，请选中此复选框。

**Output estimated state <X\_est>**
:   如果希望模块输出估计状态，请选中此复选框。

**Output MSE of estimated state <MSE\_est>**
:   如果希望模块输出估计状态的均方误差，请选中此复选框。

**Output predicted measurement <Z\_prd>**
:   如果希望模块输出预测测量值，请选中此复选框。

**Output predicted state <X\_prd>**
:   如果希望模块输出预测状态，请选中此复选框。

**Output MSE of predicted state <MSE\_prb>**
:   如果希望模块输出预测状态的均方误差，请选中此复选框。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

预测或估计动态系统的状态

使用 Kalman Filter 模块从一系列不完整和/或含噪测量中预测或估计动态系统的状态。假设有一个含噪线性系统由以下方程定义：

xk=Axk−1+wk−1zk=Hxk+vk

此模块可以使用先前估计的状态 x^k−1 来预测时间 *k* 处的当前状态 xk−，如下式所示：

xk−=Ax^k−1Pk−=AP^k−1AT+Q

此模块还可以使用当前测量 zk 和预测状态 xk− 来估计时间 *k* 处的当前状态值 x^k，使其成为更精确的近似：

Kk=Pk−HT(HPk−HT+R)−1x^k=xk−+Kk(zk−Hxk−)P^k=(I−KkH)Pk−

上式中各变量的定义如下表所示。

| 变量 | 定义 | 默认值或初始条件 |
| --- | --- | --- |
| *x* | 状态 | 不适用 |
| x^ | 估计状态 | `zeros([6, 1])` |
| x− | 预测状态 | 不适用 |
| *A* | 状态转移矩阵 | [101000010100001000000100000010000001] |
| *w* | 过程噪声 | 不适用 |
| *z* | 测量 | 不适用 |
| *H* | 测量矩阵 | [100000010000000010000001] |
| *v* | 测量噪声 | 不适用 |
| P^ | 估计误差协方差 | `10*eye(6)` |
| *P-* | 预测误差协方差 | 不适用 |
| *Q* | 过程噪声协方差 | `0.05*eye(6)` |
| *K* | 卡尔曼增益 | 不适用 |
| *R* | 测量噪声协方差 | `eye(4)` |
| *I* | 单位矩阵 | 不适用 |

在上述方程中，*z* 是测量值向量。大多数情况下，模块处理 Z，即一个 M×N 矩阵，其中 M 是测量值的数量，N 是滤波器的数量。

使用 **Number of filters** 参数指定用于预测或估计当前值的滤波器数量。

使用 **Enable filters** 参数指定每个时间步中哪些滤波器被启用或禁用。如果选择 `Always`，则滤波器始终启用。如果选择 `Specify via input port <Enable>`，则模块上会出现 Enable 端口。此端口的输入必须是长度为滤波器数量的由 1 和 0 组成的行向量。例如，如果有 3 个滤波器，并且 Enable 端口的输入为 [1 0 1]，则此时间步中仅启用第一个和第三个滤波器。如果选中 **当滤波器被禁用时，重置估计状态和估计误差协方差** 复选框，则与已禁用滤波器对应的估计状态和预测状态以及估计误差协方差将重置为其初始值。

**注意**

所有滤波器具有相同的状态转移矩阵、测量矩阵、初始条件和噪声协方差，但它们的状态、测量、启用和 MSE 信号是各自独立的。在状态、测量、启用和 MSE 信号中，每一列对应一个滤波器。

使用 **Measurement matrix source** 参数指定如何输入测量矩阵值。如果选择 `Specify via dialog`，则对话框中会出现 **Measurement matrix** 参数。如果选择 `Input port <H>`，则模块上会出现 H 端口。使用此端口指定测量矩阵。
