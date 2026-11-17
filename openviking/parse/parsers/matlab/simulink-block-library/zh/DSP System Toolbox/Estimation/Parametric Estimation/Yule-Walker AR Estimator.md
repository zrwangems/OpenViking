---
type: simulink-block
title: 'Yule-Walker AR Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Parametric Estimation'
documentation_page: 'yulewalkerarestimator'
documentation_source_path: 'ref/yulewalkerarestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Yule-Walker AR Estimator

## 端口

### 输入

### **Input** — 输入向量 | 矩阵

将输入数据指定为向量或矩阵。该模块假定输入数据是由白噪声驱动的 AR 系统的输出。

当您指定矩阵时，该模块将矩阵的每一列视为一个通道。如果输入是长度为 *N* 的行向量，则该模块将输入视为具有 *N* 个不同通道。如果输入是无向向量，则该模块将输入视为单通道。

#### 依赖

要使用行向量作为输入，请将 **Output(s)** 设置为 `A`。

**数据类型：** `single` | `double`
### 输出

### **A** — AR 模型多项式系数的归一化估计 向量 | 矩阵

AR 模型多项式系数 *A*(*z*) 的归一化估计，以向量或矩阵形式返回。如果输出是向量，则其长度为 *p*+1，按 *z* 的降幂排列。如果输出是矩阵，则矩阵的每一列长度为 *p*+1，包含按 *z* 的降幂排列的 AR 模型系数的归一化估计。

该模块对每个连续输入帧独立计算这些系数的估计。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) —— 估计的 AR 模型的传递函数
- *G* —— 模型增益的平方
- *A*(*z*) —— AR 模型的多项式系数

#### 依赖

要启用此端口，请将 **Output(s)** 参数设置为 `A` 或 `A and K`。

**数据类型：** `single` | `double`

### **K** — 反射系数 列向量 | 无向向量 | 矩阵

反射系数（Levinson 递推的次要结果），以列向量、长度为 *p* 的无向向量或大小为 *p*×*N* 的矩阵形式返回，其中 *N* 是输入通道数。对于每个输入通道，端口 **K** 输出一个长度为 *p* 的列，其元素为 AR 模型反射系数。

#### 依赖

要启用此端口，请将 **Output(s)** 参数设置为 `K` 或 `A and K`。

要输出反射系数 *K*，请将输入指定为行向量、无向向量或矩阵。

**数据类型：** `single` | `double`

### **G** — 模型增益的平方 标量 | 向量

每个输入通道的估计 AR 模型增益的平方，以标量或长度为 *N* 的向量形式返回，其中 *N* 是输入通道数。端口 **G** 为每个通道输出一个标量。

以下是估计的 AR 模型的传递函数方程，其中显示了模型的增益和多项式系数：

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) —— 估计的 AR 模型的传递函数
- *G* —— 模型增益的平方
- *A*(*z*) —— AR 模型的多项式系数

**数据类型：** `single` | `double`

## 参数

### **Output(s)** — AR 模型系数的输出 `A`（默认）| `A and K` | `K`

指定该模块输出模型系数（`A`）、反射系数（`K`）还是两者都输出（`A and K`）。

### **Inherit estimation order from input dimensions** — 从输入维度继承估计阶数 `on`（默认）| `off`

当您选中 **Inherit estimation order from input dimensions** 参数时，该模块将全极点模型的阶数 *p* 设置为比每个输入通道的长度小 1 的值。否则，阶数为您在 **Estimation order** 参数中指定的值。

### **Estimation order** — AR 模型的阶数 `4`（默认）| 非负整数

将 AR 模型的阶数 *p* 指定为非负整数。

为保证有效输出，您必须将 **Estimation order** 参数设置为小于或等于输入通道长度一半的标量。

#### 依赖

要启用此参数，请清除 **Inherit estimation order from input dimensions** 参数。

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

使用 Yule-Walker 方法计算自回归（AR）模型参数的估计

Yule-Walker AR Estimator 模块使用 Yule-Walker AR 方法（也称为自相关方法），通过最小化最小二乘意义下的前向预测误差，将自回归（AR）模型拟合到加窗输入数据。此过程产生 Yule-Walker 方程，该模块使用 Levinson-Durbin 递推求解这些方程。该模块的输出始终是非奇异的。
