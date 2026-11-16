---
type: simulink-block
title: 'Gamepad Simulator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Utilities'
documentation_page: 'gamepadsimulator'
documentation_source_path: 'vexv5/ref/gamepadsimulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamepad Simulator

## 端口

R2025b 中未提供文档。

## 参数

**选择游戏手柄的类型**
:   选择连接到计算机的游戏手柄类型。

**输入操纵杆 ID**
:   输入从 1 开始编号的操纵杆 ID。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2018b 中引入**

## 描述

使用 Logitech F310 或 XBOX Controller 获取 VEX 游戏手柄的仿真值

获取 VEX® 游戏手柄的仿真值。此模块仅适用于仿真。前四个输出端口返回的值为 –127 到 127 范围内的模拟值，其余 12 个输出端口返回的值为逻辑值。前四个端口对应于操纵杆上的四个控制轴。其余 12 个端口对应于 VEX 游戏手柄上的 12 个按钮。Logitech® Gamepad F310 上与 Gamepad Simulator 端口 (1–8) 对应的按钮如图所示。

在仿真包含此模块的模型之前，必须将 Gamepad F310 或 XBOX 游戏手柄连接到计算机。在仿真过程中，使用已连接的游戏手柄为 Simulink® 模型提供仿真输入。

**注意**

确保 Gamepad F310 设备背面的输入模式开关处于 D 位置，此模块才能正常工作。有关 Gamepad F310 上输入模式开关的更多信息，请参阅 https://support.logi.com/hc/en-us。

在代码生成过程中，Gamepad Simulator 模块会被忽略，并且不会对生成的代码产生任何影响。
