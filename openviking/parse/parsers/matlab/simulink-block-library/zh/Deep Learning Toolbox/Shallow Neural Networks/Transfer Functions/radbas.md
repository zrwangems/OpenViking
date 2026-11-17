---
type: simulink-block
title: 'radbas'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'radbas'
documentation_source_path: 'ref/radbas.html'
language: zh-CN
chinese_source: worker-translation
---

# radbas

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

径向基传递函数

`radbas` 是一种神经传递函数。传递函数根据其净输入计算某层的输出。

`A = radbas(N,FP)` 接受一个或两个输入，

|  |  |
| --- | --- |
| `N` | `S`×`Q` 的净输入（列）向量矩阵 |
| `FP` | 函数参数结构体（忽略） |

并返回 `A`，一个 `S`×`Q` 矩阵，即对 `N` 的每个元素应用径向基函数的结果。
