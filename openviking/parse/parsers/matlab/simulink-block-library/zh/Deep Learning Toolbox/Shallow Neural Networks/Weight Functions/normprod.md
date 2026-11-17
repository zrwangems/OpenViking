---
type: simulink-block
title: 'normprod'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Weight Functions'
documentation_page: 'normprod'
documentation_source_path: 'ref/normprod.html'
language: zh-CN
chinese_source: worker-translation
---

# normprod

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

归一化点积权重函数

`normprod` 是一种权重函数。权重函数对输入应用权重以获得加权输入。

`Z = normprod(W,P,FP)` 接受以下输入，

|  |  |
| --- | --- |
| `W` | `S`×`R` 权重矩阵 |
| `P` | `Q` 个输入（列）向量的 `R`×`Q` 矩阵 |
| `FP` | 函数参数的行元胞数组（可选，忽略） |

并返回归一化点积的 `S`×`Q` 矩阵。

`dim = normprod('size',S,R,FP)` 接受层维度
`S`、输入维度 `R` 和函数参数，并
返回权重尺寸 [`S`×`R`]。

`dw = normprod('dz_dw',W,P,Z,FP)` 返回
`Z` 关于 `W` 的导数。
