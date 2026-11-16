---
type: simulink-block
title: 'MMF Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Sources'
documentation_page: 'mmfsource'
documentation_source_path: 'ref/mmfsource.html'
language: zh-CN
chinese_source: worker-translation
---

# MMF Source

## 端口

该模块具有两个与其端子关联的磁守恒端口。

## 参数

**Constant mmf**
:   输出磁动势。可以指定任意实数值。默认值为 `1` A。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

理想磁动势源

MMF Source 模块表示理想磁动势 (mmf) 源，无论流经该源的磁通如何，它都能在其输出端子之间维持指定的恒定磁动势。

使用 **Constant mmf** 参数指定输出磁动势，该参数可以为正值、负值或零。
