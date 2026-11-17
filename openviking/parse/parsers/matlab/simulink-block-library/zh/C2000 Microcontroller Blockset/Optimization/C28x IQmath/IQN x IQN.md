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
chinese_source: worker-translation
---

# C2000 IQN x IQN

## 端口

在 R2025b 中未记录。

## 参数

**乘法选项**
:   要执行的乘法类型：

    - `Multiply` — 将数字相乘。
    - `Multiply with Rounding` — 将数字相乘并对结果进行舍入。
    - `Multiply with Rounding and Saturation` — 将数字相乘，并将结果舍入和饱和到最大值。

**乘法选项**
:   要执行的乘法类型：

    - `Multiply` — 将数字相乘。
    - `Multiply with Rounding` — 将数字相乘并对结果进行舍入。
    - `Multiply with Rounding and Saturation` — 将数字相乘，并将结果舍入和饱和到最大值。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

将具有相同 Q 格式的 IQ 数字相乘

# C2000 IQN x IQN

将具有相同 Q 格式的 IQ 数字相乘

此模块将两个 IQ 数字相乘。可选地，它还可以对结果进行舍入和饱和。

**注意**

此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

- C2000 IQN x IQN 模块
