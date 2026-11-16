---
type: simulink-block
title: 'Hydraulic Mass Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicmassflowratesource'
documentation_source_path: 'ref/hydraulicmassflowratesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Mass Flow Rate Source

## 端口

该模块具有以下端口：

`T`
:   与源入口关联的液压守恒端口。

`P`
:   与源出口关联的液压守恒端口。

`M`
:   控制信号端口。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a: 将被删除

未来版本中将移除 Hydraulic 库。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅《升级 Hydraulic 模型以使用 Isothermal Liquid 模块》。

## 描述

（将被删除）液压网络中由质量流量表征的理想机械能源

Hydraulic Mass Flow Rate Source 模块表示液压网络中的一个理想机械能源，无论源两端的压差如何，都能保持指定的质量流量。该源不会产生任何因摩擦导致的损失。模块连接 T 和 P 分别对应液压入口端口和出口端口。通过该源的质量流量与控制端口 M 处的信号成正比。

正质量流量使液体从端口 T 流向端口 P。
