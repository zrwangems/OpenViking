---
type: simulink-block
title: 'Internal Force'
family: 'forces-and-torques'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'internalforce'
documentation_source_path: 'ref/internalforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Internal Force

## 端口

该模块包含坐标系端口 **B** 和 **F**，分别表示基座端口坐标系和从动端口坐标系。物理信号端口 **fm** 用于指定作用于两个端口坐标系之间的内力。

## 参数

在 R2025b 中未提供文档。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

在两个坐标系原点之间相互作用的一般力

该模块表示一对在基座坐标系原点和从动坐标系原点之间相互作用的一般力。力对中的两个力大小相等、方向相反。一个力作用于基座坐标系原点，方向沿从动坐标系原点到基座坐标系原点的连接矢量。另一个力作用于从动坐标系原点，方向沿基座坐标系原点到从动坐标系原点的连接矢量。

为指定内力，该模块提供了物理信号端口 **fm**。正输入信号表示斥力，会将基座坐标系原点和从动坐标系原点相互推开。负输入信号表示引力，会将基座坐标系原点和从动坐标系原点相互拉近。如果在任意时刻两个坐标系原点重合，内力方向将变为未定义，Simscape™ Multibody™ 可能会因错误而停止。
