---
type: simulink-block
title: 'Electromagnetic Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Elements'
documentation_page: 'electromagneticconverter'
documentation_source_path: 'ref/electromagneticconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Electromagnetic Converter

## 端口

该模块具有以下端口：

`N`
:   与模块 North 端子关联的磁守恒端口。

`S`
:   与模块 South 端子关联的磁守恒端口。

`+`
:   正电守恒端口。

`-`
:   负电守恒端口。

## 参数

**Number of winding turns**
:   电气绕组匝数。默认值为 `1`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

无损电磁能量转换装置

Electromagnetic Converter 模块提供电气域与磁域之间的通用接口。

该模块基于以下方程：

MMF=N⋅I

V=−N⋅dΦdt

其中

|  |  |
| --- | --- |
| *MMF* | 磁端口两端的磁动势（mmf） |
| *Φ* | 通过磁端口的磁通量 |
| *I* | 通过电端口的电流 |
| *V* | 电端口两端的电压 |
| *N* | 电气绕组匝数 |
| *t* | 仿真时间 |

连接 N 和 S 为磁守恒端口，连接 + 和 – 为电守恒端口。如果从电气 + 到 – 端口的电流为正，则产生的 mmf 在磁 N 到 S 端口两端为正。从 N 流向 S 的磁通正变化率会在 + 和 – 端口两端产生负感应电压。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
