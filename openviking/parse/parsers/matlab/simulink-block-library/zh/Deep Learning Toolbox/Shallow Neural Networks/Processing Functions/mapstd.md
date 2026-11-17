---
type: simulink-block
title: 'mapstd'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'mapstd'
documentation_source_path: 'ref/mapstd.html'
language: zh-CN
chinese_source: worker-translation
---

# mapstd

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

**在 R2006a 中引入**

## 描述

通过将每一行的均值映射为 0、偏差映射为 1 来处理矩阵

`mapstd` 通过将每一行的均值和标准差变换为 `ymean` 和 `ystd` 来处理矩阵。

`[Y,PS] = mapstd(X,ymean,ystd)` 接受 `X` 和可选参数，

|  |  |
| --- | --- |
| `X` | `N`×`Q` 矩阵 |
| `ymean` | `Y` 每一行的均值（默认为 0） |
| `ystd` | `Y` 每一行的标准差（默认为 1） |

并返回

|  |  |
| --- | --- |
| `Y` | `N`×`Q` 矩阵 |
| `PS` | 允许对值进行一致处理的处理设置 |

`[Y,PS] = mapstd(X,FP)` 将参数作为结构体接受：`FP.ymean`、`FP.ystd`。

`Y = mapstd('apply',X,PS)` 在给定 `X` 和设置 `PS` 的情况下返回 `Y`。

`X = mapstd('reverse',Y,PS)` 在给定 `Y` 和设置 `PS` 的情况下返回 `X`。

`dx_dy = mapstd('dx_dy',X,Y,PS)` 返回反向导数。
