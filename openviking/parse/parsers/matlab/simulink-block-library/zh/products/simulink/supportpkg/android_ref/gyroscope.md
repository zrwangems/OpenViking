---
type: simulink-block
title: 'Gyroscope'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'gyroscope'
documentation_source_path: 'supportpkg/android_ref/gyroscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyroscope

## 端口

### 输出

### **X** — *X* 轴陀螺仪数据标量

该模块输出设备的 *X* 轴陀螺仪数据。

**数据类型：** `single`

### **Y** — *Y* 轴陀螺仪数据标量

该模块输出设备的 *Y* 轴陀螺仪数据。

**数据类型：** `single`

### **Z** — *Z* 轴陀螺仪数据标量

该模块输出设备的 *Z* 轴陀螺仪数据。

**数据类型：** `single`

## 参数

### **Sample time** — 采样时间间隔 `0.1`（默认） | 非负标量

指定一个离散时间间隔（以 seconds 为单位），模块按此间隔读取设备的陀螺仪传感器并输出数据。

**注意**

**Sample time** 的值越小，处理器需要在更短时间内完成相同数量的指令，这可能会导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量绕 X、Y 和 Z 轴的旋转速度，单位为 rad/s

使用 Gyroscope 模块测量设备绕 *X*、*Y* 和 *Z* 轴的旋转速度。该数据从设备的陀螺仪传感器获取。

对于设备上的任何正轴，顺时针旋转输出负值，逆时针旋转输出正值。例如，如果将设备正面朝上放在桌面上并顺时针旋转，则该模块对 *Z* 轴输出负值。

下图显示了典型 Android® 手机的 *X*、*Y* 和 *Z* 正轴方向。

下图显示了典型 Android 平板电脑的 *X*、*Y* 和 *Z* 正轴方向。

**注意**

在未连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅模块在仿真中产生零值或不执行任何操作。
