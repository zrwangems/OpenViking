---
type: simulink-block
title: 'Digital Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'digitalinput'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口

R2025b 中未提供文档。

## 参数

**数字端口**
:   选择一个数字引脚（或端口），其值介于 1 和 12 之间。

    不要将同一引脚编号分配给模型中的多个模块。

**添加用于仿真的输入端口**
:   选中此复选框以仿真 Digital Input 模块。

**采样时间**
:   指定此模块读取数字引脚值的时间间隔，以秒为单位。此参数值默认为 1/5 秒。如果选中**添加用于仿真的输入端口**复选框，则隐藏**采样时间**参数，并继承其值（Sample time = -1）。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2017a 中引入**

## 描述

读取输入引脚的数字值

读取所选数字端口（引脚）的数字值或逻辑值（1 或 0）。您可以使用 VEX® 微控制器上最多 12 个数字 IO 引脚。有关微控制器数字引脚布局的信息，请参阅 `VEX Cortex Pin-out`。

在没有硬件的仿真期间，如果没有 Source 模块连接到仿真输入端口，此模块将输出零。请参阅“模块在仿真中产生零或不执行任何操作”。要实现仿真行为，请连接 VEX Microcontroller 库中 Utilities 库里的 Source 模块。

在代码生成期间，连接到 Digital Input 模块输入端口的任何仿真模块都会被忽略，并且不会影响生成的代码。

此模块生成的代码可能无法正常工作。如果 VEX 微控制器通过橙色 USB A to A 电缆连接到 PC，且未连接可用的 VEX 7.2V 电池，则 VEX 电池为传感器供电。
