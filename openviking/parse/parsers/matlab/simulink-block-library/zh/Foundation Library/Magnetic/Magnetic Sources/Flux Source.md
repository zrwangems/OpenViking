---
type: simulink-block
title: 'Flux Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sources'
documentation_page: 'fluxsource'
documentation_source_path: 'ref/fluxsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Flux Source

## 端口

该模块有两个与其端子关联的磁守恒端口。

## 参数

**Constant flux**
:   输出磁通。您可以指定任意实数值。默认值为 `0.001` Wb。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

理想磁通源

Flux Source 模块表示一个理想磁通源，其强度足以维持通过它的指定恒定磁通，无论其端子间的磁动势如何。

您通过 **Constant flux** 参数指定输出磁通，该参数可以为正、负或零。

磁通流动的正方向由箭头指示。
