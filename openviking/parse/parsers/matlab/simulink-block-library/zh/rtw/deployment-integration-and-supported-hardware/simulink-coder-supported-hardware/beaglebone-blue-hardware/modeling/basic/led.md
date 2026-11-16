---
type: simulink-block
title: 'LED'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'led'
documentation_source_path: 'beagleboneblue/ref/led.html'
language: zh-CN
chinese_source: worker-translation
---

# LED

## 端口

### 输入

### **Port\_1** — 输入信号标量

如果模块的输入为非零值，则 **LED** 参数指定的 LED 点亮。如果模块的输入为零，则 **LED** 参数指定的 LED 熄灭。

例如，如果 **LED** 参数设置为 `GREEN`，并且模块的输入为 `5`，则硬件上的绿色 LED 开始发光。

**数据类型：** `uint8`

## 参数

### **LED** — 用户可控 LED `RED` (默认) | `GREEN`

选择要点亮或熄灭的 LED。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

点亮内置 LED

LED 模块点亮硬件上的用户可控 LED。

该模块接受 `uint8` 值作为输入。如果模块的输入为非零值，则 **LED** 参数指定的 LED 点亮。如果模块的输入为零，则 **LED** 参数指定的 LED 熄灭。

在无硬件的仿真中，此模块不执行任何操作。请参阅 Block Produces Zeros or Does Nothing in Simulation。

**注意**

不要在一个模型中的多个模块内指定同一个 LED。
