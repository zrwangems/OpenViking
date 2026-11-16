---
type: simulink-block
title: 'Analog Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'analogoutput'
documentation_source_path: 'freedomboard/ref/analogoutput.html'
language: zh-CN
chinese_source: official
---

# Analog Output

## 端口

R2025b 官方文档未提供。

## 参数

R2025b 官方文档未提供。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2014b 中推出**

## 描述

向 PTE30 引脚发送模拟输出信号

向 FRDM-KL25Z 板上的引脚 PTE30 发送模拟输出信号。当您提供介于 0.0-1.0 之间的值时，此模块向引脚 PTE30 发出模拟信号，使得：

Vout = 3.3\*(1 + input\*4095)/4096

确保在同一模型内仅使用一个 Analog Output 模块。

在没有硬件的仿真期间，此模块不执行任何操作。
