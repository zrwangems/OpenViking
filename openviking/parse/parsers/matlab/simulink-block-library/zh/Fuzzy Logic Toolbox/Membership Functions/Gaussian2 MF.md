---
type: simulink-block
title: 'Gaussian2 MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'gaussian2mf'
documentation_source_path: 'gaussian2mf.html'
language: zh-CN
chinese_source: worker-translation
---

# Gaussian2 MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度一致。**MF** 的每个元素是对 **x** 中对应元素计算得到的隶属度值。

当 *c*1 ≤ *c*2 时，隶属函数在区间 [*c*1, *c*2] 上达到最大值 `1`。

否则，当 *c*1 > *c*2 时，最大值小于一。

## 参数

### **Standard deviation for left curve sigma1** — 左侧高斯标准差 `3`（默认）| 标量

左侧高斯函数的标准差 *σ*1。

#### 编程使用

|  |
| --- |
| **模块参数**：`sigma1` |
| **类型**：string, character vector |
| **默认值**：`"3"` |

### **Mean for left curve c1** — 左侧高斯均值 `-1`（默认）| 标量

左侧高斯函数的均值 *c*1。

#### 编程使用

|  |
| --- |
| **模块参数**：`mu1` |
| **类型**：string, character vector |
| **默认值**：`"-1"` |

### **Standard deviation for right curve sigma2** — 右侧高斯标准差 `1`（默认）| 标量

右侧高斯函数的标准差 *σ*2。

#### 编程使用

|  |
| --- |
| **模块参数**：`sigma2` |
| **类型**：string, character vector |
| **默认值**：`"1"` |

### **Mean for right curve c2** — 右侧高斯均值 `5`（默认）| 标量

右侧高斯函数的均值 *c*2。

#### 编程使用

|  |
| --- |
| **模块参数**：`mu2` |
| **类型**：string, character vector |
| **默认值**：`"5"` |

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

两个高斯隶属函数的组合

Gaussian2 MF 模块实现基于两个高斯函数组合的隶属函数。这两个高斯函数由以下方程给出。

f(x;σk,ck)=e−(x−ck)22σk2

其中 *k* = 1,2。参数 *c*1 和 *σ*1 是定义最左侧曲线的均值和标准差。参数 *c*2 和 *σ*2 是定义最右侧曲线的均值和标准差。
