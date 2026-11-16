---
type: simulink-block
title: 'Competition Switch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'competitionswitch'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/competitionswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Competition Switch

## 端口

### 输入

### **Auto** — 用于在仿真期间启用 Autonomous 模式的信号 `1` | `0`

将源模块连接到此端口，以仿真 VEX 竞赛中 Competition Switch 的位置。

#### 依赖关系

仅当选择 **为仿真添加输入端口** 参数时，此端口才会出现。

**数据类型：** `Boolean`

### **Driver** — 用于在仿真期间启用 Driver 模式的信号 `1` | `0`

将源模块连接到此端口，以仿真 VEX 竞赛中 Competition Switch 的位置。

#### 依赖关系

仅当选择 **为仿真添加输入端口** 参数时，此端口才会出现。

**数据类型：** `Boolean`
### 输出

### **Auto** — 基于开关输出 Autonomous 模式的逻辑值 `1` | `0`

如果 VEXnet Competition Switch 上的开关位置为 Autonomous，则输出为 `1`。

当 **Auto** 输出端口为 1 且 **Driver** 输出端口为 0 时，机器人处于 Autonomous 模式。

**数据类型：** `Boolean`

### **Driver** — 基于开关为 Driver 模式提供逻辑值的输出端口 `1` | `0`

如果 VEXnet Competition Switch 中的开关位置设置为 `Driver`，则输出为 `1`。

当 Auto 输出端口为 0 且 Driver 输出端口为 1 时，机器人处于 Driver 模式。

**数据类型：** `Boolean`

当 Auto 和 Driver 输出均为 0 时，连接到 VEXnet Competition Switch 的机器人处于禁用状态。

## 参数

### **为仿真添加输入端口** — 添加两个输入端口以仿真输入值 `off`（默认） | `on`

选中此复选框可添加两个输入端口 – **Auto** 和 **Driver** – 以仿真 VEXnet Competition Switch 的位置。

### **采样时间** — 用于获取值的采样时间 `0.02`（默认） | 正实数

Competition Switch 模块读取 VEXnet Competition Switch 中开关位置的频率，以秒为单位指定。默认值为 0.02 秒。

当 **采样时间** 参数隐藏时，其值将被继承。

#### 依赖关系

仅当未选择 **为仿真添加输入端口** 时，此参数才可用。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

读取 VEXnet Competition Switch 的开关位置，并为 Autonomous 和 Driver 模式提供逻辑值

Competition Switch 模块读取 VEXnet Competition Switch 的开关位置，并为 Autonomous 模式和 Driver 模式提供相应的逻辑值（1 或 0）。此模块可用于根据开关位置在 Driver 模式和 Autonomous 模式所需的逻辑之间切换。
