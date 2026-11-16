---
type: simulink-block
title: 'Gamepad Joystick'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'gamepadjoystick'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadjoystick.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamepad Joystick

## 端口

### 输入

### **Port\_1** — 仿真期间使用的模拟信号，整数，范围 [ –128 127]

连接一个源模块，例如来自 Simulink® Support Package for ARM® Cortex®-based VEX Microcontroller 中 Utilities 库的 Gamepad Simulator 模块。

#### 依赖项

仅当选择 **Add input port for simulation** 参数时，此端口才会出现。

**数据类型:** `double`
### 输出

### **Port\_1** — 与操纵杆沿轴位置对应的模拟信号，整数，范围 [ –128 127]

模块输出根据操纵杆沿指定控制轴的位置在 –128 到 127 之间变化。值 0 表示操纵杆未沿该轴移动。

在仿真期间，没有硬件时，如果没有源模块连接到仿真输入端口，此模块会输出零（请参阅 Block Produces Zeros or Does Nothing in Simulation）。

**数据类型:** `double`

## 参数

### **Joystick Number** — 操纵杆编号 `1`（默认）

此参数为只读。您可以有一对 VEX 游戏手柄来控制连接到 VEX 微控制器的外设。但是，在 VEX Robotics 和 BEST Robotics 竞赛中，每支队伍只允许使用一个游戏手柄。因此，**Joystick Number** 默认设置为 1，且不能更改。

### **Analog Channel (1 to 4)** — 选择 *x-y* 模拟操纵杆的控制轴 1（默认）

选择要在 VEX 游戏手柄上读取的控制轴。右操纵杆的水平轴标记为 1，其垂直轴标记为 2。左操纵杆的水平轴标记为 3，其垂直轴标记为 4。根据您的选择，模块的掩码图标会在 Simulink Editor 中更新。

### **Add input port for simulation** — 添加一个输入端口以仿真操纵杆 `off`（默认） | `on`

选中此复选框可添加一个输入端口，以便在仿真期间指定模拟值。

### **Sample time** — 从操纵杆获取模拟值的采样时间 `0.02`（默认） | 正实数

Gamepad Joystick 模块应以 seconds 为单位从游戏手柄操纵杆读取值的频率。默认值为 0.02 seconds。

如果选中 **Add input port for simulation** 复选框，则 **Sample time** 参数会隐藏，其值将被继承。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成期间，任何连接到 Gamepad Joystick 模块输入端口的仿真模块都会被忽略，并且对生成的代码没有影响。

## 版本历史

**在 R2016a 中引入**

## 描述

表示 VEX 游戏手柄 x - y 模拟操纵杆上的一个控制轴并读取值

Gamepad Joystick 模块用于表示 VEX® 游戏手柄上 *x-y* 模拟操纵杆的一个控制轴。该模块根据操纵杆沿该轴的位置读取相应的模拟值。VEX 游戏手柄上有两个模拟操纵杆，每个操纵杆有两个控制轴（*x-y*）。
