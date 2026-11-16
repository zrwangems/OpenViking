---
type: simulink-block
title: 'Gamepad Joystick'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Gamepad'
documentation_page: 'gamepadjoystick'
documentation_source_path: 'vexv5/ref/gamepadjoystick.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamepad Joystick

## 端口

### 输出

### **Port\_1** — 输出端口，其值为对应摇杆沿轴 `-128` 到 `127` 位置的模拟信号

模块输出根据摇杆沿指定控制轴的位置，范围为 -128 到 127。值为 0 表示摇杆未沿该轴移动。

在仿真期间，无硬件时，如果没有 Source 模块连接到仿真输入端口，此模块输出零（参见“模块在仿真中产生零或不执行任何操作”）。在代码生成期间，任何连接到 Gamepad Joystick 模块输入端的仿真模块都会被忽略，并且对生成的代码没有影响。

**数据类型：** `double`

## 参数

### **Gamepad Type** — 选择游戏手柄控制类型 `Primary`（默认）| `Partner`

你可以使用一对 VEX V5 Controller gamepad 来控制连接到 VEX EDR V5 Robot Brain 的外设。

### **Analog Channel (1 to 4)** — 选择 VEX V5 Controller gamepad 上 x-y 模拟摇杆的控制轴（1 到 4）。默认值为 1

根据 VEX 游戏手柄上摇杆的标签选择控制轴。右摇杆的水平轴标记为 **1**，垂直轴标记为 **2**。左摇杆的水平轴标记为 **3**，垂直轴标记为 **4**。根据你对此参数的选择，模块的封装图标会在 Simulink® Editor 中更新。

### **Sample time** — 从摇杆获取模拟值的采样时间 `0.02`（默认）| seconds

指定 Gamepad Joystick 模块读取游戏手柄摇杆值的频率。默认值为 0.02 seconds.

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Gamepad

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

表示 VEX V5 Controller gamepad 上 x-y 模拟摇杆的一个控制轴并读取值

Gamepad Joystick 模块用于表示 VEX® V5 Controller gamepad 上 x-y 模拟摇杆的一个控制轴，并根据摇杆沿该轴的位置读取对应的模拟值。VEX V5 Controller gamepad 上有两个模拟摇杆，每个摇杆有两个控制轴。
