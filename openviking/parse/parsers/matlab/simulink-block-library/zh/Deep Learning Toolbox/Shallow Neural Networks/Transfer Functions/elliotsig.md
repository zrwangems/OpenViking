---
type: simulink-block
title: 'elliotsig'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'elliotsig'
documentation_source_path: 'ref/elliotsig.html'
language: zh-CN
chinese_source: worker-translation
---

# elliotsig

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

**在 R2012b 中引入**

## 描述

Elliot 对称 sigmoid 传递函数

传递函数将神经网络层的净输入转换为净输出。

`A = elliotsig(N)` 接受一个 `S`×`Q` 的净输入（列）向量矩阵 `N`，并返回一个 `S`×`Q` 的输出向量矩阵 `A`，其中 `N` 的每个元素通过一个“S 形”函数从区间 `[-inf inf]` 压缩到区间 `[-1 1]`。

该传递函数相对于其他 sigmoid 函数的优势在于，它在简单的计算硬件上计算速度快，因为它不需要任何指数或三角函数。其劣势在于，它仅在大输入时才会趋于平坦，因此其作用不像其他 sigmoid 函数那样局部化。这可能导致更多的训练迭代，或需要更多神经元才能达到相同的精度。
