---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'analoginput'
documentation_source_path: 'freedomboard/ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

R2025b 中未提供文档。

## 参数

**Analog pin**
:   从 A0-A5 中选择用于测量电压的模拟引脚。请确保不要为模型中的多个模块选择相同的引脚编号。

**Sample time**
:   指定此模块读取引脚值的时间间隔，以 seconds 为单位。

**View pin map**
:   单击此按钮可打开开发板的快照，其中包含 GPIO 引脚的参考信息。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**引入于 R2014b**

## 描述

测量模拟输入引脚的电压

测量所选模拟输入引脚（A0-A5）的电压。模块输出一个范围在 0.0 到 1.0 之间、分辨率为 16 bit 的值。最大电压由输入参考电压 VREFH 决定，VREFH 默认使用 3.3 Volt 电源。

在没有硬件的仿真过程中，此模块输出零。
