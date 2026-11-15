---
type: simulink-block
title: 'Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'pressuresensor'
documentation_source_path: 'supportpkg/android_ref/pressuresensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Sensor

## 端口

### 输出

### **Port\_1** — 大气压力数据标量

此模块输出大气压力数据，单位为百帕 (hPa)。

**数据类型：** `single`

## 参数

### **采样时间** — 采样时间间隔 `0.1`（默认）| 非负标量

指定一个离散时间间隔（以秒为单位），模块在该间隔读取设备的压力传感器并输出数据。

**注意**

较小的 **采样时间** 值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量环境空气压力，单位为百帕 (hPa)

使用 Pressure Sensor 模块从 Android® 设备上的压力传感器测量大气压力，单位为百帕 (hPa)。

**注意**

在未连接硬件的仿真期间，此模块不执行任何操作。有关详细信息，请参阅“模块在仿真中产生零值或不执行任何操作”。
