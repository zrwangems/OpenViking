---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Actuators'
documentation_page: 'dcmotor'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Motor

## 端口

### 输入

### **Port\_1** — 设置电机速度的输入模拟信号，整数范围为 [ –128 127]

模块输入值的范围可以为 –128 到 127。符号决定电机的旋转方向，幅度决定速度。模块输入值为 `0` 会停止电机。

DC Motor 模块的输入模拟信号可来自模型中其他模块的输出（例如，来自 Gamepad Joystick 模块）。

在无硬件的仿真期间，如果没有模块连接到输入端口，DC Motor 模块会发出零（请参见“模块在仿真中产生零或不执行任何操作”）。如果 DC Motor 的输入值超出 –128 到 127 的范围，在仿真期间会收到错误消息。

**数据类型：** `double`
### 输出

### **Port\_1** — 仿真期间的电机速度，标量

输出是电机的速度，通过将来自输入端口的値乘以 **Gearing Ratio** 参数的值并将乘积四舍五入到最接近的整数来计算。将 Sink 模块（例如 Display 模块或 Scope 模块）连接到输出端口以查看仿真输出。Sink 模块可在 Simulink® Support Package for ARM Cortex-based VEX Microcontroller 的 Utilities 库中找到。

#### 依赖关系

仅当您选择 **Add output port to measure speed during simulation** 参数时，此端口才会出现。

**数据类型：** `double`

## 参数

### **Motor Channel** — 直流电机的电机通道 `1`（默认）| 1 到 10

选择 ARM Cortex-based VEX Microcontroller 上连接到直流电机的电机通道或引脚。

不要在同一模型中将同一通道编号分配给多个 DC Motor 模块。

### **Gearing Ratio** — 仿真期间电机的齿轮比 `1/13.5`（默认）| (`driving gear`) / (`driven gear`)

此参数仅适用于仿真行为。齿轮比值是一个比例因子，用于将模块的输入值（–128 到 127）缩放为近似电机 RPM。请相应调整它，以使仿真的电机速度与实际安装中的电机速度匹配。

### **Add output port to measure speed during simulation** — 为仿真添加输出端口 `off`（默认）| `on`

选中此复选框可添加输出端口，以在仿真期间输出直流电机的速度。

## 所属库

Simulink Coder Support Package for ARM Cortex-based Microcontroller / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在代码生成期间，连接到 DC Motor 模块输出端口的仿真模块会被忽略，并且不会影响生成的代码。

## 版本历史

**在 R2016a 中引入**

## 描述

表示连接的直流电机并设置电机速度

DC Motor 模块表示连接到 ARM® Cortex®-based VEX® Microcontroller 上指定电机通道的直流电机。输入信号设置电机的速度。VEX 微控制器上有 10 个电机通道（或引脚），您可以将其连接到直流电机。有关微控制器引脚布局的信息，请参见 VEX Robotics 的 VEX Cortex Pin-Out 图。
