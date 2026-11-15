---
type: simulink-block
title: 'Humidity Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'humiditysensor'
documentation_source_path: 'supportpkg/android_ref/humiditysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Humidity Sensor

## 端口

### 输出

### **Port\_1** — 相对湿度数据标量

该模块以百分比 (%) 输出相对湿度。

**数据类型：** `single`

## 参数

### **采样时间** — 采样时间间隔 `0.1`（默认）| 非负标量

指定一个离散时间间隔（以 seconds 为单位），模块按此间隔读取设备的湿度传感器并输出数据。

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

以百分比测量相对空气湿度

使用 Humidity Sensor 模块，以百分比形式测量 Android® 设备上湿度传感器测得的相对空气湿度测量值。

**注意**

在未连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅“仿真中模块产生零值或不执行任何操作”。
