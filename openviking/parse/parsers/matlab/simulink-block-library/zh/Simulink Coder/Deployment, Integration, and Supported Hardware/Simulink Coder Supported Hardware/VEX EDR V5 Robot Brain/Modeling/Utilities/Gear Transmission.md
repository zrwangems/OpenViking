---
type: simulink-block
title: 'Gear Transmission'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Utilities'
documentation_page: 'geartransmission'
documentation_source_path: 'vexv5/ref/geartransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Gear Transmission

## 端口

未在 R2025b 中提供文档。

## 参数

未在 R2025b 中提供文档。

## 所属库

未在 R2025b 中提供文档。

## 模块特性

未在 R2025b 中提供文档。

## 扩展功能

未在 R2025b 中提供文档。

## 版本历史

**自 R2018b 起引入**

## 描述

根据输入值设置标量值（1 到 4）

根据输入端口的信号，将标量值设置在 1 到 4 的范围内。输入端口 Up 和 Down 接收来自数字按钮的逻辑值。当 Up 值为 HIGH (1) 时，Gear Transmission 模块的输出递增 1。如果 Down 值为 HIGH (1)，则 Gear Transmission 模块的输出递减 1。如果两个输入值均未发生变化，则档位值不变。即使输入值发生变化，档位值也不会低于 1 或高于 4。

例如，在模型中使用此模块，通过将档位输出值作为 Gamepad Joystick 信号的缩放因子，来控制机器人的电机速度。该值可以在摇杆的整个范围内上调或下调电机的速度值。
