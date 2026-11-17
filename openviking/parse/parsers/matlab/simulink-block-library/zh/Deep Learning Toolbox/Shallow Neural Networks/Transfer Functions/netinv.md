---
type: simulink-block
title: 'netinv'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'netinv'
documentation_source_path: 'ref/netinv.html'
language: zh-CN
chinese_source: worker-translation
---

# netinv

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

逆传递函数

`netinv` 是一个传递函数。传递函数根据网络的净输入计算某层的输出。

`A = netinv(N,FP)` 接受以下输入

|  |  |
| --- | --- |
| `N` | `S`×`Q` 的净输入（列）向量矩阵 |
| `FP` | 函数参数结构体（忽略） |

并返回 `1/N`。

`info = netinv('code')` 返回关于此函数的信息。支持以下代码：

`netinv('name')` 返回此函数的名称。

`netinv('output',FP)` 返回 [`min`
`max`] 输出范围。

`netinv('active',FP)` 返回 [`min`
`max`] 活动输入范围。

`netinv('fullderiv')` 返回 1 或 0，取决于
`dA_dN` 是
`S`×`S`×`Q` 还是
`S`×`Q`。

`netinv('fpnames')` 返回函数参数的名称。

`netinv('fpdefaults')` 返回默认函数参数。
