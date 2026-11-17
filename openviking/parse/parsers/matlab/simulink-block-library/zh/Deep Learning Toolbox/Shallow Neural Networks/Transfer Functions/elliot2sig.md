---
type: simulink-block
title: 'elliot2sig'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'elliot2sig'
documentation_source_path: 'ref/elliot2sig.html'
language: zh-CN
chinese_source: worker-translation
---

# elliot2sig

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012b 中引入**

## 描述

Elliot 2 对称 sigmoid 传递函数

传递函数将神经网络层的净输入转换为其净输出。此函数是原始 Elliot sigmoid 函数的一种变体。它具有更陡的斜率，更接近 `tansig`，但在中心处不如后者平滑。

`A = elliot2sig(N)` 接受一个 `S`×`Q` 的矩阵，该矩阵由 `S` 个 `N` 元素净输入列向量组成，并返回一个 `S`×`Q` 的输出向量矩阵 `A`，其中 `N` 的每个元素通过一个“S 形”函数从区间 `[-inf inf]` 压缩到区间 `[-1 1]`。

此传递函数相对于其他 sigmoid 函数的优势在于，它在简单的计算硬件上计算速度快，因为它不需要任何指数或三角函数。其缺点是在零点附近偏离了经典的 sigmoid 形状。
