---
type: simulink-block
title: 'tribas'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'tribas'
documentation_source_path: 'ref/tribas.html'
language: zh-CN
chinese_source: worker-translation
---

# tribas

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

**在 R2006a 之前引入**

## 描述

三角基传递函数

`tribas` 是一种神经网络传递函数。传递函数根据网络的净输入计算层的输出。

`A = tribas(N,FP)` 接受 `N` 和可选的函数参数，

|  |  |
| --- | --- |
| `N` | `S`×`Q` 的净输入（列）向量矩阵 |
| `FP` | 函数参数的结构体（忽略） |

并返回 `A`，一个 `S`×`Q` 矩阵，表示对 `N` 的每个元素应用三角基函数的结果。

`info = tribas('code')` 可以采用以下形式返回特定信息：

`tribas('name')` 返回此函数的名称。

`tribas('output',FP)` 返回 `[min max]` 输出范围。

`tribas('active',FP)` 返回 `[min max]` 有效输入范围。

`tribas('fullderiv')` 返回 1 或 0，取决于 `dA_dN` 是 `S`×`S`×`Q` 还是 `S`×`Q`。

`tribas('fpnames')` 返回函数参数的名称。

`tribas('fpdefaults')` 返回默认函数参数。
