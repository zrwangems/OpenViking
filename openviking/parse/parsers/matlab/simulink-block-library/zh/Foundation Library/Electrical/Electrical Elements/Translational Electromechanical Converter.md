---
type: simulink-block
title: 'Translational Electromechanical Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'translationalelectromechanicalconverter'
documentation_source_path: 'ref/translationalelectromechanicalconverter.html'
language: zh-CN
chinese_source: official
---

# Translational Electromechanical Converter

## 端口

模块具有以下端口：

`+`
:   与转换器正极端子关联的电气守恒端口。

`-`
:   与转换器负极端子关联的电气守恒端口。

`C`
:   机械平移守恒端口。

`R`
:   机械平移守恒端口。

## 参数

**比例常数 K**
:   机电转换的比例常数。默认值为 `0.1` V/(m/s)。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

电气平移域和机械平移域之间的接口

Translational Electromechanical Converter 模块提供电气平移域和机械平移域之间的接口。它以平移运动形式将电能转换为机械能，反之亦然。转换器用以下方程描述：

F=K·I

V=K·U

其中

|  |  |
| --- | --- |
| *`V`* | 转换器的电气端口两端的电压 |
| *`I`* | 通过转换器的电气端口的电流 |
| *`F`* | 力 |
| *`U`* | 速度 |
| *`K`* | 比例常数 |

Translational Electromechanical Converter 模块表示无损机电能量转换，因此两个方程式都使用相同的比例常数。

连接端 + 和 - 是分别对应于转换器的正极端子和负极端子的守恒电气端口。连接端 C 和 R 是守恒机械平移端口。如果电流从正极端子到负极端子的方向为正，则产生的力从端口 C 到端口 R 的方向也为正。这一方向可通过对 K 使用负值来改变。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
