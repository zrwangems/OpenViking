---
type: simulink-block
title: 'Inverse Square Law Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'inversesquarelawforce'
documentation_source_path: 'ref/inversesquarelawforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Square Law Force

## 端口

该模块包含坐标系端口 B 和 F，分别表示基础坐标系和从动坐标系。

在模块对话框中选中 **Sense Force** 会暴露一个额外的物理信号端口 **fm**。

## 参数

**Force Constant**
:   指定平方反比定律力的比例常数。该常数是一个集总参数，用于编码力的大小对两个坐标系原点之间距离平方反比的依赖关系。默认值为 `1`。选择或指定一个物理单位。

**Sense Force**
:   选中该复选框以检测作用在两个坐标系原点之间的平方反比定律力的带符号大小。该模块会暴露一个额外的物理信号端口以输出力信号。输出信号为标量值。如果力为排斥力，则该值为正；如果力为吸引力，则该值为负。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

力与两个坐标系原点之间距离的平方成反比

该模块表示一对力，其大小与基础坐标系和从动坐标系原点之间距离的平方成反比。该力对中的两个力大小相等但方向相反。一个力作用在基础坐标系原点上，沿从从动坐标系原点指向基础坐标系原点的向量方向。另一个力作用在从动坐标系原点上，沿从基础坐标系原点指向从动坐标系原点的向量方向。

力的大小取决于您指定的力常数。正的力常数表示排斥力，将两个坐标系原点推开。负的力常数表示吸引力，将两个坐标系原点拉近。
