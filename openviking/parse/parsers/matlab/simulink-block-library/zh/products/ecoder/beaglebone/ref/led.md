---
type: simulink-block
title: 'LED'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'led'
documentation_source_path: 'beaglebone/ref/led.html'
language: zh-CN
chinese_source: worker-translation
---

# LED

## 端口

### 输入

### **Port\_1** — 输入信号标量

如果模块的输入为非零值，则 **LED** 参数指定的 LED 会点亮（ON）。如果模块的输入为零，则 **LED** 参数指定的 LED 会熄灭（OFF）。

例如，如果 **LED** 参数设置为 `GREEN`，并且模块的输入为 `5`，则硬件上的绿色 LED 开始发光。

**数据类型：** `Boolean`

## 参数

### **LED** — 用户可控 LED `USR0`（默认） | `USR1``USR2``USR3`

选择要在 BeagleBone 硬件板上打开或关闭的 LED。要查看 BeagleBone 板上 LED 的位置，请点击 **查看 LED 位置**。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

点亮 BeagleBone 板上的内置 LED

使用 LED 模块点亮 BeagleBone® 板上用户可控制的 LED。在没有硬件的仿真期间，此模块不执行任何操作。请参阅“模块在仿真中产生零或不执行任何操作”。

**注意**

不要在模型中的多个模块中指定同一个 LED。
