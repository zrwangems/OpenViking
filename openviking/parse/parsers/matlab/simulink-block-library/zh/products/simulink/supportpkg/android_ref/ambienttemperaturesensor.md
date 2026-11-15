---
type: simulink-block
title: 'Ambient Temperature Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'ambienttemperaturesensor'
documentation_source_path: 'supportpkg/android_ref/ambienttemperaturesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ambient Temperature Sensor

## 端口

### 输出

### **Port\_1** — 温度数据标量

该模块输出从设备温度传感器读取的数据。

**数据类型：** `single`

## 参数

### **采样时间** — 采样时间间隔 `0.1`（默认值）| 非负标量

指定一个离散时间间隔，单位为 seconds，该模块按此间隔读取设备温度传感器并输出数据。

**注意**

较小的 **采样时间** 值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量环境温度，单位为 degree Celsius

使用 Ambient Temperature Sensor 模块从 Android® 设备上的温度传感器测量环境温度（单位为 degree Celsius）。

**注意**

在未连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅模块在仿真中产生零值或不执行任何操作。
