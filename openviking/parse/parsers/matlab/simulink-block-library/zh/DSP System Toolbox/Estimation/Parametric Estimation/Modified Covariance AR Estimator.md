---
type: simulink-block
title: 'Modified Covariance AR Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Parametric Estimation'
documentation_page: 'modifiedcovariancearestimator'
documentation_source_path: 'ref/modifiedcovariancearestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Modified Covariance AR Estimator

## 端口

### 输入

### **Input** — 输入列向量 | 未定向向量

将输入数据指定为列向量或未定向向量。该模块假设输入数据是由白噪声驱动的 AR 系统的输出，并表示来自单通道信号的一帧连续时间样本。

**数据类型：** `single` | `double`

### 输出

### **A** — AR 模型多项式系数的归一化估计列向量

AR 模型多项式系数 *A*(*z*) 的归一化估计，返回为按 *z* 的降幂排列、长度为 *p*+1 的列向量。

该模块针对每个连续输入帧独立计算这些系数的估计。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) —— 估计的 AR 模型的传递函数
- *G* —— 标量增益
- *A*(*z*) —— AR 模型的多项式系数

**数据类型：** `single` | `double`

### **G** — 模型增益标量

估计的 AR 模型的增益，返回为标量。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) —— 估计的 AR 模型的传递函数
- *G* —— 标量增益
- *A*(*z*) —— AR 模型的多项式系数

**数据类型：** `single` | `double`

## 参数

### **Estimation order** — AR 模型的阶数 `4`（默认）| 正整数

将 AR 模型（全极点模型）的估计阶数 *p* 指定为正整数。为保证输出非奇异，必须将 **Estimation order** 参数设置为小于或等于输入向量长度的三分之二。否则，输出可能为奇异。

## 所属库

DSP System Toolbox / Estimation / Parametric Estimation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用修正协方差方法计算自回归 (AR) 模型参数的估计

Modified Covariance AR Estimator 模块使用修正协方差方法将自回归 (AR) 模型拟合到输入数据。此方法在最小二乘意义上最小化前向和后向预测误差。
