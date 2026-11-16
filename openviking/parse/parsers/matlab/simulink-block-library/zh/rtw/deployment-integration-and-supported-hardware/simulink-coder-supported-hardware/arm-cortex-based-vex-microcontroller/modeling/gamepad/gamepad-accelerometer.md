---
type: simulink-block
title: 'Gamepad Accelerometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'gamepadaccelerometer'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadaccelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamepad Accelerometer

## 端口

### 输入

### **Port\_1** — 仿真期间使用的模拟信号，integer，范围为 [–128 127]

连接一个源模块，例如来自 Simulink® Support Package for ARM® Cortex®-based VEX Microcontroller 中 Utilities 库的 Gamepad Simulator 模块。

#### 依赖关系

仅当选择 **Add input port for simulation** 参数时，此端口才会出现。

**数据类型：** `double`
### 输出

### **Port\_1** — 来自加速度计的模拟值，integer，范围为 [ –128 127]

根据所选轴和游戏手柄的方向，模块输出范围为 –128 到 127。

在仿真期间，没有硬件时，如果没有 Source 模块连接到仿真输入端口，此模块会输出零（请参阅 Block Produces Zeros or Does Nothing in Simulation）。

**数据类型：** `double`

## 参数

### **Joystick** — 游戏手柄编号 `1`（默认值）

此参数为只读。你可以有一对 VEX 游戏手柄来控制连接到 VEX 微控制器的外设。但是，在 VEX Robotics 和 BEST Robotics 比赛中，参赛队只允许使用一个游戏手柄。因此，**Joystick** 默认设置为 1，且不能更改。

### **Axis of Rotation (X-axis = 1, Y-axis = 2)** — 选择游戏手柄的旋转轴 `1` | `2`（默认值）

旋转轴决定使用哪个加速度计来生成输出值。为水平 *x* 轴选择 1，为垂直 *y* 轴选择 2。

### **Add input port for simulation** — 添加输入端口以仿真输入加速度 `off`（默认值） | `on`

选中此复选框可添加一个输入端口，用于指定加速度的模拟值。

### **Sample time** — 获取加速度模拟值的采样时间 `0.02`（默认值） | 正实数

Gamepad Accelerometer 模块应从游戏手柄读取值的频率，以秒为单位指定。默认值为 0.02 秒。

如果选中 **Add input port for simulation** 复选框，则 **Sample time** 参数会隐藏，且其值会被继承。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成期间，任何连接到 Gamepad Accelerometer 模块输入端的仿真模块都会被忽略，并且对生成的代码没有影响。

## 版本历史

**在 R2016a 中引入**

## 描述

从 VEX 游戏手柄加速度计读取模拟值

Gamepad Accelerometer 模块用于根据游戏手柄的旋转轴（*x* 或 *y*）从 VEX® 游戏手柄加速度计读取模拟值。

此模块的输出范围为 –128 到 127。VEX 游戏手柄上有两个加速度计，它们的轴相互垂直对齐。沿水平轴 (1) 或垂直轴 (2) 旋转 VEX 游戏手柄会产生 –128 到 127 范围内的输出值。你可以使用此模拟值来控制连接到 VEX 微控制器的外设，例如直流电机。
