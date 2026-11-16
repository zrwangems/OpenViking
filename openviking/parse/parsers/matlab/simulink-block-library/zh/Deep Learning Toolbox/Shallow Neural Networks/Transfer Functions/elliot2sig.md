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

R2025b 中未记录。

## 参数

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

Elliot 2 对称 S 型传递函数

传递函数将神经网络层的净输入转换为净输出。此函数是原始 Elliot S 型函数的变体。它的斜率更陡，更接近 `tansig`，但在中心处不如其平滑。

`A = elliot2sig(N)` 接受一个由 `S` 个 `N` 元素净输入列向量组成的 `S`×`Q` 矩阵，并返回一个 `S`×`Q` 的输出向量矩阵 `A`，其中 `N` 的每个元素都通过一个“S 形”函数从区间 `[-inf inf]` 压缩到区间 `[-1 1]`。

与其他 S 型函数相比，此传递函数的优势在于，在简单计算硬件上计算速度快，因为它不需要任何指数函数或三角函数。其缺点是，它在零点附近偏离经典 S 型形状。
