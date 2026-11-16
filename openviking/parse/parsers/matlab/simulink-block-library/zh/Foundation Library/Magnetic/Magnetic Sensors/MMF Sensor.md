---
type: simulink-block
title: 'MMF Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sensors'
documentation_page: 'mmfsensor'
documentation_source_path: 'ref/mmfsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# MMF Sensor

## 端口

该模块具有以下端口：

`N`
:   与传感器 North 端子相关联的磁守恒端口。

`S`
:   与传感器 South 端子相关联的磁守恒端口。

该模块还具有一个物理信号输出端口，用于输出 mmf 的值。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

理想磁动势传感器

MMF Sensor 模块表示理想磁动势 (mmf) 传感器，即一种将任意磁连接之间测得的磁动势转换为与该磁动势成正比的物理信号的设备。

连接 N 和 S 是磁守恒端口，传感器通过这些端口连接到电路。物理信号端口输出磁动势的值。
