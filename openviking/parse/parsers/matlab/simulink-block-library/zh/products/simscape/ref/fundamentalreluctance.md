---
type: simulink-block
title: 'Fundamental Reluctance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Elements'
documentation_page: 'fundamentalreluctance'
documentation_source_path: 'ref/fundamentalreluctance.html'
language: zh-CN
chinese_source: worker-translation
---

# Fundamental Reluctance

## 端口

该模块具有以下端口：

`N`
:   与模块北端子相关联的磁守恒端口。

`S`
:   与模块南端子相关联的磁守恒端口。

## 参数

**Reluctance**
:   元件两端的磁动势 (mmf) 与由此产生的流过元件的磁通之比。默认值为 `8e4` 1/H。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

磁阻的简化实现

Fundamental Reluctance 模块提供磁阻的简化模型，即阻碍磁通流动的元件。与根据所建模部分的几何形状计算磁阻的 Reluctance 模块不同，Fundamental Reluctance 模块允许您直接将磁阻值指定为模块参数。

该模块基于以下方程：

MMF=Φ⋅ℜ

其中：

|  |  |
| --- | --- |
| *MMF* | 元件两端的磁动势 (mmf) |
| *Φ* | 通过元件的磁通 |
| ℜ | 磁阻 |

N 和 S 连接端口是磁守恒端口。磁阻两端的磁动势 (mmf) 由 MMF(N)−MMF(S) 给出，当磁通从 N 到 S 流过器件时，磁通符号为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
