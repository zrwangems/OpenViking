---
type: simulink-block
title: 'Variable Reluctance'
family: 'magnetic'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Elements'
documentation_page: 'variablereluctance'
documentation_source_path: 'ref/variablereluctance.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Reluctance

## 端口

该模块具有以下端口：

`N`
:   与模块北极端子相关联的磁守恒端口。

`S`
:   与模块南极端子相关联的磁守恒端口。

该模块还具有一个物理信号输入端口，用于提供气隙长度或区段厚度的值。

## 参数

**最小长度或厚度 X>=0**
:   气隙长度或区段厚度的最小值。
    如果输入信号低于此值（例如变为负值），
    则使用此最小值。参数值必须为非负。
    默认值为 `0`。

**横截面积**
:   所建模区段的横截面积。默认值为 `0.01` m^2。

**材料相对磁导率**
:   区段材料的相对磁导率。默认值为 `1`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2010a 中推出**

## 描述

电磁系统中的可变磁阻

Variable Reluctance 模块对可变磁阻进行建模，即对阻碍磁通流动的元件进行建模。元件两端的磁动势 (mmf) 与由此产生的流经元件的磁通之比定义为磁阻，并且磁阻取决于输入物理信号的值。

该模块基于以下方程：

MMF=Φ⋅ℜ

ℜ=Xμ0⋅μr⋅A

其中

|  |  |
| --- | --- |
| *MMF* | 元件两端的磁动势 (mmf) |
| *Φ* | 通过元件的磁通 |
| ℜ | 磁阻 |
| *X* | 物理信号端口提供的值 |
| *μ*0 | 磁导率常数 |
| *μ*r | 材料的相对磁导率 |
| *A* | 所建模区段的横截面积 |

N 和 S 连接端口为磁守恒端口。磁阻两端的磁动势由 MMF(N)−MMF(S) 给出，当磁通从 N 到 S 流经该器件时，磁通符号为正。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期大小的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可来自不同来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关详细信息，请参阅修改模块变量的标称值。
