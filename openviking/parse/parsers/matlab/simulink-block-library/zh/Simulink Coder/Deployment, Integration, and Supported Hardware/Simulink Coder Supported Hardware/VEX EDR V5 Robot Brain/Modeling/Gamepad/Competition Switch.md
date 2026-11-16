---
type: simulink-block
title: 'Competition Switch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Gamepad'
documentation_page: 'competitionswitch'
documentation_source_path: 'vexv5/ref/competitionswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Competition Switch

## 端口

### 输出

### **Auto** — 输出端口，根据开关位置 `1` 或 `0` 为 Autonomous 模式提供逻辑值

如果在 VEXnet Competetion Switch 中开关位置设置为 `Enabled` 和 `Autonomous`，则输出为 1。

当 Auto 输出端口为 1 且 Driver 输出端口为 0 时，机器人处于 Autonomous 模式。

**数据类型：** `Boolean`

### **Driver** — 输出端口，根据开关位置 `1` 或 `0` 为 Driver Controlled 模式提供逻辑值

如果在 VEXnet Competition Switch 中开关位置设置为 `Enabled` 和 `Driver`，则输出为 1。

当 Auto 输出端口为 0 且 Driver 输出端口为 1 时，机器人处于 Driver 模式。

**数据类型：** `Boolean`

### **Pre-Auto** — 输出端口，根据开关位置 `1` 或 `0` 为 Pre-autonomous 模式提供逻辑值

如果在 VEXnet Competition Switch 中开关位置设置为 `Disabled`，则输出为 1。

**数据类型：** `Boolean`

下表列出了基于开关位置的不同模式以及三个输出。

| Enable/Disable Switch | Autonomous/Driver Switch | 模式 | Pre-Auto | Auto | Driver |
| --- | --- | --- | --- | --- | --- |
| Disable | Autonomous | Pre-Autonomous | 1 | 0 | 0 |
| Enable | Autonomous | Autonomous | 0 | 1 | 0 |
| Enable | Driver | Driver Controlled | 0 | 0 | 1 |
| Disable | Driver | Disabled | 0 | 0 | 0 |

## 参数

### **Sample time** — 用于获取值的采样时间 `0.02`（默认）| seconds

指定 Competition Switch 模块应多久读取一次 VEXnet Competition Switch 中开关的位置。默认值为 0.02 秒。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Gamepad

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

读取 VEXnet Competition Switch 或场地控制器的开关位置

Competition Switch 模块用于读取 VEXnet Competition Switch 的开关位置，并提供相应的逻辑值（1 或 0）作为输出。基于开关位置，该模块可用于启用 Pre-Autonomous、Autonomous 和 Driver Controlled 模式所需的逻辑。
