---
type: simulink-block
title: 'Servo Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'servowrite'
documentation_source_path: 'freedomboard/ref/servowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Servo Write

## 端口

在 R2025b 中未提供文档。

## 参数

**Servo**
:   选择 Servo 0 或 Servo 1 电机。

**最小角度 (degrees)**
:   指定伺服电机可达到的最小角度。

**最大角度 (degrees)**
:   指定伺服电机可达到的最大角度。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2014b 中引入**

## 描述

驱动伺服电机转至指定角度

NXP TFC 扩展板最多可连接两个伺服电机。

Servo Write 模块使用周期为 20ms 的 PWM 信号驱动伺服电机。该模块控制伺服电机在指定的最小角度和最大角度之间转动。
该模块会将任何超出指定范围的值限制在该范围内。

在没有硬件的情况下进行仿真时，此模块不执行任何操作。
