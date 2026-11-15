---
type: simulink-block
title: 'TMP102 Temperature Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'tmp102temperaturesensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/tmp102temperaturesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# TMP102 Temperature Sensor

## 端口

### 输出

### **Temperature** — 以 degree Celsius 为单位的环境温度标量

该端口输出 TMP102 传感器读取的环境温度，单位为 degree Celsius。

**数据类型：** `double`

## 参数

### 主要

### **I2C module** — I2C 通信模块 `1`（默认）| 标量

指定 Raspberry Pi® 硬件上用于与 TMP102 传感器通信的 I2C 模块。

要在 Raspberry Pi 硬件上启用辅助 I2C 总线，请按照 Enable Secondary I2C Bus of Raspberry Pi Hardware 中提到的步骤操作。

### **I2C address** — I2C 外设地址 `0x48`（默认）| `0x49` | `0x4A` | `0x4B`

指定要从中读取 TMP102 温度数据的 I2C 外设设备地址。

最多可将四个 TMP102 温度传感器连接到 Raspberry Pi 硬件。传感器连接的 I2C 地址取决于传感器 ADD0 引脚的状态。下表提供了 I2C 地址及其对应的 ADD0 引脚连接详细信息。

| Raspberry Pi 引脚连接 | I2C 地址 |
| --- | --- |
| GND | 0x48 |
| VCC | 0x49 |
| SDA | 0x4A |
| SCL | 0x4B |

### **Sample time** — 时间频率 `1`（默认）| 正整数

指定该模块从 TMP102 传感器读取温度值的频率。

### 高级

### **Temperature alert limits (oC)** — 传感器的温度阈值限制 [`16`,`60`]（默认）| 标量

输入最小和最大温度阈值限制，以便当环境温度等于或超过最大阈值时，在 TMP102 传感器的 alert 引脚上生成信号。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

使用 TMP102 温度传感器读取以 degree Celsius 为单位的环境温度

使用 TMP102 Temperature Sensor 模块从 TMP102 传感器读取环境温度值，单位为 degree Celsius。
