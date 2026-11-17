---
type: simulink-block
title: 'Reluctance'
family: 'magnetic'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Elements'
documentation_page: 'reluctance'
documentation_source_path: 'ref/reluctance.html'
language: zh-CN
chinese_source: worker-translation
---

# Reluctance

## 端口

该模块具有以下端口：

`N`
:   与模块北端子相关联的磁守恒端口。

`S`
:   与模块南端子相关联的磁守恒端口。

## 参数

**部分或间隙的厚度或长度**
:   所建模部分的厚度，或气隙长度。
    默认值为 `0.001` m。

**横截面积**
:   所建模部分的横截面积。默认值为 `0.01` m^2。

**材料的相对磁导率**
:   部分材料的相对磁导率。默认值为 `1`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中推出**

## 描述

磁阻

Reluctance 模块用于对磁阻（即阻碍磁通流动的组件）进行建模。组件两端的磁动势 (mmf) 与由此产生的流过组件的磁通量之比为常数，该比值定义为磁阻。磁阻取决于所建模部分的几何形状。

该模块基于以下方程：

MMF=Φ⋅ℜ

ℜ=gμ0⋅μr⋅A

其中

|  |  |
| --- | --- |
| *MMF* | 组件两端的磁动势 (mmf) |
| *Φ* | 通过组件的磁通量 |
| ℜ | 磁阻 |
| *g* | 所建模部分的厚度，或气隙长度 |
| *μ*0 | 磁导率常数 |
| *μ*r | 材料的相对磁导率 |
| *A* | 所建模部分的横截面积 |

连接 N 和 S 是磁守恒端口。磁阻两端的 mmf 由 MMF(N)−MMF(S) 给出，当磁通从 N 到 S 流经器件时，磁通符号为正。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标值**部分。有关详细信息，请参阅为模块变量设置优先级和初始目标值。

标称值提供了一种指定模型中变量预期大小的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关详细信息，请参阅修改模块变量的标称值。
