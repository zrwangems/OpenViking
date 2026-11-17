---
type: simulink-block
title: 'poslin'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'poslin'
documentation_source_path: 'ref/poslin.html'
language: zh-CN
chinese_source: worker-translation
---

# poslin

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

正线性传递函数

`poslin` 是一种神经网络传递函数。传递函数根据其净输入计算某一层的输出。

`A = poslin(N,FP)` 接受 `N` 和可选的函数参数，

|  |  |
| --- | --- |
| `N` | 净输入（列）向量的 `S`×`Q` 矩阵 |
| `FP` | 函数参数的结构体（忽略） |

并返回 `A`，即 `N` 的元素被裁剪到 `[0, inf]` 后的 `S`×`Q` 矩阵。

`info = poslin('code')` 返回关于此函数的信息。支持以下代码：

`poslin('name')` 返回此函数的名称。

`poslin('output',FP)` 返回 `[min max]` 输出范围。

`poslin('active',FP)` 返回 `[min max]` 活动范围。

`poslin('fullderiv')` 返回 1 或 0，取决于 `dA_dN` 是 `S`×`S`×`Q` 还是 `S`×`Q`。

`poslin('fpnames')` 返回函数参数的名称。

`poslin('fpdefaults')` 返回默认函数参数。
