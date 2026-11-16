---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'analoginput'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

R2025b 中未提供文档。

## 参数

**模拟端口**
:   选择一个模拟通道（或端口），取值介于 1 和 8 之间。

    不要将同一通道编号分配给模型中的多个模块。

**添加用于仿真的输入端口**
:   选中此复选框可对模拟输入模块进行仿真。

**采样时间**
:   指定此模块读取引脚值的时间间隔，以 seconds 为单位。此参数的默认值为 1/5 second。如果选中**添加用于仿真的输入端口**复选框，则会隐藏**采样时间**参数，并继承其值 (Sample time = -1)。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2017a 中引入**

## 描述

读取连接到模拟输入引脚的传感器的值

读取所选模拟端口（引脚）的电压。使用模拟输入引脚测量传感器（如电位器）的输出（电压）。12-bit 传感器值的范围为 0 到 4095，对应 0V 到 5V 的输入电压。VEX® 微控制器上最多可使用 8 个模拟 IO 引脚。有关微控制器数字引脚布局的信息，请参阅 `VEX
Cortex Pin-out`。

在代码生成期间，连接到 Analog Input 模块输入端口的任何仿真模块都会被忽略，不会对生成的代码产生任何影响。

在没有硬件的情况下进行仿真时，如果没有 Source 模块连接到仿真输入端口，此模块将输出零。请参阅“模块在仿真中产生零或不执行任何操作”。要实现仿真行为，请从 VEX Microcontroller 库中的 Utilities 库连接一个 Source 模块。

要使此模块生成的代码能够在与 PC 建立系留连接的 VEX 微控制器上正常工作，请确保将 VEX 7.2V 电池连接到微控制器，并打开电池电源。
