---
type: simulink-block
title: 'LCD Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / LCD'
documentation_page: 'lcdbutton'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/lcdbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# LCD Button

## 端口

### 输入

### **Port\_1** — 用于仿真目的的所选按钮状态 标量

选择 **Add input port for simulation** 参数后，输入端口将可用。

对于仿真行为，请通过源模块从此端口提供按钮的状态。

此端口上的任何非零值表示按钮已按下。此端口上的值 `0` 表示按钮已释放。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Port\_1** — 所选按钮的状态：按下时为 `1`，释放时为 `0` 标量

模块输出 LCD Display Module 上所选的按钮的状态：按下时为 `1`，释放时为 `0`。

**数据类型：** `double`

## 参数

### **UART port** — UART 端口号 `UART1`（默认） | `UART2`

选择 LCD Display Module 所连接到的微控制器上的 UART 端口号。

### **Button** — 要读取逻辑状态的按钮 `Left`（默认） | `Center` | `Right`

选择要读取其逻辑状态（按下或释放）的按钮。

### **Add input port for simulation** — 指定是否要运行普通模式仿真 off（默认） | on

如果要运行普通模式仿真，并由源模块提供输入值，请选择此参数。

### **Sample time** — 指定读取按钮状态的频率 `0.2`（默认）

指定模块读取按钮状态的频率，以 seconds 为单位。

#### 依赖关系

如果选择 **Add input port for simulation** 参数，则 **Sample time** 参数会隐藏，并且该值会被继承（Sample time = -1）。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller/LCD

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

读取 LCD Display Module 上所选的按钮的逻辑状态

LCD Button 模块读取 LCD Display Module 上所选的按钮的逻辑状态。要选择按钮，请使用 **Button** 参数。

按钮按下时，模块输出为 1。按钮释放时，模块输出为 0。

LCD Display Module 上有三个按钮：Left、Center 和 Right。要控制外设（例如连接到 VEX 微控制器的伺服电机），请使用这些按钮的值。

在仿真期间，没有硬件时，如果没有任何源模块连接到仿真输入端口，此模块会输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。要进行仿真，请从 VEX 微控制器库中的 Utilities 库连接一个源模块。

在代码生成期间，连接到 LCD Button 模块输入端的任何仿真模块都会被忽略，并且对生成的代码没有影响。
