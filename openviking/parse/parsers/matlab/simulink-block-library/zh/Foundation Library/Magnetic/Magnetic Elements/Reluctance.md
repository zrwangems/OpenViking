---
type: simulink-block
title: 'Reluctance'
family: 'simscape'
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
:   与模块北端子关联的磁守恒端口。

`S`
:   与模块南端子关联的磁守恒端口。

## 参数

**Thickness or length of section or gap**
:   所建模区段的厚度，或气隙的长度。
    默认值为 `0.001` m。

**Cross-sectional area**
:   所建模区段的面积。默认值为 `0.01` m^2。

**Relative permeability of material**
:   区段材料的相对磁导率。默认值为 `1`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

磁阻

Reluctance 模块对磁阻进行建模，即抵抗磁通流动的组件。组件两端的磁动势（mmf）与流过组件的所得磁通之比是恒定的，该比值定义为磁阻。磁阻取决于所建模区段的几何形状。

该模块基于以下方程：

MMF=Φ⋅ℜ

ℜ=gμ0⋅μr⋅A

其中

|  |  |
| --- | --- |
| *MMF* | 组件两端的磁动势（mmf） |
| *Φ* | 通过组件的磁通 |
| ℜ | 磁阻 |
| *g* | 所建模区段的厚度，或气隙的长度 |
| *μ*0 | 磁导率常数 |
| *μ*r | 材料的相对磁导率 |
| *A* | 所建模区段的面积 |

连接 N 和 S 是磁守恒端口。磁阻两端的 mmf 由 MMF(N)−MMF(S) 给出，当磁通从 N 流向 S 通过器件时，磁通的符号为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
