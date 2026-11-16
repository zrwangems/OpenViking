---
type: simulink-block
title: 'Potentiometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'potentiometer'
documentation_source_path: 'freedomboard/ref/potentiometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Potentiometer

## 端口

在 R2025b 中未提供文档。

## 参数

**电位器**
:   选择电位器 A 或 B。

**采样时间**
:   指定此模块读取电位器值的时间间隔，单位为 seconds。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**于 R2014b 中引入**

## 描述

读取电位器的状态

NXP TFC 扩展板配有两个板载电位器（POTA 和 POTB）。

模块根据电位器的当前角位置输出 -1.0 到 1.0 之间的值。这些值分别对应电位器完全逆时针旋转或完全顺时针旋转时的状态。

在没有硬件的仿真过程中，此模块输出零值。
