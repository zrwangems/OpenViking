---
type: simulink-block
title: 'Absolute Reference (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'absolutereference2p'
documentation_source_path: 'ref/absolutereference2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Absolute Reference (2P)

## 端口

该模块具有一个两相流体守恒端口。该端口标识设置为零压力和比内能的两相流体节点。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023a: 不再推荐使用 Absolute Reference (2P) 模块

Pressure & Temperature Sensor (2P) 模块现在包含一个隐式参考节点，这意味着您只需要一个端口即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才需要暴露第二个端口。

在以前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，您需要将端口 **B** 连接到 Absolute Reference (2P) 模块。这不再必要，因为您现在可以通过将 Pressure & Temperature Sensor (2P) 模块的 **Measurement reference** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。现有模型中如果已将 Absolute Reference (2P) 模块连接到 Pressure & Temperature Sensor (2P) 模块，则继续像以前一样工作。

## 描述

（不推荐）零绝对压力和比内能处的参考点

Absolute Reference (2P) 模块表示零绝对压力和比内能处的参考点。与 Pressure & Internal Energy Sensor (2P) 模块配合使用，以测量两相流体节点处的绝对压力和比内能。
