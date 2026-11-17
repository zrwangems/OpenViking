---
type: simulink-block
title: 'Variable Reluctance'
family: 'simscape'
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
:   与模块 North 端子关联的磁守恒端口。

`S`
:   与模块 South 端子关联的磁守恒端口。

该模块还具有一个物理信号输入端口，用于提供气隙长度或截面厚度的值。

## 参数

**Minimum length or thickness X>=0**
:   气隙长度或截面厚度的最小值。
    如果输入信号低于此水平（例如变为负值），
    则使用此最小值。该参数值必须为非负。
    默认值为 `0`。

**Cross-sectional area**
:   所建模截面的面积。默认值为 `0.01` m^2。

**Relative permeability of material**
:   截面材料的相对磁导率。默认值为 `1`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

电磁系统中的可变磁阻

Variable Reluctance 模块对可变磁阻进行建模，即对阻碍磁通流动的组件进行建模。组件两端的磁动势（mmf）与流过组件的所得磁通之比定义为磁阻，并且取决于输入物理信号的值。

该模块基于以下方程：

MMF=Φ⋅ℜ

ℜ=Xμ0⋅μr⋅A

其中

|  |  |
| --- | --- |
| *MMF* | 组件两端的磁动势（mmf） |
| *Φ* | 通过组件的磁通 |
| ℜ | 磁阻 |
| *X* | 物理信号端口处提供的值 |
| *μ*0 | 磁导率常数 |
| *μ*r | 材料的相对磁导率 |
| *A* | 所建模截面的面积 |

连接 N 和 S 是磁守恒端口。磁阻两端的 mmf 由 MMF(N)−MMF(S) 给出，当磁通从 N 流向 S 通过器件时，磁通的符号为正。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。
使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
