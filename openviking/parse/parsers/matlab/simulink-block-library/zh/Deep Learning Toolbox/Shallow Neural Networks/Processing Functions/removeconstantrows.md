---
type: simulink-block
title: 'removeconstantrows'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'removeconstantrows'
documentation_source_path: 'ref/removeconstantrows.html'
language: zh-CN
chinese_source: worker-translation
---

# removeconstantrows

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

**在 R2006a 中引入**

## 描述

通过删除具有常量值的行来处理矩阵

`removeconstantrows` 通过删除具有常量值的行来处理矩阵。

`[Y,PS] = removeconstantrows(X,max_range)` 接受 `X`
和一个可选参数，

|  |  |
| --- | --- |
| `X` | `N`×`Q` 矩阵 |
| `max_range` | 要删除的行的最大取值范围（默认值为 0） |

并返回

|  |  |
| --- | --- |
| `Y` | 已删除 `N` `-` `M` 行的 `M`×`Q` 矩阵 |
| `PS` | 允许对值进行一致处理的处理设置 |

`[Y,PS] = removeconstantrows(X,FP)` 以结构体形式接受参数：
`FP.max_range`。

`Y = removeconstantrows('apply',X,PS)` 在给定 `X` 和设置 `PS` 的情况下返回 `Y`。

`X = removeconstantrows('reverse',Y,PS)` 在给定 `Y` 和设置 `PS` 的情况下返回 `X`。

输入矩阵中的任何 `NaN` 值都被视为缺失数据，并且不被视为唯一值。因此，例如，`removeconstantrows`
会从矩阵 `[1 1 1 NaN; 1 1 1 2]` 中删除第一行。
