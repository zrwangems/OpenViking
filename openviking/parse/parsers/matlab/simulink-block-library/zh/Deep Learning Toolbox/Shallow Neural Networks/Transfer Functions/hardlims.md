---
type: simulink-block
title: 'hardlims'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'hardlims'
documentation_source_path: 'ref/hardlims.html'
language: zh-CN
chinese_source: worker-translation
---

# hardlims

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

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

对称硬限幅传递函数

`hardlims` 是一种神经网络传递函数。传递函数根据其净输入计算层的输出。

`A = hardlims(N,FP)` 接受 `N` 和可选的函数参数，

|  |  |
| --- | --- |
| `N` | 净输入（列）向量的 `S`×`Q` 矩阵 |
| `FP` | 函数参数的结构体（忽略） |

并返回 `A`，即 `S`×`Q` 的 +1/–1 矩阵，其中 `N` ≥ 0 的位置为 +1。

`info = hardlims('code')` 根据指定的代码字符串返回信息：

`hardlims('name')` 返回此函数的名称。

`hardlims('output',FP)` 返回 `[min max]` 输出范围。

`hardlims('active',FP)` 返回 `[min max]` 活动输入范围。

`hardlims('fullderiv')` 返回 1 或 0，取决于 `dA_dN` 是 `S`×`S`×`Q` 还是 `S`×`Q`。

`hardlims('fpnames')` 返回函数参数的名称。

`hardlims('fpdefaults')` 返回默认函数参数。
