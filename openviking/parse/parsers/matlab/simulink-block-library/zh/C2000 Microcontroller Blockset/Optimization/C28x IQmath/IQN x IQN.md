---
type: simulink-block
title: 'C2000 IQN x IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000iqnxiqn'
documentation_source_path: 'ref/c2000iqnxiqn.html'
language: zh-CN
chinese_source: official
---

# C2000 IQN x IQN

## 端口

R2025b 官方文档未提供。

## 参数

**乘法选项**
:   要执行的乘法类型：

    - **乘** - 将数字相乘。
    - **Multiply with Rounding** - 将数字相乘并对结果进行四舍五入。
    - **Multiply with Rounding and Saturation** - 将数字相乘，并将结果四舍五入并饱和至最大值。

**乘法选项**
:   要执行的乘法类型：

    - **乘** - 将数字相乘。
    - **Multiply with Rounding** - 将数字相乘并对结果进行四舍五入。
    - **Multiply with Rounding and Saturation** - 将数字相乘，并将结果四舍五入并饱和至最大值。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

将具有相同 Q 格式的 IQ 数相乘

本页采用了机器翻译。点击此处可查看英文原文。

# C2000 IQN x IQN

将具有相同 Q 格式的 IQ 数相乘

这个模块用于计算两个智商数值的乘积。它还可以对结果进行四舍五入和饱和处理。

**注意**

该模块的实现过程中，在代码生成期间不会调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而该模块使用的 MathWorks® 代码根据模块输入动态调整 Q 格式。有关更多信息，请参阅Using the IQmath Library。

- C2000 IQN x IQN block

##
