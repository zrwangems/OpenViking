---
type: simulink-block
title: 'Electromagnetic Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Elements'
documentation_page: 'electromagneticconverter'
documentation_source_path: 'ref/electromagneticconverter.html'
language: zh-CN
chinese_source: official
---

# Electromagnetic Converter

## 端口

模块具有以下端口：

`N`
:   与模块北端关联的磁守恒端口。

`S`
:   与模块南端关联的磁守恒端口。

`+`
:   正电气守恒端口。

`-`
:   负电气守恒端口。

## 参数

**绕组匝数**
:   电气绕组匝数。默认值为 `1`。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2010a 中推出**

## 描述

无损电磁能量转换设备

Electromagnetic Converter 模块提供电气域和磁域之间的通用接口。

该模块基于以下方程：

MMF=N⋅I

V=−N⋅dΦdt

其中

|  |  |
| --- | --- |
| *MMF* | 磁端口两端的磁动势 (mmf) |
| *Φ* | 通过磁端口的磁通 |
| *I* | 通过电气端口的电流 |
| *V* | 电气端口两端的电压 |
| *N* | 电气绕组匝数 |
| *t* | 仿真时间 |

连接端 N 和 S 是磁守恒端口，连接端 + 和 – 是电气守恒端口。如果电流从电气端口 + 到电气端口 - 的方向为正，则产生的 mmf 从磁端口 N 到磁端口 S 的方向也为正。从 N 流向 S 的磁通的正变化率会使 + 和 - 端口之间产生负感应电压。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
