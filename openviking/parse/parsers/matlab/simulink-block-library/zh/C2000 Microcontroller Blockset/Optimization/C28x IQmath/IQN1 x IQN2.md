---
type: simulink-block
title: 'C2000 IQN1 x IQN2'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000iqn1xiqn2'
documentation_source_path: 'ref/c2000iqn1xiqn2.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 IQN1 x IQN2

## 端口

R2025b 中未记录。

## 参数

**Q 值**
:   Q 值，取值范围为 1 到 30，用于指定输出的精度

**Q 值**
:   Q 值，取值范围为 1 到 30，用于指定输出的精度

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

将具有不同 Q 格式的 IQ 数相乘

# C2000 IQN1 x IQN2

将具有不同 Q 格式的 IQ 数相乘

当两个 IQ 数以不同的 Q 格式表示时，此模块会将这两个 IQ 数相乘。结果的格式在对话框中指定。

**注意**

此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关详细信息，请参阅使用 IQmath 库。

- C2000 IQN1 x IQN2 模块
