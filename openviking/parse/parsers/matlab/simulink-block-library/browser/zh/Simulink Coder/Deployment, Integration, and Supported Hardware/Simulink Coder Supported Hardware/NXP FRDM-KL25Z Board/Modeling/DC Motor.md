---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'dcmotor'
documentation_source_path: 'freedomboard/ref/dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Motor

## 端口

在 R2025b 中未提供文档。

## 参数

**DC motor**
:   选择 DC Motor A 或 DC Motor B。

    选择 DC Motor B 时，请确保不要在同一模型中使用 RGB LED 模块。

    DC Motor B 使用的 PTC2 引脚和 RGB LED 模块中蓝色 LED 使用的 LED\_BLUE (PTD1) 引脚都属于 Timer 0 Channel 1。在 Simulink® 模型中，使用属于同一定时器通道组合的引脚会导致引脚冲突错误。因此，当您使用 DC Motor B 和 RGB LED 模块构建模型时，会收到引脚冲突错误消息。结果是，您甚至也无法使用 RGB LED 模块中的 LED\_RED 引脚和 LED\_GREEN 引脚。作为 RGB LED 模块的替代方案，您可以使用两个 PWM Output 模块，并将其输出引脚分别设置为 LED\_RED 和 LED\_GREEN。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2014b 中引入**

## 描述

驱动直流电机沿任一方向旋转

NXP TFC 扩展板最多可连接两个直流电机。DC Motor 模块以介于完全反向 (-1.0) 和完全正向 (1.0) 之间的转矩驱动直流电机。由此产生的速度和转矩取决于连接到 TFC 扩展板的电池的当前状态。

在没有硬件的情况下进行仿真时，此模块不执行任何操作。
