---
type: simulink-block
title: 'fixunknowns'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'fixunknowns'
documentation_source_path: 'ref/fixunknowns.html'
language: zh-CN
chinese_source: worker-translation
---

# fixunknowns

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

通过标记含有未知值的行来处理数据

`fixunknowns` 通过将每个包含未知值（由 `NaN` 表示）的行替换为两行信息来处理矩阵。

第一行包含原始行，其中 `NaN` 值被替换为该行的均值。第二行包含 1 和 0 值，分别指示第一行中哪些值是已知的或未知的。

`[y,ps] = fixunknowns(X)` 接受以下输入，

|  |  |
| --- | --- |
| `X` | `N`×`Q` 矩阵 |

并返回

|  |  |
| --- | --- |
| `Y` | `M`×`Q` 矩阵，其中添加了 `M - N` 行 |
| `PS` | 允许对值进行一致处理的处理设置 |

`[y,ps] = fixunknowns(X,FP)` 接受参数的空结构体 `FP`。

`Y = fixunknowns('apply',X,PS)` 在给定 `X` 和设置 `PS` 的情况下返回 `Y`。

`X = fixunknowns('reverse',Y,PS)` 在给定 `Y` 和设置 `PS` 的情况下返回 `X`。

`name = fixunknowns('name')` 返回此处理方法的名称。

`fp = fixunknowns('pdefaults')` 返回默认的处理参数结构体。

`pd = fixunknowns('pdesc')` 返回处理参数描述。

`fixunknowns('pcheck',fp)` 如果任何参数非法则抛出错误。
