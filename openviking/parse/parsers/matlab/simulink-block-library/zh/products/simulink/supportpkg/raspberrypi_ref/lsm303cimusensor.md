---
type: simulink-block
title: 'LSM303C IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'lsm303cimusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm303cimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM303C IMU Sensor

## 端口

### 输出

### **Acceleration** — LSM303C 传感器测得的线性加速度行向量

由连接到 Raspberry Pi 板的 LSM303C 传感器沿 x、y 和 z 轴测得的线性加速度（单位为 m/s2），指定为行向量 [x,y,z]。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Magnetic Field** — LSM303C 传感器测得的磁场强度行向量

由连接到 Raspberry Pi 板的 LSM303C 传感器沿 x、y 和 z 轴测得的磁场强度（单位为 µT），指定为行向量 [x,y,z]。

#### 依赖关系

仅当选择 **Magnetic Field (µT)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — LSM303C 传感器测得的温度标量

由连接到 Raspberry Pi 板的 LSM303C 传感器测得的温度（单位为 ℃）。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Acceleration Status** — 加速度值的状态 `0` | `1`

沿三个轴的加速度值的状态，指定为按 [z,y,x] 顺序的行向量，用于指示读取的数据是否为新值。`0` 表示读取的数据为新值，`1` 表示读取的数据不是新值。

#### 依赖关系

仅当选择 **Acceleration Status** 参数时，此输出端口才会出现。

**数据类型：** `Boolean`

### **Magnetic Field Status** — 磁场值的状态 `0` | `1`

沿三个轴的磁场值的状态，指定为按 [z,y,x] 顺序的行向量，用于指示读取的数据是否为新值。`0` 表示读取的数据为新值，`1` 表示读取的数据不是新值。

#### 依赖关系

仅当选择 **Magnetic Field Status** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

#### 主选项卡

### **I2C module** — 用于通信的模块 `1` (默认)

指定板上用于 I2C 通信的模块。

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on` (默认) | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on` (默认) | `off`

选择此参数可将 **Magnetic Field** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on` (默认) | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Acceleration Status** — 设置用于获取加速度状态的输出端口 `off` (默认) | `on`

选择此参数可将 **Acceleration Status** 设置为输出端口之一。

### **Magnetic Field Status** — 设置用于获取磁场状态的输出端口 `off` (默认) | `on`

选择此参数可将 **Magnetic Field Status** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1` (默认) | 正整数

指定此模块从 LSM303 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Accelerometer range** — 用于测量线性加速度的满量程 `±2g` (默认) | `±4g` | `±8g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Accelerometer output data rate** — 加速度计数据被采样的速率 `10 Hz` (默认) | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz`

选择加速度计数据被采样的输出数据速率，这也决定了带宽。

### **Magnetometer range** — 用于测量磁场的满量程 `±16 gauss` (默认)

选择用于测量磁场的满量程。

### **Magnetometer output data rate** — 磁力计数据被采样的速率 `0.625 Hz` (默认) | `1.25 Hz` | `2.5 Hz` | `5 Hz` | `10 Hz` | `20 Hz` | `40 Hz` | `80 Hz`

选择磁力计数据被采样的输出数据速率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

测量来自 LSM303C 传感器的线性加速度、磁场强度和温度

LSM303C IMU Sensor 模块输出由连接到 Raspberry Pi® 板的 LSM303C 传感器测得的沿 x、y 和 z 轴的线性加速度和磁场强度值。该模块还输出 LSM303C 传感器读取的温度。
