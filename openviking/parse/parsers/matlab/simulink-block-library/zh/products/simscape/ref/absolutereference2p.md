---
type: simulink-block
title: 'Absolute Reference (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'absolutereference2p'
documentation_source_path: 'ref/absolutereference2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Absolute Reference (2P)

## 端口

在 R2025b 中未记录。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023a: 不再推荐 Absolute Reference (2P) 模块

Pressure & Temperature Sensor (2P) 模块现在包含一个隐式参考节点，这意味着你只需要一个端口即可进行压力或温度的绝对测量。仅当你需要测量模型中两个节点之间的压力或温度差时，才需要暴露第二个端口。

在之前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，你需要将端口 **B** 连接到 Absolute Reference (2P) 模块。现在不再需要这样做，因为你可以通过将 Pressure & Temperature Sensor (2P) 模块的 **Measurement reference** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。将 Absolute Reference (2P) 模块连接到 Pressure & Temperature Sensor (2P) 模块的现有模型将继续像以前一样工作。

## 描述

（不推荐）绝对压力为零且比内能为零处的参考点
