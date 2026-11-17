---
type: simulink-block
title: 'Gravitational Field'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'gravitationalfield'
documentation_source_path: 'ref/gravitationalfield.html'
language: zh-CN
chinese_source: worker-translation
---

# Gravitational Field

## 端口

Frame port B 表示一个坐标系，其原点位于产生引力场的质点处。

## 参数

**Mass**
:   产生引力场的总质量。由此产生的引力与该质量成正比。该质量不会为模型增加惯性。质量参数的默认值为 `1.0` kg。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

质点引起的力场

该模块表示一个质点的引力场。
该场在每个刚体的质心处施加引力。力的大小随距场原点的距离平方衰减，场原点与 base port frame 原点重合。
刚体所受的力由牛顿万有引力定律得出：

Fg=− GMmRBF2，

其中：

- *F*g 是引力场施加在给定刚体上的力。
- *G* 是万有引力常数，6.67384 × 10-11 m3kg-1s-2。
- *M* 是产生引力场的总质量。
- *m* 是引力作用其上的刚体总质量。
- *R*BF 是源质量位置与刚体质心之间的距离。

图中显示了这些变量。该图展示了引力与距离之间的平方反比关系。

源质量可以为正或为负。组合多个该模块的实例，以对正质量和负质量扰动施加在更强引力场上的引力效应进行建模，例如由于低密度材料沿行星表面某一部分聚集而导致行星引力减小。

该模块不考虑其他刚体对场源质量施加的引力。若要包含这些力，可以将 Gravitational Field 模块连接到模型中的其他刚体。或者，可以使用 Inverse Square Law Force 模块对单对刚体之间的引力进行建模。

该引力场是时不变的。若要指定随时间变化且空间均匀的场，请使用 Mechanism Configuration 模块。
