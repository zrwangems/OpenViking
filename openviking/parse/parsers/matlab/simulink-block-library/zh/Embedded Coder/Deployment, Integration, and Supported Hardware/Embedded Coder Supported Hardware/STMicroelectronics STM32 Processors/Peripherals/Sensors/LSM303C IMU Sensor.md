---
type: simulink-block
title: 'LSM303C IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lsm303cimusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lsm303cimusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LSM303C IMU Sensor

## 端口

### 输出

### **Acceleration** — 由 LSM303C 传感器测得的线性加速度行向量

由连接至 STM32 Processors 的 LSM303C 传感器测得的线性加速度（以 m/s2 为单位），沿 x-、y- 和 z- 轴，指定为 `n`-by-3 向量，其中 `n` 是每帧样本数的值。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Magnetic Field** — 由 LSM303C 传感器测得的磁场强度行向量

由连接至 STM32 Processors 的 LSM303C 传感器测得的磁场强度（以 µT 为单位），沿 x-、y- 和 z- 轴，指定为 `n`-by-3 向量，其中 `n` 是每帧样本数的值。

#### 依赖关系

仅当选择 **Magnetic Field (µT)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 LSM303C 传感器测得的温度标量

由连接至 STM32 Processors 的 LSM303C 传感器测得的温度（以 ℃ 为单位）。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Acceleration Status** — 加速度值状态 `0` | `1`

沿三个轴的加速度值状态，按 [z,y,x] 顺序指定为行向量，以指示读取的数据是否为新值。`0` 表示读取的数据为新值，`1` 表示读取的数据不是新值。

#### 依赖关系

仅当选择 **Acceleration Status** 参数时，此输出端口才会出现。

**数据类型：** `Boolean`

### **Magnetic Field Status** — 磁场值状态 `0` | `1`

沿三个轴的磁场值状态，按 [z,y,x] 顺序指定为行向量，以指示读取的数据是否为新值。`0` 表示读取的数据为新值，`1` 表示读取的数据不是新值。

#### 依赖关系

仅当选择 **Magnetic Field Status** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Timestamp** — 读取数据时的时间戳矩阵 | (`n`)-by-1

从传感器读取数据时的时间戳（以 seconds 为单位），返回为 `n`-by-1 矩阵，其中 `n` 是每帧样本数的值。

#### 依赖关系

仅当选择 **Timestamp** 参数时，此输出端口才会出现。

**数据类型：** `double`

## 参数

#### 主选项卡

### **I2C module** — I2C 通信模块 `I2C1`（默认） | 标量

指定 STM32 Processors 上用于与传感器外设通信的 I2C 模块。

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on`（默认） | `off`

选择此参数可将 **Magnetic Field** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `on`（默认） | `off`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Acceleration Status** — 设置用于获取加速度状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Acceleration Status** 设置为输出端口之一。

### **Magnetic Field Status** — 设置用于获取磁场状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Magnetic Field Status** 设置为输出端口之一。

### **Timestamp** — 设置用于获取时间戳的输出端口 `off`（默认） | `on`

选择此参数可将 **Timestamp** 设置为输出端口之一。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 LSM303 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 根据模型中的模块上下文确定模块的最佳采样时间。输出采样时间是您指定的 `Sample time` 的乘积。

#### 高级选项卡

### **Accelerometer range** — 用于测量线性加速度的满量程 `±2g`（默认） | `±4g` | `±8g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Accelerometer output data rate** — 加速度计数据采样的速率 `10 Hz`（默认） | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz`

选择加速度计数据采样的输出数据速率，该速率也决定带宽。

### **Magnetometer range** — 用于测量磁场的满量程 `±16 gauss`（默认）

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Magnetometer output data rate** — 磁力计数据采样的速率 `0.625 Hz`（默认） | `1.25 Hz` | `2.5 Hz` | `5 Hz` | `10 Hz` | `20 Hz` | `40 Hz` | `80 Hz`

选择磁力计数据采样的输出数据速率。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

测量来自 LSM303C 传感器的线性加速度、磁场强度和温度

LSM303C IMU Sensor 模块输出由连接至 STM32 Processors 的 LSM303C 传感器测得的沿 x-、y- 和 z- 轴的线性加速度和磁场强度值。该模块还输出由 LSM303C 传感器读取的温度。
