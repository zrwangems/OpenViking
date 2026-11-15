---
type: simulink-block
title: 'Servo Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'servomotor'
documentation_source_path: 'vexv5/ref/servomotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Servo Motor

## 端口

### 输入

### **Port\_1** — 用于设置伺服电机角位置的输入信号，整数范围为 [–128 127]

Servo Motor 模块的输入信号可以来自模型中的其他模块。例如：

- 如果将 Gamepad Joystick 模块连接为 Servo Motor 模块的输入，则输入值可以根据游戏手柄上操纵杆的位置在 –128 到 127 之间变化，然后转换为伺服电机的角位置值（以度为单位）。对于模块输入值 ‘0’，伺服电机保持静止。
- 如果将 Gamepad Button 模块连同 Gain 模块连接为 Servo Motor 模块的输入，则可以在按钮保持按下期间将输入设置为特定值，然后转换为伺服电机的角位置值（以度为单位）。

**数据类型：** `double`

## 参数

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 使用的 smart port `None`（默认）| `1` 到 `21`

如果使用 3-Wire Expander，请指定 VEX EDR V5 Robot Brain 上扩展器所连接的 smart port。

### **Port** — 选择连接到伺服电机的 3-wire 端口 A（默认）| `A` 到 `H`

选择 VEX EDR V5 Robot Brain 上连接到伺服电机的 3-wire 端口。

请勿在同一模型中将同一端口分配给多个 Servo Motor 模块。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

表示已连接的伺服电机并设置角位置值

Servo Motor 模块表示连接到 VEX® EDR V5 Robot Brain 上指定 3-wire 端口的伺服电机。该模块的输入信号设置伺服电机的角位置值。VEX EDR V5 Robot Brain 上有八个可用于连接伺服电机的 3-wire 端口。
