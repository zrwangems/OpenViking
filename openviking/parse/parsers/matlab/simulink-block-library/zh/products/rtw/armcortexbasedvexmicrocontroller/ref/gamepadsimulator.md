---
type: simulink-block
title: 'Gamepad Simulator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'gamepadsimulator'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadsimulator.html'
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
:   输入从 1 开始的操纵杆 ID。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2018b 中推出**

## 描述

使用 Logitech F310 或 XBOX Controller 获取 VEX 游戏手柄的仿真值

获取 VEX® 游戏手柄的仿真值。此模块仅适用于仿真。返回值中，前四个输出端口为范围在 –127 到 127 之间的模拟值，其余 12 个输出端口为逻辑值。前四个端口对应操纵杆上的四个控制轴。其余 12 个端口对应 VEX 游戏手柄上的 12 个按钮。与 Gamepad Simulator 端口 (1–8) 对应的 Logitech® Gamepad F310 按钮如图所示。

在对包含此模块的模型进行仿真之前，必须将 Gamepad F310 或 XBOX 游戏手柄连接到计算机。在仿真期间，使用连接的游戏手柄为 Simulink® 模型提供仿真输入。

**注意**

要确保此模块正常工作，Gamepad F310 设备背面的输入模式开关必须处于位置 D。有关 Gamepad F310 上输入模式开关的更多信息，请参阅 https://support.logi.com/hc/en-us。

在代码生成期间，Gamepad Simulator 模块会被忽略，对生成的代码没有任何影响。
