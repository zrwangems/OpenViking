---
type: simulink-block
title: 'Real Time'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'realtime'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/realtime.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Time

## 端口

在 R2025b 中未提供文档说明。

## 参数

**时间缩放因子**
:   输入时间缩放因子，以减慢仿真速度，使其接近实时。

    例如，当输入的时间缩放因子为 1 时，仿真中的 1 秒需要 1 秒实际时间来运行。仿真时间与实际时间相同。

    当输入的时间缩放因子为 5 时，仿真中的 1 秒需要 5 秒实际时间来运行。仿真运行速度为实时的五分之一。

## 所属库

在 R2025b 中未提供文档说明。

## 模块特性

在 R2025b 中未提供文档说明。

## 扩展功能

在 R2025b 中未提供文档说明。

## 版本历史

**在 R2018b 中引入**

## 描述

使仿真速度减慢至接近实时

在模型中放置此模块，以减慢仿真速度，使其接近实际时间。要指定实际时间与仿真时间之间的比率，请使用模块中的时间缩放因子参数。

**注意**

Real Time 模块将在 Simulink® Coder™ Support Package for ARM® Cortex®-based VEX® Microcontroller 的下一版本中弃用。您可以改用 Simulink 编辑器中的 Simulation Pacing 选项。
