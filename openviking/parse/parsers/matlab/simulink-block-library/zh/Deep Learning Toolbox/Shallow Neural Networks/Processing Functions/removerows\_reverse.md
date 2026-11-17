---
type: simulink-block
title: 'removerows'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'removerows'
documentation_source_path: 'ref/removerows.html'
language: zh-CN
chinese_source: worker-translation
---

# removerows

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

通过移除指定索引的行来处理矩阵

`removerows` 通过移除指定索引的行来处理矩阵。

`[Y,PS] = removerows(X,'ind',ind)` 接受 `X` 和一个可选参数，

|  |  |
| --- | --- |
| `X` | `N`×`Q` 矩阵 |
| `ind` | 要移除的行索引向量（默认为 `[]`） |

并返回

|  |  |
| --- | --- |
| `Y` | `M`×`Q` 矩阵，其中 `M == N-length(ind)` |
| `PS` | 允许对值进行一致处理的处理设置 |

`[Y,PS] = removerows(X,FP)` 将参数作为结构体接受：`FP.ind`。

`Y = removerows('apply',X,PS)` 在给定 `X` 和设置 `PS` 的情况下返回 `Y`。

`X = removerows('reverse',Y,PS)` 在给定 `Y` 和设置 `PS` 的情况下返回 `X`。

`dx_dy = removerows('dx',X,Y,PS)` 返回 `Y` 关于 `X` 的 `M`×`N`×`Q` 导数。

`dx_dy = removerows('dx',X,[],PS)` 返回导数，效率较低。

`name = removerows('name')` 返回此处理方法的名称。

`fp = removerows('pdefaults')` 返回默认的处理参数结构体。

`names = removerows('pdesc')` 返回处理参数描述。

`removerows('pcheck',FP)` 如果任何参数非法则抛出错误。
