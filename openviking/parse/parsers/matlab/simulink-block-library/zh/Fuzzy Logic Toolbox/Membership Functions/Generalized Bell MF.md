---
type: simulink-block
title: 'Generalized Bell MF'
family: 'membership-functions'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'generalizedbellmf'
documentation_source_path: 'generalizedbellmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Generalized Bell MF

## 端口

### 输入

### **x** — 输入值 标量 | 向量

为其计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度匹配。**MF** 的每个元素都是为 **x** 的对应元素计算得到的隶属度值。

## 参数

### **a** — 函数形状参数 `5`（默认）| 标量

与 **b** 一起定义隶属函数形状的参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认值：** `"5"` |

### **b** — 函数形状参数 `4`（默认）| 正标量

与 **a** 一起定义隶属函数形状的参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `b` |
| **类型：** string, character vector |
| **默认值：** `"4"` |

### **c** — 中心点 `0`（默认）| 标量

函数中心点。

#### 程序化使用

|  |
| --- |
| **模块参数：** `c` |
| **类型：** string, character vector |
| **默认值：** `"0"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成
使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

广义钟形隶属函数

Generalized Bell MF 模块实现基于广义钟形函数的隶属函数。

f(x;a,b,c)=11+|x−ca|2b

这里，*a* 和 *b* 控制函数的宽度，*c* 控制函数的中心。
