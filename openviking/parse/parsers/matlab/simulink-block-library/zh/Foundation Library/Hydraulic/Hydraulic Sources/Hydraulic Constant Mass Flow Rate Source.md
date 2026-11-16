---
type: simulink-block
title: 'Hydraulic Constant Mass Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicconstantmassflowratesource'
documentation_source_path: 'ref/hydraulicconstantmassflowratesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Constant Mass Flow Rate Source

## 端口

该模块具有以下端口：

`T`
:   与源入口关联的液压守恒端口。

`P`
:   与源出口关联的液压守恒端口。

## 参数

**质量流量**
:   指定通过源的质量流量。默认值为
    `0.001` kg/s。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a：将移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、易用性和数值性能。

有关更新模型的详细信息，请参阅将 Hydraulic 模型升级为使用 Isothermal Liquid 模块。

## 描述

（将移除）液压网络中理想的机械能源，以恒定质量流量为特征

Hydraulic Constant Mass Flow Rate Source 模块表示液压网络中的理想机械能源，无论源两端的压差如何，都能保持恒定质量流量。该源不会因摩擦产生任何损失。**质量流量**参数指定通过源的质量流量。

模块连接 T 和 P 分别对应液压入口和出口端口。正质量流量使液体从端口 T 流向端口 P。
