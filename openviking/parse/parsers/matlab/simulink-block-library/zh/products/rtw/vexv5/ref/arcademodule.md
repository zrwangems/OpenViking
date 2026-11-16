---
type: simulink-block
title: 'Arcade Module'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Utilities'
documentation_page: 'arcademodule'
documentation_source_path: 'vexv5/ref/arcademodule.html'
language: zh-CN
chinese_source: worker-translation
---

# Arcade Module

## 端口

在 R2025b 中未提供文档说明。

## 参数

在 R2025b 中未提供文档说明。

## 所属库

在 R2025b 中未提供文档说明。

## 模块特性

在 R2025b 中未提供文档说明。

## 扩展功能

在 R2025b 中未提供文档说明。

## 版本历史

**在 R2018b 中推出**

## 描述

获取采用 Arcade 配置的机器人的右轮和左轮速度值

获取 Arcade 机器人右轮和左轮的速度值。Arcade 风格的机器人控制使用单个操纵杆上的两个轴来控制前进和后退运动以及左右差速。第一个输入端口映射到操纵杆的垂直轴。第二个输入端口映射到同一操纵杆的水平轴。第一个输出为右电机速度，第二个输出为左电机速度。

Arcade Module 模块使用以下公式确定电机速度：

- *RightMotorSpeed* = min(max((*y*−*x*),−127), 127)
- *LeftMotorSpeed* = min(max((*x*+*y*),−127), 127)

其中，*x* 和 *y* 表示操纵杆的位置。

例如，当操纵杆完全向前推动时，*y* = 127 且 *x* = 0。此时 `RightMotorSpeed` 的值为 127，`LeftMotorSpeed` 的值也为 127，从而使机器人向前移动。

**注意**

Arcade Module 模块与 Field Simulator 模块不兼容。避免在模型中同时使用 Field Simulator 模块和 Arcade Module 模块。
