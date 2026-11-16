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

坐标系端口 B 表示一个坐标系，其原点位于产生引力场的点质量处。

## 参数

**Mass**
:   产生引力场的总质量。由此产生的引力与该质量成正比。此质量
    不会向模型添加任何惯性。质量参数的默认值为 `1.0` kg。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

点质量产生的力场

此模块表示点质量的引力场。该场在每个刚体的质心处施加引力。
力的大小随其与场原点之间距离的平方而衰减，场原点与基础端口
坐标系的原点重合。刚体所受的力遵循牛顿万有引力定律：

Fg=− GMmRBF2,

其中：

- *F*g 是引力场对给定刚体施加的力。
- *G* 是万有引力常数，其值为 6.67384 × 10-11 m3kg-1s-2。
- *M* 是产生引力场的总质量。
- *m* 是引力所作用的刚体的总质量。
- *R*BF 是源质量位置与刚体质心之间的距离。

图中显示了这些变量。该图还显示了引力与距离之间的平方反比关系。

源质量可以为正，也可以为负。组合使用此模块的多个实例，可以对
正、负质量扰动在较强引力场中引起的引力效应进行建模，例如，对
因行星表面某一部分的低密度物质聚集而导致行星引力减小的情况
进行建模。

此模块不包括其他刚体对场源质量施加的引力。要包含这些力，可以
将 Gravitational Field 模块连接到模型中的其他刚体。或者，可以
使用 Inverse Square Law Force 模块对一对刚体之间的引力进行建模。

引力场不随时间变化。要指定随时间变化但在空间上均匀的场，请使用
Mechanism Configuration 模块。
