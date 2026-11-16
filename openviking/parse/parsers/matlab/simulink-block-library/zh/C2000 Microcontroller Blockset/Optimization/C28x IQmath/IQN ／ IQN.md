---
type: simulink-block
title: 'C2000 Division IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000divisioniqn'
documentation_source_path: 'ref/c2000divisioniqn.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Division IQN

## 端口

在 R2025b 中未记录。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

在 R2025b 中未记录。

## 描述

对 IQ 数进行除法

此模块使用 Newton-Raphson 技术对两个采用相同 Q format 的数进行相除。所得商使用与输入相同的 Q format。

**注意**

在代码生成期间，此模块的实现不会调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q format。有关详细信息，请参阅 Using the IQmath Library。
