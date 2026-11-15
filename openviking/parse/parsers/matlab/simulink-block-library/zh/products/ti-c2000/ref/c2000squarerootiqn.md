---
type: simulink-block
title: 'C2000 Square Root IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x IQmath'
documentation_page: 'c2000squarerootiqn'
documentation_source_path: 'ref/c2000squarerootiqn.html'
language: zh-CN
chinese_source: official
---

# C2000 Square Root IQN

## 端口

R2025b 官方文档未提供。

## 参数

**函数**
:   是计算平方根还是平方根的倒数

    - **Square root (\_sqrt)** - 计算平方根。
    - **Inverse square root (\_isqrt)** - 计算平方根的倒数。

**函数**
:   是计算平方根还是平方根的倒数

    - **Square root (\_sqrt)** - 计算平方根。
    - **Inverse square root (\_isqrt)** - 计算平方根的倒数。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

智商数的平方根或倒数平方根

本页采用了机器翻译。点击此处可查看英文原文。

# C2000 Square Root IQN

智商数的平方根或倒数平方根

该模块计算智商数的平方根或平方根的倒数，并返回相同 Q 格式的智商数。该模块使用查表法和牛顿-拉夫逊近似法。

该模块的负输入将返回零值。

**注意**

该模块的实现过程中，在代码生成期间不会调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而该模块使用的 MathWorks® 代码根据模块输入动态调整 Q 格式。有关更多信息，请参阅Using the IQmath Library。

##
