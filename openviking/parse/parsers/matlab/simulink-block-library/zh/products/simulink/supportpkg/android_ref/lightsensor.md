---
type: simulink-block
title: 'Light Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'lightsensor'
documentation_source_path: 'supportpkg/android_ref/lightsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Light Sensor

## 端口

### 输出

### **Port\_1** — 环境光数据标量

该模块输出环境光，单位为 lux (lx)。

**数据类型：** `single`

## 参数

### **Sample time** — 采样时间间隔 `0.1`（默认） | 非负标量

指定一个离散时间间隔（以秒为单位），模块在该时间间隔读取设备的光传感器并输出数据。

**注意**

**Sample time** 的值越小，处理器需要在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量环境光水平，单位为 lux (lx)

使用 Light Sensor 模块从 Android® 设备上的光传感器测量环境光，单位为 lux (lx)。

**注意**

在未连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅“模块在仿真中产生零值或不执行任何操作”。
