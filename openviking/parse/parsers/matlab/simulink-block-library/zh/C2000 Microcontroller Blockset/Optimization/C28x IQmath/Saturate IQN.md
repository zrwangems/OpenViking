---
type: simulink-block
title: 'C2000 Saturate IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000saturateiqn'
documentation_source_path: 'ref/c2000saturateiqn.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Saturate IQN

## 端口

R2025b 中未记录。

## 参数

**Upper Limit**
:   要饱和到的最大实世界值

**Lower Limit**
:   要饱和到的最小实世界值

**Upper Limit**
:   要饱和到的最大实世界值

**Lower Limit**
:   要饱和到的最小实世界值

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

对 IQ 数进行饱和处理

# C2000 Saturate IQN

对 IQ 数进行饱和处理

此模块将输入 IQ 数饱和到指定的上限和下限。
返回值是与输入具有相同 Q 值的 IQ 数。

**注意**

此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q
设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关
更多信息，请参阅 Using the IQmath Library。

- C2000 Saturate IQN 模块
