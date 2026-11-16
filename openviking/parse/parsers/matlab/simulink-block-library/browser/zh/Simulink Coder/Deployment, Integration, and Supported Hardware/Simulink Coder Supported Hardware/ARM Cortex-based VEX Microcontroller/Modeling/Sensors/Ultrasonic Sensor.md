---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/ultrasonicsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ultrasonic Sensor

## 端口

R2025b 中未提供文档。

## 参数

**INPUT (Ping 端口)**
:   选择超声波传感器上‘INPUT’连接器所连接的数字端口。要了解 INPUT 端口，请点击模块参数对话框中的 **什么是 INPUT 和 OUTPUT？** 按钮。

**OUTPUT (Echo 端口)**
:   选择超声波传感器上‘OUTPUT’连接器所连接的数字端口。要了解 OUTPUT 端口，请点击模块参数对话框中的 **什么是 INPUT 和 OUTPUT？** 按钮。可以为 OUTPUT 选择除端口号 10 以外的任意端口号。

**添加用于仿真的输入端口**
:   如果希望在普通模式仿真中由源模块提供输入值，请选中此复选框。

**采样时间**
:   指定此模块读取距离的时间间隔，单位为 seconds。如果选中 **添加用于仿真的输入端口** 复选框，则会隐藏 **采样时间** 参数，并继承其值 (Sample time = -1)。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2017a 中引入**

## 描述

测量到物体的距离：0.02 至 2.0 meters (m)

利用高频声波测量机器人行进路径上物体的距离。当物体位于距传感器 0.02 至 2.0 meters 的范围内时，该模块可检测到该物体。对于距离超过 2 meters 的物体，该模块输出值 0。

在未连接硬件的情况下进行仿真时，如果没有 Source 模块连接到仿真输入端口，此模块将输出零。请参阅“模块在仿真中输出零或不执行任何操作”。要实现仿真行为，请从 VEX Microcontroller 库中的 Utilities 库连接一个 Source 模块。在代码生成期间，连接到 Ultrasonic Sensor 模块输入端口的任何仿真模块都会被忽略，并且不会对生成的代码产生任何影响。
