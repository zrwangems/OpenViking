---
type: simulink-block
title: 'Gear Transmission'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'geartransmission'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/geartransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Gear Transmission

## 端口

R2025b 中未提供文档。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2018b 中引入**

## 描述

根据输入值设置标量值（1 到 4）

根据输入端口的信号，设置一个范围在 1 到 4 之间的标量值。输入端口 Up 和 Down 接收来自数字按钮的逻辑值。当 Up 值为 HIGH (1) 时，Gear Transmission 模块的输出递增 1。如果 Down 值为 HIGH (1)，则 Gear Transmission 模块的输出递减 1。如果两个输入值均未发生变化，则挡位值不变。即使输入值发生变化，挡位值也不会低于 1 或高于 4。

例如，在模型中使用此模块，通过将挡位输出值用作 Gamepad Joystick 信号的缩放因子，来控制机器人的电机速度。该值可以在操纵杆的整个范围内放大或缩小电机的速度值。
