---
type: simulink-block
title: 'radbasn'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'radbasn'
documentation_source_path: 'ref/radbasn.html'
language: zh-CN
chinese_source: worker-translation
---

# radbasn

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

**在 R2010b 中引入**

## 描述

归一化径向基传递函数

`radbasn` 是一种神经网络传递函数。传递函数根据网络的净输入计算层的输出。此函数等效于 radbas，不同之处在于输出向量通过除以归一化前的值之和进行归一化。

`A = radbasn(N,FP)` 接受一个或两个输入，

|  |  |
| --- | --- |
| `N` | `S`×`Q` 的净输入（列）向量矩阵 |
| `FP` | 函数参数结构体（忽略） |

并返回 `A`，一个 `S`×`Q` 矩阵，表示对 `N` 的每个元素应用径向基函数的结果。
