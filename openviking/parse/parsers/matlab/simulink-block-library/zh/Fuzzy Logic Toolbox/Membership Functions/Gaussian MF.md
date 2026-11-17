---
type: simulink-block
title: 'Gaussian MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'gaussianmf'
documentation_source_path: 'gaussianmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Gaussian MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度一致。**MF** 的每个元素是为 **x** 中对应元素计算得到的隶属度值。

## 参数

### **Standard deviation sigma** — 标准差 `1`（默认）| 标量

高斯函数的标准差 *σ*。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sigma` |
| **类型：** string、字符向量 |
| **默认：** `"1"` |

### **Mean c** — 均值 `0`（默认）| 标量

高斯函数的均值 *c*。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mu` |
| **类型：** string、字符向量 |
| **默认：** `"0"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

高斯隶属函数

Gaussian MF 模块实现基于对称高斯函数的隶属函数。

f(x;σ,c)=e−(x−c)22σ2

其中，*c* 是高斯函数的均值，*σ* 是高斯函数的标准差。

高斯隶属函数与高斯概率分布不同。例如，高斯隶属函数的最大值始终为 `1`。有关高斯概率分布的更多信息，请参阅 Normal Distribution (Statistics and Machine Learning Toolbox)。
