---
type: simulink-block
title: 'Hydraulic Constant Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicconstantflowratesource'
documentation_source_path: 'ref/hydraulicconstantflowratesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Constant Flow Rate Source

## 端口

该模块具有以下端口：

`T`
:   与源入口关联的液压守恒端口。

`P`
:   与源出口关联的液压守恒端口。

## 参数

**Source flow rate**
:   指定通过源的流量。默认值为
    `0.001` m^3/s。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2023a: 将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供更高的精度、可用性和
数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）理想液压能源，以恒定流量为特征

Hydraulic Constant Flow Rate Source 模块表示一个理想的
液压能源，其功率足以在源两端存在压差的情况下
仍在其出口处维持指定流量。**Source flow rate** 参数指定通过
源的流量。

模块连接 T 和 P 分别对应液压入口端口和出口端口。
模块正方向为从端口 T 到端口 P。
