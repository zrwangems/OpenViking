---
type: simulink-block
title: 'Burg AR Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Parametric Estimation'
documentation_page: 'burgarestimator'
documentation_source_path: 'ref/burgarestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Burg AR Estimator

## 端口
```yaml
ports:
- name: Input
  summary: 输入列向量 | 无定向向量
  direction: input
  data_types: single | double
- name: A
  summary: AR 模型多项式系数的归一化估计 列向量
  direction: output
  data_types: single | double
- name: K
  summary: 反射系数 列向量
  direction: output
  data_types: single | double
- name: G
  summary: 模型增益 标量
  direction: output
  data_types: single | double
```

### 输入

### **Input** — 输入列向量 | 无定向向量

将输入数据指定为列向量或无定向向量。该模块假设输入数据是由白噪声驱动的 AR 系统的输出，并表示来自单通道信号的一帧连续时间采样。

**数据类型：** `single` | `double`
### 输出

### **A** — AR 模型多项式系数的归一化估计 列向量

AR 模型多项式系数 *A*(*z*) 的归一化估计，以按 *z* 的降幂排列的长度为 *p*+1 的列向量形式返回。

该模块对每个连续输入帧独立计算这些系数的估计值。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) —— 估计的 AR 模型的传递函数
- *G* —— 标量增益
- *A*(*z*) —— AR 模型的多项式系数

#### 依赖

要启用此端口，请将 **Output(s)** 参数设置为 `A` 或 `A and K`。

**数据类型：** `single` | `double`

### **K** — 反射系数 列向量

反射系数（Levinson 递推的次要结果），以长度为 *p* 的列向量形式返回。

#### 依赖

要启用此端口，请将 **Output(s)** 参数设置为 `K` 或 `A and K`。

**数据类型：** `single` | `double`

### **G** — 模型增益 标量

估计的 AR 模型的增益，以标量形式返回。

H(z)=GA(z)=G1+a(2)z−1+…+a(p+1)z−p

其中，

- *H*(*z*) —— 估计的 AR 模型的传递函数
- *G* —— 标量增益
- *A*(*z*) —— AR 模型的多项式系数

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Output(s)
  summary: 输出 A（默认）| A and K | K
  group: ''
- name: Inherit estimation order from input dimensions
  summary: 从输入维度继承估计阶数 on（默认）| off
  group: ''
- name: Estimation order
  summary: AR 模型的阶数 4（默认）| 非负整数
  group: ''
```

### **Output(s)** — 输出 `A`（默认）| `A and K` | `K`

指定模块输出模型系数（`A`）、反射系数（`K`）还是两者都输出（`A and K`）。

### **Inherit estimation order from input dimensions** — 从输入维度继承估计阶数 `on`（默认）| `off`

当您选中 **Inherit estimation order from input dimensions** 参数时，模块将全极点模型的阶数 *p* 设置为比输入向量长度小 1 的值。否则，阶数为您在 **Estimation order** 参数中指定的值。

### **Estimation order** — AR 模型的阶数 `4`（默认）| 非负整数

将 AR 模型的阶数 *p* 指定为非负整数。

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

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Burg 方法计算自回归（AR）模型参数的估计

Burg AR Estimator 模块使用 Burg 方法，通过最小化（最小二乘）前向和后向预测误差，同时约束 AR 参数满足 Levinson-Durbin 递推，来将自回归（AR）模型拟合到输入数据。
