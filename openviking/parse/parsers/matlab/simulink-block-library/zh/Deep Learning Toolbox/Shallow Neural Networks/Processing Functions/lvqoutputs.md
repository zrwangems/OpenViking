---
type: simulink-block
title: 'lvqoutputs'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'lvqoutputs'
documentation_source_path: 'ref/lvqoutputs.html'
language: zh-CN
chinese_source: worker-translation
---

# lvqoutputs

## 端口

R2025b 中未记录。

## 参数

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

LVQ 输出处理函数

`[X,settings] = lvqoutputs(X)` 原样返回其参数，但会将目标类别的比例存储在 settings 中，供 `initlvq` 用于初始化权重。

`X = lvqoutputs('apply',X,PS)` 返回 `X`。

`X = lvqoutputs('reverse',X,PS)` 返回 `X`。

`dx_dy = lvqoutputs('dx_dy',X,X,PS)` 返回单位导数。
