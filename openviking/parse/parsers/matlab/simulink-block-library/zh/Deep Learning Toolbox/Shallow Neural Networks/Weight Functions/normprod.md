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

`normprod` 是一个权重函数。权重函数将权重应用于输入以得到加权输入。

`Z = normprod(W,P,FP)` 接受以下输入，

|  |  |
| --- | --- |
| `W` | `S`×`R` 权重矩阵 |
| `P` | `R`×`Q` 矩阵，包含 `Q` 个输入（列）向量 |
| `FP` | 函数参数的行元胞数组（可选，忽略） |

并返回 `S`×`Q` 归一化点积矩阵。

`dim = normprod('size',S,R,FP)` 接受层维度 `S`、输入维度 `R` 和函数参数，并返回权重大小 [`S`×`R`]。

`dw = normprod('dz_dw',W,P,Z,FP)` 返回 `Z` 关于 `W` 的导数。
