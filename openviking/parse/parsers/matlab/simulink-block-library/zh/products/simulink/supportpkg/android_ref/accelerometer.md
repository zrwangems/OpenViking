---
type: simulink-block
title: 'Accelerometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'accelerometer'
documentation_source_path: 'supportpkg/android_ref/accelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Accelerometer

## 端口

### 输出

### **X** — *X* 轴加速度计数据标量

该模块输出设备的 *X* 轴加速度计数据。

**数据类型：** `single`

### **Y** — *Y* 轴加速度计数据标量

该模块输出设备的 *Y* 轴加速度计数据。

**数据类型：** `single`

### **Z** — *Z* 轴加速度计数据标量

该模块输出设备的 *Z* 轴加速度计数据。

**数据类型：** `single`

## 参数

### **采样时间** — 采样时间间隔 `0.1`（默认） | 非负标量

指定一个离散时间间隔，以秒为单位，在该时间间隔内，模块读取设备的加速度计传感器并输出数据。

**注意**

**采样时间** 的值越小，处理器必须在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

## 描述

测量沿 X、Y 和 Z 轴的线性加速度，单位为 m/s2

使用 Accelerometer 模块测量沿 *X*、*Y* 和 *Z* 轴的线性加速度，单位为 m/s2。

下图显示了相对于典型 Android® 手机的 X、Y 和 Z 方向轴。

下图显示了相对于典型 Android 平板电脑的 X、Y 和 Z 方向轴。

相对于设备的 *X*、*Y* 和 *Z* 方向轴保持不变。例如，如果将设备正面朝上放在桌子上，*Z* 轴测量地球重力的加速度并输出 ≈ 9.81，单位为 m/s2。*X* 和 *Y* 轴垂直于地球重力加速度，二者均输出 ≈ 0.00，单位为 m/s2。

**注意**

在没有连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。
