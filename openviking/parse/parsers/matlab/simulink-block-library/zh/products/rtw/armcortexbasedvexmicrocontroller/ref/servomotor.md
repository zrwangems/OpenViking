---
type: simulink-block
title: 'Servo Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Actuators'
documentation_page: 'servomotor'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/servomotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Servo Motor

## 端口

### 输入

### **Port\_1** — 设置伺服电机角位置的输入信号 整数，范围为 [ –128 127]

Servo Motor 模块的输入信号可以来自模型中的其他模块。例如：

- 如果将 Gamepad Joystick 模块连接为 Servo Motor 模块的输入，则输入值可以根据操纵杆的位置在 –128 到 127 之间变化，然后转换为伺服电机的角度位置值（以 degrees 为单位）。对于模块输入值 ‘0’，伺服电机静止。
- 如果将 Gamepad Button 模块连同 Gain 模块连接为 Servo Motor 模块的输入，则可以在按钮保持按下期间将输入设置为特定值，该值会转换为伺服电机的角度位置值（以 degrees 为单位）。

在没有硬件的仿真期间，如果没有模块连接到输入端口，Servo Motor 模块会输出零（请参阅“模块在仿真中产生零或不执行任何操作”）。如果 Servo Motor 的输入值超出 –128 到 127 的范围，则会在仿真期间收到错误消息。

**数据类型：** `double`
### 输出

### **Port\_1** — 仿真期间的伺服角度 标量

输出是伺服电机的角度，以 degrees 为单位。将 Sink 模块（例如 Display 或 Scope 模块）连接到输出端口，以查看仿真输出。Sink 模块可在 Simulink® Support Package for ARM Cortex-based VEX Microcontroller 的 Utilities 库中找到。

#### 依赖关系

仅当选择 **添加输出端口以测量仿真期间的伺服角度** 参数时，此端口才会出现。

**数据类型：** `double`

## 参数

### **电机通道** — 选择伺服电机的电机通道 1 (默认) | `1` 到 `10`

选择 ARM Cortex-based VEX Microcontroller 上连接到伺服电机的电机通道或引脚。

不要在同一模型中将相同的通道编号分配给多个 Servo Motor 模块。

### **添加输出端口以测量仿真期间的伺服角度** — 为仿真添加输出端口 `off` (默认) | `on`

选中此复选框可添加输出端口，以在仿真期间输出伺服电机的角度。

## 所属库

Simulink Coder Support Package for ARM Cortex-based Microcontroller / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成期间，连接到 Servo Motor 模块输出端口的任何仿真模块都会被忽略，并且对生成的代码没有影响。

## 版本历史

**在 R2016a 中引入**

## 描述

表示连接的伺服电机并设置角度位置值

Servo Motor 模块表示连接到 ARM® Cortex®-based VEX® Microcontroller 上指定电机通道的伺服电机。输入信号设置伺服电机的角度位置值。VEX 微控制器上有 10 个电机通道（或引脚），可连接到伺服电机。有关微控制器的引脚布局信息，请参阅 VEX Robotics 的 VEX Cortex Pin-Out 图。
