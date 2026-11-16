---
type: simulink-block
title: 'Hydraulic Pressure Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sensors'
documentation_page: 'hydraulicpressuresensor'
documentation_source_path: 'ref/hydraulicpressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Pressure Sensor

## 端口

该模块具有以下端口：

`A`
:   与传感器正探头关联的液压守恒端口。

`B`
:   与传感器负（参考）探头关联的液压守恒端口。

`P`
:   输出压力值的物理信号端口。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a: 将移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的更多信息，请参阅“将 Hydraulic 模型升级为使用 Isothermal Liquid 模块”。

## 描述

(将移除) 理想压力传感装置

Hydraulic Pressure Sensor 模块表示理想液压压力传感器，即一种将两点之间测得的液压压差转换为与该压力成比例的控制信号的装置。该传感器是理想的，因为它不考虑惯性、摩擦力、延迟、压力损失等。

连接 A 和 B 是守恒液压端口，用于将传感器连接到液压管路。连接 P 是输出压力值的物理信号端口。传感器的正方向为从 A 到 B。这意味着压差确定为 p=pA−pB。
