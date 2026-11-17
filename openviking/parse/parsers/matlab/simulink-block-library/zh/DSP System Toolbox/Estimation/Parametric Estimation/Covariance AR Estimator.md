---
type: simulink-block
title: 'Covariance AR Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Parametric Estimation'
documentation_page: 'covariancearestimator'
documentation_source_path: 'ref/covariancearestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Covariance AR Estimator

## 端口

### 输入

### **Input** — 输入列向量 | 无向向量

将输入数据指定为列向量或无向向量。该模块假设输入数据是由白噪声驱动的 AR 系统的输出，并表示来自单通道信号的一帧连续时间采样。

**数据类型：** `single` | `double`
### 输出

### **A** — AR 模型多项式系数的归一化估计 列向量

AR 模型多项式系数 *A*(*z*) 的归一化估计，以长度为 *p*+1 的列向量形式返回，按 *z* 的降幂排列。

该模块对每个连续输入帧独立计算这些系数的估计。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) –– 估计的 AR 模型的传递函数
- *G* –– 标量增益
- *A*(*z*) –– AR 模型的多项式系数

**数据类型：** `single` | `double`

### **G** — 模型增益 标量

估计的 AR 模型的增益，以标量形式返回。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) –– 估计的 AR 模型的传递函数
- *G* –– 标量增益
- *A*(*z*) –– AR 模型的多项式系数

**数据类型：** `single` | `double`

## 参数

### **Estimation order** — AR 模型的阶数 `4`（默认）| 正整数

将全极点 AR 模型的估计阶数 *p* 指定为正整数。为保证输出非奇异，必须将 *p* 设置为小于或等于输入向量长度的一半。否则，输出可能奇异。

## 所属库

DSP System Toolbox / Estimation / Parametric Estimation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用协方差方法计算自回归（AR）模型参数的估计

Covariance AR Estimator 模块使用协方差方法将自回归（AR）模型拟合到输入数据。该方法在最小二乘意义上最小化前向预测误差。
