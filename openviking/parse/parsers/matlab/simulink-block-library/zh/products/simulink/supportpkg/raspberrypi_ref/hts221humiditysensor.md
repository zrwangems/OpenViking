---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/hts221humiditysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# HTS221 Humidity Sensor

## 端口

### 输出

### **Humidity** — 相对湿度输出端口标量

从 Humidity sensor 测得的相对湿度，以百分比表示。

**Data Types:** `double`

### **Temperature** — 环境温度输出端口标量

从 Humidity sensor 测得的环境温度，以摄氏度为单位。

**Data Types:** `double`

## 参数

### **Board** — SenseHAT 所连接的 Raspberry Pi 板的型号 `Pi 2 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择 SenseHAT 所连接的 Raspberry Pi 硬件。

### **Sensor output data rate (ODR)** — 传感器测量数据的速率 12.5 Hz（默认） | 1 Hz | 7 Hz

Humidity sensor 测量相对湿度和环境温度的速率。

### **Sample time** — 从 Humidity sensor 读取测量数据的频率 0.1（默认） | scalar

指定此模块从 Humidity sensor 读取测量数据的频率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2007a 中引入**

## 描述

从 Humidity sensor 测量相对湿度和环境温度

使用 Raspberry Pi® SenseHAT 板载的 Humidity sensor (HTS221) 测量相对湿度和环境温度。
