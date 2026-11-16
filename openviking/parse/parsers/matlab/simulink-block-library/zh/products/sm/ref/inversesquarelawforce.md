---
type: simulink-block
title: 'Inverse Square Law Force'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Loads'
documentation_page: 'inversesquarelawforce'
documentation_source_path: 'ref/inversesquarelawforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Square Law Force

## 端口

该模块包含坐标系端口 B 和 F，分别表示基础坐标系和从动坐标系。

在模块对话框中选中 **Sense Force** 后，会显示一个额外的物理信号端口 **fm**。

## 参数

**Force Constant**
:   指定平方反比力的比例常数。该常数是一个集总参数，用于表征力的大小对两个坐标系原点之间距离的平方倒数的依赖关系。默认值为 `1`。选择或指定物理单位。

**Sense Force**
:   选中此复选框可感测作用在两个坐标系原点之间的平方反比力的带符号量值。该模块会显示一个额外的物理信号端口，用于输出力信号。输出信号为标量值。如果该力为斥力，则此值为正；如果该力为引力，则此值为负。

## 所属库

R2025b 中未提供相关文档。

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中推出**

## 描述

大小与两个坐标系原点之间距离的平方成反比的力

该模块表示一对力，其大小与基础坐标系原点和从动坐标系原点之间距离的平方成反比。该力对中的两个力大小相等、方向相反。其中一个力作用于基础坐标系原点，方向沿从从动坐标系原点指向基础坐标系原点的矢量。另一个力作用于从动坐标系原点，方向沿从基础坐标系原点指向从动坐标系原点的矢量。

力的大小取决于您指定的力常数。正的力常数表示斥力，该力将两个坐标系原点推开。负的力常数表示引力，该力将两个坐标系原点拉近。
