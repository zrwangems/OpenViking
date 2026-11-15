---
type: simulink-block
title: 'LED'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'led'
documentation_source_path: 'supportpkg/raspberrypi_ref/led.html'
language: zh-CN
chinese_source: worker-translation
---

# LED

## 端口

### 输入

### **Port\_1** — 输入信号标量

如果模块的输入为非零值，则 **LED** 参数指定的 LED 点亮。如果模块的输入为零，
则 **LED** 参数指定的 LED 熄灭。

例如，如果 **LED** 参数设置为
`led0(Green)`，且模块的输入为
`5`，则硬件上的绿色 LED 开始发光。

**数据类型：** `uint8`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 2 Model B` (默认) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您的 Raspberry Pi 硬件板。您可以在目标硬件、
产品包装或产品文档中找到此信息。

### **LED** — 用户可控 LED `led0(Green)` (默认) | Raspberry Pi 板上的 LED

选择要在 Raspberry Pi 硬件板上点亮或熄灭的 LED。要查看 Raspberry Pi 板上 LED 的位置，请点击 **查看 LED 位置**。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2013a 中引入**

## 描述

点亮 Raspberry Pi 板上的内置 LED

使用 LED 模块点亮 Raspberry Pi® 板上的用户可控 LED。在没有硬件的仿真期间，此模块不执行任何操作。请参阅
模块在仿真中产生零值或不执行任何操作。

**注意**

不要在一个模型中的多个模块内指定同一个 LED。
