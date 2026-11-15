---
type: simulink-block
title: 'LSM9DS1 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'lsm9ds1imusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm9ds1imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM9DS1 IMU Sensor

## 端口

### 输出

### **AngVelocity** — 由陀螺仪向量测得的沿各轴的角速度

角速度，形式为 `[1x3]` 向量。每个值表示沿 X、Y 和 Z 轴测得的角速度，单位为 degrees per second (dps)。

**数据类型：** `double`

### **Accel** — 由加速度计向量测得的沿各轴的加速度

该模块输出加速度，形式为 `[1x3]` 向量。每个值表示沿 X、Y 和 Z 轴测得的加速度，单位为 `g (9.8 m/s2)`。

**数据类型：** `double`

### **MagField** — 由磁力计向量测得的沿各轴的磁场强度

该模块输出磁场，形式为 `[1x3]` 向量。每个值表示沿 X、Y 和 Z 轴测得的磁场，单位为 micro Tesla`(μT)`。

## 参数

### **查看轴信息** — 用于查看 LSM9DS1 IMU Sensor 轴信息的按钮

单击此按钮可查看 LSM9DS1 IMU Sensor 相对于 SenseHAT 的 X、Y 和 Z 轴。

### **板卡** — 连接了 SenseHAT 的 Raspberry Pi 板型号 `Pi 3 Model B+`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi Zero W` | `Pi 4 Model B` | `Pi 5 Model`

选择连接了 SenseHAT 的 Raspberry Pi 硬件。

### **活动传感器** — Raspberry Pi SenseHAT 上的活动传感器 `Accelerometer, Gyroscope and Magnetometer`（默认） | `Accelerometer and Gyroscope` | `Accelerometer and Magnetometer` | `Gyroscope and Magnetometer` | `Accelerometer` | `Gyroscope` | `Magnetometer`

选择活动传感器，以根据需求测量角速度、加速度、磁场或这些测量的组合。

每个活动传感器在“高级设置”下都提供了一组参数，您可以对这些参数进行配置以获得所需行为。

### **加速度计 – 输出数据速率** — 加速度测量速率 119 Hz（默认） | 10 Hz | 50 Hz | 238 Hz | 476 Hz | 952 Hz

选择您希望加速度计测量加速度的速率。

### **加速度计 – 满量程范围** — 加速度计的灵敏度 +/- 2g（默认） | +/- 4g | +/- 8g | +/- 16g

选择测量加速度所需的灵敏度。这是传感器可测量的上限和下限。通常，对于所有传感器，满量程范围较低的传感器可获得更精确的测量结果。

### **加速度计 – 带宽** — 传感器工作的频率范围 50 Hz（默认） | 105 Hz | 211 Hz | 408 Hz

设置与加速度测量相关联的低通滤波器的带宽。更多信息请参阅 LSM9DS1 数据表。

### **陀螺仪 – 输出数据速率** — 角速度测量速率 119 Hz（默认） | 14.9 Hz | 59.5 Hz | 238 Hz | 476 Hz | 952 Hz

选择您希望陀螺仪测量角速度的速率。

### **陀螺仪 – 满量程范围** — 陀螺仪的灵敏度 245 dps（默认） | 500 dps | 2000 dps

选择测量角速度所需的灵敏度。这是传感器可测量的上限和下限。通常，对于所有传感器，满量程范围较低的传感器可获得更精确的测量结果。

### **陀螺仪 – 带宽模式** — 传感器工作的频率范围 0（默认） | 1 | 2 | 3

选择所需的带宽模式，以设置与陀螺仪相关联的低通滤波器的截止频率。有关截止频率的信息，请参阅表格。

更多信息请参阅 LSM9DS1 数据表。

### **陀螺仪 - 启用高通滤波器** — 为陀螺仪操作启用高通滤波器的选项 off（默认） | on

选中此复选框可为陀螺仪操作启用高通滤波器。

### **陀螺仪 – 高通滤波器模式** — 陀螺仪高通滤波器的工作模式 0（默认） | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

选择高通滤波器模式，以设置高通滤波器所需的截止频率。请参阅给出的表格以选择所需的截止频率。

更多信息请参阅 LSM9DS1 数据表。

### **磁力计 – 输出数据速率** — 磁场测量速率 40 Hz（默认） | 0.625 Hz | 1.25 Hz | 2.5 Hz | 5 Hz | 10 Hz | 20 Hz | 80 Hz

选择您希望磁力计测量磁场的速率。

### **磁力计 – 满量程范围** — 磁力计的灵敏度 +/- 4 gauss（默认） | +/- 8 gauss | +/- 12 gauss | +/- 16 gauss

选择测量磁场所需的灵敏度。这是传感器可测量的上限和下限。通常，对于所有传感器，满量程范围较低的传感器可获得更精确的测量结果。

### **采样时间** — 从活动传感器读取数据的频率 0.1（默认） | scalar

指定此模块从活动传感器读取数据的频率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

测量沿 X、Y 和 Z 轴的线性加速度、角速率和磁场

使用 Raspberry Pi® SenseHAT 板载的 9–DoF IMU（Inertial Measurement Unit）传感器测量线性加速度、角速率和磁场。

IMU 传感器（LSM9DS1）包括加速度计、陀螺仪和磁力计。使用此模块，您可以测量连接了 SenseHAT 的 Raspberry Pi 的惯性运动。

选择所需的活动传感器，以测量角速度、加速度、磁场或这些测量的组合。

该模块输出加速度，形式为 double 数据类型的 `[1x3]` 向量值，单位为 ‘g’ (9.8 m/s^2)；输出角速率，形式为 double 数据类型的 `[1x3]` 向量值，单位为 ‘degrees per second’ (dps)；输出磁场，形式为 double 数据类型的 `[1x3]` 向量值，单位为 micro Tesla (µT)。

您可以选择性地应用特定的高级设置，以根据您的需求自定义传感器行为。

SenseHAT 上 IMU 传感器的轴信息如下所示。
