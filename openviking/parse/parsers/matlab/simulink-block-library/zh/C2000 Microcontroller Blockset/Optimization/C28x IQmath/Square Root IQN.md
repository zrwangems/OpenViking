---
type: simulink-block
title: 'C2000 Square Root IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000squarerootiqn'
documentation_source_path: 'ref/c2000squarerootiqn.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Square Root IQN

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Function**
:   是计算平方根还是逆平方根

    - `Square root (_sqrt)` — 计算平方根。
    - `Inverse square root (_isqrt)` — 计算逆平方根。

**Function**
:   是计算平方根还是逆平方根

    - `Square root (_sqrt)` — 计算平方根。
    - `Inverse square root (_isqrt)` — 计算逆平方根。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

IQ 数的平方根或逆平方根

# C2000 Square Root IQN

IQ 数的平方根或逆平方根

此模块计算 IQ 数的平方根或逆平方根，并返回相同 Q 格式的 IQ 数。该模块使用查表和 Newton-Raphson 近似。

此模块的负输入返回值为零。

**注意**

此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关详细信息，请参阅 Using the IQmath Library。
