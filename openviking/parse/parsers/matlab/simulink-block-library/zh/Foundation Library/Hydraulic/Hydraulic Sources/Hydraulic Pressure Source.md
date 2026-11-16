---
type: simulink-block
title: 'Hydraulic Pressure Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicpressuresource'
documentation_source_path: 'ref/hydraulicpressuresource.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Pressure Source

## 端口

模块具有以下端口：

`T`
:   与源入口关联的液压守恒端口。

`P`
:   与源出口关联的液压守恒端口。

`S`
:   控制信号端口。

## 参数

未在 R2025b 中记录。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a：将删除

Hydraulic library 将在未来版本中删除。请改用 Isothermal Liquid library。Isothermal Liquid library 中的模块提供更高的准确性、可用性和数值性能。

有关更新模型的更多信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将删除）以压力为特性的理想液压能源

Hydraulic Pressure Source 模块表示一种理想液压能源，其足够强大，无论系统消耗的流量如何，都能在其出口处保持指定压力。模块连接 T 和 P 分别对应液压入口和出口端口，连接 S 表示控制信号端口。源两端的压差

p=pP−pT

其中 *p*P、
*p*T 是源端口处的表压，其与控制端口 S 处的信号成正比。可以使用各种 Simulink® 信号源来生成所需的压力变化曲线。

模块正方向为从端口 P 到端口 T。这意味着如果流量从 P 流向 T，则流量为正。如果源向端口 P 输送能量，则源产生的功率为负。
