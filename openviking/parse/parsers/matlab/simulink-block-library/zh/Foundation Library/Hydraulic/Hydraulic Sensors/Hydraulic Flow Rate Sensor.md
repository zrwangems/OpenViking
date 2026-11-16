---
type: simulink-block
title: 'Hydraulic Flow Rate Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sensors'
documentation_page: 'hydraulicflowratesensor'
documentation_source_path: 'ref/hydraulicflowratesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Flow Rate Sensor

## 端口

该模块具有以下端口：

`A`
:   与传感器正探头关联的液压守恒端口。

`B`
:   与传感器负（参考）探头关联的液压守恒端口。

`Q`
:   输出体积流量值的物理信号端口。

`M`
:   输出质量流量值的物理信号端口。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a: 将删除

Hydraulic 库将在未来版本中删除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅升级 Hydraulic 模型以使用 Isothermal Liquid 模块。

## 描述

（将删除）理想流量计

Hydraulic Flow Rate Sensor 模块表示理想流量计，即一种将通过液压管路的体积流量转换为与该流量成比例的控制信号的设备。连接 Q 是物理信号端口，输出体积流量值。连接 M 是物理信号端口，输出质量流量值。该传感器是理想的，因为它不考虑惯性、摩擦、延迟、压力损失等。

连接 A 和 B 是将传感器连接到液压管路的守恒液压端口。传感器的正方向是从 A 到 B。这意味着如果流量从 A 流向 B，则流量为正。
