---
type: simulink-block
title: 'satlin'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'satlin'
documentation_source_path: 'ref/satlin.html'
language: zh-CN
chinese_source: worker-translation
---

# satlin

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

饱和线性传递函数

`satlin` 是一种神经网络传递函数。传递函数根据其净输入计算层的输出。

`A = satlin(N,FP)` 接受两个输入，

|  |  |
| --- | --- |
| `N` | `S`×`Q` 的净输入（列）向量矩阵 |
| `FP` | 函数参数的结构体（忽略） |

并返回 `A`，即 `N` 的元素被裁剪到 `[0, 1]` 范围内的 `S`×`Q` 矩阵。

`info = satlin('code')` 为每个支持的 *`code`* 字符向量返回有用的信息：

`satlin('name')` 返回此函数的名称。

`satlin('output',FP)` 返回 `[min max]` 输出范围。

`satlin('active',FP)` 返回 `[min max]` 活动输入范围。

`satlin('fullderiv')` 返回 1 或 0，取决于 `dA_dN` 是 `S`×`S`×`Q` 还是 `S`×`Q`。

`satlin('fpnames')` 返回函数参数的名称。

`satlin('fpdefaults')` 返回默认函数参数。
