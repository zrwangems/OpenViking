---
type: simulink-block
title: 'Flux Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sensors'
documentation_page: 'fluxsensor'
documentation_source_path: 'ref/fluxsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Flux Sensor

## 端口

该模块具有以下端口：

`N`
:   与传感器 North 端子关联的磁守恒端口。

`S`
:   与传感器 South 端子关联的磁守恒端口。

该模块还具有一个物理信号输出端口，用于输出磁通值。

## 参数

在 R2025b 中未提供文档。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

理想磁通传感器

Flux Sensor 模块表示理想磁通传感器，即一种将任意磁支路中测得的磁通转换为与该磁通成正比的物理信号的设备。

连接 N 和 S 是磁守恒端口，传感器通过这些端口接入电路。物理信号端口输出磁通值，当磁通从 N 端口流向 S 端口时，该值为正。
