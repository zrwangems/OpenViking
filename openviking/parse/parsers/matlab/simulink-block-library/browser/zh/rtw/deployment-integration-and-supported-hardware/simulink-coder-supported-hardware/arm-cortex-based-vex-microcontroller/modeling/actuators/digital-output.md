---
type: simulink-block
title: 'Digital Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Actuators'
documentation_page: 'digitaloutput'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/digitaloutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Output

## 端口

### 输入

### **Port\_1** — 设置引脚的逻辑值（1 或 0） `1` | `0`

将输入端口连接到一个生成逻辑值（`1` 或 `0`）的模块。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 仿真期间使用的信号 `1` | `0`

将 Simulink® Support Package for ARM Cortex-based VEX Microcontroller 中 Utilities 库的适当接收器模块连接到输出端口，以查看仿真输出。

在仿真期间，如果输入端口未连接任何模块，此模块将输出零（请参阅 Block Produces Zeros or Does Nothing in Simulation）。

#### 依赖项

仅当您选择 **Add output port for simulation** 参数时，此端口才会出现。

**数据类型：** `Boolean`

## 参数

### **Digital Port (1 to 12)** — 选择 VEX Microcontroller 上的数字引脚（或端口） `1`（默认） | [1 12] 范围内的整数

您可以选择 VEX Microcontroller 上的 12 个数字 IO 引脚之一，将其用作数字输出。

不要将相同的引脚编号分配给模型中的多个模块。

### **Add output port for simulation** — 添加输出端口以仿真逻辑输出 `off`（默认） | `on`

选中此复选框可添加一个输出端口，用于仿真该模块的逻辑输出。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

将一个引脚表示为数字输出并设置逻辑值

Digital Output 模块用于将基于 ARM® Cortex® 的 VEX® Microcontroller 上的 12 个数字 IO 引脚之一表示为数字输出。该模块设置引脚的数字/逻辑值（1 或 0）。有关微控制器的引脚布局信息，请参阅来自 VEX Robotics 的 VEX Cortex Pin-Out 图。
