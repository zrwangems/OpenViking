---
type: simulink-block
title: 'processpca'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'processpca'
documentation_source_path: 'ref/processpca.html'
language: zh-CN
chinese_source: worker-translation
---

# processpca

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

**在 R2006a 中引入**

## 描述

使用主成分分析处理矩阵的列

`processpca` 使用主成分分析处理矩阵，使得每一行不相关，各行按其总变异的贡献量排序，并且对总变异贡献小于 `maxfrac` 的行被移除。

`[Y,PS] = processpca(X,maxfrac)` 接受 `X` 和一个可选参数，

|  |  |
| --- | --- |
| `X` | `N`×`Q` 矩阵 |
| `maxfrac` | 被移除行的最大方差比例（默认值为 0） |

并返回

|  |  |
| --- | --- |
| `Y` | `M`×`Q` 矩阵，其中删除了 `N` `-` `M` 行 |
| `PS` | 允许对值进行一致处理的处理设置 |

`[Y,PS] = processpca(X,FP)` 接受参数作为结构体：
`FP.maxfrac`。

`Y = processpca('apply',X,PS)` 在给定 `X` 和设置 `PS` 的情况下返回 `Y`。

`X = processpca('reverse',Y,PS)` 在给定 `Y` 和设置 `PS` 的情况下返回 `X`。

`name = processpca('name')` 返回此处理方法的名称。

`fp = processpca('pdefaults')` 返回默认处理参数结构体。

`names = processpca('pdesc')` 返回处理参数描述。

`processpca('pcheck',fp);` 如果任何参数非法则抛出错误。
