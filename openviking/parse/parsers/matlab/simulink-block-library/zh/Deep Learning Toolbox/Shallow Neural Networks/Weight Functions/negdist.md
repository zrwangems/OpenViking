---
type: simulink-block
title: 'negdist'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Weight Functions'
documentation_page: 'negdist'
documentation_source_path: 'ref/negdist.html'
language: zh-CN
chinese_source: worker-translation
---

# negdist

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

负距离权重函数

`negdist` 是一种权重函数。权重函数对输入应用权重以获得加权输入。

`Z = negdist(W,P)` 接受以下输入，

|  |  |
| --- | --- |
| `W` | `S`×`R` 权重矩阵 |
| `P` | `R`×`Q` 的 `Q` 个输入（列）向量矩阵 |
| `FP` | 函数参数的行元胞数组（可选，忽略） |

并返回 `S`×`Q` 的负向量距离矩阵。

`dim = negdist('size',S,R,FP)` 接受层维度
`S`、输入维度 `R` 和函数参数，并返回权重尺寸 [`S`×`R`]。

`dw = negdist('dz_dw',W,P,Z,FP)` 返回
`Z` 关于 `W` 的导数。
