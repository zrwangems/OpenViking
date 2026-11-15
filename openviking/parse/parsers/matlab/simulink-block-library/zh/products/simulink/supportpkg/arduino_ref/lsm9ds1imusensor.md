---
type: simulink-block
title: 'LSM9DS1 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'lsm9ds1imusensor'
documentation_source_path: 'supportpkg/arduino_ref/lsm9ds1imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM9DS1 IMU Sensor

## 端口

### 输出

您可以选择活动传感器来测量角速度、加速度、磁场或这些测量的组合。

### **Acceleration (m/s^2)** — 由加速度计向量测量的沿每个轴的加速度

模块输出加速度作为 `n`×3 向量，其中 `n` 是指定为 Samples per frame 的值。每个值表示沿 X、Y 和 Z 轴的加速度测量值，单位为 `g(9.8 m/s^2)`。

#### 依赖关系

仅当选择 **Acceleration** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Angular rate (dps)** — 由陀螺仪向量测量的沿每个轴的角速度

模块输出速度作为 `n`×3 向量，其中 `n` 是指定为 Samples per frame 的值。每个值表示沿 X、Y 和 Z 轴的角速度测量值，单位为 degrees per second (dps)。

#### 依赖关系

仅当选择 **Angular rate** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Magnetic Field (µT)** — 由磁力计向量测量的沿每个轴的磁场强度

模块输出磁场作为 `n`×3 向量，其中 `n` 是指定为 Samples per frame 的值。每个值表示沿 X、Y 和 Z 轴的磁场测量值，单位为 micro Tesla (µT)。

#### 依赖关系

仅当选择 **Magnetic field** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Timestamp** — 读取数据时的时间戳矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（以秒为单位），返回为 `n`×1 矩阵，其中 `n` 是指定为 Samples per frame 的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认） | scalar

指定 Arduino 硬件上的 I2C 模块，以与传感器外设通信。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **I2C addresses** — 用于与传感器通信的外设地址 Accelerometer/Gyroscope: `0x6A` and Magnetometer: `0x1C`（默认） | `0x6B` | `0x1E`

用于与 LSM9DS1 传感器上的加速度计、陀螺仪和磁力计外设通信的外设地址取决于硬件板上 SDA\_M 和 SDA\_AG 引脚的状态。此表提供了与引脚及其状态对应的外设地址。

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SDA\_M (Magnetometer) | 0 | 0x1C |
| 1 | 0x1E |
| SDA\_AG (Accelerometer and Gyroscope) | 0 | 0x6A |
| 1 | 0x6B |

**数据类型：** `uint8`

#### 选择传感器输出

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular rate (dps)** — 设置用于读取角速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Angular Rate** 设置为输出端口之一。

### **Magnetic field (uT)** — 设置用于获取磁场的输出端口 `on`（默认） | `off`

选择此参数可将 **Magnetic Field** 设置为输出端口之一。

### **Timestamp (s)** — 设置用于获取时间戳的输出端口 `off`（默认） | `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

#### 高级传感器设置（可选）

### **Accelerometer Output Data Rate** — 加速度测量速率 `119` Hz（默认） | `10` Hz | `50` Hz | `238` Hz | `476` Hz | `952` Hz

选择您希望加速度计测量加速度的速率。

### **Accelerometer Full Scale Range** — 加速度计灵敏度 +/-`2` g（默认） | +/-`4` g | +/-`8` g | +/-`16` g

选择测量加速度所需的灵敏度。此参数指定传感器可测量的上限和下限。通常，对于所有传感器，低满量程范围可获得更精确的测量。

### **Accelerometer Bandwidth** — 传感器工作的频率范围 `50` Hz（默认） | `105` Hz | `211` Hz | `408` Hz

设置与加速度测量相关的低通滤波器的带宽。

有关更多信息，请参阅 LSM9DS1 Sensor 数据手册。

### **Gyroscope Output Data Rate** — 角速度测量速率 `119` Hz（默认） | `14.9` Hz | `59.5` Hz | `238` Hz | `476` Hz | `952` Hz

选择您希望陀螺仪测量角速度的速率。

### **Gyroscope Full Scale Range** — 陀螺仪灵敏度 `245` dps（默认） | `500` dps | `2000` dps

选择测量角速度所需的灵敏度。此参数指定传感器可测量的上限和下限。通常，对于所有传感器，低满量程范围的传感器可获得更精确的测量。

### **Gyroscope Bandwidth Mode** — 传感器工作的频率范围 `0`（默认） | `1` | `2` | `3`

选择所需带宽模式，以设置与陀螺仪相关的低通滤波器的截止频率。有关截止频率的信息，请参阅此表。

**低通滤波器 2 (LPF2) 后的输出数据速率 (ODR) 和带宽配置设置**

| 带宽模式 | ODR (Hz) | 截止频率 (Hz) |
| --- | --- | --- |
| 0 | 14.9 | NA |
| 1 | 14.9 | NA |
| 2 | 14.9 | NA |
| 3 | 14.9 | NA |
| 0 | 59.5 | 16 |
| 1 | 59.5 | 16 |
| 2 | 59.5 | 16 |
| 3 | 59.5 | 16 |
| 0 | 119 | 14 |
| 1 | 119 | 31 |
| 2 | 119 | 31 |
| 3 | 119 | 31 |
| 0 | 238 | 14 |
| 1 | 238 | 29 |
| 2 | 238 | 63 |
| 3 | 238 | 78 |
| 0 | 476 | 21 |
| 1 | 476 | 28 |
| 2 | 476 | 57 |
| 3 | 476 | 100 |
| 0 | 952 | 33 |
| 1 | 952 | 40 |
| 2 | 952 | 58 |
| 3 | 952 | 100 |

### **Enable High Pass Filter** — 为陀螺仪启用高通滤波器的选项 on（默认） | off

选择此选项可为陀螺仪启用高通滤波器。

### **Gyroscope High Pass Filter Mode** — 陀螺仪高通滤波器的工作模式 `0`（默认） | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9`

选择高通滤波器模式，以设置高通滤波器所需的截止频率。请参考下表选择所需的截止频率。

**陀螺仪高通滤波器截止频率配置 (Hz)**

| HPF Mode | ODR=14.9 Hz | ODR=59.5 Hz | ODR=119 Hz | ODR=238 Hz | ODR=476 Hz | ODR=952 Hz |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 4 | 8 | 15 | 30 | 57 |
| 1 | 0.5 | 2 | 4 | 8 | 15 | 30 |
| 2 | 0.2 | 1 | 2 | 4 | 8 | 15 |
| 3 | 0.1 | 0.5 | 1 | 2 | 4 | 8 |
| 4 | 0.05 | 0.2 | 0.5 | 1 | 2 | 4 |
| 5 | 0.02 | 0.1 | 0.2 | 0.5 | 1 | 2 |
| 6 | 0.01 | 0.05 | 0.1 | 0.2 | 0.5 | 1 |
| 7 | 0.005 | 0.02 | 0.05 | 0.1 | 0.2 | 0.5 |
| 8 | 0.002 | 0.01 | 0.02 | 0.005 | 0.1 | 0.2 |
| 9 | 0.001 | 0.005 | 0.01 | 0.002 | 0.005 | 0.1 |

有关更多信息，请参阅 LSM9DS1 Sensor 数据手册。

### **Magnetometer Output Data Rate** — 磁场测量速率 `40` Hz（默认） | `0.625` Hz | `1.25` Hz | `25` Hz | `5` Hz | `10` Hz | `20` Hz | `80` Hz

选择您希望 Magnetometer 测量磁场的所需速率。

### **Magnetometer Full Scale Range** — Magnetometer 灵敏度 +/-`4` gauss（默认） | +/-`8` gauss | +/-`12` gauss | +/-`16` gauss

选择测量磁场所需的灵敏度。此参数指定传感器可测量的上限和下限。通常，对于所有传感器，低满量程范围可获得更精确的测量。

### **Timestamp** — 设置用于获取时间戳的输出端口 `off`（默认） | `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### **Samples per frame** — 模块输出的样本数 `1`（默认） | positive integer

指定模块输出的样本数。

您在此处指定的值也用于计算输出采样时间：

Output sample time = `Samples per frame * Sample time` \* `Sample time`。

### **Sample time** — 从活动传感器读取数据的时间 `0.1`（默认） | scalar

输入模块从活动传感器读取值的时间间隔（以秒为单位）。输出采样时间是您指定的 `Samples per frame` 和 `Sample time` 的乘积。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

测量沿 X、Y 和 Z 轴的线性加速度、角速度和磁场

LSM9DS1 IMU Sensor 模块使用与 Arduino® 硬件接口的 LSM9DS1 Inertial Measurement Unit (IMU) 传感器，测量沿 X、Y 和 Z 轴的线性加速度、角速度和磁场。此 9-Degree of Freedom (DoF) IMU 传感器包括加速度计、陀螺仪和磁力计，分别用于测量线性加速度、角速度和磁场。

**注意**

如果您使用的是 Arduino Nano 33 BLE Sense 硬件（其始终包含嵌入式传感器），则不支持从包含 LSM9DS1 传感器的分线板读取数据。
