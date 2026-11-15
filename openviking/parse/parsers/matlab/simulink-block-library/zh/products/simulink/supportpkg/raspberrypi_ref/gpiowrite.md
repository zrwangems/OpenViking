---
type: simulink-block
title: 'GPIO Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'gpiowrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/gpiowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# GPIO Write

## 端口

### 输入

### **Port\_1** — 设置 GPIO 引脚状态标量

该模块接受一个逻辑值来设置数字引脚的状态。

**数据类型：** `Boolean`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择你的 Raspberry Pi 硬件板。你可以在目标硬件、产品包装或产品文档中找到此信息。

### **GPIO number** — Raspberry Pi 硬件板的 GPIO 引脚 `4` (default) | `17` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

选择 Raspberry Pi 硬件板的 GPIO 引脚以设置其逻辑状态。不要在 Simulink® 模型中的多个模块中使用同一个 GPIO 引脚。有关 Raspberry Pi GPIO 引脚的更多信息，请点击 **View pin map**。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

设置 GPIO 引脚状态

使用 GPIO Write 模块设置 Raspberry Pi® 板数字引脚的逻辑值。

**警告**

以下操作可能会损坏你的目标硬件：

- 超过可施加到 GPIO 引脚的最大电压。
- 将 GPIO 引脚短接到地。
- 将处于高电压的 GPIO 引脚与处于低电压的另一 GPIO 引脚短接。
- 将 GPIO 引脚连接到高于最大电压的电压源。
- 同时将多个 GPIO 引脚驱动为高电平，从而超过最大电流。
