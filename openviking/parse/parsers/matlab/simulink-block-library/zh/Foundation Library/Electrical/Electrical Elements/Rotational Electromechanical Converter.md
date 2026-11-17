---
type: simulink-block
title: 'Rotational Electromechanical Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'rotationalelectromechanicalconverter'
documentation_source_path: 'ref/rotationalelectromechanicalconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Electromechanical Converter

## 端口
```yaml
ports: []
```

该模块具有以下端口：

`+`
:   与转换器正极端子关联的电学守恒端口。

`-`
:   与转换器负极端子关联的电学守恒端口。

`C`
:   机械旋转守恒端口。

`R`
:   机械旋转守恒端口。
## 参数
```yaml
parameters: []
```

**Constant of proportionality K**
:   机电转换的比例常数。
    默认值为 `0.1` V/(rad/s)。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气域与机械旋转域之间的接口

Rotational Electromechanical Converter 模块提供电气域与机械旋转域之间的接口。它将电能转换为旋转运动形式的机械能，反之亦然。该转换器由以下方程描述：

T=K·I

V=K·ω

其中

|  |  |
| --- | --- |
| *`V`* | 转换器电学端口两端的电压 |
| *`I`* | 流过转换器电学端口的电流 |
| *`T`* | 转矩 |
| ω | 角速度 |
| *`K`* | 比例常数 |

Rotational Electromechanical Converter 模块表示无损耗的机电能量转换，因此两个方程中使用相同的比例常数。

连接 + 和 – 是对应于转换器正极和负极端子的守恒电学端口。连接 C 和 R 是守恒机械旋转端口。如果从正极端子流向负极端子的电流为正，则产生的转矩为正，作用方向从端口 C 到端口 R。可以通过使用负的 K 值来改变该方向。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
