---
type: simulink-block
title: 'LPS25h Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'lps25hpressuresensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lps25hpressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LPS25h Pressure Sensor

## 端口

### 输出

### **Pressure** — 气压输出端口（标量）

从 Pressure sensor 测量的气压，以 hectoPascal (hPa) 为单位。

**数据类型：** `double`

### **Temp** — 环境温度输出端口（标量）

从 Pressure sensor 测量的环境温度，以 degree Celsius (C) 为单位。

**数据类型：** `double`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 2 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您的 Raspberry Pi 硬件板。您可以在目标硬件、产品包装或产品文档中找到此信息。

### **Sensor output data rate (ODR)** — 传感器测量数据的速率 12.5 Hz（默认） | 1 Hz | 7 Hz

Pressure sensor 测量气压和环境温度的速率。

### **Sample time** — 从 Pressure sensor 读取测量数据的频率 0.1（默认） | scalar

指定此模块从 Pressure sensor 读取测量数据的频率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

测量气压和环境温度

使用 Raspberry Pi® SenseHAT 板载的 Pressure sensor 测量气压和环境温度。
