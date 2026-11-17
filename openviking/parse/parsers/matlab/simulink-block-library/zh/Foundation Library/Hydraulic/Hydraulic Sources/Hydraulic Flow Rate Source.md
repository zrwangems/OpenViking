---
type: simulink-block
title: 'Hydraulic Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicflowratesource'
documentation_source_path: 'ref/hydraulicflowratesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Flow Rate Source

## 端口

该模块具有以下端口：

`T`
:   与源入口关联的液压守恒端口。

`P`
:   与源出口关联的液压守恒端口。

`S`
:   控制信号端口。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）理想的液压能源，以流量为特征

Hydraulic Flow Rate Source 模块表示一个理想的液压能源，其功率足以在源两端存在压差的情况下仍在其出口处维持指定的流量。模块连接 T 和 P 分别对应液压入口和出口端口，连接 S 表示控制信号端口。通过源的流量与控制端口 S 处的信号成正比。可以使用各种 Simulink® 信号源来生成所需的流量变化曲线。

该模块的正方向为从端口 T 到端口 P。这意味着如果流量从 T 流向 P，则流量为正。压差确定为 p=pP−pT，如果源出口处的压力大于其入口处的压力，则为负。如果源向端口 P 输送能量，则源产生的功率为负。
