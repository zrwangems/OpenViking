---
type: simulink-block
title: 'netprod'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Net Input Functions'
documentation_page: 'netprod'
documentation_source_path: 'ref/netprod.html'
language: zh-CN
chinese_source: worker-translation
---

# netprod

## 端口

未在 R2025b 中记录。

## 参数

未在 R2025b 中记录。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

乘积净输入函数

`netprod` 是一个净输入函数。净输入函数通过组合层的加权输入和偏置来计算该层的净输入。

`N = netprod({Z1,Z2,...,Zn})` 接受

|  |  |
| --- | --- |
| `Zi` | 行元胞数组中的 `S`-by-`Q` 矩阵 |

并返回 `Z1` 到 `Zn` 的逐元素乘积。

`info = netprod('code')` 返回有关此函数的信息。支持以下代码：

|  |  |
| --- | --- |
| `'deriv'` | 导数函数的名称 |
| `'fullderiv'` | 完整 `N`-by-`S`-by-`Q` 导数 = 1，逐元素 `S`-by-`Q` 导数 = 0 |
| `'name'` | 全名 |
| `'fpnames'` | 返回函数参数的名称 |
| `'fpdefaults'` | 返回默认函数参数 |
