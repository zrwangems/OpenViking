---
type: simulink-block
title: 'Gamepad Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'gamepadbutton'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamepad Button

## 端口

### 输入

### **Port\_1** — 仿真期间使用的数字信号 `1` | `0`

连接源模块，例如来自 Simulink® Support Package for ARM® Cortex®-based VEX Microcontroller 中 Utilities library 的 Gamepad Simulator 模块。

#### 依赖项

仅当选择 **Add input port for simulation** 参数时，此端口才会出现。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 表示按钮状态的逻辑值 `1` 或 `0`

按下按钮时，模块输出为 `1`；否则（按钮处于释放状态时），模块输出为 `0`。

在没有硬件的仿真期间，如果没有任何源模块连接到输入端口，此模块会输出零（请参阅“在仿真中模块产生零或不执行任何操作”）。

**数据类型：** `Boolean`

## 参数

### **Joystick** — 选择操纵杆编号 `1`（默认）

此参数为只读。你可以使用一对 VEX 游戏手柄来控制连接到 VEX 微控制器的外设。但是，在 VEX Robotics 和 BEST Robotics 竞赛中，每个队伍只允许使用一个游戏手柄。因此，**Joystick** 默认设置为 1，且无法更改。

### **Channel (5 to 8)** — 选择通道或按钮组 `5` | `6` | `7` | `8`（默认）

选择 VEX 游戏手柄上的通道或按钮组。VEX 游戏手柄有四个通道 – 5、6、7 和 8 – 共包含 12 个按钮。

### **Button (Down, Up)** — 选择所选通道中的按钮 `Down`（默认） | `Up` | `Right` | `Left`

此参数的选项因你选择的 **Channel** 而异。通道 5 和 6 只有 Up 和 Down 按钮，而通道 7 和 8 有 Up、Down、Right 和 Left 按钮。进行选择之前，请查看 VEX 游戏手柄上按钮的标签。

### **Add input port for simulation** — 添加输入端口以仿真按钮的逻辑值 `off`（默认） | `on`

选中此复选框可添加一个输入端口，以在仿真期间指定按钮的逻辑值。

### **Sample time** — 用于获取按钮逻辑值的采样时间 `0.02`（默认） | 正实数

Gamepad Button 模块应读取按钮逻辑值的频率，以 seconds 为单位。默认值为 0.02 seconds。

#### 依赖项

如果选中 **Add input port for simulation** 复选框，则 **Sample time** 参数会隐藏，且其值会被继承。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成期间，连接到 Gamepad Button 模块输入端口的任何仿真模块都会被忽略，并且对生成的代码没有影响。

## 版本历史

**在 R2016a 中引入**

## 描述

表示 VEX 游戏手柄上的一个按钮并读取逻辑值

Gamepad Button 模块用于表示 VEX® 游戏手柄上的 12 个按钮之一。该模块根据按钮是按下还是释放来读取相应的逻辑值（1 或 0）。
