---
type: simulink-block
title: 'Digital Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'digitalinput'
documentation_source_path: 'freedomboard/ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口

R2025b 中未提供文档。

## 参数

**引脚**
:   选择一个数字引脚。

    确保不要将同一引脚编号分配给模型中的多个模块。

**采样时间**
:   指定此模块读取数字引脚值的时间间隔，以秒为单位。此参数值默认为 1/10 秒。

**查看引脚映射**
:   单击此按钮可打开开发板的快照，其中包含 GPIO 引脚的参考信息。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**于 R2014b 中引入**

## 描述

读取数字输入引脚的逻辑值

读取所选数字输入引脚的逻辑值。FRDM-KL25Z 开发板上有 14 个引脚可用作数字信号的输入，即 D0-D13。此开发板的数字引脚布局与标准 Arduino Digital Pins 兼容。

在没有硬件的情况下进行仿真时，此模块输出零。
