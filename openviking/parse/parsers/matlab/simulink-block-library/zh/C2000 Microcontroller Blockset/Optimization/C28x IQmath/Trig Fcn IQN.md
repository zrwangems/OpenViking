---
type: simulink-block
title: 'C2000 Trig Fcn IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000trigfcniqn'
documentation_source_path: 'ref/c2000trigfcniqn.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Trig Fcn IQN

## 端口

R2025b 中未记录。

## 参数

**Function**
:   要计算的三角函数类型：

    - `_IQsin` — 计算正弦
      `(sin(A))`，其中 A 以 radians 为单位。
    - `_IQsinPU` — 计算标幺正弦
      `(sin(2*pi*A))`，其中 A 以 per-unit radians 为单位。
    - `_IQcos` — 计算余弦
      `(cos(A))`，其中 A 以 radians 为单位。
    - `_IQcosPU` — 计算标幺余弦
      `(cos(2*pi*A))`，其中 A 以 per-unit radians 为单位。

**Function**
:   要计算的三角函数类型：

    - `_IQsin` — 计算正弦
      `(sin(A))`，其中 A 以 radians 为单位。
    - `_IQsinPU` — 计算标幺正弦
      `(sin(2*pi*A))`，其中 A 以 per-unit radians 为单位。
    - `_IQcos` — 计算余弦
      `(cos(A))`，其中 A 以 radians 为单位。
    - `_IQcosPU` — 计算标幺余弦
      `(cos(2*pi*A))`，其中 A 以 per-unit radians 为单位。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

IQ 数的正弦、余弦或反正切

# C2000 Trig Fcn IQN

IQ 数的正弦、余弦或反正切

此模块计算基本三角函数，并将结果作为 IQ 数返回。`_IQsinPU` 和 `_IQcosPU` 的有效 Q 值为 1 到 30。对于所有其他项，有效 Q 值为 1 到 29。

**注意**

此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关详细信息，请参阅 Using the IQmath Library。

- C2000 Trig Fcn IQN 模块
