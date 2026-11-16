---
type: simulink-block
title: 'Flux Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Sources'
documentation_page: 'fluxsource'
documentation_source_path: 'ref/fluxsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Flux Source

## 端口

该模块具有两个与其端子相关联的磁守恒端口。

## 参数

**Constant flux**
:   输出磁通。可以指定任意实数值。默认值为 `0.001` Wb。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

理想磁通源

Flux Source 模块表示一个理想磁通源，无论其两端的磁动势 (mmf) 如何，该磁通源都能维持通过它的指定恒定磁通。

使用 **Constant flux** 参数指定输出磁通，该参数值可以为正、负或零。

箭头指示磁通流动的正方向。
