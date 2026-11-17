---
type: simulink-block
title: 'satlins'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'satlins'
documentation_source_path: 'ref/satlins.html'
language: zh-CN
chinese_source: worker-translation
---

# satlins

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

对称饱和线性传递函数

`satlins` 是一种神经网络传递函数。传递函数根据其净输入计算某层的输出。

`A = satlins(N,FP)` 接受 `N` 和一个可选参数，

|  |  |
| --- | --- |
| `N` | 净输入（列）向量的 `S`×`Q` 矩阵 |
| `FP` | 函数参数的结构体（可选，忽略） |

并返回 `A`，即 `N` 的元素被裁剪到 `[-1, 1]` 后的 `S`×`Q` 矩阵。

`info = satlins('code')` 为每个支持的 *`code`* 字符向量返回有用的信息：

`satlins('name')` 返回此函数的名称。

`satlins('output',FP)` 返回 `[min max]` 输出范围。

`satlins('active',FP)` 返回 `[min max]` 有效输入范围。

`satlins('fullderiv')` 返回 1 或 0，取决于 `dA_dN` 是 `S`×`S`×`Q` 还是 `S`×`Q`。

`satlins('fpnames')` 返回函数参数的名称。

`satlins('fpdefaults')` 返回默认函数参数。
