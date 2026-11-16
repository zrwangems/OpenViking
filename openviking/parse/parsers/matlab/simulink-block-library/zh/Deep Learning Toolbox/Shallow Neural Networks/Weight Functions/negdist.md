---
type: simulink-block
title: 'negdist'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Weight Functions'
documentation_page: 'negdist'
documentation_source_path: 'ref/negdist.html'
language: zh-CN
chinese_source: worker-translation
---

# negdist

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

**在 R2006a 之前引入**

## 描述

负距离权重函数

`negdist` 是一种权重函数。权重函数将权重应用于输入以得到加权输入。

`Z = negdist(W,P)` 接受以下输入，

|  |  |
| --- | --- |
| `W` | `S`-by-`R` 权重矩阵 |
| `P` | `R`-by-`Q` 矩阵，包含 `Q` 个输入（列）向量 |
| `FP` | 函数参数的行元胞数组（可选，忽略） |

并返回负向量距离的 `S`-by-`Q` 矩阵。

`dim = negdist('size',S,R,FP)` 接受层维度 `S`、输入维度 `R` 和函数参数，并返回权重大小 [`S`-by-`R`]。

`dw = negdist('dz_dw',W,P,Z,FP)` 返回 `Z` 关于 `W` 的导数。
