---
type: simulink-block
title: 'Battery Indicator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'batteryindicator'
documentation_source_path: 'freedomboard/ref/batteryindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Indicator

## 端口

在 R2025b 中未提供文档。

## 参数

在 R2025b 中未提供文档。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 TFC shield 上的 LED 显示电池电压水平

此模块控制 TFC Shield 上的四个 LED，以指示电池电压的当前水平。每个 LED 代表电池电压的 25%。当输入介于 0.75 和 1.0 之间时，四个 LED 全部点亮；当输入降低到介于 0.0 和 0.25 之间的值时，只有一个 LED 点亮。

在没有硬件的情况下进行仿真时，此模块不执行任何操作。
